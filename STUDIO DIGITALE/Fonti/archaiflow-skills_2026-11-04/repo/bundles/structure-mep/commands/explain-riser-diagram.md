---
title: Explain Riser Diagram
summary: Read an MEP riser diagram and find where it disagrees with the plans
discipline: structure-mep
tags: ["Reference"]
description: "Reads a plumbing, electrical, fire protection or mechanical riser diagram in plain English and then does the check nobody runs: comparing it against the architectural plans floor by floor, since a riser diagram is a schematic with no geometry and it is routinely drawn for a building whose shafts, floor levels or floor count have since changed. Explains what the diagram is showing, what it deliberately does not show, and every place it assumes something the plans do not provide. Carries no pipe or conduit sizes, no slopes and no code requirements. It does not check the engineering and does not replace the MEP engineer. For adding up the shaft space use `/size-shaft`."
argument-hint: <riser-diagram> [floor-plans]
---

# Explain Riser Diagram

A riser diagram has no scale, no geometry and no location. It says what connects
to what, vertically, and it is the only drawing in the set that shows the system
as a whole. It is also the drawing least often checked against the plans, which
is why a riser can be correct as a schematic and impossible as a building.

## Scope and limits — read first

**What this does.** Explains what the diagram shows and what it deliberately
omits, then walks it against the architectural plans floor by floor and reports
every disagreement.

**What this does not do.**

- It carries **no sizes, no slopes, no code requirements.** All from the
  engineer and from code text you quote.
- **It does not check the engineering.** Whether the system is correctly sized,
  vented, pressurised or protected is the MEP engineer's.
- It does not size the shaft. `/size-shaft` adds up the space.
- It does not replace the MEP engineer.

**What you need before starting.** The riser diagram. The architectural plans
for every level it crosses, including the roof and any below-grade level. The
floor-to-floor dimensions. The shaft locations.

## Inputs the command needs

1. **The diagram**, complete, with its legend and notes.
2. **The plans**, every level, at the same revision or with revisions stated.
3. **Floor-to-floor dimensions** and the level names as the plans use them.
4. **Shaft locations**, and what else is in them.

## Workflow

### Step 1 — Say what a riser diagram is and is not

Every run starts here:

It is a schematic. It has no scale, no plan position and no true lengths.
Vertical order is real; horizontal position is not. Two lines side by side on
the diagram may be forty feet apart in the building, and a line drawn as a
short jog may be a long horizontal run through a ceiling that has no room for
it.

### Step 2 — Explain what it shows

Walk the diagram and explain in plain English:

- What system it is, and what the legend's symbols mean.
- Where it enters the building, and from where.
- What it connects to at each level.
- Where the equipment is: pumps, tanks, valves, meters, backflow devices,
  panels, transformers, air handlers.
- What direction things flow, and whether by gravity or by pressure. Gravity is
  the constraint that decides floor levels.
- Where the system branches, and what is served by each branch.
- Anything marked future, existing, by others, or not in contract.

### Step 3 — Walk it against the plans, level by level

The check that earns the exercise:

| Level | Diagram shows | Plans show | Agree? |
|---|---|---|---|

For each level:

- Does the level exist on the plans, with the same name? Diagrams outlive floor
  count changes.
- Is there a shaft where the riser is, on that floor and on every floor between?
  A riser passing a level with no shaft is passing through something.
- Does the branch shown at that level have somewhere to go horizontally? A
  branch to a room the plans do not have is the common finding.
- Is the equipment shown at that level in a room that exists and is big enough?
- Does anything land in a rated assembly, and is that accounted for? Point at
  `design-fire-barrier`.

### Step 4 — Check the three things a schematic hides

- **Gravity.** For any gravity system, does the fall work over the real
  horizontal distance the plans imply, and does the invert at the bottom work
  with the level it has to reach? A schematic shows the slope as a line at any
  angle. Report this as a question for the engineer with the real distances
  named.
- **Horizontal runs.** Every jog on the diagram is a horizontal run somewhere.
  Name each one, say what ceiling or floor void it needs, and say whether the
  plans provide it.
- **Where it enters and leaves the building.** Compare against the civil set and
  the site plan. Point at `civil-drawing-review`.

### Step 5 — Report

- What the diagram shows, in plain English.
- The level-by-level comparison, disagreements first.
- Every horizontal run implied and whether there is room.
- The gravity questions, with real distances.
- Every level on the plans that the diagram does not show, and every level on
  the diagram the plans do not have.
- The revision dates of both, and whether they are the same issue.

Close by saying that no engineering was checked and that the diagram is a
schematic.

## Rules

- **Say what a riser diagram is, first, every run.**
- **Never state a size, a slope, or a code requirement.**
- Compare level by level, in both directions.
- Name every horizontal run the diagram implies.
- Raise gravity as a question with the real distances, never as a calculation.
- Report the revision dates of both documents.
- Never check the engineering.

## Anti-patterns

- Reading the diagram as though horizontal position were real.
- Checking the typical floor and not every floor.
- Missing that the diagram shows a level count the plans no longer have.
- Treating a jog as a detail rather than as a horizontal run.
- Calculating a gravity fall.
- Comparing documents at different revisions without saying so.
- Ignoring where the system enters the building.
