---
title: Draft Substantial Completion
summary: Draft the certificate, and check whether the date it claims is real
discipline: construction-admin
tags: ["Construction Admin"]
description: "Drafts a certificate of substantial completion and tests the date before writing it: establishes what the contract defines substantial completion to mean rather than assuming, checks the definition against what has actually been achieved, separates the incomplete work that bars the date from the work that only goes on the list, and sets out what the date moves — insurance, warranties, liquidated damages, retainage, and the owner's occupancy. Carries no contract definitions, no standard forms and no time periods; every one comes from the executed agreement you supply, because the definition and its consequences differ between contract families. For tracking closeout deliverables use the `closeout-check` skill; for the list itself use `punch-list`. It does not certify anything and does not replace the Architect of Record."
argument-hint: <project> [claimed-date]
---

# Draft Substantial Completion

Substantial completion is a date with more consequences attached to it than any
other in the project, and it is routinely certified because the building looks
finished. The certificate is a professional act with liability behind it, and
the question it answers is not whether the work looks done.

## Scope and limits — read first

**What this does.** Establishes the contract's own definition, tests what has
been achieved against that definition rather than against appearance, sorts the
outstanding work into what bars the date and what does not, and sets out
everything the date shifts.

**What this does not do.**

- It carries **no definition and no form.** What substantial completion means,
  which certificate form is required, and what periods run from the date all
  come from the executed agreement, quoted. Contract families define it
  differently and the differences matter.
- It does not certify. Certification is the Architect of Record's act.
- It does not decide the date. It tests a claimed date against the quoted
  definition and reports what does not meet it.
- It does not produce the punch list. `punch-list` does, and this reads it.
- It does not track closeout deliverables. `closeout-check` does.
- It does not resolve a dispute about the date. Where the contractor claims one
  date and the evidence supports another, it sets out both and the gap.

**What you need before starting.** The executed agreement's definition of
substantial completion and everything the contract makes contingent on it. The
claimed date and what supports it. The punch list. The status of every
regulatory approval required for occupancy. The owner's intended use.

## Inputs the command needs

1. **The contract definition**, quoted, plus every clause that runs from the
   date: warranties, insurance transfer, liquidated damages, retainage, final
   payment, the correction period.
2. **The claimed date**, and what the contractor offers in support.
3. **The punch list**, with each item's status.
4. **Regulatory status**: certificate of occupancy or its equivalent, fire
   department sign-off, elevator, health, whatever this project needs.
5. **What the owner intends to do** on and after the date.

## Workflow

### Step 1 — Quote the definition, then test against it

State the contract's definition verbatim. Then, item by item, test what has been
achieved against each element of that definition. Not against whether the
building looks complete.

Most definitions turn on the owner being able to occupy or use the work for its
intended purpose. That is a functional test, and it is answered by asking what
the owner cannot do yet.

### Step 2 — Sort outstanding work into two

| Item | Bars the date | Goes on the list only | Why |
|---|---|---|---|

The distinction is the whole exercise. Work bars the date when it prevents the
owner using the work for its intended purpose, or when a regulatory approval
depends on it. Everything else goes on the list.

Count both. If anything bars the date, say plainly that the certificate cannot
be drafted for the claimed date and name what has to happen.

### Step 3 — Check the regulatory position separately

A certificate of occupancy that has not been issued is not a punch list item.
List every required approval, its status, and what it gates. Where an approval
is conditional, list the conditions and who discharges them.

An occupancy approval outstanding almost always bars the date, whatever the
building looks like.

### Step 4 — Set out what the date moves

From the quoted clauses, list every consequence with its period:

| What shifts | From the contract clause | Period | Who is affected |
|---|---|---|---|

Cover at least: warranty commencement, the correction period, insurance transfer
from builder's risk to the owner's, liquidated damages stopping, retainage
reduction, utilities and maintenance transfer, security responsibility, the
final payment sequence.

Leave every period as quoted, never recalled. Say plainly that the owner should
confirm insurance is in place before the date, because the gap between
builder's risk ending and the owner's policy starting is a real and expensive
one.

### Step 5 — Draft, or say why not

If nothing bars the date, draft the certificate in the form the contract
requires, with the date, the list attached, and the consequences stated.

If something bars it, do not draft. Produce instead: what bars it, what would
clear it, and what a realistic date looks like given that.

If the parties disagree, set out both positions with the evidence for each and
say plainly that the certificate is the Architect's determination and not a
negotiation.

### Step 6 — Report and save

Counts of barring and non-barring items, the regulatory position, the
consequences table, then the draft or the reason there is none.

Ask whether to write it to a file and where.

## Rules

- **Never supply a definition, a form, or a period.** All from the executed
  agreement, quoted.
- Test against the contract definition, never against appearance.
- Sort every outstanding item into bars or does not bar, and give a reason.
- Treat regulatory approvals separately from punch items.
- Never draft a certificate when something bars the date.
- Never write the words certify or certified. That is the Architect of Record's
  act.
- Name the insurance gap on every run.

## Anti-patterns

- Drafting because the building looks finished.
- Recalling a warranty period or a correction period.
- Putting an outstanding occupancy approval on the punch list.
- Treating a long punch list as barring, or a short one as clearing.
- Backdating to suit a payment application.
- Presenting the date as agreed when the parties disagree.
- Issuing without saying what the date moves.
