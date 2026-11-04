---
name: civil-drawing-review
description: "Reads a civil set against the architectural set for the disagreements that only show up where the two meet: the finished floor against the finished grade at every door, the accessible route against the actual slopes, where utilities enter the building against where the risers are, and what the civil drawings assume about a building they were not drawn from. Reports every conflict with both values and rules on neither. Trigger on \"review the civil drawings\", \"do the civil and architectural agree\", \"grading around the building\", \"utility entry coordination\", \"civil-drawing-review\", or a civil set issued for coordination. Carries no slope limits, no cover requirements and no utility standards; accessibility limits come from the standard you quote and utility requirements from the utility. It is not civil engineering, does not check drainage design, and does not replace the civil engineer or the Architect of Record."
license: MIT
metadata:
  title: "Civil Drawing Review"
  summary: "Check the civil set against the architectural, in both directions"
  discipline: "code-life-safety"
  tags: "Review"
---

# Civil Drawing Review

The civil set and the architectural set are drawn by different people from
different base information at different times, and they meet along one line: the
building perimeter. Almost every coordination failure between them is found at a
door threshold or at a utility entry.

## Scope and limits — read first

**What this does.** Compares the two sets where they meet, in both directions,
and reports disagreements with both values rather than deciding which is right.
Works the perimeter door by door and the utilities entry by entry.

**What this does not do.**

- **It is not civil engineering.** It does not check drainage capacity, pipe
  sizing, detention volume, pavement design or erosion control. Those are the
  civil engineer's and this does not second-guess them.
- **It carries no limits.** Accessible route slopes come from the accessibility
  standard you quote; cover, separation and clearance requirements come from the
  utility and the jurisdiction.
- It does not review the survey. `survey-review` does, and a civil set drawn on
  a survey nobody reviewed inherits every gap in it.
- It does not resolve conflicts. It names them with both values.
- It does not replace the civil engineer or the Architect of Record.

**What you need before starting.** Both sets, at the same revision or with the
revisions stated. The finished floor elevations. The accessibility standard, if
the accessible route is to be checked. The utility requirements, if available.

## Workflow

### Step 1. Establish what you are comparing

Ask, in one message:

> 1. What revision is each set, and were they issued from the same architectural
>    background? A civil set drawn on a superseded plan is the most common
>    finding and it is a process problem.
> 2. What are the finished floor elevations, and in what datum? Both sets in the
>    same datum?
> 3. Which accessibility standard applies, and can you quote its slope
>    provisions?
> 4. Which utilities serve the building, and are their requirements available?
> 5. Has the survey been reviewed?

**A datum mismatch between the sets makes every elevation comparison
meaningless.** Check it first and stop if they differ.

### Step 2. Walk the perimeter, door by door

Every door in the building envelope, including the ones nobody thinks about:
service, refuse, plant, emergency exits.

| Door | FFE | Grade at door (civil) | Difference | Threshold condition | Landing shown? |
|---|---|---|---|---|---|

- Does the difference work with the threshold detail, or does it need a step, a
  ramp, or regrading?
- Is there a level landing outside, and does the civil grading actually produce
  one?
- Does water run toward the door? A grade that falls to the building is a
  finding whatever the threshold looks like.
- Is the door on the accessible route, and if so does the grading support it?

An exit door that discharges onto a slope is both an accessibility and an egress
finding, and it is invisible in either set alone.

### Step 3. Trace the accessible route across both sets

Follow the route from the accessible parking or the property line to the
entrance, and at every segment compare the civil slopes against the standard you
quoted:

- Running slope and cross slope along each segment.
- Landings at every change of direction and at every door.
- Where the route crosses a drive aisle or a drop-off.
- Where curb ramps are and whether the route actually uses them.
- What the route does in the rain, and where water crosses it.

Report each segment with the civil slope and the quoted limit. Never state a
limit that was not supplied.

### Step 4. Work the utilities, entry by entry

| Service | Enters where (civil) | Riser or room (arch) | Agree? | Invert / depth | Clearance to others |
|---|---|---|---|---|---|

- Does each service enter where the building has somewhere for it to go?
- Do inverts work with the building's floor levels, especially for gravity
  drainage? A sanitary invert that is above the level it has to serve is a
  scheme problem, not a coordination note.
- Do services cross each other, or cross foundations, at conflicting depths?
- Are meters, backflow devices, transformers and fire department connections
  located on both sets, in the same place, and is each accessible?
- Does anything land inside a required setback, an easement, or a fire access
  route?

### Step 5. Read the rest of the perimeter

- Retaining walls: shown on both sets, at the same height, and whose scope?
- Site walls, steps and railings: on which set, and detailed by whom?
- Below-grade structure against the grading, and whether the waterproofing
  extends to the right height. Point at `design-below-grade-assembly`.
- Trench drains, area drains and their relationship to the building line.
- Fire access route against the building, and whether the grading supports the
  loads and slopes the fire department requires.
- Landscape over structure, and who carries the build-up.

### Step 6. Report

| Finding | Architectural says | Civil says | Kind |
|---|---|---|---|

Kind is `conflict`, `gap` (neither set shows it), or `duplicate` (both show it,
which will eventually disagree).

**Report both values and rule on neither.** Then:

- Findings ordered by consequence: anything affecting a floor level, a gravity
  invert or the accessible route first.
- Everything neither set shows, listed. This is the most valuable list and the
  hardest to produce.
- What could not be checked and why.

### Step 7. Save, if asked

Ask whether to write the review to a file and where.

## Rules

- **Check the datum first** and stop if the two sets differ.
- **Never supply a slope limit, a cover depth, or a utility requirement.**
- Walk every door, including service and exit doors.
- Report both values on every conflict and decide neither.
- Report gaps as well as conflicts.
- Never check drainage design or pipe sizing.

## Anti-patterns

- Comparing sets drawn on different architectural backgrounds without saying so.
- Checking the main entrance and not the service doors.
- Recalling an accessible route slope limit.
- Reviewing the civil set as though it were the civil engineer's work to
  approve.
- Resolving a conflict by choosing the architectural value.
- Missing the gravity invert problem because both sets are internally
  consistent.
- Treating a retaining wall shown on both sets as coordinated.

## Resources

None. This skill is one file. Output is written directly at the path you choose.
