# Provenance — Drawing Checklist References

## What this skill is — and is not

The drawing-checklist skill is a **practice guide**, not a contractual specification. It generates phase-specific drawing-set checklists (SD / DD / CD / IFC) by synthesizing common North American AEC office practice. Most checklist items are derived from common-practice convention, not direct quotation of any single published authority.

When an item directly maps to AIA B101-2017 phase definitions, NCS v6 sheet conventions, or another named authority, it should be marked with a section pin. Where no clean authority exists (e.g. specific percent-complete ranges, the 100-item coordination list), the item is labeled office convention and the user is told to verify against their firm's BIM execution plan and the project-specific contract.

This is the asymmetric mitigation called for by the standards-verification rule (memory: `feedback_standards_verification.md`). Row-by-row mapping to AIA B101 / NCS v6 is the eventual goal; this provenance file tracks current status.

## Primary sources

**AIA B101-2017 — Standard Form of Agreement Between Owner and Architect**
- Publisher: American Institute of Architects
- Edition: **2017** (current; next major AIA contract revision expected ~2027)
- Public information: https://www.aiacontracts.com
- Sections relevant to phase definitions:
  - §3.2 Schematic Design Phase Services
  - §3.3 Design Development Phase Services
  - §3.4 Construction Documents Phase Services
  - §3.5 Bidding or Negotiation Phase Services
  - §3.6 Construction Phase Services
- Note: AIA B101 defines the **scope of services** at each phase but does **not** mandate specific percent-complete values, sheet types, or sheet content. Office-convention percentages (SD ~15-30%, DD ~35-50%, CD 100%) are industry shorthand, not B101 requirements.

**US National CAD Standard (NCS) v6**
- Publisher: National Institute of Building Sciences (NIBS), in coordination with AIA + CSI
- Edition: **v6** (current as of 2026-05-09)
- Public information: https://www.nationalcadstandard.org
- Module 2 — Uniform Drawing System (UDS): sheet identification (discipline designator + sheet-type digit + sheet sequence), sheet organization, drawing set organization
- Module 3 — Plotting Guidelines, Module 4 — CAD Layer Guidelines: not bundled; out of this checklist's scope

**AIA Best Practices**
- Publisher: AIA
- Public information: https://www.aia.org/practicing-architecture/best-practices
- Topical guidance referenced where coordination items align (drawing coordination, QA/QC, phase deliverables). Best Practices guidance is advisory, not contractual.

**MEP / structural coordination references** (cited where coordination items align)
- AISC 303 — Code of Standard Practice for Steel Buildings and Bridges (American Institute of Steel Construction)
- ASHRAE Handbook — HVAC Applications / HVAC Systems and Equipment
- ASCE 7 — Minimum Design Loads (referenced for roof-equipment loads, parapets, structural-architectural interface)
- General MEP coordination guides (firm- and project-specific BIM execution plans)

## Coverage of this skill

| Reference file | Covers | Source basis |
|----------------|--------|--------------|
| `phase_deliverables.md` | Per-phase intent, typical sheets, level of detail, owner deliverable | AIA B101-2017 §3.2 / §3.3 / §3.4 / §3.5 phase scopes; specific percent-complete values and sheet enumerations are office convention |
| `sheet_types.md` | Per-phase content expectations by sheet series (G / A-0 / A-1 / ... / A-9) | NCS v6 Module 2 sheet identification; per-phase content lists are office convention |
| `coordination_flags.md` | 100-item architectural ↔ structural and architectural ↔ MEP coordination list | Synthesis of common AEC coordination practice; AIA Best Practices, AISC 303, ASHRAE, ASCE 7 — **no single published authority** |
| `assets/checklist-template.md` | Markdown template for the generated checklist | Office convention |

## Verification status

- **Last verified against AIA B101-2017 + NCS v6**: 2026-05-09
- **Status**: Phase intents map cleanly to AIA B101-2017 §3.2-§3.5 phase descriptions. Sheet-series naming maps cleanly to NCS v6 Module 2. **Per-item content lists, percent-complete ranges, and the 100-item coordination list are NOT directly quoted** from any authority and are labeled office convention or marked `[verify B101-2017 §X.X]` where the exact section pin is not yet confirmed.
- **Eventual goal**: Row-by-row mapping of every checklist item to AIA B101-2017 / NCS v6 / AIA Best Practices section pins, with `[verify]` flags retired as each row is confirmed.

## Out of bundled scope (refer to authoritative sources)

- **Verbatim AIA B101 / A201 contract text** — AIA contracts are copyrighted; this skill paraphrases scope at section level, not full clauses. The user's project-specific B101 governs.
- **Verbatim NCS v6 specification** — NCS v6 is licensed by NIBS; only sheet-identification conventions (discipline + sheet-type digit) are referenced. Full layer / line / hatch standards are not bundled.
- **Office / firm CAD or BIM standards** — every firm has internal standards that may amend or override NCS v6. The checklist must be reconciled against the project's BIM execution plan.
- **Project-specific contracts** — owner-architect contracts (B101, B102, B103, custom) may redefine phase percent-complete thresholds, deliverable lists, or issue-set conventions. Contract language overrides this checklist.
- **Non-NA drawing standards** (BS 1192, ISO 19650, EU CAD conventions) — NA AEC focus only.
- **Full discipline checklists for structural / MEP / civil / landscape** — this skill's coordination flags cover the architectural interface only. Full per-discipline checklists are out of scope.

## How to verify

1. Compare phase intents in `phase_deliverables.md` against AIA B101-2017 §3.2-§3.5. Phase percent-complete values are NOT in B101 — confirm office-convention status.
2. Compare sheet-series naming in `sheet_types.md` against NCS v6 Module 2 (Uniform Drawing System).
3. Compare coordination items in `coordination_flags.md` against AIA Best Practices and the project's BIM execution plan. Expect deltas — the 100-item list is a synthesis, not a published checklist.
4. For each `[verify B101-2017 §X.X]` flag, look up the exact section in the project's B101 and replace the flag with the confirmed citation.
5. If conventions differ, file an issue against `archtmpl`.

## Version pin warning

AIA contract documents and NCS publish on multi-year cycles. Re-verify when:
- AIA publishes B101-2024 / B101-2027 (next major revision expected ~2027),
- NIBS publishes NCS v7,
- AIA revises Best Practices guidance affecting drawing-set conventions,
- A jurisdiction (e.g. NYC DOB, NYC SCA, CA HCAI, DSA, GSA) publishes a CAD/BIM standard that amends NCS v6 for that AHJ.

Update the **Last verified** date above on each verification. That date is the record. This line used to name a `Version` and a `Last Verified` property in a Notion database; that database was removed on 2026-07-28 and this file is now the only place the date lives.
