---
title: Draft ASI
summary: Instruct the contractor without changing cost or time
discipline: construction-admin
tags: ["Construction Admin", "Document Generation", "AIA A201"]
description: Draft an Architect's Supplemental Instruction (AIA G710-2017) for instructions with no change to Contract Sum or Contract Time. Use /draft-ccd for changes that DO affect cost/time; use /draft-bulletin for permit-set bulletin/addendum cover language.
argument-hint: <asi-number-or-subject>
---

# Draft ASI

Draft an Architect's Supplemental Instruction following AIA G710-2017 form conventions. ASI is the CA-phase instrument for clarifications and minor changes that do **not** alter Contract Sum or Contract Time, per AIA A201-2017 §7.4. Output is Markdown ready to paste into Word / email / Procore.

If the proposed instruction visibly changes scope, schedule, or cost, stop and route the user to `/draft-ccd` (which generates AIA G714-2017 — Construction Change Directive, A201 §7.3).

## Input you need

Before drafting, gather:

1. **Project name** and **project number**.
2. **ASI number** — sequential within the project (e.g., `ASI-014`).
3. **Date** in `Month DD, YYYY`.
4. **Architect** — firm of record (AOR) + responsible PIC.
5. **Owner** — legal name as written in the Owner-Contractor Agreement.
6. **Contractor** — legal name (GC / CM-at-Risk).
7. **Distribution** — Cc list (Owner, GC, CM, affected subs, Structural / MEP if drawing-driven).
8. **Affected drawings / specs** — sheet numbers and / or CSI section numbers the instruction modifies or clarifies.
9. **Instruction text** — what the AOR is directing. Concrete, with locations and dimensions.
10. **Attachments** — sketches (SK-##), revised details, marked-up plans, photos.
11. **Confirmation that no change to Contract Sum or Contract Time results** — required by A201 §7.4. If the user is unsure, surface the gap and offer `/draft-ccd` instead.

If any of the above is missing or ambiguous, ask the user before drafting. Do not invent drawing numbers, dimensions, sub names, or PIC names.

## Output template

```markdown
# Architect's Supplemental Instruction — ASI-XXX

**AIA Document G710-2017**

**Project:** [Name] (Project No. [######])
**Owner:** [Legal name]
**Architect:** [Firm], by [PIC name]
**Contractor:** [Legal name]
**ASI No.:** ASI-XXX
**Date:** [Month DD, YYYY]
**Distribution:** [Owner / Contractor / CM / Field / Consultants — list]

---

The Work shall be carried out in accordance with the following supplemental instructions issued in accordance with the Contract Documents without change in Contract Sum or Contract Time. Proceeding with the Work in accordance with these instructions indicates your acknowledgement that there will be no change in the Contract Sum or Contract Time.

> *Reference: AIA A201-2017 §7.4 (Minor Changes in the Work). The verbatim contract clause text is not reproduced here — confirm against your executed A201.*

---

## Description of Supplemental Instruction

[Plain-English directive. Concrete: location (grid, room #, sheet), dimensions, materials, tolerances. Reference the affected document by sheet # / spec § / detail #.]

## Affected Documents

| Doc type | Number / Section | Note |
|----------|------------------|------|
| Drawing | A-301 / Detail 4 | Slab depression revised — see SK-A-014 |
| Spec | 09 30 13 §2.02 | Tile thinset bed thickness clarified |

## Attachments

- SK-A-014 — Revised slab depression detail (1 sheet, dated [Month DD, YYYY])
- Photo log — Field condition at Grid B-3 (3 images)

---

**Issued by:** [PIC name, AIA, Firm]
**Date:** [Month DD, YYYY]
```

## Workflow

1. Echo back: project, ASI #, affected-doc count, attachment count, distribution count. One line.
2. Verify the user has confirmed **no change to Contract Sum or Contract Time**. If unconfirmed, ask. If the user indicates there IS a cost or time change, stop and route to `/draft-ccd`.
3. If any required input is missing, list the gap and stop.
4. If the user wants the verbatim AIA A201 §7.4 clause embedded (rather than the short reference shown above), ask them to paste from their executed A201 — do **not** quote A201 from training. Optionally offer to WebFetch from `https://www.aiacontracts.com/` if the user authorizes (note: largely paywalled — paste is the realistic path).
5. Produce the full ASI Markdown.
6. After the draft, list any items flagged for follow-up (TBD attachments, missing PIC, ambiguous distribution) so the user can resolve them before issuing.

## NA AEC conventions

- **English only.** No Hangul.
- **Imperial-first** units (`ft`, `in`, `sf`); metric in parens only when useful.
- **Dates** use `Month DD, YYYY`.
- **Roles** — `Architect of Record (AOR)`, `Owner`, `Construction Manager (CM)`, `MEP Engineer`, `Structural Engineer (SE)`, `General Contractor (GC)`. Never `Director` as a project role.
- **Firms** — full legal name on first reference.
- **AIA references** — `AIA G710-2017` (the form), `AIA A201-2017 §7.4` (Minor Changes in the Work).
- **Sketch numbering** — `SK-A-XXX` (architectural), `SK-S-XXX` (structural), `SK-M-XXX` (mechanical), etc.
- **Floor labels** — `Level 3`, `L3`, or `3rd floor`. Never `3F`.
- **AHJs** — name specifically when the instruction implicates code review (`NYC DOB`, `LADBS`, `CA DSA`, `CA HCAI`, `FDNY`).

## Constraints

- ASI is **only** for changes with no Contract Sum or Contract Time impact (A201 §7.4). Confirm before drafting.
- Do not fabricate sheet numbers, dimensions, sub names, or PIC names.
- Do not reproduce AIA A201 §7.4 verbatim text from training. If the user wants the clause embedded, they must paste it from their executed A201.
- Do not reproduce the AIA G710-2017 form layout pixel-for-pixel — the output is a Markdown record of the same fields, suitable for transcription into the official form.
- The instruction must be **directive** (not optional / not a question). RFIs ask; ASIs direct. If the user's text is interrogative, surface the gap and route to the `rfi-writer` skill.

## Anti-patterns

- Drafting an ASI for a change that obviously affects cost or time (new equipment, added scope, accelerated schedule). Route to `/draft-ccd`.
- Quoting AIA A201 §7.4 verbatim from memory. Even paraphrases that "everyone knows" must be confirmed against the user's executed A201.
- Inventing a sketch number (`SK-A-014`) without the user supplying it. The drawing log is the source of truth.
- Treating the ASI as a decision document. ASI is the AOR's instruction; the underlying decision lives in the design log / RFI response / meeting minutes.
- Adding a "Cost Impact" or "Schedule Impact" row. By definition (A201 §7.4), an ASI has neither — if the user wants those rows, they want a CCD.
- Using `Director` as a role. Use `PIC`, `Project Manager`, `Project Architect`, etc.
