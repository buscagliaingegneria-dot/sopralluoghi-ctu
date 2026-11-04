---
name: penetration-review
description: "Works through every penetration of a rated, acoustic or structural assembly and asks the three questions that get answered separately and should be answered together: what performance the assembly has to keep, what physically closes the hole, and whether a listed or tested system exists for that penetrant in that assembly. Builds the register across disciplines, since penetrations are made by trades who never see each other's drawings. Trigger on \"penetration review\", \"firestopping check\", \"what closes this hole\", \"acoustic penetrations\", \"sleeve schedule review\", \"penetration-review\", or an MEP set laid over the rated wall plan. Carries no listings, no ratings and no acoustic values; the required performance comes from your code analysis and every closure is a listed or tested system you cite. For the assembly's own continuity use `design-fire-barrier`; for air and water use `air-barrier-trace`. It does not replace the Architect of Record."
license: MIT
metadata:
  title: "Penetration Review"
  summary: "Find every hole through an assembly and say what closes it, and to what"
  discipline: "structure-mep"
  tags: "Review"
---

# Penetration Review

Penetrations are made by five trades who never read each other's drawings,
through assemblies drawn by a sixth. Each hole is closed by somebody, to some
standard, with a product chosen on site. The register is the only place all of
it comes together, and most projects do not have one.

## Scope and limits — read first

**What this does.** Builds a register of every penetration through every
assembly with a performance requirement, and for each one records the required
performance, the physical closure, and the listing or test that supports it.

**What this does not do.**

- **It carries no listings, ratings or values.** Required fire ratings come from
  your code analysis; acoustic requirements from the specification or the
  acoustician; every firestop system is a listed system you cite by number from
  the listing document.
- **It does not verify a listing.** Whether a system is listed for that
  penetrant, that assembly, that annular space and that orientation is checked
  against the listing itself. This checks whether anyone has cited one.
- It does not cover the assembly's own continuity. `design-fire-barrier` traces
  the surface; this reviews what goes through it.
- It does not cover air, water and vapor. `air-barrier-trace` does, and a
  penetration usually breaches both, which is why the register notes it.
- It does not do structural work. A penetration through a structural element is
  the engineer's to approve.
- It does not replace the Architect of Record.

**What you need before starting.** The rated assembly plan and legend. The
acoustic requirements, if any. Every discipline's drawings: mechanical,
electrical, plumbing, fire protection, communications, security, and the
structural set. The specification section on firestopping.

## Workflow

### Step 1. Establish what has performance to keep

Ask, in one message:

> 1. Which assemblies carry a required performance, and what is it? Fire, smoke,
>    acoustic, structural, air, or several at once.
> 2. Where does each requirement come from? Quote it.
> 3. Which discipline drawings do you have, and at what revision?
> 4. What does the specification say about firestopping: who provides it, to
>    what standard, and whether submittals are required per condition?
> 5. Is there a coordinated model, or are these separate drawings?

**An assembly usually carries more than one requirement**, and they are closed
by different products. A rated wall that is also an acoustic separation needs
both, and a firestop that satisfies the rating may not satisfy the acoustic
requirement.

### Step 2. Build the register, discipline by discipline

Work each discipline's drawings over the assembly plan and log every crossing.

| # | Assembly | Requirements | Penetrant | Discipline | Size | Closure | Listing cited | Status |
|---|---|---|---|---|---|---|---|---|

Do not summarise by type. A register saying "all pipe penetrations" is not a
register; the listing depends on the pipe's material, size, insulation and the
assembly it passes through, and those vary along one wall.

Include the penetrations nobody draws: recessed boxes, back-to-back outlets,
control joints, structural connections, anchors, hangers, and anything a
specialist trade brings later.

### Step 3. Check each one for the three questions together

For every row:

- **What performance must be kept?** All of the assembly's requirements, not
  just the fire rating.
- **What closes it?** A named physical closure. "Firestop" is not a closure; a
  system is.
- **Is there a listing for this exact condition?** Penetrant material, size,
  insulation, annular space, assembly type, and orientation all have to match.
  Mark `cited`, `not cited`, or `no known system`.

`no known system` is a real outcome and it means the design has to change. It is
found on site otherwise.

### Step 4. Find the ones that only appear across disciplines

The value of doing this in one register:

- **Two penetrants too close together.** Listings specify minimum separation
  between penetrations, and two trades each drew a hole without seeing the
  other.
- **Back-to-back penetrations** through the same assembly.
- **Penetrations clustered enough to compromise the assembly** structurally or
  in aggregate.
- **A penetration through a structural element** that the structural drawings do
  not show.
- **Something crossing a dedicated space or a clearance zone.** Point at
  `design-electrical-room`.
- **A penetration through an assembly that also carries the air barrier.** Point
  at `air-barrier-trace`.

### Step 5. Report

- Counts by status, `no known system` and `not cited` first.
- Cross-discipline conflicts, individually.
- Penetrations of structural elements, listed for the engineer.
- Assemblies where the acoustic requirement was not addressed alongside the
  fire rating.
- What could not be reviewed: missing discipline drawings, drawings at different
  revisions, a specification that does not say who provides firestopping.

Close with the standing limits: no listing was verified, and the register
records what is drawn rather than what will be built.

### Step 6. Save

Ask where. CSV, because the register becomes a submittal checklist and an
inspection list.

## Rules

- **Never supply a listing number, a rating, or an acoustic value.**
- **Never verify a listing.** Record whether one was cited.
- Log every penetration individually. Never summarise by type.
- Record all of an assembly's requirements, not only the fire rating.
- Include the penetrations nobody draws.
- Check separation between adjacent penetrations across disciplines.
- Say plainly when there is no known system.

## Anti-patterns

- Reviewing the mechanical drawings and calling it a penetration review.
- Logging "typical pipe penetration" for a run of different pipes.
- Recalling a firestop system number.
- Addressing the fire rating and not the acoustic requirement.
- Missing two penetrations too close together because each discipline was
  reviewed alone.
- Treating a recessed box as too small to matter.
- Accepting "firestop per specification" as a closure.
- Reviewing drawings at different revisions without saying so.

## Resources

None. This skill is one file. The register is written at the path you choose.
