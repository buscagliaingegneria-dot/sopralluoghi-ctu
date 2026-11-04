#!/usr/bin/env python3
"""Bootstrap docs/decarbonization/ folder with a roadmap index."""
import argparse
from pathlib import Path

DEFAULT_INDEX = """# Decarbonization Roadmaps

| Date | Project | Building | Baseline EUI | Target | Jurisdiction | Mandate | Horizon | File |
|------|---------|----------|--------------|--------|--------------|---------|---------|------|
"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--decarb-dir", default="docs/decarbonization")
    args = parser.parse_args()

    ddir = Path(args.decarb_dir)
    ddir.mkdir(parents=True, exist_ok=True)

    index = ddir / "index.md"
    if index.exists():
        print(f"Index already exists: {index}")
        return

    index.write_text(DEFAULT_INDEX)
    print(f"Created: {index}")


if __name__ == "__main__":
    main()
