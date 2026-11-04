---
name: embodied-carbon-tracker
description: "Keeps one dated record of a project's embodied carbon as the design changes: quantities from your own take-off, factors from the data source you name, and the result kept per element and per life-cycle stage rather than as one number, because a single figure hides which decision moved it. Records the boundary and the data vintage on every entry, since two projects' figures are comparable only when both are stated. Trigger on \"embodied carbon\", \"track the carbon on this design\", \"whole life carbon\", \"EPD\", \"upfront carbon\", \"A1-A3\", \"embodied-carbon-tracker\", or a material change with a question about its carbon. Carries no emission factors and no benchmarks; every factor comes from an EPD or a database you name, with its vintage. `decarbonization-strategist` plans the operational path over years; this counts what the materials carry. It is not an LCA and does not replace the sustainability consultant."
license: MIT
metadata:
  title: "Embodied Carbon Tracker"
  summary: "Track embodied carbon by stage against factors you supply"
  discipline: "envelope-performance"
  tags: "Tracking"
---

# Embodied Carbon Tracker

Embodied carbon gets reported as one number at one moment, usually late, usually
to satisfy a requirement. The number is not the useful part. Which element
carries the most, and what happened to it when the structure changed, is, and
neither survives being totalled.

## Scope and limits — read first

**What this does.** Keeps one dated log per project. Records quantities, the
factor applied to each with its source and vintage, and the result per element
and per life-cycle stage. Tracks how each moves as the design changes, so a
decision can be attributed rather than guessed at.

**What this does not do.**

- **It carries no factors and no benchmarks.** Every emission factor comes from
  an environmental product declaration or a database you name, with its vintage
  and its geography. Factors differ by product, by plant, by year and by
  country, and a recalled figure is a wrong one.
- **It is not an LCA.** A life-cycle assessment has a method, a scope and a
  practitioner. This is the running record a design team keeps between
  assessments, and it says so on every output.
- It does not take off quantities. Yours, from the model or the drawings, with
  the basis recorded.
- It does not plan the reduction path. `decarbonization-strategist` does that
  over five to fifteen years, mostly operational; this counts what the materials
  carry.
- It does not certify. `leed-tracker` and `passive-house-tracker` hold
  certification scorecards.
- It does not replace the sustainability consultant.

**What you need before starting.** What is being counted and to what boundary.
The data source for factors, named. Quantities, with what they came from. The
requirement or target, if there is one, quoted.

## Workflow

### Step 1. Fix the boundary and the source before any number

Ask, in one message:

> 1. What is being counted: which life-cycle stages, and which elements? Upfront
>    only, or through use, end of life and beyond?
> 2. What is in scope and what is out: structure, envelope, finishes, services,
>    site, temporary works, furniture?
> 3. What data source for factors, and what vintage? An EPD per product, a
>    generic database, or a mix?
> 4. What geography do the factors assume, and does it match where this is
>    built?
> 5. Is there a target or a requirement, quoted, and on what boundary was it
>    set?
> 6. Where do quantities come from, and who produces them?

**Two projects' figures are comparable only when both boundaries and both data
vintages are stated.** Record them once, at the top of the log, and repeat them
on every output. A figure quoted without them is not a figure.

### Step 2. Log per element and per stage, never as a total

| Element | Quantity | Unit | Factor | Source | Vintage | Stage | Result | Date |
|---|---|---|---|---|---|---|---|---|

Keep the stages separate. Upfront carbon and end-of-life behave differently
under a design change, and a combined figure moves for reasons nobody can trace.

Every row carries its factor's source and vintage in the row, not in a note
somewhere. When a factor is updated, the old row stays and a new row is added.

Where a quantity is an estimate rather than a take-off, mark it. Early figures
are mostly estimates and that is fine; pretending otherwise is not.

### Step 3. Record what moved, and why

The point of the log:

| Date | What changed in the design | Element affected | Before | After | Who decided |
|---|---|---|---|---|---|

Every design change that moves a number gets an entry. A structural system
change, a facade material change, a change in floor build-up, a specification
change from the contractor.

**Never overwrite a previous figure.** The sequence is the record, and a project
that can say what a decision cost in carbon is a project that can make the next
one deliberately.

### Step 4. Read the shape, not the total

At each read-back:

- **The largest contributors, ranked.** Usually a short list and usually the
  structure. This is the only ranking worth acting on.
- **What has moved since last time**, with the decision attached.
- **What is still estimated** rather than taken off, counted.
- **What is out of the boundary**, restated, because it is the first thing
  anyone forgets.
- **The factors that are generic** rather than product-specific, and where a
  product EPD would change the answer materially.
- Against the target if there is one, on the target's own boundary, and say
  plainly when the two boundaries differ.

### Step 5. Say what the number is not

On every output, three lines:

- The boundary and the data vintage.
- That this is a running record, not an assessment.
- That the figure is comparable only to figures on the same boundary with
  comparable data.

Where a figure will be reported outside the team, say that an assessment by a
practitioner is what belongs in a report, and that this feeds it.

### Step 6. Write the log

One dated file per project, appended to rather than rewritten. Ask where it
lives on the first run and use the same path after.

## Rules

- **Never supply an emission factor or a benchmark.** Every one comes from a
  source you name, with a vintage.
- State the boundary and the data vintage on every output.
- Keep results per element and per stage. Never report one total alone.
- Mark estimated quantities as estimated.
- Never overwrite a figure. Add a row and record what changed.
- Attribute every movement to a design decision and a decider.
- Say on every run that this is a running record and not an assessment.

## Anti-patterns

- Reporting one number.
- Recalling a factor for concrete, steel or timber because the figure is
  well known.
- Comparing against a benchmark set on a different boundary.
- Using a generic database factor for the one element that dominates the result.
- Overwriting the earlier figure when the design changes, which loses the only
  interesting information in the log.
- Counting the envelope carefully and leaving the structure as an estimate,
  when the structure usually dominates.
- Presenting the running record as an assessment.
- Ignoring the data vintage because the factor came from a reputable source.

## Resources

None. This skill is one file. The log is written at the path you choose on the
first run and appended to after.
