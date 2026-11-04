#!/usr/bin/env python3
"""Append a constructability-review entry to docs/constructability-reviews/index.md.

Idempotent for the (date, project-slug, phase) tuple: refuses to add a duplicate row.
The review file itself is expected at:
    docs/constructability-reviews/<project-slug>/<YYYY-MM-DD>-<project-slug>-<phase>.md
"""
import argparse
import sys
from datetime import date
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", default=date.today().isoformat())
    parser.add_argument("--project-slug", required=True, help="e.g. 'acme-hq'")
    parser.add_argument(
        "--phase",
        required=True,
        help="SD | DD | CD | IFC (or '50% CD', '95% CD', 'GMP set' as free text)",
    )
    parser.add_argument(
        "--gc-engaged",
        required=True,
        choices=["yes", "no", "CMar"],
        help="Is a GC / CMar / preconstruction partner engaged?",
    )
    parser.add_argument(
        "--primary-axes",
        required=True,
        help="comma-separated axis tags, e.g. 'sequencing,mep-coordination,install-access'",
    )
    parser.add_argument("--severity-high", type=int, default=0)
    parser.add_argument("--reviews-dir", default="docs/constructability-reviews")
    args = parser.parse_args()

    index = Path(args.reviews_dir) / "index.md"
    if not index.exists():
        sys.exit(
            f"Index not found: {index}. Run init_constructability_workspace.py first."
        )

    phase_slug = args.phase.lower().replace(" ", "-").replace("%", "pct")
    filename = f"{args.date}-{args.project_slug}-{phase_slug}.md"
    rel_path = f"./{args.project_slug}/{filename}"
    row = (
        f"| {args.date} | {args.project_slug} | {args.phase} | "
        f"{args.gc_engaged} | {args.severity_high} | "
        f"{args.primary_axes} | [{filename}]({rel_path}) |"
    )

    content = index.read_text()
    duplicate_prefix = (
        f"| {args.date} | {args.project_slug} | {args.phase} |"
    )
    if any(line.startswith(duplicate_prefix) for line in content.splitlines()):
        sys.exit(
            f"Row already exists for {args.date} / {args.project_slug} / {args.phase}."
        )

    if not content.endswith("\n"):
        content += "\n"
    content += row + "\n"
    index.write_text(content)
    print(f"Appended: {args.date}/{args.project_slug}/{args.phase} -> {index}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
