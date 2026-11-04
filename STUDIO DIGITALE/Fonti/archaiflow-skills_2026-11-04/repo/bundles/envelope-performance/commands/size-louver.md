---
title: Size Louver
summary: Add up the louver face a mechanical airflow needs, from data you supply
discipline: envelope-performance
tags: ["Analysis"]
description: "Adds up the face area a louver needs from the airflow the engineer gives and the performance data of the actual louver being considered: required free area from airflow and maximum face velocity, required face area from the product's free-area fraction, then the fit into the opening the elevation actually has, mullions and frames included. Reports required face size against the opening as drawn. Carries no velocities, no free-area percentages, and no rain-class limits; the airflow comes from the mechanical engineer and every performance figure from the data sheet of the named louver, because free area varies by product and by size and a remembered percentage sizes the wrong louver. It does not size the duct or the fan behind the louver — `design-duct` does — it does not lay out the room the air serves (`design-mechanical-room`), and it does not compose the elevation the louver lands on (`facade-module`)."
argument-hint: <airflow> <louver-model> [opening-as-drawn]
---

# Size Louver

A louver is sized twice: once by the engineer, in free area, and once by the
elevation, in face area. The gap between those two numbers is the free-area
fraction of the specific product, and it is the number everyone remembers
instead of reading. The remembered figure sizes a louver that whistles, drinks
rain, or does not fit the opening the facade already committed to.

## Scope and limits — read first

**What this does.** Takes the airflow, the maximum face velocity, and the
free-area data of the named louver, and works out the face size required:
free area first, face area from the product's fraction, then the fit against
the opening as drawn, frames and mullions counted.

**What this does not do.**

- It carries **no performance figures.** No face velocities, no free-area
  percentages, no rain-class thresholds, no screen deratings. Every figure
  comes from the data sheet of the named product or from the engineer, with
  its source stated.
- It does not size the airflow. The CFM is the mechanical engineer's number.
  `design-duct` sizes what runs behind the louver.
- It does not place the louver on the elevation. `facade-module` holds the
  panelization; this reports the face area the opening has to yield.
- It does not check code clearances. Distance from grade, from property
  lines, from exhaust to intake, and from anything that burns is code and
  mechanical-code text, quoted by you, never recalled.

**What you need before starting.** The airflow per louver from the engineer,
whether it is intake or exhaust, the named louver product and its data sheet,
the opening as drawn if there is one, and any velocity or rain criterion the
engineer or the spec sets.

## Inputs the command needs

1. **The airflow**, per louver, with the engineer named as its source, and
   whether the louver is intake or exhaust, because the allowable velocities
   differ and both come from the data or the engineer.
2. **The louver**, by manufacturer and model, with its data sheet: free-area
   fraction at the size in question, maximum recommended face velocity or the
   beginning-of-water-penetration velocity, and the frame dimensions.
3. **The screen**, if any. Bird and insect screens reduce free area by an
   amount the data sheet states; an insect screen is not a bird screen.
4. **The opening as drawn**, if the elevation already has one, with what
   surrounds it.
5. **Any criterion from the spec or the engineer**: a velocity limit, a rain
   class, a pressure-drop budget.

## Workflow

### Step 1 — Read the inputs back and flag what is missing

List each figure with its source. Anything without a source is `not supplied`
and stays that way. Never substitute a typical velocity or a typical free-area
percentage; free area varies by product and by size, and the data sheet's
figure at the tested size is the only one that counts.

### Step 2 — Work out the free area

```
required free area = airflow / maximum face velocity     <arithmetic shown>
```

Both terms with their sources beside them. If a screen derating applies, apply
it here, from the data sheet's figure, shown.

### Step 3 — Work out the face area

```
required face area = required free area / free-area fraction   <arithmetic shown>
```

State the fraction's source and the size it was tested at. If the required
louver is much smaller than the tested size, say the fraction will be lower at
small sizes and the data sheet or the manufacturer has to confirm it; do not
extrapolate.

### Step 4 — Fit it to the opening

```
face required     <width x height options that satisfy the area>
frame and mullions <from the data sheet, subtracted from the glass line>
opening as drawn  <as given>
difference        <fits / short by, in the user's units>
```

A louver bank has mullions and a frame, and the free area lives inside them.
If the opening as drawn is short, report by how much and note the two moves:
a bigger opening, or a product with a higher fraction, both of which are
decisions for the engineer and the elevation, not for this command.

### Step 5 — Report and hand off

The table, then: every `not supplied` figure counted, the intake-exhaust
distinction confirmed, and the hand-offs named. Clearances to grade, property
lines, other openings, and contaminant sources are code text you quote;
whether the pressure drop works is the engineer's; where the louver sits on
the elevation is `facade-module`.

### Step 6 — Save, if asked

Ask whether to write the sizing to a file and where.

## Rules

- **Never supply a velocity, a fraction, or a derating.** Every term carries
  its source, and the source is a data sheet or the engineer.
- Show the arithmetic at every step, in the user's units, never converted.
- Free area varies by size: state the tested size next to the fraction, every
  run.
- Intake and exhaust are different problems. Confirm which this is.
- Code clearances are quoted by the user or left as named open questions.
- Never pick the louver. This sizes the face the airflow needs; the product
  is the spec's decision.

## Anti-patterns

- Using a remembered "about 50%" free area. The range across real products is
  wide, and the remembered figure is wrong in the direction that whistles.
- Sizing at the data sheet's velocity for a louver in a rain class the spec
  does not allow.
- Ignoring the screen because it is a screen.
- Extrapolating a big louver's fraction down to a small louver.
- Treating the opening as drawn as the requirement instead of the constraint.
- Quoting a code clearance from memory instead of asking for the text.
