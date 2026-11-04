---
name: decarbonization-strategist
description: "Builds a phased decarbonisation roadmap for a building over five to fifteen years, covering operational carbon (envelope, systems, electrification, on-site renewables, off-site supply) and embodied carbon (materials, reuse against new build), sequenced against the mandate dates and incentives the user names. Trigger on \"decarbonization roadmap\", \"decarb plan\", \"net zero strategy\", \"electrification roadmap\", \"embodied carbon plan\", \"carbon reduction plan\", a pasted owner brief with a carbon target, or an energy baseline with a jurisdiction. Works in any jurisdiction. Every mandate date, cap, threshold, and incentive value comes from the user; the skill supplies the sequencing method and never a regulatory figure. Produces a roadmap memo, not an energy model, not a life cycle assessment, and not a binding commitment."
license: MIT
metadata:
  title: "Carbon Roadmap"
  summary: "Plan a building's path to lower carbon over 5-15 years"
  discipline: "envelope-performance"
  tags: "Compliance, Pre-Design, Analysis, Project Management"
---

## Overview


Build a 5–15 year decarbonization roadmap for a single building (existing or new). Combine:

1. **Operational carbon** — envelope improvements, HVAC efficiency + electrification, hot water electrification, on-site renewables, off-site RECs.
2. **Embodied carbon** — low-carbon concrete, EPD-driven steel, mass timber substitution, retain-vs.-replace decisions on existing structure.
3. **Regulatory mandate timeline** — jurisdiction-specific deadlines (LL97 cap periods, Title 24 cycle, BERDO targets, AIA 2030 ratchet).
4. **Incentive stack** — federal IRA tax credits, state rebates, utility programs.
5. **Phased capex sequencing** — what to do this year, in 5 years, in 10 years.

Output is a roadmap memo in `docs/decarbonization/` that the owner / sustainability consultant / energy modeler takes into the actual technical scopes (whole-building energy model, LCA, incentive applications).


This skill is **strategic**, not technical: it does not produce energy-model outputs, LCA reports, or final incentive calculations. It frames the **sequence of decisions** that carbonization-impact technical work will prove out.


Aligned with NYC LL97, Boston BERDO, Washington DC BEPS, CA Title 24 Part 6, CA SB 253, Vancouver ZEBP, AIA 2030 Commitment + SE 2050, SBTi Buildings, IRA, EPA Portfolio Manager + ENERGY STAR, EC3 / Athena / OneClick LCA / Tally.


## Scope and limits — read first


**What this does.** Sequences a building's decarbonization moves over five to
fifteen years, operational and embodied, against the mandate dates and
incentives you name, and writes a roadmap memo to `docs/decarbonization/`. The
output is an order of decisions with phasing attached, and the reasoning for
the order.

**What this does not do.**

- **It does not supply a cap, a threshold, a fine, or an incentive rate.** Every
  regulatory figure comes from you or from the primary source named in
  `references/mandate_landscape.md`, which points at the publishing authority
  rather than reciting its tables. LL97's caps and the IRA's credit rates have
  both been restructured since enactment, and a stale figure here would drive a
  capital plan.
- It does not model energy. No EUI is calculated, projected, or verified. That
  is an energy modeller working in IES VE, EnergyPlus, eQUEST, or OpenStudio.
- It does not perform an LCA. Embodied carbon moves are named and sequenced;
  the quantities come from an LCA consultant.
- It does not quote capital cost. Cost benchmarks move annually and belong to
  the cost consultant.
- It does not prove compliance. The energy model, the LCA, and the filed
  benchmarking submission do that. The roadmap only says what to file and when.

**What you need before starting.** Building type and area, existing or new, the
jurisdiction with its named AHJ, a baseline EUI with its source, the owner's
targets and hold horizon, and the authority's own text for any cap, threshold,
or deadline you want the sequence built around.

## When to use


Trigger on:

- Pasted owner OPR with a carbon, EUI, or net-zero target.
- Building baseline (existing EUI from Portfolio Manager / utility bills, OR new-construction modeled EUI from Title 24 / IECC compliance).
- Explicit asks: "decarbonization roadmap", "decarb plan", "LL97 strategy", "Title 24 path", "2030 Commitment plan", "embodied carbon plan", "electrification roadmap", "net-zero strategy", "BERDO path", "IRA stacking question".
- Hand-off from `passive-house-tracker` or `leed-tracker` when the certification target requires a longer-horizon carbon plan beyond the certification scorecard.

Do NOT trigger for:

- Whole-building energy modeling (use sustainability consultant + energy modeler — IES VE, EnergyPlus, eQUEST, OpenStudio).
- LCA / embodied carbon detailed modeling (use LCA consultant + EC3 / Athena / OneClick LCA / Tally).
- Single-credit LEED / WELL / PHIUS scoring (use the respective tracker skill).
- Single-mandate compliance check (use jurisdiction-specific code skill — e.g., `climate-zone-mapper` for IECC).
- Incentive application drafting (use sustainability consultant + tax counsel for federal incentives).

## Workflow


### Step 1 — Bootstrap if needed


