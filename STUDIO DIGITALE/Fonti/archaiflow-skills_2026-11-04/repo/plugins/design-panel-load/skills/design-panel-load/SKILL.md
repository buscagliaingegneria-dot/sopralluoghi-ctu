---
name: design-panel-load
description: "Totals an electrical panel or service load: connected load summed by the categories your code uses, demand factors applied as you cite them, continuous-load multipliers as you cite them, and the result converted to amps at the voltage you state, with every step of the arithmetic shown. Trigger on \"panel load\", \"load calc\", \"service size\", \"connected load\", \"demand load\", \"panel schedule totals\", \"design-panel-load\", or a pasted load list. Works with any electrical code. The user supplies the load list, the category rules, the demand factor rows, and any multipliers, pasted and cited; the skill never supplies a demand factor, a VA allowance, or a multiplier from memory or from web search, and categories without a cited factor come out at connected load, marked unverified. Load totalling only: conductor and breaker sizing, fault current, voltage drop, and coordination are the electrical engineer's calculations and stop the run."
license: MIT
metadata:
  title: "Design Panel Load"
  summary: "Total a panel's connected load and apply your demand factors"
  discipline: "structure-mep"
  tags: "Design, Analysis"
---

# Design Panel Load

A load calculation is bookkeeping with two traps: the demand factors are
code rows that change by edition, and a category quietly totalled without
its factor looks the same as one totalled with it. So the factors arrive by
paste, cited, and every category prints its arithmetic.

## Scope and limits — read first

**What this does.** Takes your load list, groups it by the categories your
code defines as you assign them, sums connected VA per category, applies
the demand factor rows and multipliers you paste, sums the demand total,
and converts to amps at the voltage and phase you state. Every step
printed.

**What this does not do.**

- **It does not know any electrical code values.** No demand factors, no
  VA-per-area allowances, no minimum circuit loads, no continuous-load
  multipliers. Every one comes from your code, pasted and cited. That is
  the design, not a gap.
- **It does not size anything.** Conductors, breakers, panels, and
  transformers are selections against a code the engineer applies; the run
  ends at amps.
- It does not compute fault current, voltage drop, arc flash, or
  selective coordination.
- It does not invent loads. A load list is what you paste; it never adds
  receptacle or lighting allowances on its own, though it will apply an
  allowance row you cite to an area you give, arithmetic shown.
- It does not decide which category a load belongs to. You assign; it
  totals. A load left unassigned is totalled separately and reported as
  such.
- Single panel or service at a time. Fault-tolerant distribution, load
  flow between panels, and generator sizing stop the run.

**What you need before starting.** The governing code and edition, the
load list with VA and category assignments, the demand factor rows for
those categories, and the system voltage and phase.

## Workflow

### Step 1. Establish the basis

Ask, in one message:

> 1. Which electrical code governs, and which edition?
> 2. The system voltage and phase for the amps conversion.
> 3. How will you supply the load list and the factor rows: paste, type,
>    or name a file?
> 4. Any continuous loads, and the multiplier your code applies to them,
>    cited?

### Step 2. Collect the loads

One line per load or load group: description, VA (or W with power factor
you state), category as you assign it, continuous or not. Area-based
allowances arrive as a rate row you cite plus the area it applies to.

Anything unstated is missing. Never substitute a typical VA, and never
assume a load is non-continuous because it was not mentioned.

### Step 3. Compute, showing every step

```
Category <name>
  loads                    <each, as given>
  connected                <sum>
  demand factor row        <as pasted>  [cited]
  demand                   <arithmetic>
Continuous loads
  multiplier               <as cited>
  adjusted                 <arithmetic>
Unassigned loads           <sum, listed, marked unverified>
Totals
  connected                <sum>
  demand                   <sum, excluding unverified, stated>
Amps
  system                   <voltage, phase, as given>
  I = VA / (k * V)         <formula as applies, then arithmetic>
```

A category with no cited factor totals at connected load and is marked
`unverified: no demand factor supplied`, and the demand total says which
categories it excludes from factoring.

### Step 4. Report

Connected and demand totals, amps, the unverified list first, the code and
edition at the top. Then:

> Every factor, allowance, and multiplier here came from the code rows you
> supplied. I did the arithmetic and supplied no electrical values. This is
> a preliminary load total; the electrical engineer sizes the equipment.

### Step 5. Save, if asked

Ask whether to write the calculation to a file and where. Write it
directly, including the per-category arithmetic. There is no template and
no script.

## Rules

- **Never supply a demand factor, an allowance, or a multiplier.** There
  are none in this file.
- **The user assigns categories.** An unassigned load stays visible as
  unassigned, never absorbed into the nearest category.
- **Print the cited row beside every factored total.**
- **The demand total names what it excludes.** A total over a partial list
  must say so on the same line.
- **Stop at amps.** No equipment names, no breaker sizes, no conductor
  sizes.
- Never convert units silently; W to VA passes through the power factor
  you state.
- Say on every run that this is preliminary.

## Anti-patterns

- Recalling a familiar demand factor or receptacle allowance. Those rows
  move between editions and jurisdictions; familiarity is the risk, not
  the defense.
- Classifying loads by their names because the categories seem obvious.
- Treating unassigned loads as general receptacles.
- Dropping the continuous-load question because no load was flagged.
- Ending with a breaker or panel size because the amps make it obvious.

## Resources

None. This skill is one file. Output is written directly at the path you
name.
