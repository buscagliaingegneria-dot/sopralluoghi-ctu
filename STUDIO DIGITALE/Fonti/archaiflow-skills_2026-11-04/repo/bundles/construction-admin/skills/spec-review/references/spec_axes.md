# Spec Review — Eight Axes

Detailed framework for auditing a project specification against North American practice norms. Each axis carries sub-criteria, common failure modes, and example findings phrased the way they should appear in the review file.

Aligned with CSI MasterFormat 2020, CSI SectionFormat / PageFormat, AIA MasterSpec / SpecLink / ARCAT-derived office masters, ConsensusDOCS, and major agency masters (UFGS for USACE, P-100 for GSA, OSP for CA HCAI, NYC SCA spec).

---

## 1. Division completeness

**Sub-criteria:**

- Required Divisions present for the project's scope. Division 00 (Procurement & Contracting), 01 (General Requirements), 02 (Existing Conditions, on renovations), 03-09 (typical building shell + interiors), 10-14 (specialties / equipment / furnishings), 21-23 (fire suppression / plumbing / HVAC), 25-28 (integrated automation, electrical, communications, electronic safety), 31-33 (earthwork / exterior improvements / utilities) on ground-up.
- Section-numbering follows MasterFormat 2020 (e.g., 08 41 13 — Aluminum-Framed Entrances and Storefronts; not the legacy 08 12 16).
- Division-level introduction sections present where the master uses them (e.g., Section 23 05 00 Common Work for HVAC).

**Common failure modes:**

- Renovation project missing Division 02. Existing-conditions language scattered across Division 01 instead.
- Division 13 (Special Construction) absent on a lab / medical / data center project.
- Division 25 (Integrated Automation) absent on a building marketed as "smart."
- Section numbers using legacy MasterFormat 1995 (e.g., "08120 — Aluminum Doors") in a modern spec book.

**Example finding:**

> Spec book Table of Contents lists Sections 01-09 only. Project includes site work (utilities, paving, landscaping) per Civil drawings C1-C6. Divisions 31-33 (Earthwork / Exterior Improvements / Utilities) are absent. Either add the missing Divisions to the spec book or confirm site work is in a separate Civil-only spec package and reference it in Section 01 11 00.

---

## 2. Drawing-spec coordination

**Sub-criteria:**

- Spec-section refs on drawings (e.g., "see 08 41 13") resolve to actual sections in the spec book.
- Sheet/detail refs in specs resolve to actual drawings.
- Material call-outs on plans match products in spec basis-of-design.
- Schedules (door, window, finish, hardware) resolve to specs.
- Reference standards on drawings align with reference standards in specs.

**Common failure modes:**

- Drawing notes say "see 09 24 00 for stucco assembly"; Section 09 24 00 doesn't exist (assembly was moved to 07 24 00 EIFS in a revision; drawing not updated).
- Door schedule callout for "HW Group 12"; Section 08 71 00 hardware sets only go through Group 10.
- Spec section references "see Sheet A8.04 for sill flashing detail"; Sheet A8.04 is the roof plan.

**Example finding:**

> Drawing G0.01 General Notes Item 7: "All exterior insulated metal panels per Section 07 42 13." Section 07 42 13 in the spec book is "Metal Wall Panels" (single-skin); insulated metal panels are Section 07 42 16. Either renumber the spec section, update the General Note to 07 42 16, or confirm which assembly is intended. Drawings and spec must align before 100% CD.

---

## 3. Prescriptive vs performance balance

**Sub-criteria:**

- Each section uses prescriptive language (named product / dimension / installation method) where the owner has a defined preference.
- Performance language (test result / criterion / industry standard) where multiple products may comply.
- Mixed within a section is fine; contradictory within a section is a defect.
- Performance criteria explicitly tied to a measurable test ("Air leakage ≤0.06 cfm/sf at 6.24 psf").

**Common failure modes:**

