---
title: Test Egress
summary: Check one egress question - pass, fail, or marginal
discipline: code-life-safety
tags: ["Compliance"]
description: Single-question egress gut-check (occupant load, exit count, common path, travel distance) — user pastes or authorizes fetch of operative § text; PASS / FAIL / MARGINAL with explicit attribution. Carries no IBC values internally.
argument-hint: <egress-element> <provided-values> [jurisdiction]
---

# Test Egress

Single-element egress gut-check — one question on occupant load, exit count, common path of travel, or travel distance — against IBC text the **user supplies**.

**This command does not carry IBC values.** Every limit cited in the output is a verbatim quote from text the user pasted, or text the command fetched from an explicitly-named official URL with the user's authorization. The output makes the source of every number explicit.

For a multi-element life-safety pass, use the `code-compliance-review` skill. For plain-English interpretation of a single § with no math, use `/explain-code` with `code = IBC`.

## Inputs the command needs

1. **Egress element** — name the single question under test:
   - Occupant load (area + occupancy + function category → load)
   - Exit count (occupant load + story → 1 vs 2 vs 3+ exits)
   - Common path of travel (proposed `ft` vs limit by occupancy + sprinklered)
   - Travel distance (proposed `ft` vs limit by occupancy + sprinklered)
   - Dead-end corridor (proposed `ft` vs limit)
   - Stairway capacity / door clearance (geometry — see `/test-stair`)

2. **Provided values** — what the design has, with labels:
   - Area `sf` (gross / net) and function category
   - Occupant load (count)
   - Travel distance `ft` from remotest point to exit
   - Common path `ft`
   - Story (`Level 1` at grade vs `L2`+)
   - Sprinklered (`NFPA 13`, `NFPA 13R`, `NFPA 13D`, or non-sprinklered)

3. **Occupancy group** — `IBC` Ch. 3 group letter (`A-1` … `A-5`, `B`, `E`, `F-1`/`F-2`, `H-1` … `H-5`, `I-1` … `I-4`, `M`, `R-1` … `R-4`, `S-1`/`S-2`, `U`). Mixed occupancy must be tested per function.

4. **Jurisdiction** — base IBC always applies. Verify the jurisdiction-adopted edition with the AHJ. If a stricter overlay is in scope, name it:
   - NYC BC (Ch. 10 amendments to base IBC)
   - California Building Code Part 2 (CA edition of IBC)
   - DSA — K-12 schools
   - CA HCAI — hospitals
   - NYC SCA — public schools
   - Boston Building Code
   - Ontario Building Code Part 3 — Canadian projects (different framework, not IBC)

5. **Source for the operative § text** — one of:
   - **Paste** the verbatim § text. Include the citation header as it appears in the source (e.g. `IBC 2024 §1006.3.2 — Egress from Stories or Occupied Roofs`).
   - **Fetch online** — explicitly authorize the command to WebFetch from an official source. ICC editions are paywalled; AHJ amendment pages are typically free:
     - NYC BC: `https://www.nyc.gov/site/buildings/codes/2022-construction-codes.page`
     - California Building Code: `https://codes.iccsafe.org/codes/california` (often paywalled — paste preferred)
     - OBC 2024: `https://www.ontario.ca/laws/regulation/240163`
   - **local RAG index** — if the relevant code is indexed in the workspace's local RAG, route there.

   The command refuses to compute against recalled values. If no source is in hand and a fetch is not authorized, it stops and asks.

## Workflow

1. **Echo parsed inputs** in one line: egress element / provided values / occupancy / jurisdiction.
2. **Identify the reference area** — point at the chapter / division of the relevant code for the user's egress question (e.g., "IBC Ch. 10 — Means of Egress"). Do **not** claim a specific § number from recall.
3. **Acquire source text:**
   - If the user pasted text in the request, use that.
   - Otherwise ask: "Paste the operative § text, or say 'fetch from [NYC BC / OBC 2024 / etc.]'."
   - On 'fetch', WebFetch the named official URL, quote the operative paragraph(s) verbatim, and ask the user to confirm this is the correct § for the question before proceeding.
4. **For overlay jurisdictions** (NYC BC, CBC, OBC, DSA, CA HCAI) require the overlay text in addition to base IBC. A NYC project compared only against base IBC is incomplete — say so and stop until the overlay text is provided or the user explicitly opts out.
5. **Math against verbatim source.** For each provided value, quote the matching clause from the source text (blockquoted), state the comparison, label PASS / FAIL / MARGINAL, and report the margin.
6. **Output** the table + source attribution + caveats.

