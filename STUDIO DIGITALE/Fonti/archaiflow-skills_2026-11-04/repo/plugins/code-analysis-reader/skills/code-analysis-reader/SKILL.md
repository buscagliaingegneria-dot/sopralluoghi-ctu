---
name: code-analysis-reader
description: "Reads a code analysis produced by somebody else — a previous architect, a code consultant, a design-build partner, an earlier phase of your own project — and separates its three layers: the determinations it made, the arithmetic it showed, and the conclusions it stated without either. A code analysis is a chain of decisions and the first link, the occupancy classification, silently sets everything after it. Trigger on \"read this code analysis\", \"we inherited a code summary\", \"is this code sheet still right\", \"the consultant sent their analysis\", \"code-analysis-reader\", or a code analysis handed over. Carries no code text and no limits; every figure in it is checked for whether it was cited, not for whether it is correct. `code-analysis-builder` assembles your own; this reads one you were given. It does not verify compliance and does not replace the code consultant or the Architect of Record."
license: MIT
metadata:
  title: "Code Analysis Reader"
  summary: "Read somebody else's code analysis for what it assumed and never showed"
  discipline: "code-life-safety"
  tags: "Compliance, Review"
---

# Code Analysis Reader

A code analysis arrives on a cover sheet: a block of classifications, a few
tables, some numbers. It reads as fact. It is a chain of decisions, and the
first one — what occupancy this is — silently sets everything after it. Nobody
inheriting the sheet knows which parts were determined, which were calculated,
and which were typed.

## Scope and limits — read first

**What this does.** Separates the analysis into determinations, arithmetic, and
bare assertions. Traces which later figures depend on which earlier decisions.
Checks whether each figure carries a citation and whether the design it
describes is the current one.

**What this does not do.**

- **It carries no code text and no limits.** Nothing here says whether a figure
  is right. It says whether it was cited, whether it was shown, and what it
  depends on.
- It does not verify compliance. `compliance-check` holds a drawing against
  text you paste; `code-compliance-review` audits a plan across eight axes.
- It does not verify citations. `cite-check` does, and it should be run on the
  ones that matter.
- It does not build an analysis. `code-analysis-builder` does.
- It does not replace the code consultant or the Architect of Record.

**What you need before starting.** The analysis, complete, with its tables and
notes. Who produced it, when, and for what design. The current drawings. The
jurisdiction and adopted edition.

## Workflow

### Step 1. Establish whose it is and what it describes

Ask, or read off the sheet:

> 1. Who produced it, when, and for what stage?
> 2. **Which drawing revision does it describe?** Named, dated.
> 3. Which code, which edition, and does it mention local amendments?
> 4. Has anything about the building changed since: area, height, storeys, use,
>    construction type, sprinklering?
> 5. Was it reviewed by an authority, and did anything come back on it?

**Question 4 is where inherited analyses fail.** The sheet is correct for a
building that no longer exists, and nobody re-runs it because it looks
finished.

### Step 2. Sort every entry into three layers

| Entry | Determination / Arithmetic / Asserted | Cited? |
|---|---|---|

- **Determination.** A judgement somebody made: the occupancy classification,
  the construction type, whether uses are separated or non-separated, whether
  something counts as a storey or a mezzanine. These are decisions and they can
  be argued.
- **Arithmetic.** A calculation whose working is shown or could be: allowable
  area, occupant load, exit widths.
- **Asserted.** A figure or a statement with neither a citation nor working.

**Report the asserted count first.** An analysis made mostly of assertions is
not an analysis, whoever sealed it.

### Step 3. Trace what depends on what

The chain, and it runs one way:

```
occupancy classification
  -> construction type permitted
     -> allowable area and height
        -> whether increases were applied, and which
           -> separations required
              -> occupant load
                 -> exits, widths, travel distance
```

For each determination, list what downstream figures rest on it. Then say
plainly: **if the classification is wrong, everything below it is wrong**, and
the classification is the entry most often made in one line with no reasoning.

Where a building has more than one use, check whether the analysis says
separated or non-separated and whether it applied that consistently. It is a
common inconsistency and it changes the allowable area.

### Step 4. Find what is missing rather than wrong

The parts a code analysis routinely omits:

- The arithmetic behind the allowable area, showing which increases were taken.
- Whether sprinklering is assumed, and whether the sprinkler system as designed
  actually earns the increase claimed.
- The occupant load by space, rather than a single total.
- Travel distance and common path, measured rather than stated.
- Accessibility scoping counts.
- Anything about the existing building, where there is one.
- Local amendments.

For each, say whether it is absent, present but unshown, or present and shown.

### Step 5. Check it against the drawings as they are

| The analysis says | The drawings show | Agree? |
|---|---|---|

Areas, storeys, heights, occupancies by space, exits and their locations,
rated assemblies. **A code analysis that disagrees with the plans is the first
thing a plan examiner finds**, and it is what stops the review. Point at
`senior-plan-examiner`.

### Step 6. Report

- Asserted count, first.
- The determinations, with what each one carries downstream.
- What is missing or unshown.
- Every disagreement with the current drawings.
- Whether it describes the current revision at all.
- What to re-run and what to ask its author.

Close by saying nothing was verified as correct, and naming `cite-check`,
`compliance-check` and the code consultant.

### Step 7. Save, if asked

Ask whether to write the reading to a file and where. Keep it where the analysis
was inherited: it records what was adopted and what was not.

## Rules

- **Read which drawing revision it describes, first.**
- Sort every entry into determination, arithmetic, or asserted, and report the
  asserted count first.
- Trace what each determination carries downstream.
- Say plainly that a wrong classification invalidates everything below it.
- Check the analysis against the current drawings.
- Never say a figure is right or wrong. Say whether it was cited and shown.

## Anti-patterns

- Adopting an inherited analysis because it looks complete.
- Reading the numbers and not the classification they rest on.
- Missing that the building has changed since.
- Treating a sealed sheet as verified.
- Accepting an allowable area with no working shown.
- Assuming sprinklering earns the increase claimed.
- Checking the analysis and not comparing it to the plans.

## Resources

None. This skill is one file. Output is written directly at the path you choose.
