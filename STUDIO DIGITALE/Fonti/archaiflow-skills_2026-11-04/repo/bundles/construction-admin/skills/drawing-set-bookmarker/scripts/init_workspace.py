#!/usr/bin/env python3
"""Bootstrap docs/drawing-sets/ folder and verify pikepdf availability."""
import argparse
import importlib.util
import sys
from pathlib import Path

DEFAULT_INDEX_TEMPLATE = """# Drawing Sets — Processed Log

| Date | Source PDF | Sheet Count | Bookmarked PDF | Index CSV |
|------|------------|-------------|----------------|-----------|
"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--sets-dir",
        default="docs/drawing-sets",
        help="Drawing-sets directory (default: docs/drawing-sets)",
    )
    parser.add_argument(
        "--template",
        help="Path to index template (overrides default)",
    )
    parser.add_argument(
        "--skip-deps-check",
        action="store_true",
        help="Skip pikepdf import check",
    )
    args = parser.parse_args()

    sets_dir = Path(args.sets_dir)
    sets_dir.mkdir(parents=True, exist_ok=True)
    (sets_dir / ".cache").mkdir(exist_ok=True)

    index_file = sets_dir / "index.md"
    if not index_file.exists():
        if args.template and Path(args.template).exists():
            content = Path(args.template).read_text()
        else:
            content = DEFAULT_INDEX_TEMPLATE
        index_file.write_text(content)
        print(f"Created: {index_file}")
    else:
        print(f"Index already exists: {index_file}")

    if not args.skip_deps_check:
        if importlib.util.find_spec("pikepdf") is None:
            print(
                "ERROR: pikepdf is not installed. Bookmark application requires it.\n"
                "Install with one of:\n"
                "    pip install pikepdf\n"
                "    pip3 install pikepdf\n"
                "    python3 -m pip install pikepdf",
                file=sys.stderr,
            )
            sys.exit(2)
        print("pikepdf: OK")


if __name__ == "__main__":
    main()
