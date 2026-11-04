#!/usr/bin/env python3
"""Append a meeting entry to docs/meetings/index.md."""
import argparse
import sys
from datetime import date
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", default=date.today().isoformat())
    parser.add_argument("--slug", required=True)
    parser.add_argument("--attendees", required=True, help="comma- or slash-separated roles")
    parser.add_argument("--decision-count", type=int, default=0)
    parser.add_argument("--todo-count", type=int, default=0)
    parser.add_argument("--meetings-dir", default="docs/meetings")
    args = parser.parse_args()

    index = Path(args.meetings_dir) / "index.md"
    if not index.exists():
        sys.exit(f"Index not found: {index}. Run init_meetings_workspace.py first.")

    filename = f"{args.date}-{args.slug}.md"
    row = (
        f"| {args.date} | {args.slug} | {args.attendees} | "
        f"{args.decision_count} | {args.todo_count} | "
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