Check that `docs/decarbonization/index.md` exists. If not:


```bash
python scripts/init_decarb_workspace.py
```


### Step 2 — Anchor the project context


Read `docs/project.md` if it exists. Pull:

- **Building type + use** (multifamily / office / retail / institutional / industrial / mixed). Determines mandate applicability and benchmark medians.
- **Existing or new construction.** Existing buildings face benchmarking + cap mandates (LL97, BERDO, BEPS). New construction faces code-cycle mandates (Title 24, IECC + state stretch).
- **Square footage** (gross, conditioned, by-use breakdown). Mandates often kick in at thresholds (LL97: 25,000 sf; BERDO: 20,000 sf in 2025, lower thresholds later).
- **Jurisdiction + named AHJ.** The mandate landscape varies sharply — see `references/mandate_landscape.md`.
- **Baseline EUI** (kBtu/sf/yr — site EUI for existing, modeled EUI for new). Source: EPA Portfolio Manager (existing); compliance model output (new).
- **Owner targets** — IRR / NPV thresholds, hard deadlines (LL97 Compliance Period 2 starts 2030), certification commitments (LEED Gold, PHIUS+, WELL v2), 2030 Commitment / SBTi.
- **Capex tolerance + horizon** — owner staying long-term vs. flipping; sale at year 5 vs. hold for 30 years drastically changes ROI calculus.
- **Trigger event** — pending major renovation, leasing turnover, equipment end-of-life, electrification mandate effective date, refinancing covenant.

### Step 3 — Map applicable mandates


Use `references/mandate_landscape.md`. For the named jurisdiction, identify:

- **Carbon-cap mandate** (LL97 / BERDO / BEPS) — building-class-specific cap, compliance periods, fine schedule. **Cite from references/ verbatim — do not recall caps from memory.**
- **Energy-code mandate** (IECC + state stretch / Title 24 Part 6 / NYS ECCC / WSEC) — applicable at permit. New construction or major renovation triggers.
- **Disclosure / benchmarking mandate** (CA SB 253, NYC LL84/87, BERDO benchmarking) — annual reporting requirements.
- **Resilience overlay** (NYC LL126 façade, FEMA flood zone, Title 24 wildfire) — affects sequencing.
- **Federal mandate** (Executive Orders on federal building decarbonization, GSA P-100 sustainability requirements) — federal projects only.

For each mandate, document: applicable / not applicable, threshold met (Y/N), next deadline, fine exposure, available compliance pathways.


### Step 4 — Build the operational carbon path


Use `references/operational_carbon_pathway.md`. The standard sequence:

1. **Envelope** — air sealing, insulation upgrade, window replacement / film. Baseline-load reduction ALWAYS comes first (avoids oversizing electrified equipment).
2. **HVAC efficiency** — controls, BAS optimization, recommissioning. Cheap, fast.
3. **HVAC electrification** — replace fossil-fired boilers / furnaces / DHW with heat pumps. The largest operational carbon move on most buildings; staging matters.
4. **DHW electrification** — heat-pump water heaters; large central systems may stage longer than space heat.
5. **Cooking electrification** — induction, electric ovens (multifamily, commercial kitchens); often last to electrify.
6. **On-site renewables** — rooftop PV, EV charging infrastructure (some grid-resilience overlap).
7. **Off-site renewables** — RECs / PPAs to close residual operational carbon. Acceptable as last lever, not first.

Document the project's sequence with phasing: now / 5 yr / 10 yr / 15 yr.


### Step 5 — Build the embodied carbon path


Use `references/embodied_carbon_pathway.md`. The standard moves:

1. **Build less / retain more.** Refurbishment + adaptive reuse beats new construction on embodied carbon almost always.
2. **Concrete** — Portland-cement substitution (slag, fly ash, LC3); lower-strength specs where structural; CarbonCure / Solidia-treated.
3. **Steel** — EAF (electric arc furnace) over BOF (basic oxygen furnace); EPD-required spec; recycled-content targets.
4. **Insulation** — avoid HFC-blown foam; use EPS / mineral wool / cellulose; check GWP.
5. **Mass timber** — substitute for concrete / steel on appropriate spans; carbon-storage benefit + sequestration (LCA accounting matters).
6. **Façade** — aluminum recycled-content, low-carbon glass.
7. **Interior finishes** — health-product declarations (HPDs) + EPDs.

Document the project's embodied-carbon move set with phasing.


### Step 6 — Stack the incentives


Use `references/incentives_stack.md`. For the project profile, layer:

- **Federal IRA** — §13301 (179D commercial deduction), §13303 (45L residential credit), §48 (Investment Tax Credit for renewables), §13501 (45Y/48E clean electricity), Domestic-content bonus, Energy-community bonus, Prevailing-wage + apprenticeship bonus.
- **State** — CA SGIP, NY NYSERDA, MA Mass Save, IL ComEd, etc. — varies sharply.
- **Utility** — local utility incentives for heat pumps, building decarbonization, BAS optimization.
- **Carbon credit / offset markets** — caution; not a substitute for direct reductions.

