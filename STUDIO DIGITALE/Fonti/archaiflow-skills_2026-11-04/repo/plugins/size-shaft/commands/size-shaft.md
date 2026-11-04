---
title: Size Shaft
summary: Add up what has to fit in a shaft, plus the room to install and reach it
discipline: structure-mep
tags: ["Analysis"]
description: "Adds up the architectural space a mechanical, electrical or plumbing shaft needs from the schedule of what runs in it: the services and their dimensions as you supply them, the clearances each needs from the others, the space to install them in the order they get installed, the access to reach anything that has to be maintained, and the rated enclosure around all of it. Reports the required clear dimension against the shaft you have drawn. Carries no duct sizes, no pipe dimensions, no clearances and no rating requirements; the services come from the engineer and the clearances from code and manufacturer data. It does not size the services themselves — `design-duct` sizes a duct run — and it does not replace the MEP engineer or the Architect of Record."
argument-hint: <services-list> [drawn-shaft-size]
---

# Size Shaft

A shaft is drawn early, at a size somebody remembered, and it is the hardest
thing in the building to make bigger later. It is also sized by the wrong
arithmetic: the sum of the services, when what it actually has to hold is the
services plus the space to get them in and the space to reach them.

## Scope and limits — read first

**What this does.** Takes the schedule of what runs in the shaft and adds up the
architectural dimension it requires: services, clearances between them,
installation space, maintenance access, and the enclosure.

**What this does not do.**

- It carries **no dimensions of any kind.** Not a duct size, not a pipe
  diameter, not an insulation thickness, not a clearance, not an enclosure
  thickness. Everything comes from the engineer, from manufacturer data, or from
  code text you quote.
- It does not size the services. `design-duct` sizes a duct run; the MEP
  engineer sizes the rest. This holds the space for what they give you.
- It does not design the enclosure's rating or its penetrations.
  `design-fire-barrier` does.
- It does not lay out the plant rooms the shaft serves.
  `design-mechanical-room` and `design-electrical-room` do.
- It does not do smoke control, shaft pressurisation, or stack effect.

**What you need before starting.** The schedule of services with dimensions,
from the engineer. What each service needs in clearance to the next and to the
enclosure. What has to be accessed, and from where. The rating required. The
shaft as currently drawn.

## Inputs the command needs

1. **The services**, itemised: what each is, its outside dimension including
   insulation, and who supplied the figure.
2. **Clearances**: between services, to the enclosure, and any that come from
   code or from a manufacturer, each with its source.
3. **Access**: what has to be reached, how often, and from which side. Valves,
   dampers, cleanouts, meters, junction boxes.
4. **The enclosure**: rating required and construction proposed.
5. **The shaft as drawn**, if there is one.
6. **Continuity**: does the shaft run the full height, and does anything enter
   or leave at each floor?

## Workflow

### Step 1 — Read the schedule back and flag what is missing

List every service with its dimension and source. Anything without a dimension
is `not supplied` and stays that way. Never substitute a typical size.

Flag services that are commonly forgotten in a shaft schedule and ask whether
they are in the list: condensate, refrigerant, gas, fire protection standpipe
and its valves, sprinkler mains, communications and low voltage, pneumatic tube,
grease waste, vent stacks, and anything the specialist trades bring later.

### Step 2 — Add up the section, not the sum

The shaft's dimension is a two-dimensional packing problem, not a total.

```
across      <service> + <clearance> + <service> + <clearance> + ... + <enclosure>
deep        <deepest service> + <clearance> + <enclosure>
```

Show the arithmetic in both directions with the source beside each term. State
that the packing arrangement is an assumption unless you were given one, and
that a different arrangement gives a different shaft.

### Step 3 — Add installation space

The services do not appear in place. Ask, and report:

- In what order are they installed, and can each one get past the ones already
  there?
- Does anything arrive in a length that has to be manoeuvred inside the shaft?
- Is there a service that has to be installed from a floor other than where it
  runs?
- Is the shaft built around the services, or are they threaded into a completed
  shaft? These give different dimensions.

An assembly that fits in section and cannot be installed is the most common
shaft failure.

### Step 4 — Add maintenance access

For each item that has to be reached:

| Item | Reached from | Access needed | Frequency |
|---|---|---|---|

- Is access from inside the shaft, from an adjacent room, or through an access
  panel? Each has a different dimensional consequence.
- Is there a shaft that requires a person to enter it? That is a confined space
  and it carries requirements this command does not know; flag it.
- Does the access panel land in a corridor, a unit, a tenant space? Access
  through a leased space is an operational problem, not a detail.

### Step 5 — Compare and report

| | Required | Drawn | Difference |
|---|---|---|---|
| Across | | | |
| Deep | | | |

Then:

- Every `not supplied` dimension, counted.
- Every assumption made about arrangement or installation.
- Where the shaft has to change size over its height, and what that does to the
  floors above and below.
- What is out of scope and named: rating and penetrations, smoke control,
  structural openings, and the plant rooms at each end.

### Step 6 — Save, if asked

Ask whether to write the take-off to a file and where.

## Rules

- **Never supply a dimension or a clearance.** Every term carries its source.
- Show the arithmetic in both directions, with the packing arrangement stated as
  an assumption.
- Add installation space and access space as separate additions, never as a
  percentage.
- Ask about the commonly forgotten services, every run.
- Flag any shaft requiring entry as a confined space question.
- Never size a service.

## Anti-patterns

- Summing the service dimensions and calling that the shaft.
- Adding a percentage for clearance instead of the actual clearances.
- Recalling a typical duct or pipe size.
- Ignoring how the services get installed.
- Putting the access panel in a leased space without saying so.
- Sizing the shaft for the typical floor and not checking where it changes.
- Sizing the enclosure's rating here.
