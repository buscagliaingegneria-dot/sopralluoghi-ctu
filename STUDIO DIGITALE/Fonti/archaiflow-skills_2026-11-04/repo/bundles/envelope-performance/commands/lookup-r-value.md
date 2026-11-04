---
title: Lookup R-value
summary: Look up an assembly R-value or U-factor
discipline: envelope-performance
tags: ["Compliance"]
description: Look up an assembly R-value or U-factor — user picks Standard (DOE Building America Solution Center) or Own Source (manufacturer spec sheet, ASHRAE 90.1 App.A paste, indexed PDF); verbatim quote + SourceURL. Carries no R-values internally.
argument-hint: <assembly-description> [climate-zone]
---

# Lookup R-value

Retrieve an assembly R-value or U-factor — wall / roof / floor / slab / fenestration — from a source the **user authorizes**. No internal envelope values; every output row cites a verbatim quote with a SourceURL.

For PASS / FAIL math against `IECC` prescriptive tables, use `/test-energy` or `/test-glazing`. For interpretation use `/explain-u-value`.

## Inputs the command needs

1. **Assembly type** — name one:
   - Wall — `mass`, `metal-framed`, `wood-framed`, `framed + continuous insulation (CI)`
   - Roof — `insulation entirely above deck`, `metal building`, `attic and other`
   - Floor — `mass`, `steel-joist`, `wood-framed`
   - Slab on grade — perimeter R-value and depth (`F-factor`)
   - Below-grade wall — CI rating and depth
   - Fenestration — U-factor / SHGC / VT (NFRC-rated whole-window, not center-of-glass)
2. **Climate zone (CZ)** — `1A`, `2A`, `2B`, `3A`–`3C`, `4A`–`4C`, `5A`–`5C`, `6A`–`6B`, `7`, `8`. Optional but narrows the search.
3. **Specifics** — framing factor (e.g., `2x6 @ 16 in o.c.`), insulation type (`R-21 mineral wool batt`, `R-7.5 polyiso CI`), framing material (`steel`, `wood`).

## Step 1 — Source preference (always ask first)

Tell the user, all at once:

> "Where should I retrieve the R-value / U-factor from?
> (a) **Standard** — `https://basc.pnnl.gov/` (DOE Building America Solution Center, free) for whole-assembly performance and best-practice details. I will WebFetch on confirmation and quote the verbatim assembly summary.
> (b) **Your own source** — paste from `ASHRAE 90.1-2022 App. A` (per-assembly U-factor calculations), a manufacturer spec sheet (`Owens Corning`, `Knauf`, `Rockwool`, `Dow`, `Henry`), a locally indexed envelope PDF, or a project basis-of-design.
> (c) **Both** — fetch DOE Building America AND check your source; report any mismatch.
>
> Pick (a), (b), or (c)."

The command does not proceed without an explicit pick.

## Step 2 — Acquire source

- **(a) Standard fetch** — WebFetch `https://basc.pnnl.gov/` with the user's keywords (assembly + CZ + framing). Quote the verbatim assembly summary including R-value, U-factor, framing factor, and any notes on thermal bridging. Record fetched URL and ISO timestamp.
- **(b) Own source** — accept paste or WebFetch a user-provided URL on confirmation. Quote verbatim and record source.
- **(c) Both** — execute (a) and (b); present both quotes; flag any divergence.

If DOE Building America has no entry for the queried assembly + CZ, fall back to: WebSearch `<assembly> <CZ> R-value site:basc.pnnl.gov OR site:nrel.gov OR site:energy.gov` → ask user to confirm match → ask user to paste from `ASHRAE 90.1 App. A` or a manufacturer spec.

## Step 3 — Output

