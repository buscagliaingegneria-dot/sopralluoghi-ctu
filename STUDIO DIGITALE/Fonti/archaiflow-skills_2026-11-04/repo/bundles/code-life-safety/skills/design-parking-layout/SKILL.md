---
name: design-parking-layout
description: "Lays out a parking floor from the module rather than from the space left over: settles the bay and aisle dimensions and the column grid that follows from them, works the ramp against the floor-to-floor it has to climb, places accessible spaces where the standard requires them rather than where they fit, and reports the count achieved against the count required. Trigger on \"parking layout\", \"how many cars fit\", \"parking bay module\", \"ramp slope and transitions\", \"where do the accessible spaces go\", \"design-parking-layout\", or a garage floor plate with a count to hit. Carries no bay dimensions, no aisle widths, no ramp slopes, no headroom and no accessible ratios; every one comes from the jurisdiction's standard or the accessibility standard you quote. `/test-parking` counts what is required. It does not do traffic or structural engineering and does not replace the Architect of Record."
license: MIT
metadata:
  title: "Design Parking Layout"
  summary: "Lay out parking around the bay, the aisle, and the ramp"
  discipline: "code-life-safety"
  tags: "Design"
---

# Design Parking Layout

Parking is drawn last, into whatever the building left, and then the count comes
up short. It works the other way round: the bay and the aisle set a module, the
module sets the column grid, and the grid is a structural decision that has to
be made before the floors above are planned.

## Scope and limits — read first

**What this does.** Settles the module, works the grid that follows, works the
ramp against the floor-to-floor, places the accessible spaces to the standard,
and reports the count against what is required.

**What this does not do.**

- **It carries no dimensions.** No bay width or length, no aisle width, no ramp
  slope or transition length, no headroom, no accessible space or aisle
  dimension, no accessible ratio. Every one comes from the jurisdiction's
  parking standard, the accessibility standard, or the code you quote.
- It does not count what is required. `/test-parking` does that against the
  zoning table, and this takes its output as the target.
- It does not do traffic engineering. Queuing at the entrance, the street
  movement and the impact study are `senior-traffic-engineer`'s.
- It does not do structural engineering. The grid it produces is a proposal to
  take to the engineer.
- It does not do ventilation, drainage, or fire protection of the garage. Each
  is code and each is named as a question.
- It does not replace the Architect of Record.

**What you need before starting.** The required count, from `/test-parking`. The
plate and the levels. Floor-to-floor. The jurisdiction's parking standard and
the accessibility standard, quoted. Where the entrance is, from
`site-access-study`. What is above.

## Workflow

### Step 1. Establish the standards and the target

Ask, in one message:

> 1. What count is required, and from what? Point at `/test-parking`.
> 2. Quote the jurisdiction's parking standard: bay dimensions, aisle widths by
>    angle, ramp slopes and transitions, headroom, and whether compact or
>    tandem spaces are permitted and in what proportion.
> 3. Quote the accessibility standard's provisions: how many, of what kind,
>    dimensions, access aisles, and where they have to be relative to the
>    entrance.
> 4. What is the plate, how many levels, and what is the floor-to-floor?
> 5. Where does the entrance come in, and at what level? Point at
>    `site-access-study`.
> 6. What is above: is this under a building whose grid is already set, or free?
> 7. Is any of it below grade? Point at `design-below-grade-assembly`.

Question 6 decides the exercise. A garage under a set grid is a fitting problem;
a free garage sets its own grid and the building above may have to follow.

### Step 2. Settle the module, then the grid

The module is the bay plus the aisle plus the bay. Work it from the quoted
dimensions and state the arithmetic. Then:

- How many bays fit between columns, and what column spacing that implies.
- Whether the column sits between bays or in one. A column in a bay costs a
  space or makes the bay unusable; a column between bays sets the spacing.
- What the module does to the plate: how many modules fit, and what is left over
  at the edges.
- Whether the angle is worth changing. Ninety degrees, sixty and forty-five give
  different bay counts per length and different aisle widths, and the trade is
  real.

**Report the grid as a proposal to the structural engineer**, with what it costs
if it has to change.

### Step 3. Work the ramp against the floor-to-floor

The ramp is the constraint that most often removes spaces:

- What rise does it have to climb, and over what length at the quoted slope?
- Transitions at the top and bottom, which are shallower and take more length.
- Whether the ramp is a separate structure or a sloped floor with parking on it,
  and whether the standard permits parking on a slope of that grade.
- One-way or two-way, and what that does to the aisle it feeds.
- Where the ramp lands on each level, and what it does to the layout there.
- Headroom under the ramp and over it, and where the low point is against the
  quoted clearance. **Vans and accessible routes need more, and the accessible
  spaces have to be reachable at that clearance the whole way.**

### Step 4. Place the accessible spaces where the standard requires

Not where they fit at the end:

- The number and kind required, from the quoted standard.
- Where they must be relative to the accessible entrance, quoted.
- The access aisle beside each, whether it may be shared, and which side.
- The clearance on the route from the space to the entrance, including under the
  ramp and at the lift lobby.
- Where the accessible route crosses a drive aisle, and what happens there.
- Whether any of them are on a slope, and whether the standard permits it.

Point at `accessibility-specialist` for the route as a journey.

### Step 5. Count, and report what the layout costs

| Level | Standard | Compact | Tandem | Accessible | Total |
|---|---|---|---|---|---|

Then:

- Total achieved against total required, and the difference.
- What each constraint cost, itemised: the ramp, the columns, the entrance, the
  stair and lift cores, the plant, the turning space at dead ends.
- Whether compact or tandem spaces are being used to reach the number, and
  whether the quoted standard permits that proportion.
- What one more level, or a different angle, or a different grid would change.

### Step 6. Report what is out of scope and unresolved

Name each with who takes it:

- Ventilation of an enclosed garage, and whether it is mechanical.
- Drainage, and where water from vehicles goes.
- Fire protection and whether the garage is a separate occupancy. Point at
  `senior-code-consultant`.
- Structural loading and the grid proposal.
- Lighting and security sightlines.
- EV provision, which is increasingly required and changes the electrical room.
  Point at `design-electrical-room`.

Then ask whether to write the layout to a file and where.

## Rules

- **Never supply a bay, aisle, slope, headroom, or accessible ratio.**
- Settle the module before drawing anything, and report the grid as a proposal
  to the engineer.
- Work the ramp against the actual floor-to-floor, including transitions.
- Place the accessible spaces to the standard, before the count is optimised.
- Report what each constraint cost in spaces.
- Name the out-of-scope items every run.

## Anti-patterns

- Drawing parking into the space the building left.
- Setting the column grid without checking how many bays fit between.
- Forgetting the ramp transitions, which are the longest part.
- Placing accessible spaces last, wherever there is room.
- Recalling a bay dimension or an aisle width.
- Hitting the count with compact spaces without checking the permitted
  proportion.
- Ignoring headroom on the accessible route under the ramp.
- Treating garage ventilation and drainage as somebody else's without naming
  who.

## Resources

None. This skill is one file. Output is written directly at the path you choose.
