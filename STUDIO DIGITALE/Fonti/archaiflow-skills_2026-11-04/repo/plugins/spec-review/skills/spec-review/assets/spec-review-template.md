# Spec Review — {{PROJECT_NAME}}

**Spec phase:** {{PHASE — e.g., "DD outline", "50% CD", "95% CD", "Issue-for-permit"}}
**Spec system:** {{SYSTEM — e.g., "AIA MasterSpec", "office master", "USACE UFGS", "NYC SCA"}}
**Delivery method:** {{DELIVERY — DBB / CMAR / DB / IPD}}
**AHJ / jurisdiction:** {{AHJ}}
**Code edition basis:** {{CODE_EDITION}}
**OPR reference:** {{OPR_REF}}
**Reviewer:** {{REVIEWER}}
**Review date:** {{DATE}}

---

## Summary

{{ONE_PARAGRAPH_SUMMARY — spec book scope, 2-3 highest-severity findings, drawing-spec coordination defects requiring both a spec edit and a drawing edit.}}

---

## Findings by axis

Note only the axes with real signal.

### 1. Division completeness

{{FINDING_DIVISIONS}}

### 2. Drawing-spec coordination

{{FINDING_DWG_SPEC}}

### 3. Prescriptive vs performance balance

{{FINDING_PRESCRIPTIVE}}

### 4. Basis-of-design & "or equal"

{{FINDING_BOD}}

### 5. Reference-standard currency

{{FINDING_STANDARDS}}

### 6. AHJ-specific references

{{FINDING_AHJ}}

### 7. Section-internal completeness (Part 1/2/3)

{{FINDING_INTERNAL}}

### 8. OPR alignment

{{FINDING_OPR}}

---

## Findings register

| # | Section | Part / paragraph | Issue | Severity | Fix |
|---|---|---|---|---|---|
| 1 | {{F1_SECTION}} | {{F1_PARA}} | {{F1_ISSUE}} | {{F1_SEV}} | {{F1_FIX}} |
| 2 | {{F2_SECTION}} | {{F2_PARA}} | {{F2_ISSUE}} | {{F2_SEV}} | {{F2_FIX}} |
| 3 | {{F3_SECTION}} | {{F3_PARA}} | {{F3_ISSUE}} | {{F3_SEV}} | {{F3_FIX}} |

Severity tags: **High** (defect; will cause bid risk or AHJ rejection), **Medium** (likely RFI in CA), **Low** (cleanup).

---

## Drawing-spec coordination defects

Defects requiring both a spec edit and a drawing edit (highest CO risk if not caught now):

- [ ] {{DWG_SPEC_1}}
- [ ] {{DWG_SPEC_2}}

---

## Reference-standard updates

Standards cited with outdated edition years that should be updated. **Verify each "current edition" against the publisher (ASTM, ACI, ASHRAE, NFPA, UL, etc.) at review time** — do not pull from a bundled lookup table; standards revise on rolling cycles and a stale lookup is a defect-injection risk. Cite the publisher URL or document accessed in the verification column.

| Standard | Cited edition | Current edition (verified at review) | Verified via | Action |
|---|---|---|---|---|
| {{STD_1}} | {{STD_1_OLD}} | {{STD_1_NEW}} | {{STD_1_SOURCE — e.g., astm.org product page accessed YYYY-MM-DD}} | {{STD_1_ACTION}} |
| {{STD_2}} | {{STD_2_OLD}} | {{STD_2_NEW}} | {{STD_2_SOURCE}} | {{STD_2_ACTION}} |

---

## Missing or incomplete sections

Sections that are absent or have placeholder language at this phase:

- [ ] {{MISSING_1}}
- [ ] {{MISSING_2}}

---

## OPR-driven sections to verify

Performance criteria from the OPR and the spec sections that must enforce them:

| OPR criterion | Spec section that should enforce | Status |
|---|---|---|
| {{OPR_1}} | {{OPR_1_SECTION}} | {{OPR_1_STATUS}} |
| {{OPR_2}} | {{OPR_2_SECTION}} | {{OPR_2_STATUS}} |

---

## Recommended next skills / actions

- {{NEXT_1 — e.g., "Run `bid-review` once 95% CD spec issues; pre-load divisions where prescriptive language drives bid risk."}}
- {{NEXT_2 — e.g., "Coordinate fire-rated assemblies with `code-compliance-review` against IBC §714 firestopping."}}

---

## References cited

- {{REF_1 — e.g., "CSI MasterFormat 2020"}}
- {{REF_2 — e.g., "AIA B101-2017 §3.4.5"}}
- {{REF_3 — e.g., "ASTM C1396-17 (verified at astm.org, accessed 2026-05-09)"}}
