---
name: budget-reconciliation
description: "Works the conversation every project has and most handle badly: the design costs more than the budget. Establishes first what each number actually is, since a client's budget often excludes things an estimate includes and half the gap disappears there. Then sorts the ways of closing it into the four that behave differently — less area, less quality, less scope, more money — and prices each move in what it costs the design rather than only in what it saves. Trigger on \"we are over budget\", \"the estimate came back high\", \"what do we cut\", \"value engineering at design stage\", \"the client's budget will not cover this\", \"budget-reconciliation\", or an estimate set against a budget with a gap between them. Carries no costs, no rates and no benchmarks; every figure comes from the estimator, the contractor, or a source you name. `value-engineering-advisor` sorts a cost-cutting list during construction; this is the design-stage conversation. It does not estimate and does not replace the Architect of Record."
license: MIT
metadata:
  title: "Budget Reconciliation"
  summary: "Close the gap between the programme and the budget, and price what goes"
  discipline: "design-building-types"
  tags: "Design, Project Management"
---

# Budget Reconciliation

The estimate comes back high and the meeting that follows decides the project.
Handled as a list of things to delete, it produces a worse building at a price
nobody predicted and a client who has lost confidence. Handled as four different
kinds of move, each priced in what it costs the design, it is a decision the
client can actually make.

## Scope and limits — read first

**What this does.** Establishes what the two numbers are before comparing them,
sorts the ways of closing the gap into four kinds, and prices each move in both
directions: what it saves, and what the design gives up.

**What this does not do.**

- **It carries no costs, rates or benchmarks.** Every figure comes from the
  estimator, the contractor, or a source you name. `/lookup-cost` quotes a
  benchmark with its source.
- **It does not estimate.** Where a saving has no number against it, it stays
  without one and is reported as unpriced rather than guessed.
- It is not construction-stage value engineering. `value-engineering-advisor`
  sorts a contractor's list into accept, alternate and block. This is the
  earlier conversation, where the moves available are larger and cheaper.
- It does not decide. The client decides, and the point of the exercise is
  giving them something decidable.
- It does not manage the fee consequence. Redesign costs the practice time;
  `draft-additional-services` and `utilization-tracker` handle that side.
- It does not replace the Architect of Record.

**What you need before starting.** The estimate, with its breakdown and its
exclusions. The budget, and what it was meant to cover. The programme. What the
client has said is untouchable.

## Workflow

### Step 1. Establish what each number is, before comparing them

The step that is skipped, and it often closes a third of the gap on its own.

| | Budget | Estimate |
|---|---|---|
| What it covers | | |
| What it excludes | | |
| When it was set / made | | |
| Contingency in it | | |
| Escalation in it | | |
| Fees, permits, FF&E, IT, moving | | |
| Land, financing | | |

Then ask the questions the table raises:

- Does the client's budget include soft costs the estimate excludes, or the
  reverse? A client saying "my budget is X" usually means everything, and an
  estimate usually means construction only.
- Are the two on the same date? A budget set eighteen months ago against a
  current estimate is partly an escalation conversation, not a design one.
- Is contingency counted once, twice, or not at all?
- Are they on the same area basis? Point at `area-measurement`.

**Report the gap after this reconciliation, not before.** Say what the original
gap was, what this step accounted for, and what remains. The remainder is the
real problem, and it is usually smaller than the number in the room.

### Step 2. Sort the moves into four kinds, because they behave differently

| Kind | What it means | What it costs |
|---|---|---|
| **Less area** | Build less of it | Programme. Usually the largest single lever and the least popular |
| **Less quality** | Same building, cheaper | Durability, maintenance, and how it reads. Often reappears as an operating cost |
| **Less scope** | Defer or remove part | Phasing risk, and it is rarely as cheap later |
| **More money** | Raise the budget | The client's problem, and sometimes the right answer |

Every proposal goes in exactly one. The four are worth separating because a
client who will not lose area may readily raise the budget, and a list that
mixes them makes that invisible.

**Name "more money" as an option every run**, even when it is unwelcome. A
reconciliation that only offers cuts has decided something the client should
decide.

### Step 3. Price each move in both directions

| # | Move | Kind | Saves | What the design gives up | Reversible later? | Source of the figure |
|---|---|---|---|---|---|---|

The fifth and sixth columns are the ones that make this different from a cut
list:

- **What the design gives up** in a sentence, concretely. Not "reduced quality".
  What a person in the building would notice.
- **Reversible later** matters more than clients expect. Leaving out a fit-out is
  reversible; a lower floor-to-floor, a smaller structural grid, or a thinner
  wall is not, and neither is anything buried.

Anything with no figure in `Saves` is reported as unpriced. Never estimate to
fill the column.

### Step 4. Find the moves that are cheap now and impossible later

Sort the list by when the decision has to be made rather than by what it saves:

- Moves that must happen now or never: anything structural, anything about
  levels, anything below grade, anything in the envelope's build-up.
- Moves that can wait: finishes, fit-out, landscape, FF&E, some equipment.
- Moves that get more expensive the longer they wait: anything requiring
  redesign of a set already coordinated.

Say plainly which decisions the meeting actually has to reach today. Most cut
lists treat every item as equally urgent, and the ones that matter get lost.

### Step 5. Say what the reconciliation costs to produce

Two things, honestly:

- **Redesign.** Which moves require redrawing, how much, and whether that is
  additional services under the agreement. Point at
  `draft-additional-services`. A practice that absorbs three rounds of redesign
  silently has paid for the client's budget problem.
- **Programme.** What each move does to the date, including a re-estimate.

### Step 6. Report

- The reconciliation from Step 1, first, with the gap before and after.
- The remaining gap, and the four-kind table with what each kind could
  contribute.
- The priced moves, with `what the design gives up` and `reversible`.
- What has to be decided today versus what can wait.
- Everything unpriced, listed.
- The redesign and programme cost of proceeding.

Close by saying nothing was estimated here, and that the moves are the client's
to choose.

### Step 7. Save

Ask where. This becomes the record of what was decided and what it cost, and it
is read back when somebody asks in a year why the building does not have the
thing that was in the early drawings.

## Rules

- **Never supply a cost, a rate, or a benchmark.**
- **Reconcile what the two numbers are before reporting a gap.**
- Sort every move into exactly one of the four kinds.
- Offer "more money" as an option, every run.
- Every move states what the design gives up, concretely.
- Mark every move reversible or not.
- An unpriced move stays unpriced. Never estimate to fill a column.
- Say which decisions have to be made today.

## Anti-patterns

- Producing a list of cuts.
- Comparing a client's all-in budget against a construction-only estimate.
- Ignoring escalation between the date of the budget and the date of the
  estimate.
- Mixing the four kinds in one list, which hides that the client would rather
  raise the budget.
- Cutting the envelope, which is buried, before cutting the fit-out, which is
  not.
- Absorbing the redesign silently.
- Estimating a saving to make the list add up.
- Treating every item as equally urgent.

## Resources

None. This skill is one file. Output is written directly at the path you choose.