```markdown
# Lookup R-value — [Assembly, CZ]

**Assembly:** [2x6 wood-framed wall + R-5 CI / Roof insulation entirely above deck / Slab perimeter]
**Climate zone:** [4A — NYC / 3B — LA / unspecified]
**Specifics:** [framing, insulation type, layers]
**Source preference:** [(a) DOE Building America / (b) own source — name / (c) both]

## Reference area
DOE Building America Solution Center (`https://basc.pnnl.gov/`); `ASHRAE 90.1-2022 App. A` (assembly U-factor calculations); manufacturer spec sheets for product-specific values; `IECC 2024` for prescriptive minimums (use `/test-energy` for PASS / FAIL).

## Source quote
> [Verbatim assembly summary — layer-by-layer description, total R-value, U-factor, framing factor, thermal bridging notes.]

(Source: WebFetched from `https://basc.pnnl.gov/...` on <YYYY-MM-DD> / pasted by user from <doc>)

## Assembly summary table
| Field | Value (per quoted source) |
|---|---|
| Assembly type | "<verbatim>" |
| Total R-value (effective) | "<verbatim>" |
| Total U-factor | "<verbatim>" |
| Framing factor applied | "<verbatim, e.g., 23% for 2x6 @ 16 in o.c.>" |
| Layers (verbatim) | "<...>" |
| Climate zone applicability | "<verbatim, if stated>" |
| Source date | "<...>" |

## Divergence (if (c))
- [Bullet — any R / U / framing-factor difference between DOE Building America and own source.]

## Caveats
- This is a retrieval, not a compliance check. The MEP Engineer / Architect of Record select and stamp the assembly; this command does not verify against `IECC 2024` minimums (use `/test-energy`).
- Effective R-value depends on framing factor and thermal bridging through fasteners. Cavity-only R-value overstates assembly performance — use the source's framing-factor-aware value.
- Manufacturer spec sheets list center-of-cavity R-values that ignore framing — verify the quoted value is whole-assembly.
- For fenestration U-factor / SHGC / VT, NFRC whole-window ratings only; center-of-glass values are not equivalent.
- Binding interpretation is the AOR / MEP Engineer stamp plus AHJ review (`NYC DOB`, `LADBS`, `DSA`, `CA HCAI`, `Toronto Building`).
```

## NA AEC conventions (enforce)

- English only.
- R-values lead, U-factors second. Imperial-first throughout. Never lead with `W/m²K`.
- Climate zones: `ASHRAE 169` / `IECC 2024 Ch. 3` — `1A` … `8`.
- Codes / sources: `IECC 2024`, `ASHRAE 90.1-2022`, `ASHRAE 90.2-2018`, `DOE Building America`, `NFRC`, `NBC 2020 Sec. 9.36`, `OBC SB-10`, `CA Title 24 Part 6`. Reject `KBC`, `KS`, `EN`, `BS`, `JIS`, `DIN`.
- AHJs named: `NYC DOB`, `LADBS`, `DSA`, `CA HCAI`, `Toronto Building`, `Boston ISD`, `Chicago DOB`. Never `the AHJ` or `the city`.
- Floors: Level 3 / L3 / 3rd floor. Never `3F`.
- Roles: Architect of Record (AOR), MEP Engineer, Energy Modeler, Commissioning Authority (CxA). Never `Director` as a project role.

## Constraints

- Never invent R-values or U-factors from recall.
- Never paraphrase the source summary — verbatim only.
- Always ask the source-preference question at Step 1; do not skip.
- Never WebFetch from manufacturer marketing pages without explicit user authorization — DOE Building America or user-named source only.
- Always include the SourceURL + timestamp.
- Always flag the framing-factor caveat when the user provides cavity-only R-value.
- Caveat block always present.
- Markdown only. No Word / PDF.

## Anti-patterns (never do)

- Stating "R-30 batts + R-5 CI = R-25 effective" from recall — never. The effective value comes from `ASHRAE 90.1 App. A`, DOE BA, or manufacturer assembly testing.
- Adding cavity R + CI R linearly — non-additive due to framing factor.
- Treating center-of-glass U-factor as NFRC whole-window.
- Auto-fetching without explicit user authorization.
- Skipping Step 1 (source preference question) — never.
- Running `/test-energy` from inside this command — pointer-only.
