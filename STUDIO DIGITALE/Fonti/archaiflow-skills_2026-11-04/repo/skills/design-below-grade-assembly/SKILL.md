---
name: design-below-grade-assembly
description: "Builds a below-grade wall or slab assembly from the water condition first: takes the groundwater regime, the soil, the structure, how the space below grade will be used and whether the waterproofing can ever be reached again, then places the water, thermal and vapor control layers in an order, gives every layer a job, and works the joints, penetrations and the at-grade transition where below-grade work actually fails. Trigger on \"below grade waterproofing\", \"basement wall build-up\", \"foundation wall assembly\", \"slab on grade vapor barrier\", \"blindside waterproofing\", \"design-below-grade-assembly\", or a foundation wall and a water table named with a request for what goes between them. Supplies the ordering logic and the questions each condition has to answer; supplies no thickness, no permeance, no hydrostatic head, no code requirement and no proprietary product. It does not size drainage, does not do geotechnical or structural work, and does not replace the waterproofing consultant or the Architect of Record."
license: MIT
metadata:
  title: "Design Below-Grade Assembly"
  summary: "Build up a below-grade wall or slab where water comes first and drying does not"
  discipline: "envelope-performance"
  tags: "Design"
---

# Design Below-Grade Assembly

Everything above grade gets inspected, maintained and eventually replaced.
Below-grade waterproofing gets buried the week it goes in and stays buried for
the life of the building. There is no drying direction, no second chance and no
access, so the ordering has to be right the first time and the sequence of the
trades is part of the design.

## Scope and limits — read first

**What this does.** Takes the water condition first, because it governs every
other decision: whether there is hydrostatic pressure, seasonally or always, and
what the drainage regime around the building is meant to be. Then places the
control layers against the structure and the intended use of the space, gives
every layer a job, and works the joints, penetrations and the at-grade
transition. It also names, explicitly, which face of the structure the
waterproofing goes on and what that does to the buildability.

**What this does not do.**

- **It supplies no numbers.** No thickness, no permeance, no hydrostatic head,
  no drainage pipe size, no depth to water table, no code requirement.
- It does not know your ground. The water table, its seasonal range, the soil,
  the chemistry, the presence of contamination or gas: all from the
  geotechnical and environmental reports, quoted by you. `geotech-report-review`
  reads that report; this assumes it has been read.
- It does not size drainage. Perimeter drain, sump capacity, discharge point and
  what happens when the sump fails: civil and plumbing engineering.
- **It does no structural work.** Retained height, lateral earth pressure,
  waterproofing that has to span a construction joint, tieback penetrations
  under load: engineering.
- It does not check the stack. There is no meaningful drying analysis here to
  hand off; `condensation-check` still applies where the below-grade wall meets
  conditioned space, and the assembly says where that boundary is.
- It does not resolve sequencing with the contractor. It names the sequencing
  decisions that are actually design decisions, which is a different thing.
- It does not replace the waterproofing consultant or the Architect of Record.

**What you need before starting.** The groundwater condition and its source. The
soil report's relevant findings. The structure: cast in place, precast, blocks,
shoring left in place. Whether excavation allows access to the outside face or
whether this has to go on blind. What the space below grade is for, and how dry
it has to be for that use. Whether the slab and the wall are poured by the same
trade in the same week.

## Workflow

### Step 1. Take the water condition first

Ask, in one message:

> 1. Is there hydrostatic pressure: always, seasonally, or never? What is the
>    source of that answer, and what is the seasonal range?
> 2. What does the geotechnical report say that bears on this: soil type,
>    drainage, chemistry, gas?
> 3. What is the structure, and how is it built?
> 4. Can you get to the outside face, or is this blindside against shoring?
> 5. What is the space for, and how dry does it have to be? An archive, a
>    parking garage and a mechanical room are three different assemblies.
> 6. Is any of it under a slab, and does the slab receive a moisture-sensitive
>    finish?
> 7. What is already fixed: an excavation line, a property line, a shoring
>    system already designed, a water management approach already agreed?

The tolerance for water is the design driver, not the waterproofing product. A
parking garage that can drain a leak and an archive that cannot are not the same
problem even with the same water table.

### Step 2. Place the control layers, water first and on a named face

Present as a table, reason column in full sentences:

| Control layer | Which face | Why there | Continuous at |
|---|---|---|---|

