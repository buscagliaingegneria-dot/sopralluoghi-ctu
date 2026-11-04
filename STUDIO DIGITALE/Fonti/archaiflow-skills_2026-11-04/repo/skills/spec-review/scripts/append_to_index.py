#!/usr/bin/env python3
"""Append a spec-review entry to docs/spec-reviews/index.md."""
import argparse
import sys
from datetime import date
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", default=date.today().isoformat())
    parser.add_argument("--slug", required=True)
    parser.add_argument(
        "--spec-phase",
        required=True,
        help="e.g. 'DD outline', '50% CD', '95% CD', 'Issue-for-permit'",
    )
    parser.add_argument(
        "--primary-axes",
        required=True,
        help="comma-separated axis tags, e.g. 'drawing-coordination,reference-standards,opr-alignment'",
    )
    parser.add_argument("--findings-high", type=int, default=0)
    parser.add_argument("--reviews-dir", default="docs/spec-reviews")
    args = parser.parse_args()

    index = Path(args.reviews_dir) / "index.md"
    if not index.exists():
        sys.exit(f"Index not found: {index}. Run init_spec_review_workspace.py first.")

    filename = f"{args.date}-{args.slug}.md"
    row = (
        f"| {args.date} | {args.slug} | {args.spec_phase} | {args.findings_high} | "
        f"{args.primary_axes} | [{filename}](./{filename}) |"
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
