#!/usr/bin/env python3
"""Bootstrap docs/rfis/ folder with an RFI log file."""
import argparse
from pathlib import Path

DEFAULT_TEMPLATE = """# RFI Log

| RFI No | Date | Subject | To | Priority | Due | File | Status |
|--------|------|---------|----|----------|-----|------|--------|
"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rfi-dir", default="docs/rfis", help="RFI directory (default: docs/rfis)")
    parser.add_argument("--template", help="Path to log template file (overrides default)")
    args = parser.parse_args()

    rfi_dir = Path(args.rfi_dir)
    rfi_dir.mkdir(parents=True, exist_ok=True)

    log_file = rfi_dir / "RFI-log.md"
    if log_file.exists():
        print(f"Log already exists: {log_file}")
        return

    if args.template and Path(args.template).exists():
        content = Path(args.template).read_text()
    else:
        content = DEFAULT_TEMPLATE

    log_file.write_text(content)
    print(f"Created: {log_file}")


if __name__ == "__main__":
    main()
