---
title: Explain Stamp
summary: Explain what a submittal stamp commits you to
discipline: construction-admin
tags: ["AIA A201", "Construction Admin"]
description: Interpret a submittal stamp marking (A / AAN / RNR / R) and what it binds the contractor and architect to under AIA A201 §3.12
argument-hint: <stamp-mark-or-submittal-paste>
---

# Explain Stamp

Interpret a submittal review stamp marking and the binding effect on the contractor and Architect of Record under AIA A201-2017 §3.12. Output is an inline interpretation citing the stamp class, AIA G712 record convention, and §3.12.7 distribution of risk. For a full submittal-log audit, use the `submittal-review` skill.

## Input you need

Before interpreting, gather:

- **Stamp marking** — quote the stamp text verbatim. Standard four:
  - `A` / `Approved` / `No Exceptions Taken` — submittal accepted as submitted.
  - `AAN` / `Approved As Noted` / `Make Corrections Noted` — accepted with marked corrections; resubmittal not required, but the contractor must execute the marked corrections.
  - `RNR` / `Revise & Resubmit` — substantive issues; contractor must correct and resubmit before fabrication.
  - `R` / `Rejected` / `Not Approved` — non-conforming; contractor must replace with conforming submittal.
  - Variants exist: `Reviewed`, `For Information Only`, `Furnish As Corrected`, `No Action Taken`. Quote stamp text verbatim — do not collapse to the standard four.
- **Submittal type** — shop drawing, product data, sample, mock-up, color selection, schedule of values, certificate of insurance. Each carries different binding force under A201-2017 §3.12.4.
- **Issuing party** — `Architect of Record (AOR)`, `Engineer of Record (EOR)`, consulting engineer (MEP, structural, civil), `Owner's Representative`. Sub-consultant stamps flow through AOR per `B101-2017 §3.6.4.2`.
- **AIA contract context** — `A201-2017 §3.12` (Submittals), `§3.12.6` (Contractor's review prior to AOR submission), `§3.12.7` (Architect's review limitations), `§3.12.10` (deviations from Contract Documents).
- **Submittal log reference** — `AIA G712` (Shop Drawing & Sample Record) entry number, transmittal #, project log reference.
- **Specific question** — Examples: "Does AAN waive the Contract requirement?", "Can the GC fabricate off an `A` stamp?", "What's our liability on a `Reviewed for design intent only` stamp?"

If the stamp text or submittal context is paraphrased rather than quoted, ask for verbatim before interpreting.

## Output structure

```markdown
# Explain Stamp — [Marking, plain title]

**Marking:** [A / AAN / RNR / R / variant]
**Submittal:** [§07 27 26 — Air Barrier shop drawing, transmittal #SD-024]
**Issued by:** [Architect of Record / Engineer of Record / MEP consultant]
**Contract:** [A201-2017]
**Question:** [the user's specific question]

---

## What the marking means (literal)

[1–2 sentences. Quote the stamp text verbatim and the standard meaning per industry convention. If the stamp text is non-standard, state that and quote as printed.]

## A201-2017 §3.12 binding effect

- **Contractor's obligation** — [What the GC must do next under §3.12.6 / §3.12.10. Quote relevant § verbatim.]
- **Architect's review scope** — [What §3.12.7 limits the AOR's review to: "checking conformance with information given and design concept expressed in the Contract Documents", explicitly not means / methods / safety / coordination.]
- **Deviation flag** — [If the submittal includes deviations under §3.12.10, what the GC must explicitly identify in writing on the submittal cover.]

## Risk allocation

- [Bullet — what an `A` or `AAN` stamp does **not** waive: §3.5 warranty, §3.3 means and methods, §3.4 materials and equipment, §3.2 site verification.]
- [Bullet — common AOR boilerplate: "Reviewed for general conformance with design intent only — no responsibility for dimensions, quantities, fabrication processes, or coordination."]
- [Bullet — GC's continuing obligations: A201-2017 §3.2 (site verification), §3.12.5 (Contractor's review prior to AOR submission), §3.12.10 (deviations identified).]

## What to do next

- [Bullet — fabrication, resubmittal, RFI, or change-order trigger based on the marking.]
- [Bullet — log entry in `AIA G712` Shop Drawing & Sample Record.]
- [Bullet — distribution: copy to Owner per A201-2017 §3.12.6 and to Owner's Representative.]

## Caveats

- Stamp meanings are conventional, not contractual unless defined in the General Requirements (Division 01) or A201 modifications. Always cross-check the project's submittal-procedures spec section (`§01 33 00`).
- Owner-modified A201 may shift the §3.12.7 limitation. Public owners (NYC SCA, GSA, USACE) and CMc deliveries (`A102-2017`, `A103-2017`) often expand AOR review duties beyond design-intent.
- For a binding interpretation on a contested submittal, route through the `rfi-writer` skill to formalize the question to the AOR.
```

## NA AEC conventions (enforce)

- **English only.** No Hangul anywhere.
- **Stamp markings** — quote verbatim. Standard four: `A`, `AAN`, `RNR`, `R`. Variants must be quoted as printed; do not collapse non-standard text into the standard four.
- **AIA citation format** — `A201-2017 §3.12.6`, `B101-2017 §3.6.4`. Always include the edition.
- **AIA G-series forms** — `G712` (Shop Drawing & Sample Record), `G714` (CCD), `G701` (Change Order), `G710` (ASI).
- **Submittal types** — `shop drawing`, `product data`, `sample`, `mock-up`, `color selection`, `schedule of values`, `certificate of insurance`. Per CSI MasterFormat 2020 Division 01 + AIA A201-2017.
- **CSI section numbers** — MasterFormat 2020 form `XX YY ZZ` (e.g., `07 27 26`). Never `07.27.26` or `7-27-26`.
- **Roles** — `Architect of Record (AOR)`, `Engineer of Record (EOR)`, `General Contractor (GC)`, `Construction Manager (CM)`, `Owner's Representative`, `Subcontractor`. Never use `Director` as a project role.
- **AHJs** — `NYC SCA`, `NYC DDC`, `GSA`, `USACE`, `DSA`, `CA HCAI` when statutory submittals apply. Never `the AHJ`, `the city`, or `local authority` generically.
- **Codes referenced** — IBC / IRC / NFPA / 2010 ADA / ASCE 7. Never `KBC`, `KS`, `EN`, `BS`, `JIS`, `DIN`.
- **Imperial-first** units; metric in parens only when useful.
- **Floor labels** — `L3`, `Level 3`, `3rd floor`. Never `3F`.

## Constraints

- Do not invent stamp language. Quote the actual stamp printed by the AOR / EOR / consultant.
- Do not invent submittal-review boilerplate. If the project's stamp uses non-standard text, quote it and stop — do not extrapolate to standard meanings.
- Always cite A201-2017 §3.12.6 (Contractor's review) and §3.12.7 (Architect's limited review) when explaining binding effect.
- Coexists with `submittal-review` skill (multi-submittal log audit) and `rfi-writer` (formalizing contested submittals). Redirect for multi-item scope.
- Markdown only. No Word / PDF output, no `aec-doc-gen` dependency.

## Workflow

1. Echo back: marking, submittal type + section number, issuing party, contract edition, question. One line.
2. If the stamp text is paraphrased rather than quoted, ask for the exact wording before proceeding.
3. Produce the response in one shot.
4. Surface next-step actions explicitly (fabricate / resubmit / open RFI / log G712 entry / route to Owner per §3.12.6).
5. If the project's stamp diverges from the standard four, flag the divergence and recommend cross-checking `§01 33 00 — Submittal Procedures`.
