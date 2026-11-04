---
title: Test Open Space
summary: Check provided open space against what the district requires
discipline: code-life-safety
tags: ["Compliance"]
description: "Checks a parcel's provided open space against the requirement in the zoning text you supply or paste, and does the part that goes wrong: applying the definition. Open space, usable open space, landscaped area, permeable area and amenity space are different terms with different rules about what counts, and a check that measures the wrong area passes on paper. Establishes which term the district uses, what its text says counts and what does not, then measures what you provided against it. Carries no ratios and no definitions; both come from the jurisdiction's published text. The other bulk topics — FAR, lot coverage, setback and height — are `/test-far`; for a full worksheet use the `zoning-summary` skill."
argument-hint: <jurisdiction> <district> <provided-areas>
---

# Test Open Space

Open space requirements are simple arithmetic over a definition that is not
simple. What counts toward it, at what depth, at what dimension, above or below
grade, planted or paved, public or private: the definition decides the answer
and it varies by district within one jurisdiction.

## Scope and limits — read first

**What this does.** Establishes which term the district actually uses, extracts
its definition and the ratio from text you supply or that is fetched from the
jurisdiction's own portal, then holds your provided areas against it.

**What this does not do.**

- It carries **no ratio and no definition.** Both come from the jurisdiction,
  quoted verbatim.
- It does not cover FAR, lot coverage, setback or height. `/test-far` does.
- It does not cover bonuses, overlays, special districts or planned unit
  developments, all of which routinely change the open space requirement.
- It does not measure your site. You supply the areas, broken down as the
  definition requires.
- It does not decide landscape design, planting or stormwater performance.

**What you need before starting.** The jurisdiction and the base district. The
zoning text for open space, pasted, or a portal the command may fetch from. Your
provided areas, itemised by what they are and where they sit.

## Inputs the command needs

1. **Jurisdiction and district**, named as the jurisdiction names them.
2. **The zoning text**, pasted, or authorisation to fetch from the
   jurisdiction's published portal. Both the requirement and the definition.
3. **Provided areas**, itemised: what each is, its area, whether it is at grade,
   on a podium or on a roof, whether planted or paved, its minimum dimension,
   and whether it is publicly accessible.
4. **Lot area**, if the requirement is expressed as a ratio.

## Workflow

### Step 1 — Establish which term governs

Different districts use different terms and they are not interchangeable. Report
which one the district's text uses, and quote it. If more than one applies —
a landscaped area minimum and a usable open space minimum, say — treat them as
separate checks with separate arithmetic. They very often are.

### Step 2 — Extract the definition, and read it for exclusions

Quote the definition verbatim, then list what it says about:

- Minimum dimension in any direction, and whether a strip below it counts.
- Whether area above grade counts: podium, terrace, roof.
- Whether paved, planted, or permeable is required.
- Whether driveways, parking, setbacks, easements or required yards count.
- Whether it has to be accessible, to whom, and at what hours.
- Whether area under overhangs or projections counts.

**The exclusions are where the check fails.** A calculation that counted the
required side yard, or a strip narrower than the minimum dimension, passes and
is wrong.

### Step 3 — Test each provided area against the definition

| Area | What it is | Provided | Counts? | Which clause | Note |
|---|---|---|---|---|---|

Mark each `counts`, `does not count`, or `unclear`. Never resolve an `unclear`
by choosing the favourable reading; report it as a question for the authority.

### Step 4 — Compare and report

- Required, from the quoted ratio and the lot area, with the arithmetic shown.
- Provided that counts, totalled.
- Provided that does not count, totalled separately, with the reason per item.
- Pass, fail, or marginal, against the quoted requirement.
- Every `unclear` item, listed, with the clause that is ambiguous.
- Out of scope, flagged: bonuses, overlays, special districts, PUD provisions.

### Step 5 — Save, if asked

Ask whether to write the check to a file and where.

## Rules

- **Never supply a ratio or a definition.**
- Quote the definition before doing any arithmetic.
- Read the exclusions and list them explicitly.
- An `unclear` item stays unclear. Never resolve it in the applicant's favour.
- Report counting and non-counting areas as two separate totals.
- Quoting text found by web search is not quoting the zoning. Only the
  jurisdiction's own portal or a paste.

## Anti-patterns

- Recalling an open space ratio for a district type.
- Treating open space, usable open space and landscaped area as one thing.
- Counting a required yard or setback without checking whether the text allows
  it.
- Counting a strip narrower than the stated minimum dimension.
- Counting roof or podium area without a clause that permits it.
- Producing a single total that mixes counting and non-counting areas.
- Applying a bonus provision. Out of scope, flag it.
