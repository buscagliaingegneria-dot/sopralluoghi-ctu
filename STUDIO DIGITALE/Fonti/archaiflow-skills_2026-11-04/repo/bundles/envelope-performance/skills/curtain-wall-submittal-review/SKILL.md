---
name: curtain-wall-submittal-review
description: "Reads a curtain wall or unitised facade submittal package as a system rather than as a set of sections: checks that the drainage and pressure-equalisation strategy is coherent through every joint, that the thermal break line is continuous and lands where the wall's insulation does, that movement is provided for at stack joints and anchors, that the tested system and the drawn system are the same system, and that the interfaces to every adjoining assembly have an owner. Trigger on \"curtain wall shop drawing review\", \"unitised facade submittal\", \"review the glazing submittal\", \"stack joint detail review\", \"is the thermal break continuous\", \"curtain-wall-submittal-review\", or a facade shop drawing package handed over for comment. Carries no performance criteria, no test values and no tolerances; all come from the specification and the test reports, quoted. It reviews and comments, does not stamp or approve, and does not replace the facade engineer or the Architect of Record."
license: MIT
metadata:
  title: "Curtain Wall Submittal Review"
  summary: "Read a curtain wall submittal for the things a general review will not catch"
  discipline: "envelope-performance"
  tags: "Review"
---

# Curtain Wall Submittal Review

A general submittal review reads a package against the documents. A curtain wall
package needs that plus one thing more: it has to be read as a system, because
its failures are systemic. A drainage path is either continuous through every
joint in the grid or it is not, and no single section shows that.

## Scope and limits — read first

**What this does.** Reads a curtain wall or unitised facade package for the six
system-level questions that a section-by-section review does not reach: the
drainage and pressure-equalisation strategy, the continuity of the thermal break
line, the provision for movement, the match between the tested system and the
drawn one, the interfaces to adjoining assemblies, and the sequence the system
requires. It produces comments; it does not act on them.

**What this does not do.**

- **It carries no criteria.** Air and water performance classes, structural test
  pressures, deflection limits, thermal performance targets, tolerances: all
  from the specification, quoted. Without the specification it reports
  observations and no verdicts.
- It does not replace the general submittal review. Product data, finishes,
  glass makeup, warranties and the rest are `submittal-review`'s work. Run both.
- **It does no engineering.** Mullion sizing, anchor design, deflection,
  thermal stress in the glass, seismic drift: the facade engineer's. This names
  where those live and whether the package addresses them.
- It does not verify test reports. Whether a test was validly performed, on what
  specimen and to what standard, is between the testing agency, the specification
  and the facade engineer. This checks whether the tested configuration and the
  submitted configuration are the same one.
- It does not stamp, approve, or take exception on anyone's behalf. It writes
  the comments; the Architect of Record acts.
- It does not replace the facade engineer or the Architect of Record.

**What you need before starting.** The submittal package. The specification
section, quoted. The contract drawings for the interfaces. Any test reports
being relied on. The reviewed shop drawings of adjoining assemblies, if they
exist.

## Workflow

### Step 1. Establish what is being relied on

Ask, in one message:

> 1. What is in the package: plans, elevations, sections, details, calculations,
>    test reports, samples?
> 2. Which specification section governs, and can you quote its performance
>    requirements?
> 3. Is the system proprietary and previously tested, engineered for this
>    project, or a hybrid? A hybrid is the case that needs the most attention
>    and it is often not declared.
> 4. Which test reports are being relied on, and on what specimen?
> 5. Which adjoining assemblies does this meet, and have those been submitted?
> 6. What is the review turnaround, and what is on the critical path behind it?

### Step 2. Trace drainage and pressure equalisation through the whole grid

Not at one section. Follow water from where it enters to where it leaves:

- Into the glazing pocket, out through the weeps: at every horizontal.
- Down the vertical joints: what carries it, and where does it cross a
  horizontal without leaking into the interior side?
- At the stack joint in a unitised system: the single most consequential
  detail in the package.
- At the bottom of the facade, and at every interruption: a spandrel, a floor
  slab, a change of module, a corner.
- Where the drainage discharges, and onto what.

If pressure equalisation is claimed, ask where the compartment boundaries are
and whether they are continuous. A pressure-equalised system with unbounded
compartments is a drained system with a claim attached.

### Step 3. Trace the thermal break line

Follow it as one line around the whole facade, and report where it breaks:

- Through the vertical and horizontal members.
- At the stack joint and the anchor.
- Where the facade meets the slab edge, and whether the wall's insulation and
  the frame's break land on the same plane.
- At corners, at spandrels, at the head and the base.
- At every anchor and bracket, since anchors are usually steel through the
  insulation.

Report each break. Do not quantify: that is a hand-off.

### Step 4. Check movement, then check the tested system against the drawn one

**Movement.** Where does the system take dead load, live load deflection of the
slab, thermal movement, and building drift? Name the component that takes each.
A stack joint that accommodates one of the four is a stack joint that fails on
the others.

**Tested against drawn.** Compare the tested specimen with the submitted
configuration and report each difference: module size, glass makeup, corner
condition, anchor type, air seal detail, framing depth. Then say whether the
package explains why each difference does not invalidate the test. It usually
does not explain, and that is a legitimate comment.

### Step 5. Give every interface an owner

List each assembly this facade meets and, for each, whether the package shows
it, whether it shows it consistently with the other trade's package, and who is
responsible for the joint:

- Slab edge and perimeter fire safing.
- Roof and parapet.
- Adjoining wall assemblies of a different type.
- Base of facade and any transition at grade.
- Doors, louvres, vents, and any penetration.
- Interior finishes returning to the frame.

An interface shown on neither package is the one that gets built twice.

### Step 6. Write the comments and report

| # | Comment | Where | Clause or drawing | System-level or local |
|---|---|---|---|---|

Report the counts, system-level comments first. Then:

- What the package does not contain that the specification requires.
- Every difference between the tested and drawn systems, restated.
- Every interface with no owner.
- What has to be resolved before fabrication starts, separated from what can
  follow.

Close with the standing limits: no engineering was performed, no test report was
validated, and this is comment rather than approval.

### Step 7. Save, if asked

Ask whether to write the comments to a file and where, and write it directly.

## Rules

- **Never supply a performance criterion or a tolerance.** They come from the
  specification, quoted.
- Trace drainage and the thermal break as continuous lines, never section by
  section.
- Report the tested-versus-drawn differences even when they look minor. The
  package should explain them; that it does not is the comment.
- Every interface gets an owner named or gets flagged as having none.
- Sort comments into system-level and local, and report system-level first.
- Never write approved, rejected, or take exception. Those are the Architect of
  Record's words.
- Say on every run that no engineering was performed.

## Anti-patterns

- Reviewing the sections one at a time and never asking whether the drainage
  path closes.
- Accepting a pressure-equalisation claim without asking where the compartments
  are bounded.
- Treating the thermal break as continuous because it is continuous in the
  typical section.
- Recalling an air or water performance class because it is the usual one for
  this building type.
- Letting a hybrid system be reviewed as a proprietary tested one.
- Assuming an interface is the other trade's because it is not drawn here.
- Quoting a specification clause from memory.
- Sizing a mullion or checking a deflection. That is the facade engineer's.

## Resources

None. This skill is one file. Output is written directly at the path you choose.
