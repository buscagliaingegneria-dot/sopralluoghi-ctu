---
name: design-window-perimeter
description: "Details the three sides of an opening as a sequence rather than as three sections: takes the wall assembly, the window type and how it is anchored, then works the head, the jamb and the sill in the order the trades actually build them, laps each control layer over the one below it, and names where water that gets past the window is collected and put back out. Trigger on \"window head jamb sill\", \"window perimeter detail\", \"sill pan\", \"flashing sequence at an opening\", \"how does the air barrier close at a window\", \"punched opening detail\", \"design-window-perimeter\", or a window and a wall build-up named with a request for how they meet. Supplies the sequencing and lap logic and the questions each side has to answer; supplies no dimension, no shim space, no sealant joint size, no code requirement and no proprietary product. Requires the wall assembly as input and does not design it. It does no structural work and does not replace the enclosure consultant or the Architect of Record."
license: MIT
metadata:
  title: "Design Window Perimeter"
  summary: "Detail a window head, jamb, and sill in the order they get installed"
  discipline: "envelope-performance"
  tags: "Design"
---

# Design Window Perimeter

A window perimeter is not three details. It is one sequence, built from the
bottom up by trades arriving in an order, and every lap either sheds water or
catches it depending on which one went in first. Drawn as three separate
sections, it is usually three details that individually work and together do
not.

## Scope and limits — read first

**What this does.** Takes the wall assembly and the window, and works the
opening as one continuous problem. Establishes the sill first because everything
laps over it, then the jambs, then the head. For each of the four control layers
it names where the layer in the wall meets the layer in the window, in which
direction the lap runs, and which trade makes it. Then it names where water that
gets past the window goes, because some always does.

**What this does not do.**

- **It supplies no numbers.** No shim space, no sill pan slope, no sealant joint
  width, no end dam height, no anchor spacing, no code requirement.
- **It does not design the wall.** It needs the wall assembly as input with its
  four control layers located. Run `design-wall-assembly` first or bring the
  build-up you have.
- It does not select the window. Frame material, thermal break, glazing,
  performance class and the test standard it was rated to all arrive here as
  input, quoted from the schedule or the manufacturer.
- **It does no structural work.** Anchor design, dead load transfer, wind load
  on the frame, lintel or head support: engineering.
- It does not run the thermal arithmetic. The perimeter is where the assembly's
  worst thermal bridge usually is, and quantifying it is a hand-off.
- It does not resolve the operable window's hardware, restrictors, or fall
  protection.
- It does not replace the enclosure consultant or the Architect of Record.

**What you need before starting.** The wall assembly, layer by layer, with its
four control layers located. The window type, its frame depth, and how it is
anchored. Where in the wall depth the window sits. Whether the opening is
punched, ribbon, or a full unitised system, which changes the problem
completely. Whether there is an exterior sill, a projecting element, or a
recessed reveal above.

## Workflow

### Step 1. Take the wall, the window, and its position in the depth

Ask, in one message:

> 1. The wall build-up, inside to outside, with the four control layers located.
> 2. The window type and frame, and how it is anchored to what.
> 3. Where in the wall depth does the window sit: aligned with the structure,
>    with the insulation, or with the cladding face? This decides most of the
>    rest.
> 4. Is the opening punched, part of a ribbon, or a unitised system? A punched
>    opening in a drained wall and a unitised curtain wall are different
>    problems and only the first is what this skill is shaped for.
> 5. Is there an exterior sill, a projecting head, a recessed reveal, a shading
>    element?
> 6. What is the sequence of trades: does the window arrive before or after the
>    weather barrier is on and the cladding is up?
> 7. What is already fixed: a window schedule, a facade module, a head height, a
>    reveal depth already drawn?

Question 6 is not a construction question. If the window arrives after the
weather barrier, the laps run one way; if before, they run the other. That is a
design decision and it belongs on the drawing.

### Step 2. Locate each control layer's transfer at the opening

One row per control layer, all three sides at once, because the answer has to be
consistent around the opening:

| Control layer | Plane in the wall | Where it meets the window | Head | Jamb | Sill |
|---|---|---|---|---|---|

- **Water.** The wall's drainage plane has to be brought to the window and
  terminated on it, not near it. Name the physical component at each of the
  three sides.
- **Air.** The air seal from the wall's air barrier to the window frame,
  continuous around all four sides including under the sill. Name the material
  and say whether it is accessible after the window is in.
