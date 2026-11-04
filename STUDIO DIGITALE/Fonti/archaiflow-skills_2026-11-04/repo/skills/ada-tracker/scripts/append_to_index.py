#!/usr/bin/env python3
"""Append a row to docs/ada/index.md."""
import argparse
import sys
from datetime import date
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", required=True, help="Project slug")
    parser.add_argument("--jurisdiction", required=True, help="Jurisdiction (e.g. Federal, NYC, CA)")
    parser.add_argument("--row-count", required=True, type=int)
    parser.add_argument("--csv", required=True, help="CSV filename")
    parser.add_argument("--preview", required=True, help="Markdown preview filename")
    parser.add_argument("--standard", default="2010 ADA Standards (DOJ)")
    parser.add_argument("--date", default=date.today().isoformat())
    parser.add_argument("--ada-dir", default="docs/ada")
    args = parser.parse_args()

    index_file = Path(args.ada_dir) / "index.md"
    if not index_file.exists():
        sys.exit(f"Index not found: {index_file}. Run init_workspace.py first.")

    row = (
        f"| {args.date} | {args.project} | {args.jurisdiction} | {args.standard} | "
        f"{args.row_count} | [{args.csv}](./{args.csv}) | [{args.preview}](./{args.preview}) |"
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
