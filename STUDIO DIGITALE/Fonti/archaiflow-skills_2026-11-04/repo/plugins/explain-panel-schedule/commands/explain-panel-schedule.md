---
title: Explain Panel Schedule
summary: Read an electrical panel schedule and say what it means for the architecture
discipline: structure-mep
tags: ["Reference"]
description: "Reads an electrical panel schedule in plain English for someone who is not an electrical engineer: what each column is, how the circuits map to spaces, what the connected and demand loads mean, whether the panel has spare capacity and what spare actually means, and what the schedule implies for the architecture — where the panel has to go, how much wall it takes, what clearance in front of it cannot be built on, and what feeds it. Carries no clearance dimensions, no demand factors and no code requirements; those come from the code text you quote or from the engineer. It does not check the electrical design and does not replace the electrical engineer. For totalling a panel's load use the `design-panel-load` skill."
argument-hint: <panel-schedule>
---

# Explain Panel Schedule

A panel schedule is handed to the architect as a coordination document and read
as a wall of numbers. Three things in it are architectural decisions: where the
panel goes, how much space it and its clearance take, and whether there is room
to add anything later.

## Scope and limits — read first

**What this does.** Explains the document, then translates it into the things
that affect the drawings.

**What this does not do.**

- It carries **no dimensions, no demand factors and no code requirements.**
  Working clearance in front of a panel is code text; quote it and the
  explanation holds the layout against it.
- It does not check the electrical design. Whether the panel is correctly sized,
  the breakers correctly selected, or the loads correctly calculated is the
  electrical engineer's.
- It does not total the load. `design-panel-load` does that with values you
  supply.
- It does not lay out the electrical room. `design-electrical-room` does.
- It does not replace the electrical engineer.

**What you need before starting.** The panel schedule. The floor plan showing
where the panel is. The code's working clearance provisions, if you want the
layout checked.

## Inputs the command needs

1. **The schedule**, complete, including the header block and any notes.
2. **The plan**, showing the panel's location and what is around it.
3. **The code text on working clearance**, if a layout check is wanted.

## Workflow

### Step 1 — Explain the header

The header carries more architectural information than the circuit list:

- **Voltage and phase.** What the panel distributes, and in plain terms what
  that means for what it can serve.
- **Main breaker or main lugs.** Whether the panel can be switched off at
  itself, which matters for maintenance and for where it can be.
- **Bus rating and main rating.** The ceiling on what the panel can carry.
- **Fed from.** Where its supply comes from, which is a route through the
  building that has to exist.
- **Mounting.** Surface or recessed. Recessed needs wall depth and that depth
  is often more than the wall provides, especially in a rated wall.
- **Location.** As stated, against what the plan shows.

### Step 2 — Explain the circuit list

- Each row is a circuit: a breaker, a size, and what it serves.
- Odd and even numbering runs down two columns because the panel is fed by two
  or three phases alternating down the bus. Explain why the numbering looks
  strange.
- Poles: single, double, triple, and what each is typically for.
- **Spares and spaces are different things.** A spare is a breaker installed and
  not connected; a space is a slot with no breaker. Say how many of each, and
  say that a schedule showing neither has no room to grow without a new panel.
- Notes, and anything marked as future, by others, or existing to remain.

### Step 3 — Explain the load summary

- **Connected load** is everything added up as though it all ran at once.
- **Demand load** is connected load after factors are applied, because it does
  not all run at once. The factors come from the code and from the engineer.
- Say which figure the panel and the feeder are sized against.
- Say what the difference between them implies: a large gap is normal and a
  small one means little diversity was assumed.

Never state a demand factor. Say the engineer applied them and name the figures
as given.

### Step 4 — Translate into architecture

The point of the exercise:

| Question | What the schedule says | What to check |
|---|---|---|
| Where does it go? | Location as stated | Against the plan |
| How much wall? | Panel dimensions, from the schedule or the cut sheet | Wall length and depth |
| Recessed or surface? | Mounting | Wall depth, and whether the wall is rated |
| What cannot be built in front? | Working clearance | Quote the code; it is a keep-clear zone with dimensions and it is not negotiable |
| Can it be in this room? | | Some rooms are not permitted to contain panels; quote the code |
| Where does the feeder run? | Fed from | A route through the building, and it needs space |
| Room to grow? | Spares and spaces | If none, adding anything later means a new panel and a new location |

**Working clearance is the one that gets built over.** It is a volume in front
of the panel, it appears on no architectural drawing by default, and joinery,
storage and equipment end up in it.

### Step 5 — Report

The header in plain English, the circuit list explained, the load summary, then
the architectural table with everything that has to be checked against the plan.

List what could not be answered from the schedule alone and who to ask.

## Rules

- **Never state a clearance, a demand factor, or a code requirement.**
- **Never check the electrical design.**
- Distinguish spares from spaces, every run.
- Say which figure the panel is sized against.
- Name the working clearance as a keep-clear volume and say it is code text to
  quote.
- Point at the engineer for anything the schedule does not answer.

## Anti-patterns

- Explaining the circuits and not the header, which is where the architecture
  is.
- Treating spares and spaces as the same thing.
- Recalling a working clearance dimension.
- Ignoring recessed mounting depth in a rated wall.
- Reading the connected load as the demand load.
- Checking whether the panel is correctly sized.
- Treating "fed from" as somebody else's problem. It is a route through the
  building.
