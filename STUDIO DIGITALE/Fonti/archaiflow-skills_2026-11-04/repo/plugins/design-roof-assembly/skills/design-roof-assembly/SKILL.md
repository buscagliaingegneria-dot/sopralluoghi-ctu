---
name: design-roof-assembly
description: "Builds a low-slope or steep-slope roof assembly from what the roof has to do rather than from a remembered stack: takes the membrane or covering, the deck, the climate, the interior humidity, the equipment landing on it and the slope you have to work with, then places the four control layers (water, air, vapor, thermal) in an order, gives every layer a stated job, and works the curbs, drains, penetrations and edges where roofs actually leak. Trigger on \"design a roof assembly\", \"roof build-up\", \"compact roof\", \"what goes above the deck\", \"insulation above or below the deck\", \"vented or unvented roof\", \"design-roof-assembly\", or a membrane and a deck named with a request for what sits between them. Supplies the ordering logic and the questions each condition has to answer; supplies no R-value, no permeance, no slope minimum, no code requirement and no proprietary product. The arithmetic belongs to condensation-check and the continuity audit to air-barrier-trace, both of which this hands off to."
license: MIT
metadata:
  title: "Design Roof Assembly"
  summary: "Build up a roof assembly and place the control layers a roof cannot dry through"
  discipline: "envelope-performance"
  tags: "Design"
---

# Design Roof Assembly

A wall in a temperate climate usually gets a second chance: it can dry one way
or the other. A compact roof often cannot dry in either direction, so anything
that gets into it stays. That single difference is why a roof stack has to be
decided rather than adapted from a wall.

## Scope and limits — read first

**What this does.** Takes the demands on one roof area: the covering, the deck
and what spans it, the climate, how humid the space below is meant to run, the
slope available, and what will be sitting on or passing through the roof.
Places the four control layers against those demands, states whether the
assembly can dry at all and in which direction, gives every layer a job, and
then works the conditions where roofs fail, which is almost never the field.

**What this does not do.**

- **It supplies no numbers.** No R-value, no permeance, no thickness, no minimum
  slope, no drain sizing, no fastener pattern, no code requirement. It places a
  layer and names what the layer has to achieve; the value comes from your
  manufacturer data, your climate data and your code text.
- **It does not check the stack it helped you build.** Boundary temperatures and
  the condensing plane belong to `condensation-check`. Air barrier continuity
  around the building belongs to `air-barrier-trace`. Run both on what comes out
  of here.
- It does not size drainage. How many drains, how big, where the overflow goes
  and what the roof weighs when the primary drains block: plumbing code and
  structural engineering, both quoted by you.
- **It does no structural work.** Deck span, ponding, equipment loads, uplift
  resistance and attachment: all engineering. The assembly names where those
  decisions land and hands them over.
- It does not resolve the warranty. What a manufacturer will warrant, and what
  in this stack voids it, is between you and them. It is a real constraint and
  it is not knowledge this skill has.
- One roof area at a time. Where two areas meet at a different level, that is a
  transition and it gets flagged, not resolved.
- It does not replace the roof consultant or the Architect of Record.

**What you need before starting.** The covering, or the fact that it is open.
The deck and what it is made of. The climate zone and its source. How the space
below runs: humidity, whether it is conditioned, whether it is a pool or a
kitchen or a warehouse. The slope you have and how you get it. What lands on the
roof, what passes through it, and whether anyone has to walk on it.

## Workflow

### Step 1. Take the demands, not the layers

Ask, in one message:

> 1. What is the covering, or is it open? Membrane, and adhered or ballasted or
>    mechanically attached? Or a steep-slope covering with laps?
> 2. What is the deck, and what spans it?
> 3. What climate zone, and from what source?
> 4. What runs below: conditioned or not, and how humid? A natatorium, a
>    commercial kitchen and an office are three different roofs.
> 5. Where does the slope come from: the structure, tapered insulation, or a
>    fill? And is it enough to drain, given what you have to work with?
> 6. What sits on the roof, what passes through it, and does anyone walk on it?
> 7. What is already fixed: a floor-to-floor, a parapet height, an equipment
>    layout, a warranty already selected?

If the user offers a stack instead, take it as a proposal to be tested against
the demands, not as the answer.

### Step 2. Decide whether this roof can dry at all, then place the control layers

