#!/usr/bin/env python3
"""Bootstrap docs/stakeholders/ folder with a stakeholder map index."""
import argparse
from pathlib import Path

DEFAULT_INDEX = """# Stakeholder Maps

| Date | Slug | Project Type | Delivery Method | Owner Type | File |
|------|------|--------------|-----------------|------------|------|
"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stakeholders-dir", default="docs/stakeholders")
    args = parser.parse_args()

    sdir = Path(args.stakeholders_dir)
    sdir.mkdir(parents=True, exist_ok=True)

    index = sdir / "index.md"
    if index.exists():
        print(f"Index already exists: {index}")
        return

    index.write_text(DEFAULT_INDEX)
    print(f"Created: {index}")


if __name__ == "__main__":
    main()
