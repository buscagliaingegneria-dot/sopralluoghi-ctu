#!/usr/bin/env python3
"""Append one row to docs/fees/index.md.

Never use Edit on docs/fees/index.md directly — table alignment breaks.
This script is the only writer.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--date", required=True, help="YYYY-MM-DD")
    p.add_argument("--project", required=True, help="project slug")
    p.add_argument("--type", required=True, help="project type")
    p.add_argument("--sector", required=True, help="sector (federal-civilian / federal-dod / federal-va / state / private)")
    p.add_argument("--cc", required=True, help="construction cost USD")
    p.add_argument("--pct", required=True, help="Method A applied % (e.g., 0.06)")
    p.add_argument("--amount", required=True, help="Method A amount USD")
    p.add_argument("--source", required=True, help="path to source fee md (e.g., <slug>-fee.md)")
    args = p.parse_args()

    index = Path("docs/fees/index.md")
    if not index.exists():
        print(f"ERROR: {index} does not exist. Run scripts/init_workspace.py first.", file=sys.stderr)
        return 2

    pct_display = f"{float(args.pct)*100:.2f}%"
    cc_display = f"${float(args.cc):,.0f}"
    amount_display = f"${float(args.amount):,.0f}"

    row = (
        f"| {args.date} | {args.project} | {args.type} | {args.sector} | "
        f"{cc_display} | {pct_display} | {amount_display} | "
        f"[{args.source}]({args.source}) |\n"
    )

    with index.open("a") as f:
        f.write(row)
    print(f"Appended row to {index}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
