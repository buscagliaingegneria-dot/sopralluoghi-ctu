---
title: Test Fire Rating
summary: Check the required hourly rating for an element
discipline: code-life-safety
tags: ["Compliance"]
description: Single-element fire-resistance rating gut-check via IBC Table 601 + Table 602 — for each element the command WebFetches the relevant Table row live from codes.iccsafe.org (or accepts a paste) and labels the required hourly rating against the verbatim source. Carries no IBC values internally. Federal IBC only — state amendments and sprinkler-trade adjustments (§403, §504, §506) are out-of-scope.
argument-hint: <construction-type> <element> [separation-distance] [edition]
---

# Test Fire Rating

Single-element fire-resistance rating lookup against IBC Table 601 (interior structural elements + non-load-bearing walls) and Table 602 (exterior walls by separation distance) **as fetched live from codes.iccsafe.org** or as pasted by the user. The command **bundles no values** and **recalls no values** from training; every required hour rating is a verbatim quote from the source with a SourceURL.

For full code-compliance audit (construction type + height + area + sprinkler trade) use the `code-compliance-review` skill. For plain-English interpretation of a single Table use `/explain-code` with `code = IBC <edition>`. For the assembly listing (UL design number / GA file number) — out of scope here; consult UL Fire Resistance Directory or GA Fire Resistance Design Manual separately.

## Why this pattern (read first)

IBC Table 601 + 602 cells differ across IBC 2018 / 2021 / 2024 in several rows. Bundled transcriptions silently misquote when written from training-data recall (well-tracker incident, 2026-05-09). The workflow asks "should I fetch Table 601 from codes.iccsafe.org?" then WebFetches the operative row, quotes the source URL inline, and only then labels the rating.

The user MUST have a connection to the public internet during use, OR be willing to paste the relevant Table row + § text. There is no offline fallback to bundled values — by design.

## Scope and limits — read first

This command checks **IBC Table 601 + Table 602 Federal lookup** ONLY. It does NOT cover:

- **State / city amendments**: NYC BC Table 601, CA CBC Table 601, FL Building Code, MA 780 CMR amendments.
- **Sprinkler-trade adjustments** (IBC §403.3.1 high-rise, §504 height increase, §506 area increase, §510 horizontal building separation, IBC §602.4 height/area trade-off).
- **Heavy timber Type IV-A / IV-B / IV-C / IV-HT** char-rating calc per §602.4 — fetched but not computed.
- **Mass timber UL design numbers / acceptance criteria** — out-of-scope.
- **Assembly listings** (UL design / GA file / WHI / Intertek) — refer to UL Fire Resistance Directory / GA Manual.
- **Shaft / corridor / occupancy-separation rating** (Tables 509, 707, 711, 1020) — separate workflow.
- **Smoke barrier / smoke partition** (§709, §710) — separate.
- **Through-penetration / joint firestop UL listings** — separate.

State amendments and sprinkler-trade adjustments are the user's burden to verify separately. The report flags out-of-scope items.

## Authoritative sources used

| Standard | Public source |
|---|---|
| IBC 2024 | https://codes.iccsafe.org/content/IBC2024P1 |
| IBC 2021 | https://codes.iccsafe.org/content/IBC2021P2 |
| IBC 2018 | https://codes.iccsafe.org/content/IBC2018 |

If the user's jurisdiction adopted a different edition, ask for the edition first. Do not WebFetch from convenience aggregators (UpCodes, etc.) as authoritative — only codes.iccsafe.org or the jurisdiction portal.

## Inputs the command needs

1. **Construction type** — IBC §602: I-A / I-B / II-A / II-B / III-A / III-B / IV-A / IV-B / IV-C / IV-HT (IBC 2021+) / V-A / V-B.
2. **Element under test** — pick from Table 601 columns and Table 602:
   - Primary structural frame
   - Bearing walls — exterior
   - Bearing walls — interior
   - Non-bearing walls and partitions — exterior (Table 602 — separation-distance dependent)
   - Non-bearing walls and partitions — interior
   - Floor construction and associated secondary members
   - Roof construction and associated secondary members
3. **For exterior walls (Table 602)** — fire separation distance (FSD) in ft, AND occupancy group (H, F-1/M/S-1, F-2/S-2/U, A/B/E/I/R/U/L).
4. **Edition** — IBC 2018 / 2021 / 2024.
5. **Jurisdiction** — for the report only (state amendments are out-of-scope).
6. **Auto-fetch?** — "fetch all without re-asking" or per-topic confirm.

## Required citations

| Topic | IBC § (subject area) |
|---|---|
| Construction-type rating matrix | Table 601 |
| Exterior wall rating by fire separation distance | Table 602 |
| Construction type definitions | §602 |
| Heavy-timber type IV provisions | §602.4 |
| Reduction for sprinkler / height / area trade | §403, §504, §506 (out-of-scope here — flag) |

The verbatim § number + hour rating + table row comes from the source the workflow fetches or the user pastes.

## Workflow

### Step 1 — Confirm scope

> "This command looks up IBC Table 601 + Table 602 Federal only. Sprinkler-trade adjustments (§403 high-rise, §504 height increase, §506 area increase, §510 horizontal building separation, §602.4 timber char), state amendments (NYC BC, CA CBC, etc.), and assembly listings (UL / GA / WHI) are NOT covered. To proceed I need:
> 1. Construction type (I-A / I-B / II-A / II-B / III-A / III-B / IV-A/B/C/HT / V-A / V-B).
> 2. Element under test (primary frame / bearing wall / non-bearing wall / floor / roof).
> 3. For exterior walls: fire separation distance (ft) + occupancy group.
> 4. IBC edition (2018 / 2021 / 2024).
> 5. Jurisdiction (for the report only).
> 6. **Auto-fetch?** — 'fetch all without re-asking' or per-topic confirm.
>
> Continue?"

