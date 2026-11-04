---
name: submission-reader
description: "Reads a letter from an authority — a correction letter, a completeness notice, a staff report, a conditional approval, a denial — and separates the four things inside it that behave differently: what must change, what must be shown, what must be answered, and what is a comment with nothing to do. Then finds the parts that carry a clock, since a response period or an appeal window is usually one line in the middle of a page. Trigger on \"they sent this back\", \"read this correction letter\", \"what does the city actually want\", \"plan check comments came in\", \"submission-reader\", or any letter from an authority handed over to work out. Carries no procedures and no periods; every deadline comes from the letter or from the jurisdiction. `plan-check-response-builder` writes the response; this works out what the letter asked. It does not replace the code consultant, the expeditor, or the Architect of Record."
license: MIT
metadata:
  title: "Submission Reader"
  summary: "Read what an authority sent back and say what it actually requires"
  discipline: "code-life-safety"
  tags: "Compliance, Review"
---

# Submission Reader

A correction letter arrives and gets read as a list of problems. It is usually
four different kinds of thing written in one voice, and one of them has a date
attached that nobody noticed.

## Scope and limits — read first

**What this does.** Takes the letter and sorts every item into what it actually
asks for, finds anything with a clock on it, and separates what the authority
requires from what a reviewer merely observed.

**What this does not do.**

- **It carries no procedures, periods or appeal rights.** Those come from the
  letter, the jurisdiction's published process, or the expeditor. Point at
  `permit-expeditor`.
- It does not write the response. `plan-check-response-builder` does, and it
  takes this as input.
- It does not decide whether the reviewer is right. Where an item looks wrong,
  it is marked as a disagreement to be decided, not argued here. Point at
  `cite-check` for any citation the letter relies on.
- It does not track the submission. `permit-tracker` does.
- It does not replace the code consultant, the expeditor, or the Architect of
  Record.

**What you need before starting.** The letter, complete, including its header,
its footer and anything attached. What was submitted and when. Whether anything
was said verbally before or after it.

## Workflow

### Step 1. Read the parts nobody reads

Before the numbered comments, work the letter's furniture:

- Who wrote it, in what role, and are there several reviewers with separate
  sections? Different disciplines write differently and are answered
  differently.
- What kind of letter is it: correction, incomplete, approved with conditions,
  denied, or a staff report to a body that has not met yet? These have entirely
  different next steps.
- **Any date, period, or deadline anywhere in it**, including the footer and any
  standard paragraph. A response period, a resubmission window, an expiry, an
  appeal period.
- What it says about how to respond: format, number of copies, portal, whether
  a response matrix is required.
- Whether it references a previous letter, and whether every item from that one
  is accounted for.

### Step 2. Sort every item into four kinds

| # | Item, quoted | Kind | Who acts |
|---|---|---|---|

- **Change something.** The design has to change.
- **Show something.** The design is fine and the drawing does not say it. Often
  the largest group, and the cheapest.
- **Answer something.** A question, or a request for a calculation, a report, or
  a citation.
- **Comment.** An observation, a courtesy note, or a reference to something
  outside this submission. Nothing to do, and it still gets acknowledged.

**Never renumber**, and split any item containing more than one demand,
lettering under the original number. Report the count before and after
splitting; the difference is where resubmittals fail.

### Step 3. Find what is actually blocking

Not every item stops the permit:

| # | Blocks issue | Blocks a later stage | Neither |
|---|---|---|---|

Some items are conditions on an approval that already exists, some are deferred
to a later submittal, and some have to be cleared before anything moves. The
letter rarely distinguishes them and the programme depends on it.

### Step 4. Mark the items you disagree with, without arguing yet

| # | Reviewer's position | Why it may be wrong | Citation given? |
|---|---|---|---|

Where the item rests on a citation, point at `cite-check`. Where it rests on an
interpretation, mark it as a conversation rather than a response — a phone call
resolves more of these than a written argument, and a written disagreement costs
a review cycle.

**Count the disagreements.** A response disputing most of the letter is a
conversation to have before it is submitted.

### Step 5. Report

- The clock, first: every date and period found, and what happens if each
  passes.
- Whether it got past intake, or whether this is an incompleteness notice, which
  is a different and faster problem.
- Counts by kind, with `show something` named separately because it is the
  cheapest group and usually the biggest.
- Blocking versus non-blocking counts.
- Disagreements, counted, with whether each carries a citation.
- Anything in the letter that references a previous round and is not accounted
  for.
- What has to be obtained from someone else: a consultant, a report, a test.

Then point at `plan-check-response-builder` and at `permit-tracker`.

### Step 6. Save

Ask where. The letter and this reading get read together later, often by
somebody who was not there.

## Rules

- **Read the dates before the comments**, every run.
- Never renumber, and split multi-part items under the original number.
- Sort every item into one of the four kinds.
- Separate blocking from non-blocking.
- Mark disagreements without arguing them here.
- Never treat a comment as a requirement, or a requirement as a comment.
- Point at `cite-check` for every citation the letter relies on.

## Anti-patterns

- Reading the numbered list and not the footer.
- Treating the whole letter as changes to the design.
- Missing that most items are "show it", not "change it".
- Renumbering into a tidier order.
- Arguing in the reading rather than marking the disagreement.
- Missing that it is an incompleteness notice, which needs a different and
  faster response.
- Not checking that the previous round's items were all resolved.

## Resources

None. This skill is one file. Output is written directly at the path you choose.
