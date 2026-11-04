---
title: Draft Spec Snippet
summary: Write a product paragraph for a spec section
discipline: construction-admin
tags: ["Design", "Document Generation"]
description: Draft a CSI MasterFormat 2020 Part 2 (Products) paragraph for a single product within a spec section. Use /explain-spec to interpret an existing CSI section; use the spec-review skill for full-spec audit; use /draft-callout for drawing-side product references.
argument-hint: <csi-section-and-product>
---

# Draft Spec Snippet

Draft a single Part 2 (Products) paragraph for a CSI-format specification section, following CSI MasterFormat 2020 numbering and SectionFormat 3-Part structure (Part 1 General / Part 2 Products / Part 3 Execution). Output is a Markdown excerpt the user pastes into the project specification book — Part 2 only, with explicit notes on what the user must still write in Part 1 and Part 3.

For full-spec authoring use the `spec-review` skill. For Part 1 General language (submittals, references, quality assurance), most firms have boilerplate — this command does **not** draft Part 1.

## Input you need

Before drafting, gather:

1. **CSI section number and title** — six-digit MasterFormat 2020 (e.g., `08 71 00 — Door Hardware`, `09 30 13 — Ceramic Tiling`, `23 36 00 — Air Terminal Units`).
2. **Product / system** — what is being specified (e.g., "VAV box with hot-water reheat", "porcelain floor tile", "mortise lockset").
3. **Basis-of-Design (BOD) manufacturer + model** — e.g., `Trane VariTrane VCWF`, `Daltile Identity ID01 12x24`, `Schlage L9080P-06A`.
4. **Spec phase** — `SD` (outline spec, performance only), `DD` (mid-spec, BOD identified), `CD` (final spec, prescriptive + performance), `Permit` / `Bid` (locked).
5. **Approach** — `Prescriptive` (manufacturer + model named, alternates restricted), `Performance` (criteria only, multiple manufacturers acceptable), or `Hybrid` (BOD named with "or approved equal").
6. **Alternates language** — one of:
   - `Open` — "or approved equal" (any manufacturer meeting criteria)
   - `Restricted` — list of pre-approved alternates (e.g., "Trane, Carrier, Daikin acceptable")
   - `Sole source` — single manufacturer only (requires Owner authorization, public-bid-law impact)
7. **Key performance criteria** — what the product must do (e.g., for a VAV box: airflow range, sound level NC, minimum turndown ratio; for tile: PEI rating, DCOF wet, water absorption).

If any of the above is missing or ambiguous, ask the user before drafting. Do not invent manufacturer model numbers, performance values, or alternate manufacturer names.

## Output template

```markdown
# Spec Snippet — [CSI Section # — Title]

**CSI MasterFormat 2020**
**Phase:** [SD / DD / CD / Permit / Bid]
**Approach:** [Prescriptive / Performance / Hybrid]
**Alternates:** [Open / Restricted / Sole source]

---

## PART 2 — PRODUCTS

### 2.0X [PRODUCT NAME — e.g., AIR TERMINAL UNITS, VARIABLE AIR VOLUME]

#### A. Manufacturers

[Choose the alternates language matching the user's selection:]

**Open (BOD + or approved equal):**
> 1. Basis-of-Design: [Manufacturer], [Model], or approved equal.
> 2. Substitution requests shall comply with Section 01 25 00.

**Restricted (named alternates):**
> 1. Basis-of-Design: [Manufacturer], [Model].
> 2. Acceptable alternates, subject to compliance with the performance criteria of this Section: [Alt 1], [Alt 2], [Alt 3].
> 3. Substitution requests shall comply with Section 01 25 00.

**Sole source (single manufacturer):**
> 1. Sole source: [Manufacturer], [Model]. No substitutions.
> 2. Sole-source designation is authorized by the Owner; refer to Section 01 25 00.

#### B. Performance Criteria

> 1. [Criterion 1] — [value, range, or test method reference]
> 2. [Criterion 2] — [value, range, or test method reference]
> 3. [Criterion 3] — [value, range, or test method reference]

> *Replace bracketed values with project-specific performance data. Do not retain example values without verifying against the BOD manufacturer's published cut-sheet.*

#### C. Configuration

> 1. [Size / capacity / arrangement clause — project-specific]
> 2. [Accessory clause — controls, finishes, options]

---

## What you still need to write

This command drafts **Part 2 / [section #]** only. The full spec section requires:

- **Part 1 — General** — submittals (per `01 33 00`), references (ASTM / ANSI / UL standards cited), quality assurance, delivery, warranty. Most firms have boilerplate.
- **Part 3 — Execution** — examination, preparation, installation tolerances, field quality control, cleaning. Coordinate with manufacturer's printed installation instructions.
- **Cross-references**:
  - Drawing references (sheet # / detail #) where this product appears.
  - Other spec sections this section depends on (`07 92 00` Joint Sealants, `08 71 00` Door Hardware, etc.).
  - Schedule entries (Door / Window / Equipment / Finish Schedule).
```

