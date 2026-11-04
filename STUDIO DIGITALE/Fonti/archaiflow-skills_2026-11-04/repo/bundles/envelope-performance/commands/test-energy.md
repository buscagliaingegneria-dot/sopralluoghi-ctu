---
title: Test Energy
summary: Check one assembly against the energy table for your zone
discipline: envelope-performance
tags: ["Compliance"]
description: Single-assembly prescriptive energy gut-check (R-value or U-factor vs IECC table by climate zone) — user pastes or authorizes fetch of operative IECC table; PASS / FAIL / MARGINAL with explicit attribution. Carries no IECC values internally.
argument-hint: <assembly-and-r-or-u> <climate-zone> [project-type] [jurisdiction]
---

# Test Energy

Single-assembly prescriptive energy gut-check — proposed R-value or U-factor versus the IECC prescriptive table for the assembly + climate zone — against `IECC` text the **user supplies**.

**This command does not carry IECC values.** Every limit cited in the output is a verbatim quote from text the user pasted, or text the command fetched from an explicitly-named official URL with the user's authorization.

For a multi-assembly envelope sweep, use the `energy-compliance` skill (when shipped; full `COMcheck` / `REScheck` documentation). For interpretation use `/explain-u-value`. For fenestration-specific tests use `/test-glazing`.

## Inputs the command needs

1. **Assembly under test** — name one:
   - Above-grade wall — mass / metal-framed / wood-framed / framed + continuous insulation
   - Roof — insulation entirely above deck / metal building / attic and other
   - Floor — mass / steel-joist / wood-framed
   - Slab on grade (perimeter R-value and depth)
   - Below-grade wall (CI rating and depth)
