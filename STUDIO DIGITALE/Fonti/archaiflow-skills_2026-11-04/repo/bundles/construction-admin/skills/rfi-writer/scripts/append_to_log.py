#!/usr/bin/env python3
"""Append an RFI entry to the RFI log table."""
import argparse
import sys
from datetime import date
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--number", required=True, help="RFI number (e.g. 007)")
    parser.add_argument("--subject", required=True)
    parser.add_argument("--to", required=True, help="Recipient (consultant/firm)")
    parser.add_argument("--priority", required=True, choices=["Critical", "Standard", "Low"])
    parser.add_argument("--due", required=True, help="Due date YYYY-MM-DD")
    parser.add_argument("--file", required=True, help="RFI filename (e.g. RFI-007-...md)")
    parser.add_argument("--date", default=date.today().isoformat())
    parser.add_argument("--rfi-dir", default="docs/rfis")
    args = parser.parse_args()

    log_file = Path(args.rfi_dir) / "RFI-log.md"
    if not log_file.exists():
        sys.exit(f"Log not found: {log_file}. Run init_rfi_workspace.py first.")

    row = (
        f"| {args.number} | {args.date} | {args.subject} | {args.to} | "
        f"{args.priority} | {args.due} | [{args.file}](./{args.file}) | Open |"
    )

    content = log_file.read_text()
    if f"| {args.number} |" in content and any(
        line.startswith(f"| {args.number} |") for line in content.splitlines()
    ):
        sys.exit(f"Row for RFI {args.number} already exists.")

    if not content.endswith("\n"):
        content += "\n"
    content += row + "\n"

    log_file.write_text(content)
    print(f"Appended: RFI {args.number} -> {log_file}")


if __name__ == "__main__":
    main()
