---
title: Test ADA
summary: Math-check one accessibility clearance against the source
discipline: code-life-safety
tags: ["Compliance"]
description: Single-element 2010 ADA clearance gut-check — for each compliance topic the command WebFetches the operative § live from ada.gov (or accepts a paste) and math-checks provided dimensions against the verbatim source. Carries no ADA values internally. Federal 2010 ADA only — state amendments (CA Title 24 Pt 2 Ch.11B, ICC A117.1) are out-of-scope.
argument-hint: <space-type> <provided-dims> [edition-and-jurisdiction]
---

# Test ADA

Single-element accessibility gut-check (one door, one ramp run, one toilet compartment, etc.) against **Federal 2010 ADA Standards §§ as fetched live from ada.gov** or as pasted by the user. The skill bundles **no values** and recalls **no values** from training; every limit in the output is a verbatim quote with a SourceURL.

For a multi-element ADA scoping pass use the `ada-tracker` skill. For plain-English interpretation of a single § with no math use `/explain-code` with `code = 2010 ADA`.

## Why this pattern (read first)

This command bundles nothing and recalls nothing — for every compliance topic the workflow asks "should I fetch §X from ada.gov?" then WebFetches the operative paragraph, quotes the source URL inline, and only then math-checks. Rationale: bundled standards transcriptions silently misquote when written from training-data recall (well-tracker incident, 2026-05-09); live fetch + visible source URL keeps the authoritative copy in front of the user every check.

The user MUST have a connection to the public internet during use, OR be willing to paste the relevant § text. There is no offline fallback to bundled values — by design.

## Scope and limits — read first

This command checks **Federal 2010 ADA Standards for Accessible Design** ONLY. It does NOT cover:

- **State / city amendments**: CA Title 24 Pt 2 Ch.11B (CBC), CA HCAI / DSA scoping, NYC LL58, MA AAB, TX TAS, MN Ch.1341, FL Building Code Accessibility, etc.
- **ICC A117.1-2017** (state-adopted accessibility companion — different cross-section, handrail-extension, and clear-floor-space figures).
- **CSA B651** (Canadian projects — different framework, not ADA).
- **ABA / GSA P-100** federal-facility overlays.
- **IBC accessibility provisions** (Ch.11) where they diverge from 2010 ADA.

When the project is governed by a state overlay (CA, TX, NY, etc.) the user must run their own check against the overlay text — out-of-scope here. The command flags this in the report.

## Authoritative sources used

The workflow fetches from this public URL only (ask user before each fetch):

| Standard | Public source |
|---|---|
| 2010 ADA Standards | https://www.ada.gov/law-and-regs/design-standards/2010-stds/ |

If a WebFetch returns a paywall / login wall or empty body, fall back: (a) WebSearch with `2010 ADA §<section> <topic keywords> site:ada.gov`; (b) ask the user to paste from their copy. A local RAG index is acceptable if the user has indexed the 2010 ADA PDF.

## Inputs the command needs

1. **Space type** — name the single element under test:
   - Door (clear width / maneuvering / threshold / hardware)
   - Ramp run (running slope / cross slope / landing / edge protection / handrail extension)
   - Toilet room / WC compartment (turning space / fixture clearance / grab bar)
   - Lavatory / sink (knee clearance / forward reach)
   - Parking (count / accessible vs van / slope / signage)
   - Transfer / clear floor space (forward / side / obstructed approach)
   - Drinking fountain (spout height / knee clearance)
   - Reach range (forward / side / obstructed)
   - Operable parts (height / force / one-hand operation)
   - Elevator (cab clearance / hall call height)
2. **Provided dimensions** — what the design has, with labels (in / ft / 1:X slope / lb force).
3. **Jurisdiction** — for the report only (state overlays are out-of-scope; the report flags any overlay the user must verify separately).
4. **Auto-fetch?** — say "fetch all without re-asking" once and the workflow WebFetches each topic without confirming each time. Otherwise the workflow confirms before every fetch.

If a value is missing after asking, mark its row `Status: input missing`. Never substitute a typical value.

## Required citations

For each topic in scope of the user's space, the workflow fetches the corresponding 2010 ADA §. Topic-level mapping (the verbatim § number + text comes from what the workflow fetches or what the user pastes):

| Topic | 2010 ADA § (subject area; verify number from fetch) |
|---|---|
| Door clear width | §404 (Doors, Doorways, and Gates) |
| Door maneuvering clearance | §404 |
| Door threshold | §404 |
| Door hardware (height / operation) | §404, §309 (Operable parts) |
| Ramp running slope / cross slope | §405 |
| Ramp landing | §405 |
| Ramp handrail extension | §505 |
| Toilet room turning space | §603, §304 (Turning space) |
| WC clearance / grab bars | §604 |
| Lavatory knee clearance / reach | §606, §305, §308 |
| Accessible parking count / van | §208, §502 |
| Transfer / clear floor space | §305, §306 |
| Drinking fountain spout / knee | §602 |
| Reach range | §308 |
| Operable parts | §309 |
| Elevator cab / hall call | §407 |

## Workflow

### Step 1 — Confirm scope

Tell the user, all at once:

> "This command checks Federal 2010 ADA Standards only. State overlays (CA Title 24 11B, ICC A117.1, NYC LL58, etc.) are NOT covered — the report flags any overlay you must verify separately. To proceed I need:
> 1. Space type and provided dimensions.
> 2. Jurisdiction (for the report only — overlays are out-of-scope).
> 3. **Auto-fetch?** — 'fetch all without re-asking' or per-topic confirm.
>
> Continue?"

