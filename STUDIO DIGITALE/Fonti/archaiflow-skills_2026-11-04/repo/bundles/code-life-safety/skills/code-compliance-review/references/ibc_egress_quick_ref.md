# IBC Egress Quick Reference (2021 / 2024)

Condensed lookup for occupant-load factors, common-path / travel-distance limits, exit-count thresholds, corridor and dead-end limits, and accessible-route requirements. Use this for fast on-the-fly orientation; **verify the actual code text against the AHJ's adopted PDF / ICC Digital Codes before publishing a finding.** Per-row values shift between IBC editions and between state amendments — this file marks `[verify per IBC ed.]` where recall confidence is not high.

Edition: IBC 2021 with notes where IBC 2024 differs. State amendments (CBC, NYS, FBC, OBC, etc.) override; check `code_editions_by_jurisdiction.md`.

---

## Occupant-load factors — Table 1004.5 (excerpt) [verify per IBC ed.]

These are recalled values for orientation. Confirm the row (and especially footnotes — many use-types are sub-categorized) against the AHJ-adopted edition before quoting.

| Use | Factor | Basis |
|---|---|---|
| Assembly, concentrated (no fixed seats) | 7 | Net |
| Assembly, unconcentrated (tables/chairs) | 15 | Net |
| Assembly, fixed seats | seat count | — |
| Assembly, standing space | 5 | Net |
| Bowling alley (allow 5 / lane) | 7 | — |
| Business areas | 150 | Gross |
| Conference rooms / meeting rooms | 15 | Net (per footnote a) |
| Educational, classroom | 20 | Net |
| Educational, shops / vocational | 50 | Net |
| Industrial | 100 | Gross |
| Institutional, sleeping (general) | 120 | Gross |
| I-2 patient sleeping | 240 | Gross |
| Library, reading rooms | 50 | Net |
| Library, stack area | 100 | Gross |
| Mercantile, basement / grade floor | 30 | Gross |
| Mercantile, upper floors | 60 | Gross |
| Parking garages | 200 | Gross |
| Residential | 200 | Gross |
| Storage, mechanical equipment | 300 | Gross |

Net = walls and fixed obstructions excluded; Gross = entire floor area. **Conference / meeting rooms route to Assembly Unconcentrated by Table 1004.5 footnote** — this footnote is the most common occupant-load error in B-occupancy plans.

---

## Common-path-of-travel — Table 1006.2.1 (excerpt) [verify per IBC ed.]

Common-path limits depend on occupancy, sprinkler status, and (for some occupancies) the occupant load served. The IBC 2021 table has multiple footnotes and per-row exceptions. Recall-only values below — confirm before quoting.

| Occupancy | Sprinklered (NFPA 13) | Unsprinklered |
|---|---|---|
| A, E, M | [verify per IBC ed.] (commonly 75 ft) | [verify per IBC ed.] (commonly 75 ft) |
| B (occ load ≤30) | [verify per IBC ed.] (commonly 100 ft) | [verify per IBC ed.] (commonly 75 ft) |
| B (occ load >30) | [verify per IBC ed.] (commonly 100 ft) | [verify per IBC ed.] (commonly 75 ft) |
| F-1, S-1 | [verify per IBC ed.] (commonly 100 ft) | [verify per IBC ed.] (commonly 75 ft) |
| H-1, H-2 | 25 ft [verify per IBC ed.] | 25 ft [verify per IBC ed.] |
| I-1, R-1, R-2, R-3, R-4 | [verify per IBC ed.] (commonly 75 ft) | [verify per IBC ed.] (commonly 75 ft) |
| I-2 | [verify per IBC ed.] | NP unsprinklered (most cases) |

NP = Not Permitted. R-occupancy common path is measured *within* the dwelling unit per §1006.2.1 footnote and has separate limits — consult the table directly.

---

## Travel distance — Table 1017.2 (excerpt) [verify per IBC ed.]

| Occupancy | Sprinklered | Unsprinklered |
|---|---|---|
| A, E | 250 ft [verify] | 200 ft [verify] |
| B, F-1, M, S-1 | 300 ft [verify] | 200 ft [verify] |
| F-2, S-2 | 400 ft [verify] | 300 ft [verify] |
| H-1 | 75 ft [verify] | NP |
| H-2 | 100 ft [verify] | NP |
| H-3 | 150 ft [verify] | NP |
| H-4 | 175 ft [verify] | NP |
| H-5 | 200 ft [verify] | NP |
| I-1 | 250 ft [verify] | 200 ft [verify] |
| I-2 | 200 ft [verify] | NP |
| R-1, R-2, R-3 | 250 ft [verify] | 200 ft [verify] |
| R-4 | 250 ft [verify] | 200 ft [verify] |
| U | 250 ft [verify] | 200 ft [verify] |

