---
title: Count Loading Berths
summary: Work out required loading berths from the table you supply
discipline: code-life-safety
tags: ["Compliance"]
description: "Computes required off-street loading from the zoning table you supply: applies the ratio by use and floor area, applies the berth dimensions and vertical clearance the text states, and then asks the question the table does not — whether a truck can actually reach the berth, turn, and leave without reversing into the street. Reports the code count and the operational check separately, because a project can satisfy one and fail the other. Carries no ratios, no berth dimensions and no design vehicle; all come from the jurisdiction's text and from the operation. For parking counts use `/test-parking`; for how everything reaches the site use the `site-access-study` skill."
argument-hint: <jurisdiction> <district> <uses-and-areas>
---

# Count Loading Berths

Loading is a count in the zoning table and a geometry problem on the site, and
the two are checked at different times by different people. The count is
satisfied on the zoning sheet; the geometry is discovered when a truck cannot
make the turn.

## Scope and limits — read first

**What this does.** Applies the jurisdiction's loading table to the uses and
areas you give, and separately reports whether the berths as located can be
reached and left, using the design vehicle you name.

**What this does not do.**

- It carries **no ratios, no berth dimensions and no clearances.** All from the
  jurisdiction's zoning text, quoted.
- It carries **no design vehicle.** Which truck the site has to accommodate
  comes from the operation, the tenant, or the standard your civil engineer
  uses. The zoning berth size and the actual vehicle are different things and
  the difference matters.
- It does not do turning analysis. Swept path analysis is the civil or traffic
  engineer's, with software. This asks the question and names who answers it.
- It does not cover parking. `/test-parking` does.
- It does not design the service yard, the dock levellers, or the refuse
  strategy.

**What you need before starting.** The jurisdiction and district. The loading
table, pasted. The uses and their floor areas as the table measures them. The
proposed berth locations. The design vehicle, if known.

## Inputs the command needs

1. **Jurisdiction and district.**
2. **The loading table**, pasted, with its notes and the berth dimensions and
   clearances it requires.
3. **Uses and floor areas**, as the table measures them. Gross, net, or by
   tenant: the table says which and they differ.
4. **Proposed berths**: how many, where, and their dimensions.
5. **The design vehicle**, or the statement that it has not been established.

## Workflow

### Step 1 — Apply the table

Quote the row for each use, then the arithmetic:

```
<use>   <area as the table measures it>   <ratio quoted>   =   <berths required>
```

Then read the table's notes. Loading tables carry more consequential notes than
most: whether uses aggregate or are counted separately, whether a shared berth
is permitted, whether a smaller berth substitutes, and what happens below a
threshold area.

Report required, provided, and the difference.

### Step 2 — Check the berths against the stated dimensions

Each proposed berth against the table's required length, width and vertical
clearance. Report per berth, not as a total. A berth short by a foot is not a
berth.

Vertical clearance is checked along the whole approach, not only at the berth.
A berth under a podium reached through a garage with lower clearance is not
reachable.

### Step 3 — Ask the operational question separately

The table is satisfied or it is not. This is a different question:

- Can the design vehicle reach the berth from the street it will arrive on?
- Can it turn, or does it reverse, and does it reverse from or onto the public
  right of way? Reversing onto the street is prohibited in many jurisdictions
  and is a refusal wherever it is not.
- Can it leave in forward gear?
- What does it conflict with on the way: pedestrians, parking, the accessible
  route, the fire access route, the refuse route?
- Where does it wait if the berth is occupied?
- What hours does it arrive, and does that change the answer?

Report these as findings, each with what would resolve it, and name the traffic
or civil engineer as the party who confirms.

### Step 4 — Report the two checks separately

| Check | Result | Source |
|---|---|---|
| Zoning count | required / provided / pass or fail | Table row quoted |
| Berth dimensions | per berth | Table quoted |
| Operational access | findings | Design vehicle named |

**Never merge them into one verdict.** A project can meet the count and be
unbuildable, or fail the count and work perfectly.

Then: every assumption made rather than supplied, counted, and everything out of
scope flagged: swept path analysis, refuse strategy, dock equipment.

### Step 5 — Save, if asked

Ask whether to write the check to a file and where.

## Rules

- **Never supply a ratio, a berth dimension, a clearance, or a design vehicle.**
- Read the table's notes and report which were applied.
- Check vertical clearance along the whole approach.
- Report the zoning count and the operational check as two separate results.
- Never state that a truck can make a turn. Name who confirms it.
- Quoting a table found by web search is not quoting the zoning.

## Anti-patterns

- Recalling a loading ratio for a use.
- Assuming a design vehicle from the building type.
- Checking clearance at the berth and not on the way in.
- Merging the count and the access check into one pass or fail.
- Accepting a berth that requires reversing onto the street.
- Aggregating uses when the table counts them separately, or the reverse.
- Performing swept path analysis.