- **Vapor.** Whether the perimeter seal is vapor-tight, vapor-open, or different
  on the inside and the outside, and whether that matches the wall's drying
  strategy.
- **Thermal.** Where insulation meets the frame, and whether the frame's thermal
  break lines up with the wall's insulation plane. If they do not line up, say
  plainly that there is a thermal bridge around the full perimeter of every
  opening and that it has not been quantified.

Alignment between the frame's thermal break and the wall's insulation plane is
the single decision that most often gets made by the window schedule rather than
by anyone looking at a section.

### Step 3. Build the sequence, sill first, and read the gaps

Not three details. One numbered sequence of who does what, in order:

| # | Trade / component | What it does | Laps over | Value needed from you |
|---|---|---|---|---|

Start at the sill, because everything above laps onto it.

- **Sill.** The pan and what closes its ends. Which way it drains and where it
  discharges to. Whether the pan is continuous or made in pieces, and what
  happens at the joints if it is.
- **Jambs.** How the jamb flashing laps into the sill pan, and how the wall's
  drainage plane laps over the jamb flashing.
- **Head.** How the head flashing laps over the window and under the wall's
  drainage plane, and where it drains out at each end.

Then read between the rows:

- Does every lap run so that water on the outside of one layer stays on the
  outside of the next one down?
- Is any lap dependent on a sealant bead rather than on geometry?
- Does the sequence require a trade to come back after another has finished, and
  is that realistic?
- Is the air seal reachable at the moment the sequence asks for it?

### Step 4. Work the corners, ends, and what interrupts the opening

- The four corners of the opening, where two flashings meet and neither is
  continuous.
- The ends of the sill pan and the ends of the head flashing, and where each
  discharges.
- Any mullion, transom, or coupled unit inside the opening.
- Where the opening meets something else: a spandrel below, another opening
  beside it, a corner of the building, a floor line.
- Any projecting sill, canopy, or shading element that penetrates a control
  layer.
- Interior finishes returning into the reveal, and whether they conceal the air
  seal.

### Step 5. Name where water that gets past the window goes

Some water always gets past. State plainly:

- The path water takes from the window frame's own drainage to the outside.
- Whether that path passes through the wall's cavity, and if so what it lands on
  on the way.
- Whether the sill pan discharges to the outside face or into the cavity, and
  what receives it there.
- What happens if the discharge point blocks: where the water then goes and
  whether anyone would see it.

An opening whose drainage terminates inside a cavity with no named receiver is
not detailed, however many sections have been drawn.

### Step 6. Report, and hand off

The control layer table, the sequence table with its between-row notes, the
corners and interruptions, then the drainage path. Close with the hand-offs,
every time:

- The perimeter thermal bridge has not been quantified, and it runs around every
  opening in the building.
- Anchor and structural design is open.
- Air barrier continuity around the building belongs to `air-barrier-trace`, and
  openings are the junction it fails at most.
- The window's own tested performance and the manufacturer's required
  installation are open and have not been read.

Count the open values on the face of the output. Then ask whether to write the
detail to a file and where, and write it directly, tables included.

## Rules

- **Never supply a number.** Not a shim space, not a pan slope, not an end dam
  height, not a joint width, not as a placeholder.
- **Never recall a code or a manufacturer's installation requirement.** Both come
  from documents you quote.
- Refuse to proceed without the wall assembly. The perimeter is a junction.
- Work the sill first, always. Sequence is the design.
- State the trade sequence explicitly and put it on the drawing. It is not the
  contractor's business alone.
- Name the alignment between the frame's thermal break and the wall's insulation
  plane, every run.
- Name where water past the window goes, every run.

## Anti-patterns

- Drawing head, jamb and sill as three independent sections. They are one
  sequence and the laps only work in one order.
- Detailing the sill without a pan, or with a pan whose ends are open.
- Relying on a sealant bead where geometry should be shedding the water.
- Assuming the window frame is watertight and detailing no secondary path.
- Recalling a required pan slope or end dam height because the figure feels
  standard.
- Quoting a manufacturer's installation instruction found by web search.
- Locating the window in the wall depth by elevation appearance alone, without
  saying what it does to the thermal break alignment.
- Calling the opening resolved with no named receiver for the sill pan discharge.
- Running `air-barrier-trace` from inside this skill. It is a hand-off.

## Resources

None. This skill is one file. Output is written directly at the path you choose.
