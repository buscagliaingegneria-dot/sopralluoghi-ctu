#!/usr/bin/env python3
"""Compute LEED v4.1 BD+C: NC scorecard totals.

Reads the user's scorecard CSV and the bundled point matrix
(`references/leed_v41_bdc_nc_points.md`), then computes:

  - Committed points (Status == "Yes")
  - Optimistic points (Status in {"Yes", "Maybe"})
  - Per-category subtotals
  - Predicted certification level for each total
  - Prerequisite compliance status

Writes a JSON summary at --out. The script never invents thresholds, max
points, or credit IDs — every reference is parsed from the bundled matrix.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path


def _resolve_refs_dir(start: Path) -> Path:
    """Find the skill's references/ folder relative to this script."""
    return start.resolve().parent.parent / "references"


def parse_point_matrix(matrix_md: str) -> tuple[dict, list[tuple[int, int, str]], dict]:
    """Parse references/leed_v41_bdc_nc_points.md.

    Returns (credits, thresholds, category_caps):
      credits          dict[credit_id] -> {"name", "type", "max", "category"}
      thresholds       list of (low, high, level) — high is inclusive
      category_caps    dict[category] -> max int
    """
    credits: dict = {}
    thresholds: list[tuple[int, int, str]] = []
    category_caps: dict = {}

    current_category: str | None = None
    in_thresholds = False
    in_category_totals = False

    for line in matrix_md.splitlines():
        line_strip = line.strip()

        # Detect category header lines like "## Sustainable Sites (SS) — 10 points"
        m = re.match(r"^##\s+(.+?)\s+\(([A-Z]{2})\)\s+—\s+(\d+)\s+points?\s*$", line_strip)
        if m:
            current_category = m.group(2)
            category_caps[current_category] = int(m.group(3))
            in_thresholds = False
            in_category_totals = False
            continue

        # Threshold table marker
        if line_strip.startswith("## Certification thresholds"):
            in_thresholds = True
            continue
        if in_thresholds:
            m = re.match(
                r"^\|\s*(Certified|Silver|Gold|Platinum)\s*\|\s*(\d+)\s*[–\-]\s*(\d+)\s*\|",
                line_strip,
            )
            if m:
                thresholds.append((int(m.group(2)), int(m.group(3)), m.group(1)))
            elif line_strip.startswith("---") or (
                line_strip.startswith("##") and "thresholds" not in line_strip.lower()
            ):
                in_thresholds = False

        # Credit rows: "| LT Cr 4 | Credit | Surrounding Density and Diverse Uses | 5 |"
        m = re.match(
            r"^\|\s*([A-Z]{2})\s+(Pre|Cr)\s+(\d+)\s*\|\s*(P|Credit)\s*\|\s*(.+?)\s*\|\s*([\d—\-]+)\s*\|",
            line_strip,
        )
        if m and current_category:
            cat = m.group(1)
            kind = m.group(2)
            num = m.group(3)
            type_label = m.group(4)
            name = m.group(5).strip()
            max_str = m.group(6).strip()
            credit_id = f"{cat} {kind} {num}"
            max_pts = 0 if max_str in ("—", "-") else int(max_str)
            credits[credit_id] = {
                "name": name,
                "type": "P" if type_label == "P" else "Credit",
                "max": max_pts,
                "category": cat,
            }

    if not credits:
        raise ValueError("Failed to parse any credits from references file.")
    if not thresholds:
        raise ValueError("Failed to parse certification thresholds.")
    if not category_caps:
        raise ValueError("Failed to parse category caps.")

    return credits, thresholds, category_caps


