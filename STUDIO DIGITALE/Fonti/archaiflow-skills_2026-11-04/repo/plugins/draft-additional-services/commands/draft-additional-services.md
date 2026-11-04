---
title: Draft Additional Services
summary: Draft an additional services request before the work is done, not after
discipline: practice-contracts
tags: ["Project Management"]
description: "Drafts an additional services request and first tests whether it is one: checks the work against the agreement's own basic services definition and the proposal's exclusions, establishes what caused it and whether the cause was within the architect's control, and checks whether notice was required before the work began. Writes the request around the cause rather than around the hours, because a client refuses an hours-based request and accepts a cause-based one. Carries no rates and no contract terms; both come from the executed agreement. For the original proposal use `/draft-proposal`; for tracking the fee use the `fee-tracker` skill."
argument-hint: <what-happened> [hours-or-fee]
---

# Draft Additional Services

Most additional services are never billed. The work gets done because it is
easier than the conversation, and by the time anyone raises it the moment has
passed and the request looks opportunistic. The mechanism is notice, and notice
is before.

## Scope and limits — read first

**What this does.** Tests whether the work is genuinely additional under the
executed agreement, establishes the cause, checks the notice position, and
drafts the request around the cause.

**What this does not do.**

- It carries **no rates and no contract terms.** Both come from the executed
  agreement, quoted.
- It does not decide whether to ask. That is a judgement about the relationship,
  the fee at stake and the rest of the project.
- It does not price the work. You supply the hours or the fee.
- It does not resolve a refusal. `dispute-advisor` covers what happens next.
- It does not give legal advice.

**What you need before starting.** The executed agreement's definition of basic
services and its additional services provision, quoted. The proposal's
exclusions and assumptions. What happened, what caused it, and when. Whether
work has started. The hours or fee.

## Inputs the command needs

1. **The agreement's provisions**, quoted: basic services, additional services,
   and the notice requirement.
2. **The proposal's exclusions and assumptions**, if the proposal is part of the
   agreement.
3. **What happened**, factually, with dates.
4. **What caused it**, and who or what it was.
5. **Whether the work has started**, and how much is done.
6. **The hours or fee.**

## Workflow

### Step 1 — Test whether it is additional at all

Four questions, in order:

| Question | If yes |
|---|---|
| Is it inside basic services as the agreement defines them? | Not additional. Stop and say why |
| Is it inside a stated exclusion or a broken assumption? | Additional. Quote which |
| Was it caused by the architect's own error or omission? | Not additional. Say so plainly |
| Was it caused by the client, a third party, an authority, or a changed condition? | Additional. Name the cause |

**Question 3 is the one that has to be answered honestly.** Redesign following
the architect's own coordination failure is not additional, and asking for it
costs more than the fee does. Say so directly if that is the answer.

Where the cause is mixed, say so and propose a split rather than claiming the
whole.

### Step 2 — Check the notice position

From the quoted provision:

- Does the agreement require notice before the work proceeds?
- Has work started? If so, how much, and was notice given?
- Is there a time limit on making the request?

Report the position plainly. **Where work has already been done without notice,
say so and say it weakens the request.** Do not draft as though the sequence had
been correct. A request that pretends otherwise invites the client to check.

### Step 3 — Build the request around the cause

The structure a client accepts:

1. **What happened.** Factual, dated, neutral. No characterisation of anybody.
2. **Why it is additional.** The quoted clause or the quoted exclusion, and how
   this falls under it.
3. **What it requires.** The work, described so the client can see its size.
4. **What it costs**, and on what basis from the agreement.
5. **What happens if it is not authorised.** The consequence to the project,
   stated without threat: the programme, the deliverable, or the risk that
   remains.
6. **What is needed to proceed.** Written authorisation, and by when.

### Step 4 — Screen before sending

Read the draft for:

- Any sentence that blames somebody. Cause is factual; blame is a negotiation
  loss.
- Any hours-first framing. The cause comes first, always.
- Any claim not supported by a quoted clause or exclusion.
- Any suggestion that work has already proceeded, where it has not.
- Any implied threat in point 5.
- Round numbers that look like a negotiating position rather than a cost.

Report the flags before calling the draft ready.

### Step 5 — Report

The test result, the notice position, the draft, the flags, and a plain
statement of how strong the request is. Where it is weak, say why, so the
decision to send it is made knowingly.

## Rules

- **Never supply a rate or a contract term.**
- Run the four tests before drafting.
- **Say plainly when the cause is the architect's own.**
- Report the notice position honestly, including when work has already started.
- Cause first, hours last.
- Never blame anybody in the draft.
- Never imply that work stops as a threat. State the consequence factually.

## Anti-patterns

- Raising it after the work is finished and hoping.
- Leading with the hours.
- Claiming the whole of a mixed-cause item.
- Describing an error as a changed condition.
- Naming a person as the cause.
- Asking for authorisation with no date.
- Sending a request built on a clause nobody has read.
