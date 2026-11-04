# PHI Classic / Plus / Premium — Fixed Criteria

> **Source**: Passive House Institute (PHI), *Building Criteria for the Passive House, EnerPHit and PHI Low Energy Building Standard*, Version 9f (2016, with errata through 2025). Publicly available at https://passiv.de/downloads/03_building_criteria_en.pdf.

> **Format note**: PHI Building Criteria use SI/metric values. The "Target" column below quotes the imperial-converted value (matching PHIUS / NA convention) with the metric source value in parens for verifiability. The skill's `compute_score.py` parses the leading numeric of `Target`. Direction = `lower is better` (Actual ≤ Target = pass) for energy demands and air leakage; `higher is better` for renewable supply if added.

> **Compliance method**: PHI offers two pathways for heating: (1) Annual specific heating demand ≤ 4.75 kBtu/sf·yr (15 kWh/m²·a), OR (2) Heating load ≤ 3.17 Btu/h·ft² (10 W/m²) — choose ONE. The skill captures both as separate metrics; the user must indicate which pathway is being pursued.

---

## PHI Classic

> **Source**: PHI Building Criteria 2016, §1.2 — Classic Class.

| Metric | Direction | Target | Units |
|--------|-----------|--------|-------|
| Annual heating demand | lower is better | ≤ 4.75 (15 kWh/m²·a) | kBtu/sf·yr |
| Heating load | lower is better | ≤ 3.17 (10 W/m²) | Btu/h·ft² |
| Annual cooling+dehum demand | lower is better | ≤ 4.75 (15 kWh/m²·a) | kBtu/sf·yr |
| Cooling load | lower is better | ≤ 3.17 (10 W/m²) | Btu/h·ft² |
| Source primary energy demand | lower is better | ≤ 38 (120 kWh/m²·a) | kBtu/sf·yr |
| Air leakage (pressurization) | lower is better | ≤ 0.6 | ACH50 |
| Frequency of overheating | lower is better | ≤ 10 | % hours over 77 °F (25 °C) |

> Heating: meet EITHER annual demand OR heating load — not both. Cooling: same convention.
>
> "Source primary energy demand" was renamed in newer PHI editions to "PER demand" (Primary Energy Renewable) ≤ 60 kWh/m²·a (≈ 19 kBtu/sf·yr). The skill records the PHI 2016 Classic primary energy target. For projects pursuing PER, override the Target cell with the PER value and note in `Source`.

---

## PHI Plus

> **Source**: PHI Building Criteria 2016, §1.2 — Plus Class. Plus class adds renewable energy generation requirements on top of Classic; heating / cooling / airtightness / overheating identical to Classic.

| Metric | Direction | Target | Units |
|--------|-----------|--------|-------|
| Annual heating demand | lower is better | ≤ 4.75 (15 kWh/m²·a) | kBtu/sf·yr |
| Heating load | lower is better | ≤ 3.17 (10 W/m²) | Btu/h·ft² |
| Annual cooling+dehum demand | lower is better | ≤ 4.75 (15 kWh/m²·a) | kBtu/sf·yr |
| Cooling load | lower is better | ≤ 3.17 (10 W/m²) | Btu/h·ft² |
| PER demand (Primary Energy Renewable) | lower is better | ≤ 14.27 (45 kWh/m²·a) | kBtu/sf·yr |
| Renewable energy generation | higher is better | ≥ 19.03 (60 kWh/m²·a-of-projected-footprint) | kBtu/sf·yr-of-projected-footprint |
| Air leakage (pressurization) | lower is better | ≤ 0.6 | ACH50 |
| Frequency of overheating | lower is better | ≤ 10 | % hours over 77 °F (25 °C) |

> Note on Plus generation units: PHI normalizes renewable generation **per projected building footprint area** (the building's plan-projected ground area), NOT per ICFA / treated floor area. A multi-story building has a smaller footprint than ICFA, so the per-footprint normalization yields a higher numerical generation target than a per-ICFA reading would. Always confirm the user's renewable-generation calculation uses the projected footprint.

---

## PHI Premium

> **Source**: PHI Building Criteria 2016, §1.2 — Premium Class. Premium class is most stringent; demands and generation both more aggressive than Plus.

| Metric | Direction | Target | Units |
|--------|-----------|--------|-------|
| Annual heating demand | lower is better | ≤ 4.75 (15 kWh/m²·a) | kBtu/sf·yr |
| Heating load | lower is better | ≤ 3.17 (10 W/m²) | Btu/h·ft² |
| Annual cooling+dehum demand | lower is better | ≤ 4.75 (15 kWh/m²·a) | kBtu/sf·yr |
| Cooling load | lower is better | ≤ 3.17 (10 W/m²) | Btu/h·ft² |
| PER demand (Primary Energy Renewable) | lower is better | ≤ 9.51 (30 kWh/m²·a) | kBtu/sf·yr |
| Renewable energy generation | higher is better | ≥ 38.06 (120 kWh/m²·a-of-projected-footprint) | kBtu/sf·yr-of-projected-footprint |
| Air leakage (pressurization) | lower is better | ≤ 0.6 | ACH50 |
| Frequency of overheating | lower is better | ≤ 10 | % hours over 77 °F (25 °C) |

> Note on Premium generation units: same footprint-normalization convention as Plus — PHI normalizes generation per projected building footprint, not per ICFA / treated floor area. Premium doubles the Plus target.

---

## Coverage

This file covers PHI Classic, Plus, Premium fixed metric criteria. It does NOT cover:

- **EnerPHit** (PHI retrofit) — out of scope; different baseline.
- **PHI Low Energy Building** — alternate / lower-stringency PHI class. Not bundled.
- **Per-component limits** (window U-factor, opaque-wall U-factor) — those are derivative outcomes from meeting the integrated heating/load targets, not separate compliance criteria.
- **Comfort temperature setpoints** beyond the overheating threshold — refer to PHI Building Criteria §2.
- **Acoustic, IAQ, daylighting requirements** — separate PHI / non-PHI standards.

For metrics not bundled, the user must consult the PHI Building Criteria PDF directly.
