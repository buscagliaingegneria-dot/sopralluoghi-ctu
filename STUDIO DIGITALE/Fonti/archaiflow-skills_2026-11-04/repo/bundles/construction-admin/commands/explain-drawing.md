---
title: Explain Drawing
summary: Explain a detail, callout, or section in plain English
discipline: construction-admin
tags: ["Construction Admin", "Construction"]
description: Interpret an architectural drawing detail, callout, or section in plain English (NCS sheet citation, NA conventions)
argument-hint: <sheet-number-or-detail-callout>
---

# Explain Drawing

Interpret a specific drawing element — a detail, section, callout, schedule reference, or sheet — in plain English. Output is an inline explanation with NCS-6 sheet/detail citation. For a full drawing-set walk-through, use the `drawing-reader` skill instead.

## Input you need

Before interpreting, gather:

- **Sheet identification** — sheet number (NCS-6 format: `A-301`, `S-201`, `M-401`, `E-501`), sheet title (e.g., `WALL SECTIONS`, `RCP — LEVEL 3`), and discipline (`A` Architectural / `S` Structural / `M` Mechanical / `P` Plumbing / `E` Electrical / `FP` Fire Protection / `C` Civil / `L` Landscape / `T` Telecom).
- **Drawing element** — what specifically the user wants explained:
  - **Detail callout** — `4/A-301`, `Detail 6 / A5.21`, `SIM A-301/4`.
  - **Section cut** — `Section A-A on A-201`, `Building Section 1 on A-401`.
  - **Schedule reference** — `Door Type 12 / A-601`, `Window Type W-04 / A-602`.
  - **Plan callout** — `Room 305 — see RCP A-201`, `keynote 14 on A-101`.
  - **Title block / general notes** — issue revision triangle, code analysis block, sheet index reference.
- **Drawing content** — the user must provide either:
  - A paste of the drawing text / callouts / dimensions / notes the question is about, OR
  - The PDF path so the `drawing-reader` skill or `Read` tool can pull the page.
  - Do not invent dimensions, materials, or callout numbers.
- **Issue / phase** — `IFP` (Issued for Permit) / `IFC` (Issued for Construction) / `IFB` (Issued for Bid) / `100% CD` / `Record Drawings` / `As-Built`. Affects how the response treats binding-vs-informational content.
- **Specific question** — what the user wants to know. Examples: "What does keynote 14 reference?", "Is this a fire-rated assembly?", "What's the slab depression at the bathroom?", "Why is this section cut here?"

If any required input is missing, list the gap and stop. Do not interpret a drawing element without seeing its actual content.

## Output structure

Produce a single Markdown response in this layout:

```markdown
# Explain Drawing — [Sheet # / Element]

**Sheet:** [A-301 — Wall Sections]
**Discipline:** [Architectural / Structural / MEP / Civil / Landscape]
**Element:** [Detail 4/A-301 / Section A-A / Door Type 12 / etc.]
**Issue:** [IFP / IFC / IFB / 100% CD / Record / As-Built]
**Question:** [the user's specific question]

---

## What's drawn (literal description)

[2–4 sentences. The literal content of the element — geometry, materials shown, dimensions, callouts, hatching patterns. Quote callout text verbatim. Cite the specific detail / keynote / dimension as `(per Detail 4/A-301)` or `(keynote 14, A-101)`.]

## Plain-English meaning

[2–4 sentences. What this element communicates to the contractor / owner / consultant. If it's a coordination instruction, say so. If it's a representational convention (poché, hatching, line weight hierarchy), explain.]

## Cross-references

- [Bullet — other sheets / details this element points to. e.g., "Detail 4/A-301 references Spec Section 07 27 26 (air barrier) for membrane material."]
- [Bullet — schedules / specs this element depends on.]
- [Bullet — coordination items: "MEP penetration callout — confirm with M-401 RCP for fire-damper location."]

## NA AEC conventions used

- [Bullet — the NCS / AIA / industry conventions visible in this element. e.g., "SIM = `similar` per NCS-6 Module 02. Read with care; SIM details rarely match 1:1."]
- [Bullet — fire-rating annotation (`1HR`, `2HR`, `UL U419`), if visible.]
- [Bullet — dimension-string convention (face-of-stud / face-of-finish / centerline) if relevant.]

## Caveats

- This interpretation is based **only** on the drawing content the user provided. Cross-references that were not pulled may change the meaning.
- For binding interpretation on an `IFC` set, the AOR's RFI response governs — not this command. Open an RFI via the `rfi-writer` skill if the drawing is ambiguous in the field.
- [Bullet — if `IFP`-only and not yet `IFC`, flag that contractor work cannot proceed off this set.]
- [Bullet — if `As-Built` / `Record`, flag that field conditions may differ from the drawing.]
```

