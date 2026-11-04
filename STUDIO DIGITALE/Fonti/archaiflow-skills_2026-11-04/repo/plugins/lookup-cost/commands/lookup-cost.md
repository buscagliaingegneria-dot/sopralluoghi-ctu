---
title: Lookup Cost
summary: Look up a cost-per-square-foot benchmark, quoted with its source
discipline: construction-admin
tags: ["Compliance"]
description: Look up a $/sf cost benchmark for a building type or scope — user picks Standard (GSA P-100, Turner / Mortenson / RLB indices, federal benchmarks) or Own Source (RSMeans paste, GC quote, in-house cost database, indexed PDF); verbatim quote + SourceURL. Carries no $/sf values internally.
argument-hint: <project-type-and-region> [year] [scope]
---

# Lookup Cost

Retrieve a $/sf benchmark for a building type, scope, or assembly — from a source the **user authorizes**. No internal cost values; every output row cites a verbatim quote with a SourceURL.

This command is a benchmark retriever, not an estimator. For full cost estimation, engage a cost consultant or use a licensed `RSMeans` / `Gordian` / `CostX` tool. For payment application work, use `/draft-payment-application`.

## Inputs the command needs

1. **Project type** — name as the source categorizes:
   - Federal: GSA building category (`PBS Lab`, `PBS Office`, `PBS Court`), USACE category code
   - Commercial: `office Class A high-rise`, `medical office building`, `hospital acute care`, `school K-12`, `lab BSL-2`, `data center Tier III`, `multifamily Type V wood`, `multifamily Type I concrete`, `industrial warehouse`, `parking structure precast`
   - Civil: `roadway widening per lane-mile`, `pedestrian bridge per linear foot`
2. **Region** — North-American region or specific city: `Northeast US`, `Bay Area CA`, `Houston TX`, `Toronto ON`, `Pacific Northwest`. Cost varies materially by region.
3. **Year** — base year for the index (`2026`, `2025`, `2024`). Cost-index values escalate annually; the source year matters.
4. **Scope** — `total project cost (TPC)`, `construction hard cost only`, `construction + soft cost`, `tenant improvement only`, `core and shell only`, `building cost (without site work)`. The benchmark unit changes by scope.

## Step 1 — Source preference (always ask first)

Tell the user, all at once:

> "Where should I retrieve the cost benchmark from?
> (a) **Standard** — public federal benchmarks: `GSA P-100` (Federal Buildings Performance Standards, free), `GSA PBS Funded Projects` historical data, `USACE Pax Newsletter`, `RLB International Construction Cost Report` (free annual), `Turner Building Cost Index` (free quarterly), `Mortenson Cost Index` (free quarterly). I will WebFetch on confirmation and quote the verbatim cost benchmark.
> (b) **Your own source** — paste from `RSMeans Building Construction Cost Data` (paywalled, paste only), `Gordian` / `CostX` exported summary, in-house cost database, GC's recent quote, or a locally indexed cost report.
> (c) **Both** — fetch standard AND check your source; report any divergence.
>
> Pick (a), (b), or (c)."

The command does not proceed without an explicit pick. It does not WebFetch from convenience aggregators (e.g., `levelset.com`, `procore.com` cost articles) as the standard source.

## Step 2 — Acquire source

- **(a) Standard fetch** — WebFetch the named federal / public source URL with the user's keywords (project type + region + year). Quote the verbatim benchmark including unit, date, and any included scope notes. Record the fetched URL and ISO timestamp.
  - GSA P-100: `https://www.gsa.gov/real-estate/design-and-construction/engineering-and-architecture/p100-facilities-standards`
  - RLB ICCR: `https://www.rlb.com/americas/insight/`
  - Turner: `https://www.turnerconstruction.com/cost-index`
  - Mortenson: `https://www.mortenson.com/cost-index`
- **(b) Own source** — accept paste or WebFetch a user-provided URL on confirmation. Quote verbatim and record source.
- **(c) Both** — execute (a) and (b); present both quotes; flag any divergence.

If a fetch returns a paywall (most cost data is licensed), fall back to: WebSearch `<project type> $/sf <region> <year> site:gsa.gov OR site:rlb.com OR site:turnerconstruction.com` → ask user to confirm match → ask user to paste from licensed source.

## Step 3 — Output