If the project is CSA B651 (Canada) or ICC A117.1 governed: stop and tell the user this command applies 2010 ADA only — refer to a separate workflow.

### Step 2 — Gather geometry (ask only what is missing)

Treat each dim as missing if the user hasn't stated it; never substitute a typical value.

### Step 3 — Fetch each authoritative § LIVE (one topic at a time)

For each topic in the Required citations table that applies to the user's space type:

1. Tell the user the topic + the source URL. Example:
   > "Need 2010 ADA §404 (Door maneuvering) — should I WebFetch from `https://www.ada.gov/law-and-regs/design-standards/2010-stds/`?"
   (Skip the per-topic prompt if the user gave blanket "fetch all" in Step 1.)
2. WebFetch on confirmation. On paywall / empty body, fall back to WebSearch `2010 ADA §<section> <topic> site:ada.gov` → WebFetch the first official-looking result. If still nothing, ask user to paste.
3. Extract the verbatim relevant paragraph + the source URL + a fetch timestamp. Quote 1-2 sentences back to the user so they can sanity-check.
4. Hold the citation in memory for the comparison step. Re-use within the same session — do not re-fetch.

### Step 4 — Compare inline and present the result

For each topic, compare the user's geometry against the limit extracted from the fetched citation. Present as a markdown table:

| Item | Required | Actual | Status | CitedSection | SourceURL | FetchedAt | Confidence | Remarks |
|---|---|---|---|---|---|---|---|---|

Where:
- `Required` — verbatim quote (or formatted dim) from the fetched citation. Prefer verbatim.
- `Actual` — value the user provided.
- `Status` — `pass` / `fail` / `input missing` / `out-of-scope`.
- `CitedSection` — e.g. `2010 ADA §404.2.4.1`.
- `SourceURL` — the URL returned by WebFetch (NOT a guessed canonical URL).
- `FetchedAt` — ISO timestamp of the fetch.
- `Confidence` — `high` (verbatim quote, dim clearly extracted), `medium` (paraphrase or value inferred), `low` (input missing / fetch ambiguous).
- `Remarks` — exception notes, scope warnings, AOR-confirms reminders.

### Step 5 — Optional persistence

After the inline table, ask:
> "Save this as a file? (a) markdown, (b) CSV, (c) both, (d) inline only. Path?"

If the user picks save, write directly with Write — no scripts, no templates. Default suggested path `docs/ada/<element-id>-ada-check.{csv|md}`, but use whatever the user names.

### Step 6 — Report

After the table (and optional save), tell the user:
- Counts: total / pass / fail / input missing / out-of-scope.
- Fail rows with Required / Actual + cited § + SourceURL so the user can re-verify in 30s.
- Input-missing rows naming what to provide for a re-run.
- Out-of-scope rows naming where the user must verify separately (state overlay text, ICC A117.1, CSA B651, ABA, AOR for ambiguous fetch).
- Reminder: this is a model-code dimensional check based on the URL fetched at the timestamp shown. AOR's stamped opinion governs; AHJ confirms compliance with adopted overlays (NOT checked here).

## NA AEC conventions (enforce)

- English only.
- Imperial-first: in, ft, % slope, 1:X slope, lb force. Metric only if the source uses it.
- Slope conventions per source — `1:12`, `1:48`, `%`. Do not convert to degrees.
- AHJs named specifically: DOJ (federal ADA), CA DSA / HCAI, NYC DOB, LADBS, Toronto Building, GSA, USACE. Never "the AHJ" generically.
- Floor labels: Level 3 / L3 / 3rd floor. Never 3F.
- Roles: Architect of Record (AOR), Accessibility Consultant, Code Consultant. Never "Director" as a project role.

## Constraints

- **Never recall ADA values from training.** For every dimensional limit the workflow MUST WebFetch (or accept user paste) and quote the SourceURL. If a fetch fails and the user cannot paste, write `Status: input missing` with `Remarks` naming what to look up.
- **Always confirm with the user before WebFetch**, unless blanket "fetch all" was given in Step 1.
- **Source URL is mandatory in every output row.** A row without `SourceURL` is invalid.
- **Comparison is inline (Claude does it).** No script, no hardcoded limits, no bundled tables.
- **No bundled files.** This command's body is the only artifact; no `references/`, `scripts/`, or `assets/`.
- **State overlays are out-of-scope.** Do not paste / fetch CA 11B, ICC A117.1, NYC LL58 inside this command — flag in the out-of-scope report and the user runs a separate check.
- **Caveat block always present.** Including for trivial PASS results.

## Anti-patterns

- Filling a `Required` cell from training-data recall instead of a WebFetch quote. Even values "everyone knows" (32" door, 1:12 ramp) MUST be confirmed live.
- Fetching without first asking the user (unless blanket OK was given).
- Auto-converting source units (`1:12` → `~8.3% / ~5°`) — quote the source as-is.
- Treating "no overlay text" as "federal applies, fine" for a CA project — incomplete; flag in out-of-scope.
- Re-introducing a `references/ada-2010.md` of transcribed ADA text — deliberately none.
- Re-introducing a `check_ada.py` with hardcoded clearance constants — deliberately none.
- "Looks fine" / "should be OK" hedging — verdicts are binary against quoted source: PASS / FAIL / MARGINAL.
- Running `ada-tracker` or `/explain-code` from inside this command — pointer-only.

## Resources

None. This command is intentionally body-only — see "Why this pattern" above. Output files (CSV, markdown) are written directly with Write at the user's chosen path.
