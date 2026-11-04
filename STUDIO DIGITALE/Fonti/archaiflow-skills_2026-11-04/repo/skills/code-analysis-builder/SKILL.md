---
name: code-analysis-builder
description: "Assembles the code analysis block that goes on a permit set cover sheet, in six parts: occupancy classification, construction type, height and area with the allowable-area arithmetic shown, fire-resistance summary, means-of-egress summary, and accessibility statement. Trigger on \"code analysis\", \"cover sheet code block\", \"G001 code block\", \"code-analysis-builder\", \"allowable area calc\", \"construction type check\", or a pasted program with use, footprint, and sprinkler condition. Works in any jurisdiction. The user names the governing code and edition and supplies every value by typing it, pasting the clause or table row, or naming a file to read. The skill never supplies a code value from memory or from web search, and any line without a supplied value is printed as unverified rather than filled in. Does not replace the Architect of Record or the AHJ."
license: MIT
metadata:
  title: "Code Analysis"
  summary: "Assemble the code analysis block for a cover sheet"
  discipline: "code-life-safety"
  tags: "Compliance, Design"
---

# Code Analysis Builder

Build the cover-sheet code block from values you supply, and print it with a
citation on every line. The six parts of that block are the same in every permit
set. What goes in them is not, so it comes from you.

## Scope and limits — read first

**What this does.** Collects your project inputs and the code values you supply,
assembles them into the six-part block a cover sheet carries, shows the
allowable-area arithmetic step by step, and marks every line with where its
value came from. Any line you did not supply a value for prints as
`[unverified]` rather than being filled in.

**What this does not do.**

- **It does not tell you what your code requires.** It has no tables, no
  thresholds, and no formulas in it. Every value and every formula comes from
  you. That is the design, not a gap.
- It does not classify your building. You name the occupancy and construction
  type; it records what you named and what you cited.
- It does not compute occupant load or check egress. Run `design-occupancy-load`
  and `design-egress`, or supply the summary figures.
- It does not cover high-rise additions, atrium or smoke control, or
  existing-building provisions. Each is flagged and left to a note on the sheet.
- It does not draw the sheet. It produces the text block.
- It does not replace the Architect of Record and does not anticipate the AHJ.

**What you need before starting.** The governing code and edition, your program
and building inputs, and the clause or table text for each value you want on
the sheet.

## Workflow

### Step 1. Establish the code and the flags

Ask, in one message:

> 1. Which code governs this project, and which edition? Name any separate
>    accessibility standard and energy code that appear on your cover sheets.
> 2. Project name, address, and the authority having jurisdiction.
> 3. Any of these present: high-rise, atrium or smoke control, existing-building
>    work, incidental or special uses? Each becomes a flagged note rather than a
>    checked line.
> 4. How will you supply values? Type them, paste the clause or table row, or
>    name a file I should read.

Record the code and edition. They print at the head of the block and on every
cited line.

### Step 2. Collect the project inputs

- Occupancy classification for each use, as your code names them, and whether
  the building is treated as mixed use
- If mixed, which approach applies: separated, non-separated, or your code's
  equivalent, and the separation rating if separated
- Construction type, as your code names it
- Sprinkler condition and the standard the system is designed to
- Building footprint area, storey count, and building height
- Frontage or open perimeter figures, if your code's area increase uses them
- Fire separation distance at each exterior wall
- Occupant load summary, and where it came from
- Accessible route scope for the project

### Step 3. Collect one value per line, part by part

For each line in the six parts below, ask for the value. Accept exactly three
kinds of answer.

1. **A typed value.** Record it and ask which clause or table it came from.
2. **A pasted clause or table row.** Read the value out of it and quote it back.
   Name the row you took, since most of these are tables keyed by occupancy and
   construction type.
3. **A file to read.** Read it, quote the row, cite file and line.

If none arrives, the line prints `[unverified]`. Do not offer a value, do not
search for one, and do not carry a value from one part into another as an
assumption.

**Part 1, occupancy.** Classification for each use. Mixed-use approach.
Separation rating if separated. Incidental or special uses, if any.

**Part 2, construction type.** Type designation. What that type permits in
combustibility terms, in your code's words.

**Part 3, height and area.** Allowable height. Allowable storeys. Base allowable
area. The increase method your code uses, stated as a formula, with each input
named. Then the arithmetic, shown line by line, and the result compared to the
actual.

**Part 4, fire resistance.** Required rating for each building element.
Required rating for exterior walls at each fire separation distance. Opening
protectives and penetrations, as callouts rather than values.

**Part 5, means of egress.** Occupant load summary. Required exits per storey.
Egress capacity factor. Common path limit. Travel distance limit. A pointer to
the dimensional checks rather than the dimensions.

**Part 6, accessibility.** Which parts of the building must be accessible.
Employee work-area treatment. Accessible route requirement. Accessible unit
counts if residential. Accessible means of egress, as a callout.

### Step 4. Show the area arithmetic

Do not print a result without the steps. For the allowable-area line:

```
Formula, as supplied:      <written out>
  base allowable area      <value>   [cited as ...]
  <each increase term>     <value>   [cited as ...]
  = allowable              <result>
Actual area                <value>   [from your input]
Result                     <pass | fail | unverified>
```

If any input to the formula is unverified, the result is `unverified`, not a
number. A formula run on a guessed input produces a confident wrong answer,
which is the failure this whole skill is shaped to avoid.

### Step 5. Assemble and print the block

```
CODE ANALYSIS — <project>
CODE: <code and edition, as supplied>          AHJ: <as supplied>
PREPARED: <date>   ALL VALUES SUPPLIED BY <name>, NOT BY THIS TOOL

1  OCCUPANCY
2  CONSTRUCTION TYPE
3  HEIGHT AND AREA
4  FIRE RESISTANCE
5  MEANS OF EGRESS
6  ACCESSIBILITY

NOTES: <flagged items from Step 1>
UNVERIFIED: <count> lines. Listed below with what each one needs.
```

Every line inside a part carries its value, its citation, and its status. The
unverified count goes at the foot of the block, not buried in it, so nobody
copies the block onto a sheet believing it is complete.

### Step 6. Save, if asked

Ask whether to write the block to a file and where. Write it directly. There is
no template and no script.

## Rules

- **Never supply a code value or a formula.** Not from memory, not from a
  search, not from a figure in this file. There are none in this file.
- **An unverified input makes the result unverified.** Never carry arithmetic
  through a blank.
- **Name the row every table value came from**, including occupancy and
  construction type. A right number off the wrong row reads exactly like a right
  answer.
- **Never convert units** and never round an area to a neater figure.
- Print the unverified count on the block itself, every time.
- Occupancy and construction type are the user's calls, recorded and cited, not
  the skill's determinations.

## Anti-patterns

- Filling a table value from recall because the combination is a common one.
- Searching the web for a table and using what comes back as the value. Search
  finds which code governs; it does not quote it reliably.
- Printing an allowable area from a formula with a guessed base or a guessed
  increase, which is exactly how a cover sheet acquires a number nobody can
  trace.
- Producing a block with no unverified count, so a partial run looks finished.
- Carrying a value from the egress part into the area part, or the reverse,
  without asking whether the same row applies.
- Bundling a table into this skill later. It has none on purpose, and a bundled
  table goes stale silently while still looking authoritative.

## Resources

None. This skill is one file. Output is written directly at the path you name.