```markdown
# Lookup Cost — [Project type, Region, Year]

**Project type:** [PBS Office / Class A office high-rise / hospital acute care / etc.]
**Region:** [Bay Area CA / Northeast US / Toronto ON]
**Year:** [2026 base year / 2025 historical]
**Scope:** [TPC / construction hard cost only / TI only / core and shell]
**Source preference:** [(a) Standard — name / (b) own source — name / (c) both]

## Reference area
GSA P-100 / GSA PBS Funded Projects historical / USACE Pax Newsletter / RLB ICCR / Turner Cost Index / Mortenson Cost Index / RSMeans (licensed, paste only).

## Source quote
> [Verbatim benchmark — cost per `sf` (or per unit), the project type as the source defines it, year of the index, region adjuster if stated, included / excluded scope notes.]

(Source: WebFetched from `<URL>` on <YYYY-MM-DD> / pasted by user from <doc>)

## Benchmark table
| Field | Value (per quoted source) |
|---|---|
| Project type | "<verbatim>" |
| Cost benchmark | "<verbatim, e.g., $850 / sf TPC>" |
| Region adjuster | "<verbatim, e.g., 1.18 for Bay Area>" |
| Year of index | "<verbatim>" |
| Scope included | "<verbatim>" |
| Scope excluded | "<verbatim>" |
| Sample size / data range | "<verbatim, if stated>" |

## Divergence (if (c))
- [Bullet — any $/sf or scope difference between standard and own source.]

## Caveats
- This is a benchmark retrieval, not an estimate. A bona fide construction estimate requires a cost consultant or licensed estimating software (`RSMeans`, `Gordian`, `CostX`).
- Cost indices escalate. Verify the source year and apply ENR Construction Cost Index (CCI) escalation if benchmarking against a future bid year.
- Region adjusters vary materially. A national $/sf without region adjustment misleads on coastal CA, NYC, and Toronto projects.
- Scope inclusions / exclusions matter. `TPC` includes soft costs; `construction hard cost` does not. `TI only` differs from `core and shell`.
- For licensed `RSMeans` access, the user must paste the relevant catalog row — RSMeans data is not free and cannot be WebFetched from public sources.
- For federal projects, `GSA P-100` is the design-quality standard, and `GSA PBS funded projects` historical is the cost benchmark; do not conflate.
- Binding cost determination is the Owner's accepted bid plus contracted change orders, not a benchmark retrieval.
```

## NA AEC conventions (enforce)

- English only.
- USD currency, `$/sf` (gross or rentable — state which). Never `$/m²`, never KRW.
- Imperial-first throughout. Region naming as the source uses (`Bay Area CA`, `Northeast US`, `Toronto ON`).
- Cost sources: `GSA P-100`, `GSA PBS funded projects`, `USACE Pax`, `RLB ICCR`, `Turner Cost Index`, `Mortenson Cost Index`, `RSMeans Building Construction Cost Data` (licensed, paste only), `Gordian` (paste only), `CostX` (paste only), `ENR Construction Cost Index` (CCI escalator). Reject `KBC`, `KS`, `EN`, `BS`, `JIS`, `DIN`.
- Federal AHJs named: `GSA`, `USACE`, `VA`, `FEMA`. State / local: `NYC SCA`, `CA HCAI`, `DSA`, `Port Authority`. Never `the AHJ` or `the city`.
- Floors: Level 3 / L3 / 3rd floor. Never `3F`.
- Roles: `Owner`, `Owner's Representative`, `Cost Consultant` (`Quantity Surveyor` in Canada), `General Contractor (GC)`, `Construction Manager (CM)`, `Project Executive`. Never `Director` as a project role.

## Constraints

- Never invent $/sf or cost values from recall.
- Never paraphrase the benchmark — verbatim only including units, year, and scope notes.
- Always ask the source-preference question at Step 1; do not skip.
- Never WebFetch from convenience aggregators or third-party cost-article sites as the standard source — federal / publisher-direct only.
- Always include the SourceURL + timestamp.
- Always state the year and region adjuster — bare $/sf without context misleads.
- Caveat block always present.
- Markdown only. No Word / PDF.

## Anti-patterns (never do)

- Stating "$850 / sf for Class A office in NYC" from recall — never. The benchmark comes from a fetch or paste.
- Conflating `TPC` with `construction hard cost only` — different by 25-40%.
- Using a national average without region adjustment for high-cost markets (Bay Area, NYC, Toronto, DC, Boston).
- Quoting `RSMeans` from training — the data is licensed; only paste from the user's licensed access.
- Auto-fetching from `levelset.com`, `procore.com`, or other convenience cost articles — not authoritative.
- Auto-fetching without explicit user authorization.
- Skipping Step 1 (source preference question) — never.
- Treating this command as an estimator — pointer to cost consultant.
