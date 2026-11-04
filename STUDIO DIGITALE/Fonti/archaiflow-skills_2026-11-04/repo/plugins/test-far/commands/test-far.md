---
title: Test FAR
summary: Check floor area ratio, coverage, setback, and height
discipline: code-life-safety
tags: ["Compliance"]
description: Single-parcel zoning gut-check (FAR / lot coverage / setback / height) — for each topic the command WebFetches the operative § live from the jurisdiction's published zoning portal (or accepts a paste) and math-checks provided dimensions against the verbatim source. Carries no zoning values internally. Single base district only — overlays / bonuses / variances are out-of-scope.
argument-hint: <jurisdiction> <district> <provided-dims>
---

# Test FAR

Single-parcel zoning gut-check (Floor Area Ratio, lot coverage, setback / yard, height limit) against the **AHJ's published Zoning Resolution / Zoning Code text**. Zoning is fully local — there is no federal base. The command bundles **no values** and recalls **no values** from training; every limit in the output is a verbatim quote from text the user pasted or text WebFetched live from the jurisdiction portal.

For master-plan / form-based-code / public-realm questions use the `urban-designer` agent. For NYC parcel-level lookups including overlays use the `nyc-zoning-lookup` skill. For a full zoning worksheet across all use, bulk, and yard provisions use the `zoning-summary` skill.

## Why this pattern (read first)

Zoning text changes annually in many jurisdictions and varies parcel-to-parcel via overlays, contextual rules, and special districts. Bundled zoning transcriptions go stale instantly and silently misquote when written from training-data recall. The workflow asks "should I fetch §X from <AHJ portal>?" then WebFetches the operative paragraph, quotes the source URL inline, and only then math-checks.

The user MUST have a connection to the public internet during use, OR be willing to paste the relevant § text. There is no offline fallback to bundled values — by design.

## Scope and limits — read first

This command checks **a single parcel against a single base district** in the user's stated jurisdiction. It does NOT cover:

- **Special districts / overlays / contextual modifiers** (NYC ZR §X-145+ Quality Housing, NYC R10 sliver rule, LA Specific Plans, SF Special Use Districts, Toronto site-and-area-specific overrides).
- **Bonus FAR** (NYC Inclusionary Housing / Voluntary IH / MIH / plaza bonus / transit bonus, LA TOC, SF Density Bonus).
- **Variance / special permit / certification approvals** (BSA in NYC, ZA Determinations in LA, Toronto Committee of Adjustment).
- **Site plan review / design review / urban design controls.**
- **Building code separation requirements** (those are IBC §602 — see `/test-fire-rating`).
- **Subdivision / parcelization / lot mergers.**
- **Coastal / floodplain / historic-overlay restrictions.**

Local amendments and last year's zoning text changes are the user's burden to verify. The report flags out-of-scope items the user must run separately.

## Authoritative sources used

The workflow fetches from the jurisdiction-published zoning portal of the user's stated jurisdiction. Pre-vetted public sources:

| Jurisdiction | Public source |
|---|---|
| NYC | https://zr.planning.nyc.gov/ |
| Los Angeles | https://planning.lacity.org/zoning/ |
| Chicago | https://www.chicago.gov/city/en/depts/dcd/supp_info/citywide_zoning.html |
| San Francisco | https://codelibrary.amlegal.com/codes/san_francisco/latest/sf_planning |
| Boston | https://library.municode.com/ma/boston/codes/redevelopment_authority |
| Seattle | https://library.municode.com/wa/seattle/codes/municipal_code |
| Toronto | https://www.toronto.ca/city-government/planning-development/zoning-by-law-preliminary-zoning-reviews/ |
| Houston | Houston has no euclidean zoning — Ch.42 lot/building line rules apply |

