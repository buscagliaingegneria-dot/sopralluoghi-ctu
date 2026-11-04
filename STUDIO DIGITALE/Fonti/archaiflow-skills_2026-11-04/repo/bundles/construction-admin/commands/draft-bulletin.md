---
title: Draft Bulletin
summary: Write a cover letter for a bulletin or addendum
discipline: construction-admin
tags: ["Construction Admin", "Document Generation", "AIA A201"]
description: Draft a CD-set bulletin or pre-bid addendum cover letter for distribution to bidders, GC, or AHJ. Use /draft-asi for in-CA architect's instructions; use /draft-ccd for changes affecting Contract Sum or Time. Bulletin = CA-phase modification; Addendum = bid-phase pre-execution document (per AIA A201 §1.1.1).
argument-hint: <bulletin-or-addendum-number>
---

# Draft Bulletin

Draft the cover letter that accompanies a CD-set Bulletin (CA phase, modifies executed Contract Documents) or a pre-bid Addendum (bid phase, becomes part of the Contract Documents per AIA A201-2017 §1.1.1). Output is Markdown ready to paste into Word / email or render to PDF for plan-set distribution.

The two are distinct under A201 — confirm phase before drafting.

## Input you need

Before drafting, gather:

1. **Project name** and **project number**.
2. **Phase** — `Addendum` (pre-bid, before Contract execution) **or** `Bulletin` (CA phase, after Contract execution). The cover language differs.
3. **Bulletin / Addendum number** — sequential within the phase log (e.g., `Addendum 03`, `Bulletin 07`).
4. **Date** in `Month DD, YYYY`.
5. **Issued by** — AOR firm + PIC name.
6. **Distribution** — bidders list (addendum) or contract parties (bulletin).
7. **Sheets / specs revised** — sheet numbers (with new revision tag), spec sections (with revision date).
8. **Description of changes** — concise change-by-change list.
9. **Reference documents** — drawings, sketches (SK-##), spec excerpts, prior RFI numbers, prior ASI / Bulletin numbers being superseded.
10. **Response deadline** — only for addenda (bidders' question cutoff or bid-revision deadline) or RFI-driven bulletins; otherwise `N/A`.

If any of the above is missing or ambiguous, ask the user before drafting. Do not invent sheet numbers, revision tags, or RFI numbers.

## Output template

```markdown
# [Bulletin | Addendum] No. XX — [Project Name]

**Project:** [Name] (Project No. [######])
**Document Type:** [Bulletin (CA-phase modification) | Addendum (pre-bid)]
**No.:** [Bulletin XX | Addendum XX]
**Date:** [Month DD, YYYY]
**Issued by:** [Firm], by [PIC name, AIA]
**Distribution:** [list — bidders for Addendum / Owner + GC + Subs for Bulletin]

---

[Choose one cover paragraph based on phase:]

**For Addendum (pre-bid):**
> This Addendum forms part of the Contract Documents and modifies the original Bidding Documents dated [Month DD, YYYY]. Acknowledge receipt of this Addendum in the space provided on the Bid Form. Failure to do so may subject the Bidder to disqualification.
>
> *Reference: AIA A201-2017 §1.1.1 (Addenda issued prior to execution of the Contract are part of the Contract Documents). Verbatim contract clause text is not reproduced here — confirm against the project A201.*

**For Bulletin (CA-phase):**
> This Bulletin issues a Modification to the Contract Documents pursuant to AIA A201-2017 §1.1.1. The Contractor shall incorporate the revisions described herein into the Work. Any change in Contract Sum or Contract Time arising from this Bulletin shall be processed via Construction Change Directive (G714) or Change Order (G701) as applicable.
>
> *Reference: AIA A201-2017 §1.1.1 (Modifications). Verbatim contract clause text is not reproduced here — confirm against the executed A201.*

---

## Description of Revisions

| # | Sheet / Spec § | Brief Description | Reason |
|---|----------------|-------------------|--------|
| 1 | A-301 Rev 4 | Revised slab depression detail at typical bathroom | RFI-038 response |
| 2 | 09 30 13 §2.02 | Tile thinset thickness range tightened | Coordination w/ Sheet A-301 |
| 3 | M-201 Rev 3 | Added VAV box at Room 312 | Owner program change |

## Reference Documents

- SK-A-018 — Revised slab depression detail (1 sheet, dated [Month DD, YYYY])
- RFI-038 — Slab levelness at bathrooms (response dated [Month DD, YYYY])
- Bulletin 05 — Superseded by this Bulletin item #2

## Response Required

[Bidders / Contractor] shall acknowledge receipt by [Month DD, YYYY] and submit any questions arising from this [Addendum / Bulletin] by [Month DD, YYYY] or `N/A` if not applicable.

---

**Issued by:** [PIC name, AIA, Firm]
**Date:** [Month DD, YYYY]
```

## Workflow

1. Confirm phase: **Addendum (pre-bid)** or **Bulletin (CA)**. The cover paragraph differs and the consequence under A201 §1.1.1 differs — do not conflate.
2. Echo back: project, document type + number, sheet/spec count, distribution scope. One line.
3. If any required input is missing, list the gap and stop.
4. If the user wants verbatim AIA A201 §1.1.1 text embedded (rather than the short reference shown), ask them to paste from the executed A201 or project Bidding Documents. Do **not** quote A201 from training. Optional WebFetch from `https://www.aiacontracts.com/` if the user authorizes (paywalled — paste is the realistic path).
5. If any item supersedes a prior Bulletin / Addendum / ASI, list the superseded number explicitly in the Reference Documents section.
6. Produce the full Bulletin / Addendum cover Markdown.
7. After the draft, remind the user to update the Bulletin / Addendum log and to issue the actual revised drawings / spec pages alongside this cover.

## NA AEC conventions

- **English only.** No Hangul.
- **Imperial-first** units (`ft`, `in`, `sf`); metric in parens only when useful.
- **Dates** use `Month DD, YYYY`.
- **Sheet revision tags** — match the project's revision log convention (e.g., `Rev 3`, `R3`, `Δ3`). Default to `Rev N` if user does not specify.
- **Roles** — `AOR`, `Owner`, `CM`, `MEP Engineer`, `SE`, `GC`. Never `Director` as a project role.
- **Firms** — full legal name on first reference.
- **AIA references** — `AIA A201-2017 §1.1.1` (Contract Documents, including Modifications and Addenda), `AIA G714-2017` (CCD downstream), `AIA G701-2017` (Change Order downstream).
- **AHJs** — name specifically when issuing a bulletin tied to plan-check response (`NYC DOB`, `LADBS`, `CA DSA`, `CA HCAI`, `FDNY`).
- **Floor labels** — `Level 3`, `L3`, or `3rd floor`. Never `3F`.

## Constraints

- **Phase is required.** Addendum and Bulletin are categorically distinct under A201 §1.1.1. The cover paragraph and distribution differ.
- Do not fabricate sheet numbers, revision tags, RFI numbers, or superseded Bulletin / ASI numbers.
- Do not reproduce AIA A201 §1.1.1 verbatim text from training.
- This command produces only the **cover letter**. The revised sheets and spec pages are separate deliverables — remind the user.
- For Bulletins that affect Contract Sum or Contract Time, the user must also issue a CCD (`/draft-ccd`) or Change Order (G701). Note this in the Reference Documents section.
- Do not promise approval timelines for Addenda — bid-phase questions and bidder acknowledgement deadlines belong to the Owner / Procurement Officer, not the AOR.

## Anti-patterns

- Conflating Addendum and Bulletin. Addendum = pre-bid, becomes Contract Doc on execution. Bulletin = post-execution Modification.
- Quoting AIA A201 §1.1.1 verbatim from training. User pastes.
- Drafting a Bulletin cover that affects Contract Sum / Time without flagging that a CCD or Change Order must follow.
- Inventing a superseded prior Bulletin / ASI number. The Bulletin log is the source of truth.
- Treating the cover letter as the deliverable. The revised sheets / specs are the actual document — the cover is transmittal language only.
- Using `Director` as a role.
