---
name: existing-conditions-survey
description: "Plans and records a measured survey of an existing building so that every dimension later designed against carries its provenance: what to capture before going, how to close a measurement so errors are caught on site rather than in the office, and the discipline of marking every line as measured, taken from a record drawing, or assumed. Produces the record and the list of what still has to be opened up or verified. Trigger on \"measure the existing building\", \"as-built survey\", \"existing conditions\", \"we only have the old drawings\", \"what do I measure on the site visit\", \"existing-conditions-survey\", or a renovation starting with no reliable information. Carries no tolerances and no survey standards; the level of accuracy needed comes from what the drawings will be used for. It is not a land survey — `survey-review` reads one — and not a structural, hazardous materials, or condition assessment, each of which is a specialist's and is named as a hand-off."
license: MIT
metadata:
  title: "Existing Conditions Survey"
  summary: "Record what is actually there, and mark what you did not verify"
  discipline: "design-building-types"
  tags: "Pre-Design, Analysis"
---

# Existing Conditions Survey

Every dimension in a renovation is measured from something. When nobody wrote
down which lines were measured, which came off a drawing from 1974, and which
somebody assumed, the whole set inherits an accuracy nobody can state. The cost
shows up at framing.

## Scope and limits — read first

**What this does.** Plans the visit so the right things get captured the first
time, sets out how to measure so errors are found on site, and records the
result with a provenance mark against every line. Produces the list of what
still needs opening up, and hands the specialist investigations to specialists.

**What this does not do.**

- **It carries no tolerances and no standards.** How accurate is accurate enough
  depends on what the drawings will be used for: a feasibility sketch and a
  shop-drawing background need different work.
- **It is not a land survey.** Boundaries, easements and levels relative to a
  datum are a surveyor's. `survey-review` reads that document.
- **It is not a condition assessment.** Whether something is failing, whether
  the structure is adequate, whether there is asbestos, lead or mould: each is a
  specialist's and each is named as a hand-off. This records what is there, not
  what is wrong with it.
- It does not open anything up. It produces the list of what should be.
- It does not scan or model. Where a point cloud exists, it says what still has
  to be verified by hand, which is more than people expect.
- It does not replace the Architect of Record.

**What you need before starting.** What the drawings will be used for. Whatever
record drawings exist and their date. Access: what you can get into, when, and
what is occupied. The scope of work, so the survey is proportionate.

## Workflow

### Step 1. Fix the purpose, because it sets the effort

Ask, in one message:

> 1. What will these drawings be used for: a feasibility study, a permit set, a
>    construction set, a shop drawing background?
> 2. What is the scope of work? A survey of the whole building for a kitchen
>    renovation is waste; a survey of one room for a structural change is
>    negligence.
> 3. What record drawings exist, from when, and were they as-built or as-issued?
> 4. What access is there: what rooms, what times, what is occupied, is there a
>    ceiling to open, is there a basement and a roof hatch?
> 5. Who is going, with what, and how long do they have?
> 6. Is there a point cloud or a scan?

**Record drawings are the trap.** As-issued drawings show what was designed;
what was built differs, and forty years of unpermitted work differs again.
Establish which kind exists and treat both as unverified until measured.

### Step 2. Build the capture list before going

The things people come back without, every time. Work the list and mark what
this project actually needs:

- Overall dimensions taken as one continuous run, not as a chain of small ones.
- Floor-to-floor and floor-to-ceiling, in several places per floor. They differ.
- Structure: what is visible, where, what direction it spans, what is concealed.
- Every opening: width, height, head height, and which way doors swing.
- Wall thicknesses, and whether structural or not where that is visible.
- Levels: within a floor, and between floors and to grade. Old floors are not
  level and it matters at every threshold.
- Services: panels, meters, boilers, units, where risers run, where they enter.
- Above the ceiling: what is up there, in at least one place per area.
- Roof: assembly if visible, drains, penetrations, equipment.
- Below grade: what the basement shows about the structure and the water.
- Photographs, systematically, with a plan showing where each was taken from.
- What connects to a neighbour: party walls, shared structure, shared services.

### Step 3. Measure so that errors are found on site

The method that separates a survey from a set of numbers:

- **Close every loop.** Measure a room's walls and check the sum against the
  overall dimension taken separately. A closure that does not close is found in
  ten seconds on site and in three weeks in the office.
- **Take running dimensions**, not a chain of individual ones, so errors do not
  accumulate.
- Take one long overall dimension per elevation and per floor to hold everything
  else against.
- Measure diagonals in rooms that matter. Nothing is square.
- Record the datum you used and use the same one everywhere.
- Note what you could not reach and why, at the time, on the sketch.

### Step 4. Record every line with its provenance

The whole point. Every element in the resulting drawing is one of:

| Mark | Means |
|---|---|
| Measured | Somebody measured it, on a date |
| Record | Taken from a record drawing, with its date |
| Assumed | Inferred, patterned from elsewhere, or guessed |

Report the counts, and put them on the drawing. **Anything not marked is
assumed**, and a set that does not distinguish these is a set where every
dimension carries the accuracy of its worst line.

Concealed structure and concealed services are almost always `assumed`. Say so
rather than drawing them confidently.

### Step 5. Produce the two lists that come after

**To be verified before design proceeds.** Things a scheme would be built on
that are currently `record` or `assumed`, ordered by what depends on them.

**To be opened up, and by whom.** Where a wall, a ceiling or a floor has to be
opened, what would be learned, when it has to happen to be useful, and who
carries the cost and the making good. A programme with no decision point after
opening up is a programme that will be broken by what is found.

Then the specialist hand-offs, each named:

- Structural investigation and capacity: the structural engineer.
- Hazardous materials: a survey by a qualified party, **before the scope is
  fixed**. Point at `adaptive-reuse-architect`.
- Land survey and levels to a datum: a surveyor.
- Services capacity and condition: the MEP engineer.
- Building condition and defects: a condition surveyor.

### Step 6. Report

- The provenance counts, first.
- What was captured and what was not, with why.
- Closures that did not close, and what was done about them.
- The verify list and the open-up list.
- The specialist hand-offs, with which have been commissioned.
- What the drawings are and are not fit for, stated plainly, so nobody uses a
  feasibility survey as a construction background.

### Step 7. Save

Ask where. The record is a file that gets read for the life of the project, and
the provenance marks have to survive into the drawing set.

## Rules

- **Fix the purpose before planning the visit.** It sets everything.
- **Every line is marked measured, record, or assumed.** There is no fourth
  state and nothing is unmarked.
- Treat record drawings as unverified, including as-builts.
- Close every loop on site.
- State what the drawings are fit for, on the drawings.
- Never record a condition judgement. That is a specialist's.
- Name the hazardous materials survey before the scope is fixed, every run.

## Anti-patterns

- Redrawing the record drawings and calling it a survey.
- Chaining small dimensions across a long wall.
- Drawing concealed structure with the same line weight as measured structure.
- Coming back without floor-to-floor heights, which is the most common omission.
- Assuming a building is square, level, or symmetrical.
- Surveying the whole building for a small scope, or one room for a large one.
- Fixing the programme before the hazardous materials survey.
- Producing a drawing that does not say what it is fit for.

## Resources

None. This skill is one file. Output is written directly at the path you choose.
