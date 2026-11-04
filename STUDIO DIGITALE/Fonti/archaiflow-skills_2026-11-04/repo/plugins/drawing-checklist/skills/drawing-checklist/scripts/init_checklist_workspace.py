#!/usr/bin/env python3
"""Bootstrap docs/checklists/ folder with a checklist index."""
import argparse
from pathlib import Path

DEFAULT_INDEX = """# Drawing Checklists

| Date | Phase | Discipline | Project Type | Slug | File |
|------|-------|------------|--------------|------|------|
"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checklists-dir", default="docs/checklists")
    args = parser.parse_args()

    cdir = Path(args.checklists_dir)
    cdir.mkdir(parents=True, exist_ok=True)

    index = cdir / "index.md"
    if index.exists():
        print(f"Index already exists: {index}")
        return

    index.write_text(DEFAULT_INDEX)
    print(f"Created: {index}")


if __name__ == "__main__":
    main()
