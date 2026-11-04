---
name: design-fire-barrier
description: "Follows one rated assembly as a continuous surface rather than as a wall type on a plan: establishes what kind of separation it is and therefore what continuity the code demands, traces it from floor slab to deck above and along its full length, and works every place the rating is interrupted by a penetration, a joint, a duct, a door, a glazed opening or the structure it is attached to. Trigger on \"fire barrier detail\", \"rated wall continuity\", \"does this wall go to deck\", \"firestopping at the top of wall\", \"fire partition versus fire barrier\", \"rated assembly penetrations\", \"design-fire-barrier\", or a rated wall named with a question about how it is built. Carries no hourly ratings, no opening limits, no tested assembly numbers and no firestop listings; the required rating comes from `/test-fire-rating` or your code analysis, and every assembly and firestop is a tested and listed system you cite. It does not replace the fire protection engineer, the code consultant, or the Architect of Record."
license: MIT
metadata:
  title: "Design Fire Barrier"
  summary: "Follow a rated assembly from floor to deck and find where the rating stops"
  discipline: "code-life-safety"
  tags: "Design"
---

# Design Fire Barrier

A rated wall is not a wall type. It is a continuous surface that has to hold a
rating from the floor it sits on to the deck above, along its whole length, past
every duct, pipe, conduit, joint and door in it. It is drawn as a hatch on a
plan and it fails at the places the plan does not show.

## Scope and limits — read first

**What this does.** Establishes what kind of separation the assembly is, because
the continuity requirement follows from that and not from the hourly number.
Traces the assembly as a surface: up to the deck or to a rated ceiling, along
its length, around every corner and interruption. Then works each interruption
and names what has to close it and what listing that closure comes from.

**What this does not do.**

- **It carries no ratings and no limits.** Not the required hours, not the
  maximum opening area, not the number of openings permitted, not a tested
  assembly number, not a firestop system number. The required rating comes from
  your code analysis or from `/test-fire-rating`. Tested assemblies and firestop
  systems come from listings you cite.
- **It does not choose the separation type.** Whether this is a fire wall, a
  fire barrier, a fire partition, a smoke barrier or a smoke partition is a code
  determination with different continuity rules for each. State which; the skill
  will not decide it, and the difference between them is exactly what this
  hinges on.
- It does not verify a listing. Whether a tested assembly matches what you are
  building, and whether a firestop system is listed for that penetrant in that
  assembly, is checked against the listing document.
- It does no engineering. Structural attachment at the head of wall, deflection
  of the structure above, seismic movement of a rated joint: engineering, and
  they arrive here as constraints.
- It does not cover fire-resistance-rated structural elements: columns, beams,
  floor assemblies. Those are separate.
- It does not replace the fire protection engineer, the code consultant, or the
  Architect of Record.

**What you need before starting.** What kind of separation this is, and what
requires it, quoted. The required rating. The tested assembly you intend to use.
The structure above and below. What passes through it, from the MEP set if it
exists. Every door and glazed opening in it.

## Workflow

### Step 1. Establish what kind of separation it is

Ask, in one message:

> 1. What kind of separation is this, and what code section requires it? Quote
>    the section.
> 2. What is the required rating, and where did the figure come from?
> 3. What tested assembly are you using, and do you have the listing?
> 4. What is above: a deck, a rated floor assembly, a rated ceiling membrane, a
>    plenum?
> 5. What is below: a slab, a rated floor, a raised floor, a void?
> 6. Is the building sprinklered, and does that change what your quoted section
>    permits?
> 7. What passes through it, and is there an MEP set?

The kind of separation decides everything. Two assemblies with the same hourly
number can have entirely different continuity requirements, and a wall drawn to
the ceiling because "it is only a one-hour" is the most common version of this
mistake.

### Step 2. Trace the surface, top and bottom first

Report the assembly as a continuous surface:

- **Top.** Where does it terminate, and does the quoted section allow that
  termination? Deck, rated ceiling, or a rated floor above. If it stops at a
  suspended ceiling, name what makes the ceiling part of the rated assembly, or
  say that nothing does.
- **Head of wall joint.** The gap between the top of the wall and the structure,
  and the listed joint system that closes it. This joint has to accommodate
  movement and hold a rating at the same time, and that is a listed system, not
  a detail to be invented.
- **Bottom.** What it sits on, and whether the floor construction is continuous
  beneath it.
- **Ends.** Where it terminates horizontally: at another rated assembly, at an
  exterior wall, at a corner. Say what makes the junction continuous.
- **Length.** Any change in construction along its run, any offset, any place it
  steps around structure.

### Step 3. Work every interruption

For each, name what closes it and what listing that closure comes from. Leave
every number as a question.

| Interruption | Type | What closes it | Listing needed from you | Movement? |
|---|---|---|---|---|

Work through:

- **Penetrations.** Every pipe, conduit, cable tray, sleeve. Combustible and
  non-combustible penetrants are different listings.
- **Ducts.** Whether a damper is required, what kind, and how it is accessed.
  Access is a design decision and it usually appears late and badly.
- **Doors.** Rating, hardware, closer, and whether the opening is permitted at
  all in this kind of separation.
- **Glazed openings.** Whether permitted, what kind of glazing, and whether it
  is rated for temperature rise as well as flame.
- **Joints.** Head of wall, wall to wall, expansion joints crossing the barrier.
- **Structure passing through.** A beam or a column crossing the plane, and
  whether it is separately rated.
- **Recessed items.** Boxes, panels, cabinets, and whether the assembly's rating
  survives a recess in it.

### Step 4. Check the interruptions against the whole

Two questions that only make sense over the whole assembly:

- **Aggregate limits.** Does your quoted section limit the total area or number
  of openings in this kind of separation? If so, the individual openings have to
  be added up, and that total is a number you supply and check.
- **Opposite sides.** Are penetrations or recesses on opposite faces offset as
  the tested assembly requires?

### Step 5. Report

- The surface trace, top to bottom, with any termination that the quoted section
  does not appear to allow flagged.
- The interruption table, with every missing listing counted.
- Interruptions with no closure identified, listed first.
- What is on the MEP set that this assembly does not yet account for, or the
  statement that no MEP set was supplied.
- Every number still open.

Close with the standing limits: no rating was recalled, no listing was verified,
and structural and movement questions at the head of wall are open.

### Step 6. Save, if asked

Ask whether to write the trace to a file and where.

## Rules

- **Never supply a rating, an opening limit, or a listing number.**
- **Never assume the separation type.** Ask, and quote what requires it.
- Trace top and bottom before anything else. Termination is where rated walls
  most often fail.
- Every interruption names a closure and a listing, or is flagged as having
  none.
- Head of wall is a listed system, never a drawn detail.
- Say on every run that no listing was verified.
- Quoting a code clause found by web search is not quoting the code.

## Anti-patterns

- Treating the hourly number as the whole requirement and ignoring what kind of
  separation it is.
- Stopping a rated wall at a suspended ceiling with nothing making the ceiling
  part of the assembly.
- Drawing the head of wall as a sealant joint.
- Recalling a tested assembly number or a firestop system number.
- Ignoring damper access until the ceiling is drawn.
- Counting openings individually when the section limits the aggregate.
- Assuming a sprinklered building relaxes a requirement without quoting the text
  that says so.
- Treating a recessed panel as too small to matter.

## Resources

None. This skill is one file. Output is written directly at the path you choose.
