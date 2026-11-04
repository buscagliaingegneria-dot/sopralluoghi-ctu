#!/usr/bin/env python3
"""Read RFI log and print the next zero-padded RFI number."""
import argparse
import re
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rfi-dir", default="docs/rfis")
    parser.add_argument("--width", type=int, default=3, help="zero-pad width (default: 3)")
    args = parser.parse_args()

    log_file = Path(args.rfi_dir) / "RFI-log.md"
    if not log_file.exists():
        print(str(1).zfill(args.width))
        return

    content = log_file.read_text()
    numbers = []
    for line in content.splitlines():
        # Match table rows starting with | <number> |, skip the header separator (---)
        m = re.match(r"^\|\s*(\d+)\s*\|", line)
        if m:
            numbers.append(int(m.group(1)))

    next_n = max(numbers) + 1 if numbers else 1
    print(str(next_n).zfill(args.width))


if __name__ == "__main__":
    main()
