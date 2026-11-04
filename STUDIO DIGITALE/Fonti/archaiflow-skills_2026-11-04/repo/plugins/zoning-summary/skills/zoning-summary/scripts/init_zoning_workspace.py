#!/usr/bin/env python3
"""Bootstrap docs/zoning/ folder with a zoning index."""
import argparse
from pathlib import Path

DEFAULT_INDEX = """# Zoning Summaries

| Date | Site | Jurisdiction (City, State/Province) | Zone | Use | File |
|------|------|--------------------------------------|------|-----|------|
"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--zoning-dir", default="docs/zoning")
    args = parser.parse_args()

    zdir = Path(args.zoning_dir)
    zdir.mkdir(parents=True, exist_ok=True)

    index = zdir / "index.md"
    if index.exists():
        print(f"Index already exists: {index}")
        return

    index.write_text(DEFAULT_INDEX)
    print(f"Created: {index}")


if __name__ == "__main__":
    main()
