#!/usr/bin/env python3
"""Compute Passive House scorecard pass/fail.

Reads the user's scorecard CSV and the bundled criteria file (PHI fixed
criteria for `phi_*` paths; PHIUS+ 2021 methodology for `phius_2021`).

For each metric, computes:
  - Status: pass | fail | pending | N/A
  - Gap: Actual - Target (positive => over-target = fail for lower_is_better)

Aggregate:
  - all_pass: True/False
  - failures: list of metric names with gap > tolerance
  - pending: list of metric names still missing Actual or Target

Writes JSON at --out. The script never invents target values — for PHIUS+
2021, the Target column must be supplied by the user (from their PHIUS
Source Zero portal export); for PHI paths, target values are parsed from
references/phi_classic_criteria.md.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path


def _resolve_refs_dir(start: Path) -> Path:
    return start.resolve().parent.parent / "references"


def parse_phi_criteria(md: str, path_key: str) -> dict[str, dict]:
    """Parse references/phi_classic_criteria.md.

    Looks for a section header matching "## PHI Classic" / "## PHI Plus" /
    "## PHI Premium" and reads the table under it:

    | Metric | Direction | Target | Units |

    Returns: dict[metric_name] -> {"target": float, "direction": str, "units": str}
    """
    section_label = {
        "phi_classic": "PHI Classic",
        "phi_plus": "PHI Plus",
        "phi_premium": "PHI Premium",
    }.get(path_key)
    if section_label is None:
        return {}

    out: dict[str, dict] = {}
    in_section = False
    header_seen = False

    for raw in md.splitlines():
        line = raw.strip()
        if line.startswith("## "):
            in_section = section_label.lower() in line.lower()
            header_seen = False
            continue
        if not in_section:
            continue
        if not line.startswith("|"):
            continue

        cells = [c.strip() for c in line.strip("|").split("|")]
        # Skip separator rows
        if all(set(c) <= {"-", ":", " "} for c in cells):
            continue
        # Header row sets the "header_seen" flag
        if not header_seen and cells[0].lower() in {"metric"}:
            header_seen = True
            continue
        if not header_seen:
            continue
        if len(cells) < 4:
            continue

        metric, direction, target_raw, units = cells[0], cells[1], cells[2], cells[3]
        # Pull leading numeric out of target cell ("≤ 4.75" -> 4.75)
        m = re.search(r"-?\d+(?:\.\d+)?", target_raw)
        if not m:
            continue
        out[metric] = {
            "target": float(m.group(0)),
            "direction": direction.lower(),
            "units": units,
            "target_raw": target_raw,
        }

    return out


def evaluate(target: float, actual: float, direction: str, tol: float = 1e-9) -> tuple[str, float]:
    gap = actual - target
    if direction.startswith("lower"):
        return ("pass" if gap <= tol else "fail"), gap
    if direction.startswith("higher"):
        return ("pass" if gap >= -tol else "fail"), gap
    return "pending", gap


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scorecard", required=True)
    parser.add_argument(
        "--cert-path",
        required=True,
        choices=["phius_2021", "phi_classic", "phi_plus", "phi_premium"],
    )
    parser.add_argument("--out", required=True)
    parser.add_argument("--criteria", help="Override path to PHI criteria .md")
    args = parser.parse_args()

    sc_path = Path(args.scorecard)
    if not sc_path.exists():
        sys.exit(f"Scorecard CSV not found: {sc_path}")

    criteria: dict[str, dict] = {}
    if args.cert_path.startswith("phi_"):
        crit_path = (
            Path(args.criteria)
            if args.criteria
            else _resolve_refs_dir(Path(__file__)) / "phi_classic_criteria.md"
        )
        if not crit_path.exists():
            sys.exit(f"PHI criteria reference not found: {crit_path}")
        criteria = parse_phi_criteria(crit_path.read_text(), args.cert_path)
        if not criteria:
            sys.exit(
                f"Failed to parse criteria for '{args.cert_path}' from {crit_path}. "
                "Check section header + table format."
            )

    rows_out: list[dict] = []
    failures: list[str] = []
    pending: list[str] = []
    pass_count = 0
    fail_count = 0
    na_count = 0

    with sc_path.open() as fh:
        # Skip leading comment lines (start with '#') so the scorecard template
        # can carry a CSV-comment header documenting PHI vs PHIUS section
        # semantics. csv.DictReader has no native comment handling.
        non_comment_lines = [ln for ln in fh if not ln.lstrip().startswith("#")]
        reader = csv.DictReader(non_comment_lines)
        for row in reader:
            metric = (row.get("Metric") or "").strip()
            direction = (row.get("Direction") or "").strip().lower()
            target_str = (row.get("Target") or "").strip()
            actual_str = (row.get("Actual") or "").strip()
            units = (row.get("Units") or "").strip()
            status_in = (row.get("Status") or "").strip().lower()

            if status_in == "n/a":
                rows_out.append(
                    {**row, "Status": "N/A", "Gap": "", "TargetSource": "user-marked N/A"}
                )
                na_count += 1
                continue

            # For PHI paths, override Target from references if not user-supplied
            target_source = "user-supplied"
            if args.cert_path.startswith("phi_"):
                ref = criteria.get(metric)
                if ref:
                    target_str = str(ref["target"])
                    direction = ref["direction"]
                    units = ref["units"]
                    target_source = "references/phi_classic_criteria.md"
            else:
                # PHIUS+ 2021: user must supply target
                target_source = "user (PHIUS Source Zero portal)"

            if not target_str or not actual_str or not direction:
                pending.append(metric)
                rows_out.append(
                    {
                        **row,
                        "Direction": direction,
                        "Target": target_str,
                        "Actual": actual_str,
                        "Units": units,
                        "Status": "pending",
                        "Gap": "",
                        "TargetSource": target_source,
                    }
                )
                continue

            try:
                target = float(target_str)
                actual = float(actual_str)
            except ValueError:
                pending.append(metric)
                rows_out.append(
                    {
                        **row,
                        "Direction": direction,
                        "Target": target_str,
                        "Actual": actual_str,
                        "Units": units,
                        "Status": "pending (non-numeric)",
                        "Gap": "",
                        "TargetSource": target_source,
                    }
                )
                continue

            status, gap = evaluate(target, actual, direction)
            if status == "pass":
                pass_count += 1
            elif status == "fail":
                fail_count += 1
                failures.append(f"{metric}: {actual} {units} vs target {target} {units} (gap {gap:+.3f})")

            rows_out.append(
                {
                    **row,
                    "Direction": direction,
                    "Target": str(target),
                    "Actual": str(actual),
                    "Units": units,
                    "Status": status,
                    "Gap": f"{gap:+.3f}",
                    "TargetSource": target_source,
                }
            )

    out = {
        "cert_path": args.cert_path,
        "computed_at": datetime.now(timezone.utc).isoformat(),
        "totals": {
            "pass": pass_count,
            "fail": fail_count,
            "pending": len(pending),
            "n_a": na_count,
        },
        "all_pass": fail_count == 0 and len(pending) == 0,
        "failures": failures,
        "pending": pending,
        "rows": rows_out,
    }

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, indent=2))

    print(
        f"Cert path: {args.cert_path}. "
        f"Pass: {pass_count}. Fail: {fail_count}. "
        f"Pending: {len(pending)}. N/A: {na_count}. "
        f"all_pass: {out['all_pass']}. JSON -> {out_path}."
    )


if __name__ == "__main__":
    main()
