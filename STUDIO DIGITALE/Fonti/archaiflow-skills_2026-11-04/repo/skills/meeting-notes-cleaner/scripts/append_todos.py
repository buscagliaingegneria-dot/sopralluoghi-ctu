#!/usr/bin/env python3
"""Append a To-do item to docs/todos.md with a back-reference to the source meeting."""
import argparse
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--meeting",
        required=True,
        help="Source meeting slug, e.g. 2026-05-06-design-coordination",
    )
    parser.add_argument("--owner", required=True)
    parser.add_argument("--task", required=True)
    parser.add_argument("--due", required=True, help="YYYY-MM-DD or 'next meeting'")
    parser.add_argument("--todos-file", default="docs/todos.md")
    args = parser.parse_args()

    todos = Path(args.todos_file)
    if not todos.exists():
        sys.exit(f"Todos file not found: {todos}. Run init_meetings_workspace.py first.")

    row = (
        f"| {args.owner} | {args.task} | {args.due} | "
        f"[{args.meeting}](meetings/{args.meeting}.md) | Open |"
    )

    content = todos.read_text()
    fingerprint_prefix = f"| {args.owner} | {args.task} |"
    for line in content.splitlines():
        if line.startswith(fingerprint_prefix) and args.meeting in line:
            sys.exit(f"To-do already exists: {args.owner} / {args.task} from {args.meeting}.")

    if not content.endswith("\n"):
        content += "\n"
    content += row + "\n"
    todos.write_text(content)
    print(f"Appended: {args.owner} / {args.task} -> {todos}")


if __name__ == "__main__":
    main()
