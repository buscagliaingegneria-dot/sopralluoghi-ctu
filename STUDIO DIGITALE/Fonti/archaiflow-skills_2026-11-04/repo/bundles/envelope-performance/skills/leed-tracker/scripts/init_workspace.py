#!/usr/bin/env python3
"""Bootstrap docs/leed/ folder with a LEED tracker index."""
import argparse
from pathlib import Path

DEFAULT_INDEX_TEMPLATE = """# LEED Tracker — Project Log

| Date | Project | Target | Phase | Committed | Optimistic | Predicted Cert | CSV | Summary |
|------|---------|--------|-------|-----------|------------|----------------|-----|---------|
"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--leed-dir", default="docs/leed")
    parser.add_argument("--template")
    args = parser.parse_args()

    leed_dir = Path(args.leed_dir)
    leed_dir.mkdir(parents=True, exist_ok=True)
    (leed_dir / ".cache").mkdir(exist_ok=True)

    index_file = leed_dir / "index.md"
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