**Cite incentive amounts from references/ — do not recall from memory.** IRA provisions have changed multiple times since 2022 enactment; confirm current rates via IRS guidance.


### Step 7 — Phase + sequence the capex


Use the templates in `assets/decarb_roadmap_template.md`. The phasing logic:

- **Year 0 (now)** — fast, no-regret actions: benchmarking submission, BAS optimization, controls / setpoints, lighting LED retrofit, low-cost air sealing.
- **Year 1–3** — medium capex, high impact: envelope improvements, HVAC partial electrification, on-site PV start.
- **Year 4–7** — major capex, mandate-driven: full HVAC electrification, DHW electrification, façade upgrade if BERDO / LL97 cap pressure.
- **Year 8–15** — finishing moves: cooking electrification, cooking-load shifting, off-site PPA / RECs to close residual.

Sequence so that mandate deadlines are met **with margin**. NYC LL97 Compliance Period 2 (2030–2034) starts 2030; building-decarb capex needs 2–4 years of design + procurement + install + commissioning lead time.


### Step 8 — Write the roadmap memo


Use `assets/decarb_roadmap_template.md`. The memo includes:

- **Header** — project, building profile, baseline EUI, owner targets, jurisdiction, date.
- **Mandate landscape** — applicable mandates with deadlines and fine exposure.
- **Baseline + target EUI / carbon trajectory** — table or chart description.
- **Operational carbon path** — sequenced moves with year, scope, capex range, kBtu/sf reduction.
- **Embodied carbon path** — sequenced moves (mostly relevant for new construction or major renovation).
- **Incentive stack** — applicable federal + state + utility programs with amounts (from `references/`).
- **Phased capex schedule** — table by year.
- **Open questions** for the energy modeler / LCA consultant / tax counsel / utility.
- **Risk flag** — regulatory landscape changes, pending legislation, technology cost trajectory.
- **Disclaimers** — strategic plan, not energy model or LCA.

Write to `docs/decarbonization/<project-slug>-<YYYY-MM-DD>.md` and append to `docs/decarbonization/index.md`.


### Step 9 — Hand off


The roadmap is strategic. Hand off to:

- **Energy modeler / sustainability consultant** for whole-building energy model under proposed scope.
- **LCA consultant** for embodied carbon quantification.
- **MEP engineer** for system sizing under the proposed electrification path.
- **Tax counsel** for IRA + state incentive application strategy.
- **Owner facilities + capex planning** for phased capex inclusion in long-range plan.
- `passive-house-tracker` / `leed-tracker` for certification overlays.
- `value-engineering-advisor` if budget constraints challenge the roadmap.

## Anti-patterns

- **Never recall LL97 caps, BERDO targets, BEPS performance standards, or fine schedules from memory.** Cite from `references/mandate_landscape.md` only. The 2024 amendments to LL97 (Article 321) restructured the cap formula; the 2026 BERDO performance period began Jan 2025; the 2025 Title 24 cycle starts Jan 2026. **Regulatory landscape changes faster than this skill — verify last-verified date on every reference; if > 12 months, flag for re-verification.**
- **Never recall IRA tax credit amounts from memory.** §13301 (179D), §13303 (45L), §48, §45Y, §48E rates and bonus eligibility (domestic-content, energy-community, prevailing-wage) have changed multiple times since IRA enactment (Aug 2022). Cite from `references/incentives_stack.md` and direct user to IRS guidance + tax counsel for application.
- **Never present this skill's roadmap as a guaranteed compliance pathway.** The roadmap names _strategic moves and phasing_; actual compliance is proven by the energy model, LCA, and final permit / benchmarking submission.
- **Never recommend off-site RECs / offsets as a primary compliance strategy.** They are last-lever residual closure, not first move. LL97 explicitly limits REC + offset substitution per Article 321; BERDO and other mandates similarly restrict.
- **Never skip the "build less / retain more" check on embodied carbon.** New construction's embodied carbon often dwarfs decades of operational carbon savings. This skill must explicitly evaluate refurbishment / adaptive reuse against new construction.
- **Never recommend electrifying space heat without first reducing envelope load.** Electrified equipment sized to a leaky envelope is oversized, expensive, and underperforms. Envelope first, then electrify.
- **Never quote $/sf or $/MMBtu cost numbers from memory.** Cost benchmarks (RSMeans, RMI Net-Zero Buildings cost data, NREL ATB) update annually. Direct user to current source.

## Resources

- `scripts/init_decarb_workspace.py` — bootstrap `docs/decarbonization/` and `index.md`.
- `references/_provenance.md` — pinned editions; **regulatory landscape changes fast.**
- `references/mandate_landscape.md` — jurisdiction-specific carbon mandates.
- `references/operational_carbon_pathway.md` — standard operational decarb sequence.
- `references/embodied_carbon_pathway.md` — standard embodied decarb moves.
- `references/incentives_stack.md` — federal IRA + state + utility incentives.
- `references/phasing_patterns.md` — common phasing patterns.
- `references/aia_2030_sbti_targets.md` — AIA 2030 Commitment + SBTi.
- `assets/decarb_roadmap_template.md` — roadmap memo template.
