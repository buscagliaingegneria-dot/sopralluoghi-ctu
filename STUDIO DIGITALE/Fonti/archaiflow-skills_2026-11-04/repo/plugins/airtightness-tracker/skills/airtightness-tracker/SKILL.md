---
name: airtightness-tracker
description: "Keeps one dated record of a project's airtightness target from the moment it is written into the specification to the moment it is tested: what the target is and where it came from, which surface the enclosure boundary follows, every junction that has to be sealed and who owns it, every intermediate test and what it found, and every change that moves the number or the boundary. Trigger on \"airtightness tracker\", \"blower door target\", \"track the air leakage requirement\", \"who owns this junction\", \"air barrier sign-off log\", \"airtightness-tracker\", or an air leakage target named with a request to keep track of it. Carries no target values, no test standards and no unit conversions; the target, its units and its test method all come from the specification or the certification the project is chasing. It is not a test, does not model leakage, and does not replace the enclosure consultant or the Architect of Record."
license: MIT
metadata:
  title: "Airtightness Tracker"
  summary: "Track one airtightness target from the spec through the site to the test"
  discipline: "envelope-performance"
  tags: "Tracking"
---

# Airtightness Tracker

An airtightness target is set once, early, by someone who will not be on site,
and tested once, late, when fixing it costs the most. Everything between those
two moments is where the number is won or lost, and almost none of it is
written down anywhere.

## Scope and limits — read first

**What this does.** Keeps one dated log for one project. Records the target and
its provenance, the enclosure boundary as an actual surface, every junction that
has to be sealed with an owner against it, every test and inspection with what
it found, and every change that moves the target or the boundary. It reads back
what is still open at any point.

**What this does not do.**

- **It carries no values.** No target, no units, no conversion between the units
  different standards use, no pass threshold. The target and its units come from
  the specification or the certification, quoted with the standard they belong
  to. A number recorded without its unit and test method is not a target and it
  gets logged as incomplete.
- It does not test anything and it is not a blower door. It records what a test
  found, from the tester's report.
- It does not model or predict leakage. A predicted result is not a tracked one.
- It does not audit continuity. Whether the air barrier is actually continuous
  around the building is `air-barrier-trace`'s work, run against drawings. This
  tracks whether the junctions that audit found have been resolved and by whom.
- It does not assign responsibility. It records the assignment somebody made, or
  records that nobody has.
- It does not replace the enclosure consultant or the Architect of Record.

**What you need before starting.** The target, quoted, with its units, its test
standard, and where it is written. The enclosure boundary, or the fact that it
has not been drawn. The junction list, from `air-barrier-trace` or from the
design team. The project phase.

## Workflow

### Step 1. Record the target and where it came from

Ask, in one message:

> 1. What is the target, in what units, tested to which standard, and where is
>    it written? A number without all four is logged as incomplete.
> 2. Is it a contractual requirement, a certification threshold, or an
>    aspiration? These behave differently when the project gets tight.
> 3. Is there an intermediate target as well as a final one?
> 4. What happens if it is not met? Is there a remedy in the contract?
> 5. Has the enclosure boundary been drawn as a single continuous surface?
> 6. What phase is the project in?

Question 2 is the one that predicts the outcome. An aspiration and a contractual
requirement look identical in the specification and behave nothing alike in
month fourteen.

### Step 2. Record the boundary as a surface, not a concept

Log which face of which assembly the air barrier is on, for every enclosure
type, and where the boundary changes from one plane to another. Record any
volume whose inclusion is undecided: unconditioned basements, attics, adjoining
tenancies, shafts, the space behind a service riser.

An undecided volume is logged as open. It changes both the target's denominator
and who has to seal what, and it is usually decided by accident on site.

### Step 3. Log the junctions with an owner each

| # | Junction | Boundary crosses | Owner | Detail ref | Status | Date | Note |
|---|---|---|---|---|---|---|---|

Status is one of: `not detailed`, `detailed`, `submitted`, `installed`,
`inspected`, `sealed and signed off`. Never invent a status; where nobody has
said, the status is what it was and the note records that it was asked.

Every junction has one owner, named as a trade or a party. **A junction with two
owners has none**, and it gets flagged as such rather than logged as covered.

### Step 4. Log every test, every inspection, and every change

Three kinds of entry, all dated:

- **Test.** Who tested, when, to what standard, what the result was in the
  target's units, and what the report says about the conditions. Record the
  report reference. If the result is in different units from the target, record
  both as given and flag the conversion as not performed here.
- **Inspection.** Who looked, at what, when, and what was found open. Smoke
  testing and thermal imaging get logged here, not as tests.
- **Change.** Anything that moves the target, the boundary, a junction detail,
  or an owner. Record what changed, who decided, and the date. A change with no
  decision-maker recorded is logged as such.

### Step 5. Read back what is open

On request, and at every phase change, report:

- Junctions by status, with `not detailed` and `no owner` first.
- Volumes still undecided.
- The gap between the last test result and the target, in the target's units,
  stated as a measurement and never as a prediction of the final result.
- Changes since the last read-back.
- Whether the target itself has moved, and who moved it.

### Step 6. Write the log

One dated file per project, appended to rather than rewritten. Ask where it
lives on the first run and use the same path after. Every entry carries a date
and a source. There is no template and no script.

## Rules

- **Never supply a target, a unit conversion, or a threshold.** All come from
  the specification or the certification, quoted with the standard.
- A number without units and a test standard is logged as incomplete, never as a
  target.
- Every junction has exactly one owner, or is flagged as having none.
- A predicted result is never logged as a result.
- Record what someone said, with who and when. Never infer a status.
- Report `not detailed` and `no owner` first in every read-back.
- Never convert between units. Record both figures as given and flag it.

## Anti-patterns

- Recording a target without its test standard, which makes two projects'
  numbers look comparable when they are not.
- Converting a result into the target's units so the comparison looks clean.
- Logging a junction as covered because two trades were both mentioned.
- Treating a thermal image or a smoke test as a test result.
- Predicting the final result from an intermediate one.
- Letting the enclosure boundary stay a concept rather than a named surface.
- Rewriting an earlier entry when the target changes. Log the change; keep the
  history.
- Running `air-barrier-trace` from inside this skill. It is a separate audit and
  its output is this log's input.

## Resources

None. This skill is one file. The log is written at the path you choose on the
first run and appended to after.
