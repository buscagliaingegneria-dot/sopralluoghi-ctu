# Operational Carbon Pathway

Standard sequence for reducing operational carbon on existing or new buildings. The order matters — envelope-first, then electrify, then offset residual. Doing it out of order yields oversized equipment, stranded capex, and incomplete mandate compliance.

---

## The standard sequence

### Step 1 — Benchmark + measure

**What:** Submit benchmarking (LL84, BERDO, BEPS, WA Clean Buildings). Pull current site EUI from EPA Portfolio Manager. Identify ENERGY STAR Score (where applicable).

**Why first:** No decarb path without baseline. Many mandates trigger off the benchmarking submission.

**Capex:** Low (consultant fee for first submission, then internal staff).

**Carbon impact:** Indirect — surfaces opportunities. Directly required for compliance.

---

### Step 2 — Controls / BAS optimization / commissioning

**What:** Re-commissioning (RCx) of existing BAS; setpoint tuning; schedule optimization; sensor calibration; sequence-of-operations review. Investment-grade audit (IGA) where the building is large or complex.

**Why this order:** Cheapest, fastest. Often achieves 5–15% energy reduction with no equipment change. Establishes operational baseline before capex.

**Capex:** Low to medium ($0.50 – $2 / sf for re-commissioning, varies). Verify with current consultant pricing.

**Carbon impact:** 5–15% operational EUI reduction typical (RCx benchmark literature).

**Mandate alignment:** NYC LL87 decennial RCx requirement.

---

### Step 3 — Lighting + plug-load

**What:** LED retrofit (most buildings already done; check); occupancy sensors; daylight harvesting; plug-load controls.

**Why this order:** Independent of HVAC; quick payback; reduces internal heat gain, which then reduces cooling load (so should precede cooling-equipment sizing decisions).

**Capex:** Low to medium.

**Mandate alignment:** NYC LL88 lighting + sub-metering; CA Title 24 Part 6 LPD requirements; IECC C405.

---

### Step 4 — Envelope improvements

**What:** Air-sealing; roof insulation; wall insulation (where feasible without major façade rework); window upgrade or window-film; vestibule additions; cool-roof.

**Why this order:** Reduces baseline heating + cooling load. **Critical: must precede HVAC equipment sizing for any electrification (Step 5).** Electrified equipment sized to a leaky envelope is oversized, inefficient, and stranded asset.

**Capex:** Medium to high ($5 – $50+ / sf depending on scope; full façade replacement is order of magnitude higher). Verify with current cost benchmarks.

**Carbon impact:** 10–30% operational EUI reduction typical for major envelope upgrade.

**Mandate alignment:** IECC envelope requirements; LL126 façade-inspection cycle (intersect timing with envelope retrofit); NYC LL97 (envelope-driven cap relief); CALGreen Tier 1+2.

---

### Step 5 — HVAC efficiency improvements + electrification

**What:**

- **Efficiency improvements first** (where electrification is delayed): higher-efficiency boilers, ECM motors, VFDs, ERVs / DOAS, CO2-DCV.
- **Electrification of space heat:** replace fossil-fired boilers / furnaces with air-source or ground-source heat pumps. Cold-climate ASHPs effective in CZ 5–7. VRF for partial / phased electrification.
- **Electrification of cooling:** typically already electric; check for replacement opportunities.
- **DHW electrification:** heat-pump water heaters (HPWHs); central CO2 HPWH for multifamily / hotel / large facility.
- **Cooking electrification (multifamily / commercial kitchens):** induction cooktops, electric ovens. Often last to convert.

**Why this order:** Largest single operational-carbon move on most fossil-fired buildings. Requires envelope-load reduction (Step 4) first.

**Capex:** High ($15 – $100+ / sf for full electrification, varies sharply by building type, climate zone, and existing infrastructure). Verify with current cost benchmarks.

**Carbon impact:** 20–50% operational carbon reduction typical for full electrification (depending on grid mix).

**Mandate alignment:** NYC LL97 (electrification is the only path to Compliance Period 2 caps for most buildings); CA Title 24 2025 cycle (heat-pump first cycle); BERDO 2.0; WA Clean Buildings; Vancouver ZEBP; Toronto TGS.

**Phasing notes:**