If the jurisdiction is not in the table, the user must paste the relevant § text — fetched URLs that the command cannot verify as the jurisdiction's official source must not be used. Do not WebFetch from up.codes / zoneomics / etc. as authoritative — they are convenience aggregators, not the jurisdiction source of truth.

## Inputs the command needs

1. **Jurisdiction** — name the jurisdiction specifically (NYC DCP, City of LA Planning, City of Toronto Planning, etc.).
2. **District** — base zoning district code as the jurisdiction uses it (NYC `R6A` / `M1-4`, LA `R3`, Toronto `R-T`, Chicago `RT-4`, SF `RH-3`).
3. **Provided dimensions** — what the design has, with labels:
   - GFA / floor area (sf, or m² if the jurisdiction uses metric)
   - Lot area
   - Building footprint / lot coverage
   - Setbacks / yards (front, side, rear) in ft
   - Building height (ft + stories)
   - Other district-specific (rear yard equivalent, sky exposure plane, encroachment plane, lot line wall)
4. **Auto-fetch?** — say "fetch all without re-asking" once or per-topic confirm.

## Required citations (verify exact § from fetch)

Topic-level mapping. Specific § numbers come from the source the workflow fetches or the user pastes.

| Topic | NYC ZR (subject area) | LA LAMC | Chicago | Toronto Bylaw 569-2013 | SF Planning Code |
|---|---|---|---|---|---|
| FAR | Article II §23-15 / Art.III §33-12 / Art.IV §43-12 (district-specific) | §12.21.1 | use-specific table | §10 (district) | §124 |
| Lot coverage | Art.II §23-141 / Art.IV §43-13 | §12.21.1 | use-specific | §10 | §124 |
| Setbacks / yards | Art.II §23-44 / Art.IV §43-14 | §12.21.1.C | use-specific | §10 | §132, §134 |
| Height | Art.II §23-63 / Art.IV §43-43 | §12.21.1 | use-specific | §10 | §260 |
| Bulk / sky-exposure | Art.II §23-65 / Art.III §33-43 | n/a | n/a | n/a | n/a |
| Rear yard equivalent | Art.II §23-532 | n/a | n/a | n/a | n/a |

## Workflow

### Step 1 — Confirm scope

Tell the user, all at once:

> "This command checks a single parcel against a single base zoning district. Special districts, overlays, contextual modifiers, bonus FAR (IH / MIH / TOC / plaza), variances, and AHJ approvals are NOT covered — the report flags any out-of-scope items you must verify separately. To proceed I need:
> 1. Jurisdiction (NYC DCP / LA Planning / Toronto / etc.).
> 2. Base district code (NYC `R6A`, LA `R3`, etc.).
> 3. Provided dimensions (GFA, lot area, footprint, setbacks, height, plus district-specific).
> 4. **Auto-fetch?** — 'fetch all without re-asking' or per-topic confirm.
>
> Continue?"

If the jurisdiction is Houston: tell the user Houston has no euclidean zoning; this command cannot run a FAR / coverage check. Ch.42 lot/building line rules apply — paste those for a custom check.

### Step 2 — Gather dims (ask only what is missing)

Treat each dim as missing if the user hasn't stated it; never substitute a typical value.

### Step 3 — Fetch each authoritative § LIVE (one topic at a time)

For each topic in the Required citations table that applies to the district:

1. Tell the user the topic + the constructed source URL from the jurisdiction portal in Authoritative sources. Example:
   > "Need NYC ZR §23-15 (FAR for residential R6A) — should I WebFetch from `https://zr.planning.nyc.gov/`?"
   (Skip the per-topic prompt if the user gave blanket "fetch all" in Step 1.)
2. WebFetch on confirmation. On paywall / empty body, fall back to WebSearch with `<jurisdiction> zoning §<section> <topic> site:<official-domain>` → WebFetch the first AHJ-domain result. If still nothing, ask user to paste.
3. Extract the verbatim relevant paragraph + the source URL + a fetch timestamp. Quote 1-2 sentences back to the user so they can sanity-check the district + topic match.
4. Hold the citation in memory for the comparison step. Re-use within the same session — do not re-fetch.

