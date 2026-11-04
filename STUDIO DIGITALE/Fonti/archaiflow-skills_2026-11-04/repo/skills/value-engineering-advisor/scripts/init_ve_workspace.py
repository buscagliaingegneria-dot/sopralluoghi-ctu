#!/usr/bin/env python3
"""Bootstrap docs/value-engineering/ folder with a VE-review index."""
import argparse
from pathlib import Path

DEFAULT_INDEX = """# Value Engineering Reviews

| Date | Round | Phase | Gap $ | Accepted $ | Alternate $ | Blocked $ | File |
|------|-------|-------|-------|------------|-------------|-----------|------|
"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ve-dir", default="docs/value-engineering")
    args = parser.parse_args()

    vdir = Path(args.ve_dir)
    vdir.mkdir(parents=True, exist_ok=True)

    index = vdir / "index.md"
    if index.exists():
        print(f"Index already exists: {index}")
        return

    index.write_text(DEFAULT_INDEX)
    print(f"Created: {index}")


if __name__ == "__main__":
    main()
