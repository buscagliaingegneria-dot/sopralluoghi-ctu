---
title: Test Ramp
summary: Check a ramp's slope, landings, and handrails
discipline: code-life-safety
tags: ["Compliance"]
description: Single-ramp gut-check (slope / cross-slope / rise per run / landing / handrail / edge protection) against 2010 ADA §405 and IBC §1012 — user pastes or authorizes fetch of operative § text; PASS / FAIL / MARGINAL with explicit attribution. Carries no values internally.
argument-hint: <provided-dims> [jurisdiction]
---

# Test Ramp

Single-ramp run gut-check — running slope, cross slope, rise per run, landing dimensions, handrail height + extensions, edge protection — against `2010 ADA §405` (accessibility) and `IBC §1012` (general code) text the **user supplies**.

**This command does not carry values.** Every limit cited in the output is a verbatim quote from text the user pasted, or text the command fetched from an explicitly-named official URL with the user's authorization.

For multi-ramp egress scoping, use the `design-egress` skill; for project-wide accessibility scoping, use the `ada-tracker` skill. For aisle ramps in assembly, the rules differ — see `IBC §1029.13`. For ADA single-space clearance use `/test-ada`.

## Inputs the command needs

1. **Ramp use** — egress ramp / accessible route / aisle ramp (assembly) / loading-dock approach. Different rules apply.
2. **Provided dimensions** — labeled:
   - Running slope (`1:X` or `%`)
   - Cross slope (`1:X` or `%`)
   - Total rise per run (`in`)
   - Run length between landings (`ft`)
   - Landing length and width (`ft` × `ft`, with intermediate landings)
   - Clear width between handrails / between rails-and-walls (`in`)
   - Handrail top height above ramp surface (`in`)
   - Handrail extension at top and bottom (`in`)
   - Edge protection (`curb` `4 in` / `barrier` / `extended floor surface`)
3. **Project type** — commercial (`2010 ADA` applies), residential (FHA design — separate framework), state-funded CA (`CA Title 24 Part 2 Ch. 11B-405` is stricter on some clauses), federal (`ABAAS`).
4. **Jurisdiction** — name AHJ + governing instrument:
   - NYC DOB (NYC BC Ch. 11)
   - LADBS
   - DSA (CA K-12)
   - CA HCAI (CA hospitals)
   - Toronto Building (`OBC 2024 Sec. 3.8`)
5. **Source for the operative § text** — paste / fetch / local index:
   - Paste verbatim `2010 ADA §405` and `IBC §1012` paragraphs, including header.
   - Fetch from `https://www.ada.gov/law-and-regs/design-standards/2010-stds/` (federal ADA, free).
   - Fetch IBC § from AHJ amendment page where free.
   - a local RAG index if the standards are indexed locally.

The command refuses to compute against recalled slope / dimension values.

## Workflow

1. Echo parsed inputs: ramp use / provided dims / project type / jurisdiction.
2. Identify reference areas: `2010 ADA §405 — Ramps` and `IBC Ch. 10 §1012 — Ramps`. Do not claim specific clause numbers from recall.
3. Acquire source text — both ADA and IBC if both apply; CA / MA / NY projects may require the state overlay text additionally.
4. For overlay jurisdictions, require overlay text or stop.
5. Math against verbatim sources — each provided dimension gets a row, citing whichever standard is more restrictive.
6. Output table + attribution + caveats.

## Output template

```markdown
# Test Ramp — [Ramp use, plain title]

**Ramp use:** [Egress ramp / accessible route / aisle ramp / loading-dock approach]
**Provided:** [labeled dims]
**Project type:** [commercial — 2010 ADA / CA — Title 24 Part 2 Ch. 11B / federal — ABAAS]
**Jurisdiction:** [NYC DOB / LADBS / DSA / CA HCAI / Toronto Building]

## Reference area
- ADA: `2010 ADA §405 — Ramps`.
- IBC: `IBC Ch. 10 §1012 — Ramps`.
- Aisle ramps in assembly: `IBC §1029.13`.

## Source text under test
> [Verbatim quote of `2010 ADA §405` paragraphs.]

(Source: pasted by user / fetched from `https://www.ada.gov/law-and-regs/design-standards/2010-stds/` on <YYYY-MM-DD>)

