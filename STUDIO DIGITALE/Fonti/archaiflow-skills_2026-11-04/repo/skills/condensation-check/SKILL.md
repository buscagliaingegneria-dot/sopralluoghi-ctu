---
name: condensation-check
description: "Works out where water condenses inside a wall, roof, or floor assembly: the temperature at every layer boundary from the layer R-values and the design conditions, the dew point of the indoor air from its temperature and relative humidity, and which boundary is the first to fall below it. Then walks the layers in order of vapor permeance to flag a vapor-tight layer sitting on the cold side of the insulation, or two of them sealing the assembly from both directions. Trigger on \"condensation check\", \"dew point in this wall\", \"will this assembly condense\", \"vapor retarder on the wrong side\", \"sheathing temperature\", \"condensation-check\", or an assembly listed layer by layer with indoor and outdoor conditions. Every R-value, permeance, design temperature, and humidity comes from the user, out of manufacturer data, a climate data set, or the project's own documents; the skill supplies the heat-flow and psychrometric relations and never a material property."
license: MIT
metadata:
  title: "Condensation Check"
  summary: "Trace the temperature gradient through an assembly and find the dew point"
  discipline: "envelope-performance"
  tags: "Analysis, Design"
---

# Condensation Check

Give it the layers in order and the conditions on both sides, and it computes
the temperature at every boundary, then tells you which boundary is cold enough
for the indoor air to give up its water. The heat-flow and psychrometric
relations are the only things it knows. Every material property is yours.

## Scope and limits — read first

**What this does.** Takes an assembly layer by layer from inside face to
outside face, each layer with an R-value and a vapor permeance. Computes the
boundary temperatures from the ratio of accumulated R to total R across the
design temperature difference, computes the dew point of the indoor air from
its temperature and relative humidity, and compares the two at every boundary
to name the first condensing plane. Then reads the permeance column in order
and flags a vapor-tight layer sitting on the cold side of the insulation, or a
pair of them that leaves the assembly no direction to dry in.

**What this does not do.**

- **It does not know any material properties.** No R-values, no permeance
  ratings, no conductivities, no thicknesses. Every one comes from you, off a
  manufacturer's data sheet or a source you name. That is the design, not a gap.
- It does not know your design conditions. Outdoor design temperature, indoor
  temperature, indoor relative humidity: those come from a climate data set and
  from how the building is meant to be run, both yours to bring.
- It does not know what your code requires. The ratio of continuous exterior
  insulation to cavity insulation, the vapor retarder class permitted in your
  climate zone, whether a given retarder is allowed behind a given sheathing:
  that is code text. Quote the requirement and the arithmetic gets held against
  it. It will not be recalled.
- **Steady-state, one dimension.** One temperature difference through a stack of
  flat layers. No thermal bridges (framing, slab edges, shelf angles,
  fasteners), no moisture stored in the materials, no drying across a season, no
  sun-driven inward vapor drive. An assembly that clears here can still condense
  at the stud.
- **It does not model air leakage.** Air moving through a gap carries far more
  water than diffusion through the layers does, and it is the mechanism behind
  most condensation that actually happens. This skill sees the layers, not the
  holes. Run `air-barrier-trace` for those.
- It is not WUFI. A hygrothermal simulation runs hourly weather against material
  storage curves over years. This is the hand check you do before deciding
  whether that simulation is worth commissioning.
- It does not replace the enclosure consultant or the Architect of Record.

**What you need before starting.** The assembly in order, inside face to outside
face, with an R-value per layer and, for the vapor pass, a permeance per layer
with its unit and test method. The outdoor design temperature, the indoor
temperature, and the indoor relative humidity, each with its source. If you want
a verdict rather than a measurement, the code requirement you are checking
against, quoted.

## Workflow

### Step 1. Take the assembly in order

Ask, in one message:

