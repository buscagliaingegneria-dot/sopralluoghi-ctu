#!/usr/bin/env python3
"""Append a comparison row to docs/drawing-diffs/index.md."""
import argparse
import sys
from datetime import date
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--old", required=True, help="Older PDF basename (for log only)")
    parser.add_argument("--new", required=True, help="Newer PDF basename (for log only)")
    parser.add_argument("--sheets-compared", required=True, type=int)
    parser.add_argument("--sheets-changed", required=True, type=int)
    parser.add_argument("--report", required=True, help="Report filename")
    parser.add_argument("--date", default=date.today().isoformat())
    parser.add_argument("--diffs-dir", default="docs/drawing-diffs")
    args = parser.parse_args()

    index_file = Path(args.diffs_dir) / "index.md"
    if not index_file.exists():
        sys.exit(f"Index not found: {index_file}. Run init_workspace.py first.")

    row = (
        f"| {args.date} | {args.old} | {args.new} | {args.sheets_compared} | "
        f"{args.sheets_changed} | [{args.report}](./{args.report}) |"
    )

    content = index_file.read_text(encoding="utf-8")
    if row in content:
        sys.exit(f"Identical row already present in {index_file}.")

    if not content.endswith("\n"):
        content += "\n"
    content += row + "\n"

    index_file.write_text(content, encoding="utf-8")
    print(f"Appended: {args.old} -> {args.new} in {index_file}")


if __name__ == "__main__":
    main()
