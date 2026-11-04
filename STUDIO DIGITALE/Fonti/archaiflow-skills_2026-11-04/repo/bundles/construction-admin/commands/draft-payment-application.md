---
title: Draft Payment Application
summary: Draft a contractor payment application
discipline: construction-admin
tags: ["Construction Admin", "AIA G702", "AIA G703"]
description: Draft a contractor payment application (AIA G702 cover + G703 continuation, Excel default)
argument-hint: <period-ending-date-or-app-number>
---

# Draft Payment Application

Draft a contractor's Application and Certificate for Payment per AIA G702 (cover) and G703 (continuation sheet). Output is Markdown that renders to Excel so retainage, prior-period totals, and current-period billing arithmetic flow automatically.

## Input you need

Before drafting, gather:

- **Project name** and **project number**.
- **Application number** — sequential, monthly (e.g., `Pay App #08`).
- **Period to** date in `Month DD, YYYY`.
- **Distribution to** — Owner, Architect.
- **Contractor** — full legal name.
- **Owner** — full legal name.
- **Architect** — AOR firm.
- **Original contract sum**, **net change by Change Orders to date**, **current contract sum**.
- **Schedule of Values (SOV)** — list of line items, each with:
  - Item No.
  - Description (CSI division / system / sub-trade)
  - CSI number (e.g., `03 30 00`)
  - Scheduled value (USD)
  - Work completed from previous applications (USD)
  - Work completed this period (USD)
  - Materials presently stored (not in D or E) (USD)
  - Total completed and stored to date
  - % complete
  - Balance to finish
  - Retainage (USD)
- **Retainage rate** — e.g., `5%` or `10% reduced to 5% at 50% completion`.

If any of the above is missing or ambiguous, ask the user before drafting. Do not invent line items or dollar amounts.

## Output structure

```markdown
# Application and Certificate for Payment — App. No. XX

**Project:** [Name] (Project No. [######])
**Application No.:** XX
**Period to:** [Month DD, YYYY]
**Contractor:** [Full legal name]
**Owner:** [Full legal name]
**Architect:** [Firm — AOR]
**Per:** AIA G702 / G703, AIA A201 §9.3

---

## G702 — Application Summary

| Line | Amount (USD) |
|------|--------------|
| 1. Original Contract Sum | $X,XXX,XXX.XX |
| 2. Net change by Change Orders | $X,XXX.XX |
| 3. Contract Sum to date (Line 1 + Line 2) | $X,XXX,XXX.XX |
| 4. Total completed and stored to date (G703 Column G total) | $X,XXX,XXX.XX |
| 5. Retainage |  |
|     a. X% of completed work (G703 Columns D + E) | $XX,XXX.XX |
|     b. X% of stored material (G703 Column F) | $X,XXX.XX |
|     **Total Retainage (Line 5a + 5b)** | **$XX,XXX.XX** |
| 6. Total earned less Retainage (Line 4 − Line 5 Total) | $X,XXX,XXX.XX |
| 7. Less previous Certificates for Payment (Line 6 from prior application) | $X,XXX,XXX.XX |
| **8. Current Payment Due** | **$XXX,XXX.XX** |
| 9. Balance to finish, including Retainage (Line 3 − Line 6) | $XX,XXX.XX |

---

## G703 — Continuation Sheet (Schedule of Values)

| Item No. | Description | CSI | A. Scheduled Value | B. Prior Work Completed | C. This Period | D. Materials Stored | E. Total to Date (B+C+D) | F. % (E÷A) | G. Balance to Finish (A−E) | H. Retainage |
|----------|-------------|-----|--------------------|--------------------------|----------------|----------------------|----------------------------|------------|----------------------------|-------------|
| 1 | Concrete | 03 30 00 | $XXX,XXX | $XXX,XXX | $X,XXX | $0 | $XXX,XXX | XX% | $X,XXX | $X,XXX |
| 2 | Masonry | 04 20 00 | $XXX,XXX | ... | ... | ... | ... | ... | ... | ... |
| ... | | | | | | | | | | |
| **Totals** | | | $X,XXX,XXX | $X,XXX,XXX | $XX,XXX | $X,XXX | $X,XXX,XXX | XX% | $XX,XXX | $XX,XXX |

---

## Contractor's Certification

The undersigned Contractor certifies that to the best of the Contractor's knowledge, information, and belief the Work covered by this Application for Payment has been completed in accordance with the Contract Documents, that all amounts have been paid by the Contractor for Work for which previous Certificates for Payment were issued and payments received from the Owner, and that current payment shown herein is now due.

**By:** _______________________  **Date:** _______________________
**State of:** _______  **County of:** _______
Subscribed and sworn to before me this ___ day of ____________, [YYYY].
Notary Public: _______________________  My Commission expires: _______________________

## Architect's Certificate for Payment

In accordance with the Contract Documents, based on on-site observations and the data comprising this application, the Architect certifies to the Owner that to the best of the Architect's knowledge, information, and belief the Work has progressed as indicated, the quality of the Work is in accordance with the Contract Documents, and the Contractor is entitled to payment of the AMOUNT CERTIFIED.

**Amount Certified:** $XXX,XXX.XX (attach explanation if amount differs from amount applied)
**By Architect:** _______________________  **Date:** _______________________
```

## NA AEC conventions

- **English only.** No Hangul.
- **Currency** — USD with `$` prefix and two decimal places (e.g., `$12,345.67`).
- **Imperial-first** units in any descriptive line items.
- **Dates** use `Month DD, YYYY`.
- **Roles** — `Contractor`, `Owner`, `Architect of Record (AOR)`. Never `Director` as a project role.
- **CSI references** — 6-digit MasterFormat numbers (e.g., `03 30 00` Cast-in-Place Concrete, `04 20 00` Unit Masonry, `09 51 00` Acoustical Ceilings). Use spaces between digit-pairs, not dashes.
- **AIA references** — `AIA G702`, `AIA G703`, `AIA A201 §9.3` (Applications for Payment).
- **Retainage** — typical 10% reduced to 5% at 50% completion, or per contract. State the rate explicitly in the table caption.

## Constraints

- Do not fabricate line items, dollar amounts, or CSI numbers. If a line item lacks one of A–H, mark `TBD` literally and stop.
- All G702 lines must arithmetically reconcile (Line 3 = Line 1 + Line 2; Line 6 = Line 4 − Line 5; Line 8 = Line 6 − Line 7; Line 9 = Line 3 − Line 6). If the user's numbers do not reconcile, surface the discrepancy and stop.
- All G703 row totals must reconcile (E = B + C + D; F = E ÷ A; G = A − E). If they do not, flag and stop.
- The Contractor's Certification and Architect's Certificate boilerplate is required by AIA — do not modify or omit.
- Excel output requires the `aec-doc-gen` companion skill. If unavailable, output Markdown and instruct the user to install via the catalog.
- The amount the Architect certifies (line at the bottom) may differ from the amount the Contractor applied for. If the user has not specified a certified amount, default to the Contractor's applied amount and flag this for AOR review.

## Workflow

1. Echo back: project, app number, period ending, line item count, current payment due. One line.
2. If any required input is missing, list the gap and stop.
3. Verify all G702 and G703 arithmetic. If anything fails to reconcile, surface and stop.
4. Otherwise, produce the full payment application Markdown.
5. If Excel output was asked for, hand the Markdown to the `aec-doc-gen` skill and ask it for `.xlsx`. The summary and the schedule of values are separate tables, so they land on separate sheets.
6. After the draft, remind the user that the application requires Contractor notarization and Architect certification before submission to Owner.
