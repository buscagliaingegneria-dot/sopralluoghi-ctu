---
name: calculation-reader
description: "Reads any calculation an architect is handed — structural, thermal, egress, drainage, load, acoustic — and checks the part an architect can and should check: the inputs, the assumptions, the standard it was worked to, and the version of the design it was worked from. The arithmetic is sealed by somebody and is not the architect's to verify; the inputs frequently describe a building that has changed since. Trigger on \"read this calculation\", \"they sent calcs\", \"what did the engineer assume here\", \"is this calc still valid\", \"calculation-reader\", or any calculation handed over. Carries no formulas, values or code limits. It verifies no arithmetic, has no engineering opinion, and does not replace the engineer of record or the Architect of Record."
license: MIT
metadata:
  title: "Calculation Reader"
  summary: "Read an engineer's calculation for its inputs, not its arithmetic"
  discipline: "structure-mep"
  tags: "Review, Reference"
---

# Calculation Reader

A calculation arrives, gets filed, and nobody reads it because nobody can check
it. That is the wrong conclusion from a true premise. The arithmetic is sealed
and is not yours. The inputs are not sealed, and they routinely describe a
building that has since moved.

## Scope and limits — read first

**What this does.** Reads the front and the edges of a calculation: what it was
worked to, what it assumed, what design it worked from, and what it concludes.
Then checks those against the project as it is now.

**What this does not do.**

- **It verifies no arithmetic.** Not one line. The calculation is sealed by
  somebody whose job that is, and checking it from an architect's chair is
  useless and unwise.
- **It carries no formulas, values or limits.**
- **It has no engineering opinion.** Where something looks inconsistent, it is
  reported as a question for the engineer, never as an error.
- It does not read a schedule or a cut sheet. `schedule-reader` and
  `equipment-reader` do.
- It does not replace the engineer of record or the Architect of Record.

**What you need before starting.** The calculation, complete, including its
cover, its assumptions and its references. The current design. What it is being
relied on for.

## Workflow

### Step 1. Read the cover, which is most of the value

Before any page of working:

- Who prepared it, who checked it, and is it sealed?
- What date, and what revision?
- **What design does it reference: which drawing, at which revision, on which
  date?** This is the question the whole reading turns on.
- What standard or code edition was it worked to?
- What is its stated scope: which elements, which conditions, which load cases?
- Is it stated as preliminary, for coordination, or for construction?

### Step 2. Check it against the design as it is now

| The calculation assumed | The design now is | Still valid? |
|---|---|---|

Go through the geometry and the conditions it names: spans, heights, areas,
levels, occupancies, spacings, openings, materials, what is above and below.

**A calculation worked from a superseded drawing is the most common finding and
the most consequential.** It is not an error by the engineer; it is a
coordination fact, and it is nobody's job until somebody looks.

Report every place the design has moved since, and say plainly that the
engineer has to confirm whether the result still holds. Never conclude it
yourself either way.

### Step 3. Pull out the assumptions

Calculations state assumptions in prose at the front and then never again:

- What loads, from where, and are they the ones this building has?
- What material properties, and are they what is specified?
- What restraint, support or continuity is assumed at the edges? This is the one
  that most often assumes something the architecture does not provide.
- What is assumed about the construction sequence.
- What is assumed to be provided by others, including by the architect.
- What is explicitly excluded.

For each, ask the only question that matters here: **does the building actually
provide that?**

### Step 4. Read what it concludes, and what that demands of the architecture

The result is rarely just a number:

- What size, thickness, depth, or quantity does it conclude?
- What does that do to the space around it: a deeper beam, a thicker wall, a
  larger shaft, a bigger plant room?
- What does it require of the architecture to be true: a restraint, a
  connection, a diaphragm, a clear route, a stated finish?
- Does it depend on something being built in a particular order?
- Does it hand anything to a delegated designer?

### Step 5. Say what has to happen next

- Where the design has moved: confirm with the engineer, named.
- Where an assumption is not provided by the building: raise it, named.
- Where the conclusion changes the architecture: what has to be drawn.
- Where the calculation is preliminary: what triggers the final one and when it
  is needed.
- Where the standard edition may not be the adopted one: point at `cite-check`.

### Step 6. Report

- The cover facts, with the referenced drawing revision named first.
- Every place the design has moved since, with the confirmation needed.
- Every assumption, with whether the building provides it.
- What the conclusion demands of the architecture.
- Every inconsistency, phrased as a question for the engineer.
- What was not read: the working, which was not checked and is not yours.

Close by saying no arithmetic was verified.

### Step 7. Save, if asked

Ask whether to write the reading to a file and where. Keep it: a calculation
read against a revision is the record of when it was last known to apply.

## Rules

- **Never check the arithmetic.** Not one line.
- **Read the referenced drawing revision first.**
- Compare every stated geometry and condition against the current design.
- Ask, for every assumption, whether the building provides it.
- Report inconsistencies as questions for the engineer, never as errors.
- Never conclude that a result still holds, or that it does not.
- Say what the conclusion demands of the architecture.

## Anti-patterns

- Filing it because it cannot be checked.
- Checking the maths.
- Missing that it was worked from a superseded drawing.
- Accepting an assumed restraint or support the architecture does not provide.
- Reading the answer and not what the answer demands.
- Calling an inconsistency an error.
- Treating a preliminary calculation as final because it was issued.

## Resources

None. This skill is one file. Output is written directly at the path you choose.
