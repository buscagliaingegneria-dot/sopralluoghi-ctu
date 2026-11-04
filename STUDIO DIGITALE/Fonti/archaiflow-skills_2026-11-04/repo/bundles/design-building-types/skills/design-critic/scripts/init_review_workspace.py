#!/usr/bin/env python3
"""Bootstrap docs/reviews/ folder with a review index."""
import argparse
from pathlib import Path

DEFAULT_INDEX = """# Design Reviews

| Date | Topic | Tone | Primary Axes | File |
|------|-------|------|--------------|------|
"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--reviews-dir", default="docs/reviews")
    args = parser.parse_args()

    rdir = Path(args.reviews_dir)
    rdir.mkdir(parents=True, exist_ok=True)

    index = rdir / "index.md"
    if index.exists():
        print(f"Index already exists: {index}")
        return

    index.write_text(DEFAULT_INDEX)
    print(f"Created: {index}")


if __name__ == "__main__":
    main()
