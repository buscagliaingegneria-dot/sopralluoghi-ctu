#!/usr/bin/env python3
"""Append a bid-review entry to docs/bids/index.md."""
import argparse
import sys
from datetime import date
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", default=date.today().isoformat())
    parser.add_argument("--slug", required=True)
    parser.add_argument(
        "--bid-type",
        required=True,
        help="gc-base | sub-bid | gmp | db-proposal | alternates-only",
    )
    parser.add_argument("--bidder-count", required=True, type=int)
    parser.add_argument("--recommended", required=True, help="Recommended bidder name")
    parser.add_argument(
        "--primary-axes",
        required=True,
        help="comma-separated axis tags, e.g. 'scope,qualifications,alternates'",
    )
    parser.add_argument("--bids-dir", default="docs/bids")
    args = parser.parse_args()

    index = Path(args.bids_dir) / "index.md"
    if not index.exists():
        sys.exit(f"Index not found: {index}. Run init_bids_workspace.py first.")

    filename = f"{args.date}-{args.slug}.md"
    row = (
        f"| {args.date} | {args.slug} | {args.bid_type} | {args.bidder_count} | "
        f"{args.recommended} | {args.primary_axes} | [{filename}](./{filename}) |"
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
