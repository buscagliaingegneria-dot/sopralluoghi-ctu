#!/usr/bin/env python3
"""Bootstrap docs/submittals/ folder with a submittal log."""
import argparse
from pathlib import Path

DEFAULT_INDEX = """# Submittal Log

AIA G712-style submittal log. Action stamps: A = Approved, B = Approved as noted, C = Revise & resubmit, D = Rejected, E = For record only.

| Date | Spec Section | Slug | Rev | Stamp | Primary Axes | File |
|------|--------------|------|-----|-------|--------------|------|
"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--submittals-dir", default="docs/submittals")
    args = parser.parse_args()

    sdir = Path(args.submittals_dir)
    sdir.mkdir(parents=True, exist_ok=True)

    index = sdir / "index.md"
    if index.exists():
        print(f"Index already exists: {index}")
        return

    index.write_text(DEFAULT_INDEX)
    print(f"Created: {index}")


if __name__ == "__main__":
    main()
