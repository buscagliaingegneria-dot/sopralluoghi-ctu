---
name: utilization-tracker
description: "Keeps one dated record of hours against fee at the level where it can still be acted on: by phase and by person rather than by project total, with the percentage of work complete recorded separately from the percentage of fee spent, since a project can be on budget and forty percent behind. Records what caused each overrun so the pattern separates from the incident, and flags the hours that should have been additional services before they are written off. Trigger on \"utilization tracker\", \"are we over on this project\", \"hours against fee\", \"track the team's time by phase\", \"utilization-tracker\", or a timesheet export handed over to make sense of. Carries no rates, no utilization targets and no benchmarks; the practice sets those. It does not replace the accounting system — it reads what that produces — and it does not replace `fee-tracker`, which follows the fee itself."
license: MIT
metadata:
  title: "Utilization Tracker"
  summary: "Track hours against fee by phase, and see the overrun while it is small"
  discipline: "practice-contracts"
  tags: "Tracking"
---

# Utilization Tracker

A project total tells you it is over when it is too late. Phase and person tell
you at the point somebody could still change how the work is being done, and
they tell you why, which is the part that improves the next fee proposal.

## Scope and limits — read first

**What this does.** Records hours against fee by phase and by person, keeps
progress and spend as two separate figures, records the cause of each overrun,
and flags hours that belong in an additional services request rather than in a
write-off.

**What this does not do.**

- **It carries no rates, no targets and no benchmarks.** Charge-out rates,
  utilization targets and what a phase should cost are the practice's own. It
  will help you record yours; it will not supply them.
- It is not an accounting system and it does not replace one. It reads what
  yours exports.
- It does not follow the fee itself. `fee-tracker` tracks earned against billed
  and invoiced. This tracks effort against fee, which is a different question.
- It does not estimate. `fee-estimator` does.
- It does not evaluate people. Hours by person show where effort went, not how
  well it was spent, and the log says so.

**What you need before starting.** The fee, split by phase as the proposal
split it. The hours, by phase and person, from your timesheet system. An honest
assessment of progress by phase. Your rates, if you want money rather than
hours.

## Workflow

### Step 1. Establish the structure

Ask, in one message:

> 1. What is the fee, split by phase as the proposal splits it? If the proposal
>    did not split it, say so; the tracking will be coarser and that is the
>    finding.
> 2. What can your timesheet system export, and at what granularity?
> 3. Do you want hours, money, or both? Money needs rates.
> 4. Who is on the project, and at what rate band?
> 5. How is progress assessed, and by whom?
> 6. What is the reporting rhythm: weekly, monthly, at phase ends?

### Step 2. Record progress and spend as two separate figures

The core of the method:

| Phase | Fee | Spent | % fee spent | % work complete | Gap | Assessed by | Date |
|---|---|---|---|---|---|---|---|

**Never combine them into one health figure.** A phase at 50% of fee and 50%
complete is fine. A phase at 50% of fee and 25% complete is in trouble and the
combined number would have said 50%.

Progress is assessed by a person and recorded with their name and the date. It
is a judgement, it is optimistic by default, and attributing it is what makes it
improve.

### Step 3. Record hours by person, and read what they say

| Person | Phase | Hours | Band | Note |
|---|---|---|---|---|

Two readings that only appear at this level:

- **Seniority mix.** Work being done by more senior people than it was priced
  for is the most common quiet overrun, and it does not show in a project total.
- **Concentration.** One person carrying a phase is a programme risk and often a
  sign the work was not set up to be shared.

Report both as observations about how the work is organised, never about the
people.

### Step 4. Record the cause of every overrun

An overrun with no cause recorded teaches nothing:

| Phase | Overrun | Cause | Category | Recoverable? |
|---|---|---|---|---|

Categories, and each behaves differently:

- **Fee was wrong.** The estimate missed something. Feeds `fee-estimator` and
  the next proposal.
- **Scope grew.** The client asked for more. **Should be an additional services
  request**, and if it has not been made, that is the flag.
- **Client-caused.** Delay, indecision, rework from changed direction. Often
  recoverable and usually not asked for.
- **Our own.** Rework from our error, or from getting it wrong the first time.
  Not recoverable and worth recording honestly, because the pattern is where the
  practice improves.
- **Programme extended.** The project is taking longer at the same effort per
  month. The most invisible category and the one lump sums are most exposed to.

**Report recoverable overruns that have not been claimed, every read-back.** This
is the single most valuable output.

### Step 5. Read back

At the reporting rhythm:

- Phases where spend exceeds progress, largest gap first.
- Recoverable overrun not yet claimed, with the cause and the date it arose.
  Point at `/draft-additional-services`.
- Seniority mix against how the phase was priced.
- Cause categories, totalled, across the project.
- Phases not yet started with what remains, and phases finished with what they
  actually cost.

Report elapsed and actual. Never forecast a final cost. Where the practice wants
a projection, it is a person's estimate, recorded with their name.

### Step 6. Write the log

One dated file per project, appended to rather than rewritten. Ask where it
lives on the first run and use the same path after. At project end, the cause
categories are the input to `lessons-learned` and to the next fee proposal.

## Rules

- **Never supply a rate, a target, or a benchmark.**
- **Keep progress and spend as two figures.** Never combine them.
- Progress assessments carry the assessor's name and the date.
- Every overrun records a cause and a category.
- Report unclaimed recoverable overrun in every read-back.
- Never forecast. A projection is a named person's estimate.
- Report hours by person as an observation about the work, never about the
  person.
- Append; never rewrite an earlier entry.

## Anti-patterns

- Tracking the project total only.
- Reporting one health percentage that merges spend and progress.
- Recording an overrun with no cause.
- Writing off scope growth instead of raising it as additional services.
- Assessing progress with nobody's name against it.
- Using the log to evaluate individuals.
- Forecasting the final cost from the current burn rate.
- Rewriting an earlier progress figure once the real one is known. Log both.

## Resources

None. This skill is one file. The log is written at the path you choose on the
first run and appended to after.
