---
project: {{PROJECT_NAME}}
date: {{YYYY-MM-DD}}
reviewer: {{REVIEWER}}
phase: {{SD | DD | CD | IFC}}
gc_engaged: {{yes | no | CMar}}
---

# Constructability Review — {{PROJECT_NAME}}

**Phase:** {{PHASE — e.g., "DD", "50% CD", "95% CD", "GMP set", "IFC"}}
**Delivery method:** {{DELIVERY — DBB / CMAR / DB / IPD}}
**Construction type:** {{TYPE — IBC §602}}
**Structural system:** {{STRUCTURE — steel / CIP concrete / mass timber / hybrid}}
**Envelope system:** {{ENVELOPE — curtain wall / panelized / brick veneer / etc.}}
**Site context:** {{SITE — e.g., "urban infill, 3 sides bordered, no off-site lay-down"}}
**AHJ(s):** {{AHJS — e.g., "NYC DOB + FDNY", "CA HCAI", "DSA", "GSA Region 9"}}
**Reviewer:** {{REVIEWER}}
**Review date:** {{DATE}}
**GC / CMar / preconstruction partner:** {{GC_NAME — or "not yet engaged"}}
**Dominant risk axis:** {{DOMINANT — e.g., "long-lead procurement, phased occupancy"}}

---

## Summary

{{ONE_PARAGRAPH_SUMMARY — CD set status, 2-3 highest-severity findings with estimated change-order avoidance value when caught now vs at CA, and the overall recommendation (proceed / proceed-with-conditions / hold-for-rework).}}

---

## Findings by axis

Each finding severity-tagged: **High** (will cause CO or schedule slip if not addressed before next CD set), **Medium** (likely to surface as RFI in CA), **Low** (worth noting; resolvable without redesign).

Note only the axes with real signal. For axes that are clearly fine, state so in one line.

### 1. Trade sequencing & critical path

{{FINDING_SEQUENCING}}

### 2. Tolerance stack-up