Answer the drying question before placing anything, because it constrains every
position that follows. A compact roof with a membrane above and a vapor retarder
below has no direction to dry in; that is a legitimate design and it means the
assembly has to be built to stay dry rather than to recover.

State the answer, then present the control layers as a table with the reason
column in full sentences:

| Control layer | Where it sits | Why there | Continuous at |
|---|---|---|---|

- **Water.** The covering, and what happens to water that gets past it. Name the
  secondary drainage path or say plainly there is none.
- **Air.** Which plane stops air, and note in the last column every place it has
  to carry: down the parapet to meet the wall's air barrier, around every
  penetration, across every joint in the deck.
- **Vapor.** Whether there is a vapor retarder and on which side of the
  insulation. On a roof this is more consequential than on a wall, because a
  membrane above is already close to vapor-tight and a second retarder below
  closes the assembly from both sides.
- **Thermal.** Above the deck, below it, or split. If any is below, say plainly
  that the deck itself is then cold and the vapor question changes with it.

Where one material serves two functions, say so, and say that one failure then
takes out both.

### Step 3. Build the stack, deck upward, and read the gaps between rows

| # | Layer | Its job | Control layer? | Value needed from you |
|---|---|---|---|---|

The last column stays as questions. **A layer with no job comes out.**

Then read between the rows:

- Is anything trapped between two vapor-tight layers with no way out?
- Does a fastener pass through a control layer, and what closes it?
- Does the slope get built inside the stack, and does that change any layer's
  thickness across the roof?
- Do two materials meet that should not touch, chemically or by temperature?

### Step 4. Work the conditions, where the roof stops or gets interrupted

The field of a roof rarely fails. Name every one of these and say what each of
the four control layers does there:

- The perimeter: parapet, or edge and fascia. Where the roof's air barrier meets
  the wall's.
- Every drain and every overflow or scupper.
- Every penetration: pipes, conduit, vents, structure passing through.
- Every curb: equipment, skylights, hatches, ductwork.
- Expansion joints, and any change in deck direction or level.
- Where this roof area meets another at a different height.
- Any tie-back, davit, or fall arrest anchor already planned.

An empty list here means one was forgotten, not that the roof is simple.

### Step 5. Name the drying direction the assembly actually has

Read the stack back and state which way it can dry, or that it cannot. Compare
that to what Step 2 assumed. If the assembly turns out to be closed both ways,
say so plainly and name the consequence: every joint, curb and penetration is
now the whole waterproofing strategy, because nothing gets a second chance.

State a direction, never a rate.

### Step 6. Report, and hand off

The control layer table, the stack table with its between-row notes, the
conditions list, then prose on what is unresolved. Close with the hand-offs,
every time:

- The arithmetic has not been run. `condensation-check` takes it.
- Air barrier continuity has not been audited. `air-barrier-trace` takes it.
- Drainage sizing, structural capacity and the warranty are all open, and named
  as open.

Count the open values on the face of the output. Then ask whether to write the
assembly to a file and where, and write it directly, tables included.

## Rules

- **Never supply a number.** Not a thickness, not an R-value, not a permeance,
  not a slope, not a drain count, not as a placeholder that looks like a value.
- **Never recall a code requirement.** Minimum slope, required insulation,
  vapor retarder rules by zone, overflow provisions: all quoted by you.
- Answer the drying question before placing a layer. On a roof it constrains
  everything after it.
- Every layer carries a job in a sentence, or it comes out.
- Name every condition in Step 4 even when the answer is short.
- Say on every run that the arithmetic has not been done here, and that the
  manufacturer's warranty has not been checked against this stack.

## Anti-patterns

- Adapting a wall stack by turning it on its side. A wall can usually dry; a
  compact roof usually cannot, and the vapor decision is not the same one.
- Adding a vapor retarder below the deck by habit when the membrane above is
  already vapor-tight. That closes the assembly from both directions.
- Recalling a minimum slope, a per-inch R-value, or a "typical" tapered
  build-up because the figure feels standard.
- Quoting a code clause found by web search. Search identifies which document
  governs; it does not verify what it says.
- Calling the roof resolved with an empty conditions list.
- Treating drainage as sized because the drains are located.
- Running `condensation-check` or `air-barrier-trace` from inside this skill.
  Both are hand-offs, named and not executed.

## Resources

None. This skill is one file. Output is written directly at the path you choose.
