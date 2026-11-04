---
title: Compare Assembly
summary: Put two or more envelope build-ups side by side on criteria you name
discipline: envelope-performance
tags: ["Analysis"]
description: "Compares two or more envelope assemblies — wall, roof, or below-grade build-ups — on the criteria you name, using values you supply for each one. Builds the comparison matrix, holds every assembly to the same criteria, and marks any cell where one assembly has a figure and another does not, because that asymmetry is where a comparison quietly decides itself. Carries no material properties, no code minimums, and no cost data; every number in the table comes from you or from a source you name. For comparing design options generally rather than build-ups specifically use the `option-compare` skill; for the arithmetic inside one assembly use `condensation-check`; for laying out a new assembly use `design-wall-assembly` or `design-roof-assembly`."
argument-hint: <assembly-a> <assembly-b> [criteria]
---

# Compare Assembly

Two build-ups, or three, held to the same criteria with the same rigour. The
usual failure is not picking wrong; it is comparing an assembly you have costed
against one you have not, and calling the first one cheaper.

## Scope and limits — read first

**What this does.** Takes two or more envelope assemblies with their layers and
whatever values you have for each, takes the criteria you want to decide on,
builds one matrix, and reports where the comparison is actually decidable and
where it is not.

**What this does not do.**

- It carries **no values**. No R-values, no permeances, no costs, no carbon
  figures, no code minimums. Every number comes from you, with its source.
- It does not run the physics. Boundary temperatures and condensing planes for
  any one assembly belong to `condensation-check`. Run that on each, then
  compare the outputs here.
- It does not recommend. It reports which assembly leads on which criterion and
  where the data does not support a call. The decision is yours.
- It is not a general options comparison. For scheme-level or programme-level
  decisions use the `option-compare` skill.

**What you need before starting.** Each assembly layer by layer. The criteria
you are deciding on. For each criterion, a value per assembly, or an explicit
"unknown".

## Inputs the command needs

1. **The assemblies**, named and listed layer by layer, in order.
2. **The criteria.** Ask if not given. Common ones: thermal performance,
   condensation risk, drying capability, fire, acoustic, weight, thickness,
   buildability, sequencing, maintenance access, cost, embodied carbon, warranty
   availability, availability of the trade locally.
3. **A value per assembly per criterion**, each with its source, or the word
   `unknown`.

Never substitute a typical value for an unknown. Never carry a value from one
assembly across to another because they "use the same insulation".

## Workflow

### Step 1 — Read the assemblies back

Number the layers of each, in order, and confirm the order is inside face to
outside face for all of them. An assembly entered in a different direction from
its neighbour produces a matrix that looks fine and compares nothing.

### Step 2 — Fix the criteria before looking at any value

Agree the criteria list first and write it down. Criteria chosen after the
values are on the table are criteria chosen to reach an answer.

Ask which criteria are **thresholds** (must pass) and which are **trade-offs**
(more is better). Say back which is which.

### Step 3 — Build the matrix

| Criterion | Threshold or trade-off | Assembly A | Assembly B | Source per cell | Comparable? |
|---|---|---|---|---|---|

The last column is the point. Mark a row **not comparable** when one assembly has
a figure and another has `unknown`, when the two figures came from different
kinds of source, or when they were measured or modelled differently. Do not fill
a gap to make a row look complete.

### Step 4 — Report

- Which assemblies fail a threshold, and on which criterion.
- Which leads on each trade-off, among the rows that are comparable.
- **The count of rows that are not comparable**, listed by name. This number is
  reported before any conclusion, because it is what decides whether there is a
  conclusion.
- What to go and find to make the incomparable rows comparable.

If more than a couple of rows are not comparable, say plainly that the
comparison is not yet decidable and name what is missing, rather than ranking on
the rows that happen to be filled.

### Step 5 — Save, if asked

Ask whether to write the matrix to a file and where. Markdown or CSV.

## Rules

- **Never supply a value.** Not a property, not a cost, not a carbon figure, not
  as a placeholder that looks like a number.
- **Never recall a code minimum** as the threshold. Thresholds are quoted by the
  user.
- Fix the criteria before the values are visible.
- An `unknown` stays `unknown` for the whole run.
- Report the incomparable count before the conclusion, every time.
- Never rank on partial data without saying the data is partial.

## Anti-patterns

- Filling a gap with a typical figure so the table looks finished.
- Comparing a modelled value for one assembly against a tested value for
  another without flagging it.
- Adding a criterion after seeing the values.
- Ranking assemblies when half the matrix is unknown.
- Quoting a manufacturer's figure found by web search rather than from the data
  sheet the user names.
- Recommending an assembly. This command reports; you decide.
