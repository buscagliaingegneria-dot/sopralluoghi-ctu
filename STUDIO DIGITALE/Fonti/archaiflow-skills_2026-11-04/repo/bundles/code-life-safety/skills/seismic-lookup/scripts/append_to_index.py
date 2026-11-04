#!/usr/bin/env python3
"""Append a row to docs/seismic/index.md."""
import argparse
import sys
from datetime import date
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", required=True)
    parser.add_argument("--lat", required=True)
    parser.add_argument("--lon", required=True)
    parser.add_argument("--risk-category", required=True)
    parser.add_argument("--site-class", required=True)
    parser.add_argument("--sdc", required=True)
    parser.add_argument("--sds", required=True)
    parser.add_argument("--sd1", required=True)
    parser.add_argument("--csv", required=True)
    parser.add_argument("--summary", required=True)
    parser.add_argument("--date", default=date.today().isoformat())
    parser.add_argument("--seismic-dir", default="docs/seismic")
    args = parser.parse_args()

    index_file = Path(args.seismic_dir) / "index.md"
    if not index_file.exists():
        sys.exit(f"Index not found: {index_file}. Run init_workspace.py first.")

    row = (
        f"| {args.date} | {args.project} | {args.lat} | {args.lon} | "
        f"{args.risk_category} | {args.site_class} | "
        f"{args.sdc} | {args.sds} | {args.sd1} | "
        f"[{args.csv}](./{args.csv}) | [{args.summary}](./{args.summary}) |"
    )

    content = index_file.read_text()
    if row in content:
        sys.exit(f"Identical row already present in {index_file}.")

    if not content.endswith("\n"):
        content += "\n"
    content += row + "\n"
    index_file.write_text(content)
    print(f"Appended: {args.project} -> {index_file}")


if __name__ == "__main__":
    main()
