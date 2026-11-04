---
name: design-expansion-joint
description: "Works movement in the enclosure as two questions rather than one: where the joints have to be, given the movements you can name and where they accumulate, and then how each of the four control layers (water, air, vapor, thermal) crosses a gap that opens and closes for the life of the building. Trigger on \"expansion joint\", \"movement joint\", \"control joint\", \"where do the joints go\", \"building separation joint\", \"how does the air barrier cross a joint\", \"design-expansion-joint\", or a long facade or a structural break named with a request for how the enclosure handles movement. Supplies the reasoning about movement sources, accumulation and joint hierarchy, and the questions each crossing has to answer; supplies no joint spacing, no movement coefficient, no joint width, no code requirement and no proprietary product. It does no structural or thermal calculation and does not replace the enclosure consultant or the Architect of Record."
license: MIT
metadata:
  title: "Design Expansion Joint"
  summary: "Place movement joints and carry the control layers across a gap that moves"
  discipline: "envelope-performance"
  tags: "Design"
---

# Design Expansion Joint

Every control layer in an enclosure is asked to be continuous. A movement joint
is the place where continuity has to survive a gap that changes width every day
for sixty years. A layer that is continuous but cannot move will tear, and it
will tear where nobody is looking.

## Scope and limits — read first

**What this does.** Separates the two questions that usually get answered
together and badly. First: where do joints belong, given the movements present,
where those movements accumulate, and where the structure has already decided
for you. Second: at each joint, how does each of the four control layers get
across, with what material, and how much movement does that material have to
take. It also sorts joints into a hierarchy, because a building separation joint
and a cladding control joint are not the same thing and should not be drawn the
same way.

**What this does not do.**

- **It supplies no numbers.** No joint spacing, no joint width, no coefficient
  of expansion, no movement range, no sealant extension capability, no code
  requirement.
- **It does no calculation.** How much a given facade moves over a given
  temperature range is arithmetic against material properties you supply, and it
  belongs with the engineer and the manufacturer. This skill names what has to be
  calculated and by whom.
- **It does no structural work.** Where the structure needs a separation joint,
  what the frame does at that joint, seismic separation, differential settlement:
  all engineering, and they arrive here as constraints.
- It does not select sealants or gaskets. It describes the movement a joint
  material has to accommodate and the direction of that movement, in enough
  detail to go shopping.
- It does not resolve the joint's appearance. Where a joint lands is a facade
  composition question as well as a technical one, and that conversation belongs
  with the elevation.
- It covers the enclosure. Interior movement joints in slabs, partitions and
  finishes follow different rules and are out of scope.
- It does not replace the enclosure consultant or the Architect of Record.

**What you need before starting.** The enclosure assemblies involved. The
structural joints already fixed, and why they are where they are. The materials
in the cladding and their movement behaviour, with a source. The building's
overall geometry: lengths, changes in direction, changes in height, and where
two structures meet. The climate range the facade will see, which is not the
same as the design temperatures used for heat loss.

## Workflow

### Step 1. Take the movements and what has already been decided

Ask, in one message:

> 1. What structural joints already exist, where, and why? Those are fixed and
>    the enclosure has to follow them.
> 2. What is the cladding, and what moves it: temperature, moisture, curing,
>    creep, or load? Name each mechanism you know about.
> 3. What is the geometry: overall lengths, re-entrant corners, changes in
>    height, wings meeting a core, an addition meeting an existing building?
> 4. What is the temperature range this facade will actually see, in the sun and
>    in winter, and from what source?
> 5. Are two structures involved, with different foundations or different ages?
> 6. What is already fixed: a facade module, a panel size, a joint pattern
>    already drawn?

Movement sources get listed separately, not merged into one allowance. Thermal
movement reverses; moisture expansion in fired clay does not; concrete shrinkage
happens once and never comes back. A single number that covers all of them
covers none of them.

### Step 2. Sort the joints into a hierarchy and place them

Not every joint is the same joint. Present the hierarchy as a table, with the
placement reasoning in full sentences:

| Joint type | What it separates | What moves across it | Where it has to be |
|---|---|---|---|

Work down the hierarchy:

- **Building separation joint.** Two structures, moving independently. The
  enclosure has no choice about where this is, and every control layer has to
  cross the largest gap in the building here.
