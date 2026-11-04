---
title: Count Plumbing Fixtures
summary: Work out required fixture counts from the table you supply
discipline: code-life-safety
tags: ["Compliance"]
description: "Computes required plumbing fixture counts for a building from the occupant load and the fixture ratio table you supply: splits the occupant load by use and by sex where the table does, applies each ratio, rounds the way the table says to round, and reports the count per fixture type per sex alongside what was provided. Carries no ratios, no occupant load factors and no rounding rules — every one of those is code text you quote or paste, because fixture tables differ between the plumbing code, the building code and local amendments, and they are amended often. For the occupant load itself use `/test-occupant-load` or the `design-occupancy-load` skill first. Does not size drainage, does not lay out the rooms, and does not decide accessibility counts beyond what the pasted table states."
argument-hint: <occupant-load> <use-group> [fixture-table-paste]
---

# Count Plumbing Fixtures

Fixture counts are arithmetic over a table, and the arithmetic is easy. What
goes wrong is the inputs: an occupant load carried over from a different
calculation, a table from the wrong code, and a rounding rule applied from
memory.

## Scope and limits — read first

**What this does.** Takes an occupant load you have already established, the
fixture ratio table that governs, and the split rules that come with it. Applies
the ratios, rounds as the table directs, and reports required against provided.

**What this does not do.**

- It carries **no ratios and no factors**. The fixture table comes from your
  plumbing or building code, pasted or quoted with its source. Tables differ by
  code, by edition and by local amendment.
- It does not compute the occupant load. Run `/test-occupant-load` or the
  `design-occupancy-load` skill first and bring the result. Reusing an egress
  occupant load for fixtures is sometimes right and sometimes not, and the
  answer is in your code, not here.
- It does not decide the sex split. Whether the table splits, at what ratio, and
  how it handles all-gender or single-occupant rooms is in the table and its
  notes. The notes matter as much as the numbers.
- It does not apply rounding from memory. Round up, round up after a threshold,
  round the total or round each: the table says.
- It does not size drainage or water supply, and does not lay out the rooms.
- It does not decide accessible fixture counts beyond what the pasted table and
  its referenced accessibility standard state.

**What you need before starting.** The occupant load and how it was derived. The
fixture table, pasted, with its source and edition. The use group as the table
names it. What is currently provided, if you want a comparison.

## Inputs the command needs

1. **Occupant load**, with how it was derived and whether it is the egress
   figure or a separately computed one.
2. **Use group**, as the fixture table names it, which may differ from the
   building code occupancy classification.
3. **The fixture table**, pasted, with its source, edition, and **its notes**.
4. **The sex split assumption** and where it comes from.
5. **Provided fixtures**, by type, if a comparison is wanted.

If the table is not supplied, say so and stop. There is no default table.

## Workflow

### Step 1 — Read the inputs back

State the occupant load, its derivation, the table's source and edition, and the
use group row being used. Quote the row.

Flag immediately if the occupant load was derived for egress and is being reused
here without a stated reason.

### Step 2 — Apply the split

Apply the sex split as the table directs, before applying any ratio. Show the
split as arithmetic.

If the table's notes address all-gender rooms, single-occupant rooms, or
substitution of one fixture type for another, quote the note and say whether it
is being applied.

### Step 3 — Apply each ratio and round as directed

One line per fixture type per sex, formula above the arithmetic:

```
water closets, female    <ratio quoted>    <occupants> / <ratio> = <raw>    rounded <as table directs> = <required>
```

Never round before the table says to. Never round the same figure twice.

### Step 4 — Report

| Fixture type | Sex | Required | Provided | Difference | Table row quoted |
|---|---|---|---|---|---|

Then:

- Shortfalls named individually.
- Any note in the table that was not applied, and why.
- What was assumed rather than quoted, counted.
- The reminder that drinking fountains, service sinks and accessible fixture
  counts are separate requirements in most tables and are only covered here if
  they were in the paste.

### Step 5 — Save, if asked

Ask whether to write the count to a file and where.

## Rules

- **Never supply a ratio, a factor, or a rounding rule.**
- **Never proceed without the table.** No default exists.
- Quote the table row used, verbatim, in the output.
- Read the table's notes and say which were applied and which were not.
- Show the split before the ratios.
- Never reuse the egress occupant load without stating that it was reused.
- Quoting a table found by web search is not quoting the code. Search identifies
  the document; it does not verify the text.

## Anti-patterns

- Recalling a fixture ratio for an occupancy because it is common.
- Applying a rounding convention from memory.
- Ignoring the table's notes because the numbers are in the columns.
- Producing a count when no table was supplied.
- Treating the egress occupant load as automatically the fixture occupant load.
- Reporting a total without the per-sex breakdown the table required.
