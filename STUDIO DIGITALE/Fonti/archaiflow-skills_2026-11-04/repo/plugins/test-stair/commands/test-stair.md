---
title: Test Stair
summary: Check stair geometry when you already have the code text
discipline: code-life-safety
tags: ["Compliance"]
description: Single-shot stair geometry math against IBC §1011 + 2010 ADA §504/§505 source text the user has already in hand. Lighter than the `design-stair` skill — `/test-stair` is for "I have the § text and the dims, just math it" while `design-stair` walks the full multi-turn fetch + comparison workflow. Carries no IBC / ADA values internally. Federal IBC + Federal 2010 ADA only.
argument-hint: <geometry> <pasted-section-text>
---

# Test Stair

Single-shot stair geometry math against IBC §1011 + 2010 ADA §504-§505 text the user has already in hand. The command **bundles no values** and **recalls no values** from training; every limit in the output is a verbatim quote from the user's pasted text or a live WebFetch with a SourceURL.

This command is the **light-weight sibling of the `design-stair` skill**. Use:
- **`design-stair` (skill)** when you want the multi-turn workflow: confirm edition / jurisdiction → ask geometry → "should I fetch §1011.5.2?" per topic → present table.
- **`/test-stair` (this command)** when you already have the § text pasted and the geometry pasted and want the comparison done in one shot.

If you don't have the § text and want it fetched: invoke the `design-stair` skill instead — it owns the fetch-confirmation pattern.

## Why this pattern (read first)

IBC §1011 (Stairways) + §1014 (Handrails) and 2010 ADA §504-§505 dimensions are revised between IBC editions and re-numbered occasionally. Bundled transcriptions silently misquote when written from training-data recall (well-tracker + design-stair v0 incidents, 2026-05-09 / 2026-05-10). The command compares against text the user provides — pasted from their adopted edition — and labels every row with the source.

The user MUST paste the relevant § text, OR authorize a single live WebFetch. There is no offline fallback to bundled values — by design.

## Scope and limits — read first

This command checks **Federal IBC §1011 + §1014.2/§1014.6** and **2010 ADA §504-§505** ONLY. It does NOT cover:

- **State / city amendments**: NYC LL141 + NYC BC §1011 modifications, CA Title 24 Pt 2 §1011 amendments, MA 780 CMR amendments, ICC A117.1-2017 (different handrail-extension figures).
- **IRC R311.7** (one- and two-family dwellings — different riser / tread / headroom limits).
- **Curved stairs** (§1011.9), **spiral stairs** (§1011.10), **alternating tread devices / ships ladders** (§1011.11-§1011.12), **winder geometry** (§1011.5.3).
- **Means-of-egress occupant-load capacity** (§1005.3.1).
- **Stair guards** (§1015), **stair fire-resistance enclosure** (Ch.7).
- **OSHA 29 CFR 1910.25**, **NFPA 101**.

State amendments and adjacent-code requirements are the user's burden to verify separately. The report flags out-of-scope items.

## Authoritative sources used

If the user authorizes a fetch, the workflow uses these public URLs only:

| Standard | Public source |
|---|---|
| IBC 2024 | https://codes.iccsafe.org/content/IBC2024P1 |
| IBC 2021 | https://codes.iccsafe.org/content/IBC2021P2 |
| IBC 2018 | https://codes.iccsafe.org/content/IBC2018 |
| 2010 ADA Standards | https://www.ada.gov/law-and-regs/design-standards/2010-stds/ |

Paste preferred. Fetch is single-shot per § the user nominates — for the full multi-turn fetch workflow use the `design-stair` skill.

## Inputs the command needs