The "sprinklered" column assumes NFPA 13 throughout (not 13R or 13D). State amendments and atrium increases (§404 / §1029) modify these.

---

## Number of exits — §1006.2 / §1006.3

Per story (most occupancies) [verify per IBC ed.]:

| Occupant load | Required exits |
|---|---|
| 1-49 | 1 (subject to common-path / travel limits in §1006.3 and Table 1006.3.3) |
| 50-500 | 2 |
| 501-1,000 | 3 |
| >1,000 | 4 |

Single-exit conditions (§1006.3) include limited residential stories, certain B / F-1 / M / S-1 occupancies with travel distance ≤75 ft sprinklered (with occupant-load caps). Conditions vary by occupancy and edition — check the table directly.

---

## Egress capacity factors — §1005.3 [verify per IBC ed.]

Per occupant served. **Default values apply unless the building is sprinklered with NFPA 13 + emergency voice/alarm AND is not Group H or I-2 — in which case the reduced values apply.**

| Path | Default (unsprinklered, or H, or I-2) | Reduced (NFPA 13 + voice/alarm + non-H/non-I-2) |
|---|---|---|
| Egress stairways | **0.3 in/occupant** | **0.2 in/occupant** |
| Other egress components (level, ramp ≤1:12, doors) | **0.2 in/occupant** | **0.15 in/occupant** |

The 0.2 / 0.15 reduction requires *all three* conditions: (1) sprinkler system per §903.3.1.1 (NFPA 13) or §903.3.1.2, (2) emergency voice/alarm communication per §907.5.2.2, and (3) the building is not Group H or I-2. Multiplied by the occupant load served by the component to give required clear width in inches.

---

## Door clear width — §1010.1.1 [verify per IBC ed.]

- Minimum 32 in clear (door open 90°, measured from face of door to stop).
- Maximum 48 in single leaf in a swing door.
- Power-operated and revolving doors: see §1010.1.4.
- Accessible: 32 in clear matches IBC; maneuvering clearances per ICC A117.1-2017 §404.

---

## Stair width — §1011.2 [verify per IBC ed.]

- Minimum 44 in serving >50 occupants.
- Minimum 36 in serving ≤50 occupants.
- Capacity factor: 0.3 in/occupant default; 0.2 in/occupant when reduced (see capacity table above).

Tread / riser per §1011.5: tread 11 in min, riser 4-7 in [verify]. Handrail height 34-38 in per §1014.

---

## Corridor width — §1020.3 (most uses) [verify per IBC ed.]

- 44 in min (general).
- 36 in min where occupant load ≤50.
- 72 in min in E with >100 occupants in corridor.
- 96 in min in I-2 patient corridors.

---

## Dead-end corridor — §1020.5 [verify per IBC ed.]

- Commonly 20 ft sprinklered B/F/M/S/U (recall).
- Up to 50 ft in some sprinklered B per §1020.5.1 exception.
- 0 ft in H-1.

---

## Exit separation — §1007.1.1 [verify per IBC ed.]

- Two exits required: separated by ≥1/2 the diagonal of the area served (unsprinklered) or ≥1/3 the diagonal (sprinklered with NFPA 13).
- Three or more exits: at least two satisfy the separation; the rest "reasonably distributed" per §1007.1.1.

---

## Accessible means of egress — §1009 [verify per IBC ed.]

- 1 accessible MOE per accessible space; 2 where ≥2 means of egress are required.
- Areas of refuge (§1009.6) required where the building is not sprinklered with NFPA 13 throughout, with several exceptions.
- Accessible elevator (§1009.4) qualifies as accessible MOE only with standby power, signage, monitoring, and other criteria — read §1009.4 directly.

---

## Type A / Type B dwelling units — §1107 [verify per IBC ed.]

R-2 (multifamily, 4+ units) — recall, confirm against the table:

- **Type A:** ≥2% of total units, never less than 1, where the building is required to be Accessible per §1107.6.2.1.1 (and varies by other R-occupancy sub-rows).
- **Type B:** All R-2 units in buildings with elevators (and certain non-elevator conditions). See §1107.6.4 for the actual thresholds — there are exceptions for low-rise / few-unit buildings.

---

## Stretcher elevator — §3002.4 [verify per IBC ed.]

Required in I-2, I-3 with 4+ stories, R-1 / R-2 with 4+ stories (recall — confirm the trigger condition in §3002.4 of the AHJ-adopted edition). Minimum interior dimension: commonly cited as 80 in deep × 54 in wide [verify per IBC ed.] with min door opening per the section.

---

## Use this with the adopted code text

For a specific finding, pull the exact section text from the actual IBC PDF (or jurisdiction-amended code). **This quick reference is for orientation — never quote it as authoritative in the review file.** Per-row values are recalled and may drift between editions.
