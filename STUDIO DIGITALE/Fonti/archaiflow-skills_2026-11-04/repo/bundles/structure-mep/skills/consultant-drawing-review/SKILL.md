---
name: consultant-drawing-review
description: "Reads a drawing from any consultant — structural, mechanical, electrical, plumbing, fire protection, civil, landscape, acoustic, kitchen, security — against the architectural set, from the architect's side. Checks the things that go wrong the same way whatever the discipline: the background it was drawn on, the grids and levels, what it lands in that has to stay clear, what it defers to somebody else, and where the two sets simply disagree. Trigger on \"review the consultant drawings\", \"read this engineer's drawing\", \"do these agree with our plans\", \"they issued a set, what do we check\", \"consultant-drawing-review\", or any consultant's drawing handed over. Carries no engineering values and checks no engineering. `mep-review`, `structural-drawing-review` and `civil-drawing-review` go deeper on those three; this is the one that works for the disciplines that have no skill of their own. It does not replace the engineers or the Architect of Record."
license: MIT
metadata:
  title: "Consultant Drawing Review"
  summary: "Read any consultant's drawing against the architectural set"
  discipline: "structure-mep"
  tags: "Review"
---

# Consultant Drawing Review

Three disciplines have a review skill here and a project has eight consultants.
The acoustician, the kitchen consultant, the security consultant and the
landscape architect all issue drawings that nobody reads against the
architectural set until somebody notices a conflict on site.

The failures are the same whatever the discipline, which is why one skill covers
all of them.

## Scope and limits — read first

**What this does.** Reads any consultant's drawing against the architectural set
for the five things that go wrong regardless of discipline: the background, the
grids and levels, spatial conflicts, deferred work with no owner, and plain
disagreements between the two sets.

**What this does not do.**

- **It checks no engineering.** Not a size, not a load, not a capacity, not a
  rate. Those are sealed by somebody and second-guessing them from an
  architect's chair is useless.
- **It carries no values.**
- It does not replace the three deeper skills. `mep-review`,
  `structural-drawing-review` and `civil-drawing-review` go further on those
  disciplines; use them where they exist and this where they do not.
- It does not do penetrations. `penetration-review` builds that register.
- It does not resolve conflicts. `coordination-log` tracks them to closure.
- It does not replace the engineers or the Architect of Record.

**What you need before starting.** The consultant's drawings and the
architectural set, with both revisions stated. The architectural background the
consultant drew on. What that consultant's scope is supposed to be.

## Workflow

### Step 1. Establish what you are comparing

Ask, in one message:

> 1. Which consultant, and what is their scope?
> 2. What revision is each set, and **which architectural background were the
>    consultant's drawings drawn on?**
> 3. What are they issued for: coordination, tender, construction?
> 4. What are the architectural constraints that matter here: clear heights,
>    fixed dimensions, spaces that must stay clear?
> 5. Is there a federated model, or separate drawings?

**Question 2 first, every time.** A consultant's set drawn on a superseded
background will disagree with the current plans everywhere, and reviewing it
line by line before establishing that wastes the review and insults the
consultant. If the background is old, stop and say so.

### Step 2. Grids, levels and names

Nothing after this is meaningful if these disagree:

- Grid designations and spacing, both sets.
- Level names and their elevations, both sets.
- **What each set means by a level name.** Top of slab, finished floor, top of
  structure: the same name meaning different things is the single most
  productive source of error between two sets.
- The building outline and the north point.
- Room names and numbers, if the consultant uses them.

### Step 3. Find what lands where it cannot

Whatever the discipline, the drawing puts things in space:

| Location | What the consultant shows | What is there architecturally | Conflict |
|---|---|---|---|

Work through: anything in a room that has to stay clear, anything in a required
clearance zone, anything crossing a rated assembly, anything in a ceiling void
that is already full, anything on a wall that is glazed, anything in a shaft,
anything above a space with a fixed clear height, and anything outside the
building that lands in a route, a setback or a planting area.

Report both values on every conflict and rule on neither.

### Step 4. Find what they have deferred, and to whom

Every consultant's set defers work, legitimately, and the deferral has to land
on somebody:

- Anything marked by others, by contractor, delegated design, or to be confirmed.
- Anything shown diagrammatically that somebody will have to draw properly.
- Anything requiring a builder's work opening, a support, a plinth, or backing
  that is nobody's drawing yet.
- Anything requiring access that no ceiling or panel currently provides.

**A deferred item with no owner is a gap the architect stands in.** List each
with who should own it.

### Step 5. Find what neither set shows

The most valuable list and the hardest to produce. Go through what this
consultant's scope implies and check each appears somewhere: on their drawings,
on the architectural, or nowhere.

Report the third category individually. On a project with eight consultants,
most of what gets found on site is in that list.

### Step 6. Report

| # | Finding | Consultant shows | Architectural shows | Kind |
|---|---|---|---|---|

Kind is `background`, `grid or level`, `conflict`, `deferred`, `gap`, or
`duplicate`.

Order: background and level problems first, since they invalidate the rest, then
conflicts affecting a fixed dimension, then deferred items with no owner, then
gaps.

Close by saying no engineering was reviewed, and point at `coordination-log`.

### Step 7. Save, if asked

Ask whether to write the review to a file and where.

## Rules

- **Check the background revision before reading anything.** Stop if it is old.
- **Never check or comment on the engineering.**
- Establish what each set means by a level name.
- Report both values on every conflict and decide neither.
- List every deferred item with an owner, or flag that it has none.
- Produce the list of what neither set shows.
- Where a deeper skill exists for that discipline, name it.

## Anti-patterns

- Reviewing a consultant's set drawn on a superseded background, line by line.
- Checking whether the engineering is right.
- Assuming two sets mean the same thing by the same level name.
- Choosing which set is correct.
- Treating a deferred note as somebody else's problem by default.
- Reviewing only the disciplines that have their own skill.
- Reporting conflicts and never producing the gap list.

## Resources

None. This skill is one file. Output is written directly at the path you choose.
