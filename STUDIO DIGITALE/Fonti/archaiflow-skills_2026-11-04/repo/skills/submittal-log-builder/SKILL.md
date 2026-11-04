---
name: submittal-log-builder
description: "Reads a project specification section by section, pulls out every submittal each one calls for, classifies it, and assembles a submittal log ready to issue. Trigger on \"build submittal log\", \"submittal log\", \"extract submittals from spec\", \"shop drawing log\", \"submittal register\", \"submittal-log-builder\", or a pasted specification section list. Works with any specification format and any contract. The user supplies the spec text by pasting it, naming files to read, or pointing at an indexed PDF, and supplies the review durations from their own contract. The skill never invents a submittal, never carries a list of typical submittals, and never assumes a review duration: every row traces to a line in the user's spec, and anything it could not find is listed as a gap rather than filled in."
license: MIT
metadata:
  title: "Submittal Log"
  summary: "Build a submittal log from the spec book"
  discipline: "construction-admin"
  tags: "Construction Admin, Document Generation"
---

# Submittal Log Builder

Turn a specification into a submittal log where every row points back at the
line of spec that requires it. The skill reads what you give it and lists what
it could not find. It does not know what a section usually asks for, and it does
not guess.

## Scope and limits — read first

**What this does.** Walks the specification sections you give it, finds the
submittal article in each, extracts every item called for, classifies it, and
builds a log with a spec reference on every row. Sections it could not read come
out in a gaps list, counted, so a partial log never reads as a complete one.

**What this does not do.**

- **It does not know what a section normally requires.** It carries no list of
  typical submittals. If a submittal is not in the text you supply, it does not
  appear in the log. That is the design, not a gap.
- **It does not assume review durations.** Those come from your contract or your
  Division 01 section. A row with no duration supplied shows `not specified`.
- It does not review submittals or judge whether one is adequate. It builds the
  register; the reviewer does the reviewing.
- It does not track submittal status, dates, or ball-in-court over time. It
  produces the log at issue.
- It does not read a spec you have not given it, and it does not fill in a
  section number that is missing from your list.

**What you need before starting.** The specification text, in any form it can
read, your section list, and the review durations your contract sets.

## Workflow

### Step 1. Establish the source and the contract

Ask, in one message:

> 1. How will I read the spec? Paste the sections, name files for me to read, or
>    tell me it is indexed and I will query it.
> 2. Which sections are in scope? Give the list, or tell me to work from the
>    table of contents in what you supply.
> 3. What numbering system does the spec use, and which edition?
> 4. What review duration does your contract set, and where is that written? If
>    a Division 01 section overrides it for some submittals, say so.
> 5. Any schedule milestones the log should be sorted or filtered against?

Record the numbering system and the contract reference. Both go in the log
header, so the log can be read later without the covering email.

### Step 2. Read each section

For each section in scope:

1. Locate the article that lists submittals. Numbering for that article varies
   by office and by format, so find it by heading text rather than by an
   assumed number.
2. If the article cannot be found, record the section as a gap with the reason,
   and move on. Do not substitute what the section probably asks for.
3. Extract each item the article lists, in the order listed, with the exact
   wording used.

Where a section refers to another section for its submittals, follow the
reference if that section is in scope, and record the gap if it is not.

### Step 3. Classify each item

Assign one type per row: shop drawing, product data, sample, mock-up,
certificate, test report, calculation, or closeout document. Use the spec's own
words where it names the type. Where the wording is ambiguous, mark the type
`unclear` and quote the phrase rather than picking for the user.

### Step 4. Assign durations

Apply the duration the user supplied in Step 1, per row. Where a section sets
its own duration, use that and cite the section rather than the contract. Where
neither exists, the cell reads `not specified` and the row is counted in the
summary.

Never fill a duration from a customary figure. A submittal log with a review
period nobody agreed to is a schedule commitment made by accident.

### Step 5. Build the log

| # | Section | Item, as written | Type | Duration | Duration from | Spec reference |
|---|---------|------------------|------|----------|---------------|----------------|

- **Item, as written**: the spec's wording, not a summary.
- **Duration from**: the contract clause or the section that set it, or
  `not specified`.
- **Spec reference**: section number and the article the item was read from, so
  any row can be checked in under a minute.

Then the gaps list: sections in scope that produced no rows, with the reason for
each. Then the counts: sections read, sections in the gaps list, rows produced,
rows with no duration.

Close with:

> Every row here was read out of the specification you supplied. Nothing was
> added from a typical list. The gaps list is what I could not read, not what
> the project does not need.

### Step 6. Save, if asked

Ask whether to write the log to a file and in what format, and where. Write it
directly. There is no template and no script.

## Rules

- **Never add a submittal that is not in the supplied text.** Not from memory,
  not from a search, not because a section of that number usually calls for it.
- **Never assume a review duration.** It comes from the contract or the spec,
  cited, or it is `not specified`.
- **Quote the spec's wording.** A paraphrased submittal description turns into
  an argument on site.
- **Find the submittal article by its heading, not by an assumed number.**
  Article numbering differs between offices and formats.
- **Report the gaps list every time**, with counts, on the face of the log.
- Where the spec is ambiguous about a type, mark it `unclear` and quote the
  phrase rather than deciding.

## Anti-patterns

- Filling in the submittals a section "always" has. That is the failure this
  skill exists to avoid, and it produces a log that looks complete and commits
  the contractor to things the spec never asked for.
- Applying a customary review duration because the contract was not to hand.
- Renumbering or renaming a section to match a numbering convention the project
  does not use.
- Dropping sections that could not be read, so the log looks clean.
- Summarising an item instead of quoting it.
- Bundling a list of typical submittals into this skill later. It has none on
  purpose.

## Resources

None. This skill is one file. Output is written directly at the path you name.