- Equipment end-of-life is the natural electrification trigger; don't replace fossil with fossil during the LL97 cap-pressure window.
- Electrical infrastructure upgrade (service, panels, conduit) often required; coordinate with utility.
- Phased electrification (one system at a time) cheaper than wholesale conversion.
- Resilience overlay: electrified buildings need backup (genset, BESS) for critical loads.

---

### Step 6 — On-site renewables

**What:** Rooftop PV; carport / canopy PV; battery storage (BESS) for resilience + demand-charge management; geothermal (typically requires Step 5 ground-source HVAC).

**Why this order:** Reduces purchased-grid carbon; matches well with electrified loads. PV oversizing without electrified loads is stranded capex.

**Capex:** Medium to high; PV $1.50 – $3 / W installed (verify with NREL ATB current); BESS $300 – $1500 / kWh (varies sharply, verify).

**Carbon impact:** Replaces grid mix carbon with on-site zero-carbon for the matched load.

**Incentives:** IRA §48 / §48E ITC + bonus credits (domestic content, energy community, prevailing wage). Verify current rates.

**Mandate alignment:** NYC LL97 BESS + on-site renewables credits; CA Title 24 Part 6 PV mandate (verify current cycle thresholds); CALGreen.

---

### Step 7 — Off-site renewables (RECs / PPAs / Community Solar)

**What:** Renewable Energy Credits (RECs); Power Purchase Agreements (PPAs); community solar subscriptions.

**Why last:** Closes residual operational carbon. Not a substitute for direct reductions.

**Mandate constraint:** LL97 Article 321 limits REC + offset substitution (specific %; do not recall — cite from primary source). BERDO + others similarly restrict.

**Carbon impact:** Closes residual operational carbon (typically 5–20% residual after Steps 4–6).

---

## Carbon-impact estimation (heuristic, not modeling)

For an existing fossil-fired commercial building in a moderate US climate zone, full execution of Steps 1–7 typically yields 60–90% operational-carbon reduction over 10–15 years. **This is a strategic estimate, not a modeling output.** The whole-building energy model proves out per-step kBtu/sf reductions and the LCA proves out embodied carbon impact.

Per-step ranges:

| Step | Operational carbon reduction (typical range) |
|------|----------------------------------------------|
| 1. Benchmarking | 0% direct; enables all subsequent |
| 2. Controls / RCx | 5–15% |
| 3. Lighting + plug-load | 5–10% |
| 4. Envelope | 10–30% |
| 5. HVAC efficiency + electrification | 20–50% (electrification dominates) |
| 6. On-site renewables | Variable (depends on PV roof area, BESS size) |
| 7. Off-site RECs / PPAs | Closes residual to net-zero |

Cumulative is not additive (savings stack non-linearly); the energy model is the source of truth.

---

## Anti-patterns

- **Electrifying before envelope upgrade.** Oversized equipment + low ROI.
- **Skipping benchmarking.** Mandates that drive the roadmap fire off the benchmark; without it, no triggering numbers.
- **Treating RECs as primary compliance.** Mandates limit substitution; RECs are residual closure.
- **Replacing fossil HVAC with fossil HVAC during cap pressure.** Equipment installed in 2025 will face 2030 cap pressure; locks in stranded asset.
- **Designing electrification without verifying utility electrical capacity.** Electrified building doubles or triples electrical service; utility upgrades are 12–36-month lead time.
- **Ignoring the resilience overlay.** Electrified buildings have new vulnerabilities (grid outage = no heat), so the backup strategy belongs in the roadmap rather than after it.

---

## Sequencing under deadline pressure

When a mandate deadline is < 5 years out (LL97 Compliance Period 2 starts 2030; pre-2030 building), compress Steps 1–7 into:

- **Year 1:** Benchmark + controls/RCx + lighting + investment-grade audit.
- **Year 2:** Envelope design + permit + procurement.
- **Year 3:** Envelope construction + electrification design.
- **Year 4:** Electrification permit + procurement + utility capacity confirmation.
- **Year 5:** Electrification construction + commissioning.
- **Pre-Compliance Period 2 (2029–30):** Final audit + benchmark to confirm cap compliance.

Skipping envelope is tempting under deadline pressure but produces stranded electrification capex.
