---
name: variance-request-builder
description: "Builds a variance or discretionary relief application around the findings the deciding body is legally required to make, rather than around why the project wants it: extracts each required finding from the jurisdiction's own criteria, works the evidence for each one separately, tests whether the hardship claimed is of the kind the criteria recognise, and assembles the record so the decision can survive an appeal. Trigger on \"variance request\", \"zoning relief application\", \"hardship findings\", \"special exception\", \"what do we have to prove for a variance\", \"variance-request-builder\", or a zoning requirement named as unmeetable with a request to seek relief. Carries no criteria, no precedent and no legal positions; the findings come from the jurisdiction's own text. It does not give legal advice and does not replace the land use attorney, the planner, or the Architect of Record."
license: MIT
metadata:
  title: "Variance Request Builder"
  summary: "Build the case for a variance against the findings the board has to make"
  discipline: "code-life-safety"
  tags: "Documentation"
---

# Variance Request Builder

A variance is refused because the application argued why the project needs
relief. The board cannot grant relief on that basis. It has to make specific
findings, written into the ordinance, and an application that does not give it
the evidence for each one is asking it to do something it cannot do.

## Scope and limits — read first

**What this does.** Extracts the findings the deciding body must make from the
jurisdiction's own criteria, builds the evidence for each one separately, tests
the hardship claim against what the criteria recognise, and assembles the record.

**What this does not do.**

- **It carries no criteria and no precedent.** The findings come from the
  jurisdiction's ordinance, quoted. What another board granted is not evidence
  here and a recalled precedent is worse than none.
- **It is not legal advice.** Variance standards are legal standards, they are
  litigated, and the difference between a use variance and an area variance can
  decide the application. A land use attorney reads them.
- It does not predict the outcome. Discretionary bodies are discretionary.
- It does not track the application. `entitlement-tracker` does.
- It does not build an alternative means request for a building code
  requirement. That is `alternative-means-builder` and it is a different
  process with different tests.
- It does not replace the land use attorney, the planner, or the Architect of
  Record.

**What you need before starting.** The requirement that cannot be met, quoted.
The jurisdiction's variance criteria, quoted in full. Which body decides. Why
the requirement cannot be met. What relief is sought, precisely. Any site
condition that makes this parcel different from its neighbours.

## Workflow

### Step 1. Establish the criteria and the kind of relief

Ask, in one message:

> 1. Quote the requirement that cannot be met, and the district it applies in.
> 2. Quote the jurisdiction's variance criteria in full, and say which body
>    applies them.
> 3. Is this an area variance, a use variance, a special exception, or something
>    the jurisdiction calls by another name? The tests differ, sometimes
>    substantially.
> 4. Why can the requirement not be met? Physical site condition, existing
>    building, an existing nonconforming condition, or cost?
> 5. Exactly what relief is sought, in numbers?
> 6. Has an attorney been engaged, and has staff been approached?

**If cost is the only answer to question 4, say so plainly before drafting.**
Most criteria explicitly exclude economic hardship created by the applicant, and
an application resting on it is asking to be refused.

### Step 2. Break the criteria into separate findings

Most criteria contain several findings joined by "and". Each one has to be
satisfied independently and each needs its own evidence.

| # | Finding, quoted | What it requires the board to conclude | Evidence | Strength |
|---|---|---|---|---|

Never merge two findings into one argument. A board denying an application
usually denies on one finding, and an argument that covered three at once gave
it nowhere to look.

### Step 3. Test the hardship against what the criteria recognise

Most area variance criteria ask whether the hardship arises from a condition of
the land rather than from the applicant's choices. Work through:

- What is unusual about this parcel: shape, size, topography, an existing
  structure, an easement, a prior taking or dedication?
- Is that condition shared with neighbouring parcels? A condition general to the
  district is usually not a basis; a condition unique to this parcel usually is.
- **Was the condition created by the applicant?** Self-created hardship is
  excluded almost everywhere, and it includes buying the parcel knowing the
  condition in some jurisdictions and not others.
- Is there a conforming alternative? A board will ask, and the application
  should answer before it is asked.

Say plainly, in the output, which of these the case rests on and how strong it
is.

### Step 4. Work the minimum relief necessary, and the impact findings

**Minimum.** Most criteria require the relief granted to be the least necessary.
Show the work: what was tried, what it produced, and why the amount sought is
the smallest that resolves the problem. An application seeking a round number
looks like a negotiating position.

**Impact.** Most criteria require the board to find that the relief does not harm
the neighbourhood or the ordinance's purpose. Address it directly rather than
asserting it: what changes for the adjoining properties, for the streetscape,
for light, air and privacy, and what mitigation is offered.

### Step 5. Test the case against its objections

- Which finding is weakest, and what is the answer?
- What will the neighbours say, and has any of it been addressed in the design?
- What precedent does the board worry about setting, and how is this case
  distinguishable?
- Is there a version of the project that does not need the variance, and what
  does it cost? The board will ask and "we did not study it" is a bad answer.

Name the weakest finding in the output. An application that does not know its
weak point will be told.

### Step 6. Assemble and report

- The application, finding by finding, in the jurisdiction's own order and
  format.
- The evidence list, each item with its author and reference.
- Counts: findings addressed, findings with no evidence.
- The weakest finding, named.
- Everything the case rests on that was not supplied.
- What belongs to the attorney rather than to the design team.

Close by saying this is not legal advice and that the decision is the board's
alone.

### Step 7. Save, if asked

Ask whether to write the application to a file and where, and ask about format,
since most jurisdictions prescribe one.

## Rules

- **Never supply criteria, a test, or a precedent.**
- **Address each finding separately.** Never merge two into one argument.
- Say plainly when the hardship claimed is economic or self-created.
- Show the work on minimum relief; never assert it.
- Name the weakest finding in every output.
- Never predict the outcome.
- Say this is not legal advice, once, clearly.

## Anti-patterns

- Arguing why the project needs the relief rather than why the findings are met.
- Merging the findings into one narrative.
- Citing what another board granted.
- Claiming hardship from a condition shared across the district.
- Seeking a round number without showing what was tried.
- Asserting no neighbourhood impact rather than addressing it.
- Ignoring the conforming alternative because it is unattractive.
- Confusing this with a building code alternative means request.

## Resources

None. This skill is one file. Output is written directly at the path you choose.
