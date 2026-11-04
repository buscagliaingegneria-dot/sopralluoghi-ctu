#!/usr/bin/env python3
"""Append a processed-set row to docs/drawing-sets/index.md."""
import argparse
import sys
from datetime import date
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True, help="Original PDF basename (for log only)")
    parser.add_argument("--sheet-count", required=True, type=int)
    parser.add_argument("--bookmarked", required=True, help="Bookmarked PDF filename")
    parser.add_argument("--csv", required=True, help="Index CSV filename")
    parser.add_argument("--date", default=date.today().isoformat())
    parser.add_argument("--sets-dir", default="docs/drawing-sets")
    args = parser.parse_args()

    index_file = Path(args.sets_dir) / "index.md"
    if not index_file.exists():
        sys.exit(f"Index not found: {index_file}. Run init_workspace.py first.")

    row = (
        f"| {args.date} | {args.source} | {args.sheet_count} | "
        f"[{args.bookmarked}](./{args.bookmarked}) | [{args.csv}](./{args.csv}) |"
    )

    content = index_file.read_text()
    if row in content:
        sys.exit(f"Identical row already present in {index_file}.")

    if not content.endswith("\n"):
        content += "\n"
    content += row + "\n"

    index_file.write_text(content)
    print(f"Appended: {args.source} -> {index_file}")


if __name__ == "__main__":
    main()
