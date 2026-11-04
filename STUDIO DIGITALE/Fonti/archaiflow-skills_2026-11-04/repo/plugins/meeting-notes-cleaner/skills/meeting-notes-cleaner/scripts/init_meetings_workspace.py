#!/usr/bin/env python3
"""Bootstrap docs/meetings/ folder, the meeting index, and docs/todos.md."""
import argparse
from pathlib import Path

INDEX_TEMPLATE = """# Meetings

| Date | Topic | Attendees | Decisions | To-dos | File |
|------|-------|-----------|-----------|--------|------|
"""

TODOS_TEMPLATE = """# Project To-dos

| Owner | Task | Due | Source | Status |
|-------|------|-----|--------|--------|
"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--meetings-dir", default="docs/meetings")
    parser.add_argument("--todos-file", default="docs/todos.md")
    args = parser.parse_args()

    mdir = Path(args.meetings_dir)
    mdir.mkdir(parents=True, exist_ok=True)

    index = mdir / "index.md"
    if index.exists():
        print(f"Index already exists: {index}")
    else:
        index.write_text(INDEX_TEMPLATE)
        print(f"Created: {index}")

    todos = Path(args.todos_file)
    todos.parent.mkdir(parents=True, exist_ok=True)
    if todos.exists():
        print(f"Todos already exists: {todos}")
    else:
        todos.write_text(TODOS_TEMPLATE)
        print(f"Created: {todos}")


if __name__ == "__main__":
    main()
