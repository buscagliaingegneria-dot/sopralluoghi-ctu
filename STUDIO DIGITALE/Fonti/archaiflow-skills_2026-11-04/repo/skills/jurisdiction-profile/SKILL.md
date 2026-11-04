---
name: jurisdiction-profile
description: "Builds and maintains one file per project that records the limits a code sets, each with the clause it came from, so the checking skills stop asking for the same number on every run. Trigger on \"jurisdiction profile\", \"set up the code profile\", \"record the code limits\", \"reuse my code values\", \"where do the limits come from\", or a request to fill in or extend an existing profile. Works in any jurisdiction. The profile ships empty: every value is typed, pasted from the clause, or read out of a file the user names, and a row without a clause is marked as such rather than being treated as verified. Does not look a code value up, does not carry a default, and does not decide which code governs."
license: MIT
metadata:
  title: "Jurisdiction Profile"
  summary: "Record your code's limits once, with citations, and reuse them"
  discipline: "code-life-safety"
  tags: "Compliance, Pre-Design, Project Management"
---

# Jurisdiction Profile

The checking skills ask for the same numbers every time they run. `design-stair`
wants a riser limit, `design-egress` wants a travel distance, and next month
they want them again. This writes those answers down once, next to the clause
each one came from, in a file the other skills read.

The file ships empty. What it ships is the shape.

## Scope and limits — read first

**What this does.** Creates `docs/jurisdiction.md` in your project from a blank
skeleton, walks you through filling whichever rows you need, and records each
value with the code, edition, and clause it came from and the date you recorded
it. Skills that check against a code read this file instead of asking again.

**What this does not do.**

- **It does not supply a single value.** Not one row arrives filled. Every
  number is typed by you, read out of clause text you paste, or taken from a
  file you name. That is the entire point of the file, and a profile that
  arrived populated would be worse than no profile, because it would look
  checked.
- **It does not decide which code governs your project.** You name the code, the
  edition, and any accessibility standard or local amendment. A profile built on
  the wrong edition is wrong in every row at once.
- It does not look anything up, on the web or anywhere else. Search is reliable
  for working out which code governs and unreliable for quoting it, and this
  file exists to be quoted from.
- It does not validate what you enter. A typo in a limit becomes a wrong limit
  in every skill that reads the row, which is why the clause is recorded next to
  it and why the skills quote both.
- It does not expire a row or watch for a new code cycle. Each row carries the
  date it was recorded; deciding a row is stale is yours.
- It does not check anything. It stores. The checking is `design-stair`,
  `design-egress`, `design-occupancy-load`, `code-compliance-review`, and the rest.

**What you need before starting.** The code and edition in force on the project,
and access to the clause text for whichever rows you want to fill. You can fill
none of it now and add rows as they come up; a blank row behaves exactly as it
does today, which is that the skill asks.

## Workflow

### Step 1. Establish the code in force

Ask, in one message:

> 1. Which code governs this project, and which edition?
> 2. Is there a separate accessibility standard? Which edition?
> 3. Are there local amendments, and where is their text?
> 4. Which AHJ reviews it?

Write the answers into the header block verbatim. Every row in the file inherits
this header, so a profile with a blank edition is not usable and the run says so
rather than continuing.

### Step 2. Create the file if it is not there

If `docs/jurisdiction.md` does not exist, write it from
`assets/jurisdiction-profile-skeleton.md`, filling only the header block from
Step 1 and leaving every value cell empty.

If it does exist, read it, and report which sections have rows filled and which
are still empty before adding anything.

### Step 3. Fill rows, one at a time

Ask which sections the user wants to fill now. For each row, take one of three
answers and nothing else:

1. **A typed value.** Record it, then ask which clause it came from.
2. **Pasted clause text.** Read the value out of it and quote the sentence back
   so it can be checked before it is written.
3. **A file to read.** Read it, quote the sentence, and record the file and line
   as the citation.

If none of the three arrives, leave the row empty and move on. Do not offer a
value, do not search for one, and do not treat a widely known number as exempt
from this.

Where a row has no clause behind it, write `not cited` in the Clause column
rather than leaving it blank. A blank clause on a filled value is
indistinguishable from an oversight; `not cited` is a statement.

### Step 4. Record units as given

Write the unit the code uses, in the column, without converting. A profile
holding both millimetres and inches is fine and honest. A profile that silently
converted one into the other has hidden its rounding in a file that other skills
will trust.

### Step 5. Report

Tell the user:

- The path to the profile.
- How many rows are filled, how many are empty, and how many are `not cited`.
- Which skills can now read it, and which of their items are still unanswered.

## The format

One markdown file, `docs/jurisdiction.md`. A header block, then a table per
topic. Every table has the same columns:

| Item | Key | Limit | Unit | Clause | Recorded |
|------|-----|-------|------|--------|----------|

- **Item** is the thing being limited, worded as the checking skill words it.
- **Key** is what the code splits the row by, when it splits it: use group,
  sprinklered or not, occupancy, construction type. Blank when the limit is
  unconditional. Most egress thresholds live in tables keyed this way, and a
  row copied without its key is the most common way a right number lands in the
  wrong project.
- **Limit** is the value, as the code states it. A range stays a range.
- **Unit** is the code's unit, not a converted one.
- **Clause** is code, edition, and clause number, or a file and line, or
  `not cited`.
- **Recorded** is the date you entered it.

The same item can appear more than once with different keys. That is normal and
the checking skill picks the row matching the condition it is checking.

Topic sections are fixed for the items the checking skills work through, and
open where the code splits by something only the project knows. Occupancy load
factors are the open case: a row per use and function in your building, not a
fixed list.

## How the other skills use it

A skill that checks against a code reads `docs/jurisdiction.md` before asking
anything. For each of its items:

- A filled row with a clause is used, and the clause is carried through to the
  output exactly as the skill would carry a clause you pasted.
- A filled row marked `not cited` is used and reported as `not cited` in the
  output. It is not silently promoted.
- An empty row, or no row, means the skill asks as it does today, and offers to
  write the answer back so the next run does not ask.

Nothing about the unverified path changes. An item nobody has a limit for is
still reported as unverified, on the face of the output, counted in the summary.

## Rules

- **Never write a value the user did not supply.** Not into the skeleton, not
  into an example, not as a placeholder that looks like a number.
- **Never convert a unit.** Record what the code says in the unit the code says
  it in.
- **Every filled value carries a clause or the words `not cited`.** There is no
  third state.
- The header block is required before any row is filled. A limit without an
  edition is not a citation.
- Rows are added as they are needed. An empty profile is a valid profile.
- Read the file before editing it. Another run, or the user, may have filled
  rows since.

## Anti-patterns

- Pre-filling the skeleton with the common values for a well known code so the
  user "has somewhere to start". Those are exactly the values that survive an
  edition change without anyone noticing.
- Treating a filled profile as verified because it is filled. The clause column
  is what makes a row checkable, and `not cited` rows are the ones to revisit.
- Converting the profile into a lookup table shipped with the catalog. It is a
  per-project file. A shipped one goes stale silently while continuing to look
  authoritative, which is the failure this whole catalog is built to avoid.
- Copying one project's profile into another without re-reading it. Different
  jurisdiction, different edition, sometimes different building.
- Filling a row from a previous project's profile because the code name matches.
  Editions differ, and local amendments differ inside the same edition.

## Resources

- `assets/jurisdiction-profile-skeleton.md` — the blank file, header block and
  topic tables with every value cell empty
