#!/usr/bin/env python3
"""Bootstrap docs/schedules/ folder with an index file."""
import argparse
from pathlib import Path

DEFAULT_INDEX_TEMPLATE = """# Schedules — Processed Log

| Date | Source PDF | Type | Row Count | CSV | Preview |
|------|------------|------|-----------|-----|---------|
"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--schedules-dir",
        default="docs/schedules",
        help="Schedules directory (default: docs/schedules)",
    )
    parser.add_argument(
        "--template",
        help="Path to index template (overrides default)",
    )
    args = parser.parse_args()

    sched_dir = Path(args.schedules_dir)
    sched_dir.mkdir(parents=True, exist_ok=True)
    (sched_dir / ".cache").mkdir(exist_ok=True)

    index_file = sched_dir / "index.md"
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
