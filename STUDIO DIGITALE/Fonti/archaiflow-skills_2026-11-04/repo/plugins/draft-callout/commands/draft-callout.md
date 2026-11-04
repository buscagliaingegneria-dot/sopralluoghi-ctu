---
title: Draft Callout
summary: Write the text inside a drawing callout
discipline: construction-admin
tags: ["Design", "Document Generation"]
description: Draft drawing-callout text — the words inside or next to a callout bubble — following US National CAD Standard (NCS) conventions. Produces text only, not the bubble graphic (drafting work in Revit / AutoCAD). Use /draft-spec-snippet for spec language; use /explain-drawing for interpreting an existing callout.
argument-hint: <what-is-being-called-out>
---

# Draft Callout

Draft the language for drawing callouts — detail bubbles, section markers, room names, equipment tags, plan notes — following US National CAD Standard (NCS) and Uniform Drawing System (UDS) conventions. Output is several short text snippets the user pastes into Revit annotation, AutoCAD MTEXT, or a sketch (SK-##).

This command writes the **text**, not the **graphic**. Bubble shapes, leader styles, sheet placement, and CAD-layer assignment belong in the project's CAD/BIM standard.

## Input you need

Before drafting, gather:

1. **Callout target** — what is being identified:
   - Detail (cross-reference to detail # on another sheet)
   - Section (cross-reference to a building / wall section)
   - Spec (cross-reference to CSI section #)
   - Equipment (tag for a piece of equipment — `AHU-1`, `CU-3`)
   - Room name + room number
   - Plan note (general or keyed)
   - Material (rainscreen panel, finish, paving)
2. **Destination** — where the callout points (e.g., `Detail 3 / A-501`, `Section A-A / A-201`, `09 30 13`).
3. **Modifier** — optional NCS abbreviations: `TYP` (typical), `SIM` (similar), `OPP` (opposite hand), `AB` (above), `BL` (below), `UNO` (unless noted otherwise), `EQ` (equal), `NIC` (not in contract), `FOC` (face of concrete), `FOM` (face of masonry), `FOS` (face of stud), `FOF` (face of finish).
4. **Phase** — `SD` / `DD` / `CD` / `Permit` / `Bid` (drives terseness — CD callouts are tightest).
5. **Context** — 1-line description of what the user is calling out (e.g., "a typical bathroom slab depression at L3 — repeats at all 24 bathrooms"). Used to choose modifiers.

If any of the above is missing or ambiguous, ask the user before drafting. Do not invent sheet numbers, detail numbers, or CSI section numbers.

## Output template

```markdown
# Callout Drafts — [Target type, e.g., "Typical bathroom slab depression"]

**Phase:** [SD / DD / CD]
**Context:** [1-line]

---

## Option 1 — [terse / typical / preferred]

**Callout text:**
> SLAB DEPRESSION
> SEE 3/A-501 TYP

**Use case:** Pointing from a plan to the detail on A-501. The detail repeats at all 24 bathrooms.
**Modifier reasoning:** `TYP` because the condition is identical at all 24 occurrences. If field conditions vary (slab thickness changes by floor), drop `TYP` and tag each occurrence individually.

---

## Option 2 — [with similar-condition modifier]

**Callout text:**
> SLAB DEPRESSION
> SEE 3/A-501 SIM

**Use case:** Most bathrooms match Detail 3 / A-501; a few have minor variation (different fixture layout, but same depression).
**Modifier reasoning:** `SIM` (similar) signals contractor to follow Detail 3 / A-501 with minor field-condition adaptation. Use `SIM` instead of `TYP` when the detail is the same but the surrounding context varies.

---

## Option 3 — [opposite-hand]

**Callout text:**
> SLAB DEPRESSION
> SEE 3/A-501 OPP

**Use case:** This bathroom is mirrored relative to the typical layout shown in Detail 3 / A-501.
**Modifier reasoning:** `OPP` (opposite hand) tells the contractor the geometry is mirrored. Common at stacked bathroom columns where odd / even floors mirror.

---

## Cross-references this callout assumes

- Detail 3 / A-501 must exist and be coordinated with this callout.
- Spec section [CSI #] (if material-specific) must reference the same product.
- Schedule (Door / Finish / Window) entry, if applicable.
```

## Workflow

1. Echo back: target type, destination, phase, modifier candidates. One line.
2. If any required input is missing, list the gap and stop.
3. Produce 2–4 callout options spanning the relevant modifier set (`TYP` / `SIM` / `OPP` / no modifier). Do not auto-add `TYP UNO` if the user did not ask — over-modifying is the most common defect.
4. For each option, list the use case (when to apply) and the modifier reasoning (why this modifier vs another).
5. List the cross-references the callout assumes (detail must exist, spec must coordinate, schedule must align). The user owns coordinating these.
6. If the user wants verbatim NCS-6 / UDS-04 language for a specific abbreviation, ask them to consult their NCS reference (https://www.nationalcadstandard.org/) — do **not** quote NCS section numbers or text from training unless the user pastes.

## NA AEC conventions

- **English only.** No Hangul.
- **Imperial-first** units (`ft`, `in`, `sf`); metric in parens only when useful.
- **All-caps** for callout text (NCS convention). Lowercase use-case / reasoning lines.
- **Sheet number format** — `[Detail #] / [Sheet #]` (e.g., `3 / A-501`). Slash form, not period.
- **Spec reference format** — six-digit CSI MasterFormat 2020 (e.g., `09 30 13`, not `093013` or `9-30-13`).
- **Equipment tag format** — match the project's equipment schedule (`AHU-1`, `CU-3`, `P-12`). Do not invent tag conventions.
- **Room number format** — match the project's room schedule (`312`, `L3-12`, `B1-04`). Do not invent.
- **Floor labels** — `Level 3`, `L3`, or `3rd floor`. Never `3F`.
- **NCS reference** — `US National CAD Standard v6` (NCS-6) for abbreviations and bubble conventions; **do not** quote NCS section numbers from training.

## Constraints

- Output is **callout text only** — not bubble graphics, not sheet placement, not CAD-layer assignment.
- Do not invent CSI section numbers or detail numbers. The user provides destinations.
- Do not auto-add `UNO` (unless noted otherwise) unless the user asked. `UNO` shifts liability — use sparingly.
- Do not mix modifiers (`TYP SIM` is not standard; choose one).
- Do not quote NCS-6 or UDS-04 verbatim from training. If the user wants NCS section text, they paste from their reference.
- Phase matters: SD callouts can be longer ("approx.", "future"), CD callouts are terse and definitive.

## Anti-patterns

- Adding `TYPICAL UNLESS NOTED OTHERWISE` to every callout. `UNO` is a liability shift — use only where the project standard requires it.
- Stacking modifiers (`TYP SIM`, `SIM OPP UNO`). Choose one.
- Inventing detail numbers (`3 / A-501`) without user confirmation that A-501 exists.
- Inventing NCS abbreviations not in NCS-6 (`TYPCL`, `OPPHND`). Use the canonical set or write the word.
- Quoting NCS-6 / UDS-04 section numbers from training (`per NCS-6 §UDS-04 §3.2.4`). Confirm against the user's NCS copy.
- Drafting bubble graphics or sheet-placement instructions. Out of scope.
- Mixing case (`Slab Depression / SEE 3/A-501 TYP`). Callouts are all-caps per NCS.
- Using `3F` instead of `Level 3`.