### Step 4 — Compare inline and present the result

For each topic, compare the user's provided value against the limit extracted from the fetched citation. Present as a markdown table:

| Item | Required | Actual | Status | CitedSection | SourceURL | FetchedAt | Confidence | Remarks |
|---|---|---|---|---|---|---|---|---|

Where each column matches the schema in `/test-ada` Step 4 (verbatim Required, AHJ § format in CitedSection, fetched URL in SourceURL, ISO timestamp, confidence high/medium/low, exception/scope notes in Remarks).

### Step 5 — Optional persistence

After the inline table, ask:
> "Save this as a file? (a) markdown, (b) CSV, (c) both, (d) inline only. Path?"

Default suggested path `docs/zoning/<parcel-id>-far-check.{csv|md}` if the user picks save.

### Step 6 — Report

After the table:
- Counts: total / pass / fail / input missing / out-of-scope.
- Fail rows with Required / Actual + cited § + SourceURL.
- Input-missing rows naming what to provide for a re-run.
- Out-of-scope rows naming where the user must verify separately:
  - Special district / contextual / overlay text
  - Bonus FAR (IH, MIH, TOC, plaza, transit, etc.)
  - Variance / special permit / certification path
  - Site plan / design review process
  - Floodplain / coastal / historic overlay
- Reminder: zoning text changes; verify the source revision date. AHJ rules govern (NYC DCP / BSA, LA ZA, Toronto CofA). This command does not substitute for jurisdictional review.

## NA AEC conventions (enforce)

- English only.
- Imperial-first: ft, sf, ac, du/ac, stories. Metric only if the jurisdiction uses it (Toronto, parts of CA).
- AHJs named specifically: NYC DCP / NYC BSA, City of LA Planning / LA ZA, City of Chicago DPD, SF Planning, Boston BPDA, Toronto City Planning / CofA. Never "the city" or "the jurisdiction".
- District naming as the jurisdiction uses (NYC `R6A`, not `R-6A`; LA `R3`, not `R-3`).
- Zoning § format as the jurisdiction publishes (NYC `ZR §23-15`, LA `LAMC §12.21.1.A`, Toronto `Bylaw 569-2013 §X`, SF `Planning Code §124`).

## Constraints

- **Never invent zoning values.** No federal base — local jurisdictions are the only authority.
- **Never paraphrase from training.** Source text in the output must be verbatim from user paste or WebFetch.
- **Never claim a specific § number from recall.** Topic-level pointers are fine; specific § comes from source.
- **Single base district only.** Multi-district / overlay / bonus calculations are out-of-scope.
- **Never WebFetch from convenience aggregators** (up.codes, zoneomics) as the authoritative source — only the jurisdiction portal.
- **No `docs/` artifact unless user opts in.** Markdown response only by default.
- **Caveat block always present.**
- **Fetch only after explicit user authorization.**

## Anti-patterns

- Stating an FAR / coverage / setback / height value inline ("FAR 3.0", "30 ft front yard") — never. Numbers live only in the quoted source.
- Auto-applying NYC Quality Housing / R10 sliver / plaza bonus from recall — out-of-scope; flag for user.
- Treating Houston as zoned — no euclidean zoning; Ch.42 only.
- "Looks like FAR pencils" — never. Math against quoted source, label PASS / FAIL / MARGINAL.
- Quoting up.codes or zoneomics as the source URL when the jurisdiction has its own portal.
- Auto-converting metric ↔ imperial — quote the source as-is.
- Running `zoning-summary` or `nyc-zoning-lookup` from inside this command — pointer-only.
- Claiming "FAR is the same in R6A and R6B" — districts are not interchangeable; fetch each.

## Resources

None. This command is intentionally body-only — see "Why this pattern" above.
