---
title: Lookup CSI
summary: Find the spec section number for a product or scope
discipline: construction-admin
tags: ["Compliance"]
description: Look up a CSI MasterFormat 2020 section number for a product, scope, or work category — user picks Standard (CSI public preview / publisher's Numbers and Titles list) or Own Source (project spec book, company spec library, indexed MasterFormat PDF); verbatim quote + SourceURL. Carries no MasterFormat values internally.
argument-hint: <product-or-scope-keyword>
---

# Lookup CSI

Retrieve a CSI MasterFormat 2020 section number — `XX YY ZZ — Title` — for a product, scope, or work category, from a source the **user authorizes**. No internal MasterFormat values; every output row cites a verbatim quote with a SourceURL.

For plain-English interpretation of an actual spec section, use `/explain-spec`. For a full spec audit, use the `spec-review` skill.

## Inputs the command needs

1. **Product or scope keyword** — name what is being specified. Examples:
   - `air barrier — fluid-applied membrane`
   - `aluminum-framed entrance and storefront`
   - `metal panel rainscreen`
   - `EPDM single-ply roofing`
   - `gypsum board assemblies`
   - `acoustic ceiling panels`
   - `carpet tile`
   - `chilled-water piping`
   - `LED interior lighting`
   - `low-voltage structured cabling`
2. **Division hint (optional)** — if the user already knows the division: `Div 03 — Concrete`, `Div 07 — Thermal & Moisture`, `Div 08 — Openings`, `Div 09 — Finishes`, `Div 23 — HVAC`, `Div 26 — Electrical`, `Div 27 — Communications`, `Div 28 — Electronic Safety & Security`. Narrows the search.
3. **Spec format** — `MasterSpec` (AIA), `ARCAT`, `SpecLink+`, `4specs`, project custom. Different libraries may sub-divide differently below the `XX YY ZZ` level.

## Step 1 — Source preference (always ask first)

Tell the user, all at once:

> "Where should I retrieve the CSI section number from?
> (a) **Standard** — `CSI public preview` (limited free pages at `https://www.csiresources.org/`) and the `CSI Numbers and Titles` reference list. Note: the full `MasterFormat 2020` publication is paywalled, so paste preferred for precise sub-section numbers.
> (b) **Your own source** — paste from a project spec book, your company's spec library (`MasterSpec`, `ARCAT`, `SpecLink+`), a locally indexed MasterFormat PDF, or a manufacturer's spec listing.
> (c) **Both** — fetch standard preview AND check your source; report any divergence (sub-section numbering can differ by spec library).
>
> Pick (a), (b), or (c)."

The command does not proceed without an explicit pick. Because `MasterFormat 2020` is paywalled, **(b) Your own source** is typically the higher-confidence path for sub-section precision.

## Step 2 — Acquire source

- **(a) Standard fetch** — WebFetch `https://www.csiresources.org/` with the keyword. Where the public preview is sufficient (division + level-2 group), quote the verbatim listing. For sub-section precision, ask the user to paste from their licensed `MasterFormat` access.
- **(b) Own source** — accept paste from the user's spec library, or accept a user-provided URL on confirmation. Quote verbatim.
- **(c) Both** — execute (a) and (b); present both quotes; flag any divergence (especially below level 3 — `XX YY ZZ`).

If a fetch returns a paywall (most `MasterFormat` content is licensed), fall back to: WebSearch `<keyword> CSI MasterFormat 2020 section site:csiresources.org OR site:arcat.com OR site:masterspec.com` → ask user to confirm match → ask user to paste from their access.

## Step 3 — Output

```markdown
# Lookup CSI — [Product or scope, plain title]

**Keyword:** [air barrier — fluid-applied membrane]
**Division hint:** [Div 07 — Thermal & Moisture / unspecified]
**Spec format:** [MasterSpec / ARCAT / SpecLink+ / custom / unspecified]
**Source preference:** [(a) CSI preview / (b) own source — name / (c) both]

## Reference area
CSI MasterFormat 2020 — `Numbers and Titles`. CSI public preview at `https://www.csiresources.org/`. Manufacturer-specific section assignments may vary slightly across `MasterSpec`, `ARCAT`, and `SpecLink+`.

## Source quote
> [Verbatim section number + title — e.g., `07 27 26 — Fluid-Applied Membrane Air Barriers`. Quote the listing block as printed in the source.]

(Source: WebFetched from `<URL>` on <YYYY-MM-DD> / pasted by user from <doc>)

## Section table
| Field | Value (per quoted source) |
|---|---|
| Section number | `XX YY ZZ` |
| Section title | "<verbatim>" |
| Division | "<verbatim, e.g., 07 — Thermal and Moisture Protection>" |
| Level-2 group | "<verbatim, e.g., 07 20 — Thermal Protection>" |
| Level-3 (if shown) | "<verbatim, e.g., 07 27 — Air Barriers>" |
| Scope notes | "<verbatim, if printed>" |
| Source year / edition | "<verbatim, e.g., MasterFormat 2020>" |

## Divergence (if (c))
- [Bullet — any section# / title difference between CSI preview and own source. Spec libraries (`MasterSpec`, `ARCAT`, `SpecLink+`) can sub-divide below level 3 differently.]

## Caveats
- This is a section-number retrieval, not a spec edit. The Architect of Record assigns section numbers and stamps the project spec; this command does not modify or generate spec content.
- `MasterFormat 2020` is the current edition. Older projects may reference `MasterFormat 2018`, `MasterFormat 2016`, or `MasterFormat 2010` — verify the project's spec base year before using a 2020 number on a legacy project.
- Sub-section precision (below `XX YY ZZ`) often varies by spec library. Use the user's project / company library for sub-section, not a generic `MasterFormat` lookup.
- For an actual spec section's content, use `/explain-spec`.
- Binding interpretation is the AOR's stamped spec book.
```

## NA AEC conventions (enforce)

- English only.
- CSI section format `XX YY ZZ` — six digits, single spaces, no periods, no dashes between digit groups. Examples: `07 27 26`, `08 11 13`, `09 30 13`, `23 21 13`, `26 51 13`. Never `07.27.26` or `7-27-26`.
- Imperial-first throughout (although CSI numbers are dimensionless).
- Codes / standards: `CSI MasterFormat 2020`, `CSI SectionFormat / PageFormat 2020`. Reject `KBC`, `KS`, `EN`, `BS`, `JIS`, `DIN`.
- Spec libraries / publishers: `MasterSpec` (AIA), `ARCAT`, `SpecLink+`, `4specs`. Manufacturer-spec sources cited per library.
- AHJs named when the spec section interacts with a code-driven product (e.g., NYC FDNY-listed materials, CA HCAI seismic anchorage): `NYC DOB`, `LADBS`, `DSA`, `CA HCAI`, `Toronto Building`, `NYC SCA`. Never `the AHJ` or `the city`.
- Floors: Level 3 / L3 / 3rd floor. Never `3F`.
- Roles: Architect of Record (AOR), Spec Writer, Engineer of Record (EOR), MEP Engineer. Never `Director` as a project role.

## Constraints

- Never invent CSI section numbers from recall.
- Never paraphrase the section title — verbatim only.
- Always ask the source-preference question at Step 1; do not skip.
- Never claim sub-section precision (below `XX YY ZZ`) from recall — sub-section numbering varies by spec library.
- Always include the SourceURL + timestamp.
- Always state the `MasterFormat` edition (2020 vs older) when known.
- Caveat block always present.
- Markdown only. No Word / PDF.

## Anti-patterns (never do)

- Stating "air barriers are 07 27 26" from recall — never. The section # comes from a fetch or paste.
- Asserting sub-section numbers (`07 27 26.13`) from recall — sub-sections vary by spec library and edition.
- Treating `MasterFormat 1995` legacy 5-digit numbers as equivalent to `MasterFormat 2020` 6-digit (`07 27 26` ≠ `07270`).
- Auto-fetching from manufacturer marketing pages as the source — `MasterFormat` is the publisher of record.
- Auto-fetching without explicit user authorization.
- Skipping Step 1 (source preference question) — never.
- Running `/explain-spec` from inside this command — pointer-only.
