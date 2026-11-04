#!/usr/bin/env python3
"""Append a checklist entry to docs/checklists/index.md."""
import argparse
import sys
from datetime import date
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", default=date.today().isoformat())
    parser.add_argument("--phase", required=True, help="SD | DD | CD | IFC")
    parser.add_argument("--discipline", required=True, help="e.g. architectural")
    parser.add_argument("--project-type", required=True, help="residential | commercial | civic | mixed-use | industrial")
    parser.add_argument("--slug", required=True)
    parser.add_argument("--checklists-dir", default="docs/checklists")
    args = parser.parse_args()

    index = Path(args.checklists_dir) / "index.md"
    if not index.exists():
        sys.exit(f"Index not found: {index}. Run init_checklist_workspace.py first.")

    filename = f"{args.slug}.md"
    row = (
        f"| {args.date} | {args.phase} | {args.discipline} | {args.project_type} | "
        f"{args.slug} | [{filename}](./{filename}) |"
    )

    content = index.read_text()
    if any(
        line.startswith(f"| {args.date} | {args.phase} | {args.discipline} | {args.project_type} | {args.slug} |")
        for line in content.splitlines()
    ):
        sys.exit(f"Row already exists for {args.date} / {args.phase} / {args.slug}.")

    if not content.endswith("\n"):
        content += "\n"
    content += row + "\n"
    index.write_text(content)
    print(f"Appended: {args.date}/{args.phase}/{args.slug} -> {index}")


if __name__ == "__main__":
    main()
