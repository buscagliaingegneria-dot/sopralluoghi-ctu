# Bid Benchmarks — Pointer Reference (NA)

This file does **not** contain $/sf or unit-price numbers. Concrete numbers age fast (RSMeans publishes quarterly; ENR CCI moves monthly; regional firms publish annually) and reciting them from memory is how silent errors enter a bid review. Instead, this file points to the publishers you should pull current values from, and gives a worked-example *format* for laying out a benchmark row inside a review.

If you find yourself about to write "$130 per CY for rock excavation" with no citation: stop, open RSMeans (or the regional firm's published market report), and quote the value with the source + edition.

---

## Where to pull current numbers (2026)

### $/sf turnkey construction cost benchmarks

- **RSMeans** — *Square Foot Costs with RSMeans Data*, current edition. Granular by building type, location-factored to MSA / 3-digit ZIP. The default for project sizing on private work.
- **Gordian** (RSMeans publisher) — quarterly update bulletins; CCI escalation series.
- **GSA P-100** — *Facilities Standards for the Public Buildings Service*, current edition. Federal courthouse / federal office benchmarks; useful even on non-federal civic work as a reference point.
- **AIA Compensation & Benchmarking Surveys** — fee benchmarks, not construction cost, but useful when the bid review is paired with fee-spread analysis.

### Cost escalation indices (apply to historical benchmarks)

- **ENR Construction Cost Index (CCI)** and **Building Cost Index (BCI)** — monthly. Use to escalate a published benchmark from its publication date to the bid date.
- **Bureau of Labor Statistics PPI** — *Inputs to Construction Industries* series. More volatile than ENR but closer to actual material movement.
- **Turner Building Cost Index** — quarterly; major-market focus.
- **Mortenson Cost Index** — quarterly market reports for Minneapolis, Phoenix, Denver, Chicago, Milwaukee, Seattle.

### Regional / market-specific benchmark publishers

- **Mortenson** — quarterly *Construction Cost Insights*.
- **Turner Construction** — quarterly *Building Cost Index* commentary.
- **Skanska** — annual / semi-annual *Market Insight* reports by US region.
- **Cumming Group** — quarterly *Market Cost Reports* (national + city detail).
- **Rider Levett Bucknall (RLB)** — quarterly *North America Report* with city-by-city construction cost movement.
- **NYC SCA** — published K-12 benchmarks for NYC public schools.
- **CA OPSC / DSA** — published benchmarks for CA K-12 / community college; also DSA-approval cost premium tracking.
- **GSA** — federal building benchmarks.
- **USACE** — civil works unit-cost guidance (PCC, MCACES).

### Public bid-tab data (real awards, not benchmarks)

- **State / agency bid-tab archives** — many state DOTs (Caltrans, NYSDOT, FDOT, TxDOT) publish full bid tabs. Excellent unit-price reality check for civil / earthwork / paving.
- **NYC SCA bid history** — public school awards.
- **CA HCAI** — hospital / clinical project costs (filed under OSHPD legacy tracking).

---

## Sections you would populate locally (with sourced values)

When a project actually needs a benchmark sheet, create one inside the project's review folder (`docs/bids/<slug>-benchmarks.md`) and populate the sections below from the publishers above. **Do not populate them in this file.** Leaving this file source-only protects against stale values being treated as authoritative.

- Construction $/sf benchmarks — by typology and region
- Earthwork $/CY benchmarks — by site condition (open / constrained / urban)
- Concrete & rebar — placed CY, lb-installed
- Structural steel — adjustment $/lb erected, fireproofing $/sf surface
- Envelope — storefront, curtain wall, brick, IMP, roofing
- MEP — $/gsf served by trade (HVAC, plumbing, fire, electrical, low-voltage)
- GC overhead and profit % — typical ranges by project size and delivery method
- Long-lead at-risk premium % — by item (switchgear, AHU, custom curtain wall, elevators)
- Bonding cost — % of contract value, by surety market

---

## Worked-example row format

When recording a benchmark row inside a project's local benchmark sheet, use this format. Each row is a published value, never a recalled value.

```
| Item | Range / value | Unit | Source | Edition / date | Region | Notes |
|---|---|---|---|---|---|---|
| Rock excavation, open access | <published low>-<published high> | $/CY | RSMeans Heavy Construction Cost Data | 2026 Q1 | RCI <factor> for <MSA> | Excludes blasting; add for confined |
| Curtain wall, mid-spec unitized | <published low>-<published high> | $/sf | Cumming Group Market Cost Report | 2026 Q1 | Northeast | Custom adders separate |
| Class A office mid-rise turnkey | <published low>-<published high> | $/gsf | RSMeans Square Foot Costs | 2026 Q1 | RCI 122 (NYC) | Excludes land, soft costs, FF&E |
```

Required columns:

1. **Item** — what is being measured.
2. **Range / value** — the published number(s). Always a range when the source publishes a range; never a single point if the source did not.
3. **Unit** — explicit ($/CY, $/sf, $/lb, $/gsf, %, etc.).
4. **Source** — the publisher and product name.
5. **Edition / date** — quarter and year, or specific publication date.
6. **Region** — RCI factor + MSA, or named region from the publisher.
7. **Notes** — exclusions, conditions, escalation applied.

---

## How to apply (when local benchmarks have been populated)

When a bidder's unit price is **outside** the published range:

- **Above the published range**: contractor is loading the unit price as overrun-recovery or hedging unknown scope. Typical responses: negotiate down to the range, accept with a written cap, or require a basis-of-quote.
- **Below the published range**: contractor is wagering on no-overrun or has misread scope. Typical response: clarify scope before award; require basis-of-quote.
- **Within range**: typical; no flag unless other axes raise concern.

When the leveled bid is **outside** the typology $/sf range:

- 10-20% above: scope creep, region premium, or alternates carried in. Investigate.
- More than 20% above: scope misalignment or speculative pricing. Re-bid or re-scope.
- 10-20% below: hungry-for-backlog or aggressive bid. Verify qualifications, bonding, and SOV front-loading.
- More than 20% below: high abandonment or claims-recovery risk. Treat as non-responsive in spirit pending clarification.

These thresholds are conventions; the publisher's commentary on a given quarter often changes them (e.g., during 2021-2022 supply-shock periods, "above range" was nearly universal and the threshold widened).

---

## Why this file does not list values

Concrete benchmark values from recall are how the well-tracker incident happened (`MEMORY/feedback_standards_verification.md`, 2026-05-09). Every recalled scorecard concept was wrong. The same failure mode applies here: $/sf and $/CY values vary by quarter, by RCI, by site condition, and a single hallucinated point in a bid-review memo gets weaponized in a negotiation. Source it or omit it.
