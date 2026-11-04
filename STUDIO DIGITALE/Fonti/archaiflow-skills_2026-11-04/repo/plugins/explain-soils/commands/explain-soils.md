---
title: Explain Soils
summary: Explain a geotechnical recommendation in plain English
discipline: code-life-safety
tags: ["Compliance", "Design"]
description: Interpret a geotechnical recommendation (bearing capacity, lateral pressure, frost depth, site class) in plain English with ASCE 7-22 / IBC 2024 Ch. 18 citation
argument-hint: <geotech-paste>
---

# Explain Soils

Interpret a geotechnical engineering report excerpt — bearing capacity, lateral earth pressure, frost depth, site class, liquefaction potential, settlement — in plain English with ASCE 7-22 / IBC 2024 Ch. 18 citation. Output is an inline interpretation. For full geotech-to-foundation mapping or seismic site response, engage the Engineer of Record.

## Input you need

Before interpreting, gather:

- **Geotech report excerpt** — verbatim paste of the recommendation. Required fields per question:
  - **Bearing capacity** — `psf` allowable, depth and width assumptions, factor of safety (typically 3.0 for shallow foundations).
  - **Lateral earth pressure** — active / at-rest / passive coefficient, surcharge (`psf`), water table elevation.
  - **Frost depth** — local frost line in `in`. Examples: `NYC ~42 in`, `Chicago ~42 in`, `Toronto ~48 in`, `Houston ~6 in`, `Boston ~48 in`, `Minneapolis ~60 in`.
  - **Site class** — `ASCE 7-22 Ch. 20`: `A` (hard rock), `B` (rock), `C` (very dense soil / soft rock), `D` (stiff soil), `E` (soft clay), `F` (special study). Most NA sites are `C`, `D`, or `E`.
  - **Seismic design parameters** — `Sds`, `Sd1`, `Risk Category` (per IBC 2024 §1604.5), `Seismic Design Category (SDC)` per ASCE 7-22 §11.6.
  - **Liquefaction / collapsible / expansive soils** — flag presence and recommendation.
  - **Settlement** — total and differential `in`.
- **Project context** — occupancy group (per IBC 2024 §1604.5), `Risk Category I`–`IV`, foundation type proposed (`spread footing`, `mat`, `drilled pier`, `driven pile`, `micropile`, `helical pile`), basement / no basement, building height, bay sizes (`ft`).
- **Site location** — specific city + climate / seismic context: `Portland OR (CZ 4C, SDC D)`, `Toronto ON (frost 48 in)`, `Houston TX (CZ 2A, expansive clay)`, `Bay Area CA (high SDC, liquefaction risk)`, `Minneapolis MN (frost 60 in, CZ 6A)`.
- **AHJ** — `NYC DOB` (NYC BC Ch. 18 modifies IBC), `LADBS`, `DSA` (CA K-12 schools), `CA HCAI` (CA hospitals), `Toronto Building`, `Boston ISD`, `Chicago DOB`. Geotech recommendations are AHJ-reviewable on most public projects.
- **Specific question** — Examples: "Is 3,000 psf bearing enough for `B` occupancy spread footings at 24-ft bays?", "Site Class D vs C — what changes for a 4-story?", "Frost depth 48 in — does the basement wall avoid frost protection?"

If the geotech excerpt is missing or paraphrased, ask for paste. Do not invent allowable bearing values, lateral coefficients, or seismic parameters.

## Output structure

