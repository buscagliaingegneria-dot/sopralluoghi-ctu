---
name: design-occupancy-load
description: "Computes occupant load space by space, then subtotals by use group and gives a building or floor total. Trigger on \"occupant load\", \"calc occupants\", \"occupancy load\", \"how many occupants\", \"design-occupancy-load\", \"IBC 1004\", \"OBC 3.1.17\", or a pasted program listing spaces with use and area. A foundation calculation: its output feeds egress, plumbing fixture counts, allowable area, and stair width. Works in any jurisdiction. The user names the governing code and edition and supplies each load factor by typing it, pasting the table row, or naming a file to read. The skill never supplies a factor from memory or from web search, and a space with no factor is reported as unverified rather than estimated. Does not count fixed seating, and does not replace the Architect of Record or the AHJ."
license: MIT
metadata:
  title: "Design Occupancy Load"
  summary: "Compute occupant load by use group and by space"
  discipline: "code-life-safety"
  tags: "Design, Compliance, Pre-Design"
---

# Design Occupancy Load

Turn a list of spaces into an occupant load, one space at a time, with the
factor you supplied next to every number. Divide area by factor is the same
arithmetic everywhere. The factors are not, so the factors come from you.

## Scope and limits — read first

**What this does.** Takes your space list, applies the load factor you supply
for each use, rounds by the rule you supply, and returns a table with subtotals
by use group and a total. Spaces with no factor come back as `unverified` and
are counted separately from the total, so a partial run never reads as complete.

**What this does not do.**

- **It does not tell you the load factor.** It has no factors in it. Every one
  comes from you, and a space you do not supply one for stays unverified. That
  is the design, not a gap.
- It does not sweep the rest of the plan. `code-compliance-review` covers occupant load as
  one of eight axes at review depth; this skill is the space-by-space
  calculation behind it, and the input `design-egress` expects.
- It does not decide your occupancy classification. You name the use for each
  space. Where a use splits into concentrated and unconcentrated, or into
  assembly subtypes, you say which applies.
- It does not count fixed seating. Seats are counted, not divided, and that
  count comes from you as a number.
- It does not apply cumulative loads for an exit, stair, or corridor serving
  several storeys. It reports per space and per floor, and flags that the
  cumulative step is yours.
- It does not check egress capacity, plumbing fixtures, or allowable area. It
  produces the input those need.
- It does not replace the Architect of Record or anticipate the AHJ.

**What you need before starting.** The governing code and edition, your space
list with areas, and the load factor plus area basis for each use.

## Workflow

### Step 1. Establish the code and the basis

Ask, in one message:

> 1. Which code governs this project, and which edition?
> 2. What is being counted: a whole building, one floor, or specific spaces?
> 3. What area basis are your numbers on, gross or net, and do you know which
>    basis each factor requires? The two differ enough to halve or double a
>    count, so I will ask again per factor if you are unsure.
> 4. How will you supply the factors? Type them, paste the table row, or name a
>    file I should read.

Record the code and edition. They go on every output row, so the table can be
read next year without guessing the cycle.

**Read the profile first, if there is one.** If `docs/jurisdiction.md` exists,
read its occupancy load section before asking anything else and say which use
and function combinations it already answers. Match on the Key column, which is
where the area basis is recorded: a factor keyed to net area is not the factor
for a gross measurement, and swapping them silently halves or doubles the count.
Those combinations are not asked again. A row marked `not cited` stays
`not cited` in the output. Where the file is absent nothing changes, and
`jurisdiction-profile` is what writes it.

### Step 2. Collect the space list

For each space or group of like spaces, ask for:

- Name or room number
- Use, as your code classifies it
- Function within that use where the code splits it (seating layout, sales
  versus storage, and so on)
- Floor area, and whether that figure is gross or net
- Fixed seating present, yes or no, and the seat count if yes

Never fill in an area or a use. Anything unstated is missing and is reported
that way.

### Step 3. Collect one factor per unique use and function

Work through the unique combinations, not the spaces, so a factor is asked for
once and reused. For each, accept exactly three kinds of answer.

1. **A typed factor.** Record it, and ask for the clause it came from and the
   area basis it applies to.
2. **A pasted table row.** Read the factor and the basis out of it, and quote
   the row back so it can be checked.
3. **A file to read.** Read it, quote the row, cite file and line.

If none arrives, mark every space in that combination `unverified` and continue.
Do not offer a factor, do not search for one, and do not treat a familiar number
as exempt.

When a factor arrives that `docs/jurisdiction.md` did not hold, offer to write
it there with its clause and its area basis, so the next run does not ask. Never
write a row the user did not supply.

Ask separately for the rounding rule, since codes differ on whether a fraction
rounds up, and on whether rounding happens per space or on the total.

### Step 4. Compute and report

| Space | Use | Area | Basis | Factor | Basis matches | Load | Cited as | Status |
|-------|-----|------|-------|--------|---------------|------|----------|--------|

- **Basis matches**: whether the area basis you gave for the space is the one
  the factor requires. A mismatch is reported, never silently reconciled.
- **Load**: area divided by factor, rounded by the rule you supplied. Blank when
  the row is unverified.
- **Cited as**: code, edition, clause, or file and line, or `not cited`.
- **Status**: `counted`, `unverified` (no factor), `missing` (no area or use),
  `seats` (fixed seating, count supplied), or `basis mismatch`.

Then subtotals by use group, a total of the counted rows, and a separate count
of what was not counted.

Close with:

> Factors in this table came from you, not from me. I did the arithmetic and
> supplied no code values. Unverified rows are not in the total.

And a reminder that an exit, stair, or corridor serving several storeys needs
the cumulative load, which this run did not apply.

### Step 5. Save or hand off, if asked

Ask whether to write the table to a file and where, and whether to emit the
subtotals as JSON for a downstream check. Write it directly. There is no
template and no script.

```json
{
  "code": "<code and edition as given>",
  "computed_at": "<ISO timestamp>",
  "per_space": [],
  "per_use": {},
  "counted_total": 0,
  "unverified": 0
}
```

## Rules

- **Never supply a load factor.** Not from memory, not from a search, not from a
  figure in this file. There are none in this file.
- **Never reconcile a basis mismatch quietly.** Gross against net is the error
  that halves or doubles a count while looking correct. Report it and ask.
- **A space is counted only with both an area and a factor.** Everything else is
  `unverified` or `missing`, and both are reported next to the total.
- **Round by the rule supplied, not by convention.** Ask whether it applies per
  space or to the total.
- Fixed seating is a seat count from you, never an area divided by a factor.
- Say on every run that cumulative loads for multi-storey egress components were
  not applied.

## Anti-patterns

- Filling a factor from recall because the use is a common one. Common factors
  are the ones that get carried across an edition change unnoticed.
- Searching the web for a table row and using it as the factor. Search finds
  which code governs; it does not quote it reliably, and a row that is nearly
  right reads exactly like one that is right.
- Adding unverified rows into the total to make the number look finished.
- Reusing one factor across two functions of the same use because they seem
  close. Ask which row applies.
- Converting between square feet and square metres, or rounding an area to a
  neater figure before dividing.
- Bundling a factor table into this skill later. It has none on purpose, and a
  bundled table goes stale silently while still looking authoritative.

## Resources

None. This skill is one file. Output is written directly at the path you name.
