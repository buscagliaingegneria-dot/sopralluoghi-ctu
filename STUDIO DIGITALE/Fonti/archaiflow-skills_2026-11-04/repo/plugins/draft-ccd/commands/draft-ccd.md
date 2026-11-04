---
title: Draft CCD
summary: Direct a change before cost and time are agreed
discipline: construction-admin
tags: ["Construction Admin", "Document Generation", "AIA A201", "AIA G701"]
description: Draft a Construction Change Directive (AIA G714-2017) for changes where Owner and Contractor have not agreed on Contract Sum or Contract Time. Use /draft-asi for instructions with NO change to Sum/Time; use AIA G701 Change Order once agreement is reached.
argument-hint: <ccd-number-or-subject>
---

# Draft CCD

Draft a Construction Change Directive following AIA G714-2017 form conventions. CCD is the CA-phase instrument when the Owner directs a change in scope **before** Owner and Contractor have agreed on the resulting adjustment to Contract Sum or Contract Time, per AIA A201-2017 §7.3. Output is Markdown ready to paste into Word / email / Procore.

If the parties **have** already agreed on price and time, route the user to a Change Order (AIA G701-2017). If the directive carries **no** change to Sum / Time, route to `/draft-asi`.

## Input you need

Before drafting, gather:

1. **Project name** and **project number**.
2. **CCD number** — sequential within the project (e.g., `CCD-007`).
3. **Date** in `Month DD, YYYY`.
4. **Owner** — legal name from the Owner-Contractor Agreement.
5. **Architect** — firm of record (AOR) + responsible PIC.
6. **Contractor** — legal name (GC / CM-at-Risk).
7. **Distribution** — Cc list.
8. **Description of change** — concrete scope language (added work, deleted work, substitutions, schedule acceleration).
9. **Method of payment** — required per A201 §7.3.4. One of:
   - Mutual acceptance of a lump sum
   - Unit prices stated in the Contract Documents or subsequently agreed
   - Cost to be determined in a manner agreed upon and a mutually acceptable fixed or percentage fee
   - As provided in §7.3.7 (cost determined by Architect on a reasonable basis if no agreement)
10. **Affected drawings / specs** — sheet numbers and / or CSI section numbers.
11. **Attachments** — revised details, narrative, take-off, vendor quotes (if available).
12. **Estimated cost / time impact** — even if not agreed, the Owner's expectation or AOR's order-of-magnitude estimate, marked TBD where not yet quantified.

If any of the above is missing or ambiguous, ask the user before drafting. Do not invent payment-method language, prices, or sub names.

## Output template

```markdown
# Construction Change Directive — CCD-XXX

**AIA Document G714-2017**

**Project:** [Name] (Project No. [######])
**Owner:** [Legal name]
**Architect:** [Firm], by [PIC name]
**Contractor:** [Legal name]
**CCD No.:** CCD-XXX
**Date:** [Month DD, YYYY]
**Distribution:** [Owner / Contractor / CM / Field / Consultants — list]

---

You are hereby directed to make the following change(s) in this Contract:

> *Reference: AIA A201-2017 §7.3 (Construction Change Directives). The verbatim contract clause text is not reproduced here — confirm against your executed A201.*

---

## Description of Change

[Concrete scope language. What is added / deleted / substituted. Locations (grid, room #, sheet). Dimensions, materials, equipment. Reference affected sheets and spec sections explicitly.]

## Affected Documents

| Doc type | Number / Section | Note |
|----------|------------------|------|
| Drawing | M-401 | New VAV box at Room 312 — see SK-M-007 |
| Spec | 23 36 00 §2.03 | VAV box manufacturer addition |

## Method of Adjustment to Contract Sum (per A201 §7.3.4)

[Choose one — match the user's selection verbatim:]

- [ ] Mutual acceptance of a lump sum properly itemized and supported by sufficient substantiating data to permit evaluation
- [ ] Unit prices stated in the Contract Documents or subsequently agreed upon
- [ ] Cost to be determined in a manner agreed upon by the parties and a mutually acceptable fixed or percentage fee
- [ ] As provided in §7.3.7 (cost determined by Architect on a reasonable basis if parties cannot agree)

**Estimated adjustment to Contract Sum:** [TBD / $X,XXX (estimate, not agreed) / no change]
**Estimated adjustment to Contract Time:** [TBD / X calendar days (estimate, not agreed) / no change]

## Attachments

- SK-M-007 — VAV box layout, Room 312 (1 sheet, dated [Month DD, YYYY])
- Vendor quote — [vendor name, dated [Month DD, YYYY]]

---

**Issued by:** [PIC name, AIA, Firm]
**Date:** [Month DD, YYYY]

**Owner authorization (required for issuance):**
Signed: ______________________________  Date: ______________
```

