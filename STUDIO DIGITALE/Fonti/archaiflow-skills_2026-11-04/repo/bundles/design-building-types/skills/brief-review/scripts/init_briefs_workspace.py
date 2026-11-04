#!/usr/bin/env python3
"""Bootstrap docs/briefs/ folder with a brief review index."""
import argparse
from pathlib import Path

DEFAULT_INDEX = """# Brief Reviews

| Date | Brief Type | Slug | Primary Axes | File |
|------|------------|------|--------------|------|
"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--briefs-dir", default="docs/briefs")
    args = parser.parse_args()

    bdir = Path(args.briefs_dir)
    bdir.mkdir(parents=True, exist_ok=True)

    index = bdir / "index.md"
    if index.exists():
        print(f"Index already exists: {index}")
        return

    index.write_text(DEFAULT_INDEX)
    print(f"Created: {index}")


if __name__ == "__main__":
    main()