> 1. The layers, inside face to outside face, in order, named. Order is the
>    whole thing: the same layers in a different sequence give a different
>    answer.
> 2. The R-value of each layer and where it came from. Air films are layers
>    too; if you have no value for them, say so and they will be carried as
>    unverified rather than assumed.
> 3. The permeance of each layer, with the unit (US perms, ng/Pa·s·m²) and the
>    test method (dry cup, wet cup) if you have it. A layer with no figure is
>    carried as unknown, never as vapor-open.
> 4. Outdoor design temperature, indoor temperature, indoor relative humidity,
>    and the source of each.
> 5. Which season. Winter, heat flowing out, is the usual run; a
>    cooling-dominated climate with a vapor-tight interior finish needs the
>    summer run as well.

Read the layer list back, numbered, before computing anything. An assembly
entered outside-in produces a clean-looking table that is exactly backwards.

### Step 2. Compute the boundary temperatures

Total R first, term by term, then each boundary, with the formula printed on
the line above the arithmetic:

```
R_total       <sum, shown term by term>
boundary n    T = T_out + (R accumulated outside of n / R_total) x (T_in - T_out)
```

Print the accumulated R beside each boundary temperature so any line can be
re-derived. State in the output that this heat-flow relation is one of the two
things the skill supplies itself.

### Step 3. Compute the dew point of the indoor air

From the indoor temperature and relative humidity, using the published
psychrometric relation. Print the formula, then the arithmetic, then the
approximation it carries. If you were given a dew point directly, use it and say
the derivation was skipped.

### Step 4. Compare, and name the first condensing plane

| Boundary | Temperature | Dew point | Margin | Condenses |
|---|---|---|---|---|

Walk from the warm side out and name the first boundary at or below the dew
point. That is the condensing plane, and it is where the water shows up. If no
boundary falls below, say so and name the smallest margin instead.

Report the margin as a number and stop there. **The skill holds no safety
threshold.** How much margin is enough is your judgement or your code's, and
saying a two-degree margin passes would be supplying a value nobody gave.

### Step 5. Walk the permeance in order

Read the permeance column from inside to outside and report three things:

- Where the lowest-perm layer sits relative to the insulation. A vapor-tight
  layer on the cold side stops outward drying and puts the condensing plane
  against itself.
- Whether two low-perm layers have the insulation between them. Then nothing
  that gets in can leave in either direction.
- Which direction the assembly can dry. State it as a direction, not a rate:
  there is no drying-rate model here.

Flag these, do not rule on them. Which retarder class each layer falls into, and
which class your climate zone permits, is code text you supply.

### Step 6. Report

The thermal table, then the vapor table, then prose: where the condensing plane
lands, what moving the insulation or the retarder would do to it, and what the
permeance order says about drying. Count the unverified inputs on the face of
the output.

Close every run with the standing limits: steady state, one dimension, framing
not in the arithmetic, air leakage not modeled.

### Step 7. Save, if asked

Ask whether to write the check to a file and where. Write it directly, formula
lines included. There is no template and no script.

## Rules

- **Never supply a material property.** Not an R-value, not a permeance, not in
  an example, not as a placeholder that looks like a number.
- Print the formula before the arithmetic, every time. A boundary temperature
  nobody can re-derive is not checkable.
- Read the layer order back before computing.
- Never convert units silently. If R-values arrive in one system and
  temperatures in another, stop and ask which system to run in.
- A margin is a measurement. Whether it is enough is a judgement you or your
  code makes, and it is never asserted here.
- Say on every run that air leakage is not modeled.
- Every value carries its citation or the words `not cited`. There is no third
  state.

## Anti-patterns

- Recalling a per-inch R-value for a common insulation because it is
  "standard". Manufacturers differ, products change, and the figure typed in is
  the one that has to be defensible.
- Recalling the ratio of exterior to cavity insulation a code requires, or the
  retarder class a climate zone permits. Both are code text and both go stale.
- Quoting a clause found by web search. Search identifies which document
  governs; it does not verify what the document says.
- Reporting the assembly as clear when the permeance column was never supplied.
- Presenting the result as covering the whole wall when the framing was never in
  the arithmetic.
- Running the numbers on an assembly listed outside-in.

## Resources

None. This skill is one file. Output is written directly at the path you choose.
