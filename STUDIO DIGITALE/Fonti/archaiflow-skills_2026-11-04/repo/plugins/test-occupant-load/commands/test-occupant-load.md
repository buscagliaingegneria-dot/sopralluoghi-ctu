---
title: Test Occupant Load
summary: Compute occupant load when you already have the table row
discipline: code-life-safety
tags: ["Compliance"]
description: Single-shot occupant-load math against IBC §1004 + Table 1004.5 source text the user has already in hand. Lighter than the `design-occupancy-load` skill — `/test-occupant-load` is for "I have the Table row and the SF, just compute it" while `design-occupancy-load` walks the full multi-turn fetch + multi-use sum workflow. Carries no IBC values internally. Federal IBC only.
argument-hint: <space-sf> <function> <pasted-table-row>
---

# Test Occupant Load

Single-shot occupant-load math against IBC §1004 + Table 1004.5 text the user has already in hand. The command **bundles no values** and **recalls no values** from training; every load factor in the output is a verbatim quote from the user's pasted text or a live WebFetch with a SourceURL.

This command is the **light-weight sibling of the `design-occupancy-load` skill**. Use:
- **`design-occupancy-load` (skill)** when you want the multi-turn workflow: confirm edition / jurisdiction → ask program (multiple sub-areas + functions) → "should I fetch §1004.5 + Table row?" per use group → assemble per-space loads → sum + flag multi-use rules.
- **`/test-occupant-load` (this command)** when you already have the relevant Table row pasted (or want a single-shot fetch) AND a single space + function — and you just want `ceil(SF / factor)` math with verbatim attribution.

If your project has multiple spaces / multiple use groups OR you don't have the Table row text in hand: use the `design-occupancy-load` skill — it owns the multi-turn fetch + sum pattern.

## Why this pattern (read first)

IBC §1004 + Table 1004.5 row labels and several factor values are revised between editions (IBC 2018 / 2021 / 2024). Bundled transcriptions silently misquote when written from training-data recall (well-tracker incident, 2026-05-09; design-stair v0 incident, 2026-05-10). The command compares against text the user provides — pasted from their adopted edition — and labels every row with the source.

The user MUST paste the relevant Table row + § text, OR authorize a single live WebFetch. There is no offline fallback to bundled values — by design.

## Scope and limits — read first

This command computes **a single space against IBC §1004 + Table 1004.5 Federal** ONLY. It does NOT cover:

- **State / city amendments**: NYC BC §1004 (NYC LL58), CA CBC §1004, FL Building Code §1004, etc.
- **Multi-space / multi-use computation** (§1004.6) — that's `design-occupancy-load` skill territory.
- **Means-of-egress capacity** (§1005.3.1) — separate workflow.
- **Cumulative occupant load** across multiple spaces feeding a single exit.
- **Travel distance / common path / dead-end** (§1006, §1017, §1020).
- **Posted occupant load** for assembly (§1004.5.1) — flag if user wants to apply, but command does not modify base computation.
- **Concentrated vs un-concentrated assembly distinction** based on actual seating layout — user must pick the row.
- **Industrial / S-occupancy density adjustments** based on storage rack layouts.

State amendments and adjacent-code requirements are the user's burden to verify separately.

## Authoritative sources used

If the user authorizes a fetch, the workflow uses these public URLs only:

| Standard | Public source |
|---|---|
| IBC 2024 | https://codes.iccsafe.org/content/IBC2024P1 |
| IBC 2021 | https://codes.iccsafe.org/content/IBC2021P2 |
| IBC 2018 | https://codes.iccsafe.org/content/IBC2018 |

Paste preferred. Fetch is single-shot per Table row the user nominates — for the full multi-turn fetch + multi-use sum workflow, use the `design-occupancy-load` skill.

## Inputs the command needs

1. **Space SF** — net floor area of the single space, in sf (use net-vs-gross matching what the user-pasted row specifies).
2. **Function** — the IBC Table 1004.5 row that applies. The user picks the row; the command does not classify use. Common rows include:
   - Assembly without fixed seats (concentrated / unconcentrated / standing)
   - Assembly with fixed seats (count seats per §1004.6)
   - Business areas
   - Educational classroom / shop / vocational
   - Mercantile (basement / ground / upper)
   - Industrial / S-1 / S-2
   - Residential
   - Day care / institutional / medical care / inpatient
   - Library reading rooms / stack
