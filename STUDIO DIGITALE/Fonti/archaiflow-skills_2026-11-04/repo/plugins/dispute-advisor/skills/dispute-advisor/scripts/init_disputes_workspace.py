#!/usr/bin/env python3
"""Bootstrap docs/disputes/ folder with a dispute-escalation index."""
import argparse
from pathlib import Path

DEFAULT_INDEX = """# Dispute Escalation Memos

| Date | Project | Dispute | Contract form | Ladder rung | Notice status | Counsel engaged | File |
|------|---------|---------|---------------|-------------|---------------|------------------|------|
"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--disputes-dir", default="docs/disputes")
    args = parser.parse_args()

    ddir = Path(args.disputes_dir)
    ddir.mkdir(parents=True, exist_ok=True)

    index = ddir / "index.md"
    if index.exists():
        print(f"Index already exists: {index}")
        return

    index.write_text(DEFAULT_INDEX)
    print(f"Created: {index}")


if __name__ == "__main__":
    main()
