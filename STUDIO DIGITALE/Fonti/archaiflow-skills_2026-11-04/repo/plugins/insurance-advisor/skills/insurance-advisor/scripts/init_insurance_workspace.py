#!/usr/bin/env python3
"""Bootstrap docs/insurance/ folder with an insurance-recommendation index."""
import argparse
from pathlib import Path

DEFAULT_INDEX = """# Insurance Recommendations

| Date | Project | Phase | Delivery | OCIP/CCIP/Traditional | Article 11 status | File |
|------|---------|-------|----------|------------------------|-------------------|------|
"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ins-dir", default="docs/insurance")
    args = parser.parse_args()

    idir = Path(args.ins_dir)
    idir.mkdir(parents=True, exist_ok=True)

    index = idir / "index.md"
    if index.exists():
        print(f"Index already exists: {index}")
        return

    index.write_text(DEFAULT_INDEX)
    print(f"Created: {index}")


if __name__ == "__main__":
    main()
