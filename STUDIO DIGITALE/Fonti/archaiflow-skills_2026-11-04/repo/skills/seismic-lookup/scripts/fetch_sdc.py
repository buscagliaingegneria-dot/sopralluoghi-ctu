#!/usr/bin/env python3
"""Fetch ASCE 7-22 seismic design parameters from the USGS Seismic Design Maps API.

Calls https://earthquake.usgs.gov/ws/designmaps/asce7-22.json with the
project's lat/lon, Risk Category, and Site Class. Parses the JSON
response into a per-parameter CSV + JSON cache.

Never invents seismic values. If the API is unreachable, the script
exits 1 — the workflow does NOT fall back to training-data estimates.

Site Class compatibility note (ASCE 7-22 vs USGS endpoint):
  ASCE 7-22 §20.3 / Table 20.3-1 defines NINE site classes:
      A, B, BC, C, CD, D, DE, E, F
  where BC, CD, DE are intermediate classes (added in ASCE 7-22 alongside
  the multi-period site coefficient framework).

  The USGS Seismic Design Maps web service for the asce7-22 reference
  document, however, currently accepts only the LEGACY 6-class set
  (A, B, C, D, E, F) as the `siteClass` query parameter — it has not
  been updated to take the intermediate codes directly. This is a known
  gap between the standard and the public web service.

  Practical consequence: a geotech report citing Site Class BC/CD/DE
  cannot be passed through verbatim. The user must choose the closest
  legacy neighbor and document the choice in the engineering notes.
  See `references/site_class_table.md` for the Vs30 ranges and the
  intermediate-class fallback table. Run this script with
  `--site-class-help` for an inline reminder.
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


USGS_ENDPOINT = "https://earthquake.usgs.gov/ws/designmaps/asce7-22.json"

VALID_RISK_CATEGORIES = {"I", "II", "III", "IV"}

# Legacy 6-class set accepted by the USGS asce7-22.json endpoint.
# ASCE 7-22 §20.3 also defines BC, CD, DE — see SITE_CLASS_HELP below.
VALID_SITE_CLASSES = {"A", "B", "C", "D", "E", "F"}

# ASCE 7-22 intermediate classes the USGS endpoint does NOT accept,
# mapped to the conservative (= more onerous = lower Vs30 → larger
# spectral demand) legacy neighbor. The choice must be documented in
# the engineering notes — this table is a hint, not a substitute for SE
# judgment.
INTERMEDIATE_FALLBACK = {
    "BC": ("C", "ASCE 7-22 BC: Vs30 1,800-2,500 ft/s. USGS endpoint expects legacy A-F. Use C (more conservative neighbor) and document the choice."),
    "CD": ("D", "ASCE 7-22 CD: Vs30 900-1,200 ft/s. USGS endpoint expects legacy A-F. Use D (more conservative neighbor) and document the choice."),
    "DE": ("E", "ASCE 7-22 DE: Vs30 500-600 ft/s. USGS endpoint expects legacy A-F. Use E (more conservative neighbor) and document the choice."),
}

SITE_CLASS_HELP = """\
Site Class input — ASCE 7-22 §20.3 vs USGS endpoint:

  Standard (ASCE 7-22, 9 classes):  A  B  BC  C  CD  D  DE  E  F
  USGS endpoint (legacy, 6 classes): A  B      C      D      E  F

The USGS Seismic Design Maps API for the asce7-22 reference document
accepts only the legacy 6-class set. If your geotech report cites an
ASCE 7-22 intermediate class (BC, CD, DE), choose the closest legacy
neighbor and document the choice in the engineering notes:

  BC -> C   (Vs30 1,800-2,500 ft/s; C covers 1,200-1,800 ft/s)
  CD -> D   (Vs30   900-1,200 ft/s; D covers   600-  900 ft/s)
  DE -> E   (Vs30   500-  600 ft/s; E covers <500 ft/s)

The mappings above pick the more conservative (larger spectral demand)
neighbor. A non-conservative neighbor (e.g. BC -> B) is acceptable
only when the geotech engineer explicitly supports it; flag the
deviation in the seismic summary.

