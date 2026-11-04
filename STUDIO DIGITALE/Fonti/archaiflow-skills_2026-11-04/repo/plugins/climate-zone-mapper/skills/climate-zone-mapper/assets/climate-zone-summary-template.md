# Climate Zone Envelope Summary — {{project_name}}

**Project:** {{project_name}}
**Location:** {{city}}, {{state}}
**County:** {{county}}, {{state}}
**Occupancy:** {{occupancy}}  *(commercial / residential)*
**Last updated:** {{date}}

## Climate zone

| Field | Value | Source |
|-------|-------|--------|
| IECC 2024 Climate Zone | **{{zone}}** | IECC 2024 Table C301.1 / ASHRAE 169-2021 Table A-1 |
| Zone label | {{zone_label}} | ASHRAE 169-2021 Table B-2 |
| Moisture regime | {{moisture}} | ASHRAE 169-2021 §6 |
| Warm-Humid? | {{warm_humid}} | IECC 2024 §C301.3.1 |
| Resolution confidence | {{confidence}} | climate-zone-mapper / `compute_envelope.py` |

## Envelope requirements (R-value method)

> **Source:** IECC 2024 Table C402.1.3 + Table C402.4 (commercial) / Table R402.1.2 (residential).
>
> **VERIFICATION STATUS: PENDING.** Bundled cell values in `references/iecc_2024_envelope_assemblies.md` currently read `[verify IECC 2024 Table ...]` and rows in the CSV will show `confidence: pending` until each cell is diffed against ICC Digital Codes and recorded in `references/_audit_log.md`. **Do not paste CSV values into a project specification or code-compliance submission until the relevant cell shows `confidence: high`.** See `references/_provenance.md` for the verification protocol.
>
> Verify against AHJ-codified IECC — state amendments are common (CA Title 24, NYS ECCC, MA Stretch Code, WA WSEC, OR OEESC).

See `{{project_slug}}-envelope.csv` for the full per-component table.

## AHJ amendment checklist

- [ ] Confirm AHJ has adopted IECC 2024 (most jurisdictions are still on 2021 / 2018).
- [ ] Identify state-level amendments (e.g. NYS ECCC, CA Title 24 Part 6, MA Stretch Code, WA WSEC).
- [ ] Verify any local stretch / above-code mandate (NYC LL97 / LL84, Seattle Energy Code).
- [ ] Confirm fenestration WWR ≤ prescriptive limit, or document trade-off path (C402.1.5 / C407).

## Notes / strategy

(Use this section for project-specific decisions — chosen compliance path, U-factor vs R-value method, envelope trade-offs, performance modeling notes.)

---

**Citation footer**

- Standard: IECC 2024 (Commercial + Residential Provisions), ASHRAE 169-2021
- Reference files: `references/iecc_2024_climate_zones.md`, `references/iecc_2024_envelope_assemblies.md`
- Scope: This skill returns IECC 2024 baseline values for the R-value method. AHJ amendments and trade-off paths are user responsibility.
