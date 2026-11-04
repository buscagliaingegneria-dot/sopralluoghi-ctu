#!/usr/bin/env python3
"""Append a code-review entry to docs/code-reviews/index.md.

Pure-stdlib, mirrors brief-review/scripts/append_to_index.py.
Required columns: Project, Date, Reviewer, Edition, Occupancy,
Construction Type, Status, Path.
"""
import argparse
import sys
from datetime import date
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", required=True, help="Project name as it appears on the review file")
    parser.add_argument("--date", default=date.today().isoformat())
    parser.add_argument("--reviewer", required=True, help="Reviewer name or initials")
    parser.add_argument(
        "--edition",
        required=True,
        help="Code edition basis, e.g. 'IBC 2021 / CBC 2022' or 'IBC 2021 / NYC BC 2022'",
    )
    parser.add_argument(
        "--occupancy",
        required=True,
        help="IBC use group, e.g. B, A-2, R-2, I-2; mixed as 'B + A-3 (separated)'",
    )
    parser.add_argument(
        "--construction-type",
        required=True,
        help="IBC Table 601 type, e.g. 'II-B', 'I-A', 'V-B sprinklered'",
    )
    parser.add_argument(
        "--status",
        required=True,
        choices=["draft", "issued", "AHJ-review", "resolved"],
        help="Workflow status of the review",
    )
    parser.add_argument("--slug", required=True, help="Review slug, e.g. 'acme-hq-l3'")
    parser.add_argument("--reviews-dir", default="docs/code-reviews")
    args = parser.parse_args()

    index = Path(args.reviews_dir) / "index.md"
    if not index.exists():
        sys.exit(f"Index not found: {index}. Run init_code_review_workspace.py first.")

    filename = f"{args.date}-{args.slug}-egress.md"
    row = (
        f"| {args.project} | {args.date} | {args.reviewer} | {args.edition} | "
        f"{args.occupancy} | {args.construction_type} | {args.status} | "
        f"[{filename}](./{filename}) |"
    )

    content = index.read_text()
    if any(
        line.startswith(f"| {args.project} | {args.date} |")
        and args.slug in line
        for line in content.splitlines()
    ):
        sys.exit(f"Row already exists for {args.project} / {args.date} / {args.slug}.")

    if not content.endswith("\n"):
        content += "\n"
    content += row + "\n"
    index.write_text(content)
    print(f"Appended: {args.project}/{args.date}/{args.slug} -> {index}")


if __name__ == "__main__":
    main()
