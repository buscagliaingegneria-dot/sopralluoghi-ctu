# Embodied Carbon Pathway

Standard moves for reducing embodied carbon on a building project — primarily new construction or major renovation. The "build less / retain more" principle dominates; substitution moves come second.

---

## The "build less / retain more" principle

**The most consequential embodied-carbon move is to build less.** Refurbishment / adaptive reuse retains the embodied carbon already in place; new construction adds new embodied carbon. Studies typically find:

- Demolition + new construction: 600–1,400 kgCO2e/sf embodied carbon (varies by structure type).
- Adaptive reuse + retrofit: 100–400 kgCO2e/sf.
- Operational-carbon savings from new construction (vs. retrofit) over 30 years rarely exceed embodied-carbon penalty.

**Action:** For any project where demolition is on the table, evaluate adaptive reuse first. The roadmap memo includes a retain-vs.-replace LCA comparison line item even when not the user's stated scope.

References: RMI Embodied Carbon 101; Carbon Leadership Forum CLF Materials Baselines; Architecture 2030 Roadmap to Zero.

---

## Substitution moves (when new construction is proceeding)

### Concrete

**What it represents:** Typically 30–50% of new-construction embodied carbon. Cement is the carbon-heavy ingredient (CaCO3 → CaO + CO2, plus kiln fuel).

**Moves:**

- **Portland-cement substitution** — slag (GGBS), fly ash, natural pozzolans, LC3 (limestone calcined clay). 30–70% Portland reduction possible without strength loss.
- **Lower strength specs** — many architectural concrete sections are over-specified. Coordinate with SE.
- **CarbonCure / Solidia / Carbicrete-treated mix** — sequestered CO2 in the mix.
- **Reduced quantities** — slimmer slabs, post-tensioning, voided slabs, reduced rebar percentage.
- **Recycled aggregate** — partial replacement of virgin aggregate.

**Capex impact:** Cement substitution typically cost-neutral or slightly cheaper. CarbonCure / treated mixes slightly more expensive. Reduced quantities save cost.

**Reference standards:** NRMCA NPDs (National Pollution Determinations); industry-wide EPDs; project-specific EPDs for proper accounting.

---

### Steel

**What it represents:** 15–30% of new-construction embodied carbon for steel-framed buildings.

**Moves:**

- **EAF (Electric Arc Furnace)** over **BOF (Basic Oxygen Furnace).** EAF uses recycled steel + electric heating; BOF uses iron ore + coal. EAF carbon is ~30% of BOF.
- **Spec EPD requirement.** Require structural steel EPDs at procurement; lowest-carbon EPD per cradle-to-gate.
- **Recycled-content target.** Most US structural steel is high recycled content; spec confirms.
- **Reduced quantities** — efficient sections, optimized framing, etc. (SE collaboration).

**Capex impact:** Cost-neutral or slight premium for low-carbon EPD steel.

**Reference standards:** AISC sustainability guidance; product EPDs.

---

### Insulation

**What it represents:** Smaller absolute share but very high GWP per kg for some types.

**Moves:**

- **Avoid HFC-blown closed-cell foam** (XPS, SPF). HFC blowing agents have GWP 700–4,000.
- **Use HFO-blown or water-blown alternatives.** GWP < 10.
- **EPS (expanded polystyrene)** — pentane-blown, low GWP.
- **Mineral wool, cellulose, hemp, wood-fiber.** All low-embodied; cellulose is carbon-negative (bio-sequestered).

**Capex impact:** Mineral wool / cellulose typically cost-neutral or cheaper than HFC foam.

---

### Mass timber

**What it represents:** Substitution for concrete + steel in appropriate applications. Carbon-storage benefit (sequestered carbon) plus generally lower processing carbon than concrete / steel.

**Moves:**

- **CLT (Cross-Laminated Timber)** for floor / roof slabs, walls.
- **Glulam** for beams + columns.
- **NLT / DLT** for floor / roof.
- **Hybrid steel/timber, concrete/timber** for taller structures.

**Constraints:**

- IBC heights / Type IV-A / IV-B / IV-C provisions (2021 IBC introduced).
- Sourcing — chain-of-custody (FSC / SFI / PEFC).
- Acoustic + fire detailing more complex.

**Reference standards:** WoodWorks; Mass Timber Institute; FSC chain of custody.

---

### Façade

**What it represents:** Variable; high-glass façades carry significant embodied carbon (aluminum framing + glass production).

