---
name: geotech-report-review
description: "Reads a geotechnical report from the architect's side: separates what was actually investigated from what was inferred between boreholes, pulls out every recommendation that becomes a design obligation, finds the conditions the report makes contingent on something happening later, and reports what it means for the building rather than for the foundation engineer. Trigger on \"review the geotech report\", \"what does this soils report mean for us\", \"read the geotechnical recommendations\", \"borehole log review\", \"geotech-report-review\", or a soils report handed over at the start of design. Carries no bearing values, no soil classifications and no design parameters; every figure comes from the report, quoted. It is not geotechnical engineering, does not verify a recommendation, and does not replace the geotechnical engineer, the structural engineer, or the Architect of Record. For one recommendation in plain English use `/explain-soils`."
license: MIT
metadata:
  title: "Geotech Report Review"
  summary: "Read a soils report for what it commits you to"
  discipline: "code-life-safety"
  tags: "Review"
---

# Geotech Report Review

A geotechnical report is read once, by the structural engineer, for the bearing
value. Everything else in it — the water table, what has to be removed, what
cannot be built in winter, what has to be observed during construction —
becomes an architectural problem later, usually at the worst moment.

## Scope and limits — read first

**What this does.** Reads the report for what it obliges the project to do,
separates investigated ground from inferred ground, and reports what it means
for the building: the floor level, the basement, the site work, the programme,
and the things that have to happen during construction.

**What this does not do.**

- **It carries no values.** No bearing capacities, no classifications, no
  settlement limits, no lateral pressures. Every figure is quoted from the
  report.
- **It is not geotechnical engineering** and it does not verify or second-guess
  a recommendation. Where a recommendation looks inconsistent with another, it
  says so as a question for the engineer.
- It does not do foundation design. That is the structural engineer's, working
  from this report.
- It does not review the survey. `survey-review` does.
- It does not explain one recommendation in plain English. `/explain-soils`
  does that and this points at it.
- It does not replace the geotechnical engineer, the structural engineer, or the
  Architect of Record.

**What you need before starting.** The report, complete, with the borehole logs
and the plan showing where they were. The scheme, or what is proposed. Whether
there is a basement and to what depth. The site plan.

## Workflow

### Step 1. Establish the scope of the investigation

Ask, in one message:

> 1. What was the report commissioned for, and by whom? A report for a previous
>    scheme is not a report for this one.
> 2. How many boreholes, how deep, and where were they relative to what is now
>    proposed?
> 3. When was the fieldwork done, and in what season?
> 4. Does the scheme now extend beyond where the investigation went, in plan or
>    in depth?
> 5. Is there a basement, and how deep?

**Question 4 is the one that matters most.** A building that moved fifty feet
after the boreholes were drilled is a building on inferred ground, and that is a
finding rather than a detail.

### Step 2. Separate investigated from inferred

Plot, in words, what was actually tested against what the scheme now occupies:

| Location | Investigated? | Depth reached | Under what part of the scheme |
|---|---|---|---|

Report the parts of the footprint with no borehole under or near them, and the
depths the scheme reaches that the investigation did not. Everything between
boreholes is interpolation, and the report will say so somewhere; quote it.

### Step 3. Pull out every recommendation that becomes an obligation

The report is written as advice. Once the design follows it, each item is a
commitment. List them:

| Recommendation | Quoted | Who it binds | What it costs the design |
|---|---|---|---|

Work through at least: bearing stratum and depth, whether any material has to be
removed and replaced, groundwater and what has to be done about it, slab
support, lateral earth pressures, whether the ground is expansive or
collapsible, seismic site class, corrosivity or chemical attack on concrete and
buried metal, slope stability, and any requirement for ground improvement.

### Step 4. Find the contingencies and the observation requirements

The two categories that surprise projects:

- **Contingent recommendations.** Anything phrased as "if X is encountered" or
  "subject to confirmation during construction". Each one is a decision deferred
  to the site, and each needs somebody who will make it, a budget, and time in
  the programme. List every one.
- **Observation requirements.** Where the report requires the geotechnical
  engineer to observe or test during construction, that is a scope item, a fee
  and a hold point. Every one gets named, with what happens if it is skipped.

Both belong in the specification and in the programme, and both are routinely
neither.

### Step 5. Translate to the building

What the report means for the architecture, not for the foundation:

- Does the ground floor level work, given the bearing depth, the water table and
  what has to be removed?
- Is the basement viable, and what does the water condition do to it? Point at
  `design-below-grade-assembly`.
- What does the site work look like: cut, fill, retaining, and what the report
  says about reusing excavated material.
- Programme: seasonal restrictions, dewatering, surcharge and waiting periods,
  ground improvement.
- What this does to the neighbours: vibration, dewatering drawdown, shoring
  against a party line, underpinning.
- Cost signals worth telling the client now rather than at tender.

### Step 6. Report

- The investigated-versus-inferred finding, first.
- The obligations table.
- Every contingency, with who decides and when.
- Every observation requirement, with whether it is in anybody's scope yet.
- What it means for the building.
- Every inconsistency found, as a question for the geotechnical engineer.
- What further investigation is warranted, and when it has to happen to be
  useful.

### Step 7. Save, if asked

Ask whether to write the review to a file and where.

## Rules

- **Never supply a soil value or a design parameter.** Quote the report.
- **Never verify or contradict a recommendation.** Inconsistencies are questions.
- Compare the investigation's coverage against the scheme's footprint and depth,
  every run.
- List every contingent recommendation and every observation requirement.
- Say what the report means for the building, not only for the foundation.
- Never treat a report commissioned for another scheme as current.

## Anti-patterns

- Reading the report for the bearing value and stopping.
- Treating interpolation between boreholes as investigated ground.
- Using a report from a previous scheme without checking the footprint moved.
- Leaving contingent recommendations for the contractor to discover.
- Omitting the observation requirements from the specification and the fee.
- Reporting to the structural engineer's audience rather than the design team's.
- Second-guessing a geotechnical recommendation.

## Resources

None. This skill is one file. Output is written directly at the path you choose.
