---
name: design-wall-assembly
description: "Builds an exterior wall assembly from what the wall has to do rather than from a remembered stack: takes the cladding, the structure, the climate, the fire and acoustic demands and the drying direction you state, then places the four control layers (water, air, vapor, thermal) in an order, gives every layer a stated job, and works each interface where two layers meet and each transition where the wall stops. Trigger on \"design a wall assembly\", \"wall build-up\", \"what goes in this wall\", \"layer the exterior wall\", \"where does the air barrier go\", \"rainscreen build-up\", \"design-wall-assembly\", or a cladding and a structure named with a request for what sits between them. Supplies the ordering logic and the questions each interface has to answer; supplies no R-value, no permeance, no code minimum and no proprietary product. The arithmetic on the finished stack belongs to condensation-check and the continuity audit to air-barrier-trace, both of which this hands off to."
license: MIT
metadata:
  title: "Design Wall Assembly"
  summary: "Build up an exterior wall layer by layer and place its four control layers"
  discipline: "envelope-performance"
  tags: "Design"
---

# Design Wall Assembly

Most wall assemblies get drawn by recalling one that worked somewhere else. That
is how a vapor retarder ends up on the wrong face for the climate, and how an
air barrier gets drawn across a wall with nothing said about where it ties into
the roof. This starts from what the wall has to do and puts the layers in an
order you can defend line by line.

## Scope and limits — read first

**What this does.** Takes the demands on one exterior wall type: the cladding
you have chosen or been given, the structure behind it, the climate, the fire
rating and acoustic separation it has to carry, and which direction you intend
it to dry. Places the four control layers against those demands, in an order,
with the reason for each position stated. Gives every remaining layer a job, and
removes any layer that cannot be given one. Then works the interfaces: what
happens where two layers meet, and what happens at every place the wall stops,
which is where assemblies actually fail.

**What this does not do.**

- **It supplies no numbers.** No R-value, no permeance, no thickness, no
  cavity depth, no fastener spacing, no minimum required by any code. It places
  a layer and names what the layer has to achieve; what value achieves it comes
  from your manufacturer data, your climate data and your code text.
- **It does not check the stack it helped you build.** Boundary temperatures and
  the condensing plane are arithmetic, and they belong to `condensation-check`.
  Whether the air barrier is actually continuous around the building belongs to
  `air-barrier-trace`. Run both on what comes out of here. A wall that is
  correctly ordered can still condense.
- It does not know your code. Which vapor retarder class your climate zone
  permits, whether continuous exterior insulation is required and in what ratio
  to cavity insulation, what the assembly has to achieve for fire and how it has
  to be tested: all code text. Quote it and the assembly gets held against it.
  It will not be recalled.
- It does not select products. It will describe the job a layer has to do in
  enough detail for you to go shopping. It will not name the product, and a
  named product in your input is carried as your decision, not endorsed.
- **It does no structural work.** Backup wall spanning, shelf angles, cladding
  attachment through continuous insulation, wind load on the cladding: all of
  that is engineering. The assembly names where those decisions land and hands
  them over.
- One wall type at a time. A building has several, and they meet each other; the
  transitions section flags those meetings rather than resolving them.
- It does not replace the enclosure consultant or the Architect of Record.

**What you need before starting.** The cladding, or the fact that it is still
open. The structure behind the wall. The climate zone and where it came from.
The drying direction you intend and why. Any fire rating and acoustic separation
the wall has to carry, quoted from the source that requires them. If the project
has a `docs/jurisdiction.md`, say so and the code questions get pointed at it
rather than asked twice.

## Workflow

### Step 1. Take the demands, not the layers

Ask, in one message:

> 1. What is the cladding, or is it still open? If it is fixed, say how it is
>    attached and whether it is drained and vented behind.
> 2. What is the structure behind the wall: the backup, and whether the
>    insulation can pass outside it uninterrupted.
> 3. What climate zone, and from what source?
> 4. Which direction do you intend this wall to dry, and why? Inward, outward,
>    or both.
> 5. What rating and separation does it carry, quoted from what requires them?
> 6. What is already fixed by something outside this wall: floor-to-floor
>    dimension, window type, a facade module already set, a budget already
>    committed?

If the user offers a layer stack instead, take it, but treat it as a proposal to
be tested against the demands rather than as the answer. Ask for the demands
anyway.

### Step 2. Place the four control layers first

Before any material is named, decide where each of the four planes sits and say
why. Present as a table and fill the reason column in full sentences:

| Control layer | Where it sits | Why there | Continuous at |
|---|---|---|---|

- **Water.** Which plane sheds bulk water, and where it drains to. Name the
  plane, not the product. A drained cavity and a face-sealed wall are different
  decisions and everything downstream changes with them.