## NA AEC conventions (enforce)

- **English only.** No Hangul anywhere.
- **Imperial-first** units (`ft`, `in`, `sf`, `°F`, `psf`, `plf`); metric in parens only when useful. Do not lead with `mm`, `m²`, `°C`.
- **Sheet numbers** use NCS-6 format: discipline letter + dash + sheet number (`A-301`, `S-201`, `M-401`, `E-501`, `FP-101`, `C-201`, `L-101`, `T-301`). Optional minor number (`A4.1`, `A-301.01`). **Never** "drawing 301" or "sheet 4-3" generically.
- **Detail callouts** use the NCS-6 numerator-over-denominator convention: `4/A-301` = Detail 4 on Sheet A-301. Treat `SIM` (`similar`) as a flag, not a guarantee — call it out per NCS-6 Module 02.
- **Floor labels** — `Level 3`, `L3`, or `3rd floor`. **Never** `3F`.
- **Disciplines** — `A` Architectural / `S` Structural / `M` Mechanical / `P` Plumbing / `E` Electrical / `FP` Fire Protection / `C` Civil / `L` Landscape / `T` Telecom. Use the actual NCS-6 letter, not a generic word.
- **AIA / industry references** — `AIA G701` (Change Order), `AIA A201 §3.7.4` (Contractor's responsibility for field conditions), `AIA B101 §3.6.5` (Architect's response time).
- **AHJs** — name specifically (`NYC DOB`, `LADBS`, `DSA`, `CA HCAI`, `NYC SCA`, `GSA`, `USACE`) when the question involves a code-driven element. **Never** "the city" or "the AHJ" generically.
- **Roles** — `Architect of Record (AOR)`, `Engineer of Record (EOR)`, `Owner`, `Owner's Representative`, `General Contractor (GC)`, `Construction Manager (CM)`. **Never** "Director" as a project role.

## Constraints

- Do not invent dimensions, materials, callout numbers, schedule entries, or keynote text. If the user did not paste the content, route through `drawing-reader` skill or `Read` tool first.
- Do not invent NCS-6 sheet numbers. Cite only what appears in the user's input.
- Distinguish **literal description** (what's drawn) from **interpretation** (what it means). Keep them in separate sections — the literal description is just the drawing content; the interpretation is the architectural intent.
- This command coexists with the `drawing-reader` skill. If the user wants a multi-element walk-through or a sheet-index summary, redirect to `drawing-reader` rather than padding this command's output.
- For schedule-heavy questions (door, window, finish, equipment schedules), suggest the `schedule-extractor` skill — pulling the whole schedule is its job, not this command's.
- Markdown only. This is an inline interpretation, not a transmittal document — no Word / PDF output and no `aec-doc-gen` dependency.

## Workflow

1. Echo back what was parsed: sheet #, discipline, element type, issue, question. One line.
2. If the drawing content is missing, list the gap and stop. Suggest `drawing-reader` skill or `Read` tool as the retrieval path.
3. If the issue / phase is missing on a binding question (IFC vs. IFP changes how to answer), ask before interpreting.
4. Produce the full Markdown response in one shot.
5. After the response, list any cross-referenced sheets / specs / schedules the user should pull next (e.g., "If you want the membrane spec, pull Section 07 27 26 — use `explain-spec`").
