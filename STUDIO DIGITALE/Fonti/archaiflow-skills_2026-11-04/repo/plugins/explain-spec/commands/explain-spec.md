---
title: Explain Spec
summary: Explain a specification section in plain English
discipline: construction-admin
tags: ["Construction Admin", "Construction"]
description: Interpret a CSI MasterFormat specification section in plain English (Part 1/2/3 breakdown, NA conventions)
argument-hint: <csi-section-or-product>
---

# Explain Spec

Interpret a CSI MasterFormat 2020 specification section in plain English, broken down by SectionFormat Part 1 (General) / Part 2 (Products) / Part 3 (Execution). Output is an inline explanation with verbatim §-citation. For a full spec audit (division completeness, drawing-spec coordination, reference-standard currency), use the `spec-review` skill instead.

## Input you need

Before interpreting, gather:

- **Spec section number and title** — CSI MasterFormat 2020 format: `XX YY ZZ — Title`. Examples: `07 27 26 — Fluid-Applied Membrane Air Barriers`, `08 11 13 — Hollow Metal Doors and Frames`, `09 30 13 — Ceramic Tiling`. Six digits with single spaces (no periods, no dashes between digit groups).
- **Section text** — the user must provide either:
  - A paste of the specific Part 1 / Part 2 / Part 3 article(s) the question is about (e.g., Part 2.04 Products — Acceptable Manufacturers), OR
  - The PDF path so the `Read` tool can pull the section.
  - Do not invent product names, manufacturer lists, reference standards, or installation requirements.
- **Spec format** — `MasterSpec` (AIA) / `ARCAT` / `SpecLink+` / `4specs` / project-custom. MasterSpec sections have specific Part 1 / Part 2 / Part 3 conventions; custom sections may not.
- **Issue / phase** — `IFB` (Issued for Bid) / `100% CD` / `IFC` (Issued for Construction) / `addendum` / `clarification`. Affects whether contractors are bound by the language.
- **AIA / contract context** — `AIA A201 §3.12.6` (Submittal review), `AIA A201 §1.2.1` (Documents complement each other) — relevant for "if the spec says X but the drawing says Y" questions.
- **Specific question** — what the user wants to know. Examples: "Is this a basis-of-design or a substitution-allowed product?", "What's the warranty period for this finish?", "Is this single-source manufacturer language enforceable?", "What does 'comply with manufacturer's printed instructions' actually require?"

If any required input is missing, list the gap and stop. Do not interpret a spec section without seeing its actual text.

## Output structure

Produce a single Markdown response in this layout:

```markdown
# Explain Spec — [Section XX YY ZZ Title]

**Section:** [07 27 26 — Fluid-Applied Membrane Air Barriers]
**Spec format:** [MasterSpec / ARCAT / SpecLink+ / Custom]
**Issue:** [IFB / 100% CD / IFC / Addendum #X]
**Question:** [the user's specific question]

---

## Section role (in CSI MasterFormat 2020)

[1–2 sentences. Where this section sits in the MasterFormat hierarchy — division (e.g., Division 07 — Thermal & Moisture Protection), level 2 group (07 20 — Thermal Protection), level 3 (07 27 — Air Barriers). Why a project includes this section.]

## Part 1 — General

[2–4 sentences. Scope, references, submittals (per A201 §3.12), quality assurance, warranty. Quote the specific articles relevant to the user's question.]

> [verbatim quote of the relevant Part 1 article — e.g., 1.04.A.1]

— [Section XX YY ZZ §1.04.A.1]

## Part 2 — Products

[2–4 sentences. Basis-of-design (BOD), acceptable manufacturers, performance criteria, accessories. Distinguish "single-source" / "BOD-with-substitution" / "or-equal" / "open spec" — these have different procurement implications.]

> [verbatim quote of the relevant Part 2 article — e.g., 2.04.A]

— [Section XX YY ZZ §2.04.A]

## Part 3 — Execution

[2–4 sentences. Examination, preparation, installation, field QC, protection. Quote any "comply with manufacturer's instructions" or "as recommended by manufacturer" language — these create indirect submittal requirements.]

> [verbatim quote of the relevant Part 3 article — e.g., 3.05.B]

— [Section XX YY ZZ §3.05.B]

## Plain-English meaning

[3–5 sentences. What the section actually requires of the contractor, the architect, and the manufacturer. Distinguish prescriptive (specific product / brand / SKU) from performance (criteria the contractor's submittal must meet) language.]

## Coordination with the drawings

- [Bullet — drawings that reference this section (e.g., "Wall types W1, W2, W3 on A-101 reference §07 27 26"). Per AIA A201 §1.2.1, drawings and specs are complementary — flag any conflict the user should resolve via RFI.]
- [Bullet — adjacent specs this section depends on (e.g., "§07 27 26 references §07 21 00 for insulation that backs the air barrier").]

## Caveats

- This interpretation is based **only** on the spec text the user provided or that was retrieved verbatim. Cross-referenced articles, addenda, and reference standards (ASTM, ANSI, UL) that were not pulled may change the meaning.
- For binding interpretation on an `IFC` spec, the AOR's RFI response governs — not this command. Open an RFI via the `rfi-writer` skill if the spec language is ambiguous.
- Single-source / sole-source language requires owner-approved sole-source justification on public projects (federal, GSA, USACE, state DGS, NYC SCA). Flag this if visible.
- [Bullet — reference-standard currency: e.g., "§1.03 cites ASTM E2178-13 — current edition is ASTM E2178-21. Verify with `spec-review` skill before bid."]
```

