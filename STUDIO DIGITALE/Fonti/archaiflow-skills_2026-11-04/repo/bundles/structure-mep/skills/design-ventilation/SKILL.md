---
name: design-ventilation
description: "Computes outdoor-air ventilation rates zone by zone from the rate table you paste, with every step of the arithmetic shown: people component plus area component per zone, adjusted and summed the way your standard's procedure says. Trigger on \"ventilation rate\", \"outdoor air\", \"OA calculation\", \"cfm per person\", \"air changes\", \"ventilation calc\", \"design-ventilation\", or a pasted room schedule with occupancies. Works with any ventilation standard. The user names the standard and pastes its rate rows, occupant counts or the density rule, areas, and any effectiveness or system-level factors, each cited; the skill never supplies a rate, a density, or a factor from memory or from web search, and rows without a supplied rate come out unverified rather than filled. Supply-side outdoor air only: exhaust requirements, duct sizing, and energy are other calculations. Preliminary, never a substitute for the mechanical Engineer of Record."
license: MIT
metadata:
  title: "Design Ventilation"
  summary: "Compute zone outdoor-air rates from the table you supply"
  discipline: "structure-mep"
  tags: "Design, Analysis"
---

# Design Ventilation

A ventilation calculation is one small formula run over every zone and then
summed with care. The formula is the same everywhere. The rates per person
and per unit area are rows in your standard's table, so they arrive by
paste, with the table named, and never from memory.

## Scope and limits — read first

**What this does.** Takes your zone list, applies the rate rows you paste to
the occupancies and areas you give, applies the effectiveness and
system-level factors you cite, and produces the outdoor-air requirement per
zone and the total, with the arithmetic printed for every zone.

**What this does not do.**

- **It does not know any ventilation values.** No rates per person, no rates
  per area, no occupant densities, no effectiveness values, no air-change
  targets. Every one comes from your standard, pasted and cited. That is the
  design, not a gap.
- **It does not classify your zones.** You say which table row each zone
  uses; matching a room name to an occupancy category is a judgment the
  standard's user makes, not this file.
- Supply-side outdoor air only. Exhaust requirements, transfer air,
  pressurization, and makeup air are separate checks it does not run.
- It computes the zone and system quantities your procedure defines, as you
  supply that procedure. A multiple-zone system correction runs only if you
  paste the procedure's equations; otherwise the report stops at the zone
  sums and says so.
- It does not size ducts, fans, or louvers (`design-duct` is the duct
  arithmetic), does not check energy code, and does not do CO2 or IAQ
  modeling.
- Occupant counts come from you. If you want them derived from a density,
  you paste the density row and the arithmetic is shown.

**What you need before starting.** The ventilation standard and edition,
the rate rows for your zone types, the zone list with areas, and occupant
counts or the density rows to derive them.

## Workflow

### Step 1. Establish the standard

Ask, in one message:

> 1. Which ventilation standard or code governs, and which edition?
> 2. How will you supply the rate rows: paste the table, type them, or name
>    a file?
> 3. Occupant counts directly, or derived from a density row you supply?
> 4. Does your procedure apply zone or system-level adjustments
>    (effectiveness, diversity, a multiple-zone correction)? If so, paste
>    those provisions too.

### Step 2. Collect the zones

One row per zone: name, area, occupancy as counted or the density row to
derive it, and which rate row applies, as you assign it. A zone missing any
of these stays in the list and comes out `unverified`.

Never fill a rate, a density, or an assignment because the room name makes
it obvious.

### Step 3. Compute, showing every step per zone

```
Zone <name>
  rate row, as pasted       <people rate, area rate>   [cited]
  occupants                 <as given, or density arithmetic shown>
  people component          <arithmetic>
  area component            <arithmetic>
  zone outdoor air          <sum>
  effectiveness (if given)  <as cited> -> <arithmetic>
```

Then the totals: sum of zones, and the system-level steps only as your
pasted procedure defines them, each shown. Zones with missing inputs are
listed with what each is waiting for, and excluded from totals with the
exclusion stated.

### Step 4. Report

Per-zone table, the total, the unverified list first in the summary line,
and the standard and edition printed at the top. Then:

> Every rate, density, and factor here came from the table you supplied. I
> did the arithmetic and supplied no ventilation values. This is a
> preliminary calculation; the mechanical Engineer of Record designs the
> system.

### Step 5. Save, if asked

Ask whether to write the calculation to a file and where. Write it
directly, including the per-zone arithmetic. There is no template and no
script.

## Rules

- **Never supply a rate, a density, or a factor.** There are none in this
  file.
- **The user assigns the table row to the zone.** Suggesting a category is
  allowed only as a question, never as a filled value.
- **Print the citation on every zone**, so a wrong row is visible where it
  was used.
- **Totals exclude unverified zones and say so.** A total quietly missing
  three zones reads as complete and is not.
- **Stop at the zone sums** if the system-level procedure was not supplied.
- Never convert units between the table's system and the zone list's;
  mismatched units stop the zone.
- Say on every run that this is preliminary.

## Anti-patterns

- Recalling a familiar rate because the zone is an office. The familiar
  rows are the ones nobody re-checks.
- Deriving occupants from a density that was never pasted.
- Applying an effectiveness or diversity factor by habit.
- Averaging two candidate rows when the user has not chosen.
- Summing a system total over zones that silently dropped out.

## Resources

None. This skill is one file. Output is written directly at the path you
name.
