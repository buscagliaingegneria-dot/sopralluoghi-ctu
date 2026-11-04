---
title: Explain Vapor Retarder
summary: Explain what a vapor retarder does, and what it is being asked to do here
discipline: envelope-performance
tags: ["Reference"]
description: "Explains vapor control in plain English for a specific assembly rather than in general: what diffusion is and how it differs from air leakage, what the retarder classes mean as a system, which face of the insulation a retarder is being asked to sit on in the assembly you describe, and what that position does to the direction the assembly can dry. Carries no permeance figures and no code requirements — which class your climate zone permits is code text you quote, and which class a product falls into is on its data sheet. For the arithmetic use the `condensation-check` skill; for air leakage rather than diffusion use `air-barrier-trace`; for laying out a new build-up use `design-wall-assembly`."
argument-hint: <assembly-or-question> [climate-zone]
---

# Explain Vapor Retarder

Vapor control is the part of an assembly that gets decided by habit more than
any other, usually as "the plastic goes on the warm side". This explains what
the layer is actually doing, in the assembly you have, so the decision can be
made rather than repeated.

## Scope and limits — read first

**What this does.** Explains diffusion, the retarder class system as a system,
and what a retarder's position does in the specific assembly you describe. Where
you name a climate zone, it says what question that zone raises without
answering it from memory.

**What this does not do.**

- It carries **no permeance figures** and **no class assignments**. Which class a
  product falls into is on the data sheet.
- It carries **no code requirements**. Which class your climate zone permits,
  and under what conditions, is code text. Quote it and the explanation gets
  held against it.
- It does not run the numbers. Whether your assembly actually condenses is
  arithmetic, and `condensation-check` does it.
- **It is not about air leakage.** Air moving through a gap carries far more
  water than diffusion through a layer does. That is a different mechanism, a
  different layer, and `air-barrier-trace` handles it. This command says so
  every run, because conflating the two is the most common misunderstanding in
  the subject.
- It does not tell you what to build.

**What you need before starting.** The assembly, layer by layer, if you want the
explanation to be about your wall rather than about walls. Your climate zone, if
you want the right questions raised. The code text, if you want a verdict.

## Inputs the command needs

1. **The question, or the assembly.** Either works. With an assembly, the
   explanation is specific; without one, it is general and says so.
2. **Climate zone**, and its source, if you have it.
3. **Code text**, quoted, if a verdict is wanted rather than an explanation.

## Workflow

### Step 1 — Establish what is being asked

Separate the three questions that arrive as one:

- What does a vapor retarder do? (mechanism)
- Where should it go in this assembly? (position)
- Which one is allowed here? (code)

Answer them in that order and say plainly that the third is not answered from
memory.

### Step 2 — Explain the mechanism, and separate it from air

Diffusion: water vapor moving through a material because there is more of it on
one side. Slow, steady, and driven by the vapor pressure difference.

Air leakage: air carrying water through a hole. Fast, and usually responsible
for far more moisture than diffusion.

State the separation explicitly. A perfect vapor retarder with a gap around it
is an air leakage path, and the gap wins.

### Step 3 — Explain the class system as a system

Explain that retarders are graded by how much vapor they let through, and that
the grades run from nearly closed to fairly open. Explain what "open" buys you:
the ability to dry in that direction.

**Do not state the numeric boundaries between classes and do not assign a
material to a class.** Say that the boundaries are published in the standard the
user's code references and that products state their own class and permeance.

### Step 4 — Put it in the assembly, if one was given

Walk the layers named and say:

- Which layer is the lowest-perm one, and where it sits relative to the
  insulation.
- Which direction the assembly can therefore dry.
- Whether any layer other than the intended retarder is acting as one. A foil
  facing, a membrane, an impermeable exterior cladding: these often do the job
  by accident.
- Whether there are two low-perm layers with insulation between them, which
  leaves the assembly no direction to dry in.

State these as observations. Whether the arrangement is acceptable depends on
arithmetic and code, neither of which is here.

### Step 5 — Raise the code question without answering it

If a climate zone was given, say what has to be checked: which class is
permitted for that zone and that assembly type, and whether continuous exterior
insulation changes the answer. Name the check; do not perform it from memory.

If code text was pasted, hold the assembly against the quoted text and say which
part of the text applies.

### Step 6 — Close

Every run ends with:

- Air leakage is not diffusion, and it moves more water.
- The arithmetic has not been done here. `condensation-check` does it.
- The class permitted in your zone has not been recalled.

## Rules

- **Never state a permeance figure** or a numeric class boundary.
- **Never assign a product or material to a class.**
- **Never recall what a climate zone requires.**
- Answer mechanism, then position, then code, in that order.
- Separate diffusion from air leakage in every run.
- Quoting a code clause found by web search is not quoting the code. Search
  identifies the document; it does not verify the text.

## Anti-patterns

- "The vapor barrier goes on the warm side." That is one climate's rule of
  thumb stated as physics.
- Naming a class for a common material because it is well known.
- Explaining vapor control without mentioning air leakage.
- Giving a verdict on an assembly when no code text was supplied.
- Treating a low-perm exterior cladding as irrelevant because it is not called a
  vapor retarder.
- Running `condensation-check` from inside this command. It is a pointer.
