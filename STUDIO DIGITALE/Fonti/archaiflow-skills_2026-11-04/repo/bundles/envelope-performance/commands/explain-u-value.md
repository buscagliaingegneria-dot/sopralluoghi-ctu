---
title: Explain U-value
summary: Check an assembly's R-value against your climate zone
discipline: envelope-performance
tags: ["Compliance", "Design"]
description: Interpret an envelope assembly R-value or U-factor against IECC 2024 (or ASHRAE 90.1-2022) by climate zone — pass/fail with prescriptive vs performance path
argument-hint: <assembly-and-r-or-u-and-cz>
---

# Explain U-value

Interpret an envelope assembly's R-value or U-factor against `IECC 2024` (or `ASHRAE 90.1-2022`) by climate zone. Output is an inline pass/fail interpretation with prescriptive table reference, performance-path implication, and ASHRAE alternative. For full energy modeling or `COMcheck` / `REScheck` documentation, use the `energy-compliance` skill (when shipped).

## Input you need

Before interpreting, gather:

- **Assembly** — describe the layered build:
  - **Wall** — `mass`, `metal-framed`, `wood-framed`, `framed + continuous insulation (CI)`.
  - **Roof** — `insulation entirely above deck`, `metal building`, `attic and other`.
  - **Floor** — `mass`, `steel-joist`, `wood-framed`.
  - **Slab on grade** — perimeter R-value and depth (`F-factor` per `IECC 2024 Table C402.1.4`).
  - **Below-grade wall** — CI rating and depth.
  - **Fenestration** — U-factor, SHGC, VT, frame type (`vinyl`, `aluminum thermally broken`, `fiberglass`).
- **R-value or U-factor proposed** — provide both if known. R-values lead in NA practice; U-factors only for fenestration and the U-factor alternative path in `IECC 2024 §C402.1.4`.
- **Climate zone (CZ)** — `ASHRAE 169` / `IECC 2024 Ch. 3` designation: `1A`, `2A`, `2B`, `3A`–`3C`, `4A`–`4C`, `5A`–`5C`, `6A`–`6B`, `7`, `8`. Examples: `NYC CZ 4A`, `LA CZ 3B`, `Toronto CZ 6A`, `Houston CZ 2A`, `Phoenix CZ 2B`, `Chicago CZ 5A`, `Minneapolis CZ 6A`, `Miami CZ 1A`.
- **Project type / occupancy** — `commercial` (`IECC 2024 Ch. C`) vs `residential` (`IECC 2024 Ch. R`). For commercial, the R-occupancy distinction matters: `R-2` group counts as commercial under `IECC §C402` unless individually metered low-rise.
- **Path** — `prescriptive` (table compliance), `performance` (whole-building energy modeling per `IECC §C407` or `§R405`), `ECB` (Energy Cost Budget per `ASHRAE 90.1-2022 §11`), or `outcome-based`. Prescriptive is the most common SD/DD gut-check path.
- **AHJ** — `NYC DOB` (NYC Energy Conservation Code + `Local Law 97` carbon overlay), `LADBS` (`CA Title 24 Part 6`), `DSA` (CA K-12), `CA HCAI` (CA hospitals), `Toronto Building` (`OBC SB-10`), `Boston ISD` (`Stretch Energy Code`). `CA Title 24 Part 6` is stricter than IECC on many lines.
- **Specific question** — Examples: "Is `R-30` batts + `R-5 CI` enough for a 2x6 wall in `CZ 4A`?", "Does `U-0.32` fenestration pass for `CZ 5A` commercial?", "What R-value for slab perimeter in `Toronto CZ 6A`?"

If the climate zone is missing, name the project city — pair with `climate-zone-mapper` for authoritative CZ assignment.

## Output structure

