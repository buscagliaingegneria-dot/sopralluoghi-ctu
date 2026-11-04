---
name: structural-drawing-review
description: "Reads a structural set the way an architect has to: not to check the engineering, but to find where the structure and the architecture disagree, where the frame lands in a space that has to stay clear, where a member's depth eats a ceiling, where the drawings defer something to a delegated design nobody has scoped, and where the structural set assumes an architectural layout that has since changed. Reports every conflict with both values and rules on neither. Trigger on \"review the structural drawings\", \"does the structure work with the plan\", \"beam depth coordination\", \"is this deferred to a delegated design\", \"structural-drawing-review\", or a structural set issued for coordination. Carries no loads, no spans and no code requirements; it does not check or second-guess the engineering. The counterpart for MEP is `mep-review`. It does not replace the structural engineer or the Architect of Record."
license: MIT
metadata:
  title: "Structural Drawing Review"
  summary: "Read a structural set against the architectural, from the architect's side"
  discipline: "structure-mep"
  tags: "Review"
---

# Structural Drawing Review

The architect is not going to check the engineering and should not try. What the
architect has to check is the other thing, and nobody else does it: whether the
frame that was designed fits the building that was drawn, and whether the
structural set still assumes a plan that has moved.

## Scope and limits — read first

**What this does.** Compares the structural set against the architectural set
and reports the disagreements, the spatial conflicts, and the work the
structural drawings have deferred to somebody who may not know it.

**What this does not do.**

- **It does not check the engineering.** Not loads, not spans, not member sizes,
  not connections, not lateral systems, not foundations. Those are the
  engineer's, they are sealed, and second-guessing them from an architect's
  chair is both useless and unwise.
- **It carries no values.** No spans, no depths, no loads, no code
  requirements.
- It does not cover MEP coordination. `mep-review` reads that set, and
  `penetration-review` covers holes through structure.
- It does not read the geotechnical report. `geotech-report-review` does, and
  the structural set should be consistent with it.
- It does not replace the structural engineer or the Architect of Record.

**What you need before starting.** Both sets, at stated revisions. The
architectural background the structural set was drawn on. The general notes and
the specification sections referenced. The geotechnical report, if foundations
are in scope.

## Workflow

### Step 1. Establish what you are comparing

Ask, in one message:

> 1. What revision is each set, and was the structural set drawn on the current
>    architectural background?
> 2. What phase, and what is the structural set issued for?
> 3. Do you have the general notes and the drawings they reference?
> 4. Has the geotechnical report been reviewed, and does the structural set cite
>    it?
> 5. What is fixed architecturally that the structure has to work around:
>    ceiling heights, clear spans, openings, a facade module?

**A structural set drawn on a superseded architectural background is the most
common and the most expensive finding**, and it is answered by a question rather
than by reading drawings.

### Step 2. Compare grids, levels and datums first

Nothing after this is meaningful if these disagree:

- Grid lines: same designations, same spacing, same origin on both sets.
- Levels: same names, same elevations, same datum.
- Whether structural levels are top of steel, top of slab, or finished floor,
  and whether the architectural set means the same thing by the same name. This
  one difference produces more errors than any other.
- Building outline and any relationship to the property line.

### Step 3. Find the structure that lands in the architecture

Walk the plans together and report every conflict:

| Location | Structure | Architecture | Conflict | Both values |
|---|---|---|---|---|

- Columns in rooms, in corridors, in unit layouts, in parking bays, in the
  middle of a door.
- Braced frames and shear walls where the plan wants an opening or a glass line.
- Transfer structure, and what its depth does to the floor below.
- Beams crossing where the ceiling has to be highest.
- Foundations conflicting with a lift pit, a shaft, a sump, or a below-grade
  wall.
- Slab edges, steps and depressions against the architectural floor finishes.
- Anything landing in the working clearance of an electrical room or the service
  space of a plant room.

### Step 4. Work the vertical dimension, which is where ceilings are lost

Structural depth is the constraint the architecture feels most:

- Deepest member in each area, against the floor-to-floor and the required clear
  height.
- Where members cross, and what the depth is at the crossing.
- Where services have to pass under, over, or through structure, and whether
  penetrations through members are shown and permitted. Point at
  `mep-review`.
- Slab thickness and any topping, against the floor build-up the architecture
  assumes.
- Roof structure against the roof build-up and the drainage falls.

Report the clear height available in each area against what the architecture
requires, as two figures.

### Step 5. Find what has been deferred, and to whom

The most valuable pass and the easiest to skip. Structural sets defer work
routinely and legitimately, and the deferral has to land on somebody:

- Anything marked delegated design, design-build, or by others: connections,
  cold-formed framing, stairs and railings, curtain wall attachment, precast,
  joists, canopies, elevator rail loads.
- For each: who designs it, who reviews it, whose seal, when it is submitted,
  and is it in anybody's fee?
- Anything marked to be confirmed, by supplier, or subject to shop drawings.
- Whether the specification carries the delegated design requirements the
  drawings assume.

A delegated item with no owner is a gap the architect stands in.

### Step 6. Report

| # | Finding | Structural says | Architectural says | Kind |
|---|---|---|---|---|

Kind is `conflict`, `gap`, `duplicate`, or `deferred`. Report both values on
every conflict and rule on none.

Then, in order:

- Grid, level and datum disagreements, first. Everything else waits on them.
- Conflicts affecting clear height or a fixed architectural dimension.
- Deferred items with no owner.
- What could not be checked and why.

Close by saying the engineering was not reviewed.

### Step 7. Save, if asked

Ask whether to write the review to a file and where.

## Rules

- **Never check or comment on the engineering.**
- **Never supply a span, a depth, or a load.**
- Compare grids, levels and datums before anything else, and stop if they
  disagree.
- Establish what each set means by a level name.
- Report both values on every conflict and decide neither.
- List every deferred item with who owns it, or flag that nobody does.
- Say what was not supplied and therefore not reviewed.

## Anti-patterns

- Checking whether a beam is big enough.
- Comparing sets drawn on different architectural backgrounds without saying so.
- Assuming top of steel and finished floor mean the same thing.
- Reporting a column conflict and choosing which drawing is right.
- Treating a delegated design note as somebody else's problem.
- Checking plan conflicts and not clear heights.
- Reviewing without the general notes.

## Resources

None. This skill is one file. Output is written directly at the path you choose.
