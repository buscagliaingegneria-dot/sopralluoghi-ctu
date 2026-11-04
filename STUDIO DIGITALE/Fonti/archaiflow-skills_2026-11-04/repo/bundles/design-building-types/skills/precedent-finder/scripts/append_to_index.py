#!/usr/bin/env python3
"""Append a precedent entry to docs/precedents/index.md."""
import argparse
import sys
from datetime import date
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", default=date.today().isoformat())
    parser.add_argument("--slug", required=True)
    parser.add_argument("--program", required=True, help="e.g. museum, housing, mixed-use")
    parser.add_argument("--keywords", required=True, help="comma-separated atmosphere/material keywords")
    parser.add_argument("--count", type=int, default=0, help="number of precedents in the file")
    parser.add_argument("--precedents-dir", default="docs/precedents")
    args = parser.parse_args()

    index = Path(args.precedents_dir) / "index.md"
    if not index.exists():
        sys.exit(f"Index not found: {index}. Run init_precedents_workspace.py first.")

    filename = f"{args.slug}.md"
    row = (
        f"| {args.date} | {args.slug} | {args.program} | {args.keywords} | "
        f"{args.count} | [{filename}](./{filename}) |"
    )

    content = index.read_text()
    if any(
        line.startswith(f"| {args.date} | {args.slug} |")
        for line in content.splitlines()
    ):
        sys.exit(f"Row already exists for {args.date} / {args.slug}.")

    if not content.endswith("\n"):
        content += "\n"
    content += row + "\n"
    index.write_text(content)
    print(f"Appended: {args.date}/{args.slug} -> {index}")


if __name__ == "__main__":
    main()
