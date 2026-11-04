# Provenance — LEED Tracker References

## Primary source

**LEED v4.1 BD+C: New Construction** scorecard and credit structure.

- Publisher: U.S. Green Building Council (USGBC)
- Rating system version: **v4.1**
- Adaptation: **Building Design + Construction (BD+C)**, project type **New Construction (NC)**
- Public scorecard: https://www.usgbc.org/leed/v41
- Reference Guide: USGBC LEED v4.1 BD+C Reference Guide (paywalled — purchase from usgbc.org)
- Credit numbering and point values: as published on the USGBC v4.1 scorecard PDF
- Total possible points: **110** (100 base + 6 Innovation + 4 Regional Priority)

## Coverage of this skill

| Reference file | Covers |
|----------------|--------|
| `leed_v41_bdc_nc_points.md` | Full credit list (LT/SS/WE/EA/MR/EQ/IN/RP), point values, prereqs, certification thresholds |
| `leed_categories.md` | Category-level summary (max points per category, role of each category) |

**Out of bundled scope** (refer to USGBC LEED v4.1 BD+C Reference Guide):

- Credit-by-credit *technical requirements* (modeling methodology, documentation forms, calculator templates).
- Sub-options within multi-path credits (e.g. EA Credit 2 paths beyond their headline names).
- Strategy guidance ("how to earn this credit").
- Other rating systems (Core & Shell, Schools, Retail, Hospitality, Healthcare, Data Centers, Warehouses, ID+C, O+M, ND).

## Verification status

- **Last verified against USGBC v4.1 BD+C scorecard PDF**: 2026-05-09
- **Source PDF**: `LEED-v41-BD-C-Rating-System_7-2020.pdf` (1.1 MB, dated 2020-07-10), retrieved from `https://www.usgbc.org/sites/default/files/2020-11/LEED-v41-BD-C-Rating-System_7-2020.pdf`
- **Update trigger**: When USGBC publishes a v4.1 amendment, an addendum, or v5. As of last verified date, v4.1 is current.

## Audit history

- **2026-05-09** — Cross-checked bundled credit list, max-points, and category caps against the USGBC v4.1 BD+C Rating System PDF (NC adaptation, pages 1–115 covering IP / LT / SS / WE / EA / MR + partial EQ). Findings: max-points correct on every credit; category caps correct (IP 1, LT 16, SS 10, WE 11, EA 33, MR 13, EQ 16, IN 6, RP 4 — total 110); certification thresholds correct (40 / 50 / 60 / 80). **Two credit name corrections applied**:
  - LT Cr 3: "High Priority Site" → "High-Priority Site and Equitable Development" (v4.1 added the equitable-development path).
  - WE Cr 3: "Optimize Process Water Use" → "Cooling Tower and Process Water Use".
- **2026-05-08** — Initial bundle created (subsequently flagged as recall-based; superseded by 2026-05-09 verified state).

## How to verify

1. Download the USGBC LEED v4.1 BD+C scorecard PDF from usgbc.org.
2. Compare credit names + point values against `leed_v41_bdc_nc_points.md`.
3. If they differ, the reference file is wrong — file an issue against `archtmpl`.

## Version pin warning

LEED is regularly updated:

- LEED v4 → v4.1 (2019)
- v4.1 has had multiple addenda since
- LEED v5 was in development as of 2024 — when published, this reference set must be re-verified or replaced.

Update the **Last verified** date above on each verification. That date is the record. This line used to name a `Version` and a `Last Verified` property in a Notion database; that database was removed on 2026-07-28 and this file is now the only place the date lives. Users should re-install this skill periodically (`npx archtmpl@latest --skill leed-tracker`) to pull the latest references.
