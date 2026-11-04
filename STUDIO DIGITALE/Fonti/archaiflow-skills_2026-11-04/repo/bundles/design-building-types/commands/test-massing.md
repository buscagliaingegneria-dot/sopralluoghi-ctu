---
title: Test Massing
summary: Compare massing options by computed GFA, height, and net area
discipline: design-building-types
tags: ["Design", "Analysis"]
description: "Runs the massing arithmetic for one or more schemes: floor plate area times floor count gives GFA, floor count times floor-to-floor gives height, and an optional net-to-gross factor gives net area, all compared side by side and against targets the user supplies. Trigger on \"massing options\", \"massing study\", \"how many floors do I need\", \"GFA check\", \"compare schemes\", \"test-massing\", or a pasted list of plate areas and floor counts. Pure arithmetic: it carries no zoning limits, no typical floor heights, and no typical efficiency factors. Targets come from the user's own zoning check or brief. For whether a massing is legal, use /test-far; this command answers what each option adds up to."
argument-hint: "<options: plate area, floors, floor-to-floor>"
---

# Test Massing

Take two or more massing options, run the arithmetic on each, and put the
results side by side. This is the design-side companion to `/test-far`: that
command establishes the legal limit from the zoning source, this one tells you
what each scheme adds up to so you can hold them against that limit, or against
the brief.

## Scope and limits, read first

**What this does.** For each option: gross floor area from plate area and floor
count, overall height from floor count and floor-to-floor, net area if the user
supplies a net-to-gross factor, and the deltas between options and against any
target the user names.

**What this does not do.**

- **It does not know any typical values.** No default floor-to-floor height, no
  typical efficiency factor, no standard parapet. Every number comes from the
  user. A recalled "13'-6\" is typical for office" is exactly the value this
  command must never supply.
- **It does not judge legality.** FAR, height limits, coverage, and setbacks are
  zoning questions with a jurisdiction behind them. Run `/test-far` for those;
  paste its limit here as a target if you want the comparison.
- It does not do sky exposure planes, setback geometry above a base, or any
  shaping rule. Those need the zoning text, not arithmetic.
- It does not check the program fit inside the massing. `space-program` builds
  the area requirement; this command tells you whether an option's GFA reaches
  it, not whether the rooms work.
- It does not count parking (`/test-parking`), estimate cost (`/lookup-cost`),
  or size structure.

## Input you need

Ask for anything missing; never fill a value in. Per option:

1. **A name or label**, so the table reads (Option A, "the bar scheme").
2. **Floor plate area**, in the user's units. A stepped massing is fine: take
   plate area and floor count per segment and sum the segments.
3. **Floor count**, per segment if stepped.
4. **Floor-to-floor height**, per segment if it varies. If the user wants
   height above grade including a parapet or mechanical penthouse, they state
   that dimension too.

Optional, and applied only if given:

- **Net-to-gross factor**, from the user's own benchmark or brief. Without it,
  the net column reads `n/a`, not an assumed percentage.
- **Targets**: required GFA (from the brief or `space-program`), maximum GFA or
  height (from the user's zoning check), site area for a coverage or FAR figure.

Report in the units the user gave. Do not convert between imperial and metric,
and do not round inputs to neater figures.

## Output

Show the arithmetic for each option first, one block per option:

```
Option A
  GFA      = 12,000 sf x 6 floors            = 72,000 sf
  height   = 6 x 13.5 ft                     = 81.0 ft
  net      = 72,000 sf x 0.82 (user's factor) = 59,040 sf
```

Then the comparison table:

| Option | GFA | Height | Floors | Net (if factor given) | vs target |
|---|---|---|---|---|---|

- The `vs target` column shows the surplus or shortfall against each target the
  user supplied, with the target's stated source ("zoning max per your
  /test-far run", "brief requirement").
- If site area was given, add FAR and coverage as computed figures, labelled as
  arithmetic on the user's numbers, not as zoning findings.
- Close with one line per option naming what governs it: which target it misses
  or clears by the smallest margin.

## Rules

- **Never supply a floor-to-floor height, an efficiency factor, or any other
  design value.** The whole command is arithmetic on the user's numbers.
- **Stop and ask on a missing input** rather than proceeding with a
  placeholder or a "typical" figure.
- A computed FAR is a number, not a compliance result. Say so whenever one
  appears, and point to `/test-far` for the legal check.
- Show the arithmetic before the table. A totals table nobody can trace is not
  checkable.
- Keep every option in the user's own units and precision.

## Anti-patterns

- Filling in a floor-to-floor because the use is obvious ("office, so 13'-6\"").
  That is a recalled value shaping a massing decision.
- Applying an efficiency factor the user never gave, or presenting 80-85% as a
  normal range.
- Declaring an option "compliant" because its computed FAR sits under a number
  the user mentioned in passing. Compliance needs the zoning text and belongs
  to `/test-far`.
- Converting the user's metric plate areas to imperial to match the table
  headings, or the reverse.
- Recommending an option. The command reports what each adds up to; the choice
  is design judgment and stays with the user.
