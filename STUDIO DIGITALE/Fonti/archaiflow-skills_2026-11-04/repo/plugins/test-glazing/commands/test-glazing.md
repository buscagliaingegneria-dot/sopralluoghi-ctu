---
title: Test Glazing
summary: Check a window against the energy table for your zone
discipline: envelope-performance
tags: ["Compliance"]
description: Single-window prescriptive glazing gut-check (U-factor / SHGC / VT / window-to-wall ratio) against IECC Table C402.4 by climate zone — user pastes or authorizes fetch of operative IECC table; PASS / FAIL / MARGINAL with explicit attribution. Carries no IECC values internally.
argument-hint: <fenestration-properties> <climate-zone> [project-type] [jurisdiction]
---

# Test Glazing

Single-window / fenestration prescriptive gut-check — U-factor, SHGC, VT, frame type, fixed vs operable, and window-to-wall ratio (WWR) — against `IECC Table C402.4` (commercial) or `Table R402.1.3` (residential) text the **user supplies**.

**This command does not carry IECC values.** Every limit cited in the output is a verbatim quote from text the user pasted, or text the command fetched from an explicitly-named official URL with the user's authorization.

For a multi-window envelope sweep, use the `energy-compliance` skill (when shipped). For interpretation use `/explain-u-value`. For opaque assemblies use `/test-energy`.

## Inputs the command needs

1. **Fenestration type** — name one:
   - Vertical fenestration — fixed
   - Vertical fenestration — operable
   - Skylight
   - Storefront / curtain wall
   - Door — half glazed / fully glazed
2. **Frame type** — `vinyl`, `aluminum thermally broken`, `aluminum without thermal break`, `fiberglass`, `wood`, `wood-clad`. Source tables sometimes split by frame.
3. **Proposed properties** — provide all known:
   - U-factor (`U-0.XX`, NFRC-rated)
   - SHGC (Solar Heat Gain Coefficient, NFRC-rated)
   - VT (Visible Transmittance, NFRC-rated)
   - Window-to-wall ratio (% of gross above-grade wall)