- "Provide 5/8" Type X gypsum board, USG Sheetrock Brand FireCode Core, or any equal product with X performance" — the "or equal" defeats the named product.
- Performance criteria stated qualitatively: "high-performance glazing" with no SHGC / U-factor / VT.
- Prescriptive method called out where the spec should leave means-and-methods to the contractor (e.g., spec'ing the type of nail gun).

**Example finding:**

> Section 09 24 23 Part 2.2.A.1: "Three-coat stucco system per ASTM C926 with 7/8" total thickness. Hard-trowel finish. Or any equal three-coat stucco system." The "or any equal" defeats the prescriptive scope — an EIFS or one-coat stucco bidder may claim equivalence. Either delete the "or equal" or replace the prescriptive scope with a performance-based one-coat-or-three-coat alternative.

---

## 4. Basis-of-design & "or equal"

**Sub-criteria:**

- Named manufacturers list 2-3 acceptable equals.
- Substitution mechanism per Section 01 25 00.
- "Sole-source" specifications justified per the AHJ's procurement law (typically a memo on file for public projects).
- "Approved equal" mechanism specified — typically requires written request 7-15 days before bid with comparison data.

**Common failure modes:**

- Single manufacturer named with no equals — defaults to sole-source, which on public projects may be procurement-non-compliant without a sole-source memo.
- "Or approved equal" with no defined process for approval.
- 5+ manufacturers listed without a basis-of-design — the design intent is undefined.

**Example finding:**

> Section 08 81 13 Part 2.1.A names only "Manufacturer XYZ Architectural Glazing Systems, Series 5500" with no acceptable equals. Project is publicly funded by NYC SCA. Per NYC PPB rules, sole-source specifications require a sole-source memo on file approved by the agency. Either add 2 acceptable equals (typical: Manufacturer ABC Series 4000, Manufacturer DEF Series 7200), or attach the sole-source justification memo.

---

## 5. Reference-standard currency

**Sub-criteria:**

- ASTM, ANSI, UL, NFPA, ASHRAE, AISC, ACI, ASCE, ICC standards cited with edition year.
- Year is current per `reference_standards_currency_2026.md`.
- Generic standard cited without year is a defect.

**Common failure modes:**

- "ASTM C1396" without year — the 2017 edition tests differently from the 2014 edition.
- ASTM C1396-14 cited; current is C1396-17.
- ASCE 7-16 cited when the AHJ has adopted ASCE 7-22.
- IECC 2018 cited when the jurisdiction uses IECC 2021 with state amendments.

**Example finding:**

> Section 03 30 00 Part 1.03.A references "ACI 318" without edition year. Current edition is ACI 318-19; many jurisdictions have adopted ACI 318-19 with the IBC 2021. Update to "ACI 318-19" (or whichever edition the project's AHJ has adopted; confirm with structural EOR). Same correction applies to ACI 117, ACI 301, and ACI 350 references throughout Section 03.

---

## 6. AHJ-specific references

**Sub-criteria:**

- Local amendments cited (CBC 2022 §1505 for fire-rated roof in WUI; NYC LL126 for parking-garage scope).
- AHJ-required certifications named (NYC DOB MEA / OTCR, FDNY COA, CA OSHPD/HCAI OSP, USACE UFGS specials).
- Federal projects (GSA, USACE, VA, DoD) use their own master spec systems; commercial defaults left in are findings.
- Tribal, military, and federal land projects: jurisdiction is federal regardless of state; state code references may not apply.

**Common failure modes:**

- Spec on a USACE project uses commercial CSI sections; UFGS sections required.
- NYC project missing MEA citations on products that require it (e.g., proprietary fire-rated assemblies).
- California WUI amendment §R902 missing from a roofing section in a wildfire-prone county.
- "Local jurisdiction" language without naming the actual AHJ.

**Example finding:**

> Section 07 32 13 (clay roof tile) references "ASTM C1167" without amendment for WUI areas. Project is in San Bernardino County, CA, in a Very-High Fire Hazard Severity Zone. CBC 2022 §R902 / Chapter 7A requires Class A roofing assemblies with passing 2014 SFM 12-7A-2 burning-brand and intermittent-flame tests. Add 12-7A-2 / 12-7A-3 test references and clarify Class A assembly requirement.

---

## 7. Section-internal completeness (Part 1/2/3)

Per CSI SectionFormat:

**Part 1 — General**
- 1.01 Summary
- 1.02 References
- 1.03 Definitions
- 1.04 Submittals
- 1.05 Quality Assurance
- 1.06 Delivery, Storage, and Handling
- 1.07 Project / Site Conditions
- 1.08 Warranty / Guarantee
- 1.09 Maintenance Service

**Part 2 — Products**
- 2.01 Manufacturers
- 2.02 Materials / Equipment
- 2.03 Components
- 2.04 Fabrication
- 2.05 Finishes
- 2.06 Mixes
- 2.07 Source Quality Control

**Part 3 — Execution**
- 3.01 Examination
- 3.02 Preparation
- 3.03 Installation / Application / Erection
- 3.04 Field Quality Control
- 3.05 Adjustment / Cleaning
- 3.06 Demonstration
- 3.07 Protection

**Common failure modes:**

- Part 3 (Execution) limited to "install per manufacturer's instructions" — no examination or field quality control.
- Submittal article missing required items (e.g., fire-rating test reports for a UL-listed assembly).
- Warranty article absent on a section that the spec elsewhere claims has an extended warranty (e.g., roofing).
- "TBD" or "to be determined" placeholder language at 95% CD.

**Example finding:**

> Section 07 54 23 (TPO roof membrane) Part 1.08: "Provide manufacturer's standard warranty." Section 07 50 00 Part 1.04 General Requirements states "Provide 20-year manufacturer's NDL warranty for membrane roofing." The general statement should be repeated specifically in 07 54 23.1.08 or cross-referenced explicitly. Also missing: warranty form to be included in submittals (per 07 54 23 Part 1.04).

---

## 8. OPR alignment

**Sub-criteria:**

- Performance criteria from the OPR (energy target, certification, acoustic, IAQ, embodied carbon, accessibility) actually land in the appropriate spec sections.
- Division 01 quality assurance / commissioning sections support the performance targets.
- Documentation requirements (LEED, WELL, Living Building, Passive House, RELi) match the certification target.

**Common failure modes:**

- OPR commits to LEED Gold; Division 01 quality assurance section says nothing about LEED documentation, commissioning, or LEED-specific submittals.
- OPR sets EUI ≤ 35 kBtu/sf/yr; HVAC sections (23 series) have no commissioning requirements.
- OPR sets embodied carbon target; concrete (03 30 00) has no low-carbon mix requirement, no EPD submittal.

**Example finding:**

> OPR §3.4 commits to "LEED v4.1 Gold target" and "fundamental commissioning per ASHRAE Guideline 0." Spec book has no Section 01 91 00 (Commissioning) or 01 81 13 (Sustainable Design Requirements). LEED EAp1 requires Cx; without the spec section, the contractor will not bid the Cx scope. Recommend adding 01 91 00 and 01 81 13 to the 95% CD set.
