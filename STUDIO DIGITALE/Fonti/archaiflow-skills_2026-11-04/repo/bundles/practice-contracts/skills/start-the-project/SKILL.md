---
name: start-the-project
description: "The first hour on a new project: separates the decisions that have to be made before anything is drawn from the ones that can wait, because most projects reverse that and spend a month on the ones that could have waited. Establishes who decides what, what the project is actually being measured on, which unknowns block work and which do not, and what has to be commissioned now to arrive in time. Produces the decision list and the commissioning list, and hands each part off by name. Trigger on \"we just won a project\", \"where do I start\", \"kick off\", \"what do we need before we start designing\", \"start-the-project\", or a new commission with nothing set up. Carries no schedules, no fees and no checklists of deliverables; `drawing-checklist` holds what a phase produces and this holds what a phase has to decide. It does not replace the principal or the Architect of Record."
license: MIT
metadata:
  title: "Start the Project"
  summary: "Settle what has to be decided now, and what can wait"
  discipline: "practice-contracts"
  tags: "Project Management, Pre-Design"
---

# Start the Project

A new project starts with drawing, because drawing is the thing everyone knows
how to do. Six weeks later it turns out nobody established who signs off, the
survey has not been commissioned, and the budget was never tested against the
brief.

The decisions that cost the most are all available in the first week and almost
none of them require a drawing.

## Scope and limits — read first

**What this does.** Sorts what has to happen at the start into three lists:
decisions that block work, things that have to be commissioned now because of
how long they take, and everything that can wait. Names who owns each.

**What this does not do.**

- **It carries no checklist of deliverables.** `drawing-checklist` holds what a
  phase produces. This holds what a phase has to decide, which is different and
  which nothing else covers.
- It does not set the fee or the programme. `fee-estimator` and the programme
  are separate, and this records what they depend on.
- It does not review the contract. `contract-review` does, and it is on the
  commissioning list below.
- It does not do the work it points at. Every item names a skill or a party.
- It does not replace the principal or the Architect of Record.

**What you need before starting.** What the project is. Who the client is and
how they decide. What has been agreed so far, in writing or not. Whether there
is a signed agreement.

## Workflow

### Step 1. Establish what is actually agreed, and with whom

Ask, in one message:

> 1. What is the project, in one sentence, and what has the client actually
>    asked for?
> 2. Is there a signed agreement? If not, what is being relied on, and is work
>    proceeding without one?
> 3. **Who decides?** Not who the contact is. Who can approve a design, approve
>    a cost, and sign. Is it one person, a committee, a board, or someone not in
>    the room yet?
> 4. What has been said or promised so far, including verbally, and by whom?
> 5. What is the client measuring this project on: a date, a budget, an area, a
>    permission, an occupancy, a sale?
> 6. What do they have already: a site, a survey, a brief, a previous scheme, a
>    consultant they intend to use?

**Question 3 is the one that predicts the project.** A client who cannot say who
decides will produce a project that reverses decisions, and knowing that in week
one changes how the work is structured. Point at `stakeholder-map`.

**Question 5 is the second.** A project measured on a date and a project
measured on a budget are run differently, and clients rarely say which unless
asked.

### Step 2. Sort the unknowns into blocking and not blocking

Most of what is unknown at the start does not matter yet. A few things stop
everything, and they are usually the ones nobody commissioned:

| Unknown | Blocks what | Who answers | How long | Commissioned? |
|---|---|---|---|---|

Work through the ones that are usually blocking and usually late:

- **The survey.** Nothing can be drawn accurately without it. Point at
  `survey-review` and `existing-conditions-survey`.
- **The geotechnical investigation.** Blocks the foundation and often the
  levels. Point at `geotech-report-review`.
- **Hazardous materials**, on any existing building, **before the scope is
  fixed**.
- **The zoning position**, and whether the scheme needs discretionary approval.
  Point at `zoning-summary` and `entitlement-tracker`.
- **The code path**, where the building type or the existing building makes it
  non-obvious. Point at `senior-code-consultant`.
- **The budget**, and whether it has ever been tested against the brief. Point
  at `fee-estimator` and `budget-reconciliation`.
- **Utility capacity** on infill and rural sites both.

Order by lead time, not by importance. A four-week survey commissioned in week
one and a two-day zoning check commissioned in week six is the right order even
though the zoning matters more.

### Step 3. List the decisions that have to be made before drawing

Distinct from unknowns: these are choices, not facts.

| Decision | Who makes it | By when | What it blocks |
|---|---|---|---|

Typically: the delivery method, whether the client holds the consultants or the
architect does, what standard of documentation the project gets, whether there
is a phasing constraint, what the client's approval process is and how long each
round takes, and who on the practice's side is doing what.

**Include the practice's own decisions**: who runs it, who draws it, what it is
being priced at, and what it displaces. Point at `utilization-tracker` and
`go-no-go-review` if the pursuit record exists.

### Step 4. Say plainly what can wait

The list nobody writes, and it is what protects the first month:

Materials, finishes, the elevation, the structural system in detail, the
mechanical strategy in detail, anything about the interior beyond area,
furniture, landscape, signage.

Say why each can wait: it depends on something above, or it is reversible, or it
is cheap to change later. **A project that starts with a materials conversation
has spent its first month on the most reversible decision available.**

### Step 5. Set up the record, once

The things that are cheap now and expensive to reconstruct later:

- Where project files live and how they are named. Point at `file-organizer`.
- Which trackers this project will actually keep, and who updates each.
  `project-tracker`, `permit-tracker`, `rfi-tracker`, `drawing-log` — pick the
  ones that will be maintained and skip the rest. A tracker nobody updates is
  worse than none.
- How decisions get recorded, and by whom. Point at `meeting-notes-cleaner`.
- What gets written down about verbal agreements. Point at `/draft-email`.

### Step 6. Report

- Who decides, and the answer to what the project is measured on.
- The blocking unknowns, ordered by lead time, with what is commissioned and
  what is not.
- The decisions due before drawing, with owners and dates.
- What can wait, and why.
- What is being relied on that is not in writing.
- Anything proceeding without a signed agreement, said plainly.

Then ask where to write it. This is read back at every phase change and it is
the document that says whether the project started well.

## Rules

- **Ask who decides**, and refuse to accept the name of the contact as the
  answer.
- Ask what the project is measured on.
- Order the unknowns by lead time, not by importance.
- Say what can wait, explicitly, and why.
- Name every tracker the project will actually keep and skip the rest.
- Say plainly when work is proceeding without a signed agreement.
- Point everything at a skill or a party. Do none of it here.

## Anti-patterns

- Starting with a sketch.
- Treating the client contact as the decision-maker.
- Commissioning the survey after the scheme is drawn.
- Fixing the scope before the hazardous materials survey.
- Never testing the budget against the brief.
- Setting up six trackers nobody will update.
- Spending the first month on materials.
- Working without an agreement and not saying so out loud.

## Resources

None. This skill is one file. Output is written directly at the path you choose.
