# Provenance — Passive House Tracker References

## Verification status

- **Last verified against PHIUS + PHI public sources**: 2026-05-09
- **PHI fixed criteria values are verified verbatim against PHI Building Criteria** Version 9f (2016, with errata through 2025).
- **PHIUS+ targets are project-specific and not bundled.** A sample 12-metros × 4-metrics targets table previously present in `phius_2021_targets.md:43-54` (48 cells: Phoenix / Miami / Houston / Atlanta / Los Angeles / Charlotte / Washington DC / Chicago / Boston / Minneapolis / Anchorage / Seattle × annual heating, annual cooling+dehum, peak heating, peak cooling) was removed 2026-05-09 due to fabricated content (well-tracker pattern, see `feedback_standards_verification.md`). The honest path is to direct each project to the PHIUS Source Zero portal.

## Pinned source versions

**PHIUS+ 2021** — Passive House Institute US (North America)
- Publisher: PHIUS (Passive House Institute US)
- Standard version: **PHIUS+ 2021 Certification Guidebook** (current; PHIUS 2024 supersedes 2021 in the field — when adopted by AHJ / utility programs, update references)
- Methodology: **PHIUS Source Zero methodology** (current). Targets are derived per-project; back-solves the energy budget required to achieve net-zero source energy after typical on-site renewables for the project's specific climate, geometry, occupancy, and use type.
- Public source: https://www.phius.org/phius-source-zero
- Per-project targets: fetched from the PHIUS Source Zero portal (free with PHIUS account). Not bundled into this skill — see `phius_2021_targets.md` for methodology.

**PHI** — Passive House Institute (Darmstadt, Germany)
- Publisher: Passivhaus Institut
- Standard version: **PHI Building Criteria, Version 9f (2016, with errata through 2025)**
- Classes: Classic / Plus / Premium (renewable-energy classes per PHI Building Criteria 2016)
- Public source: https://passiv.de
- Building Criteria PDF: https://passiv.de/downloads/03_building_criteria_en.pdf
- Method documentation: PHPP (Passive House Planning Package) — PHI's spreadsheet-based tool

## Coverage of this skill

| Reference file | Covers |
|----------------|--------|
| `phius_2021_targets.md` | PHIUS+ 2021 metric set + units + direction + per-project derivation methodology via PHIUS Source Zero portal. **No bundled metro→target table** — targets are project-specific. |
| `phi_classic_criteria.md` | PHI Classic / Plus / Premium fixed criteria with imperial conversions, in machine-parseable table form. Values verified verbatim against PHI Building Criteria 2016. |

**Out of bundled scope** (refer to authoritative sources):

- **PHIUS+ 2021 climate-specific targets per project** — must come from the user's PHIUS Source Zero portal export. Not bundled.
- **PHIUS 2024** — supersedes PHIUS+ 2021. Will be added when PHIUS publishes the public-facing target portal under 2024.
- **EnerPHit** — PHI retrofit standard. Different criteria (annual heating ≤ 25 kWh/m²·a base case). Out of scope.
- **PHIUS+ Source Zero certification class** — net-source-zero overlay on PHIUS+ 2021. The bundled metrics include source energy; the Source Zero overlay (target = 0 source energy after on-site renewables) is computed by PHIUS portal, not bundled here.
- **CO₂ tracking** — PHIUS+ 2021 added an embodied carbon track in the 2024 revision. Not bundled.
- **PHI EnerPHit, PHI low-energy class** — out of scope.

## How to verify

1. Open https://www.phius.org/phius-source-zero — confirm the metrics listed in `phius_2021_targets.md` match the portal's published metric set.
2. Open https://passiv.de/downloads/03_building_criteria_en.pdf — compare PHI Classic / Plus / Premium target values against `phi_classic_criteria.md` (Version 9f, 2016, with errata through 2025).
3. If any value differs, the reference file is wrong — file an issue against `archtmpl`.

## Audit history

- **2026-05-09** — Audit removed 48 fabricated PHIUS+ "sample target" cells from `phius_2021_targets.md` (well-tracker pattern, per `feedback_standards_verification.md`). PHI fixed criteria left unchanged after row-by-row verification. Provenance pinned to PHI Building Criteria Version 9f (2016, errata through 2025) + PHIUS+ 2021 Certification Guidebook + PHIUS Source Zero methodology (current).
- **2026-05-08** — Initial bundle created.

## Version pin warning

Passive House standards are updated at decade-scale, but the field-adopted version varies by region:

- **PHIUS+ 2021** is the current PHIUS standard for 2026 builds reaching certification within the 2021–2024 cycle. PHIUS 2024 is published; the field adoption is mid-transition.
- **PHI Classic / Plus / Premium** has been stable since the 2016 Building Criteria revision; current edition is Version 9f, 2016 (with minor errata through 2025).

Update the **Last verified** date above when either standard publishes a new revision. That date is the record. This line used to name a `Version` and a `Last Verified` property in a Notion database; that database was removed on 2026-07-28 and this file is now the only place the date lives.
