---
title: Draft RFI Response
summary: Answer an RFI without giving away scope, cost, or time
discipline: construction-admin
tags: ["Construction Admin"]
description: "Drafts the architect's answer to a contractor's RFI: works out first whether the answer is already in the documents, whether it is a clarification or a change, and whether it is even the architect's question to answer, then writes the response so that a clarification does not read as a direction and a direction does not travel without the instrument that carries it. Flags any answer that adds scope, cost, or time and names the instrument it belongs in — ASI, bulletin, or CCD — rather than burying it in an RFI reply. Carries no contract positions and no standard response language; the contract, the specification, and the drawings all come from you. For writing the RFI rather than answering it use `/rfi-writer`; for logging them use the `rfi-tracker` skill."
argument-hint: <rfi-number> <question-text>
---

# Draft RFI Response

An RFI answered carelessly is the cheapest way to give away a change order. The
words "provide" and "revise" in an RFI reply have been read as direction more
often than any other two words in construction administration.

## Scope and limits — read first

**What this does.** Classifies the RFI before answering it, drafts the response
to its class, and flags anything in the answer that changes scope, cost or time
so it leaves in the right instrument.

**What this does not do.**

- It carries **no contract language and no standard responses.** The contract
  form, the general conditions, the specification and the drawings come from
  you.
- It does not decide entitlement. Whether the contractor is owed time or money
  for something is a contract question with a process behind it, and the
  response is not that process.
- It does not issue anything. `/draft-asi`, `/draft-bulletin` and `/draft-ccd`
  produce the instruments; this names which one is needed.
- It does not answer for the consultants. Where the question belongs to
  structural, MEP or another consultant, it says so and stops.
- It does not track. `rfi-tracker` holds the log.

**What you need before starting.** The RFI as received, complete, with its
number, date and any attachments. The contract documents the answer will rest
on. Who else has to answer part of it. The response deadline.

## Inputs the command needs

1. **The RFI verbatim**, with number, date, and what the contractor proposed if
   they proposed anything.
2. **The relevant documents**, quoted or referenced by sheet and detail.
3. **Who owns it**: architect, a consultant, the owner, or the contractor
   themselves.
4. **The deadline**, and what is waiting on it.

## Workflow

### Step 1 — Classify before drafting

Every RFI is one of five, and the response differs entirely:

| Class | What it means | How it is answered |
|---|---|---|
| Already answered | The information is in the documents | Point at the sheet and detail. Nothing else |
| Clarification | Documents are ambiguous; no scope changes | Clarify, and say explicitly that no change results |
| Not our question | Belongs to a consultant, the owner, or the contractor | Redirect, named. Do not answer it anyway |
| Substitution or means | The contractor proposes something different | Route it to the correct process, not an RFI reply |
| Change | The answer adds or alters scope, cost or time | Answer, and name the instrument that will carry it |

State the class out loud in the draft before the response text. If the class is
unclear, say so rather than defaulting to clarification, which is the class that
gives scope away.

### Step 2 — Check whether it is already answered

Before drafting anything, look for the answer in the documents supplied. If it
is there, the response is a pointer and nothing more. Adding explanation to an
already-answered RFI is how a clarification becomes a direction.

Report how many of the questions in the RFI were already answered. If the number
is high, that is a pattern worth telling the team about, and `rfi-tracker`
records it.

### Step 3 — Split multi-part RFIs

An RFI asking three things gets three classified answers, lettered under the
original number. Never renumber. A single paragraph answering three questions
leaves two of them arguable.

### Step 4 — Draft to the class

**Already answered.** One sentence. Sheet, detail, and the words that no change
results.

**Clarification.** State what the documents say, where. Then state the
clarification. Then state explicitly that it is a clarification and that no
change in scope, cost or time is directed. That sentence is the point of the
whole reply.

**Not our question.** Name who owns it and why. Do not offer an opinion on the
answer.

**Substitution or means and methods.** Say that an RFI is not the route, name
the route the contract sets, and stop. Means and methods are the contractor's
and answering them transfers responsibility.

**Change.** Answer the question, then state plainly that the answer alters the
work and name the instrument that will follow. Never direct the change in the
RFI reply itself.

### Step 5 — Screen the draft before it goes

Read the drafted response back looking only for these:

- Any imperative verb: provide, install, revise, replace, furnish, remove. Each
  one reads as a direction. Flag every occurrence and say whether it is intended.
- Any acceptance of a proposed method.
- Any statement about cost or time.
- Any answer to a question that was not asked.
- Any part of the question left unanswered.

Report the flags before presenting the draft as ready.

### Step 6 — Report

- The class, per part.
- The draft response.
- The imperative-verb flags.
- The instrument needed, if any, and a note that it has not been issued.
- Anything routed to a consultant, and whether their answer is back.

## Rules

- **Classify before drafting.** Every run.
- **Never direct work in an RFI response.** Name the instrument.
- **Never answer a means and methods question.**
- Never renumber, and split multi-part RFIs.
- State "no change in scope, cost or time" explicitly on every clarification.
- Flag every imperative verb before calling the draft ready.
- Never quote a contract clause from memory or from web search.

## Anti-patterns

- Answering helpfully at length when the answer was already on a sheet.
- Using "provide" in a clarification.
- Accepting a proposed substitution inside an RFI reply.
- Commenting on the contractor's schedule impact claim.
- Answering a consultant's question to be helpful.
- Treating an RFI that proposes a solution as an RFI that asks a question.
- Leaving the third part of a three-part RFI unanswered.
