#!/usr/bin/env python3
"""Append a submittal entry to docs/submittals/index.md."""
import argparse
import sys
from datetime import date
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", default=date.today().isoformat())
    parser.add_argument("--spec-section", required=True, help='CSI section e.g. "08 41 13"')
    parser.add_argument("--slug", required=True)
    parser.add_argument("--revision", required=True, type=int)
    parser.add_argument(
        "--action-stamp",
        required=True,
        choices=["A", "B", "C", "D", "E"],
        help="A=Approved, B=Approved as noted, C=Revise & resubmit, D=Rejected, E=For record only",
    )
    parser.add_argument(
        "--primary-axes",
        required=True,
        help="comma-separated axis tags, e.g. 'conformance,performance,deviations'",
    )
    parser.add_argument("--submittals-dir", default="docs/submittals")
    args = parser.parse_args()

    index = Path(args.submittals_dir) / "index.md"
    if not index.exists():
        sys.exit(f"Index not found: {index}. Run init_submittals_workspace.py first.")

    section_dot = args.spec_section.replace(" ", "-")
    filename = f"{args.date}-{section_dot}-{args.slug}.md"
    row = (
        f"| {args.date} | {args.spec_section} | {args.slug} | Rev {args.revision} | "
        f"{args.action_stamp} | {args.primary_axes} | [{filename}](./{filename}) |"
    )

    content = index.read_text()
    if any(
        line.startswith(f"| {args.date} | {args.spec_section} | {args.slug} | Rev {args.revision} |")
        for line in content.splitlines()
    ):
        sys.exit(
            f"Row already exists for {args.date} / {args.spec_section} / {args.slug} Rev {args.revision}."
        )

    if not content.endswith("\n"):
        content += "\n"
    content += row + "\n"
    index.write_text(content)
    print(f"Appended: {args.date}/{args.spec_section}/{args.slug} Rev {args.revision} -> {index}")


if __name__ == "__main__":
    main()
