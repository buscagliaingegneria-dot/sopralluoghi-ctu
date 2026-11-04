---
title: Draft Proposal
summary: Draft a fee proposal that says what is not included
discipline: practice-contracts
tags: ["Project Management"]
description: "Drafts a fee proposal built around its exclusions and its assumptions rather than around its scope, because every dispute about an architect's fee is a dispute about something the proposal did not say. Establishes the basis before the number: what phases, what deliverables, how many revisions, how long the programme is assumed to be, which consultants are included, and what triggers additional services. Then writes it so that the client can see what they are not buying. Carries no rates, no percentages and no phase splits; the fee comes from you or from `fee-estimator`. For an additional services request use `/draft-additional-services`; for reviewing an owner's agreement use the `contract-review` skill."
argument-hint: <client> <project> <scope-summary>
---

# Draft Proposal

Fee disputes are almost never about the number. They are about the third round
of revisions, the extra meeting, the programme that ran eight months longer than
assumed, and the consultant everybody thought the other party was carrying. All
of those are written in the proposal or they are not.

## Scope and limits — read first

**What this does.** Establishes the basis of the fee before drafting it, then
writes the proposal with the exclusions, the assumptions and the additional
services triggers in the body rather than in a footnote.

**What this does not do.**

- It carries **no rates, no percentages, no phase splits.** Those come from you
  or from the `fee-estimator` skill.
- It does not decide your fee.
- It is not a contract. A proposal is an offer; the agreement is a separate
  document. Where the proposal will be incorporated into an agreement, say so
  and say which terms govern.
- It does not give legal advice.
- It does not negotiate.

**What you need before starting.** The client and the project. The scope. The
phases and deliverables. The programme assumed. The consultants and who holds
them. Your fee, or the basis for it. Your standard terms, if you have them.

## Inputs the command needs

1. **Client and project**, and who the proposal is addressed to.
2. **Scope**, phase by phase, with deliverables per phase.
3. **The fee**, and how it is structured: lump sum, percentage, hourly, or
   mixed. Say which phases carry which.
4. **The programme assumed**, in months per phase.
5. **Consultants**: which are included in your fee, which are held directly by
   the owner, and which are excluded entirely.
6. **Your standard exclusions and terms**, if you have them.

## Workflow

### Step 1 — Establish the basis before the number

Work through these and get an answer for each. Every one that is left open
becomes an argument later:

| Basis item | Question | Recorded |
|---|---|---|
| Phases | Which phases, and what ends each one? | |
| Deliverables | What is issued at each phase, and in what form? | |
| Revisions | How many rounds per phase before it is additional? | |
| Meetings | How many, of what kind, and who attends? | |
| Site visits | How many, over what period? | |
| Programme | How long is each phase assumed to take? | |
| Consultants | Included, owner-held, or excluded? | |
| Approvals | How many submissions to which authorities? | |
| Reimbursables | What, and at what markup? | |

**Programme is the one that gets missed.** A lump sum fee assumes a duration, and
a project that takes twice as long costs the architect twice the staff time for
the same number. Say the assumption out loud in the proposal.

### Step 2 — Write the exclusions as a list, not as prose

Exclusions buried in a paragraph do not get read. A list gets read, and it gets
questioned, which is the point: a question at proposal stage costs a phone call.

Cover at least: services not in the phase list, consultants not included,
surveys and reports, testing and commissioning, models and renderings beyond
what is stated, permit and filing fees, work arising from changes to the
programme or the brief, redesign following a budget overrun that was not caused
by the design, and extended construction administration.

### Step 3 — Write the assumptions as a list too

Assumptions and exclusions are different and both are needed. An assumption is
something you have taken as true in pricing: the programme, the site
information available, the number of building types, the approvals path, the
delivery method, the client's decision structure and who has authority.

**State that if an assumption proves wrong, the fee is revisited.** That sentence
is the mechanism; the list is what it points at.

### Step 4 — Name what triggers additional services, specifically

Not "changes to scope". Specifically:

- A change to the brief after a stated phase.
- More than the stated revision rounds.
- A programme extension beyond the stated duration.
- Redesign to meet a budget where the budget changed or was never tested.
- A change of authority requirement after submission.
- Any deliverable not on the list.

Say how they are handled: written notice, an agreed fee before work proceeds,
and that work does not start until then. Point at `/draft-additional-services`.

### Step 5 — Assemble and screen

Assemble in this order: what you will do, what you will produce, what you assume,
what is excluded, the fee and how it is invoiced, what triggers additional
services, validity period, and what happens next.

Then screen the draft for:

- Any scope stated without a deliverable.
- Any deliverable without a phase.
- The word "coordinate" without saying with whom and to what extent.
- "As required" anywhere.
- A fee split that does not add to the total.
- Any consultant mentioned without saying who holds them.

Report the flags before calling the draft ready.

### Step 6 — Report

The draft, the flags, and the list of basis items still open. Say plainly that
each open item is a future argument.

## Rules

- **Never supply a rate, a percentage, or a phase split.**
- Establish the full basis before drafting any number.
- Exclusions and assumptions are lists, never prose.
- State the programme assumption explicitly.
- Name additional services triggers specifically, never as "scope changes".
- Never call a proposal a contract.
- Screen for soft language before handing back.

## Anti-patterns

- Leading with the fee.
- Exclusions in a footnote or in small print.
- "Additional services will be charged for changes in scope." Undefined and
  therefore unenforceable in practice.
- No revision count.
- No programme assumption.
- Listing a consultant without saying who holds them.
- Assuming the client's standard agreement will fill the gaps. It will fill them
  in their favour.
