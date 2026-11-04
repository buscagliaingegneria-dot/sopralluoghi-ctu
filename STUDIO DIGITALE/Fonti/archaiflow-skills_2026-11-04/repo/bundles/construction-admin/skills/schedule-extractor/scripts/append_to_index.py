#!/usr/bin/env python3
"""Append a processed-schedule row to docs/schedules/index.md."""
import argparse
import sys
from datetime import date
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True, help="Original PDF basename")
    parser.add_argument(
        "--type",
        required=True,
        choices=["door", "window", "finish", "equipment"],
    )
    parser.add_argument("--row-count", required=True, type=int)
    parser.add_argument("--csv", required=True, help="CSV filename")
    parser.add_argument("--preview", required=True, help="Markdown preview filename")
    parser.add_argument("--date", default=date.today().isoformat())
    parser.add_argument("--schedules-dir", default="docs/schedules")
    args = parser.parse_args()

    index_file = Path(args.schedules_dir) / "index.md"
    if not index_file.exists():
        sys.exit(f"Index not found: {index_file}. Run init_workspace.py first.")

    row = (
        f"| {args.date} | {args.source} | {args.type} | {args.row_count} | "
        f"[{args.csv}](./{args.csv}) | [{args.preview}](./{args.preview}) |"
    )

    content = index_file.read_text()
    if row in content:
        sys.exit(f"Identical row already present in {index_file}.")

    if not content.endswith("\n"):
        content += "\n"
    content += row + "\n"

    index_file.write_text(content)
    print(f"Appended: {args.source} ({args.type}) -> {index_file}")


if __name__ == "__main__":
    main()