## NA AEC conventions (enforce)

- **English only.** No Hangul anywhere.
- **Imperial-first** units (`ft`, `in`, `sf`, `psf`, `°F`, `Btu`, `R-value`); metric in parens only when useful. Use `R-value` for thermal performance, **not** metric U-values (`W/m²K`).
- **CSI section numbers** use MasterFormat 2020 convention: `XX YY ZZ` (six digits, single spaces, no periods, no dashes). Examples: `07 27 26`, `08 11 13`, `09 30 13`. **Never** `07.27.26` or `7-27-26`.
- **Article numbers** within a section use SectionFormat: `1.01`, `1.04.A.1`, `2.04`, `3.05.B`. Cite as `§1.04.A.1` with the section preface (e.g., `§07 27 26 §1.04.A.1`).
- **Reference standards** name a NA standards body: `ASTM`, `ANSI`, `UL`, `NFPA`, `ASHRAE`, `ICC-ES`, `AAMA`, `WDMA`, `SMACNA`, `SDI`, `NAAMM`. **Never** `BS`, `EN`, `JIS`, or generic "the standard".
- **Contract references** — `AIA A201 §1.2.1` (documents complement each other), `AIA A201 §3.12` (Submittals), `AIA B101 §3.4.5` (Architect's spec preparation), `CSI MasterFormat 2020`, `CSI SectionFormat / PageFormat 2020`.
- **AHJs** — name specifically (`NYC DOB`, `FDNY`, `LADBS`, `DSA`, `CA HCAI`, `GSA`, `USACE`, `NYC SCA`) when the question involves code-driven product requirements (e.g., NYC FDNY-listed materials, CA HCAI seismic anchorage). **Never** "the city" or "the AHJ" generically.
- **Roles** — `Architect of Record (AOR)`, `Engineer of Record (EOR)`, `Owner`, `Owner's Representative`, `General Contractor (GC)`, `Construction Manager (CM)`. **Never** "Director" as a project role.

## Constraints

- Do not invent product names, manufacturer lists, model numbers, or reference standard editions. If the user did not paste the section text, route through the `Read` tool first.
- Do not invent CSI section numbers. Cite only what appears in the user's input.
- Always quote verbatim from the spec for the article most relevant to the question — paraphrasing changes binding language.
- Distinguish prescriptive vs performance vs proprietary language clearly. These have different procurement and substitution implications under AIA A201 §3.4.2.
- This command coexists with the `spec-review` skill. If the user wants a full audit (Part 1/2/3 completeness, drawing-spec coordination, reference-standard currency, AHJ-specific references), redirect to `spec-review` rather than padding this command's output.
- Markdown only. This is an inline interpretation, not a transmittal document — no Word / PDF output and no `aec-doc-gen` dependency.

## Workflow

1. Echo back what was parsed: section #, format, issue, question. One line.
2. If the section text is missing, list the gap and stop. Suggest the `Read` tool as the retrieval path.
3. If the question implicates submittal review or substitution, surface the relevant `AIA A201 §3.12` / `§3.4.2` clause for the user's reference.
4. Produce the full Markdown response in one shot.
5. After the response, list any cross-referenced sections, addenda, or reference standards the user should pull next (e.g., "Section §07 21 00 (insulation) is referenced — pull that next via `explain-spec` if the air-barrier-to-insulation interface is the actual question").