```markdown
# Explain Soils — [Recommendation, short title]

**Project:** [name, Portland OR / Toronto ON / Houston TX]
**Risk Category:** [I / II / III / IV per IBC 2024 §1604.5]
**Foundation type:** [Spread footing / Mat / Drilled pier / Driven pile / Helical]
**Site Class:** [C / D / E per ASCE 7-22 Ch. 20]
**SDC:** [B / C / D / E per ASCE 7-22 §11.6]
**Question:** [the user's specific question]

---

## What the geotech says (literal)

> [Verbatim quote of the bearing / lateral / frost / site class recommendation.]

(Geotech Report by [GEOR firm], dated [Month DD, YYYY], §[X.Y])

## Plain-English meaning

[3–5 sentences. What the recommendation requires of the foundation design. Translate `psf`, `pcf`, `Ka`, `Kp`, `Sds`, `SDC` into builder language. Use R-values for any thermal frost-line implication, never metric U-values.]

## How it applies here

- [Bullet — apply to the foundation type. e.g., "3,000 psf allowable + 24-ft bay → spread footings sized at ~7 ft x 7 ft for 150-kip column load. Check punching and one-way shear per `ACI 318-19` Ch. 22."]
- [Bullet — frost protection per `IBC 2024 §1809.5`: minimum embedment at frost depth, or insulated frost-protected shallow foundation.]
- [Bullet — site class flips `ASCE 7-22 §11.4.2` site coefficients (`Fa`, `Fv`); SDC drives detailing per `ASCE 7-22 Ch. 12` and `IBC 2024 §1613`.]

## Cross-references

- [Bullet — `IBC 2024 §1808` (shallow foundations), `§1810` (deep foundations), `§1809.5` (frost protection), `§1806` (presumptive load-bearing values).]
- [Bullet — `ASCE 7-22 Ch. 11` (Seismic Ground Motion), `Ch. 20` (Site Class), `Ch. 12` (Seismic Design Requirements), `Ch. 19` (Soil-Structure Interaction).]
- [Bullet — `ACI 318-19` for concrete foundation design, `AISC 360-22` for steel column-base interface, `AWC NDS-24` for wood post bases.]

## Jurisdictional flags

- **`NYC DOB`** — NYC BC Ch. 18 modifies IBC frost depth and presumptive bearing tables. Verify before relying on `IBC 2024 §1806.2` presumptive values; on NYC projects, use the executed geotech report.
- **`DSA`** — K-12 schools require enhanced QA per `DSA IR 17-12`; the geotech must be DSA-reviewed and the foundation design must comply with `California Building Code (CBC)`.
- **`CA HCAI`** — hospital projects require seismic ground-motion peer review under post-OSHPD rules; coordinate the GEOR + EOR + CA HCAI reviewer early.
- **`Toronto Building`** — `OBC 2024` Part 4 references `NBC 2020` with provincial overlays; deep frost depth (48 in) drives perimeter footing or grade-beam detailing.
- If no jurisdiction-specific amendment is known, state explicitly. Do not guess.

## Caveats

- This is an interpretation aid. The Engineer of Record's stamped foundation design governs, not this command. Geotech recommendations are inputs to the EOR; this command does not size foundations.
- Do not extrapolate bearing capacity beyond the recommended depth, width, or load type — geotech values are condition-specific.
- For liquefaction, collapsible soils, expansive clay, or shallow water table, escalate to the EOR — these often require special design (mat, drilled pier, soil improvement, or compaction grouting).
- For multiple-recommendation review or a foundation peer review, engage the GEOR / EOR or use the `foundation-design` skill (when shipped).
```

## NA AEC conventions (enforce)

- **English only.** No Hangul anywhere.
- **Imperial-first** units (`psf` bearing, `pcf` density, `in` frost depth, `kip` column load, `ft` footing dimension, `°F` temperature, `mph` wind). Metric in parens only when useful (`3,000 psf (143.6 kPa)`). Use **R-values** for any thermal context, never metric U-values.
- **Codes cited** — `IBC 2024 Ch. 16 / 17 / 18 / 19`, `IRC 2024 R401–R408`, `ASCE 7-22`, `ASCE 41-23` (existing buildings, seismic), `ACI 318-19`, `AISC 360-22`, `NBC 2020 Part 4` and `Div. B Sec. 9.4` for Canada. Never `KBC`, `KS`, `EN`, `BS`, `JIS`, `DIN` — out of catalog scope.
- **Site classification** — `ASCE 7-22 Ch. 20`: `A` … `F`. Always cite the class letter.
- **SDC** — `ASCE 7-22 §11.6`: `A` (low) through `F` (highest). Always cite.
- **Risk Category** — `IBC 2024 §1604.5`: `I`–`IV`. Always cite.
- **Roles** — `Engineer of Record (EOR)`, `Geotechnical Engineer of Record (GEOR)`, `Architect of Record (AOR)`, `Special Inspector` (per `IBC 2024 Ch. 17`), `Owner's Peer Reviewer` (`CA HCAI`). Never use `Director` as a project role.
- **AHJs** — `NYC DOB`, `LADBS`, `DSA`, `CA HCAI`, `Toronto Building`, `Boston ISD`, `Chicago DOB`. Never `the AHJ`, `the city`, or `local authority` generically.
- **Frost-depth examples** — name region: `NYC 42 in`, `Toronto 48 in`, `Houston 6 in`, `Boston 48 in`, `Minneapolis 60 in`.
- **Floor labels** — `L3`, `Level 3`, `3rd floor`. Never `3F`.

## Constraints

- Do not invent allowable bearing values, lateral coefficients, frost depths, or seismic parameters. Verbatim paste from the geotech report required.
- Distinguish geotech inputs from EOR design output. The geotech says "you may design for X"; the EOR designs and stamps. Never claim a foundation passes design without the EOR.
- Always cite both the IBC chapter and the ASCE 7 chapter where applicable — they govern jointly on most NA projects.
- Coexists with the planned `foundation-design` skill (full sizing) and EOR / GEOR consultation. Redirect for design.
- Markdown only. No Word / PDF output, no `aec-doc-gen` dependency.

## Workflow

1. Echo back: project location, Risk Category, foundation type, Site Class, SDC, question. One line.
2. If geotech excerpt is missing, ask for paste.
3. If AHJ is missing on a question where amendments matter (NYC, CA, Boston, Chicago, Toronto), ask before interpreting.
4. Produce the response in one shot.
5. Surface next-step EOR / GEOR coordination explicitly (e.g., "Liquefaction flagged → coordinate GEOR + EOR + AOR for mat or pile design and special inspection scope").
