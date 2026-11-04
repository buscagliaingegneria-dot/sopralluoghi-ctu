#!/usr/bin/env python3
"""Bootstrap docs/seismic/ folder with a seismic lookup index."""
import argparse
from pathlib import Path

DEFAULT_INDEX_TEMPLATE = """# Seismic Lookup — Project Log

| Date | Project | Lat | Lon | Risk Cat | Site Class | SDC | SDS | SD1 | CSV | Summary |
|------|---------|-----|-----|----------|------------|-----|-----|-----|-----|---------|
"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seismic-dir", default="docs/seismic")
    parser.add_argument("--template")
    args = parser.parse_args()

    seismic_dir = Path(args.seismic_dir)
    seismic_dir.mkdir(parents=True, exist_ok=True)
    (seismic_dir / ".cache").mkdir(exist_ok=True)

    index_file = seismic_dir / "index.md"
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
