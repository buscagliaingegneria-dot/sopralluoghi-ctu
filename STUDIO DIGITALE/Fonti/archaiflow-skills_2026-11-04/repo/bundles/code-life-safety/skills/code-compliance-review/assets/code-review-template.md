---
project: "{{PROJECT_NAME}}"
date: "{{YYYY-MM-DD}}"
reviewer: "{{REVIEWER_NAME_OR_INITIALS}}"
code_edition: "{{e.g., IBC 2021 + NYS 2020 supplements (NYS BC 2020)}}"
occupancy_classification: "{{e.g., B + A-3 separated per §508.4}}"
construction_type: "{{IBC Table 601 — e.g., II-B}}"
sprinklered: "{{Yes, NFPA 13 throughout | Yes, NFPA 13R | No | Partial — describe}}"
ahj: "{{e.g., NYC DOB; FDNY for life-safety; NYC SCA if public school}}"
risk_category: "{{IBC Table 1604.5 — I / II / III / IV}}"
scope: "{{e.g., Level 3 east wing, schematic plan dated 2026-04-28}}"
---

# Code Review (IBC Egress, Accessibility & Life-Safety) — {{PROJECT_NAME}}

## Summary

{{ONE_PARAGRAPH_SUMMARY — what was reviewed, the 2-3 most pressing non-compliances, and the recommended next move.}}

---

## Occupant load — calculation summary

| Space / area | Use / factor | Net or Gross | Area (sf) | Calc | Occupants |
|---|---|---|---|---|---|
| {{SPACE_1}} | {{USE / FACTOR_1}} | {{N or G}} | {{AREA_1}} | {{CALC_1}} | {{OCC_1}} |
| {{SPACE_2}} | {{USE / FACTOR_2}} | {{N or G}} | {{AREA_2}} | {{CALC_2}} | {{OCC_2}} |
| **Total per story** | | | | | **{{TOTAL_OCC}}** |

Cite the table footnote for each non-obvious factor (e.g., conference rooms scored as Assembly Unconcentrated 15 net per IBC 2021 Table 1004.5 footnote a).

---

## Findings by axis

Note only the axes with real signal. For axes that are clearly compliant, state so in one line with the section pin.

### 1. Occupancy classification & occupant load

{{FINDING_OCCUPANCY_LOAD}}

### 2. Egress capacity, travel distance & common path

{{FINDING_CAPACITY_TRAVEL_COMMONPATH}}

### 3. Exits required, remoteness & arrangement

{{FINDING_EXITS_REMOTENESS}}

### 4. Accessible means of egress

{{FINDING_ACCESSIBLE_MOE}}

### 5. Fire/smoke barriers & opening protectives

{{FINDING_FIRE_SMOKE_BARRIERS}}

### 6. Fire-resistance ratings & construction type

{{FINDING_FIRE_RESISTANCE_CONSTRUCTION}}

### 7. Accessibility (ADA + ICC A117.1 + IBC Ch. 11 + state amendments)

{{FINDING_ACCESSIBILITY}}

### 8. AHJ-specific overlays

{{FINDING_AHJ_OVERLAYS}}

---

## Findings table

Each finding tagged: **code minimum** / **above code** / **below code**. Mitigation column states the design move that resolves the finding (or AHJ avenue: code-modification, AMM, alternate compliance).

| # | Axis | Item | IBC §ref (with edition) | Status | Mitigation |
|---|------|------|-------------------------|--------|------------|
| 1 | {{AXIS_1}} | {{ITEM_1}} | {{e.g., IBC 2021 §1006.2.1, Table 1006.2.1}} | {{STATUS_1}} | {{MITIGATION_1}} |
| 2 | {{AXIS_2}} | {{ITEM_2}} | {{REF_2}} | {{STATUS_2}} | {{MITIGATION_2}} |
| 3 | {{AXIS_3}} | {{ITEM_3}} | {{REF_3}} | {{STATUS_3}} | {{MITIGATION_3}} |

---

## Hard non-compliances (resolve before next CD set)

- [ ] {{NON_COMPLIANCE_1}}
- [ ] {{NON_COMPLIANCE_2}}

---

## Borderline items (flag for AHJ pre-submittal meeting, code-modification request, or AMM)

- {{BORDERLINE_1}}
- {{BORDERLINE_2}}

---

## Action items

1. {{ACTION_1 — e.g., "Architect: revise Stair 2 enclosure rating from 1-hr to 2-hr per IBC 2021 §713.4 (shaft >4 stories)."}}
2. {{ACTION_2 — e.g., "MEP: confirm sprinkler scope is NFPA 13 (not 13R) for egress capacity factor reduction."}}
3. {{ACTION_3 — e.g., "Owner: confirm Type B unit count target before next CD set."}}

---

## Recommended next skills / actions

- {{NEXT_1 — e.g., "Pull the full accessible-MOE language from IBC 2021 §1009 in the adopted PDF."}}
- {{NEXT_2 — e.g., "Coordinate fire-rating assemblies with `spec-review` against Section 07 84 00 firestopping."}}

---

## References cited

- {{REF_1 — e.g., "IBC 2021 Table 1004.5"}}
- {{REF_2 — e.g., "IBC 2021 §1006.2.1, Table 1006.2.1"}}
- {{REF_3 — e.g., "ICC A117.1-2017 §404.2.4"}}
- {{REF_4 — e.g., "ADA 2010 §206.4"}}
- {{REF_5 — e.g., "NYC BC 2022 §[amended section]"}}