**Moves:**

- **High recycled-content aluminum.** Primary aluminum is carbon-heavy; recycled is 5% of primary's embodied carbon.
- **Lower-carbon glass.** Some manufacturers offer EPDs with significant carbon reductions.
- **Reduced glazing area.** Smaller glass areas reduce both embodied carbon AND operational HVAC load (win-win).
- **Brick veneer over rainscreen instead of curtainwall.** Brick has lower embodied carbon per sf than curtainwall in some assemblies; depends on context.

---

### Interior finishes

**What it represents:** Smaller share but cumulative; high-churn (renovated every 5–15 years), so lifecycle impact is greater than capex implies.

**Moves:**

- **EPDs + HPDs (Health Product Declarations).** Spec requirement.
- **Low-carbon flooring.** Carpet tile vs. broadloom; LVT vs. linoleum vs. ceramic.
- **No / low-formaldehyde wood products.** Cabinetry, doors, millwork.
- **Reused / salvaged materials** for non-critical elements.

**Reference standards:** UL EPDs; Cradle to Cradle certifications.

---

## LCA methodology

For a real embodied-carbon plan, use a whole-building LCA tool:

- **EC3** (Embodied Carbon in Construction Calculator) — free; product-EPD database; project comparison; typically used in DD / CD.
- **Athena Impact Estimator for Buildings** — NA-focused; whole-building cradle-to-grave.
- **OneClick LCA** — paid; whole-building + product LCA; commonly used for LEED / certifications.
- **Tally** (Autodesk Revit plugin) — LCA inside Revit; useful in design.

**Stage scope:**

- **A1–A3** (cradle-to-gate, product manufacturing) — most commonly reported; EPDs use this stage.
- **A4** (transport to site).
- **A5** (construction process, on-site emissions).
- **B1–B5** (use, maintenance, repair, replacement).
- **C1–C4** (end-of-life).
- **D** (beyond-system credits — recycling, reuse).

Most decarbonization-strategist memos recommend reporting A1–A5 (whole-life minus operational) for clarity; full A–D for certification / regulatory submission.

---

## Federal Buy Clean

Federal-procurement projects face Buy Clean Initiative thresholds for concrete, structural steel, asphalt, flat glass. **Cite GSA Buy Clean Implementation Plan + DOE / DOT specs for current thresholds.** Sub-threshold material counts as compliant; over-threshold requires waiver / alternative.

---

## State + jurisdictional embodied-carbon mandates

| Jurisdiction | Mandate | Status |
|--------------|---------|--------|
| CA Title 24 Part 11 (CALGreen) | Embodied carbon provisions in 2022 cycle (Tier 2) and 2025 cycle | Verify current cycle |
| CA Buy Clean California Act | Concrete + steel + flat glass + mineral wool insulation EPDs required for state-funded projects | AB 262 (2017) and amendments |
| New York Buy Clean NY | Concrete + steel + flat glass + asphalt EPDs for state-funded projects | Pending implementation; verify |
| Marin County Low-Carbon Concrete Code | Concrete strength + cement-content thresholds | First in US; check applicability |
| Portland OR Low-Carbon Concrete Initiative | Voluntary + city-procurement | Verify current scope |
| Vancouver Embodied Carbon Bylaw | New construction embodied-carbon thresholds | Verify current scope |
| Federal Buy Clean Initiative (EO 14057) | Concrete + steel + asphalt + flat glass thresholds for federal procurement | GSA + DOE + DOT specs |

**This list is not exhaustive — emerging area; verify current state and scope.**

---

## Anti-patterns

- **Treating embodied carbon as new-construction-only.** Renovations / fit-outs have embodied carbon (interior demo + new finishes + new MEP). LCA accounts for these.
- **Skipping retain-vs.-replace LCA.** Demo + new construction is rarely the lower-carbon path over 30 years.
- **Specifying low-carbon concrete without confirming SE acceptance.** Cement substitution affects strength gain; SE must approve mix design.
- **Specifying mass timber without sprinkler / detailing review.** IBC Type IV-A/B/C have specific requirements; not a drop-in concrete / steel substitute.
- **Reporting only A1–A3 to claim net-zero embodied carbon.** Full whole-life (A–C) is more credible; D credits depend on end-of-life actually happening.
- **Treating biogenic carbon storage in mass timber as immediate offset.** LCA convention varies; some methodologies count biogenic storage, others do not.
