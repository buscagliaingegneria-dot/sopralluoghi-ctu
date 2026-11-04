#!/usr/bin/env python3
"""Append a brief review entry to docs/briefs/index.md."""
import argparse
import sys
from datetime import date
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", default=date.today().isoformat())
    parser.add_argument("--brief-type", required=True, help="rfp | opr | program-brief | design-brief")
    parser.add_argument("--slug", required=True)
    parser.add_argument(
        "--primary-axes",
        required=True,
        help="comma-separated axis tags, e.g. 'objectives,performance,decision-rights'",
    )
    parser.add_argument("--briefs-dir", default="docs/briefs")
    args = parser.parse_args()

    index = Path(args.briefs_dir) / "index.md"
    if not index.exists():
        sys.exit(f"Index not found: {index}. Run init_briefs_workspace.py first.")

    filename = f"{args.date}-{args.slug}-review.md"
    row = (
        f"| {args.date} | {args.brief_type} | {args.slug} | "
        f"{args.primary_axes} | [{filename}](./{filename}) |"
    )

    content = index.read_text()
    if any(
        line.startswith(f"| {args.date} | {args.brief_type} | {args.slug} |")
        for line in content.splitlines()
    ):
        sys.exit(f"Row already exists for {args.date} / {args.brief_type} / {args.slug}.")

    if not content.endswith("\n"):
        content += "\n"
    content += row + "\n"
    index.write_text(content)
    print(f"Appended: {args.date}/{args.brief_type}/{args.slug} -> {index}")


if __name__ == "__main__":
    main()
