#!/usr/bin/env python3
"""Bootstrap docs/ada/ folder with an ADA tracker index."""
import argparse
from pathlib import Path

DEFAULT_INDEX_TEMPLATE = """# ADA Tracker — Project Log

| Date | Project | Jurisdiction | Standard | Row Count | CSV | Preview |
|------|---------|--------------|----------|-----------|-----|---------|
"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--ada-dir",
        default="docs/ada",
        help="ADA tracker directory (default: docs/ada)",
    )
    parser.add_argument(
        "--template",
        help="Path to index template (overrides default)",
    )
    args = parser.parse_args()

    ada_dir = Path(args.ada_dir)
    ada_dir.mkdir(parents=True, exist_ok=True)
    (ada_dir / ".cache").mkdir(exist_ok=True)

    index_file = ada_dir / "index.md"
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
