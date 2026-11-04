---
name: design-electrical-room
description: "Lays out an electrical, communications or service entrance room around the working clearances that surround the equipment rather than around the equipment itself, because those clearances are code, they are volumes, and they appear on no architectural drawing by default. Works the utility's own requirements separately from the code's, since a service entrance room is designed to the utility's standard and they will refuse a room that meets the code and not their manual. Trigger on \"electrical room layout\", \"how big does the switchgear room need to be\", \"working clearance in front of the panel\", \"service entrance room\", \"transformer vault\", \"design-electrical-room\", or an electrical equipment schedule with a room to put it in. Carries no clearance dimensions, no equipment sizes and no utility requirements. It does not do electrical design and does not replace the electrical engineer or the Architect of Record."
license: MIT
metadata:
  title: "Design Electrical Room"
  summary: "Lay out an electrical room around the clearances that cannot be built on"
  discipline: "structure-mep"
  tags: "Design"
---

# Design Electrical Room

An electrical room is mostly empty space that cannot be used, and the empty
space is the design. Working clearance is a code-defined volume in front of and
around equipment, it is not negotiable, and because nothing draws it, storage
and conduit and joinery end up inside it.

## Scope and limits — read first

**What this does.** Establishes the working clearances from the code text you
quote, places equipment so they do not conflict, works the utility's separate
requirements where there is a service entrance, and reports required against
drawn.

**What this does not do.**

- **It carries no dimensions.** Not a working clearance, not a headroom, not an
  equipment size, not a door width, not a utility requirement. All from code
  text you quote, manufacturer data, and the utility's own standard.
- **It does not do electrical design.** Sizing, selection, coordination and
  fault current are the electrical engineer's.
- It does not read a panel schedule. `/explain-panel-schedule` does.
- It does not size shafts or design the mechanical room.
- It does not cover generators, fuel storage or emergency systems beyond naming
  them as separate problems with their own requirements.
- It does not replace the electrical engineer or the Architect of Record.

**What you need before starting.** The equipment schedule with dimensions, from
the engineer. The code text on working clearance and dedicated space, quoted.
The utility's requirements, if there is a service entrance. What is above and
around the room. The route in. The room as drawn.

## Workflow

### Step 1. Establish the equipment, the code text, and the utility

Ask, in one message:

> 1. The equipment: what, how many, dimensions, and mounting. Switchgear,
>    panelboards, transformers, meters, controls, communications racks.
> 2. Quote the code's working clearance and dedicated space provisions. Both;
>    they are different requirements and the second one is the one nobody knows
>    about.
> 3. Is this a service entrance room? If so, do you have the utility's own
>    requirements document?
> 4. What is above the room, and is there anything wet up there?
> 5. What is the route in, and does anything need replacing in the building's
>    life?
> 6. The room as drawn: footprint, height, doors, and what is fixed.

**A service entrance room is designed to the utility's manual.** The utility
will refuse a room that meets code and not their standard, they refuse late, and
their requirements are not in any code book.

### Step 2. Draw the clearance volumes before placing anything

For each item of equipment:

| Equipment | Working clearance | Which faces | Height of the zone | Source quoted |
|---|---|---|---|---|

Two things get missed, every time:

- **It is a volume, not a setback.** It has a height, and nothing may be in it
  at any level, including a duct crossing above.
- **Dedicated space is a separate requirement.** The space above certain
  equipment is reserved for its own conduits and nothing else may pass through
  it. A duct or a pipe crossing that zone is a violation that gets found at
  inspection.

State whether clearance zones may overlap each other. Quote the text; do not
assume.

### Step 3. Place the equipment so no zone is compromised

Work through and report each conflict:

- Equipment facing equipment across a shared clearance.
- A door swinging into a clearance zone.
- A structural element inside a zone.
- Anything crossing a dedicated space above.
- Equipment whose clearance extends past the room's wall.

Then check the exits: rooms with large equipment often require more than one way
out, or doors that swing out with panic hardware. Quote the provision; do not
recall it.

### Step 4. Work what must not be in the room, and what must not be above it

Electrical rooms have exclusions that surprise architects:

- Piping, ducts and equipment foreign to the electrical installation are
  generally not permitted in the room. This includes the sprinkler main somebody
  routed through it.
- Wet areas above an electrical room are a problem. Ask what is above and what
  is in it.
- Storage will happen unless the room is too full to allow it. Say so.

Each of these is a code question with text to quote and each is worth raising
before the ceiling is coordinated.

### Step 5. Work heat, access and the route

- **Heat.** The equipment produces it and the room has to lose it. Ventilation
  or cooling is a requirement, it comes from the engineer, and it means either a
  louvre on an elevation or a duct into the room. Name it.
- **Route in and out.** Same as any plant room: can it get in during
  construction, and can it be replaced later? Transformers and switchgear are
  heavy and are craned or skated; ask early.
- **Height.** Equipment height plus what runs above it plus the dedicated space
  zone. Height is usually binding.
- **Structure.** Weights and any floor opening go to the structural engineer.

### Step 6. Report against what is drawn

| | Required | Drawn | Difference |
|---|---|---|---|
| Footprint | | | |
| Clear height | | | |
| Doors and exits | | | |

Then:

- Every clearance conflict, individually.
- Every dedicated space crossed by something.
- Every `not supplied` dimension, counted.
- Utility requirements not yet obtained, if this is a service entrance.
- Every code question raised and not answered.
- What goes to the structural engineer and to the mechanical engineer.

### Step 7. Save, if asked

Ask whether to write the layout to a file and where.

## Rules

- **Never supply a clearance, a dimension, or a utility requirement.**
- Treat working clearance as a volume with a height, every run.
- Ask about dedicated space separately from working clearance.
- Obtain the utility's own standard for any service entrance room, and say when
  it has not been obtained.
- Check what is above the room.
- Raise the foreign-systems exclusion before ceiling coordination.
- Send weights and openings to the structural engineer.

## Anti-patterns

- Treating working clearance as a floor setback.
- Routing a duct or a sprinkler main above switchgear.
- Designing a service entrance room to the code and not to the utility's manual.
- Recalling a clearance dimension.
- A door swinging into a clearance zone.
- Placing a wet room above.
- Sizing the room for the equipment and adding a margin.
- Leaving heat removal to be discovered during ceiling coordination.

## Resources

None. This skill is one file. Output is written directly at the path you choose.
