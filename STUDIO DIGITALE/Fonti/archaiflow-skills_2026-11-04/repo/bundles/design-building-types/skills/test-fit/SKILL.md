---
name: test-fit
description: "Runs feasibility arithmetic for a site: floors times plate against your FAR and height limits, gross to net through your efficiency, net to units through your unit sizes, parking through your ratio, laid out as side-by-side scenarios with every step shown. Trigger on \"test fit\", \"what fits\", \"does it pencil\", \"how many units\", \"buildable area\", \"yield study\", \"massing numbers\", \"test-fit\", or a pasted site area with zoning limits. Every limit and assumption comes from you or your zoning summary, cited: the skill never supplies a FAR, an efficiency factor, a unit size, or a parking ratio from memory or from web search, and a scenario built on an unverified limit says so on its face. Arithmetic only, no geometry: setback envelopes, floor plates that actually fit the lot, and massing are drawing work it does not do. Early feasibility, not a zoning compliance check (test-far checks one scheme) and never a substitute for the zoning analysis."
license: MIT
metadata:
  title: "Test Fit"
  summary: "Run the arithmetic on what fits a site under your limits"
  discipline: "design-building-types"
  tags: "Pre-Design, Analysis"
---

# Test Fit

The first real question on a site is arithmetic: how many floors of what
plate, inside what cap, yielding how many units and how much parking. The
arithmetic is the same on every site. The caps, the efficiency, and the
unit sizes are the deal's own numbers, so they come from you, cited, and
the scenarios print them next to every result.

## Scope and limits — read first

**What this does.** Takes your site number and your limits, builds the
scenarios you ask for (vary the plate, the floor count, the unit mix),
and runs each one through the same chain: envelope cap, gross area, net
area, yield, parking, with the arithmetic printed at every step and the
limiting constraint named per scenario.

**What this does not do.**

- **It does not know any limits or factors.** No FAR, no height or
  coverage limit, no efficiency factor, no unit sizes, no parking ratio.
  Every one arrives from you or from a `zoning-summary` output you point
  it at, cited. A limit you could not source is used only if you say so,
  and the scenario is stamped `unverified limit` where it prints.
- **Arithmetic, not geometry.** It multiplies plates and counts; it does
  not check that a plate fits inside the setbacks, does not shape a
  massing, and does not know where the core goes. A scenario that clears
  the numbers can still fail on the drawing board, and the report says
  exactly that.
- It is not a zoning compliance check. `test-far` checks one scheme's
  numbers against the clauses; the full analysis is `zoning-summary` and
  your own reading. Bonuses, overlays, and inclusionary tradeoffs enter
  only as limits you state.
- It does not judge whether the deal pencils. Cost and revenue are not
  in the chain; yield numbers hand off to whoever runs the pro forma.
- It does not optimize. It runs the scenarios you name, side by side;
  it does not hunt for the plate that maximizes units.

**What you need before starting.** The site area, the limits that govern
it with where each came from, your efficiency assumption, and, for unit
yield, the mix and sizes you want tested.

## Workflow

### Step 1. Collect the site and the limits

Ask, in one message:

> 1. Site area, as your survey or summary states it.
> 2. The limits that govern: FAR or plot ratio, height in floors or
>    feet, coverage, any hard cap you know of. For each: the value and
>    where it came from. A `zoning-summary` file can be named and read.
> 3. Efficiency, gross to net, as you assume it, and why.
> 4. For unit yield: the unit types, their areas, and the mix. For
>    parking: your ratio, with its source.

A limit with no source can still run, marked. A limit you decline to
mark does not run.

### Step 2. Frame the scenarios

Each scenario is a named set of choices: plate area, floor count, mix.
Two or three at a time keeps the table readable; more run in batches.
Never add a scenario the user did not ask for, however obvious the gap
between two of theirs.

### Step 3. Compute each scenario, showing every step

```
Scenario <name>
  site area              <as given>            [source]
  FAR cap                <as given>            [source]
    max buildable        <arithmetic>
  plate x floors         <as chosen>
    gross proposed       <arithmetic>          vs cap: <governs or clears>
  height check           <floors vs limit>     [source]
  coverage check         <plate/site vs limit> [source]
  efficiency             <as assumed>          [stated basis]
    net                  <arithmetic>
  unit yield             <net / mix arithmetic, per type>
  parking                <ratio arithmetic>    [source]
  governing constraint   <which limit binds first, from the arithmetic>
```

Every line carries its source. Any line on an unverified limit prints
`unverified` beside its result, and the scenario summary repeats it.

### Step 4. Report

The scenarios side by side: gross, net, units by type, parking, and the
governing constraint of each. Then the caveat, every time:

> Every limit and factor here came from you or your zoning summary. I
> did the arithmetic and supplied no values. This is early feasibility
> arithmetic, not a zoning analysis and not a massing: nothing here
> confirms a plate fits the lot. `test-far` checks a scheme; your zoning
> analysis governs.

### Step 5. Save, if asked

Ask whether to write the study to a file and where. Write it directly,
including the arithmetic. There is no template and no script.

## Rules

- **Never supply a limit, a factor, a unit size, or a ratio.** There
  are none in this file.
- **Name the governing constraint per scenario**, derived from the
  arithmetic, not from intuition.
- **Unverified limits are stamped where they print**, and again in the
  summary.
- **Run only the scenarios asked for.**
- **Show the arithmetic**, every chain, every scenario.
- Never convert units on your own; a site in acres against plates in
  square feet stops for one conversion you confirm.
- Say on every run that this is arithmetic, not zoning analysis and not
  massing.

## Anti-patterns

- Recalling a typical efficiency, parking ratio, or unit size to keep
  the chain moving. These are exactly the numbers a lender will ask the
  source of.
- Softening the unverified stamp because the scenario looks promising.
- Adding the scenario the user obviously should have asked for.
- Presenting the max-FAR scenario as the recommendation.
- Letting a scenario imply the plate fits the lot because the coverage
  arithmetic cleared.

## Resources

None. This skill is one file. Output is written directly at the path
you name.
