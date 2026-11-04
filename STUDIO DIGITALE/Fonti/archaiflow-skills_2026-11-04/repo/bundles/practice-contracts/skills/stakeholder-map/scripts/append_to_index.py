#!/usr/bin/env python3
"""Append a stakeholder map entry to docs/stakeholders/index.md."""
import argparse
import sys
from datetime import date
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", default=date.today().isoformat())
    parser.add_argument("--slug", required=True)
    parser.add_argument(
        "--project-type",
        required=True,
        help="commercial | civic | healthcare | education | residential | mixed-use | industrial",
    )
    parser.add_argument(
        "--delivery-method",
        required=True,
        help="dbb | db | cmar | ipd | pdb",
    )
    parser.add_argument(
        "--owner-type",
        required=True,
        help="private | public-municipal | public-state | public-federal | institutional | nonprofit",
    )
    parser.add_argument("--stakeholders-dir", default="docs/stakeholders")
    args = parser.parse_args()

    index = Path(args.stakeholders_dir) / "index.md"
    if not index.exists():
        sys.exit(f"Index not found: {index}. Run init_stakeholders_workspace.py first.")

    filename = f"{args.date}-{args.slug}.md"
    row = (
        f"| {args.date} | {args.slug} | {args.project_type} | "
        f"{args.delivery_method} | {args.owner_type} | "
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
