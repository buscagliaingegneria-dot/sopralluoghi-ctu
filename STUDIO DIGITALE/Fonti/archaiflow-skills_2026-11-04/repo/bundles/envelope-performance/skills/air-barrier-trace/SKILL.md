---
name: air-barrier-trace
description: "Traces each of the four enclosure control layers, air first, then water, vapor, and thermal, around a building section as one continuous line, and reports every joint where that line changes material, changes plane, or is crossed by something: foundation, slab edge, wall base, floor lines, window and door openings, corners and cladding changes, parapets and eaves, roof level changes, and every penetration. Each joint records what carries the layer on either side, what makes the connection, and which drawing shows it. Trigger on \"air barrier continuity\", \"trace the air barrier\", \"control layer check\", \"where does the air barrier break\", \"is the WRB continuous\", \"air-barrier-trace\", or a wall section handed over with a continuity question. The drawings, the layer assignments, and any airtightness target come from the user; the skill supplies the joint sequence and the questions asked at each one, and never names a membrane, tape, sealant, or leakage rate."
license: MIT
metadata:
  title: "Air Barrier Trace"
  summary: "Follow the air, water, vapor, and thermal layers around a section for breaks"
  discipline: "envelope-performance"
  tags: "Analysis, Design"
---

# Air Barrier Trace

Pick the air barrier up at one point on the section and walk it all the way
around without lifting the pen. Everywhere you have to lift it is a joint, and
that joint either has a detail or it does not. Water, vapor, and thermal ride
along the same walk.

## Scope and limits — read first

**What this does.** Walks the enclosure joint by joint in a fixed order, from
below grade around to the roof and back, asking the same four questions at each
one: which material carries the layer on the inside of the joint, which carries
it on the outside, what makes the connection between them, and which drawing
shows that connection. The air layer gets its own pass first, because it is the
one that leaks. Water, vapor, and thermal follow over the same joints. The
output is a table with one row per joint per layer, led by a count of the joints
no detail covers.

**What this does not do.**

- **It does not name products.** No membrane, no tape, no sealant, no
  fluid-applied product, no fastener. Whether two products bond to each other is
  a manufacturer's warranty question answered by their literature, not here.
- It does not know your airtightness target. Whatever the code or the owner's
  program demands, quote it and the trace is held against it as a stated goal.
  It is never recalled.
- **It reads what is drawn.** A joint with no detail is reported as not shown.
  It is not inferred to work because the assembly around it is conventional, and
  the missing detail does not get designed in the report.
- It checks continuity, not performance. No thermal bridge calculation, no dew
  point, no water penetration testing. Take the vapor question to
  `condensation-check` and the assembly against the energy table to
  `explain-u-value`.
- It does not sequence construction or judge whether a joint can be built in the
  order the trades actually arrive. It marks where that question has to be
  asked.
- It is not a mock-up and not a blower door test. Those find what drawings
  cannot.
- It does not replace the enclosure consultant, the Architect of Record, or the
  AHJ.

**What you need before starting.** The section or sections, the details that
exist and their sheet numbers, which material is intended to carry each layer in
each part of the enclosure, and, if the trace is to be held against a target,
the airtightness requirement quoted from the code or the owner's program.

## Workflow

### Step 1. Establish the enclosure and the layer assignments

Ask, in one message:

> 1. Which drawings are we tracing? Sections, details, sheet numbers.
> 2. For each part of the enclosure, below grade, slab, wall, roof, glazing,
>    which material carries the air layer? The water layer, the vapor layer, the
>    thermal layer?
> 3. Where does the enclosure boundary run wherever the building steps,
>    cantilevers, or meets an unconditioned space: garage, crawl space, unheated
>    stair? That boundary is a decision, not a drawing convention, and the trace
>    follows the one you name.
> 4. Is there an airtightness target? Quote it.

Say the assignments back before walking. A wall whose sheathing membrane is
meant to carry both air and water, drawn lapped for water only, should fail at
that sentence rather than thirty rows into a table.

### Step 2. Walk the air layer, joint by joint

Fixed sequence. Every joint gets a row, including the ones that do not apply to
this building, which are marked as such rather than dropped:

1. Footing and foundation wall to below-grade waterproofing
2. Foundation wall to slab edge
3. Slab or foundation to wall base
4. Wall to floor line at each level, including cantilevers and balconies
5. Wall to window and door rough openings: head, jamb, sill
6. Wall to wall at corners, and at every change of cladding or backup material
7. Wall to roof: parapet, eave, rake, and anywhere the wall passes the roof
   plane
8. Roof to roof at level changes and expansion joints
9. Penetrations: ducts, pipes, conduits, vents, structural steel, canopy and
   railing anchors
10. Every joint to an adjacent unconditioned space

If this building has something the list does not cover, an atrium, a tunnel, a
vegetated roof, add the joint and say it was added.

### Step 3. Repeat for water, vapor, and thermal

Same joints, one pass each. What to watch for, without supplying a number to
any of it:

- **Water.** The joint has to shed downward and lap with gravity. A joint that
  is airtight and lapped upward is a hole.
- **Vapor.** Which side of the insulation the low-perm layer lands on, and
  whether it switches sides anywhere along the walk. The arithmetic belongs to
  `condensation-check`.
- **Thermal.** Where the insulation stops and what carries through the gap.
  Every one of those is a thermal bridge with a name and a location.

### Step 4. Report

| Joint | Layer | Inside material | Outside material | Connection | Drawing | Status |
|---|---|---|---|---|---|---|

Status is one of four words. `detailed`, `incomplete`, `not shown`, `conflict`.
Nothing else, and no fifth word invented for a joint that is nearly fine. A
joint whose detail contradicts another detail is `conflict` and names both
sheets.

Lead the summary with the count: how many joints are `not shown` and how many
`conflict`, per layer. Not with the joints that are fine.

Then in prose: the joints where the layer changes material and plane at the same
time, since that is where continuity usually fails; the ones whose detail exists
on a sheet nobody would look at; and whatever could not be resolved from the
drawings alone.

### Step 5. Write it out

Ask where to write the table and the summary. If the project keeps an issue log
or a checklist, offer to hand the `not shown` rows to `drawing-checklist` rather
than tracking them twice.

## Rules

- **Never name a product.** Not a membrane, not a tape, not a sealant, not in an
  example.
- A joint with no detail is `not shown`. Never "assumed continuous", never
  "typical", and "by others" only when a drawing note says so, in which case the
  row says who.
- Read the layer assignments back before walking.
- The air layer gets its own pass. Tracing four layers at one joint is how the
  air answer ends up borrowed from the water answer.
- Count what is missing on the face of the output.
- Never recall an airtightness rate, and never quote one found by web search.

## Anti-patterns

- Marking a joint continuous because the assembly around it is conventional.
- Treating the water-resistive barrier and the air barrier as one line because
  one product often does both jobs. They are two requirements, they fail
  differently, and the lap and the seal are detailed separately.
- Designing the missing detail inside the report. Name what is missing; the
  detail is a design decision that goes through the normal review.
- Naming a tape or sealant that "always works there".
- Reporting a clean trace when half the joints came back `not shown`.
- Skipping the penetrations because they arrive as shop drawings. Most of them
  do, and those are exactly the ones nobody traced.

## Resources

None. This skill is one file. Output is written directly at the path you choose.
