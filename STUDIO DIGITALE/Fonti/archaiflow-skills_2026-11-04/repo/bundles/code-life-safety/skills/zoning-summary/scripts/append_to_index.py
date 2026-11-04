#!/usr/bin/env python3
"""Append a zoning summary entry to docs/zoning/index.md."""
import argparse
import sys
from datetime import date
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", default=date.today().isoformat())
    parser.add_argument("--site-slug", required=True)
    parser.add_argument("--jurisdiction", required=True, help="city + state/province, e.g. 'Portland, OR' or 'Toronto, ON'")
    parser.add_argument("--zone", required=True, help="zone designation, e.g. 'R-5' or 'CR 2.5'")
    parser.add_argument("--use", required=True, help="intended use / program")
    parser.add_argument("--zoning-dir", default="docs/zoning")
    args = parser.parse_args()

    index = Path(args.zoning_dir) / "index.md"
    if not index.exists():
        sys.exit(f"Index not found: {index}. Run init_zoning_workspace.py first.")

    filename = f"{args.site_slug}.md"
    row = (
        f"| {args.date} | {args.site_slug} | {args.jurisdiction} | "
        f"{args.zone} | {args.use} | [{filename}](./{filename}) |"
    )

    content = index.read_text()
    if any(
        line.startswith(f"| {args.date} | {args.site_slug} |")
        for line in content.splitlines()
    ):
        sys.exit(f"Row already exists for {args.date} / {args.site_slug}.")

    if not content.endswith("\n"):
        content += "\n"
    content += row + "\n"
    index.write_text(content)
    print(f"Appended: {args.date}/{args.site_slug} -> {index}")


if __name__ == "__main__":
    main()
