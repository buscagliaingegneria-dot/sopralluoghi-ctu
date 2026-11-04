# Phasing Patterns

Common phasing patterns for decarbonization roadmaps. The phasing logic (Year 0 / 1–3 / 4–7 / 8–15) is **internal to this skill — synthesized from RMI Reinventing Existing Buildings, Building Decarbonization Practice Guides, ULI Net Zero Imperative, Architecture 2030 Roadmap to Zero, and AIA Owner's Guide to Decarbonization.**

---

## Pattern A — Existing commercial building under cap-mandate pressure (LL97, BERDO, BEPS)

**Profile:** Mid-to-large commercial / office / multifamily; existing fossil-fired HVAC; baseline EUI 80–150 kBtu/sf/yr; mandate cap pressure within 5–10 years.

| Phase | Year | Scope | Capex profile |
|-------|------|-------|---------------|
| Year 0 — No-regret | Now | Benchmarking submission; investment-grade audit; controls / BAS optimization; lighting LED retrofit; low-cost air sealing; sub-metering for LL97 reporting | Low |
| Year 1–3 — Envelope + planning | 1–3 | Envelope assessment + design + permit; equipment-end-of-life inventory; electrification feasibility; utility electrical-capacity confirmation; tax counsel + IRA strategy | Medium |
| Year 4–7 — Major retrofit | 4–7 | Envelope construction; HVAC partial electrification (heat pumps for major zones); DHW electrification; on-site PV; BESS for resilience + demand-charge management | High (the bulk of the capex) |
| Year 8–15 — Closing the gap | 8–15 | Full HVAC electrification (remaining zones); cooking electrification (multifamily); off-site PPA / RECs to close residual; final benchmarking confirms cap compliance | Medium |

**Mandate pacing:** This pattern targets NYC LL97 Compliance Period 2 (2030–2034). Building-decarb capex needs 2–4 years lead time; pre-2030 buildings should start Year 0 by 2025 to confidently land Period 2 cap compliance.

---

## Pattern B — Existing institutional / federal / public-sector building

**Profile:** University, K-12, hospital, federal / state / municipal building; long ownership horizon; capex constrained but predictable; design-bid-build delivery; multi-year capital budget.

| Phase | Year | Scope | Capex profile |
|-------|------|-------|---------------|
| Year 0 — Plan + benchmark | Now | Building portfolio benchmark; capex prioritization; AIA 2030 / SE 2050 reporting (if signatory); IRA §179D allocation strategy (designer) | Low |
| Year 1–5 — Capital-cycle envelope + controls | 1–5 | Envelope improvements during deferred-maintenance cycles; BAS retrofit; lighting; occupancy-sensor controls; commissioning | Medium |
| Year 6–10 — Major MEP / electrification | 6–10 | HVAC electrification at equipment EOL; central plant electrification (geothermal where feasible); on-site PV at scale | High |
| Year 11–15 — Renewables + closing | 11–15 | Cooking + lab equipment electrification; community-solar / PPA; site decarbonization | Medium |

**Mandate pacing:** Federal Executive Order 14057 targets 65% emission reduction by 2030; net-zero by 2045. Federal facilities Year 0 should be 2024 to land 2030 milestone.

---

## Pattern C — New construction with carbon-target OPR

**Profile:** New office / multifamily / institutional with owner's stated decarb target (LEED Gold + Platinum, PHIUS+, net-zero, 2030 Challenge target).

| Phase | Year | Scope | Capex profile |
|-------|------|-------|---------------|
| Year 0 — Pre-design | Now | OPR + carbon target; embodied-carbon LCA scoping; passive design strategy; energy-modeling consultant onboarded; IRA §179D + §48 strategy | Low (consultant fees) |
| Year 1 — SD + DD | 1 | Envelope-load reduction in design; HVAC sizing post-envelope; on-site PV layout; embodied-carbon LCA at SD; concrete + steel low-carbon spec at DD | Medium (design + LCA modeling) |
| Year 1–2 — CD + permit | 1–2 | Code compliance (Title 24 / IECC + state); benchmarking pre-submission; LEED / PHIUS / 2030 documentation in CDs | Medium |
| Year 2–3 — Construction | 2–3 | Construction with low-carbon concrete + EPD steel; commissioning at SC; benchmarking enrollment at TCO | High |
| Year 3–5 — Post-occupancy | 3–5 | Whole-building commissioning (Cx); benchmarking submission (LL84 / BERDO / etc.); energy-model calibration to actual; AIA 2030 reporting | Low |

**Mandate pacing:** Title 24 cycle effective at permit; benchmarking effective at TCO + 1 year typically.

---

## Pattern D — Adaptive reuse / major renovation

**Profile:** Existing building converted to new use; structure retained; envelope + MEP retrofit substantial; embodied-carbon advantage is the key narrative.

| Phase | Year | Scope | Capex profile |
|-------|------|-------|---------------|
| Year 0 — Feasibility | Now | Structural + envelope condition assessment; LCA comparison (retain-vs.-replace); zoning + code-of-occupancy confirmation; IRA §179D + §48 strategy | Low |
| Year 1–2 — Design | 1–2 | Envelope retrofit + new MEP; electrification first; on-site PV; embodied-carbon LCA confirms retain-vs.-replace; 2030 Challenge documentation | Medium |
| Year 2–4 — Construction | 2–4 | Retrofit construction; commissioning; benchmarking enrollment | High |
| Year 4+ — Operations | 4+ | Benchmarking; tuning; subsequent capex per code-cycle | Medium |

**Mandate pacing:** Renovation triggers mandate applicability — confirm threshold (% replacement, sf affected) crosses or stays below the line per IBC + state amendments + LL97 / BERDO threshold rules.

---

## Pattern E — Portfolio-wide owner-side strategy

**Profile:** Owner with multiple buildings (REIT, university, hospital system, K-12 district, federal agency); annual capex budget; portfolio-wide net-zero or carbon-cap target.

| Phase | Year | Scope | Capex profile |
|-------|------|-------|---------------|
| Year 0 — Portfolio audit | Now | Benchmark every building in Portfolio Manager; rank by carbon impact + cap-pressure exposure; group capex schedules | Low |
| Year 1–3 — Tier 1 (highest-impact) | 1–3 | 5–10 buildings of largest carbon impact; full Pattern A | High |
| Year 3–7 — Tier 2 | 3–7 | Mid-tier buildings; envelope + controls + electrification | Medium-High |
| Year 7–15 — Tier 3 + finishing | 7–15 | Smaller buildings + portfolio closure; PPA / RECs to close residual | Medium |

**Mandate pacing:** Portfolio sequencing typically prioritizes mandate-exposed buildings first (LL97-applicable in NYC, BERDO-applicable in Boston, etc.).

---

## How to apply

1. Identify the project's pattern from above (or hybridize).
2. Adjust the year-tier ranges to match the controlling mandate deadline.
3. Build the per-year capex inside `assets/decarb_roadmap_template.md`.
4. Note: phasing is **planning**, not commitment. Energy model + LCA refine actual scope; this skill produces the plan they execute against.
