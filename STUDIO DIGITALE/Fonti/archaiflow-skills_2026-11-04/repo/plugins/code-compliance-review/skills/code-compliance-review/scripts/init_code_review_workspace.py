#!/usr/bin/env python3
"""Bootstrap docs/code-reviews/ folder with a code-review index.

Idempotent: re-running on an existing workspace prints a notice and exits
without touching the existing index. Mirrors the brief-review and
spec-review init scripts.
"""
import argparse
from pathlib import Path

DEFAULT_INDEX = """# Code Reviews (IBC Egress, Accessibility & Life-Safety)

| Project | Date | Reviewer | Edition | Occupancy | Construction Type | Status | Path |
|---------|------|----------|---------|-----------|-------------------|--------|------|
"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--reviews-dir", default="docs/code-reviews")
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
