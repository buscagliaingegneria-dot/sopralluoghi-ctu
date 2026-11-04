---
name: applicability-check
description: "Takes any requirement — a code section, a standard, an ordinance, a lease clause, an owner's design standard, a certification credit — and answers the question that comes before every other one: does this apply to this project at all. Works the six tests that decide it: is the document adopted or binding here, does the project fall inside its stated scope, has the trigger been met, does an exemption remove it, is this the edition that binds, and is something else more restrictive. Trigger on \"does this apply to us\", \"is this section relevant\", \"do we have to comply with this\", \"they say this applies\", \"applicability-check\", or a requirement quoted at you. Carries no text and no thresholds: every answer comes from the document you supply or the jurisdiction's own source. It does not interpret the requirement — `code-reader` takes it apart — and does not replace the code consultant or the Architect of Record."
license: MIT
metadata:
  title: "Applicability Check"
  summary: "Work out whether a requirement applies to you before reading it"
  discipline: "code-life-safety"
  tags: "Compliance"
---

# Applicability Check

Everybody reads what a requirement demands. Almost nobody first checks whether
it demands it of them. The wasted work runs in both directions: designing to a
requirement that never applied, and being surprised by one whose trigger was
met two revisions ago.

## Scope and limits — read first

**What this does.** Runs six tests on a requirement to establish whether it
applies to this project, and reports which of the six could be answered and
which could not.

**What this does not do.**

- **It carries no text, thresholds or exemptions.** Every answer comes from the
  document you supply or from the jurisdiction's own published source, never
  from recall.
- It does not interpret the requirement or take it apart. `code-reader` does
  that, and it runs after this: there is no point taking apart a requirement
  that does not apply.
- It does not verify the citation. `cite-check` does.
- It does not check the design against it. `compliance-check` does.
- It does not find the exception that helps. That is a different question and it
  is asked after this one concludes the requirement does apply.
- It does not replace the code consultant or the Architect of Record.

**What you need before starting.** The requirement, quoted, including its scope
statement and its exemptions. Who says it applies, and where they say it. The
project's own facts: use, size, height, storeys, construction type, jurisdiction,
whether existing or new.

## Workflow

### Step 1. Establish who says it applies

Ask, in one message:

> 1. The requirement, quoted, with its scope and exemption clauses.
> 2. **Who says it applies?** A reviewer, a consultant, a contractor, a
>    manufacturer, a specification, or your own assumption?
> 3. Where did they say it: a letter, a report, a spec section, a conversation?
> 4. What jurisdiction, and what is the project: use, size, height, storeys,
>    construction type, new or existing?
> 5. What is riding on the answer?

**Question 2 matters.** A reviewer saying it applies is close to the end of the
conversation. A manufacturer saying so is a sales position. Your own assumption
is the one worth checking hardest, because nobody will.

### Step 2. Run the six tests

| # | Test | Answer | Source |
|---|---|---|---|
| 1 | Is the document adopted or binding here at all? | | |
| 2 | Does the project fall inside its stated scope? | | |
| 3 | Has the trigger been met? | | |
| 4 | Does an exemption remove it? | | |
| 5 | Is this the edition that binds? | | |
| 6 | Is something else more restrictive? | | |

**1. Adopted or binding.** A code is adopted by a jurisdiction. A standard binds
because a code adopts it or a specification names it. A guideline binds nothing
on its own. Point at `standard-reader`.

**2. Scope.** Every requirement has a scope statement and it is usually one
sentence at the top of the section that nobody reads. Quote it and set the
project against it.

**3. Trigger.** Many requirements apply only above a threshold or after an
event: an area, a height, an occupant load, a change of use, an alteration
exceeding some proportion. Say what the trigger is and whether it is met, and
say when the answer would change.

**4. Exemption.** The paragraph after the requirement. Exemptions are where the
answer most often flips and where reading stops one sentence too early.

**5. Edition.** The edition that binds is the adopted or specified one, not the
current one. Point at `cite-check`.

**6. More restrictive.** Where two documents both apply, the stricter usually
governs, and answering only about this one is half an answer.

### Step 3. Report each test separately

Never a single yes or no. Three outcomes per test: `yes`, `no`, and **`cannot
answer from what was supplied`**, which is the honest one and is common.

If any of tests 1 to 4 is a clear `no`, say so plainly and stop the analysis
there — but still report the tests you could not run, because a `no` resting on
an unread scope statement is not a `no`.

### Step 4. Say what would settle it

For every test that could not be answered:

- What document would answer it.
- Who has it.
- Whether the authority should simply be asked, which is often faster than any
  of the above and is the answer people avoid. Point at `permit-expeditor`.

Where the answer is genuinely arguable, say so. Applicability is argued in front
of authorities all the time, and a question with a real argument on both sides
should be flagged as one rather than resolved here.

### Step 5. Report

- Who says it applies, and what standing that has.
- The six tests, each answered separately with its source.
- The conclusion: applies, does not apply, or cannot be determined — and never
  a conclusion that rests on a test nobody ran.
- What would settle the open tests.
- If it applies: point at `code-reader` to take it apart and at
  `compliance-check` to hold the design against it.

### Step 6. Save, if asked

Ask whether to write the check to a file and where. Point at
`jurisdiction-profile`, where a settled applicability question belongs so it is
answered once.

## Rules

- **Ask who says it applies**, before anything else.
- Run all six tests and report each separately.
- **Never conclude from a test nobody ran.** `cannot answer` is a result.
- Quote the scope statement and the exemption; never summarise them.
- Check the edition that binds, not the current one.
- Ask whether something else is more restrictive.
- Say when the answer is genuinely arguable rather than resolving it.

## Anti-patterns

- Reading what a requirement demands before asking whether it demands it of you.
- Accepting a manufacturer's or a contractor's word that something applies.
- Reading the requirement and stopping before the exemption.
- Answering about one document when two apply.
- Assuming the current edition binds.
- Producing a single yes or no.
- Concluding it does not apply because the trigger was not met, without reading
  the scope.

## Resources

None. This skill is one file. Output is written directly at the path you choose.
