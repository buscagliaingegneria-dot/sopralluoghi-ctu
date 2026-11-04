#!/usr/bin/env python3
"""Bootstrap docs/fees/ workspace for the fee-estimator skill.

Creates `docs/fees/` and an empty index file. Idempotent — re-running does
not overwrite existing files.
"""
from __future__ import annotations

import sys
from pathlib import Path


INDEX_HEADER = """# Fee Estimate Index

This file lists fee estimates produced by the `fee-estimator` skill in this project.

| Date | Project | Type | Sector | CC ($) | A: % of CC | A: Amount | Source |
|------|---------|------|--------|--------|------------|-----------|--------|
"""


def main() -> int:
    docs = Path("docs/fees")
    docs.mkdir(parents=True, exist_ok=True)
    cache = docs / ".cache"
    cache.mkdir(exist_ok=True)
    index = docs / "index.md"
    if not index.exists():
        index.write_text(INDEX_HEADER)
        print(f"Created {index}")
    else:
        print(f"{index} already exists — leaving in place")
    print(f"Workspace ready at {docs}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
