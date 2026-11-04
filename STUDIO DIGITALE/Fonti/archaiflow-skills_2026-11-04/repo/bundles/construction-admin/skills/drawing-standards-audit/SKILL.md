---
name: drawing-standards-audit
description: "Sweeps a whole drawing set for the conventions that decide whether it can be read: whether the sheet index matches the sheets, whether every reference lands on something that exists, whether the title block is complete and consistent, whether symbols and abbreviations are used as the legend defines them, and whether the same information appears twice with two answers. Reports by frequency so the systematic problems separate from the isolated ones. Trigger on \"drawing standards audit\", \"check the set for consistency\", \"do the references resolve\", \"title block check\", \"is this set ready to issue\", \"drawing-standards-audit\", or a set handed over before issue. Carries no office standard, no layer convention and no line weight table; the standard comes from your office or the project's own set. It reviews conventions rather than content — `drawing-checklist` covers what a phase should contain and `spec-review` covers the book. It does not replace the Architect of Record."
license: MIT
metadata:
  title: "Drawing Standards Audit"
  summary: "Sweep a set for the conventions that make it readable, not for what it shows"
  discipline: "construction-admin"
  tags: "Review"
---

# Drawing Standards Audit

This is not a review of what the drawings show. It is a sweep for the things
that make a set usable: that a reference lands somewhere, that the index matches
the set, that a symbol means one thing. A set can be technically right and still
generate a correction letter and forty RFIs because nobody could find anything.

## Scope and limits — read first

**What this does.** Audits a set against its own conventions and against your
office standard where you supply one. Reports findings by frequency, because
one broken reference is a typo and thirty is a process problem, and they need
different answers.

**What this does not do.**

- **It carries no standard.** No layer naming, no line weights, no text heights,
  no sheet numbering convention, no title block content. Yours or the project's,
  supplied. Where none is supplied, the audit checks internal consistency only
  and says so.
- It does not review content. Whether the detail is right, whether the design
  works, whether the phase is complete: `drawing-checklist` covers phase
  content, `constructability-review` reads it as a builder,
  `senior-plan-examiner` predicts the review.
- It does not audit the model. `model-health-audit` does.
- It does not audit the specification. `spec-review` does, and the coordination
  between the two is that skill's.
- It does not fix anything. It reports, with counts.
- It does not replace the Architect of Record.

**What you need before starting.** The set, ideally as a single PDF or a
directory. Your office standard, if there is one. The sheet index. The phase and
whether this is an issue or a check.

## Workflow

### Step 1. Establish what the standard is

Ask, in one message:

> 1. Is there an office or project standard? Paste or point at it.
> 2. What is the set, and how is it supplied?
> 3. What phase, and is this a pre-issue check or a general audit?
> 4. Have consultants' sheets been included, and are they held to the same
>    standard?
> 5. Is there a previous revision to compare against?

Where no standard exists, say plainly that the audit will check internal
consistency and nothing else. That is still worth doing and it is a different
claim.

### Step 2. Index and sheet integrity

- Every sheet in the index exists in the set.
- Every sheet in the set appears in the index.
- Sheet numbering follows a sequence, with gaps reported.
- Sheet titles in the index match the titles on the sheets.
- Consultants' sheets are present and in the sequence the index claims.

This is first because everything after depends on knowing what the set is.

### Step 3. References, in both directions

The most valuable pass, and the most tedious.

| Reference | On sheet | Points to | Exists? | Kind |
|---|---|---|---|---|

Check:

- Every detail, section, elevation and enlarged plan callout lands on a drawing
  that exists, on the sheet it names, with the number it names.
- Every drawing on a sheet is referenced from somewhere. An unreferenced detail
  is either an orphan or a missing callout.
- Every schedule reference resolves.
- Every reference to a specification section names a section that exists in the
  book.

Report broken references by kind and by frequency. Thirty broken references all
pointing at one sheet is one problem.

### Step 4. Title block and issue data

Across every sheet: project name, number, address, north point, scale, date,
revision, drawn and checked, seal block, and whatever else your standard names.
Report by field rather than by sheet, so a field missing on forty sheets reads
as one finding.

Check the revision data against the revision history and against any cloud on
the sheet. A clouded change with no revision entry, or the reverse, is a finding.

### Step 5. Symbols, abbreviations, and one-word-one-meaning

- Every symbol used appears in the legend.
- Every symbol in the legend is used.
- Every abbreviation used appears in the abbreviation list.
- The same term is used for the same thing throughout. Two words for one thing,
  or one word for two, both get reported.
- Wall types, door marks, room numbers and finish codes follow one convention.

### Step 6. Information appearing twice

Find anything stated in two places and check the two agree: a dimension on a
plan and on a detail, an area on a plan and on a schedule, a rating in a legend
and in a schedule, a note on a sheet and in the specification.

**Where the two disagree, report both values and neither as correct.** Where the
two agree, report the duplication anyway, because duplicated information will
eventually disagree.

### Step 7. Report by frequency

| Finding | Count | Systematic or isolated | Where |
|---|---|---|---|

Order by count. Then:

- Systematic findings first, with the likely cause if one is visible: a template
  problem, a missing standard, a sheet set up by a different hand.
- Isolated findings as a list.
- What could not be audited, and why: a set supplied as images, a standard not
  supplied, consultants' sheets missing.

### Step 8. Save, if asked

Ask whether to write the audit to a file and where. CSV where it becomes a task
list.

## Rules

- **Never supply a standard.** Yours, the project's, or internal consistency
  only.
- Check references in both directions.
- Report by field and by frequency, never sheet by sheet.
- Where two sources disagree, report both and rule on neither.
- Report duplicated information even when it agrees.
- Say plainly what could not be audited.
- Never fix anything.

## Anti-patterns

- Reviewing what the drawings show. Different skill, different question.
- Listing four hundred findings sheet by sheet, which nobody acts on.
- Checking that callouts resolve without checking for unreferenced drawings.
- Auditing against a remembered office standard.
- Treating a missing title block field on every sheet as forty findings.
- Deciding which of two disagreeing dimensions is right.
- Skipping consultants' sheets because they are somebody else's.

## Resources

None. This skill is one file. Output is written directly at the path you choose.
