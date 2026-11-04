---
name: subconsultant-agreement-review
description: "Reads subconsultant agreements against the prime agreement to find the gap the architect is standing in: obligations promised to the owner that were never passed down, insurance required upstream and not required downstream, payment terms that oblige payment before you are paid, and scope that appears in neither agreement. Works clause by clause across both documents and reports every mismatch with what each side says. Trigger on \"review the subconsultant agreement\", \"does our consultant agreement match the prime\", \"flow down check\", \"who carries this obligation\", \"subconsultant-agreement-review\", or a consultant agreement handed over before execution. Carries no standard-form text and no legal positions; both agreements come from you. It is not legal advice and does not replace the attorney or the Architect of Record. Read `contract-review` on the prime first."
license: MIT
metadata:
  title: "Subconsultant Agreement Review"
  summary: "Check that your subconsultant agreements match what you promised the owner"
  discipline: "practice-contracts"
  tags: "Review"
---

# Subconsultant Agreement Review

The architect sits between two agreements and is liable for the difference
between them. Every obligation promised upstream and not passed down, and every
protection required downstream that the prime does not provide, lands in that
gap. Nobody notices until a claim.

## Scope and limits — read first

**What this does.** Reads the prime and the subconsultant agreements together,
clause by clause, and reports every place they do not line up. Names which side
the gap falls on and what it exposes.

**What this does not do.**

- **It is not legal advice.** An attorney reads both. This produces the list.
- **It carries no standard-form text.** Both documents come from you.
- It does not review the prime on its own merits. `contract-review` does, and it
  should be run first. A flow-down check against an unreviewed prime propagates
  whatever is wrong upstream.
- It does not draft language.
- It does not review the consultant's competence, fee or scope adequacy. It
  reads the paper.
- It does not replace the attorney or the Architect of Record.

**What you need before starting.** The prime agreement, complete with exhibits.
Each subconsultant agreement. Your proposal and each consultant's proposal. The
insurance certificates. Which consultants are yours and which the owner holds
directly.

## Workflow

### Step 1. Establish the structure

Ask, in one message:

> 1. Which consultants do you hold, and which does the owner hold directly?
> 2. Do you have the prime agreement complete, with everything incorporated by
>    reference?
> 3. What form is each subconsultant agreement: a standard form, your own, or
>    the consultant's?
> 4. Has `contract-review` been run on the prime?
> 5. Are any already executed, and which?
> 6. Do the consultants' proposals differ from their agreements?

**An agreement drafted by the consultant is drafted to protect the consultant**,
which is legitimate and worth saying out loud, because architects routinely
accept a consultant's form without reading it as an opposing document.

### Step 2. Work the flow-down, upstream to downstream

For each obligation in the prime, ask whether it reaches the consultant:

| Prime obligation | Prime says | Sub says | Gap | Falls on |
|---|---|---|---|---|

Cover at least:

- **Standard of care.** If the prime elevates it, does the sub? If not, the
  architect has warranted work it cannot hold anyone to.
- **Indemnity.** Does the sub indemnify you on at least the terms you indemnify
  the owner? A duty to defend upstream with no duty to defend downstream is the
  classic gap.
- **Insurance.** Types, limits, additional insured, waiver of subrogation, and
  the period coverage is maintained after completion. Compare limits directly.
  A consultant carrying less than the prime requires is the architect's
  exposure. Point at `/explain-coi`.
- **Deliverables and programme.** Does the sub owe you what you owe the owner,
  and early enough that you can review it before issuing?
- **Ownership and licence.** Do you have the rights you granted the owner?
  Granting the owner reuse rights you never obtained is a common and quiet
  breach.
- **Confidentiality, publicity, assignment, dispute path and venue.**
- **Anything incorporated by reference in the prime**, especially an owner's
  standards manual. If the consultant is bound to a document they have never
  seen, that is a finding.

### Step 3. Work the payment terms in both directions

Payment is where the architect finances the project by accident:

- When are you paid, and when must you pay?
- Is payment to the consultant conditional on your being paid, and does the
  jurisdiction enforce that? Say plainly that pay-if-paid and pay-when-paid are
  treated differently in different places and that an attorney answers it.
- What happens on the owner's non-payment: may you suspend, and may the
  consultant suspend on you?
- Retainage: is any held on you, and do you hold the same downstream?
- Termination: if the owner terminates, are you able to terminate the
  consultant on the same terms, and what do you owe them?

### Step 4. Find the scope in neither agreement

The most valuable pass. Go through what the project actually requires and check
each item appears in the prime, in a subconsultant agreement, or in both:

- In the prime and no sub: the architect does it, or nobody does.
- In a sub and not the prime: you are paying for something you cannot bill.
- In two subs: paying twice, and two parties will each assume the other.
- In neither: the gap that gets discovered on site.

List each with which category it falls into.

### Step 5. Report

| # | Finding | Prime | Sub | Falls on | Severity |
|---|---|---|---|---|---|

Then, in order:

- Gaps the architect is standing in, first, most exposed first.
- Scope in neither agreement.
- Scope in two agreements.
- Everything not supplied and therefore not reviewed.
- Anything already executed with a gap in it, flagged separately, because that
  is a different conversation.
- What to take to the attorney and what to take to the broker.

Close by saying this is not legal advice.

### Step 6. Save, if asked

Ask whether to write the review to a file and where.

## Rules

- **Never quote a standard form** that was not supplied.
- Run `contract-review` on the prime first, or say it was not run.
- Compare insurance limits directly, number against number.
- Report the scope gaps in all four categories, not only the missing one.
- Flag already-executed agreements separately.
- Never assert how pay-if-paid is treated in a jurisdiction.
- Say this is not legal advice, once, clearly.

## Anti-patterns

- Reviewing the subconsultant agreement without the prime beside it.
- Accepting a consultant's own form without reading it as an opposing document.
- Assuming flow-down happens because the agreement references the prime.
- Granting the owner rights you never obtained downstream.
- Checking that insurance is required without comparing the limits.
- Finding only the missing scope and not the duplicated scope.
- Drafting replacement language.

## Resources

None. This skill is one file. Output is written directly at the path you choose.