## Workflow

1. Echo back: CSI section #, product, BOD manufacturer + model, phase, approach, alternates language. One line.
2. If any required input is missing — especially BOD model and performance criteria — list the gap and stop. Do not draft a Part 2 paragraph with placeholder values masquerading as real ones.
3. If the user wants verbatim manufacturer cut-sheet language (proprietary spec language directly from the manufacturer's published spec), ask them to paste from the cut-sheet — do **not** quote manufacturer cut-sheet text from training.
4. If the user wants verbatim CSI SectionFormat structural language (the canonical Part 1 / Part 2 / Part 3 article headers), ask them to consult the CSI Project Resource Manual — do **not** reproduce CSI proprietary outlines from training.
5. Produce the Part 2 snippet with the alternates language matching the user's selection.
6. List the cross-references and the Part 1 / Part 3 work the user must still write.
7. Flag the alternates-language consequence: `Open` shifts review burden to the AOR (each substitution request must be evaluated); `Sole source` requires Owner authorization and may have public-bid-law impact (state-specific — DSA / NYC DDC / GSA / USACE all have different rules).

## NA AEC conventions

- **English only.** No Hangul.
- **Imperial-first** units (`in`, `ft`, `sf`, `lb`, `°F`, `R-value`, `Btu`, `cfm`, `gpm`); metric in parens only when useful.
- **CSI section number format** — six-digit MasterFormat 2020 with single spaces (`09 30 13`, not `093013`).
- **CSI 3-Part structure** — Part 1 General, Part 2 Products, Part 3 Execution. Article numbers `1.01 / 1.02 / 2.01 / 2.02 / 3.01 / 3.02`.
- **All-caps** for article and paragraph titles (CSI convention). Sentence case for body.
- **References** — name the standard (`ANSI A137.1`, `UL 263`, `NFPA 80`); do not invent. NA standards only — no `EN`, `BS`, `JIS`, `KS`.
- **Performance values** — quote the BOD manufacturer's published value with units. Do not invent.
- **Roles** — `AOR`, `Owner`, `CM`, `MEP Engineer`, `SE`, `GC`. Never `Director` as a project role.
- **Floor labels** — `Level 3`, `L3`, or `3rd floor`. Never `3F`.

## Constraints

- This command drafts **Part 2 / one product** only. Not Part 1, not Part 3, not the full section.
- Do not invent manufacturer model numbers. The BOD model is owned by the user.
- Do not invent performance values (e.g., NC rating, PEI rating, DCOF, R-value). Quote the manufacturer's published cut-sheet, supplied by the user.
- Do not quote CSI SectionFormat / Project Resource Manual verbatim from training. CSI documents are member / paid resources.
- Do not quote ASTM / ANSI / UL / NFPA test-method language verbatim. Cite the standard number; the user pastes the test-method language if needed.
- Sole-source designation is **always** flagged with the Owner-authorization caveat and the public-bid-law caveat.
- "Or approved equal" is **always** paired with a Section 01 25 00 (Substitution Procedures) reference.

## Anti-patterns

- Drafting Part 1 boilerplate. Out of scope. Most firms own Part 1 templates.
- Inventing model numbers (`Trane VCWF-12-XYZ`) without the user supplying them.
- Inventing performance values (`NC 25`, `PEI 4`) without the user supplying them or pasting a cut-sheet.
- Quoting CSI SectionFormat article structure verbatim from training. CSI is a paid resource — confirm against the user's copy.
- "Or approved equal" without flagging the Section 01 25 00 review burden on AOR.
- Sole-source designation without flagging Owner authorization + public-bid-law impact (DSA / NYC DDC / GSA / USACE rules differ).
- Mixing Part 1 / Part 3 content into Part 2 (e.g., installation tolerances belong in Part 3, not Part 2 Configuration).
- Using `Director` as a role.
