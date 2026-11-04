---
name: change-order-tracker
description: "Keeps one dated log of every change from the moment it is first raised, not from the moment it becomes a change order: records where each one came from, what instrument carried it, its cost and time position at every stage, and who it is sitting with, so that the work directed but not yet priced and the changes stalled between proposal and execution are both visible. Reports the running total against the contingency and the count of changes proceeding on direction alone. Trigger on \"change order log\", \"track changes\", \"how much have we spent of the contingency\", \"what changes are outstanding\", \"work proceeding without a change order\", \"change-order-tracker\", or a change register handed over to keep. Carries no cost data, no markup rates and no contract periods; all come from the contract and the proposals. It does not price, review, or negotiate a change — `change-order-review` does that for one — and does not replace the Architect of Record."
license: MIT
metadata:
  title: "Change Order Tracker"
  summary: "Track every change from first mention to executed, including the ones that stall"
  discipline: "construction-admin"
  tags: "Tracking"
---

# Change Order Tracker

The change order log everyone keeps starts when a change order is issued. By
then the interesting part is over. The money is decided in the weeks between
somebody first raising a condition and anybody agreeing a number, and the
exposure sits in the work already directed and not yet priced.

## Scope and limits — read first

**What this does.** Logs every change from first mention, through whatever
instruments carry it, to execution or withdrawal. Holds each one's cost and time
position at each stage so movement is visible. Reports what is directed but
unpriced, what is stalled and with whom, and the total against the contingency.

**What this does not do.**

- **It carries no costs, no markup rates and no periods.** Contract markup,
  allowable overhead, response periods and the contingency amount all come from
  the contract and from you.
- It does not price anything and it does not review a proposal.
  `change-order-review` works one change; this holds all of them.
- It does not decide entitlement, and it does not negotiate.
- It does not approve. Recording that an owner approved is not approval.
- It does not track RFIs or submittals. `rfi-tracker` and
  `submittal-log-builder` do, and this records where a change came from them.
- It does not replace the Architect of Record.

**What you need before starting.** The contract's change provisions, quoted:
what instruments exist, what markup is allowed, what periods apply. The
contingency, if there is one, and who controls it. Everything raised to date,
including things that never became change orders.

## Workflow

### Step 1. Establish the machinery

Ask, in one message:

> 1. Quote the contract's change provisions: which instruments exist and what
>    each one does to cost and time.
> 2. What markup is allowed, on what, and at what tier?
> 3. What response periods apply, to whom?
> 4. Is there a contingency, how much, and who releases it?
> 5. What has been raised so far, including things that went nowhere?
> 6. Who has authority to direct work, and up to what?

Question 5 matters most. A log starting at the first executed change order is
missing the ones that are costing money right now.

### Step 2. Log every change from first mention

| # | Description | Origin | Raised by | Date raised | Instrument | Cost position | Time position | With whom | Status | Date |
|---|---|---|---|---|---|---|---|---|---|---|

`Origin` is where it came from: an RFI, a field condition, an owner request, a
design change, a code review comment, a consultant's error, a substitution. This
column is the one that pays for the log. After twenty changes it says something
nobody would otherwise know.

`Status` is one of: `raised`, `directed not priced`, `proposal received`,
`under review`, `negotiating`, `agreed not executed`, `executed`, `withdrawn`,
`disputed`.

**`directed not priced` is the status that matters.** Work proceeding on an
instrument that carries no agreed price is the project's live exposure, and it
gets its own count in every read-back.

### Step 3. Keep the position at every stage, not just the latest

Each change keeps its history: proposed, revised, agreed. Never overwrite a
number with a later one. The movement between them is the record of what
happened, and it is what anybody reviewing the project later will want.

Time is tracked as its own position. A change with an agreed cost and an
unresolved time impact is not agreed, and it gets logged as such rather than as
closed.

### Step 4. Log what is waiting on whom

Every open change sits with somebody: the contractor to price, the architect or
a consultant to review, the owner to decide, or in negotiation. Record who and
since when.

Report elapsed time against the contract period where one is quoted. Never
predict when something will resolve.

### Step 5. Read the aggregate

- **Directed not priced.** Count and description, first, every time.
- **By origin.** What is generating changes. A cluster from one origin is worth
  knowing early.
- **Running total.** Executed, agreed but not executed, and proposed, as three
  separate figures against the contingency. Never combine them into one number,
  because they are three different kinds of certainty.
- **Time.** Days sought, days agreed, days unresolved, as three figures.
- **Stalled.** Open longest, with whom, oldest first.
- **Withdrawn and disputed**, listed, because they come back.

### Step 6. Write the log

One dated file per project, appended to rather than rewritten. Ask where it
lives on the first run and use the same path after. Every entry carries a date
and a source.

## Rules

- **Never supply a cost, a markup rate, or a period.**
- Log from first mention, never from the first executed change order.
- Never overwrite a cost or time position; add the new one and keep the old.
- Report `directed not priced` first in every read-back.
- Report executed, agreed and proposed as three separate totals.
- A change with unresolved time is not closed.
- Elapsed time only. No predictions.
- Append; never rewrite an earlier entry.

## Anti-patterns

- Starting the log at the first change order.
- Combining executed, agreed and proposed into one number against the
  contingency.
- Overwriting a proposed cost with the agreed one and losing the movement.
- Closing a change whose time impact was never resolved.
- Leaving the origin column blank, which is the column that makes the log worth
  keeping.
- Treating a withdrawn change as gone.
- Predicting when the owner will decide.
- Recording an owner's verbal approval without marking it verbal.

## Resources

None. This skill is one file. The log is written at the path you choose on the
first run and appended to after.