3. **Edition** — IBC 2018 / 2021 / 2024.
4. **Jurisdiction** — for the report only (state amendments are out-of-scope).
5. **Source text** — one of:
   - Paste the verbatim Table 1004.5 row + relevant § text (preferred for `/test-occupant-load` — that's the scope).
   - Authorize one-shot fetch from the URL table above.
   - Defer to `design-occupancy-load` skill if the user wants the full multi-turn fetch workflow.

## Required citations (verify exact § from source)

Topic-level mapping. The verbatim § number + load factor comes from the user's pasted text or a single live fetch.

| Topic | IBC § (subject area) |
|---|---|
| Function classification + load factor | §1004.5 + Table 1004.5 |
| Posted increased occupant load (assembly) | §1004.5.1 (out-of-scope: user must furnish AHJ posting) |
| Multi-use combination | §1004.6 (out-of-scope: use `design-occupancy-load` skill) |
| Outdoor areas | §1004.7 |

## Workflow

### Step 1 — Confirm scope

> "This command does single-shot occupant-load math against IBC §1004 + Table 1004.5 Federal — single space, single function. State amendments (NYC BC, CA CBC, FL Building Code), means-of-egress capacity (§1005.3.1), and cumulative load across spaces are NOT covered. Multi-use spaces (§1004.6) require the `design-occupancy-load` skill instead. To proceed I need:
> 1. Space SF + function (single space, single row of Table 1004.5).
> 2. IBC edition + jurisdiction.
> 3. Source: paste the Table 1004.5 row + relevant § text, OR authorize one-shot fetch (for multi-turn fetch use `design-occupancy-load` skill).
>
> Continue?"

If multi-use space / multi-function: stop and route to `design-occupancy-load` skill.

### Step 2 — Compute against source text

Math: `occupant load = ceil(space_sf / load_factor)` for net SF rows, or per the source's expression for gross SF rows.

- Quote the row from the source (verbatim, blockquoted).
- Apply the formula with user's SF.
- Show the math: `ceil(2,400 / 100) = 24 occupants`.

Present as a markdown table:

| Item | Source factor | Space SF | Computed load | CitedSection | SourceURL | FetchedAt | Confidence | Remarks |
|---|---|---|---|---|---|---|---|---|

Schema same as `design-occupancy-load` skill. For pasted source: `SourceURL` = `pasted by user`, `FetchedAt` = paste timestamp.

### Step 3 — Optional persistence

After the inline table, ask:
> "Save this as a file? (a) markdown, (b) CSV, (c) both, (d) inline only. Path?"

Default suggested path `docs/egress/<space-id>-occupant-load.{csv|md}` if save chosen.

### Step 4 — Report

After the table:
- Total occupant load (single value for single space).
- Formula shown verbatim.
- Out-of-scope reminders:
  - Multi-use combination (§1004.6) — `design-occupancy-load` skill.
  - Means-of-egress capacity (§1005.3.1) — separate workflow.
  - Travel distance / common path / dead-end (§1006, §1017, §1020) — separate.
  - State amendment overlay (NYC BC §1004, CA CBC §1004, etc.) — user verifies.
  - Posted occupant load (§1004.5.1) — AHJ approval, user furnishes.
- AOR's stamped opinion governs; AHJ confirms compliance with adopted overlays (NOT checked here).
- If multi-space / multi-function: recommend `design-occupancy-load` skill instead.

## NA AEC conventions (enforce)

- English only.
- Imperial-first: sf (net or gross per the source), occupants. Metric only if the source uses it.
- IBC § format: `IBC 2024 §1004.5` / `IBC 2024 Table 1004.5`. Never "section 1004" generically.
- AHJs named specifically: NYC DOB, FDNY, LADBS, DSA, CA HCAI, Toronto Building, GSA, USACE.
- Roles: Architect of Record (AOR), Code Consultant, Egress Consultant.

## Constraints

- **Never recall IBC load factors from training.** Verbatim Table 1004.5 row from user paste or single live WebFetch only.
- **Never paraphrase the source.** "1 per 100 gross" must appear verbatim, not as "100 sf/person".
- **Show the formula in Remarks.** `ceil(2,400 / 100) = 24 occupants` — math visible.
- **Single space, single function.** Multi-use is `design-occupancy-load` skill territory — defer.
- **Posted occupant load** is an AHJ approval, not a recall — user must furnish AHJ-stamped posting.
- **Source URL or 'pasted by user' is mandatory in every output row.**
- **No `docs/` artifact unless user opts in.**
- **Caveat block always present.**
- **Fetch only after explicit user authorization** (single-shot per Table row).
- **Multi-turn fetch + multi-use sum is `design-occupancy-load` skill territory.** Don't reproduce that workflow here — defer.

## Anti-patterns

- Filling a `Source factor` cell from training-data recall instead of a paste / fetch quote.
- Re-introducing a `references/ibc-1004-table.md` of transcribed factors — deliberately none.
- Re-introducing a `compute_load.py` with hardcoded load-factor constants — deliberately none.
- Auto-classifying the function ("this looks like a B occupancy") — user picks the row.
- Auto-converting "1 per 7 net" into "7 sf/person" — preserve the source's expression.
- Skipping ceil-rounding ("38.5 occupants" in output) — IBC requires whole occupants.
- Computing means-of-egress capacity (0.2/0.3 in/occ → exit width) — out of scope; user runs separately.
- Quoting Table 1004.5 row from a different edition than the user's adopted edition.
- Doing multi-turn per-topic fetch confirmation — that's `design-occupancy-load` skill scope; this command is single-shot.
- Computing a multi-use sum here — that's `design-occupancy-load` skill scope; defer.

## Resources

None. This command is intentionally body-only. For the full multi-turn workflow with per-topic fetch confirmation + multi-use combination, use the `design-occupancy-load` skill.
