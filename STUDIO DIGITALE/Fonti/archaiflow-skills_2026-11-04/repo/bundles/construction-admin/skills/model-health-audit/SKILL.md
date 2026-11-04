---
name: model-health-audit
description: "Audits a building model for the practices that decide whether it stays usable: what the model is actually for and whether it is being built to that, whether geometry is modeled or drafted over, whether the data the project committed to deliver is present and consistent, what is warning or duplicated, and whether the file can be shared with consultants without an explanation. Reports by frequency and separates what will get worse from what is merely untidy. Trigger on \"model health check\", \"audit this Revit model\", \"why is the model so slow\", \"is the model ready to share\", \"BIM standards audit\", \"model-health-audit\", or a model handed over before an exchange. Carries no software-specific counts, no thresholds and no office BIM standard; the standard and the delivery requirements come from your BEP or your office. It reviews practice rather than drawings — `drawing-standards-audit` reads the sheets. It does not replace the BIM manager or the Architect of Record."
license: MIT
metadata:
  title: "Model Health Audit"
  summary: "Audit a BIM model for the habits that make it slow, wrong, or unshareable"
  discipline: "construction-admin"
  tags: "Review"
---

# Model Health Audit

A model gets audited when it is slow. By then the causes are eighteen months
old. The useful audit asks a different question first: what is this model for,
and is it being built as though that were true.

## Scope and limits — read first

**What this does.** Establishes the model's purpose from the execution plan or
from what the project actually committed to deliver, then audits practice
against that purpose. Reports findings by frequency and separates the ones that
compound from the ones that are cosmetic.

**What this does not do.**

- **It carries no thresholds and no software-specific rules.** No warning
  counts, no file size limits, no element count guidance, no naming convention.
  The standard comes from your BIM execution plan or your office, supplied.
- It is software-agnostic. Where you name the platform, the findings can be
  described in its terms; the audit itself is about practice.
- It does not open or run anything. It reads what you export or describe: an
  audit report, a warning list, a schedule, a directory, a description.
- It does not audit the drawings. `drawing-standards-audit` does.
- It does not fix, purge, or reorganise anything.
- It does not replace the BIM manager or the Architect of Record.

**What you need before starting.** The BIM execution plan, or a statement of
what the model is for and what has to be delivered from it. Whatever the
platform can export: warnings, element counts, file size, worksets or their
equivalent, view counts, family or component lists. Who else uses the model and
how.

## Workflow

### Step 1. Establish what the model is for

Ask, in one message:

> 1. What is this model for? Drawings, coordination, quantities, energy
>    analysis, handover data, facilities management, or several?
> 2. Is there a BIM execution plan? What data has the project committed to
>    deliver, at what stage, in what format?
> 3. Who else uses it and how: linked, exchanged, federated, or in a common data
>    environment?
> 4. What platform, and what can you export?
> 5. What prompted the audit: slowness, an exchange, a stage, or routine?

**Most model problems are purpose problems.** A model built for drawings and
asked for quantities was not built wrong; it was built for something else. Say
which case this is before reporting anything, because the two need opposite
remedies.

### Step 2. Geometry: modeled, drafted, or faked

Report the balance between what is modeled and what is drawn over the top:

- Detail lines, filled regions and drafted views standing in for geometry.
- Elements modeled with the wrong category, which breaks every schedule and
  filter downstream.
- Geometry modeled at a level of detail the purpose does not need, which is the
  other failure and costs performance for nothing.
- In-place or one-off elements where a repeatable component was available.

Each of these is fine in small numbers and compounds. Report counts, and mark
each as **compounds** or **cosmetic**.

### Step 3. Data: present, consistent, and going somewhere

Against the delivery commitment from Step 1:

- Which committed parameters exist, and which are empty.
- Whether the same information lives in two parameters with two answers.
- Whether values are typed consistently: free text where a list was intended,
  units mixed, spelling variants of the same value.
- Whether anything is held in a comment field that was meant to be structured
  data.

Report by parameter, not by element. A parameter empty on nine hundred elements
is one finding.

### Step 4. Warnings, duplicates and what is quietly wrong

- Warnings by type and count, ordered by count.
- Duplicates: elements in the same place twice, which corrupt every quantity.
- Elements far from the origin, unplaced, or in no workset.
- Broken or unresolved links, and links to files nobody can find.
- Anything unresolved for a long time, which is a process finding rather than a
  technical one.

### Step 5. Shareability

Whether this model can go to a consultant without an explanation attached:

- Origin and coordinates: shared, and agreed with whom?
- Levels and grids: named as everyone else names them?
- Naming: files, views, worksets, components, against the standard.
- What has to be told to the recipient about how the model is built, and whether
  any of that should have been a modeling decision instead.
- Whether the export the exchange requires actually produces what it should.

### Step 6. Report by frequency and by consequence

| Finding | Count | Compounds or cosmetic | Against purpose |
|---|---|---|---|

Ordered by count within `compounds` first. Then:

- The three findings most worth fixing, with what each would take.
- What is a purpose mismatch rather than a fault, named as such.
- What could not be audited, and what export would allow it.

Say plainly which findings are the BIM manager's process and which are
individual habit. They are fixed differently.

### Step 7. Save, if asked

Ask whether to write the audit to a file and where. CSV where it becomes a task
list.

## Rules

- **Never supply a threshold or a count anyone should aim at.**
- **Establish the purpose first**, and say when a finding is a purpose mismatch
  rather than a fault.
- Report by parameter and by warning type, never element by element.
- Mark every finding `compounds` or `cosmetic`.
- Never open, run, purge, or change anything.
- Say what could not be audited and what export would fix that.

## Anti-patterns

- Reporting a warning count as though a number were the goal.
- Auditing against a remembered platform best practice.
- Treating a model built for drawings as a failed coordination model.
- Listing findings element by element.
- Recommending a purge as the answer to a structural problem.
- Ignoring the delivery commitment because the drawings look fine.
- Confusing individual habit with a missing process.

## Resources

None. This skill is one file. Output is written directly at the path you choose.