## Output template

```markdown
# Test Egress — [Element, plain title]

**Element:** [occupant load / exit count / common path / travel distance / dead-end]
**Provided:** [labeled values]
**Occupancy:** [B / R-2 / A-3 / etc.]
**Jurisdiction:** [base IBC 2024 / + NYC BC / + CBC / + OBC / etc.]

## Reference area
[Topic-level pointer to chapter / division of the relevant code. No specific § from recall.]

## Source text under test
> [Verbatim quote from user paste or fetched URL. Preserve the source's own citation header.]

(Source: pasted by user / fetched from <URL> on <YYYY-MM-DD>)

## Comparison
| Value | Provided | Required (per quoted source) | Verdict | Margin |
|---|---|---|---|---|
| ... | ... | "<verbatim limit>" | PASS / FAIL / MARGINAL | ... |

## Jurisdictional flags
- [If overlay in scope and overlay source provided: include overlay row in the table with overlay column.]
- [If overlay in scope but overlay source missing: list the overlay § the user must also paste / fetch. Do not math against base IBC alone.]

## Caveats
- Single-element gut-check; not a life-safety audit. Use `code-compliance-review` for full project egress scoping.
- All limit values come from the source the user pasted or the URL the command fetched on <date>. The command did not recall any IBC value from training.
- IBC editions and AHJ amendments change. Verify the source edition matches the jurisdiction-adopted edition.
- Binding interpretation is the AOR's stamped opinion plus AHJ review (`NYC DOB Code Determination`, `LADBS Information Bulletin`, `DSA Interpretation of Regulations`, etc.).
```

## NA AEC conventions (enforce)

- **English only** — body, examples, output.
- **Imperial-first** units: `ft`, `in`, `sf`. Metric only if it appears verbatim in the source text.
- **Codes / standards referenced:** IBC, IRC, IFC, NFPA 101, NFPA 13, NFPA 13R, NFPA 13D, NYC BC, CBC, OBC, NBC. Reject `KBC`, `KS`, `EN`, `BS`, `JIS`, `DIN` — out of catalog scope.
- **AHJs named specifically:** NYC DOB, FDNY, LADBS, DSA, CA HCAI, NYC SCA, Boston ISD, Toronto Building, Chicago DOB, GSA, USACE. Never `the AHJ` or `the city` generically.
- **Floors:** Level 3 / L3 / 3rd floor. Never `3F`.
- **Roles:** Architect of Record (AOR), Code Consultant, Expediter (NYC), Owner, Owner's Representative. Never use `Director` as a project role.

## Constraints

- **Never invent IBC values.** If the user has not pasted source text and has not authorized a fetch, stop and ask.
- **Never paraphrase from training.** The source text in the output must be a verbatim quote from user paste or WebFetch result, blockquoted, with the source's own citation header preserved.
- **Never claim a specific § number from recall.** Topic-level pointers (chapter / division) are fine; the specific § (`§1006.3.2`, `Table 1004.5`, etc.) must come from the source.
- **Distinguish base IBC from AHJ overlay.** A NYC / CA / Toronto project that pasted only base IBC is incomplete — flag and stop until overlay text is provided or explicitly waived.
- **Single question, single shot.** Multi-element life-safety scoping is `code-compliance-review` skill territory.
- **No `docs/` artifact, no Word / PDF, no `aec-doc-gen` dependency.** Markdown response only.
- **Caveat block always present.** Including for trivial PASS results.
- **Fetch only after explicit user authorization.** Always show the URL fetched and the date.

## Anti-patterns (never do)

- Stating limit values inline ("75 ft common path for B sprinklered") — never. Numbers live only in the quoted source.
- Claiming "`§1006.3.2` says one exit allowed up to 49 occupants" from training — never. The pasted / fetched source is the only authority.
- Treating "no overlay text" as "base IBC applies, fine" for jurisdictions where the overlay governs (NYC, CA, Toronto) — incomplete by definition.
- Auto-fetching without explicit user authorization — fetch only on an explicit "fetch online" cue.
- "Looks fine" / "should be OK" hedging — verdicts are binary against quoted source: PASS / FAIL / MARGINAL.
- Running `code-compliance-review` or `/explain-code` from inside this command — pointer-only; the user invokes downstream.
- Mixing occupancy functions in a single test (e.g., assembly + business in one math row) — split per function and sum per the source's own rules.
