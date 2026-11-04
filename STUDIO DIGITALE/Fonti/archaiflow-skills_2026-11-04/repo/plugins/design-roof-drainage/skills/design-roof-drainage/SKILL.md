---
name: design-roof-drainage
description: "Works roof drainage as the architectural half of a problem the plumbing engineer sizes: where the falls come from and what they cost the build-up, where the drains land against the structure and the spaces below, where the secondary drainage goes and whether anyone would notice it running, and what the roof weighs if the primary drains block. Trigger on \"roof drainage\", \"where do the drains go\", \"tapered insulation layout\", \"overflow scuppers\", \"is the roof ponding\", \"design-roof-drainage\", or a roof plan with a question about falls. Carries no drain sizes, no rainfall intensities, no slope minimums and no code requirements; sizing is the plumbing engineer's against the code you quote, and the ponding load is the structural engineer's. `design-roof-assembly` builds the stack and names this as out of its scope. It does not replace the engineers or the Architect of Record."
license: MIT
metadata:
  title: "Design Roof Drainage"
  summary: "Get water off the roof, and say where it goes when a drain blocks"
  discipline: "envelope-performance"
  tags: "Design"
---

# Design Roof Drainage

The plumbing engineer sizes the drains. Everything else is architectural and it
gets decided by default: where the falls come from, what they do to the build-up
and the parapet, where the overflow discharges, and what the roof looks like
when the primary drains are blocked and the secondary system is doing its job.

## Scope and limits — read first

**What this does.** Works the architectural decisions in roof drainage: the fall
strategy, drain and overflow locations against the structure and the plan below,
the secondary system's discharge, and the consequences of each for the assembly,
the parapet and the elevation.

**What this does not do.**

- **It carries no numbers.** No rainfall intensity, no drain size, no minimum
  slope, no scupper dimension, no ponding load. Sizing is the plumbing
  engineer's against the code you quote, and the ponding case is the structural
  engineer's.
- **It does not size anything and does not calculate.** It names what has to be
  established and by whom.
- It does not build the roof stack. `design-roof-assembly` does, and it names
  drainage as out of its scope, which is the gap this fills.
- It does not do site drainage. Where the water goes after it leaves the
  building is civil. Point at `civil-drawing-review`.
- It does not resolve the roof warranty, which usually constrains what may be
  done at a drain.
- It does not replace the plumbing engineer, the structural engineer, or the
  Architect of Record.

**What you need before starting.** The roof plan and the structure under it. The
roof assembly, or the fact that it is not settled. What is below each candidate
drain location. The parapet and the elevation. The code's secondary drainage
provisions, quoted. Anything already on the roof.

## Workflow

### Step 1. Establish the roof and what is under it

Ask, in one message:

> 1. What is the roof: area, shape, level changes, and what is on it?
> 2. What is the structure, which way does it span, and is it level or already
>    sloping?
> 3. What is the assembly, or is it open? Point at `design-roof-assembly`.
> 4. What is directly below each part of the roof? A drain drops through the
>    building and lands somewhere.
> 5. Is there a parapet on every edge, and how high?
> 6. Quote the code's secondary drainage provisions: what is required, and does
>    it permit scuppers, a separate piped system, or either?
> 7. Is there a roof warranty in prospect with its own requirements?

### Step 2. Decide where the falls come from

Three ways to get slope, and the choice changes the whole assembly:

| Source | What it costs | What it constrains |
|---|---|---|
| The structure | Cheapest, and the ceiling below follows the fall | Only works where the space below tolerates it |
| Tapered insulation | Common, and the build-up varies across the roof | Thickness at the high point, and the parapet height |
| A fill or topping | Weight, and it is dead load somebody has to carry | Structure |

Say which, and say what it does to: the thinnest point of the assembly, the
parapet height at the low corner, the height at every upstand and curb, and the
door threshold at any roof access.

**A tapered layout has a thinnest point, and the assembly's performance at that
point is the assembly's performance.** Name it and say the R-value there is what
governs, not the average.

### Step 3. Place drains against three plans at once

A drain location has to work in the roof plan, the reflected ceiling plan and
the plan of the space below.

| Drain | Roof position | Structure it passes | Space below | Conflict |
|---|---|---|---|---|

- Drains want to be at the low point; structure wants them beside a beam, not
  through it.
- The pipe drops through every floor below and needs a route and a shaft. Point
  at `/size-shaft`.
- A drain over an occupied space is a leak in that space. Over an electrical
  room it is worse; say so.
- Drains at a parapet or at a level change have their own conditions.
- Keep drains away from where equipment will be set, and from the fall arrest
  and access routes.

### Step 4. Work the secondary system as a visible thing

Secondary drainage exists for when the primary blocks, and it is designed as an
afterthought because nobody expects to see it work.

- What kind: overflow scuppers through the parapet, a separate piped system with
  its own drains at a higher inlet, or both. Quote what the code permits.
- **Where does it discharge, and would anyone notice?** A piped secondary system
  discharging into the same stack as the primary hides the failure. A scupper
  discharging onto a public sidewalk is visible and is a different problem. This
  is a design decision with a maintenance consequence, and it is usually made by
  default.
- What the scupper does to the parapet and the elevation. Point at
  `design-parapet`.
- What the discharge lands on: paving, planting, an entrance canopy, a
  neighbour.

### Step 5. Name the blocked case and hand it over

If the primary drains block, water stands on the roof to the height of the
secondary inlet, and that water has weight.

State plainly:

- How deep the water stands before the secondary system takes it, as a
  question for the engineer rather than a figure.
- That the structural engineer has to check the roof for that load, and whether
  anyone has asked.
- Whether the roof deflects under that load in a way that deepens the pond,
  which is the mechanism behind roof collapses and is not obvious.
- What maintains the drains, how they are reached, and whether the strainers can
  be cleared without special access.

### Step 6. Report

The fall strategy and what it costs, the drain table with conflicts, the
secondary system with its discharge named, the blocked case. Then:

- Every value that has to be established, with who supplies it: rainfall
  intensity, drain sizing, ponding load.
- Every conflict between a drain location and the structure or the space below.
- What the thinnest point of the assembly is and what governs there.
- What has to reach the plumbing engineer, the structural engineer and the civil
  engineer.

Then ask whether to write the result to a file and where.

## Rules

- **Never supply a rainfall intensity, a drain size, a slope, or a load.**
- Say where the falls come from before placing a drain.
- Check every drain against the roof plan, the structure and the space below.
- Name where the secondary system discharges and whether anyone would notice it
  running.
- Raise the blocked-drain load as a question for the structural engineer, every
  run.
- Name the thinnest point of a tapered assembly.

## Anti-patterns

- Placing drains on the roof plan and leaving the drop to the plumbing engineer.
- Tapering insulation without checking the parapet height at the low corner.
- Reporting the assembly's average performance rather than its performance at
  the thinnest point.
- Running the secondary system into the same stack as the primary.
- A drain over an electrical room.
- Recalling a minimum slope or a rainfall figure.
- Treating the ponding case as somebody else's without naming who.
- Designing scuppers without looking at the elevation.

## Resources

None. This skill is one file. Output is written directly at the path you choose.
