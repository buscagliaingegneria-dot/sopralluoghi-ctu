#!/usr/bin/env python3
"""Bootstrap docs/passive-house/ folder with a Passive House tracker index."""
import argparse
from pathlib import Path

DEFAULT_INDEX_TEMPLATE = """# Passive House Tracker — Project Log

| Date | Project | Cert Path | Phase | Pass | Fail | Pending | CSV | Summary |
|------|---------|-----------|-------|-----:|-----:|--------:|-----|---------|
"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ph-dir", default="docs/passive-house")
    parser.add_argument("--template")
    args = parser.parse_args()

    ph_dir = Path(args.ph_dir)
    ph_dir.mkdir(parents=True, exist_ok=True)
    (ph_dir / ".cache").mkdir(exist_ok=True)

    index_file = ph_dir / "index.md"
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
