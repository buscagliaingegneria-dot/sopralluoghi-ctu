---
title: Draft General Note
summary: Write a general note that says something, and put it on the right sheet
discipline: construction-admin
tags: ["Documentation"]
description: "Drafts a general note for a drawing sheet and first tests whether it should exist: checks whether the requirement already lives in the specification, whether it contradicts anything already on the sheet or in the set, whether it directs means and methods, and whether it belongs on this sheet or on the cover. Writes the note in the imperative, scoped to what it actually applies to, and flags any note that shifts responsibility to the contractor for something the documents should have shown. Carries no standard note libraries and no code text; every requirement in a note comes from you, the specification, or a clause you quote. For the text inside a drawing callout use `/draft-callout`; for a spec paragraph use `/draft-spec-snippet`; for auditing the whole set's conventions use `drawing-standards-audit`."
argument-hint: <what-the-note-must-say> <sheet>
---

# Draft General Note

General notes accumulate. They get copied from the last project, they multiply,
they contradict the specification and occasionally each other, and nobody reads
them because there are ninety. A note worth adding is one that is not already
somewhere else and that changes what gets built.

## Scope and limits — read first

**What this does.** Tests whether the note should exist before drafting it,
checks it against what is already in the set, drafts it, and says which sheet it
belongs on.

**What this does not do.**

- It carries **no standard note library**. There is no built-in list of notes
  that belong on an architectural sheet. Notes that arrive from nowhere are how
  a set ends up requiring something the project does not do.
- It carries **no code text**. A note that repeats a code requirement is quoting
  it, and quoting it wrongly is worse than not quoting it at all.
- It does not write specifications. If the requirement is a specification
  requirement, the answer is a specification section, not a note.
- It does not audit the existing notes. `drawing-standards-audit` reads the set.
- It does not decide the office standard.

**What you need before starting.** What the note has to achieve. The general
notes already on the sheet and on the cover. The relevant specification
sections, if any. Which sheet is proposed.

## Inputs the command needs

1. **What the note must achieve**, in plain words.
2. **The notes already present**, on the proposed sheet and on the cover.
3. **The specification section** that covers the same subject, or the statement
   that there is none.
4. **The proposed sheet**, and what kind of sheet it is.

## Workflow

### Step 1 — Test whether it should exist

Four questions, in order. Any yes to the first two stops the draft:

| Question | If yes |
|---|---|
| Is it already in the specification? | Do not write the note. Say which section carries it |
| Is it already a note somewhere in the set? | Do not write it. Say where, and whether the two would agree |
| Does it direct means, methods, or sequence? | Do not write it. That is the contractor's and the note transfers responsibility |
| Would the set be built the same way without it? | Then it is decoration. Say so |

Report which questions were answered from documents supplied and which were
assumptions.

### Step 2 — Check it against the rest of the set

- Does it contradict a drawing, a detail, or another note?
- Does it use a term the set defines differently elsewhere?
- Does it apply to the whole sheet, or to part of it? A general note that is only
  sometimes true is a note that will be applied where it should not be.

### Step 3 — Decide which sheet

- **Cover or general notes sheet.** Applies to the whole set.
- **Discipline sheet.** Applies to that discipline's work throughout.
- **This sheet only.** Applies to what is drawn here.

A note on the wrong sheet either gets missed or gets applied too widely. Say
which and why. If the answer is "the whole set", say plainly that adding it to
one sheet will make it look sheet-specific.

### Step 4 — Draft

- Imperative. The note tells the contractor what to do.
- One requirement per note. A note doing three things gets partly complied with.
- Scoped explicitly: what it applies to, and where it does not.
- No code section numbers unless the user supplied the text and wants it cited.
- No "as required", "as necessary", "per code", or "to the satisfaction of the
  Architect". Each of those moves a decision the documents should have made into
  the field.

### Step 5 — Screen before handing back

Read the draft looking only for:

- Words that shift responsibility: verify, coordinate, confirm, as required, as
  necessary. Flag each and say whether it is intended. **Some are legitimate and
  most are not**, and a note asking the contractor to verify something the
  drawings should show is the most common way a set gets weaker.
- Anything that duplicates the specification.
- Anything that could be a dimension on a drawing instead.

Report the flags before presenting the note as ready.

### Step 6 — Report

The draft, the sheet recommendation with its reason, the flags, and any note
already in the set that this one should replace rather than join.

## Rules

- **Never produce a note from a standard library.**
- **Never quote code text** that was not supplied.
- Run the four tests before drafting, every time.
- One requirement per note.
- Flag every responsibility-shifting word before calling the draft ready.
- Say which sheet and why.
- If the answer is a specification section, say so and do not write the note.

## Anti-patterns

- Copying general notes from the last project.
- Writing a note that repeats the specification, so the two can drift.
- "Contractor to verify all dimensions in the field."
- "All work to comply with applicable codes." True, and it does nothing.
- A note that directs a sequence of work.
- Putting a set-wide note on one sheet.
- Adding a note when a dimension on the drawing would do it.
