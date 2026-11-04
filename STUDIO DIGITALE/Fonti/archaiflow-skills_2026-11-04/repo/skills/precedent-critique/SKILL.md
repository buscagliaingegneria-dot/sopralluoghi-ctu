---
name: precedent-critique
description: "Critiques the user's scheme through lenses extracted from reference projects the user supplies, instead of a generic rubric. Trigger on \"critique this through these precedents\", \"hold my scheme against these references\", \"critique this like these projects\", \"precedent-critique\", or a scheme shared alongside two or more admired projects. The user supplies both sides: their own scheme (concept text, plans, sections, images) and material for each reference (project descriptions, photographs, drawings, published texts). The skill derives three to five lenses from the supplied material, confirms them with the user, then reads the scheme through each lens. It never characterizes a firm or a project from memory: a name without material stops the run. Divergence from the references is reported and questioned, never scored. It does not design, does not rank, and does not replace the designer's judgment or a design review."
license: MIT
metadata:
  title: "Precedent Critique"
  summary: "Critique your scheme through lenses drawn from precedents you supply"
  discipline: "design-building-types"
  tags: "Design"
---

# Precedent Critique

Take the projects you admire, work out from their own material what they
actually do, and read your scheme through that. The lenses come from what you
hand over, never from a remembered idea of a firm's style.

## Scope and limits — read first

**What this does.** Reads the reference material you supply for two to four
projects, extracts the three to five moves those references share, confirms the
lenses with you, and then critiques your scheme through each one: where it
aligns, where it diverges, and whether the divergence reads as chosen or as
drift.

**What this does not do.**

- **It does not know any reference from memory.** Naming a firm or a project
  without supplying material stops the run. Even when the project is famous,
  the lens comes from the material you handed over, not from a recalled
  caricature of the office's style. That is the design, not a gap.
- It does not treat the references as a standard. Divergence is a finding to
  question, never a deduction. Your scheme is not wrong for being unlike the
  work you admire.
- It does not verify the references. If the text you paste is promotional or
  mistaken, the lens inherits that; the sources are yours to vet.
- It does not design. Like `design-critic`, it points at the next move, not at
  a different project, and it produces no plans, options, or alternatives.
- It does not check code, zoning, cost, or buildability. Those are
  `code-compliance-review`, `zoning-summary`, `value-engineering-advisor`, and
  `constructability-review`.
- It does not replace your design judgment, and it is not a substitute for a
  review with people in the room.

**What you need before starting.** Your scheme in whatever form it exists
(concept text, plans, sections, renderings), and material for each reference:
enough that a stranger could see the moves in it. Descriptions, photographs,
drawings, or published texts all work. A name alone is not material.

## When to use

Use `design-critic` for a general second opinion against its fixed six axes.
Use this skill when you have specific work you want your scheme held next to,
and you can put that work's material on the table.

`precedent-finder` is the natural first step when you have the sensibility but
not the list: it names candidate projects with source links, and you come back
here with the material you gathered from them.

## Workflow

### Step 1. Collect both sides

Ask for anything missing, in one message:

> 1. The scheme: concept text, plans, sections, images, in whatever state it is
>    in, plus the site and program in a sentence each.
> 2. The references: two to four projects, each with material. Paste the text,
>    attach the images, or name the files.
> 3. Optionally, what drew you to these references, in your own words. This is
>    checked against what the material shows, not substituted for it.

If a reference arrives as a name only, say plainly that a name is not material
and ask for some, or point to `precedent-finder` to build the list first. Do
not fill the gap from memory, and do not proceed with the references that have
material while silently dropping the one that does not.

### Step 2. Extract the lenses

Read the reference material and pull out the three to five moves that recur
across it: how the buildings meet the ground, what the section does that the
plan does not, where material restraint sits, what gets spent and what gets
suppressed. Each lens must cite the supplied material that shows it, by
reference name and by the specific passage, drawing, or image. A lens that
cannot point at something in the material is dropped, not kept on conviction.

A move that appears in one reference only is noted as that project's move, not
elevated into a lens. A lens is what the set shares.

### Step 3. Confirm the lenses

Show the lenses before critiquing, each with its citations, and ask two things:
are these the qualities you were after, and which one matters most. You may
strike a lens, add one by pointing at material that shows it, or re-rank. Do
not skip this step; a critique built on a misread of the references is worse
than no critique.

### Step 4. Read the scheme through each lens

For each confirmed lens, one of three findings, and only three:

- **Aligned**, with the place in your scheme where the lens shows up, named
  specifically.
- **Diverges**, with what the scheme does instead, and the question stated
  plainly: is this chosen, or did it drift? A chosen divergence is a position;
  a drifted one is the finding.
- **Not visible in what you shared.** Say what material would settle it. Do not
  guess this state into either of the other two.

### Step 5. Report

Close with the two or three findings worth acting on, each tied to its lens and
to something visible in the work, and the single next study that would move the
scheme most. No scores, no ranking against the references, no verdict on taste.

Then ask whether to save the critique, and where. A sensible default is
`docs/reviews/<YYYY-MM-DD>-precedent-<slug>.md`, written directly, alongside
any `design-critic` reviews already there. There is no template and no script.

## Rules

- **Never characterize a reference from memory.** The material on the table is
  the whole of what the skill knows about the project. If it is not enough,
  say so and ask, rather than quietly topping it up.
- Every lens carries its citations into the output, and every finding names
  both the lens and the place in the scheme it points at. "This feels
  un-reference-like" with no anchor is not a finding.
- Divergence is a question, not a fault. The report asks whether it was chosen;
  it never subtracts points for it.
- Three finding states, no third guessed into the first two. What the shared
  material cannot show is reported as not visible.
- Keep it bounded: three to five lenses, two or three findings worth acting on.
  Ten lenses means the references were read too thin to rank what recurs.

## Anti-patterns

- Running with "critique this like BIG" and no material. That produces a style
  caricature with a real firm's name attached, which is exactly what this skill
  exists to refuse.
- Topping up a thin excerpt with what the model knows about the project. The
  supplied material is the boundary, famous or not.
- Grading the scheme against the references: "they do X, you do not, minus
  one". The references are a way of seeing, not a rubric.
- Elevating one reference's one-off move into a lens for the set.
- Critiquing material the user only alluded to, or inferring the site and
  program instead of asking once.
- Suggesting the scheme become one of the references. The critique points to
  the next move in this project, not to a copy of another.

## Resources

None. This skill is one file. Output is written directly at the path you
choose.
