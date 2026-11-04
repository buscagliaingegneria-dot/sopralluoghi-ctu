#!/usr/bin/env python3
"""Append a comms entry to docs/client-comms/index.md."""
import argparse
import sys
from datetime import date
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", default=date.today().isoformat())
    parser.add_argument("--slug", required=True)
    parser.add_argument(
        "--direction",
        required=True,
        choices=["tech-to-client", "client-to-tech"],
    )
    parser.add_argument("--tone", default="warm", choices=["formal", "warm", "brief"])
    parser.add_argument("--comms-dir", default="docs/client-comms")
    args = parser.parse_args()

    index = Path(args.comms_dir) / "index.md"
    if not index.exists():
        sys.exit(f"Index not found: {index}. Run init_comms_workspace.py first.")

    filename = f"{args.slug}.md"
    row = (
        f"| {args.date} | {args.slug} | {args.direction} | {args.tone} | "
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
