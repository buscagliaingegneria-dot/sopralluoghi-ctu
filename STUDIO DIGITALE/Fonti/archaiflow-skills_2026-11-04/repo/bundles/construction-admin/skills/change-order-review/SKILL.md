---
name: change-order-review
description: "Reviews a proposed change order against a fixed checklist and keeps a running change log in docs/construction/change-log.md. Trigger on \"change order\", \"CO review\", \"change proposal\", \"PCO\", \"COP\", \"cost of this change\", \"change log\", \"change-order-review\", or a pasted change proposal. The checklist asks whether the scope is described, the cost is broken down, the time impact is stated, the contractual basis is named, and the markup matches what the contract allows as you quote it. The skill supplies no judgment of fair price and no contract terms from memory; clause text comes from you or explain-aia, and price sanity is lookup-cost's separate job. The log carries every change with the running total against the original contract sum, arithmetic shown. Approval is the owner's and architect's act, not this skill's."
license: MIT
metadata:
  title: "Change Order Review"
  summary: "Work through a change's scope, cost, and time before it is signed"
  discipline: "construction-admin"
  tags: "Construction Admin"
---

# Change Order Review

A change order arrives as a number and a paragraph, and the paragraph is
doing a lot of work. The review is the same short list of questions every
time, and the project needs a running record of what all the changes add up
to. This does the list and keeps the record.

## Scope and limits — read first

**What this does.** Walks a proposed change through a fixed checklist:
scope, cost breakdown, time, contractual basis, markup, overlap with earlier
changes. Then records it in `docs/construction/change-log.md` with its
status, and keeps the running total of approved changes against the original
contract sum, arithmetic shown.

**What this does not do.**

- **It does not judge whether the price is fair.** No unit costs, no
  benchmarks, no "seems high". `lookup-cost` quotes benchmarks with sources;
  comparing is your judgment.
- **It does not know your contract.** The markup limits, notice periods, and
  change mechanisms it checks against are the clauses you quote. `explain-aia`
  reads contract language; this skill applies what you hand it and cites it.
- It does not approve, reject, or negotiate. It prepares the review; the
  decision is the owner's and the architect's under the contract.
- It does not draft the change instruments. `draft-ccd` and `draft-asi`
  write those; this reviews and records what comes back priced.
- It does not track schedule. A time impact is recorded in days as claimed
  and as approved; what that does to the critical path is the scheduler's
  question.
- It does not handle claims or disputes. The moment a change is contested,
  `dispute-advisor` is the tool.

**What you need before starting.** The change proposal, the original
contract sum, and, for the markup and basis checks, the contract clauses
that govern changes, quoted or pasted.

## Workflow

### Step 1. Bootstrap if needed

Check whether `docs/construction/change-log.md` exists. If not, copy
`assets/change-log-template.md` there and record the project name and the
original contract sum as you state it. If the project has no `docs/` folder
at all, confirm before creating one.

### Step 2. Review the proposal

Work through the checklist, one finding per line, quoting the proposal where
it answers and saying `not provided` where it does not:

1. **Scope.** Is the changed work described specifically enough to price a
   second time? Does it say what is added, what is deleted, what is reused?
2. **Origin.** What triggered it: an RFI, an ASI, a CCD, an owner request, a
   field condition? Name the document and date.
3. **Cost breakdown.** Labor, material, equipment, subcontractor quotes,
   markup, each visible? A single lump figure is a finding, not a
   disqualifier.
4. **Markup.** Against the contract clause as you quote it. No clause
   supplied, the check reads `unverified` rather than passing.
5. **Time.** Days requested, or an explicit zero. Silence on time is a
   finding; silence is not zero.
6. **Credits.** Deleted work priced as a credit, at a visible rate.
7. **Overlap.** Read the log: does any earlier change touch the same work?
   Name the entries.

### Step 3. Log it

One entry: `CO-001` sequential, date received, origin document, scope in one
line, cost as submitted, time as submitted, status `proposed`. Every checklist
finding that read `not provided` or `unverified` is listed on the entry.

### Step 4. Track the status

Statuses: `proposed`, `revised`, `approved`, `rejected`, `withdrawn`. On
`approved`, record the approved cost and time, which may differ from
submitted, and update the running total:

```
Original contract sum   <as stated>
Approved changes        CO-001 <n>, CO-003 <n>, ...
Current contract sum    <arithmetic> = <n>   (<n>% of original)
```

Revisions append to the entry; the submitted numbers stay visible under the
approved ones.

### Step 5. Report

On "where are we on changes": the running total first, then proposed changes
awaiting action with days outstanding, then approved changes by origin type,
then every entry carrying unresolved findings.

## Rules

- **Silence is a finding.** No time statement, no breakdown, no basis: each
  is recorded as `not provided`, never assumed.
- **Show the running total arithmetic** every time it changes.
- **Quote the contract clause** on every markup and basis check, or mark the
  check `unverified`.
- **Submitted and approved figures both stay on the entry.** The gap between
  them is information.
- **Never delete an entry.** Withdrawn and rejected changes remain, marked.

## Anti-patterns

- Calling a price high or low. That is a benchmark question with a different
  tool and a judgment that is not this skill's.
- Passing the markup check from memory of what AIA contracts usually allow.
- Treating silence on schedule as zero time impact.
- Logging only approved changes, so the log flatters the project.
- Netting credits against additions in one line so neither is visible.

## Resources

- `assets/change-log-template.md` — the log this creates, empty.

No reference files. The terms come from your contract, not from here.