2. **Proposed value** — `R-value` (preferred for opaque) or `U-factor` (alternative path), with units. Provide both if known. Effective vs nominal — note which.
3. **Climate zone** — `1A`, `2A`, `2B`, `3A`–`3C`, `4A`–`4C`, `5A`–`5C`, `6A`–`6B`, `7`, `8`. Cite the project city if you want the command to confirm CZ via `/climate-zone-mapper` (optional).
4. **Project type** — `commercial` (`IECC Ch. C`) vs `residential` (`IECC Ch. R`). For `R-2` group, low-rise individually metered may default to residential — verify per Ch. 2.
5. **Compliance path** — `prescriptive` (this command's scope) or `performance` / `ECB` (out of scope — flag and route to `energy-compliance`, when shipped).
6. **Jurisdiction** — base IECC always applies. Stricter overlays:
   - `CA Title 24 Part 6` (stricter than IECC on most lines)
   - NYC Energy Conservation Code (NYECCC) + `Local Law 97`
   - DSA (CA K-12)
   - CA HCAI (CA hospitals)
   - OBC SB-10 (Toronto — references `ASHRAE 90.1` with provincial amendments)
   - Boston Stretch Energy Code
7. **Source for the operative table text** — paste / fetch / local index:
   - Paste verbatim row from `IECC Table C402.1.3` (R-value) / `Table C402.1.4` (U-factor) / `Table R402.1.2` / `Table R402.1.3`, including header.
   - Fetch from AHJ amendment / state energy code page.
   - a local RAG index if the IECC PDF is indexed locally.

The command refuses to compute against recalled R / U values.

## Workflow

1. Echo parsed inputs: assembly / proposed R or U / climate zone / project type / path / jurisdiction.
2. Identify reference area: `IECC Ch. C — Commercial Energy Efficiency` or `Ch. R — Residential Energy Efficiency`. Do not claim specific table values from recall.
3. Acquire source text.
4. For overlay jurisdictions (`CA Title 24 Part 6`, `NYECCC`, OBC SB-10), require overlay text or stop.
5. Math against verbatim source.
6. Output the table + attribution + caveats.

## Output template

```markdown
# Test Energy — [Assembly, CZ, plain title]

**Assembly:** [2x6 wood-framed wall + R-5 CI / Roof above-deck / Slab perimeter]
**Proposed:** [R-30 cavity + R-5 CI / U-0.064]
**Climate zone:** [4A — NYC]
**Project type:** [commercial — IECC Ch. C / residential — IECC Ch. R]
**Path:** [prescriptive — this command's scope]
**Jurisdiction:** [base IECC 2024 / + CA Title 24 Part 6 / + NYECCC / + OBC SB-10]

## Reference area
IECC Ch. C — `Table C402.1.3` (R-value alternative) / `Table C402.1.4` (U-factor alternative) / Ch. R — `Table R402.1.2` / `Table R402.1.3`.

## Source text under test
> [Verbatim quote of the table row for the assembly + CZ.]

(Source: pasted by user / fetched from <URL> on <YYYY-MM-DD>)

## Comparison
| Value | Provided | Required (per quoted source) | Verdict | Margin |
|---|---|---|---|---|
| R / U | ... | "<verbatim limit>" | PASS / FAIL / MARGINAL | ... |

## Jurisdictional flags
- [If overlay in scope and overlay source provided: include overlay row.]
- [If overlay in scope but overlay source missing: list the overlay text the user must paste / fetch. Do not math against base IECC alone for CA / NYC / Toronto / Boston.]

## Caveats
- Single-assembly prescriptive gut-check; not a stamped energy compliance report. `COMcheck` / `REScheck` or whole-building energy modeling required for permit.
- Effective R-value depends on framing factor (~23% for 2x6 @ 16 in o.c.) and thermal bridging. Cavity R-value alone overstates assembly performance — verify against the source's tabular convention.
- All limit values come from the source the user pasted or the URL fetched on <date>. The command did not recall any IECC value from training.
- IECC editions and AHJ amendments change. `IECC 2024` differs from `IECC 2021` on multiple fenestration and CI lines.
- Performance path (`IECC §C407` / `§R405`) and `ECB` (`ASHRAE 90.1-2022 §11`) are out of scope for this command — flag to `energy-compliance` (when shipped).
- Binding interpretation is the AOR / MEP Engineer stamp plus AHJ review.
```

## NA AEC conventions (enforce)

- English only.
- R-values lead, U-factors second. Imperial-first throughout. Never lead with `W/m²K` metric U-values.
- Codes: IECC, ASHRAE 90.1, ASHRAE 90.2, NBC Sec. 9.36, OBC SB-10, CA Title 24 Part 6. Reject `KBC`, `KS`, `EN`, `BS`, `JIS`, `DIN`.
- AHJs named: NYC DOB, LADBS, DSA, CA HCAI, Toronto Building, Boston ISD, Chicago DOB. Never `the AHJ` or `the city`.
- Floors: Level 3 / L3 / 3rd floor. Never `3F`.
- Roles: Architect of Record (AOR), MEP Engineer, Energy Modeler, Commissioning Authority (CxA). Never `Director` as a project role.

## Constraints

- Never invent IECC R / U values.
- Never paraphrase `Table C402.1.3` / `R402.1.2` — verbatim only.
- Never claim a specific table number / row from recall.
- Distinguish prescriptive vs performance vs ECB explicitly. This command is prescriptive only.
- Distinguish framing factor vs cavity-only — flag if the proposed is cavity-only and assembly is framed.
- Single assembly, single shot. Multi-assembly → `energy-compliance` (when shipped).
- No `docs/` artifact, no Word / PDF, no `aec-doc-gen`.
- Caveat block always present.
- Fetch only after explicit user authorization.

## Anti-patterns (never do)

- Stating values inline ("R-30 + R-7.5 CI for CZ 4A wall") — never. Numbers live only in the quoted source.
- Claiming `Table C402.1.3` row from recall — never.
- Treating CA / NYC / Toronto / Boston projects as base-IECC only — overlay text required.
- Auto-fetching without explicit authorization.
- Hedging — verdicts are PASS / FAIL / MARGINAL.
- Running `energy-compliance` from inside this command — pointer-only.
- Collapsing cavity R + CI R linearly — non-additive due to framing factor.
