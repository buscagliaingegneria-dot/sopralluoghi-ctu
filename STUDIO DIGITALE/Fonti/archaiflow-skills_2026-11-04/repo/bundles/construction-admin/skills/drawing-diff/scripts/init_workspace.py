#!/usr/bin/env python3
"""Bootstrap docs/drawing-diffs/ folder and verify PyMuPDF availability."""
import argparse
import importlib.util
import sys
from pathlib import Path

DEFAULT_INDEX_TEMPLATE = """# Drawing Diffs — Comparison Log

| Date | Old | New | Sheets Compared | Sheets Changed | Report |
|------|-----|-----|-----------------|----------------|--------|
"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--diffs-dir",
        default="docs/drawing-diffs",
        help="Drawing-diffs directory (default: docs/drawing-diffs)",
    )
    parser.add_argument(
        "--template",
        help="Path to index template (overrides default)",
    )
    parser.add_argument(
        "--skip-deps-check",
        action="store_true",
        help="Skip PyMuPDF import check",
    )
    args = parser.parse_args()

    diffs_dir = Path(args.diffs_dir)
    diffs_dir.mkdir(parents=True, exist_ok=True)
    (diffs_dir / ".cache").mkdir(exist_ok=True)

    index_file = diffs_dir / "index.md"
    if not index_file.exists():
        if args.template and Path(args.template).exists():
            content = Path(args.template).read_text(encoding="utf-8")
        else:
            content = DEFAULT_INDEX_TEMPLATE
        index_file.write_text(content, encoding="utf-8")
        print(f"Created: {index_file}")
    else:
        print(f"Index already exists: {index_file}")

    if not args.skip_deps_check:
        # PyMuPDF imports as `pymupdf` from 1.24 and as `fitz` before that.
        if (
            importlib.util.find_spec("pymupdf") is None
            and importlib.util.find_spec("fitz") is None
        ):
            print(
                "ERROR: PyMuPDF is not installed. Both diff engines require it.\n"
                "Install with one of:\n"
                "    pip install PyMuPDF\n"
                "    pip3 install PyMuPDF\n"
                "    python3 -m pip install PyMuPDF",
                file=sys.stderr,
            )
            sys.exit(2)
        print("PyMuPDF: OK")


if __name__ == "__main__":
    main()