{{FINDING_TOLERANCE — cite contributing assemblies' tolerances and source: AISC 303-22 for steel, ACI 117 for CIP concrete, SMACNA for sheet metal, glazing manufacturer install guide}}

### 3. MEP coordination & rack space

{{FINDING_MEP — above-ceiling clearance, riser stack alignment, NEC 2023 §110.26 service clearance, removal route for AHU/chiller/switchgear}}

### 4. Install access & rigging

{{FINDING_ACCESS — crane reach, hoisting paths, equipment-room dimensions, future-replacement removal route}}

### 5. Lay-down & site logistics

{{FINDING_LAYDOWN — material storage, truck deliveries, crane swing radius / airspace easements, pedestrian protection per IBC 2024 §3306, OSHA 1926 Subpart M, local AHJ}}

### 6. Temporary works

{{FINDING_TEMPORARY — shoring per OSHA 1926 Subpart P, dewatering, weather enclosure, life-safety / fire watch per NFPA 241-22}}

### 7. Materials procurement & lead times

{{FINDING_LEADTIMES — pull current quotes per `references/long_lead_items_2026.md` methodology; each lead-time number cited must reference the manufacturer + quote date}}

### 8. Phased operations & owner occupancy

{{FINDING_PHASED — owner-occupied phasing, ICRA per ASHRAE 170-2021 / FGI Guidelines 2022 for healthcare, AHJ approval for temporary conditions}}

---

## Long-Lead Risk Register

Pull current quotes per the methodology in `references/long_lead_items_2026.md`. **Do not use recalled or table-baked lead times.** Cite manufacturer, quote source, and quote date for every row.

| Item | Current lead time (weeks) | Source / quote date | Mitigation |
|---|---|---|---|
| {{LL_1_ITEM}} | {{LL_1_WEEKS}} | {{LL_1_SOURCE_DATE}} | {{LL_1_MITIGATION}} |
| {{LL_2_ITEM}} | {{LL_2_WEEKS}} | {{LL_2_SOURCE_DATE}} | {{LL_2_MITIGATION}} |
| {{LL_3_ITEM}} | {{LL_3_WEEKS}} | {{LL_3_SOURCE_DATE}} | {{LL_3_MITIGATION}} |

Source convention: "Eaton customer letter, 2026-04-12", "Trane PM rep email, 2026-04-22", "AISC market quarterly Q1 2026", "Walters fab quote, 2026-03-30". Quotes older than ~90 days should be re-confirmed before basing schedule decisions on them.

---

## Sequencing & Phasing Concerns

Issues where the documented or assumed construction sequence is physically impossible, requires rework, or conflicts with the master schedule. Reference specific schedule activities or sheet/detail callouts.

- {{SEQ_1 — e.g., "Per CPM activity 1340, curtain-wall install starts day 145; slab pour completes day 138 — only 7 days of cure vs 28-day requirement in spec section 03 30 00"}}
- {{SEQ_2}}
- {{SEQ_3}}

If the project is owner-occupied or phased, also document temporary-condition risks here — egress paths during each phase, mechanical of patient/student transitions (MOP), security boundaries, and AHJ approvals for the temporary condition (NYC DOB occupied-building protocols, CA HCAI for healthcare, DSA for K-12, GSA tenant-occupied protocols, NAVFAC / USACE for federal).

---

## Trade Coordination Conflicts

Conflicts between disciplines that surface as install-time problems even when each discipline's drawings are internally consistent. Name the discipline pair and the specific conflict.

| # | Discipline pair | Conflict | Drawing/spec ref | Severity | Recommended move |
|---|---|---|---|---|---|
| 1 | {{TC_1_PAIR — e.g., "Mechanical × Structural"}} | {{TC_1_DESC}} | {{TC_1_REF}} | {{TC_1_SEV}} | {{TC_1_MOVE}} |
| 2 | {{TC_2_PAIR — e.g., "Electrical × Architectural"}} | {{TC_2_DESC}} | {{TC_2_REF}} | {{TC_2_SEV}} | {{TC_2_MOVE}} |
| 3 | {{TC_3_PAIR — e.g., "Fire-protection × Mechanical"}} | {{TC_3_DESC}} | {{TC_3_REF}} | {{TC_3_SEV}} | {{TC_3_MOVE}} |

Common pairs that bite: Mech × Struct (duct routing through beams), Elec × Arch (panel access vs millwork), FP × Mech (sprinkler heads vs diffusers), Plumbing × Struct (riser cores vs shear walls), Low-voltage × Ceiling (cable tray vs lighting layout), Curtain wall × Steel (anchor placement tolerance vs frame deviation), Concrete × MEP (slab embeds and sleeves vs final routing).

---

## Action items

| # | Finding | Severity | Drawing/spec ref | Owner | Due | Recommended move | Est. CO if surfaced in CA (USD) |
|---|---|---|---|---|---|---|---|
| 1 | {{F1_SUMMARY}} | {{F1_SEV}} | {{F1_REF}} | {{F1_OWNER}} | {{F1_DUE}} | {{F1_MOVE}} | ${{F1_CO}} |
| 2 | {{F2_SUMMARY}} | {{F2_SEV}} | {{F2_REF}} | {{F2_OWNER}} | {{F2_DUE}} | {{F2_MOVE}} | ${{F2_CO}} |
| 3 | {{F3_SUMMARY}} | {{F3_SEV}} | {{F3_REF}} | {{F3_OWNER}} | {{F3_DUE}} | {{F3_MOVE}} | ${{F3_CO}} |

---

## High-severity items (resolve before next CD set)

- [ ] {{HIGH_1}}
- [ ] {{HIGH_2}}
- [ ] {{HIGH_3}}

---

## Recommended next skills / actions

- {{NEXT_1 — e.g., "Pre-load `submittal-review` for switchgear and AHU long-leads."}}
- {{NEXT_2 — e.g., "Coordinate phased life-safety plan with `code-compliance-review` against IBC 2024 §1023."}}

---

## References cited

- {{REF_1 — e.g., "AISC 303-22 erection tolerance"}}
- {{REF_2 — e.g., "ACI 117 CIP concrete tolerance"}}
- {{REF_3 — e.g., "SMACNA HVAC Duct Construction Standards (current)"}}
- {{REF_4 — e.g., "NEC 2023 §110.26 working space"}}
- {{REF_5 — e.g., "NFPA 241-22 fire watch / construction safeguards"}}
- {{REF_6 — e.g., "OSHA 1926 Subpart M / Subpart P"}}
- {{REF_7 — e.g., "ASHRAE 170-2021 / FGI Guidelines 2022 (healthcare)"}}
- {{REF_8 — e.g., "Eaton 2026-04-12 customer letter (switchgear lead time)"}}
