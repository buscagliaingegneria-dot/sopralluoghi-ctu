---
name: design-acoustic-separation
description: "Works acoustic separation between two spaces as a whole rather than as a wall or floor rating: establishes what the source is and what the receiver needs, then traces every path sound can take between them, because the assembly's tested rating describes the direct path only and the built result is set by whatever flanks around it. Names the structural decisions that have to be made early and cannot be fixed later. Trigger on \"acoustic separation\", \"STC between these units\", \"impact noise from above\", \"flanking\", \"why is this wall not working acoustically\", \"design-acoustic-separation\", or two spaces with a noise problem between them. Carries no ratings, no laboratory values and no criteria; the target comes from the code, the brief or the acoustician, and every assembly value is a tested figure you cite. It is not acoustic engineering and does not replace the acoustician or the Architect of Record."
license: MIT
metadata:
  title: "Design Acoustic Separation"
  summary: "Build a separation for sound, where the flanking path decides the result"
  discipline: "structure-mep"
  tags: "Design"
---

# Design Acoustic Separation

A wall is specified at a laboratory rating and the built separation comes out
lower, every time. The reason is that the rating describes sound going straight
through the middle of a wall in a test chamber, and in a building the sound goes
around it: through the floor, along the facade, over the ceiling, through a
shared duct. The assembly is the easy half.

## Scope and limits — read first

**What this does.** Establishes the source and the receiver, sets out every path
between them, and reports which paths are addressed and which are not. Names the
decisions that have to be made in the structure and the layout, before anything
is detailed.

**What this does not do.**

- **It carries no values.** No target rating, no laboratory figure for any
  assembly, no impact rating, no background level, no code criterion. The target
  comes from the code, the brief or the acoustician; every assembly figure is a
  tested value you cite with the test and the specimen.
- **It is not acoustic engineering** and it does not predict a result. Flanking
  is modelled by an acoustician with a method; this finds the paths and names
  what has to be assessed.
- It does not build the wall. `design-partition` does one partition and
  `design-wall-assembly` the exterior wall; this says what the separation needs
  of them.
- It does not design mechanical noise control. Duct-borne noise, equipment
  isolation and background levels are the mechanical engineer's with the
  acoustician.
- It does not measure anything, and a tested result on site is a different
  quantity from a laboratory rating.
- It does not replace the acoustician or the Architect of Record.

**What you need before starting.** The two spaces and what each is for. The
target, quoted, and where it comes from. The structure between and around them.
The layout: what is above, below and beside each. What services run between them.

## Workflow

### Step 1. Establish the source, the receiver and the target

Ask, in one message:

> 1. What are the two spaces, and what happens in each? A source and a receiver,
>    not just two rooms.
> 2. What kind of sound: speech, music, machinery, footfall, plumbing? Each
>    behaves differently and airborne and impact are separate problems with
>    separate ratings.
> 3. What is the target, quoted, and from where: the code, the brief, a
>    certification, the acoustician?
> 4. What is the structure between them, and what is the structure around them?
> 5. What is above and below each space, and what is on the other side of each
>    of their other walls?
> 6. What services run between them or serve both?
> 7. Is an acoustician engaged?

**Airborne and impact are separate.** A floor separating a corridor from a unit
below is two problems with two ratings, and the assembly that solves one may not
touch the other.

### Step 2. Trace every path, not just the wall

The separating assembly is one path. Set out all of them:

| # | Path | Through what | Addressed by | Status |
|---|---|---|---|---|

Work through at least:

- **Direct.** Through the separating wall or floor.
- **Flanking along the structure.** A continuous slab, a continuous facade, a
  continuous corridor wall, a structural frame carrying sound around the
  separation. This is usually the path that decides the result.
- **Over the ceiling.** A partition stopping at a suspended ceiling with a
  continuous plenum above. Point at `design-partition`.
- **Under the floor.** A raised floor, a continuous screed, a service void.
- **Around the facade.** Along the exterior wall, through the mullion, through a
  continuous spandrel or a shared window.
- **Through services.** A shared duct, a shared riser, back-to-back outlets,
  plumbing in a shared wall, a shared plenum return.
- **Through openings.** Doors, glazing, transfer grilles, undercuts.
- **Structure-borne.** Anything rigidly connecting the two: a pipe, a hanger, a
  stud, a fixing.

**Report the count of paths that nothing addresses.** That count, not the
assembly's rating, is the honest description of the separation.

### Step 3. Name the decisions that have to be made early

Some of this is settled in the structure and the layout, and cannot be improved
afterwards at any price:

- Whether the structure is continuous through the separation, and whether a
  break is possible.
- Whether the floor is a bare slab, a floating floor, or a slab with a resilient
  layer. This is a build-up thickness and a floor-to-floor decision.
- Whether the layout puts a quiet room against a noisy one at all. Moving a room
  is cheaper than any assembly.
- Whether risers and shafts are shared. Point at `/size-shaft`.
- Whether the ceiling is continuous, and whether the partition can reach the
  structure. Point at `design-partition`.
- Whether the facade is continuous past the separation, and what breaks it.

State which of these are still open and which are already fixed. Anything
already fixed constrains the rest, and saying so early is the point.

### Step 4. Work the openings and the services

Openings and services usually dominate the result:

- Every door in the path: its own rating, its seals, its threshold, and whether
  two doors in series would do what one cannot.
- Every glazed element, including internal glazing and borrowed light.
- Every duct crossing the separation, and whether it is lined, offset, or has
  an attenuator. Named as a question for the mechanical engineer.
- Every penetration, and whether the seal is acoustic as well as rated. Point
  at `penetration-review`, which logs both.
- Back-to-back and near-adjacent boxes, which defeat a wall on their own.
- Plumbing in or against the separation, which is structure-borne and is not
  fixed by mass.

### Step 5. Report

- The paths table, with the unaddressed count first.
- The early decisions, split into open and already fixed.
- Openings and services, with what has to be established for each.
- Every value that was quoted and every value still open.
- What has to reach the acoustician, the structural engineer and the mechanical
  engineer.

Close with the standing limits, every run: no result was predicted, a laboratory
rating is not a built result, and flanking has been found rather than assessed.

### Step 6. Save, if asked

Ask whether to write the assessment to a file and where.

## Rules

- **Never supply a rating, a laboratory value, or a criterion.**
- Separate airborne from impact, every run.
- Trace all the paths, and report the count nothing addresses before anything
  else.
- Never present an assembly's laboratory rating as the separation achieved.
- Name the early decisions and say which are already fixed.
- Say on every run that flanking was found here, not assessed.

## Anti-patterns

- Specifying a wall rating and calling the separation designed.
- Treating airborne and impact as one problem.
- Ignoring the corridor wall and the slab because they are not the separating
  assembly.
- Assuming a plenum above a partition is not a path.
- Back-to-back outlets in a separating wall.
- Recalling a rating for a common assembly.
- Leaving plumbing in the separating wall and expecting mass to fix it.
- Proposing an assembly upgrade when moving the room was available.

## Resources

None. This skill is one file. Output is written directly at the path you choose.
