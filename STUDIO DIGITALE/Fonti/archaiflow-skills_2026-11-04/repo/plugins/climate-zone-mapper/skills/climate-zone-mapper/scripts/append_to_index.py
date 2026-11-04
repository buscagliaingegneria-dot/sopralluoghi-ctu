#!/usr/bin/env python3
"""Append a row to docs/climate-zone/index.md."""
import argparse
import sys
from datetime import date
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", required=True)
    parser.add_argument("--location", required=True, help="City / metro name")
    parser.add_argument("--county-state", required=True, help='e.g. "Cook, IL"')
    parser.add_argument("--zone", required=True, help="e.g. 4A")
    parser.add_argument("--occupancy", required=True, help="Commercial | Residential")
    parser.add_argument("--csv", required=True)
    parser.add_argument("--summary", required=True)
    parser.add_argument("--date", default=date.today().isoformat())
    parser.add_argument("--cz-dir", default="docs/climate-zone")
    args = parser.parse_args()

    index_file = Path(args.cz_dir) / "index.md"
    if not index_file.exists():
        sys.exit(f"Index not found: {index_file}. Run init_workspace.py first.")

    row = (
        f"| {args.date} | {args.project} | {args.location} | "
        f"{args.county_state} | {args.zone} | {args.occupancy} | "
        f"[{args.csv}](./{args.csv}) | [{args.summary}](./{args.summary}) |"
    )

    content = index_file.read_text()
    if row in content:
        sys.exit(f"Identical row already present in {index_file}.")

    if not content.endswith("\n"):
        content += "\n"
    content += row + "\n"
    index_file.write_text(content)
    print(f"Appended: {args.project} -> {index_file}")


if __name__ == "__main__":
    main()