1. **Stair geometry** (each in inches; treat as missing if the user hasn't stated):
   - Width
   - Headroom clearance
   - Riser height (uniform value, or both max/min)
   - Tread depth (uniform value, or both max/min)
   - Nosing radius / projection / underside angle
   - Landing depth
   - Vertical rise between landings
   - Number of risers
   - Open risers? (yes/no)
   - Wet conditions? (yes/no)
   - Slip-resistant tread surface? (yes/no — only if wet)

2. **Handrail geometry** (skip if not on accessible route AND no IBC handrail concern):
   - Both sides? (yes/no)
   - Height above nosing
   - Wall clearance
   - Cross section: circular (give diameter) or non-circular (give perimeter + max cross-section)
   - Top extension beyond top riser
   - Bottom extension beyond bottom riser

3. **Project context:**
   - IBC edition adopted (2018 / 2021 / 2024)
   - Jurisdiction (for the report only — state amendments are out-of-scope)
   - Use group (B / A-3 / R-2 / etc. — affects §1011.5.2 exception applicability)
   - On accessible route? (yes/no)

4. **Source text** — for each topic the user wants math'd, one of:
   - Paste the verbatim § text (preferred for `/test-stair` — that's the scope).
   - Authorize one-shot fetch from the URL table above.
   - Defer to `design-stair` skill if the user wants the full multi-turn fetch workflow.

5. **Out-of-scope check.** If the stair is curved / spiral / alternating-tread / ship-ladder / IRC R311.7 dwelling / OSHA workplace / NFPA 101 governed: stop and refer to AOR / `design-stair`.

## Required citations (verify exact § from source)

Topic-level mapping. The verbatim § number + dim comes from the user's pasted text or a live fetch.

| Topic | IBC § (subject area) | 2010 ADA § |
|---|---|---|
| Stair width | §1011.2 | — |
| Headroom | §1011.3 | — |
| Riser height + tread depth | §1011.5.2 | §504.2 |
| Riser/tread uniformity | §1011.5.4 | §504.2 |
| Nosing geometry | §1011.5.5 | §504.5 |
| Landing depth | §1011.6 | — |
| Vertical rise between landings | §1011.8 | — |
| Handrail height | §1014.2 | §505.4 |
| Handrail wall clearance | — | §505.5 |
| Handrail cross-section | — | §505.7 |
| Handrail extensions | §1014.6 | §505.10 |
| Open risers | — | §504.3 |
| Both-sides handrails | — | §505.2 |
| Wet conditions / slip resistance | — | §504.7 |

## Workflow

### Step 1 — Confirm scope

> "This command does single-shot stair geometry math against IBC §1011 + 2010 ADA §504-§505. State amendments (NYC LL141, CA Title 24, ICC A117.1, MA 780 CMR), IRC R311.7 dwellings, curved/spiral/winder stairs, OSHA, and NFPA 101 are NOT covered. To proceed I need:
> 1. Stair geometry (width, headroom, riser, tread, nosing, landing, vertical rise, number of risers, open-riser y/n, wet y/n).
> 2. Handrail geometry (skip if not on accessible route).
> 3. IBC edition + jurisdiction + use group + accessible-route y/n.
> 4. Source: paste each § text, OR authorize one-shot fetch (for multi-turn fetch use the `design-stair` skill).
>
> Continue?"

If curved / spiral / winder / IRC / OSHA / NFPA 101: stop and refer to AOR / `design-stair`.

### Step 2 — Compare inline against source text

For each topic with both source text AND geometry provided:
- Quote the limit from the source (verbatim, blockquoted).
- Compare to user's geometry.
- Label `pass` / `fail` / `input missing` / `out-of-scope`.

Present as a markdown table:

| Item | Required | Actual | Status | CitedSection | SourceURL | FetchedAt | Confidence | Remarks |
|---|---|---|---|---|---|---|---|---|

Schema same as `/test-ada` Step 4. For pasted source: `SourceURL` = `pasted by user`, `FetchedAt` = paste timestamp.

### Step 3 — Optional persistence

After the inline table, ask:
> "Save this as a file? (a) markdown, (b) CSV, (c) both, (d) inline only. Path?"

Default suggested path `docs/stairs/<stair-id>-stair-check.{csv|md}` if save chosen.

### Step 4 — Report

After the table:
- Counts: total / pass / fail / input missing / out-of-scope.
- Fail rows with Required / Actual + cited § + SourceURL.
- Input-missing rows naming what to provide for a re-run.
- Out-of-scope reminders: state amendments, ICC A117.1, IRC, curved/spiral/winder, OSHA, NFPA 101 — user verifies separately.
- AOR / SE confirms structural adequacy; AHJ confirms compliance with adopted local amendments (NOT checked here).
- If many topics need fetch: recommend `design-stair` skill instead for the multi-turn fetch workflow.

## NA AEC conventions (enforce)

- English only.
- Imperial-first: in, ft, °F, lb force. Metric only if the source uses it.
- IBC § format: `IBC 2024 §1011.5.2`. ADA §: `2010 ADA §505.10`.
- AHJs named specifically: NYC DOB, LADBS, DSA, CA HCAI, Boston ISD, Toronto Building, GSA, USACE.
- Roles: Architect of Record (AOR), Structural Engineer of Record (SEOR), Code Consultant.

## Constraints

- **Never recall IBC / ADA stair values from training.** For every dim, the comparison must reference user-pasted text or live WebFetch with the SourceURL captured.
- **Never paraphrase the source.** "Riser shall be 4 in min, 7 in max" must appear verbatim, not as "4-7 in".
- **Source URL or 'pasted by user' is mandatory in every output row.**
- **For curved / spiral / winder / IRC / OSHA / NFPA 101 stairs**: stop at Step 1. This command does not check those.
- **Caveat block always present.**
- **Fetch only after explicit user authorization** (single-shot per topic).
- **Multi-turn fetch is `design-stair` skill territory.** Don't reproduce that workflow here — defer.

## Anti-patterns

- Filling a `Required` cell from training-data recall instead of a paste / fetch quote.
- Re-introducing a `check_stair.py` with hardcoded riser/tread/headroom/handrail constants — `design-stair` skill v0 had this and it was removed for this exact reason.
- Re-introducing a `references/ibc-1011.md` of transcribed code text — deliberately none.
- Auto-converting source units (4-7" → 100-178 mm) — quote the source as-is.
- Skipping the jurisdiction / edition confirmation in Step 1.
- Treating IRC R311.7 dwellings the same as IBC commercial — different limits, refer to AOR.
- "Riser is fine" / "looks compliant" — verdicts are binary against quoted source: PASS / FAIL / MARGINAL.
- Doing multi-turn per-topic fetch confirmation — that's `design-stair` skill scope; this command is single-shot.

## Resources

None. This command is intentionally body-only. For the full multi-turn workflow with per-topic fetch confirmation, use the `design-stair` skill.