## Workflow

1. Echo back: project, CCD #, payment method chosen, affected-doc count, attachment count. One line.
2. Verify the user has selected one of the four §7.3.4 payment methods. If not, ask — this field is required by the form.
3. If the user indicates Owner and Contractor **have** agreed on price/time, stop and route to AIA G701 Change Order. If the user indicates **no** change to Sum / Time, stop and route to `/draft-asi`.
4. If any required input is missing, list the gap and stop.
5. If the user wants the verbatim AIA A201 §7.3 clause embedded, ask them to paste from their executed A201 — do **not** quote A201 from training. Optionally offer to WebFetch from `https://www.aiacontracts.com/` if the user authorizes (paywalled — paste is the realistic path).
6. Produce the full CCD Markdown.
7. After the draft, list any items flagged for follow-up (TBD cost / time, missing vendor quote, missing Owner authorization) so the user can resolve them before issuing.

## NA AEC conventions

- **English only.** No Hangul.
- **Imperial-first** units (`ft`, `in`, `sf`); metric in parens only when useful.
- **Dollar amounts** in USD. Round to dollars unless cents are contractually required.
- **Calendar days** vs **working days** — match the executed A201 (most use `calendar days`).
- **Dates** use `Month DD, YYYY`.
- **Roles** — `AOR`, `Owner`, `CM`, `MEP Engineer`, `SE`, `GC`. Never `Director` as a project role.
- **Firms** — full legal name on first reference.
- **AIA references** — `AIA G714-2017` (the form), `AIA A201-2017 §7.3` (Construction Change Directives), `AIA G701-2017` (Change Order — for the agreed-price downstream document).
- **Floor labels** — `Level 3`, `L3`, or `3rd floor`. Never `3F`.

## Constraints

- The §7.3.4 payment-method selection is **required**. CCD without a method is invalid.
- CCD requires Owner signature to issue (per the form). The output template includes the Owner authorization block — do not delete it.
- Do not fabricate prices, sub names, sheet numbers, or vendor quotes.
- Do not reproduce AIA A201 §7.3 verbatim text from training. User pastes if the verbatim clause is needed.
- Do not reproduce the AIA G714-2017 form layout pixel-for-pixel — Markdown is a record of the same fields.
- If the user provides a definitive cost and time agreed by both parties, this is no longer a CCD — it is a Change Order (G701). Stop and tell the user.

## Anti-patterns

- Drafting a CCD without naming the §7.3.4 method (lump sum / unit price / cost-plus-fee / §7.3.7). The form requires a selection.
- Quoting AIA A201 §7.3 verbatim from memory. Confirm against the user's executed A201.
- Substituting a CCD for a Change Order when both parties have agreed. CCD = pre-agreement; G701 = post-agreement.
- Substituting a CCD for an ASI when there is no change to Sum / Time. Route to `/draft-asi`.
- Inventing a vendor quote, unit price, or schedule-impact estimate. TBD is acceptable; fabrication is not.
- Omitting the Owner authorization signature block. CCDs without Owner signature are unenforceable.
- Using `Director` as a role.