See references/site_class_table.md for the full Vs30/N/Su table.
"""

PARAMETER_LABELS = [
    ("ss", "Ss", "g", "Mapped MCER spectral response, 0.2-second period"),
    ("s1", "S1", "g", "Mapped MCER spectral response, 1-second period"),
    ("sms", "SMS", "g", "Site-modified MCER spectral response, 0.2-second period"),
    ("sm1", "SM1", "g", "Site-modified MCER spectral response, 1-second period"),
    ("sds", "SDS", "g", "Design spectral response acceleration, 0.2-second period"),
    ("sd1", "SD1", "g", "Design spectral response acceleration, 1-second period"),
    ("sdc", "SDC", "—", "Seismic Design Category"),
    ("pgam", "PGA_M", "g", "Site-modified peak ground acceleration"),
    ("ts", "TS", "s", "Short-period transition period (= SD1 / SDS)"),
    ("t0", "T0", "s", "0.2 × TS"),
    ("tl", "TL", "s", "Long-period transition period"),
]


def call_usgs(lat: float, lon: float, risk: str, site: str, title: str, timeout: int = 30) -> dict:
    qs = urllib.parse.urlencode(
        {
            "latitude": lat,
            "longitude": lon,
            "riskCategory": risk,
            "siteClass": site,
            "title": title,
        }
    )
    url = f"{USGS_ENDPOINT}?{qs}"
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        sys.exit(f"USGS API HTTP error {e.code}: {e.reason}. URL: {url}")
    except urllib.error.URLError as e:
        sys.exit(f"USGS API unreachable: {e.reason}. URL: {url}")
    except json.JSONDecodeError as e:
        sys.exit(f"USGS API returned non-JSON response: {e}. URL: {url}")

    if payload.get("request", {}).get("status") != "success":
        sys.exit(
            f"USGS API returned non-success status: "
            f"{payload.get('request', {}).get('status')}. URL: {url}"
        )

    data = payload.get("response", {}).get("data")
    if not data:
        sys.exit(f"USGS API response missing 'response.data'. URL: {url}")

    return {
        "url": url,
        "request_timestamp": payload.get("request", {}).get("date"),
        "data": data,
        "raw": payload,
    }


def main():
    # Pre-scan argv for --site-class-help so we can print the help block
    # without forcing the user to also supply --lat/--lon/etc.
    if "--site-class-help" in sys.argv:
        print(SITE_CLASS_HELP)
        return

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--lat", type=float, required=True)
    parser.add_argument("--lon", type=float, required=True)
    parser.add_argument("--risk-category", required=True, choices=sorted(VALID_RISK_CATEGORIES))
    parser.add_argument(
        "--site-class",
        required=True,
        help=(
            "Site Class accepted by USGS endpoint: A, B, C, D, E, F. "
            "ASCE 7-22 also defines intermediate classes BC, CD, DE — "
            "those are NOT accepted by the USGS API. "
            "Run with --site-class-help for the legacy-neighbor fallback table."
        ),
    )
    parser.add_argument(
        "--site-class-help",
        action="store_true",
        help="Print ASCE 7-22 vs USGS-endpoint Site Class compatibility notes and exit.",
    )
    parser.add_argument("--project", default="project")
    parser.add_argument("--out", required=True, help="Output JSON cache path")
    parser.add_argument("--out-csv", required=True, help="Output per-parameter CSV path")
    parser.add_argument("--timeout", type=int, default=30)
    args = parser.parse_args()

    site_class = args.site_class.strip().upper()
    if site_class in INTERMEDIATE_FALLBACK:
        neighbor, hint = INTERMEDIATE_FALLBACK[site_class]
        sys.exit(
            f"Site Class '{site_class}' is an ASCE 7-22 §20.3 intermediate class "
            f"that the USGS Seismic Design Maps API (asce7-22.json) does not accept.\n"
            f"  Hint: {hint}\n"
            f"  Suggested re-run: pass --site-class {neighbor} and document the "
            f"choice in the seismic summary.\n"
            f"  Run `python scripts/fetch_sdc.py --site-class-help` for the full "
            f"fallback table."
        )
    if site_class not in VALID_SITE_CLASSES:
        sys.exit(
            f"Site Class '{args.site_class}' is not a valid ASCE 7-22 Site Class.\n"
            f"  USGS endpoint accepts: {', '.join(sorted(VALID_SITE_CLASSES))}.\n"
            f"  ASCE 7-22 §20.3 also defines intermediate classes BC, CD, DE — "
            f"those are not accepted by the USGS API; use the closest legacy "
            f"neighbor and document the choice.\n"
            f"  Run `python scripts/fetch_sdc.py --site-class-help` for details."
        )
    args.site_class = site_class

    title = f"archtmpl seismic-lookup {args.project}"
    fetched = call_usgs(args.lat, args.lon, args.risk_category, args.site_class, title, args.timeout)
    data = fetched["data"]

    rows = []
    for key, label, units, description in PARAMETER_LABELS:
        value = data.get(key)
        rows.append(
            {
                "Parameter": label,
                "Value": "" if value is None else str(value),
                "Units": units,
                "Description": description,
                "Source": "USGS Seismic Design Maps API, ASCE 7-22 reference",
                "Confidence": "high" if value is not None else "low",
            }
        )

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        json.dumps(
            {
                "computed_at": datetime.now(timezone.utc).isoformat(),
                "request_url": fetched["url"],
                "request_timestamp": fetched["request_timestamp"],
                "input": {
                    "lat": args.lat,
                    "lon": args.lon,
                    "risk_category": args.risk_category,
                    "site_class": args.site_class,
                    "project": args.project,
                },
                "data": data,
            },
            indent=2,
        )
    )

    csv_path = Path(args.out_csv)
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with csv_path.open("w", newline="") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=[
                "Parameter",
                "Value",
                "Units",
                "Description",
                "Source",
                "Confidence",
            ],
        )
        writer.writeheader()
        for r in rows:
            writer.writerow(r)

    sdc = data.get("sdc", "")
    sds = data.get("sds", "")
    sd1 = data.get("sd1", "")
    print(
        f"Lat: {args.lat}, Lon: {args.lon}. "
        f"Risk: {args.risk_category}, Site: {args.site_class}. "
        f"SDC: {sdc}. SDS: {sds} g. SD1: {sd1} g. "
        f"USGS request: {fetched['request_timestamp']}. "
        f"JSON -> {out_path}. CSV -> {csv_path}."
    )


if __name__ == "__main__":
    main()