4. **Climate zone** — `1A`, `2A`, `2B`, `3A`–`3C`, `4A`–`4C`, `5A`–`5C`, `6A`–`6B`, `7`, `8`. Confirm via `/climate-zone-mapper` if uncertain.
5. **Project type** — `commercial` (`IECC Ch. C` — `Table C402.4`) vs `residential` (`IECC Ch. R` — `Table R402.1.3`).
6. **Compliance path** — `prescriptive` (this command's scope) or `performance` / `ECB` / `outcome-based` (out of scope — flag and route to `energy-compliance`, when shipped).
7. **Jurisdiction** — base IECC always applies. Stricter overlays:
   - `CA Title 24 Part 6` (substantially stricter on SHGC and U-factor)
   - NYC Energy Conservation Code + `Local Law 97`
   - DSA (CA K-12)
   - CA HCAI (CA hospitals)
   - OBC SB-10 (Toronto)
   - Boston Stretch Energy Code
8. **Source for the operative table text** — paste / fetch / local index:
   - Paste verbatim row from `IECC Table C402.4` or `Table R402.1.3`, including header.
   - Fetch from AHJ amendment / state energy code page.
   - a local RAG index if the IECC PDF is indexed locally.

The command refuses to compute against recalled fenestration values.

## Workflow

1. Echo parsed inputs: fenestration type / frame / proposed properties / climate zone / project type / jurisdiction.
2. Identify reference area: `IECC Ch. C — Table C402.4 — Building Envelope Requirements: Fenestration` or `Ch. R — Table R402.1.3`. Do not claim values from recall.
3. Acquire source text.
4. For overlay jurisdictions (`CA Title 24 Part 6` especially), require overlay text or stop.
5. Math against verbatim source per property (U-factor, SHGC, VT if listed, WWR if applicable).
6. Output the table + attribution + caveats.

## Output template

```markdown
# Test Glazing — [Fenestration, CZ, plain title]

**Fenestration type:** [Vertical fixed / operable / skylight / storefront]
**Frame:** [Vinyl / aluminum thermally broken / fiberglass]
**Proposed:** [U-0.32 / SHGC 0.40 / VT 0.50 / WWR 32%]
**Climate zone:** [4A — NYC]
**Project type:** [commercial — IECC Ch. C / residential — IECC Ch. R]
**Path:** [prescriptive — this command's scope]
**Jurisdiction:** [base IECC 2024 / + CA Title 24 Part 6 / + NYECCC / + OBC SB-10]

## Reference area
IECC Ch. C — `Table C402.4` (commercial fenestration); Ch. R — `Table R402.1.3` (residential fenestration); WWR limits per `IECC §C402.4.1`.

## Source text under test
> [Verbatim quote of the table row for the fenestration type + CZ.]

(Source: pasted by user / fetched from <URL> on <YYYY-MM-DD>)

## Comparison
| Property | Provided | Required (per quoted source) | Verdict | Margin |
|---|---|---|---|---|
| U-factor | ... | "<verbatim limit>" | PASS / FAIL / MARGINAL | ... |
| SHGC | ... | ... | ... | ... |
| WWR | ... | ... | ... | ... |

## Jurisdictional flags
- [If overlay in scope and overlay source provided: include overlay rows.]
- [If overlay in scope but overlay source missing: list the overlay text the user must paste / fetch.]
- [WWR > IECC `§C402.4.1` cap (typ. 30–40%) triggers performance path — flag and route to `energy-compliance` (when shipped).]
- [North-glazing / dynamic-glazing / projection-factor (PF) credits per `IECC §C402.4.3` — flag if claimed.]

## Caveats
- Single-window prescriptive gut-check; not a stamped energy compliance report.
- Use NFRC-rated values only — manufacturer center-of-glass values are not equivalent. Verify the proposed values are whole-window NFRC.
- All limit values come from the source the user pasted or the URL fetched on <date>. The command did not recall any IECC value from training.
- WWR > prescriptive cap requires either modeling or alternative-path qualification. Flag to `energy-compliance` (when shipped).
- `CA Title 24 Part 6` SHGC and U-factor caps are substantially stricter than IECC for CA projects.
- Binding interpretation is the AOR / MEP Engineer stamp plus AHJ review.
```

## NA AEC conventions (enforce)

- English only.
- Imperial-first; SHGC and VT dimensionless; WWR in %. Never lead with `W/m²K`.
- Codes: IECC, ASHRAE 90.1, ASHRAE 90.2, NBC Sec. 9.36, OBC SB-10, CA Title 24 Part 6. Reject `KBC`, `KS`, `EN`, `BS`, `JIS`, `DIN`.
- AHJs named: NYC DOB, LADBS, DSA, CA HCAI, Toronto Building, Boston ISD, Chicago DOB. Never `the AHJ` or `the city`.
- Floors: Level 3 / L3 / 3rd floor. Never `3F`.
- Roles: Architect of Record (AOR), MEP Engineer, Energy Modeler, Curtain-Wall Consultant. Never `Director` as a project role.

## Constraints

- Never invent fenestration values from recall.
- Never paraphrase `Table C402.4` / `R402.1.3` — verbatim only.
- Never claim a specific table number / row from recall.
- Distinguish whole-window NFRC vs center-of-glass — only NFRC counts for compliance.
- Distinguish prescriptive vs performance vs PF-credit paths.
- Single fenestration / system, single shot. Multi-window scoping → `energy-compliance` (when shipped).
- No `docs/` artifact, no Word / PDF, no `aec-doc-gen`.
- Caveat block always present.
- Fetch only after explicit user authorization.

## Anti-patterns (never do)

- Stating values inline ("U-0.32 / SHGC 0.40 for CZ 4A commercial") — never. Numbers live only in the quoted source.
- Claiming `Table C402.4` row from recall — never.
- Using center-of-glass U-factor as if it were NFRC whole-window.
- Treating CA projects as base-IECC only — `Title 24 Part 6` overlay required.
- Auto-fetching without explicit authorization.
- Hedging — verdicts are PASS / FAIL / MARGINAL.
- Running `energy-compliance` from inside this command — pointer-only.
