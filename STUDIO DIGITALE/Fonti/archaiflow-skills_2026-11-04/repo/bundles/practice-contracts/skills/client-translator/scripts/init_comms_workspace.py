#!/usr/bin/env python3
"""Bootstrap docs/client-comms/ folder with a comms index."""
import argparse
from pathlib import Path

DEFAULT_INDEX = """# Client Communications

| Date | Topic | Direction | Tone | File |
|------|-------|-----------|------|------|
"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--comms-dir", default="docs/client-comms")
    args = parser.parse_args()

    cdir = Path(args.comms_dir)
    cdir.mkdir(parents=True, exist_ok=True)

    index = cdir / "index.md"
    if index.exists():
        print(f"Index already exists: {index}")
        return

    index.write_text(DEFAULT_INDEX)
    print(f"Created: {index}")


if __name__ == "__main__":
    main()
