#!/usr/bin/env python3
"""Bootstrap docs/climate-zone/ folder with a climate zone tracker index."""
import argparse
from pathlib import Path

DEFAULT_INDEX_TEMPLATE = """# Climate Zone Mapper — Project Log

| Date | Project | Location | County, State | Zone | Occupancy | CSV | Summary |
|------|---------|----------|---------------|------|-----------|-----|---------|
"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cz-dir", default="docs/climate-zone")
    parser.add_argument("--template")
    args = parser.parse_args()

    cz_dir = Path(args.cz_dir)
    cz_dir.mkdir(parents=True, exist_ok=True)
    (cz_dir / ".cache").mkdir(exist_ok=True)

    index_file = cz_dir / "index.md"
    if not index_file.exists():
        if args.template and Path(args.template).exists():
            content = Path(args.template).read_text()
        else:
            content = DEFAULT_INDEX_TEMPLATE
        index_file.write_text(content)
        print(f"Created: {index_file}")
    else:
        print(f"Index already exists: {index_file}")


if __name__ == "__main__":
    main()