- **Structural expansion joint.** One structure, relieved. Again fixed by
  others; the enclosure follows.
- **Enclosure movement joint.** The facade system relieving its own movement,
  which may or may not line up with the structure's. Say plainly when it does
  not, because a facade joint half a bay from a structural joint is a common and
  expensive mistake.
- **Cladding control joint.** Within one material, relieving that material's own
  behaviour. These are the ones that get placed by pattern and should be placed
  by accumulation.

Then say where movement **accumulates**: at the ends of long runs, at re-entrant
corners, at changes of height, at openings that interrupt the field. Placement
follows accumulation, not a spacing rule.

### Step 3. Work each crossing, and read the gaps

For each joint in the hierarchy, one table:

| Control layer | What crosses the gap | Movement it must take | Value needed from you |
|---|---|---|---|

- **Water.** What sheds water across a moving gap, and where water that gets in
  is collected and discharged. A joint that has no discharge is a funnel.
- **Air.** The air seal across the gap, its expected movement range and whether
  it is reachable for replacement. This is the layer most often left as a
  sealant bead doing a structural job.
- **Vapor.** Whether the vapor strategy survives the interruption, or whether
  the joint creates a path the rest of the assembly was designed to prevent.
- **Thermal.** Whether insulation is continuous across the gap, or whether the
  joint is a thermal break in the wrong sense: a straight line of missing
  insulation the full height of the building.

Then read between the rows:

- Is any single material being asked to do two of these jobs across a moving
  gap?
- Is the joint accessible for inspection and replacement, and if not, what is
  the design life of the least durable component in it?
- Does the joint change direction, and does the crossing material survive that
  corner?

### Step 4. Work the ends, corners and intersections

Joints fail where they stop and where they meet. Name every one:

- Where each joint terminates: at the roof, at grade, at a parapet, at a
  foundation.
- Where a vertical joint meets a horizontal one.
- Where a joint turns a corner, inside or outside.
- Where a joint crosses another assembly: a window, a louvre, a soffit, a
  balcony.
- Where the joint passes the roof and the below-grade waterproofing, both of
  which have their own movement provision.

### Step 5. Name what the joint cannot take

Report the limits rather than a drying direction:

- What movement was assumed, and what happens if the real movement exceeds it.
- Which component in the joint has the shortest life, and what replacing it
  involves.
- What the joint does under a seismic event, if seismic separation was named in
  Step 1, and whether that is a different requirement from thermal movement.
- Whether any part of the joint depends on adhesion, and what that adhesion is
  to.

### Step 6. Report, and hand off

The hierarchy table, the crossing tables, the ends and intersections, then the
limits. Close with the hand-offs, every time:

- The movement range has not been calculated here and has to be, against
  material properties and a stated temperature range.
- Structural and seismic separation requirements are open and belong to the
  engineer.
- Air barrier continuity across every joint belongs to `air-barrier-trace`, and
  joints are where it most often fails.
- Sealant and gasket selection against the calculated movement is open.

Count the open values on the face of the output. Then ask whether to write the
result to a file and where, and write it directly, tables included.

## Rules

- **Never supply a number.** Not a spacing, not a width, not a coefficient, not
  a movement capability, not as a placeholder.
- **Never merge movement sources into one allowance.** List them separately with
  their mechanisms; reversible and irreversible movement are different problems.
- Take structural joints as fixed and say so. The enclosure follows them.
- Place joints by accumulation, never by a remembered spacing rule.
- Every crossing names a physical material and the movement it has to take.
- Name every termination and intersection, even when the answer is short.
- Say on every run that the movement range has not been calculated here.

## Anti-patterns

- Recalling a joint spacing for a cladding material because the figure feels
  standard. Spacing depends on the material, the fixing, the exposure and the
  climate.
- Placing a facade joint near but not at a structural joint.
- Drawing the air barrier as continuous across the gap with no material named,
  or with a sealant bead expected to take movement it was never rated for.
- Treating thermal, moisture and shrinkage movement as one number.
- Quoting a code or a manufacturer's movement capability found by web search.
- Calling the joint resolved without saying where it terminates at the top and
  the bottom.
- Leaving a joint with no discharge path for water that gets into it.
- Running `air-barrier-trace` from inside this skill. It is a hand-off.

## Resources

None. This skill is one file. Output is written directly at the path you choose.