```markdown
# Explain U-value — [Assembly, CZ, R-value]

**Assembly:** [2x6 wood-framed wall + R-5 CI / Roof insulation entirely above deck / Vinyl fenestration]
**Proposed:** [R-30 cavity + R-5 CI / U-0.32 / SHGC 0.40]
**Climate zone:** [CZ 4A — NYC]
**Project type:** [commercial — IECC 2024 §C402 / residential — IECC 2024 §R402]
**Path:** [prescriptive / performance / ECB / outcome-based]
**Question:** [the user's specific question]

---

## What IECC 2024 requires (literal)

> [Verbatim values from `IECC 2024 Table C402.1.3` (R-value alternative for above-grade walls), `Table C402.1.4` (U-factor alternative), `Table C402.4` (fenestration), `Table R402.1.2` (residential R-value), `Table R402.1.3` (residential U-factor).]

(IECC 2024 Table C402.1.3, climate zone [X])

## Pass / fail

- **R-value path** — [Compare proposed against `Table C402.1.3` minimum.]
- **U-factor alternative** — [Per `IECC 2024 §C402.1.4`, the assembly may comply via U-factor — compare against `Table C402.1.4`.]
- **Performance path** — [If prescriptive fails, the assembly may pass under whole-building modeling per `IECC 2024 §C407`. Flag without claiming the model passes — modeling is required.]

## ASHRAE 90.1-2022 alternative

- [Bullet — `IECC 2024 §C401.2` permits `ASHRAE 90.1-2022` as an alternative path. Cite the equivalent `ASHRAE 90.1-2022 §5.5` table by CZ for cross-check.]

## Jurisdictional flags

- **`CA Title 24 Part 6`** — stricter than IECC on most lines; confirm via `DSA` / `CA HCAI` / `LADBS` reviewer.
- **`NYC DOB` + `Local Law 97`** — layers carbon-intensity targets on top of envelope compliance; envelope-only gut-checks are insufficient for `Local Law 97` reporting.
- **`Toronto Building` (`OBC SB-10`)** — references `ASHRAE 90.1` with provincial amendments; verify project-specific compliance with `Toronto Building` plan reviewer.
- **`NYC SCA`** — schools layer NYC CECC on top of NYC Energy Code; coordinate with `NYC SCA` design review.
- **`Boston ISD`** — `Stretch Energy Code` raises prescriptive minimums above base IECC.
- If no AHJ-specific amendment is known, state explicitly. Do not guess.

## Cross-references

- [Bullet — `IECC 2024 Table C402.1.3` (R-value), `Table C402.1.4` (U-factor), `Table C402.4` (fenestration), `Table C402.5` (air leakage).]
- [Bullet — `ASHRAE 90.1-2022 §5.5` (CZ-specific envelope criteria), `App. A` (assembly U-factor calculations).]
- [Bullet — `IECC 2024 §C406` (additional efficiency packages — required for commercial in the 2024 cycle).]

## Caveats

- Effective R-value depends on framing factor (~23% for 2x6 @ 16 in o.c.) and thermal bridging through fasteners. Cavity R-value alone overstates assembly performance — use `Tables C402.1.3 / C402.1.4` which build the framing factor in, or compute assembly U-factor per `ASHRAE 90.1-2022 App. A`.
- Prescriptive compliance is a floor, not a ceiling. `NYC Local Law 97`, `CA Title 24 Part 6`, and outcome-based codes (`Boston Stretch Code`, `Vancouver Zero Emissions Building Plan`) often require performance modeling.
- This is a gut-check, not stamped energy compliance. `COMcheck` / `REScheck` or whole-building energy modeling is required for permit submission.
- For full energy compliance documentation, use the `energy-compliance` skill (when shipped).
```

## NA AEC conventions (enforce)

- **English only.** No Hangul anywhere.
- **R-values lead, U-factors second.** Never lead with metric U-values (`W/m²K`). When U-factor is needed (fenestration, U-factor alternative), cite IECC `U-X.XX` form (e.g., `U-0.32`).
- **Climate zones** — `ASHRAE 169` / `IECC 2024 Ch. 3`: `1A` … `8`. Always specify with letter suffix where present.
- **Codes cited** — `IECC 2024` (commercial Ch. C, residential Ch. R), `ASHRAE 90.1-2022`, `ASHRAE 90.2-2018`, `NBC 2020 Div. B Sec. 9.36`, `OBC SB-10`, `CA Title 24 Part 6`. Never `KBC`, `KS`, `EN`, `BS`, `JIS`, `DIN` — out of catalog scope.
- **AHJs** — `NYC DOB`, `LADBS`, `DSA`, `CA HCAI`, `Toronto Building`, `Boston ISD`, `Chicago DOB`. Never `the AHJ`, `the city`, or `local authority` generically.
- **Roles** — `Architect of Record (AOR)`, `MEP Engineer`, `Energy Modeler`, `Commissioning Authority (CxA)`, `LEED AP`. Never use `Director` as a project role.
- **Imperial-first** units; SHGC and VT are dimensionless; framing spacing in `in o.c.`.
- **Floor labels** — `L3`, `Level 3`, `3rd floor`. Never `3F`.

## Constraints

- Do not invent IECC table values from memory. Either cite the verbatim table value (preferred — pull from the IECC PDF if available) or state the prescriptive minimum is to be verified against the table.
- Do not collapse cavity R-value + CI R-value linearly. Use IECC's tabular U-factor alternative or assembly U-factor calculations per `ASHRAE 90.1-2022 App. A` — framing factor matters.
- Distinguish prescriptive vs performance vs ECB paths. A prescriptive fail is not a project fail if performance modeling is in scope.
- Coexists with the planned `energy-compliance` skill (full `COMcheck` / `REScheck` / model). For permit-ready documentation, redirect.
- Markdown only. No Word / PDF output, no `aec-doc-gen` dependency.

## Workflow

1. Echo back: assembly, proposed R / U, climate zone, project type, path, question. One line.
2. If climate zone is missing, infer from city using `climate-zone-mapper` or ask. CA cities default to `Title 24 Part 6` review.
3. If the proposed value is cavity R-value only and the assembly is framed, flag the framing-factor caveat before citing pass/fail.
4. Produce the response in one shot.
5. Surface next-step compliance work explicitly (e.g., "Prescriptive fails by 2 R-values → engage MEP Engineer for performance modeling per `IECC 2024 §C407`, or upgrade to `R-30 + R-7.5 CI` to clear `Table C402.1.3`").
