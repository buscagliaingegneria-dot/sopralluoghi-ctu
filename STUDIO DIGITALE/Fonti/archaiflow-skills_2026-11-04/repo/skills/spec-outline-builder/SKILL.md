---
name: spec-outline-builder
description: "Builds a specification's section list from the drawings rather than from the last project's table of contents: walks the set for every material, system and scope shown, maps each to a section, then runs the check in both directions — work drawn with no section, and sections carried forward with no work. Marks each section's status so the book's real completeness is visible rather than implied by a full-looking contents page. Trigger on \"what spec sections do we need\", \"build the table of contents\", \"spec outline\", \"do we have a section for this\", \"spec-outline-builder\", or a drawing set handed over before the book is written. Carries no section numbers, no titles and no master list; numbering comes from the format your office uses and `/lookup-csi` finds one number. For auditing a book that exists use `spec-review`; for one paragraph use `/draft-spec-snippet`."
license: MIT
metadata:
  title: "Spec Outline Builder"
  summary: "Build the section list this project needs from the drawings it has"
  discipline: "construction-admin"
  tags: "Documentation"
---

# Spec Outline Builder

A specification's contents page arrives from the last project and gets edited
down. What survives is a book that looks complete and carries three sections for
work this project does not have, while the thing on sheet A-401 has no section
at all. Both are found at tender, by the contractor, as questions.

## Scope and limits — read first

**What this does.** Walks the drawing set for scope, maps each to a section,
and reconciles in both directions. Produces a section list with a status against
each, so what is missing is visible before the book is written rather than after
it is issued.

**What this does not do.**

- **It carries no master list, no section numbers and no titles.** The numbering
  format is your office's, and `/lookup-csi` finds a number for one scope. A
  built-in master list is exactly the last-project contents page this exists to
  replace.
- It does not write the sections. `/draft-spec-snippet` writes a paragraph and a
  spec writer writes a section.
- It does not audit an existing book. `spec-review` does that, and the two run
  at different times: this before the book exists, that after.
- It does not decide what is specified where. Whether something belongs in the
  drawings, a section, or a schedule is an office decision.
- It does not read the consultants' sections unless you supply their drawings.
- It does not replace the specifier or the Architect of Record.

**What you need before starting.** The drawing set, ideally complete. The office
format and numbering. The consultants' drawings if their sections are in the
same book. The project's delivery method and phase. Any owner requirements about
the book's structure.

## Workflow

### Step 1. Establish the format and the boundaries

Ask, in one message:

> 1. What format and numbering does the office use?
> 2. What is in this book: architectural only, or the consultants too? Who writes
>    which divisions?
> 3. What phase, and is this an outline specification or a full book?
> 4. What is the delivery method? Design-build and CM at risk change what is
>    specified and how prescriptively.
> 5. Does the owner require particular sections, front-end documents, or a
>    structure of their own?
> 6. Is there a previous project's book anyone intends to start from?

**Question 6 is asked so the answer can be recorded, not so it can be used.** A
book started from a previous one inherits its sections; this builds from the
drawings and then compares.

### Step 2. Walk the drawings for scope, sheet by sheet

Not from memory of what a project usually has. From the set.

| Scope found | Where seen | Kind | Section |
|---|---|---|---|

Work the set in order and record every material, system, assembly and piece of
work shown. Include the ones that hide:

- Everything in the wall type legend, each layer of it.
- Everything in every schedule: doors, windows, finishes, hardware, equipment.
- Everything called out in a detail, including sealants, flashings, membranes,
  fasteners and accessories.
- Everything on the demolition and existing-conditions sheets.
- Site work shown on the architectural sheets.
- Anything marked by others, by owner, or not in contract, which still needs a
  boundary stated somewhere.
- Anything shown as an alternate or an allowance.

### Step 3. Map scope to sections and give each a status

| # | Section | Scope it covers | Status | Who writes it |
|---|---|---|---|---|

`Status` is one of: `needed, not started`, `drafted`, `edited for this project`,
`carried forward unedited`, `not required`.

**`carried forward unedited` is the status that matters.** A section copied from
another project and not read is the most common source of a specification that
contradicts the drawings, and a contents page does not distinguish it from a
section somebody wrote.

### Step 4. Reconcile in both directions

Two lists, and the second is the one nobody produces:

- **Drawn with no section.** Scope found in Step 2 that maps to nothing. Each is
  a question the contractor will ask or a price they will guess at.
- **Section with no work.** Sections on the intended list that nothing in the set
  requires. Each will be priced, or asked about, and each is a place the book
  can contradict the drawings.

Report both counts before anything else.

### Step 5. Check the front end and the boundaries

The parts that are not about materials:

- Front-end documents: are they somebody's, and whose?
- Division 01 general requirements, which are commonly the last thing anyone
  writes and the first thing that governs.
- Where the architectural sections stop and each consultant's begin, itemised
  for the conditions that straddle: penetrations and firestopping, ceilings
  supporting services, the facade's electrical, roof-mounted equipment
  supports, and anything a specialist trade brings.
- Allowances, alternates and unit prices, each needing a section to define them.

An interface with no owner between two consultants' books becomes a gap or a
duplication. List each.

### Step 6. Report

- The two reconciliation counts, `drawn with no section` first.
- The section list with statuses, `carried forward unedited` grouped and named.
- Interfaces between books with no owner.
- Everything found on the drawings that nobody has decided how to specify.
- What was not walked: consultants' sheets, sheets not supplied.

Then ask where to write the list, and in what form. A spreadsheet, usually,
because it becomes the specifier's work plan.

## Rules

- **Never supply a master list, a section number, or a title.**
- Build from the drawings, then compare to any inherited list. Never the reverse.
- Record `carried forward unedited` as its own status.
- Reconcile in both directions and report both counts.
- Walk the schedules and the details, not only the plans.
- Name every interface between books and give it an owner.

## Anti-patterns

- Starting from the last project's contents page.
- Recalling which sections a building type usually needs.
- Walking the plans and not the details, where most materials appear.
- Reporting only the missing sections and not the unnecessary ones.
- Treating a full-looking contents page as a complete book.
- Leaving Division 01 until the end.
- Assuming an interface belongs to the consultant because it is not on your
  sheets.

## Resources

None. This skill is one file. Output is written directly at the path you choose.
