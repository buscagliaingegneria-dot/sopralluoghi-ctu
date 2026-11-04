#!/usr/bin/env python3
"""Append a review entry to docs/reviews/index.md."""
import argparse
import sys
from datetime import date
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", default=date.today().isoformat())
    parser.add_argument("--slug", required=True)
    parser.add_argument("--tone", default="mentor", choices=["mentor", "harsh", "encouraging"])
    parser.add_argument("--primary-axes", required=True, help="comma-separated axis names")
    parser.add_argument("--reviews-dir", default="docs/reviews")
    args = parser.parse_args()

    index = Path(args.reviews_dir) / "index.md"
    if not index.exists():
        sys.exit(f"Index not found: {index}. Run init_review_workspace.py first.")

    filename = f"{args.date}-{args.slug}.md"
    row = (
        f"| {args.date} | {args.slug} | {args.tone} | {args.primary_axes} | "
        f"[{filename}](./{filename}) |"
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
