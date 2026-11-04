#!/usr/bin/env python3
"""Normalize a raw extracted schedule JSON to a standard CSV per schedule type.

Input JSON shape (produced by Claude during the vision-read step):

    {
      "schedule_type": "door" | "window" | "finish" | "equipment",
      "source_pdf": "<basename>.pdf",
      "pages": [
        {
          "page_index": 142,
          "sheet_number": "A-601",
          "headers": ["Mark", "Type", "W", "H", "HW", "Fire", "Notes"],
          "rows": [
            ["101A", "F1", "3'-0\"", "7'-0\"", "HW-1", "20 min", ""],
            ...
          ],
          "footnotes": ["HW-1: lockset, closer, hinges (3)"],
          "low_confidence_rows": [3, 7]   # optional 0-based row indices
        }
      ]
    }

Output: standard-schema CSV at --out path.

Header mapping is per `references/<type>_schedule_schema.md`. Unknown columns are
preserved at the end of the CSV with their captured names.
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

# Synonym map: lowercase capture -> standard column name.
SYNONYMS = {
    "door": {
        "mark": "Mark", "door no": "Mark", "door number": "Mark",
        "door tag": "Mark", "no.": "Mark", "no": "Mark", "#": "Mark",
        "mark no": "Mark",
        "type": "Type", "door type": "Type", "dr type": "Type",
        "type mark": "Type", "t": "Type",
        "width": "Width", "w": "Width", "door w": "Width",
        "lf width": "Width", "leaf w": "Width", "nom w": "Width",
        "height": "Height", "h": "Height", "door h": "Height",
        "lf height": "Height", "nom h": "Height",
        "thickness": "Thickness", "thk": "Thickness", "door thk": "Thickness",
        "material": "Material", "mat": "Material", "mat'l": "Material",
        "door mat": "Material", "lf material": "Material",
        "frame": "Frame", "frame mat": "Frame", "frame type": "Frame",
        "frm": "Frame", "frame mat'l": "Frame",
        "hardware set": "HardwareSet", "hardware": "HardwareSet",
        "hw": "HardwareSet", "hw set": "HardwareSet",
        "hdw": "HardwareSet", "hw group": "HardwareSet",
        "fire rating": "FireRating", "rating": "FireRating",
        "fire": "FireRating", "fr": "FireRating",
        "lbl": "FireRating", "label": "FireRating",
        "remarks": "Remarks", "notes": "Remarks", "comments": "Remarks",
        "r/m": "Remarks", "rmks": "Remarks",
    },
    "window": {
        "mark": "Mark", "window no": "Mark", "window #": "Mark",
        "win no": "Mark", "tag": "Mark", "no.": "Mark", "no": "Mark",
        "type": "Type", "window type": "Type", "win type": "Type",
        "unit type": "Type", "t": "Type",
        "width": "Width", "w": "Width", "ro w": "Width",
        "unit w": "Width", "nom w": "Width", "width (ro)": "Width",
        "height": "Height", "h": "Height", "ro h": "Height",
        "unit h": "Height", "nom h": "Height",
        "material": "Material", "mat": "Material", "mat'l": "Material",
        "frame mat": "Material", "frame": "Material",
        "glazing": "Glazing", "glass": "Glazing", "glaz": "Glazing",
        "ig": "Glazing", "igu": "Glazing", "lite make-up": "Glazing",
        "operation": "Operation", "op": "Operation",
        "operation type": "Operation", "action": "Operation",
        "function": "Operation",
        "remarks": "Remarks", "notes": "Remarks", "comments": "Remarks",
        "rmks": "Remarks",
    },
    "finish": {
        "room number": "RoomNumber", "room no": "RoomNumber",
        "room #": "RoomNumber", "rm no": "RoomNumber",
        "room": "RoomNumber", "no.": "RoomNumber", "no": "RoomNumber",
        "name": "RoomName", "room name": "RoomName",
        "rm name": "RoomName", "description": "RoomName",
        "floor": "Floor", "flr": "Floor", "floor finish": "Floor",
        "flooring": "Floor",
        "base": "Base", "bs": "Base", "base finish": "Base",
        "north wall": "NorthWall", "n wall": "NorthWall",
        "wall n": "NorthWall", "north": "NorthWall", "n": "NorthWall",
        "east wall": "EastWall", "e wall": "EastWall",
        "wall e": "EastWall", "east": "EastWall", "e": "EastWall",
        "south wall": "SouthWall", "s wall": "SouthWall",
        "wall s": "SouthWall", "south": "SouthWall", "s": "SouthWall",
        "west wall": "WestWall", "w wall": "WestWall",
        "wall w": "WestWall", "west": "WestWall", "w": "WestWall",
        "wall": "_singleWall",
        "ceiling": "Ceiling", "clg": "Ceiling", "ceiling finish": "Ceiling",
        "remarks": "Remarks", "notes": "Remarks", "comments": "Remarks",
        "rmks": "Remarks",
    },
    "equipment": {
        "tag": "Tag", "equip tag": "Tag", "eq tag": "Tag",
        "no.": "Tag", "no": "Tag", "mark": "Tag", "id": "Tag",
        "description": "Description", "desc": "Description",
        "name": "Description", "item": "Description",
        "manufacturer": "Manufacturer", "mfr": "Manufacturer",
        "mfg": "Manufacturer", "make": "Manufacturer",
        "model": "Model", "model no": "Model", "cat no": "Model",
        "power": "Power", "kw": "Power", "watts": "Power",
        "voltage": "Power", "volts": "Power",
        "remarks": "Remarks", "notes": "Remarks", "comments": "Remarks",
        "rmks": "Remarks",
    },
}

STANDARD_COLUMNS = {
    "door": [
        "Mark", "Type", "Width", "Height", "Thickness", "Material",
        "Frame", "HardwareSet", "FireRating", "Remarks",
    ],
    "window": [
        "Mark", "Type", "Width", "Height", "Material", "Glazing",
        "Operation", "Remarks",
    ],
    "finish": [
        "RoomNumber", "RoomName", "Floor", "Base",
        "NorthWall", "EastWall", "SouthWall", "WestWall",
        "Ceiling", "Remarks",
    ],
    "equipment": [
        "Tag", "Description", "Manufacturer", "Model", "Power", "Remarks",
    ],
}

# Always appended after the standard columns:
META_COLUMNS = ["SourceSheet", "SourcePage", "ConfidenceFlag"]


def _map_header(captured: str, schedule_type: str) -> str | None:
    """Return the standard column name for a captured header, or None if unknown."""
    key = captured.strip().lower()
    return SYNONYMS[schedule_type].get(key)


def main():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--raw", required=True, help="Raw JSON path (vision-extracted)")
    parser.add_argument(
        "--type",
        required=True,
        choices=["door", "window", "finish", "equipment"],
        help="Schedule type",
    )
    parser.add_argument("--out", required=True, help="Output CSV path")
    parser.add_argument(
        "--preview",
        help="Optional path to also write a markdown preview (first 20 rows)",
    )
    args = parser.parse_args()

    raw_path = Path(args.raw)
    out_path = Path(args.out)

    if not raw_path.exists():
        sys.exit(f"Raw JSON not found: {raw_path}")

    raw = json.loads(raw_path.read_text())
    if raw.get("schedule_type") and raw["schedule_type"] != args.type:
        print(
            f"WARN: --type={args.type} but raw JSON declares "
            f"schedule_type={raw['schedule_type']!r}",
            file=sys.stderr,
        )

    standard = STANDARD_COLUMNS[args.type]
    extra_cols: list[str] = []
    output_rows: list[dict] = []

    for page in raw.get("pages", []):
        headers = page.get("headers", [])
        sheet = page.get("sheet_number", "")
        page_idx = page.get("page_index", "")
        low_conf = set(page.get("low_confidence_rows", []))

        # Build a per-page mapping captured-index -> standard-or-extra-column
        col_map: list[tuple[str, str]] = []  # (kind, name) where kind in {"std", "extra"}
        for h in headers:
            mapped = _map_header(h, args.type)
            if mapped is None:
                if h not in extra_cols:
                    extra_cols.append(h)
                col_map.append(("extra", h))
            elif mapped == "_singleWall" and args.type == "finish":
                # Special: source schedule has one Wall column;
                # fan out to all four cardinal walls.
                col_map.append(("std_singleWall", "_singleWall"))
            else:
                col_map.append(("std", mapped))

        for r_idx, row in enumerate(page.get("rows", [])):
            out: dict = {col: "" for col in standard}
            for col in extra_cols:
                out.setdefault(col, "")
            single_wall_value = ""
            for c_idx, cell in enumerate(row):
                if c_idx >= len(col_map):
                    break
                kind, name = col_map[c_idx]
                if kind == "std":
                    out[name] = cell
                elif kind == "std_singleWall":
                    single_wall_value = cell
                elif kind == "extra":
                    out[name] = cell
            if args.type == "finish" and single_wall_value:
                for w in ("NorthWall", "EastWall", "SouthWall", "WestWall"):
                    if not out[w]:
                        out[w] = single_wall_value
                if "single-wall-source" not in out["Remarks"]:
                    out["Remarks"] = (
                        f"single-wall-source; {out['Remarks']}".rstrip("; ")
                    )
            out["SourceSheet"] = sheet
            out["SourcePage"] = page_idx
            out["ConfidenceFlag"] = "low" if r_idx in low_conf else ""
            output_rows.append(out)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    final_cols = standard + extra_cols + META_COLUMNS
    with out_path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=final_cols, extrasaction="ignore")
        writer.writeheader()
        for row in output_rows:
            writer.writerow(row)

    if extra_cols:
        print(
            f"NOTE: {len(extra_cols)} unmapped column(s) preserved at end of CSV: "
            f"{', '.join(extra_cols)}",
            file=sys.stderr,
        )

    print(
        f"Wrote {out_path} with {len(output_rows)} rows "
        f"({len(standard)} standard + {len(extra_cols)} extra columns)."
    )

    if args.preview:
        preview_path = Path(args.preview)
        preview_path.parent.mkdir(parents=True, exist_ok=True)
        _write_preview(preview_path, args.type, raw_path.name, final_cols, output_rows[:20])
        print(f"Wrote preview {preview_path} ({min(len(output_rows), 20)} rows).")


def _write_preview(path: Path, schedule_type: str, source: str, cols: list[str], rows: list[dict]):
    lines = [
        f"# {schedule_type.title()} Schedule — Preview",
        "",
        f"Source: `{source}`. First {len(rows)} rows.",
        "",
        "| " + " | ".join(cols) + " |",
        "|" + "|".join(["---"] * len(cols)) + "|",
    ]
    for row in rows:
        lines.append(
            "| " + " | ".join(str(row.get(c, "")).replace("|", "\\|") for c in cols) + " |"
        )
    path.write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
