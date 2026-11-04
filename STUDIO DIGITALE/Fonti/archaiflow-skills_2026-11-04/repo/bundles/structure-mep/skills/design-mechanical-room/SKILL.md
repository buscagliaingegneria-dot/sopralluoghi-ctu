---
name: design-mechanical-room
description: "Lays out a mechanical plant room from the equipment schedule the engineer gives you, and adds the four things that make it bigger than the equipment: the service clearances each unit needs, the route to get equipment in during construction and out at replacement, the air the room itself has to take in and exhaust, and the connections that leave it. Reports the required footprint and height against what is drawn. Trigger on \"size the mechanical room\", \"plant room layout\", \"will the AHU fit\", \"how do we get the chiller in\", \"mechanical room design\", \"design-mechanical-room\", or an equipment schedule handed over with a room to put it in. Carries no equipment dimensions, no clearances, no ventilation rates and no code requirements; all come from the engineer, the manufacturer and the code text you quote. It does not select or size equipment and does not replace the MEP engineer or the Architect of Record."
license: MIT
metadata:
  title: "Design Mechanical Room"
  summary: "Size a plant room for the equipment, the air, and getting it back out again"
  discipline: "structure-mep"
  tags: "Design"
---

# Design Mechanical Room

Plant rooms are drawn at the size the equipment occupies. They fail on the three
things that are not the equipment: the space to service it, the route to replace
it, and the air the room itself needs. All three are found after the walls are
built.

## Scope and limits — read first

**What this does.** Takes the equipment schedule and works out the architectural
room: footprint, height, access, ventilation and the connections leaving it.
Reports what is required against what is drawn.

**What this does not do.**

- **It carries no dimensions of any kind.** Not an equipment size, not a service
  clearance, not a ventilation rate, not a door width, not a code requirement.
  All from the engineer, the manufacturer's data, and code you quote.
- **It does not select or size equipment.** The engineer does. This holds space
  for what they give you.
- It does not do acoustics or vibration isolation beyond naming them as
  constraints on the room's position and construction.
- It does not size the shafts. `/size-shaft` does.
- It does not design the electrical room. `design-electrical-room` does.
- It does not address combustion air, flues, refrigerant safety or gas
  requirements from memory; each is code and each gets named as a question.
- It does not replace the MEP engineer or the Architect of Record.

**What you need before starting.** The equipment schedule with dimensions,
weights and service clearances, from the engineer or the manufacturer. What is
above and below the room. The route from outside. The room as drawn. The code
requirements for ventilation, combustion air and any hazardous equipment.

## Workflow

### Step 1. Take the schedule and the constraints

Ask, in one message:

> 1. The equipment schedule: what units, what dimensions, what weights, and what
>    service clearance each needs, with the source of each figure.
> 2. What is directly above and below this room? Occupied space over a plant
>    room is a vibration and acoustic constraint before it is anything else.
> 3. Where is the room relative to outside, and what is the route from a street
>    to the door?
> 4. What does the room need for its own air: ventilation, combustion air,
>    refrigerant safety, and what code requires each?
> 5. What is the room as drawn: footprint, height to structure, door, and what
>    is fixed about it?
> 6. Does anything need to come out and be replaced within the building's life?

### Step 2. Place the equipment with its clearances, not its footprint

| Unit | Footprint | Service clearance | Which sides | Total space | Source |
|---|---|---|---|---|---|

Service clearance is not a margin. It is specific to each side of each unit:
tube pull on a chiller, coil pull and filter access on an air handler, door
swing on a panel, space to lift a motor. Ask which sides and record the source
for each.

Say explicitly whether clearances may overlap between adjacent units. Sometimes
they may and sometimes they may not, and assuming they may is how a room is
drawn too small.

### Step 3. Work the height, which is usually the binding dimension

Height is checked less often than footprint and constrains more:

- Tallest unit, plus what has to happen above it.
- Ductwork and pipework crossing above the equipment, and their crossings.
- Structure, and whether any beam is in the way of a unit or a lift.
- Lifting equipment: is a beam or a hoist point needed, and has anyone told the
  structural engineer?
- Access to anything mounted high.

### Step 4. Work the two routes, in and out

**In, during construction.** Can each unit reach the room? Through which doors,
past which turns, in which order, and does anything have to arrive before a wall
is built? If a unit has to be craned in and the roof closed over it, that is a
sequencing requirement and it belongs on the drawings.

**Out, at replacement.** The one that is skipped. The building will outlive the
equipment. For each unit, state whether it can be removed and replaced through
the permanent route, or whether it can only come out in pieces, or not at all.

An answer of "not at all" is legitimate if it is a decision. It is a problem
when it is a discovery.

### Step 5. Work the room's own air, and its connections

- Ventilation for the room itself, combustion air where there is combustion,
  and refrigerant safety where required. Name each as a code question with the
  provision to quote, and say where the openings would have to be.
- Louvres and their position: they are on an elevation and they are an
  architectural decision made by an engineer's number.
- Drainage: floor drains, condensate, safety pans, and where they go.
- Every connection leaving the room, and which shaft it enters. Point at
  `/size-shaft`.
- Acoustic and vibration separation from what is above, below and beside.

### Step 6. Report against what is drawn

| | Required | Drawn | Difference |
|---|---|---|---|
| Footprint | | | |
| Clear height | | | |
| Door / access | | | |

Then:

- Every `not supplied` dimension, counted.
- Every clearance overlap assumed.
- Units that cannot be replaced through the permanent route.
- Every code question raised and not answered.
- What has to reach the structural engineer: weights, lifting points, openings.

### Step 7. Save, if asked

Ask whether to write the layout to a file and where.

## Rules

- **Never supply a dimension, a clearance, or a ventilation rate.**
- Record service clearance per side, with its source.
- State whether clearances may overlap; never assume they may.
- Check height as carefully as footprint.
- Work the replacement route on every run, and say plainly when a unit cannot
  come out.
- Name combustion air, refrigerant safety and ventilation as code questions
  rather than answering them.
- Send weights and openings to the structural engineer.

## Anti-patterns

- Drawing the room at the equipment's footprint plus a margin.
- Overlapping service clearances without checking whether that is permitted.
- Checking the footprint and not the height.
- Designing the construction route and not the replacement route.
- Recalling a ventilation rate or a combustion air requirement.
- Putting a louvre on the elevation without knowing what it serves.
- Placing a plant room under occupied space without raising vibration.

## Resources

None. This skill is one file. Output is written directly at the path you choose.