- **Water, positive side or negative side.** State which, and why. Positive side
  keeps water out of the structure and cannot be reached later. Negative side is
  accessible and lets the structure stay wet. This is the decision the rest
  follows from; do not leave it implied.
- **Drainage.** Whether water is drained away before it ever reaches the
  waterproofing, or whether the waterproofing is expected to hold it. Say which,
  because "waterproof plus a drain" and "drain so it never gets wet" are
  different assemblies with different failure behaviour.
- **Thermal.** Which side of the structure, and whether it survives being buried
  and wet. Note where the insulation stops relative to the frost line and
  relative to the floor slab, and say plainly that the joint between them is a
  thermal bridge nobody has quantified.
- **Vapor and gas.** Under slabs and against walls of occupied space. If a gas
  condition was named in Step 1, say here that the gas barrier is a separate
  requirement with its own continuity, not a by-product of the waterproofing.

There is no air barrier line in the ordinary sense below grade, but the
below-grade assembly still has to receive the air barrier of the wall above it.
Name where that happens.

### Step 3. Build the stack, soil face inward, and read the gaps between rows

| # | Layer | Its job | Control layer? | Value needed from you |
|---|---|---|---|---|

The last column stays as questions. **A layer with no job comes out.**

Then read between the rows:

- Is any layer required to be installed before the structure it protects exists?
  That is a sequencing constraint and it belongs in the drawings.
- Does anything have to survive backfill, and what protects it?
- Is a drainage layer trapped where it cannot discharge?
- Does a layer depend on adhesion to a surface that will be wet or dirty when
  the trade arrives?

### Step 4. Work the joints, penetrations, and the at-grade transition

Every one of these gets named, with what the water control layer does there:

- The wall-to-footing joint and the footing-to-slab joint.
- Every construction joint and every cold joint in the concrete, and what
  waterstop is doing there.
- Every penetration: services, sleeves, sumps, elevator pits.
- Every tieback or shoring element left in place that passes through the plane.
- The at-grade transition, where this assembly hands over to the wall above.
  This is the single most common failure point and it needs its own paragraph:
  which layer laps which, in which direction, and at what height above finished
  grade.
- Any planter, terrace or paving that sits over occupied space.

### Step 5. Name what happens when it leaks

There is no drying direction to report, so report the failure behaviour instead.
For this assembly, state:

- Where water would appear inside if the primary plane failed.
- Whether that location is accessible, and what repair would involve.
- Whether the space can tolerate it while a repair is arranged.
- Whether any part of the plane can be re-injected or re-treated from inside.

An assembly with no answer to the last two is not automatically wrong. It is a
risk that has to be a decision rather than an oversight.

### Step 6. Report, and hand off

The control layer table, the stack table with its between-row notes, the joints
and transitions, then the failure behaviour, then prose on what is unresolved.
Close with the hand-offs, every time:

- Drainage sizing, structural design and the geotechnical findings are open and
  belong elsewhere.
- Where this assembly meets conditioned space, `condensation-check` still
  applies at that boundary.
- The at-grade transition is a two-assembly problem and the wall above has not
  been designed here.

Count the open values on the face of the output. Then ask whether to write the
assembly to a file and where, and write it directly, tables included.

## Rules

- **Never supply a number.** Not a thickness, not a head, not a depth, not a
  permeance, not as a placeholder.
- **Never recall a code or a geotechnical value.** Both come from documents you
  quote.
- State positive side or negative side explicitly, every run. An implied answer
  here is the most expensive kind.
- Every layer carries a job in a sentence, or it comes out.
- Name the at-grade transition in its own paragraph, every run.
- Say on every run that this work is buried and unreachable, and that the
  sequencing constraints found in Step 3 have to reach the drawings.

## Anti-patterns

- Treating a damp-proofing condition and a hydrostatic condition as the same
  problem with a different product.
- Placing the waterproofing on the negative side by default because the
  excavation looks tight, without stating the consequence for the structure.
- Recalling a water table depth, a soil bearing value, or a "typical" membrane
  thickness. Those come from reports and data sheets.
- Quoting a code clause found by web search.
- Designing the wall and the slab as two assemblies that never meet.
- Leaving the at-grade lap direction to the shop drawings.
- Calling a gas barrier handled because a waterproofing membrane is present.

## Resources

None. This skill is one file. Output is written directly at the path you choose.
