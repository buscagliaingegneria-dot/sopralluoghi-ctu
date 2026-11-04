---
title: Explain AIA
summary: Read a contract clause from all three sides
discipline: practice-contracts
tags: ["AIA A201", "AIA B101", "Construction Admin"]
description: Interpret an AIA contract clause (A201/B101/C401/A101) in plain English with multi-POV (Owner/Architect/Contractor) read
argument-hint: <aia-form-clause-or-paste>
---

# Explain AIA

Interpret a single AIA contract clause — paste the text or cite the §, get plain-English meaning plus an Owner / Architect / Contractor POV read. Output is an inline interpretation citing form + edition + §. For full red-line review or contract markup, use the `contract-review` skill.

## Input you need

Before interpreting, gather:

- **AIA form + edition**:
  - **General Conditions** — `A201-2017`, `A201-2007`. Many owners modify A201; verify the executed version.
  - **Owner-Architect** — `B101-2017` (standard), `B102-2017`, `B103-2017` (large/complex), `B132-2019` (CMc delivery), `B141-1997`.
  - **Owner-Contractor** — `A101-2017` (stipulated sum), `A102-2017` (CMc with GMP), `A103-2017` (CMc cost-plus, no GMP), `A104-2017` (small projects), `A141-2014` (Design-Build).
  - **Architect-Consultant** — `C401-2017`, `C403-2014`.
  - **Bidding** — `A701-2018` (Instructions to Bidders), `A305-2020` (Contractor's Qualification Statement).
- **Clause reference** — `§X.Y.Z`: `A201-2017 §3.7.4` (code compliance), `§3.18` (indemnification), `B101-2017 §3.6.5` (Architect's review time), `A101-2017 §5.1.2` (Date of Substantial Completion).
- **Clause text** — paste the executed clause text (preferred — owner-modified A201 reads differently from base AIA). Memory-paraphrased clauses are unreliable across editions and across owner edits.
- **Delivery method** — `Design-Bid-Build (DBB)`, `CMc with GMP`, `CMc cost-plus no GMP`, `Design-Build (DB)`, `IPD`. Same clause reads differently across deliveries.
- **POV requested** — `Owner`, `Architect of Record (AOR)`, `Engineer of Record (EOR)`, `General Contractor (GC)`, `Construction Manager (CM)`. Default: all three primary parties (Owner / AOR / GC).
- **Project context** — public vs private owner. Public owners (`NYC SCA`, `GSA`, `USACE`, state DGS) impose statutory overrides; private commercial / institutional owners typically modify but follow base AIA structure.
- **Specific question** — Examples: "Is §3.18 indemnification too broad for the GC?", "Does B101-2017 §3.6.5 commit the AOR to a hard turnaround?", "Who pays for §6.1 separate-contractor delays?"

If the clause text is missing or paraphrased, stop and ask for the executed text.

## Output structure

```markdown
# Explain AIA — [Form-Edition §X.Y.Z, plain title]

**Form:** [AIA A201-2017 / B101-2017 / A101-2017 / C401-2017]
**Section:** [§3.18 — Indemnification]
**Delivery:** [DBB / CMc with GMP / DB / IPD]
**Clause status:** [base AIA / owner-modified — describe modification]
**Question:** [the user's specific question]

---

## What the clause says (literal)

> [Verbatim quote of the executed clause. If owner-modified, quote both the AIA base text and the owner edit in separate blockquotes.]

(AIA A201-2017 §3.18.1)

## Plain-English meaning

[3–5 sentences. What the clause obligates / permits / restricts. Translate legal phrasing without softening duty levels (`shall` ≠ `should` ≠ `may`).]

## Owner POV

- [What the Owner gains, owes, or risks under this clause.]
- [Cross-reference to related Owner duties — e.g., A201-2017 §2.2 (Information Provided by Owner), §9.2 (Schedule of Values approval).]

## AOR / EOR POV

- [What the design professional must do — response times, instruments-of-service, observations vs. inspections, Additional Services triggers.]
- [Cross-reference to B101-2017 — e.g., §3.6.4 (Submittal review), §11 (Compensation for additional services).]

## GC / CMc POV

- [What the contractor is bound to — code compliance, supervision, schedule, indemnification scope, insurance.]
- [Cross-reference to A101 / A102 / A103 — e.g., A102-2017 §6.1.2 (GMP buyout savings), §13 (Disputes).]

## Modification flags (common owner edits)

- [Bullet — areas where owners commonly mark up this clause. e.g., "Public owners (NYC SCA, GSA, USACE) often substitute statutory indemnification language tied to state-law caps."]
- [Bullet — broad-form vs. limited-form indemnification, sole vs. comparative negligence.]
- [Bullet — insurance carve-outs (waiver of subrogation, additional-insured endorsements per A201-2017 §11).]

## Caveats

- This is not legal advice. Engage Owner's counsel or risk management for binding interpretation. AIA contracts are owner-modified ~80% of the time — base-form readings rarely apply unmodified.
- Edition matters. `A201-2017` differs from `A201-2007` on §3.7.4 (code compliance), §15 (claims and disputes), and §11 (insurance) — do not interpret across editions without confirming the executed year.
- For full red-line review or multi-clause comparison, use the `contract-review` skill.
```

## NA AEC conventions (enforce)

- **English only.** No Hangul anywhere.
- **AIA citation format** — `[Form]-[Edition] §[Number]`: `A201-2017 §3.18`, `B101-2017 §3.6.5`, `A101-2017 §5.1.2`. Always include the edition. Never "AIA A201" without year.
- **Codes referenced** — IBC / IRC / NFPA / 2010 ADA / ASCE 7 / NBC. Never `KBC`, `KS`, `EN`, `BS`, `JIS`, `DIN` — out of catalog scope.
- **Roles** — `Owner`, `Owner's Representative`, `Owner's Counsel`, `Architect of Record (AOR)`, `Engineer of Record (EOR)`, `General Contractor (GC)`, `Construction Manager (CM)`, `Construction Manager as Constructor (CMc)`, `Construction Manager as Adviser (CMa)`. Never use `Director` as a project role.
- **AHJs** — name specifically when statutory overrides apply: `NYC SCA`, `NYC DDC`, `GSA`, `USACE`, `DSA`, `CA HCAI`, `NYC DOB`, `state DGS`, `port authority`. Never `the AHJ`, `the city`, or `local authority` generically.
- **Imperial-first** units (`ft`, `sf`, `°F`). Metric in parens only when useful.
- **Floor labels** — `L3`, `Level 3`, `3rd floor`. Never `3F`.

## Constraints

- Do not invent clause text. If the user pasted nothing, ask. Memory-paraphrased AIA clauses are unreliable across editions and owner edits.
- Distinguish **base AIA** from **owner-modified** language explicitly — flag every mark-up as a separate quote.
- Surface the three primary POVs (Owner / AOR / GC). Adding more POVs is fine; reducing below three is not.
- Always include the **Caveats** section with the "not legal advice" disclaimer.
- Coexists with `contract-review` skill (full red-line). For multi-clause review, redirect.
- Markdown only. No Word / PDF output, no `aec-doc-gen` dependency.

## Workflow

1. Echo back: form-edition, §, delivery method, POV scope, question. One line.
2. If clause text or edition is missing, stop and ask.
3. If owner-modified language is suspected (statutory owners, public projects, IPD), flag the assumption before interpreting.
4. Produce the response in one shot.
5. List adjacent clauses to read next (e.g., "For indemnification, also pull A201-2017 §11 Insurance — owner edits to §3.18 and §11 routinely interact").
