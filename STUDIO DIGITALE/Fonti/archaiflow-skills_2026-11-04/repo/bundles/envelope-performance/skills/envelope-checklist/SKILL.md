---
name: envelope-checklist
description: "Builds the envelope checklist for one project rather than handing over a generic one: takes the assemblies this building actually has and the phase it is at, and produces what should be resolved by now, what can still wait, and what is already late. Works from the junction list rather than from the assemblies, because assemblies get drawn and junctions get discovered. Trigger on \"envelope checklist\", \"what should be resolved by DD\", \"are we ready to issue the envelope\", \"what have we missed on the facade\", \"envelope-checklist\", or an envelope scope at a phase change. Carries no standard checklist and no performance values; the items come from the assemblies and junctions this project has. `drawing-checklist` covers the drawing set by phase; this covers the envelope by what it is made of. It does not replace the enclosure consultant or the Architect of Record."
license: MIT
metadata:
  title: "Envelope Checklist"
  summary: "Get the envelope checklist for the phase and the assemblies you have"
  discipline: "envelope-performance"
  tags: "Documentation, Review"
---

# Envelope Checklist

A generic envelope checklist has two hundred items and applies to nobody. The
useful one is short, is about this building, and separates what is late from
what has not come up yet.

## Scope and limits — read first

**What this does.** Takes the assemblies and junctions this project has, and the
phase, and produces the checklist for that combination. Marks each item resolved,
open on time, or late.

**What this does not do.**

- **It carries no standard checklist.** Items are generated from what this
  building is made of. A list that exists before the project does is a list
  nobody works through.
- **It carries no performance values.** Targets come from the code, the brief or
  the certification, quoted.
- It does not cover the drawing set. `drawing-checklist` does that by phase, and
  the two run together at a phase change.
- It does not resolve anything. Each open item names the skill or the party that
  does.
- It does not replace the enclosure consultant or the Architect of Record.

**What you need before starting.** The assemblies, or the fact that they are not
settled. The phase and the next issue date. What has already been decided. Point
at `design-envelope`, which produces the type and junction list this reads.

## Workflow

### Step 1. Take the building, not the phase

Ask, in one message:

> 1. What assemblies does this building have? Point at `design-envelope` if the
>    type list exists.
> 2. What phase, and what is the next issue?
> 3. What is fixed already: a cladding, a module, a structure, a budget?
> 4. Is there a certification or a performance target being chased?
> 5. Who is on the team: an enclosure consultant, a facade engineer, or nobody?
> 6. Is this a new build, a renovation, or both?

**Question 5 changes the list.** A project with no enclosure consultant needs
items on the architect's list that would otherwise be somebody else's, and
saying which those are is part of the value.

### Step 2. Build the list from the junctions, not the assemblies

Assemblies get drawn because they are on the wall type legend. Junctions get
discovered one at a time in production. So the checklist is built junction-first:

| # | Item | Kind | Should be resolved by | Status |
|---|---|---|---|---|

Generate items for:

- **Each assembly**: build-up settled, values established, arithmetic run
  (`condensation-check`), buildability checked.
- **Each junction**, from `design-envelope`'s schedule: base, top, corners,
  every change of type, every opening, floor lines, movement joints,
  penetrations, and where the envelope meets the roof and the ground.
- **The cross-cutting decisions**: air barrier plane, insulation position,
  drained or sealed, drying direction. One item each, for the whole building.
- **The things that are not drawings**: performance targets and their source,
  the mockup, testing, warranties, maintenance access
  (`facade-access-study`), and who is doing the specification.

### Step 3. Say what should be resolved by now

For each item, a phase by which it should be settled, and the reason. Not a
standard programme: the reason is what makes it arguable.

The ones that are usually later than they should be, and worth stating:

- The air barrier plane, because every junction detail depends on it.
- The insulation position, for the same reason.
- Whether the structure can carry the cladding attachment, because it changes
  the structural package.
- The mockup, because it needs a lead time and a place to build it.
- Maintenance access, because it changes the roof and the parapet.
- The specification, because it is written last and governs everything.

### Step 4. Mark each item and count

`Status` is one of: `resolved`, `open, on time`, `open, late`, `not started`,
`somebody else's`.

**Report `open, late` first.** Then `somebody else's`, with a name against each —
an item assigned to a consultant who has not been appointed is not assigned.

### Step 5. Report

- Late items, with what each is holding up.
- Items belonging to somebody who is not on the team yet.
- The cross-cutting decisions, and whether each is settled.
- Junctions with no detail yet, counted against the total from
  `design-envelope`.
- What can genuinely wait, said explicitly, so the list does not read as two
  hundred equally urgent things.

### Step 6. Save

Ask where. It is re-run at every phase change against the same file, so the
status column shows movement.

## Rules

- **Never supply a standard checklist.** Generate it from this building.
- Build the list junction-first.
- Every item has a phase and a reason for that phase.
- Report `open, late` first, then items assigned to somebody not yet appointed.
- Say what can wait, explicitly.
- Never resolve an item here. Name the skill or the party.

## Anti-patterns

- Handing over a generic two-hundred-item list.
- Listing assemblies and not junctions.
- A phase against each item with no reason behind it.
- Assigning items to a consultant who has not been appointed.
- Treating every open item as equally urgent.
- Leaving the specification, the mockup and maintenance access off, because they
  are not drawings.

## Resources

None. This skill is one file. Output is written directly at the path you choose.