If the user describes Type IV mass-timber and wants char-rating math: stop and tell them §602.4 char calc is out-of-scope here — refer to AOR / SE / `code-compliance-review` skill.

### Step 2 — Fetch each authoritative § / Table LIVE

For Table 601 (interior elements + non-bearing partitions) and/or Table 602 (exterior walls):

1. Tell the user the topic + the constructed source URL. Example:
   > "Need IBC 2024 Table 601 (Type II-B primary structural frame rating) — should I WebFetch from `https://codes.iccsafe.org/content/IBC2024P1`?"
2. WebFetch on confirmation. On paywall / empty body, fall back: WebSearch `IBC <edition> Table 601 site:.gov OR site:iccsafe.org` → WebFetch first official-looking result. If still nothing, ask user to paste the Table row.
3. Extract the verbatim row + the source URL + a fetch timestamp. Quote the row back so the user can confirm construction type + element.
4. For Table 602: fetch the row that matches the user's occupancy group + fire separation distance bin (e.g. `< 5 ft`, `5 to < 10 ft`, `10 to < 30 ft`, `≥ 30 ft` — verify the bin labels from the fetched edition).
5. Hold the citation in memory for the lookup step. Re-use within the same session — do not re-fetch.

### Step 3 — Lookup and present the result

For each element in scope, look up the cell from the fetched Table. Present as a markdown table:

| Element | Required (hours) | Construction type | FSD bin (if Table 602) | CitedTable | SourceURL | FetchedAt | Confidence | Remarks |
|---|---|---|---|---|---|---|---|---|

Where:
- `Required` — verbatim hourly rating from the cell (e.g. `1`, `2`, `3`, `0`, `0a`).
- `Construction type` — user input.
- `FSD bin` — fire separation distance bin from Table 602, only if exterior wall.
- `CitedTable` — e.g. `IBC 2024 Table 601` or `IBC 2024 Table 602`.
- `SourceURL` — the URL returned by WebFetch.
- `FetchedAt` — ISO timestamp.
- `Confidence` — `high` (cell verbatim, type + element clear), `medium` (FSD bin near boundary), `low` (occupancy group ambiguous).
- `Remarks` — table footnotes (e.g. `0a` superscript exception), sprinkler-trade reminder, mass-timber char reminder.

### Step 4 — Optional persistence

After the inline table, ask:
> "Save this as a file? (a) markdown, (b) CSV, (c) both, (d) inline only. Path?"

Default suggested path `docs/code/<project-id>-fire-rating.{csv|md}` if save chosen.

### Step 5 — Report

After the table:
- Per-element required hours from the cited Table.
- Footnote reminders preserved verbatim from the source.
- Out-of-scope reminders:
  - Sprinkler-trade adjustments (§403, §504, §506, §510) — separate workflow.
  - Mass-timber char calc (§602.4) — refer to AOR / SE.
  - Assembly listings (UL / GA / WHI) — Architect/SE picks compliant assemblies separately.
  - State amendment overlay (NYC BC, CA CBC, etc.) — user verifies.
  - Shaft / corridor / occupancy-separation rating (Tables 509, 707, 711, 1020) — separate.
- Reminder: this is a model-code Table lookup. AOR's stamped opinion governs; AHJ confirms compliance with adopted overlays + sprinkler-trade calcs (NOT checked here).

## NA AEC conventions (enforce)

- English only.
- Construction type as IBC publishes (`II-B`, `IV-A`, `V-B`) — not `Type 2B`, `Type IV-A`.
- IBC § format: `IBC 2024 §602.4` / `IBC 2024 Table 601`. Never "table 601" generically.
- AHJs named specifically: NYC DOB, FDNY, LADBS, DSA, Toronto Building, GSA, USACE.
- Roles: Architect of Record (AOR), Structural Engineer of Record (SEOR), Code Consultant.
- Imperial-first: ft, in, hr (rating in hours).

## Constraints

- **Never recall IBC Table 601 / 602 cells from training.** Verbatim row from WebFetch or user paste only.
- **Never paraphrase the cell.** A cell of `0a` (zero hours, footnote a) must appear as `0a` not "0 hr exception".
- **Preserve table footnotes.** They're load-bearing.
- **Source URL is mandatory in every output row.**
- **Sprinkler-trade adjustments are out-of-scope.** Do not attempt to apply §403 / §504 / §506 reduction — flag in report.
- **No `docs/` artifact unless user opts in.**
- **Caveat block always present.**
- **Fetch only after explicit user authorization.**

## Anti-patterns

- Stating an hour rating inline ("Type II-B exterior bearing wall is 0 hours") — never. Quote the cell verbatim.
- Auto-applying sprinkler reduction or mass-timber char rating — out-of-scope; flag.
- Re-introducing a `references/ibc-table-601.md` of transcribed cells — deliberately none.
- Quoting Table 601 from a different edition than the user's adopted edition.
- Missing footnote letters (`0a`, `1b`) — they encode exceptions; preserve verbatim.
- Conflating Table 601 (interior) with Table 602 (exterior FSD-dependent) — different cells.
- Treating Type IV-A / IV-B / IV-C as the same as Type IV-HT — IBC 2021+ split them; verify edition.
- Computing assembly listings (UL design number, GA file) — refer to AOR / `code-compliance-review`.
- "1-hour fire-rated should be fine" — never. Quote the cell, label the actual rating.

## Resources

None. This command is intentionally body-only — see "Why this pattern" above.
