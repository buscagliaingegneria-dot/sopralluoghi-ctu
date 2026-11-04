---
title: Compare Structural System
summary: Put structural systems side by side on what each does to the architecture
discipline: structure-mep
tags: ["Analysis"]
description: "Compares two or more structural systems — steel, cast-in-place concrete, mass timber, bearing wall, whatever is on the table — on the criteria you name, using values you and your engineer supply for each one. This is the architect's side of the decision: what each system does to floor depth and floor-to-floor height, to the grid and the spans, to fire protection strategy, to acoustics, to whether the structure can be the finish, to MEP routing, and to schedule. Builds the comparison matrix, holds every system to the same criteria, and marks any cell where one system has a figure and another does not, because that asymmetry is where a comparison quietly decides itself. Carries no spans, no depths, no costs, no carbon figures; every number comes from the engineer, the estimator, or a source you name. The engineer owns and stamps the system itself — `explain-load-path` traces how one works, `design-beam` and `design-column` check single members, and `compare-assembly` is the same matrix for envelope build-ups."
argument-hint: <system-a> <system-b> [criteria]
---

# Compare Structural System

The structural system is chosen once, early, and everything the architecture
does afterward lives inside it. It is also the decision most often inherited
rather than made: the office's usual system, the engineer's usual system, the
one the last project used. This command makes the comparison explicit, on the
architect's criteria, with the engineer's numbers.

## Scope and limits — read first

**What this does.** Takes two or more structural systems with whatever values
you and your engineer have for each, takes the criteria you want to decide on,
builds one matrix, and reports where the comparison is actually decidable and
where it is not.

**What this does not do.**

- It carries **no values**. No spans, no depths, no bay sizes, no costs, no
  carbon figures, no fire ratings. Every number comes from the engineer, the
  estimator, or a source you name.
- It does not pick the system. The structural engineer owns that decision and
  stamps its consequences. This compares what each option does to the
  architecture, so the conversation with the engineer starts from criteria
  rather than habit.
- It does not check members. `design-beam` and `design-column` hold single
  members against values your standard gives; `explain-load-path` traces how a
  system carries load.
- It is not a general options comparison. For scheme-level decisions use the
  `option-compare` skill; for envelope build-ups use `compare-assembly`.

**What you need before starting.** The candidate systems, named. The criteria
you are deciding on. For each criterion, a value per system from the engineer
or estimator, or an explicit `unknown`.

## Inputs the command needs

1. **The systems**, named specifically. "Concrete" is not a system; "two-way
   flat plate" is.
2. **The criteria.** Ask if not given. The architect's usual ones: structural
   depth and what it does to floor-to-floor, span and grid flexibility, fire
   protection strategy and what it adds, acoustic performance between floors,
   whether the structure can be exposed as finish, MEP routing through or
   under it, erection speed and weather sensitivity, foundation demand,
   future adaptability, cost, embodied carbon, and whether the local market
   builds it well.
3. **A value per system per criterion**, each with its source, or the word
   `unknown`.

Never substitute a typical value for an unknown. Never carry a value across
systems because "spans are similar".

## Workflow

### Step 1 — Read the systems back

Name each system fully and confirm the building it is being compared for:
storeys, use, and rough footprint as the user states them. The same two
systems compare differently on a different building, and a matrix with no
building attached is a magazine article.

### Step 2 — Fix the criteria before looking at any value

Agree the criteria list first and write it down. Criteria chosen after the
values are on the table are criteria chosen to reach an answer.

Ask which criteria are **thresholds** (must pass) and which are **trade-offs**
(more is better). Say back which is which.

### Step 3 — Build the matrix

| Criterion | Threshold or trade-off | System A | System B | Source per cell | Comparable? |
|---|---|---|---|---|---|

The last column is the point. Mark a row **not comparable** when one system has
a figure and another has `unknown`, when the figures came from different kinds
of source, or when one is a project number and the other is a rule of thumb.
Do not fill a gap to make a row look complete.

### Step 4 — Report

- Which systems fail a threshold, and on which criterion.
- Which leads on each trade-off, among the rows that are comparable.
- **The count of rows that are not comparable**, listed by name, reported
  before any conclusion, because it decides whether there is one.
- What to ask the engineer or estimator to make the incomparable rows
  comparable, phrased as the questions to send.

If more than a couple of rows are not comparable, say plainly that the
comparison is not yet decidable and name what is missing, rather than ranking
on the rows that happen to be filled.

### Step 5 — Save, if asked

Ask whether to write the matrix to a file and where. Markdown or CSV.

## Rules

- **Never supply a value.** Not a span, not a depth, not a cost, not a carbon
  figure, not as a placeholder that looks like a number.
- Fix the criteria before the values are visible.
- An `unknown` stays `unknown` for the whole run.
- Report the incomparable count before the conclusion, every time.
- Never rank on partial data without saying the data is partial.
- Say on every run that the engineer owns the system decision; this matrix is
  the architect's side of that conversation.

## Anti-patterns

- Filling a gap with a typical span or depth so the table looks finished.
- Comparing this project's concrete number against last project's timber
  number without flagging it.
- Adding a criterion after seeing the values.
- Ranking systems when half the matrix is unknown.
- Treating cost as the only threshold because it arrived first.
- Recommending a system. This command reports; the engineer and the team
  decide.
