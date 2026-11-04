---
title: Draft Email
summary: Write the project email, and check whether it should be an email at all
discipline: practice-contracts
tags: ["Project Management"]
description: "Drafts a project email and first decides what kind of thing it is: most are nothing, some create a record, and a few are doing the work of an instrument that has its own form and its own consequences. Screens the draft for the language that accepts scope, grants approval, or directs work without meaning to, and says plainly when the message should be an ASI, a change directive, an additional services request, or a formal letter instead. Carries no contract terms and no house style; the agreement and the office's own conventions come from you. For a letter to the building department use `/draft-letter`; for answering an RFI use `/draft-rfi-response`; for rewriting technical language for a client use the `client-translator` skill."
argument-hint: <who> <what-it-is-about>
---

# Draft Email

Most project email is nothing. A few of them are the record somebody reads out
in two years, and one sentence in an ordinary message can accept scope, approve
a substitution, or direct work. The useful step is not the writing; it is
deciding which kind of message this is before writing it.

## Scope and limits — read first

**What this does.** Classifies the message, drafts it to that class, then screens
the draft for the words that create obligations nobody intended.

**What this does not do.**

- It carries **no contract terms and no house style.** What counts as notice,
  what an approval commits you to, and how your office signs off all come from
  the agreement and from you.
- It does not decide entitlement or take a position in a dispute.
  `dispute-advisor` covers the next required step.
- It does not issue anything. Where the answer is an instrument,
  `/draft-asi`, `/draft-ccd`, `/draft-bulletin` and
  `/draft-additional-services` produce it.
- It does not translate for a client. `client-translator` does that.
- It does not send anything.

**What you need before starting.** Who it goes to and who is copied. What it is
about. Whether anything in it changes cost, time, or scope. The relevant
contract provision if the message touches one.

## Inputs the command needs

1. **Recipient and copies.** Copying the owner changes what a message is.
2. **What it is about**, in plain words.
3. **What you want to happen** after they read it.
4. **Whether it touches scope, cost, or time**, and the contract provision if so.
5. **Anything that has already been said** on the subject, and whether verbally.

## Workflow

### Step 1 — Classify before drafting

| Class | What it is | How it is handled |
|---|---|---|
| Ordinary | Scheduling, sending a file, a question with no consequence | Write it short and stop |
| Record | You will want to prove this was said, on this date | Write it to be read later, by someone who was not there |
| Notice | The contract requires notice of something | The contract may prescribe form and recipient. Quote it, and say plainly whether email satisfies it |
| Should be an instrument | It directs work, changes scope, or approves something | **Do not send as email.** Name the instrument |
| Should be a conversation | It is a disagreement, or it will read as one | Say so. Some things get worse in writing |

State the class out loud before the draft. If it is unclear, say so rather than
defaulting to ordinary, which is the class that gives things away.

### Step 2 — Where it is an instrument, stop and say so

An email that says "go ahead and use the alternate" is a substitution approval.
An email that says "please add the two doors" is a change directive. Both are
enforceable and neither is in anybody's log.

Name the instrument, name what it costs to do it properly, and offer the short
email that points at it instead: acknowledging the question and saying the
instrument follows.

### Step 3 — Draft to the class

**Ordinary.** Two or three sentences. What, and what you want back, and by when.

**Record.** Written for a reader who was not there:

- The facts, dated, in order.
- What was decided or observed, and by whom.
- What you are doing about it.
- What you need from them, and by when.
- No characterisation of anybody, and no adjectives about the situation.

**Notice.** Quote the provision, follow its form, address it to whoever the
contract names, and say in the body that it is given under that clause. Then say
in the output whether email is likely to satisfy the requirement or whether a
different delivery method is prescribed. Never assert that it does.

### Step 4 — Screen the draft

Read it back looking only for these:

- **Imperative verbs.** Provide, revise, install, remove, proceed. Each one is a
  direction. Flag every occurrence and ask whether it is intended.
- **Approval language.** Approved, accepted, no objection, looks fine, go ahead.
  These are the most expensive four words in construction email.
- **Anything about cost or time** that is not quoted from somewhere.
- **Agreement to something that has not been priced.**
- **Any sentence written while annoyed.** It will be read aloud later.
- **Copies.** Is anyone copied who changes what the message is? Is anyone
  missing who should have the record?

Report every flag before presenting the draft as ready.

### Step 5 — Report

The class, the draft, the flags, and where the class is "should be an
instrument", the instrument named and the short email offered in its place.

## Rules

- **Classify before drafting.** Every run.
- **Never approve, accept, or direct work in an email.** Name the instrument.
- Never assert that email satisfies a contractual notice requirement.
- Flag every imperative verb and every approval word before calling it ready.
- Never characterise a person or a company in the draft.
- Say when a message should be a conversation instead.

## Anti-patterns

- "Approved" as a one-word reply.
- "Go ahead" on anything that costs money.
- Writing a record email in the language of a chat message.
- Sending notice without reading what form the contract requires.
- Copying the owner into a disagreement to apply pressure.
- Answering an RFI in email rather than in the RFI. It leaves the log.
- Writing at length about who is at fault.
