#!/usr/bin/env python3
"""Bootstrap docs/bids/ folder with a bid-review index."""
import argparse
from pathlib import Path

DEFAULT_INDEX = """# Bid Reviews

| Date | Slug | Bid Type | Bidders | Recommended | Primary Axes | File |
|------|------|----------|---------|-------------|--------------|------|
"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bids-dir", default="docs/bids")
    args = parser.parse_args()

    bdir = Path(args.bids_dir)
    bdir.mkdir(parents=True, exist_ok=True)

    index = bdir / "index.md"
    if index.exists():
        print(f"Index already exists: {index}")
        return

    index.write_text(DEFAULT_INDEX)
    print(f"Created: {index}")


if __name__ == "__main__":
    main()
