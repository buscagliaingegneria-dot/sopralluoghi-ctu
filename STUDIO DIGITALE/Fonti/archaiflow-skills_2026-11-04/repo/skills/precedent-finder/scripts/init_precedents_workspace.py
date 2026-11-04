#!/usr/bin/env python3
"""Bootstrap docs/precedents/ folder with a precedent index."""
import argparse
from pathlib import Path

DEFAULT_INDEX = """# Precedents

| Date | Topic | Program | Keywords | Count | File |
|------|-------|---------|----------|-------|------|
"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precedents-dir", default="docs/precedents")
    args = parser.parse_args()

    pdir = Path(args.precedents_dir)
    pdir.mkdir(parents=True, exist_ok=True)

    index = pdir / "index.md"
    if index.exists():
        print(f"Index already exists: {index}")
        return

    index.write_text(DEFAULT_INDEX)
    print(f"Created: {index}")


if __name__ == "__main__":
    main()
