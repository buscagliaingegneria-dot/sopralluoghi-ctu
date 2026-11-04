#!/usr/bin/env python3
"""Pair pages between two drawing PDFs by the sheet number in the title block.

Page order is not used. Sets gain and lose sheets between revisions, and the
first time that happens page order stops meaning anything.
"""
import argparse
import json
import re
import sys
from pathlib import Path

try:
    import pymupdf
except ImportError:  # PyMuPDF < 1.24 only exposes `fitz`
    try:
        import fitz as pymupdf
    except ImportError:
        sys.exit(
            "ERROR: PyMuPDF is not installed.\n"
            "Install with:  pip install PyMuPDF"
        )

# A-101, A101, A2.04, S001, M-201, G-000, AD101, EP-1.
SHEET_RE = re.compile(r"^[A-Z]{1,3}[-.]?\d{1,3}(?:\.\d{1,3})?[A-Z]?$")

# Title block corner as a fraction of page width and height. NA sheets carry it
# bottom-right; a full-bottom strip still falls inside this box.
CORNER_X = 0.55
CORNER_Y = 0.50


def loose_key(sheet):
    """Pairing key that ignores separators. A-101, A101 and A.101 collapse."""
    return re.sub(r"[-. ]", "", sheet).upper()


def sheet_number_for(page):
    """Return (sheet, source) or (None, reason)."""
    words = page.get_text("words")
    if not words:
        return None, "no-text"

    rect = page.rect
    cx, cy = rect.width * CORNER_X, rect.height * CORNER_Y

    corner, anywhere = [], []
    for x0, y0, x1, y1, word, *_ in words:
        token = word.strip().upper()
        if not SHEET_RE.match(token):
            continue
        mx, my = (x0 + x1) / 2, (y0 + y1) / 2
        # Distance from the bottom-right corner, so the title block wins over a
        # matching token that happens to sit in a detail callout.
        dist = ((rect.width - mx) ** 2 + (rect.height - my) ** 2) ** 0.5
        (corner if mx >= cx and my >= cy else anywhere).append((dist, token))

    if corner:
        return min(corner)[1], "title-block"
    if anywhere:
        return min(anywhere)[1], "page-body"
    return None, "no-sheet-number"


def read_pages(path, overrides):
    doc = pymupdf.open(path)
    out = []
    for i, page in enumerate(doc, start=1):
        if i in overrides:
            out.append({"page": i, "sheet": overrides[i], "source": "override"})
            continue
        sheet, source = sheet_number_for(page)
        out.append({"page": i, "sheet": sheet, "source": source})
    doc.close()
    return out


def parse_overrides(values):
    out = {}
    for raw in values or []:
        if "=" not in raw:
            sys.exit(f"--override needs PAGE=SHEET, got: {raw}")
        page, sheet = raw.split("=", 1)
        try:
            out[int(page)] = sheet.strip()
        except ValueError:
            sys.exit(f"--override page must be a number, got: {page}")
    return out


def index_by_sheet(pages):
    """sheet -> [page, ...]. A re-issued sheet can appear twice in one file."""
    exact, loose = {}, {}
    for p in pages:
        if not p["sheet"]:
            continue
        exact.setdefault(p["sheet"], []).append(p["page"])
        loose.setdefault(loose_key(p["sheet"]), []).append(p["page"])
    return exact, loose


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--old", required=True, help="Older revision PDF")
    parser.add_argument("--new", required=True, help="Newer revision PDF")
    parser.add_argument("--out", required=True, help="Where to write the pairing JSON")
    parser.add_argument(
        "--override",
        action="append",
        metavar="PAGE=SHEET",
        help="Sheet number for a page whose title block would not read. "
             "Prefix with old: or new: to target one file (default: both)",
    )
    args = parser.parse_args()

    old_ov, new_ov = {}, {}
    for raw in args.override or []:
        if raw.startswith("old:"):
            old_ov.update(parse_overrides([raw[4:]]))
        elif raw.startswith("new:"):
            new_ov.update(parse_overrides([raw[4:]]))
        else:
            both = parse_overrides([raw])
            old_ov.update(both)
            new_ov.update(both)

    old_pages = read_pages(args.old, old_ov)
    new_pages = read_pages(args.new, new_ov)

    old_exact, old_loose = index_by_sheet(old_pages)
    new_exact, new_loose = index_by_sheet(new_pages)

    pairs, loose_pairs = [], []
    matched_old, matched_new = set(), set()

    for sheet, old_hits in old_exact.items():
        if sheet in new_exact:
            for op, np_ in zip(old_hits, new_exact[sheet]):
                pairs.append({"sheet": sheet, "old_page": op, "new_page": np_})
                matched_old.add(op)
                matched_new.add(np_)

    # Second pass on the separator-insensitive key, reported separately so a
    # renumbering never hides inside a clean pair list.
    for sheet, old_hits in old_exact.items():
        key = loose_key(sheet)
        if sheet in new_exact or key not in new_loose:
            continue
        for op, np_ in zip(old_hits, new_loose[key]):
            if op in matched_old or np_ in matched_new:
                continue
            new_sheet = next(p["sheet"] for p in new_pages if p["page"] == np_)
            loose_pairs.append(
                {"sheet": sheet, "new_sheet": new_sheet, "old_page": op, "new_page": np_}
            )
            matched_old.add(op)
            matched_new.add(np_)

    result = {
        "old_file": Path(args.old).name,
        "new_file": Path(args.new).name,
        "pairs": sorted(pairs, key=lambda p: p["sheet"]),
        "pairs_matched_loosely": loose_pairs,
        "removed": [p for p in old_pages if p["sheet"] and p["page"] not in matched_old],
        "added": [p for p in new_pages if p["sheet"] and p["page"] not in matched_new],
        "unreadable_old": [p for p in old_pages if not p["sheet"]],
        "unreadable_new": [p for p in new_pages if not p["sheet"]],
    }

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2), encoding="utf-8")

    print(f"Wrote: {out}")
    print(f"  matched      {len(result['pairs'])}")
    if loose_pairs:
        print(f"  matched loosely {len(loose_pairs)}  (separator differs, check these)")
    print(f"  added        {len(result['added'])}")
    print(f"  removed      {len(result['removed'])}")
    unreadable = len(result["unreadable_old"]) + len(result["unreadable_new"])
    if unreadable:
        print(f"  unreadable   {unreadable}  (read by eye, then re-run with --override)")


if __name__ == "__main__":
    main()