- **Air.** Which plane stops air. It has to be continuous, so name the surface
  it lives on and, in the last column, every place it has to carry across:
  to the roof, to the below-grade waterproofing, around the openings, through
  the floor lines.
- **Vapor.** Which plane, if any, controls diffusion, and on which face of the
  insulation. This is the one most often placed by habit. The drying direction
  from Step 1 decides it, not what was on the last project.
- **Thermal.** Where the insulation sits relative to the structure. Whether any
  of it is continuous outboard of the backup, and if it is not, say plainly that
  the framing is a thermal bridge nobody has quantified yet.

Two of these can share a material. Say so explicitly when they do, and note that
a shared plane means one failure takes out two functions.

### Step 3. Build the stack, outside face inward, and read the gaps between rows

List every layer in order, and give each one a job in a sentence. Present as a
table:

| # | Layer | Its job | Control layer? | Value needed from you |
|---|---|---|---|---|

The last column is where the numbers would go and do not. Write what has to be
established (a thermal resistance, a permeance class, a rating) and who supplies
it. Leave it as a question.

**A layer with no job comes out.** If a layer is in the stack because it is
usually there, that is not a job. Say so and remove it, or find the job.

Then read the table again, this time between the rows. For each pair of adjacent
layers ask what happens where they meet, and report only the pairs with an
answer worth writing down:

- Does one layer need a gap behind it, and is the gap drained, vented, or both?
- Is anything trapped between two layers that cannot dry?
- Does a fastener pass through a control layer, and what closes it?
- Do two materials meet that should not touch, chemically or galvanically?

### Step 4. Work the transitions, where the wall stops

This is the step that gets skipped and the one that gets called back. For each
place this wall ends, state what each of the four control layers does there:

- Base of wall, and how it meets the below-grade waterproofing
- Head of wall, and how it meets the roof
- Each opening: head, jamb, sill
- Floor lines and any shelf angle
- Where this wall type meets the next wall type
- Inside and outside corners
- Any penetration the program already knows about

A control layer that cannot be carried through a transition is not continuous,
whatever the wall section shows in the field.

### Step 5. Name the drying direction the assembly actually has

Read the stack back and say which way it can dry, based on where the lowest-perm
layers landed. Compare that to the intent stated in Step 1. If they disagree,
say so plainly and name which layer to move; do not quietly adjust the intent to
match the drawing.

State the direction, never a rate. There is no drying model here.

### Step 6. Report, and hand off

The control layer table, the stack table with its between-row notes, the
transitions, then prose on what is unresolved. Close with the three hand-offs,
every time:

- The arithmetic on this stack has not been run. `condensation-check` takes it.
- The continuity of the air barrier around the building has not been audited.
  `air-barrier-trace` takes it.
- Every value in the last column of the stack table is still open, and the code
  requirements are still unquoted.

Count the open values on the face of the output. Then ask whether to write the
assembly to a file and where, and write it directly, tables included. There is
no template and no script.

## Rules

- **Never supply a number.** Not a thickness, not an R-value, not a permeance,
  not a cavity depth, not in an example, not as a placeholder that looks like a
  value.
- **Never recall a code requirement.** Continuous insulation ratios, vapor
  retarder classes by zone, tested assembly requirements: all quoted by the user
  or pointed at `docs/jurisdiction.md`, never remembered.
- Place the control layers before naming a material. The order is the design;
  the products are downstream of it.
- Every layer carries a job in a sentence, or it comes out of the stack.
- The drying direction is derived from the stack and then compared to the
  intent. Never assert them as matching without the comparison.
- Name every transition even when there is nothing interesting to say about it.
  A short list of transitions means one was forgotten.
- Say on every run that the arithmetic has not been done here.

## Anti-patterns

- Producing a stack that looks like a standard detail from a manufacturer's
  library. If it could have been written without Step 1, Step 1 was skipped.
- Placing the vapor retarder toward the interior by default. That is a habit
  from one climate, and it is the single most common way this assembly goes
  wrong.
- Drawing an air barrier across the wall with no last column: continuous across
  a wall section and continuous around a building are different claims.
- Recalling a per-inch R-value, a permeance, or a "typical" cavity depth because
  the number feels standard. Products differ and change.
- Quoting a code clause found by web search. Search identifies which document
  governs; it does not verify what it says.
- Calling the assembly resolved while the transitions section is empty.
- Running `condensation-check` or `air-barrier-trace` from inside this skill.
  Both are hand-offs, named and not executed.
- Treating a stack the user pasted as the answer rather than as a proposal.

## Resources

None. This skill is one file. Output is written directly at the path you choose.