def predict_level(points: int, thresholds: list[tuple[int, int, str]]) -> str:
    # thresholds entries: (low, high, level). Highest band uses "Platinum 80–110".
    for low, high, level in thresholds:
        if low <= points <= high:
            return level
    if points < min(t[0] for t in thresholds):
        return "Not Certified"
    # If above all band highs (e.g. 111 — impossible but safe), return top.
    top = max(thresholds, key=lambda t: t[0])
    return top[2]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scorecard", required=True, help="Scorecard CSV path")
    parser.add_argument("--out", required=True, help="Output JSON path")
    parser.add_argument(
        "--matrix",
        help="Override path to point matrix .md (default: ../references/leed_v41_bdc_nc_points.md)",
    )
    args = parser.parse_args()

    scorecard_path = Path(args.scorecard)
    out_path = Path(args.out)

    if not scorecard_path.exists():
        sys.exit(f"Scorecard CSV not found: {scorecard_path}")

    matrix_path = (
        Path(args.matrix)
        if args.matrix
        else _resolve_refs_dir(Path(__file__)) / "leed_v41_bdc_nc_points.md"
    )
    if not matrix_path.exists():
        sys.exit(f"Point matrix not found: {matrix_path}")

    matrix_md = matrix_path.read_text()
    credits, thresholds, category_caps = parse_point_matrix(matrix_md)

    committed = 0
    optimistic = 0
    by_cat_committed: dict = {c: 0 for c in category_caps}
    by_cat_optimistic: dict = {c: 0 for c in category_caps}
    prereq_failures: list = []
    invalid_rows: list = []

    with scorecard_path.open() as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            credit_id = (row.get("CreditID") or "").strip()
            status = (row.get("Status") or "").strip()
            try:
                pts = int(row.get("Points") or 0)
            except ValueError:
                pts = 0

            ref = credits.get(credit_id)
            if ref is None:
                invalid_rows.append({"row": row, "reason": f"Unknown credit ID '{credit_id}'"})
                continue
            if pts > ref["max"]:
                invalid_rows.append(
                    {
                        "row": row,
                        "reason": f"Points {pts} exceed max {ref['max']} for {credit_id}",
                    }
                )
                pts = ref["max"]

            if ref["type"] == "P":
                if status not in ("Yes", "N/A"):
                    prereq_failures.append(
                        {"credit_id": credit_id, "status": status, "name": ref["name"]}
                    )
                continue

            cat = ref["category"]
            if status == "Yes":
                committed += pts
                optimistic += pts
                by_cat_committed[cat] = by_cat_committed.get(cat, 0) + pts
                by_cat_optimistic[cat] = by_cat_optimistic.get(cat, 0) + pts
            elif status == "Maybe":
                optimistic += pts
                by_cat_optimistic[cat] = by_cat_optimistic.get(cat, 0) + pts

    # Cap each category at its published max
    for cat, cap in category_caps.items():
        if by_cat_committed.get(cat, 0) > cap:
            by_cat_committed[cat] = cap
        if by_cat_optimistic.get(cat, 0) > cap:
            by_cat_optimistic[cat] = cap

    # Recompute totals from capped per-category sums
    committed = sum(by_cat_committed.values())
    optimistic = sum(by_cat_optimistic.values())

    out = {
        "rating_system": "LEED v4.1 BD+C: New Construction",
        "computed_at": __import__("datetime").datetime.utcnow().isoformat() + "Z",
        "totals": {
            "committed_points": committed,
            "optimistic_points": optimistic,
            "max_possible": sum(category_caps.values()),
        },
        "predicted_cert": {
            "committed": predict_level(committed, thresholds),
            "optimistic": predict_level(optimistic, thresholds),
        },
        "by_category": {
            cat: {
                "cap": cap,
                "committed": by_cat_committed.get(cat, 0),
                "optimistic": by_cat_optimistic.get(cat, 0),
            }
            for cat, cap in category_caps.items()
        },
        "prerequisites": {
            "all_met": len(prereq_failures) == 0,
            "failures": prereq_failures,
        },
        "invalid_rows": invalid_rows,
        "thresholds": [{"low": t[0], "high": t[1], "level": t[2]} for t in thresholds],
        "source": str(matrix_path),
    }

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, indent=2))
    print(
        f"Committed: {committed} ({out['predicted_cert']['committed']}). "
        f"Optimistic: {optimistic} ({out['predicted_cert']['optimistic']}). "
        f"Prereq failures: {len(prereq_failures)}. "
        f"Invalid rows: {len(invalid_rows)}."
    )


if __name__ == "__main__":
    main()
