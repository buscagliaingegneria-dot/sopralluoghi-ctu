---
name: facade-access-study
description: "Works out how every part of a building's envelope will be reached after it is built: cleaned, inspected, repaired, and, for glass, replaced. Inventories the envelope by zone, holds candidate access methods against each one — reach from grade, rope descent, davits, a building maintenance unit, interior access — and reports what each method demands of the design now: roof space, structure, anchors, parapets, and ground kept clear. Trigger on \"facade access\", \"how do we clean this\", \"window washing\", \"BMU\", \"davits\", \"rope access\", \"facade-access-study\", \"how does the glass get replaced\", or a tall or complex envelope with no maintenance story. The zoning of the envelope and the demands table are the skill's method; every load, every regulation, and every equipment figure comes from elsewhere: anchor and davit loads are the structural engineer's, the rules for suspended access are regulatory text the user quotes, and reach figures come from the equipment's own data."
license: MIT
metadata:
  title: "Facade Access Study"
  summary: "Work out how every face of the envelope gets reached, cleaned, and replaced"
  discipline: "envelope-performance"
  tags: "Envelope, Analysis"
---

# Facade Access Study

Every envelope gets cleaned, inspected, and eventually repaired, and on most
projects nobody designs for it: the access plan arrives after the roof is
full, the parapet is low, the landscaping blocks the boom lift, and the
biggest piece of glass has no route to the third floor. This study asks the
question while the design can still answer it.

## Scope and limits — read first

**What this does.** Splits the envelope into zones, asks what each zone needs
over its life — washing, inspection, sealant, glass replacement — and holds
the candidate access methods against each zone: what reaches it, and what
that method demands of the design now. Output is a zone-by-method matrix plus
the list of demands the design has to absorb: roof space, structure, anchor
points, parapet decisions, and ground kept permanently clear.

**What this does not do.**

- **It is not the fall-protection or suspended-access design.** Anchor
  layouts, davit engineering, and the certified system are a specialist's and
  a structural engineer's work, stamped. This study decides that the building
  will have a workable system and reserves what it needs.
- **It carries no regulatory values.** Rules for suspended maintenance,
  anchor loads, and window-cleaning provisions are regulatory and standards
  text that you quote, never recalled, because the requirements are
  jurisdictional and they change.
- It carries no equipment figures. A boom lift's reach, a BMU's outreach, and
  a davit's capacity come from the equipment's data or the consultant, with
  the source named.
- It does not design the roof or the structure it asks for. It reports the
  demand; `design-roof-assembly` and the engineer absorb it.

**What you need before starting.** Elevations or a massing with heights, the
envelope materials by area, what surrounds the building at grade, what the
roof already carries, and any maintenance expectations the owner has stated.

## Workflow

### Step 1. Inventory the envelope

Ask, in one message:

> 1. The elevations: heights, and what each face is made of.
> 2. What each surface needs over its life, as the owner and the
>    manufacturers state it: washing and how often, inspection, sealant
>    renewal, and whether glass units are replaceable from inside.
> 3. The ground around each face: setbacks, landscaping, canopies, water,
>    slopes, property lines, overhead wires, and anything a machine cannot
>    drive on.
> 4. The roof: what is already up there, the parapet heights, and what the
>    structure below was told to carry.
> 5. Any regulation or standard your jurisdiction applies to suspended or
>    powered access, quoted, or the note that it has not been pulled yet.

Then split the envelope into zones: a zone is a stretch of facade that one
method could plausibly serve. Name them; the rest of the study is per zone.

### Step 2. List the candidate methods per zone

For each zone, the methods that could reach it, from cheapest to most
committed, each with what it needs stated beside it:

- **From grade**: water-fed pole, ladder, boom or scissor lift. Needs
  surface, clearance, and reach the equipment's data confirms.
- **Rope descent from anchors or davits**: needs anchor points or davit
  bases, structure behind them, a parapet that works with it, and the
  regulatory ceiling your quoted text sets.
- **A building maintenance unit**: needs roof space, a track or parking
  position, structure, and a consultant early.
- **From inside**: operable or pivoting units sized so the work happens from
  the floor. Needs the window system to agree.
- **Occasional crane or lift closure**: legitimate for rare events like unit
  replacement, but it is a plan only if the street or the yard will actually
  close, which is a fact to check, not assume.

A zone with no plausible method is the finding, not a gap in the study.

### Step 3. Work out the glass replacement path

Separately from cleaning, because it is the question that gets missed: for
the largest unit in each zone, how does it leave the building and how does
its replacement arrive? Route, elevator or hoisting, the opening it passes
through, and what closes while it happens. A unit that arrived by crane
before the roof went on has no return trip; say so where it is true.

### Step 4. Build the matrix

| Zone | Face | Needs | Method | What it demands of the design | Source for reach and rules | Open questions |
|---|---|---|---|---|---|---|

One row per zone-method pair worth keeping. The demands column is the point
of the study: it is the list of things that must be designed in now: the
davit bases and their structure, the roof space, the parapet height decision,
the ground kept clear, the operable units.

### Step 5. Report

The matrix, then in prose: the zones with one method or none, the demands
that conflict with the current design, and the decisions that get expensive
if they wait. Then the hand-offs, named: loads and anchors to the structural
engineer, the certified system to the access consultant, the regulatory text
to whoever pulls it, quoted next time this study runs.

Close every run with: this is the design-stage plan; the certified access and
fall-protection design is a specialist's, and nothing here substitutes for
it.

### Step 6. Save, if asked

Ask whether to write the study to a file and where. Write it directly. There
is no template and no script.

## Rules

- **The zoning and the demands table are the only things this skill
  supplies.** Every reach figure, load, and rule carries a named source: the
  equipment's data, the engineer, or regulatory text the user quotes.
- Glass replacement is asked about on every run, separately from cleaning.
- A zone with no method is reported as the finding, in the first paragraph,
  not softened into an open question.
- Grade-level methods are checked against the actual ground: the planting
  plan and the canopy count as much as the setback.
- The regulatory ceiling for rope access is quoted or the question stays
  open. Never recalled.
- Never present the study as the access design. It reserves; the specialist
  designs.

## Anti-patterns

- Quoting an anchor load, a rope-access height limit, or an OSHA provision
  from memory instead of asking for the text.
- Assuming the boom lift can drive where the landscape plan put trees.
- Solving every zone with "BMU" without reporting what the BMU demands of
  the roof and the structure.
- Treating the atrium's inside faces as somebody else's problem. Interior
  glazing at height is the same study.
- Forgetting the canopy: it blocks the lift and it also has a top surface
  somebody has to reach.
- Calling the study complete with the glass replacement question unanswered.

## Resources

None. This skill is one file. Output is written directly at the path you
choose.