> [Verbatim quote of `IBC §1012` paragraphs.]

(Source: pasted by user / fetched from <URL> on <YYYY-MM-DD>)

## Comparison
| Dim | Provided | Required (per quoted source) | Verdict | Margin |
|---|---|---|---|---|
| Running slope | ... | "<verbatim limit, ADA + IBC>" | PASS / FAIL / MARGINAL | ... |
| Cross slope | ... | ... | ... | ... |
| Rise per run | ... | ... | ... | ... |
| Landing dims | ... | ... | ... | ... |
| Clear width | ... | ... | ... | ... |
| Handrail height | ... | ... | ... | ... |
| Handrail extension | ... | ... | ... | ... |
| Edge protection | ... | ... | ... | ... |

## Jurisdictional flags
- [If overlay in scope and overlay source provided: include overlay rows.]
- [If overlay in scope but overlay source missing: list the overlay text the user must paste / fetch (`CA 11B-405`, `MA AAB`).]
- [Aisle ramps in assembly use different slope limits — flag if `IBC §1029.13` applies.]

## Caveats
- Single-ramp gut-check; not a stamped accessibility / life-safety analysis.
- Both ADA and IBC apply on most commercial projects — the more restrictive value governs each dimension. CA Title 24 11B can override both.
- All limit values come from the source the user pasted or the URLs fetched on <date>. The command did not recall any value from training.
- Existing-building `Title III safe harbor` and `2010 ADA §202` alterations rules can change the answer for retrofits.
- Binding interpretation is the AOR's stamped accessibility / egress plan plus AHJ review.
```

## NA AEC conventions (enforce)

- English only.
- Imperial-first: `in`, `ft`, `1:X` slope, `%` slope. Metric only if the source uses it.
- Slope conventions per source — `1:12`, `1:48`, `%`. Do not convert to degrees.
- Codes / standards: `2010 ADA Standards`, `ANSI A117.1-2017`, `CA Title 24 Part 2 Ch. 11B`, `MA AAB 521 CMR`, `IBC`, `IRC`, `OBC 2024 Sec. 3.8`. Reject `KBC`, `KS`, `EN`, `BS`, `JIS`, `DIN`.
- AHJs named: NYC DOB, FDNY, LADBS, DSA, CA HCAI, Toronto Building, Boston ISD. Never `the AHJ` or `the city`.
- Floors: Level 3 / L3 / 3rd floor. Never `3F`.
- Roles: Architect of Record (AOR), Accessibility Consultant, CASp (CA), Civil Engineer (for site ramps). Never `Director` as a project role.

## Constraints

- Never invent ramp limit values from recall.
- Never paraphrase `§405` / `§1012` — verbatim only.
- Never claim a specific clause number (`§405.2.1`, `§1012.3`) from recall.
- Both ADA and IBC apply on most commercial — the more restrictive governs. CA / MA / NY overlay can override.
- Distinguish egress ramp / accessible route / aisle ramp / dock approach — different §.
- Single ramp, single shot. Multi-ramp scoping → `design-egress` / `ada-tracker`.
- No `docs/` artifact, no Word / PDF, no `aec-doc-gen`.
- Caveat block always present.
- Fetch only after explicit user authorization.

## Anti-patterns (never do)

- Stating slope / rise / landing limits inline ("max 1:12 slope, 30 in max rise per run") — never. Numbers live only in the quoted source.
- Claiming `§405.2` from recall — never.
- Treating ADA-only as sufficient on a commercial project — IBC `§1012` also applies.
- Treating CA / MA projects as federal-ADA-only — state overlay required.
- Converting `1:12` to `~8.3%` or `~5°` when the source uses `1:X` — quote as-is.
- Auto-fetching without explicit authorization.
- Hedging — verdicts are PASS / FAIL / MARGINAL.
- Running `design-egress` or `ada-tracker` from inside this command — pointer-only.
