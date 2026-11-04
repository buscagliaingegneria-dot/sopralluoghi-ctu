#!/usr/bin/env python3
"""Bootstrap docs/constructability-reviews/<project-slug>/ folder and the review index.

Idempotent: safe to re-run. Creates the top-level index.md only if missing,
and creates the per-project subfolder only if missing.
"""
import argparse
import re
import sys
from pathlib import Path

DEFAULT_INDEX = """# Constructability Reviews

| Date | Project | Phase | GC Engaged | High-Severity | Primary Axes | File |
|------|---------|-------|------------|---------------|--------------|------|
"""


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value[:40]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--project-slug",
        required=True,
        help="Per-project folder name, e.g. 'acme-hq', 'harbor-school'",
    )
    parser.add_argument("--reviews-dir", default="docs/constructability-reviews")
    args = parser.parse_args()

    slug = slugify(args.project_slug)
    if not slug:
        sys.exit("--project-slug must contain at least one [a-z0-9] character.")

    rdir = Path(args.reviews_dir)
    rdir.mkdir(parents=True, exist_ok=True)

    index = rdir / "index.md"
    if index.exists():
        print(f"Index already exists: {index}")
    else:
        index.write_text(DEFAULT_INDEX)
        print(f"Created: {index}")

    project_dir = rdir / slug
    if project_dir.exists():
        print(f"Project folder already exists: {project_dir}")
    else:
        project_dir.mkdir(parents=True, exist_ok=False)
        print(f"Created: {project_dir}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
