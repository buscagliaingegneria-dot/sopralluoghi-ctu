# Sheet Types

Architectural sheet types with per-phase content expectations.

**Sheet-type definitions follow NCS v6 Module 2 (Uniform Drawing System).** Per-phase content expectations below are common practice; verify against firm BIM execution plan and AIA B101 §3.X for the project-specific phase definitions. See `_provenance.md` for source authorities and verification status.

---

## G-series — General

_Source: G-series sheet-type designation per NCS v6 Module 2 (Uniform Drawing System). Per-phase content lists are common-practice synthesis._

### G-000 Cover

- SD: project name, address, team, sheet index, location map
- DD: + code summary thumbnail, key plan
- CD: + final sheet index, signature block, seal location
- IFC: + revision history block, "Issued for Construction" stamp

### G-001 / G-100 Code Summary & Life Safety

- SD: occupancy classification, construction type, allowable area calc (concept)
- DD: + life safety plans per floor (egress paths, exit widths, travel distance, occupant load)
- CD: + accessibility compliance summary, fire-rated assembly schedule, exiting calculation worksheet
- IFC: + AHJ comment responses incorporated

### G-002 Sheet Index & Symbols

- All phases: complete sheet list, symbols legend, abbreviations, drawing conventions
- DD onward: revision tracking column

---

## A-0xx — Site

_Source: A-discipline + 0-series (general/site) sheet-type designation per NCS v6 Module 2. Site-plan content expectations are common practice; verify against project civil scope and firm standards. CD-phase fire access requirements driven by IFC §503 and local AHJ amendments._

### A-001 Site Plan

- SD: footprint, setbacks, property lines, north arrow, primary access
- DD: + site grading concept, paving extents, landscape zones, utility entry points
- CD: + dimensioned site, finish grades at building, accessible routes, fire access
- IFC: + final coordination with civil

---

## A-1xx — Floor Plans

_Source: A-discipline + 1-series (plans) sheet-type designation per NCS v6 Module 2. Per-phase wall depiction (single-line / double-line) and tagging conventions are common-practice synthesis, not direct NCS quotation._

- SD: single-line walls, room names, north arrow, key plan reference
- DD: double-line walls, partition tags, room numbers, dimensions to grid + major openings, door tags
- CD: + every dimension required to build, all door/window/equipment tags, wall type tags at every wall, detail callouts to enlarged plans and wall sections
- IFC: + revision clouds and delta tags

**Common missing items at any phase:** north arrow consistency between sheets, key plan, match line for multi-sheet floors, column grid extension to plan edges.

---

## A-2xx — Reflected Ceiling Plans (RCPs)

_Source: A-discipline + 2-series (RCPs / ceiling-related) per NCS v6 Module 2. Coordination with mechanical (diffusers / sprinklers / lighting) is office convention; tied to ASHRAE / NFPA 13 sprinkler placement and project MEP scope._


- SD: not typically issued
- DD: ceiling heights, soffit/bulkhead locations, lighting layout intent, ceiling material zones
- CD: + every fixture located and tagged, ceiling-mounted equipment (diffusers, sprinklers, speakers, sensors) coordinated with MEP, access panel locations
- IFC: + revisions

**Common missing items:** ceiling height tags at every plane change, coordination with MEP for diffuser/sprinkler placement.

---

## A-3xx — Exterior Elevations

_Source: A-discipline + 3-series (elevations) per NCS v6 Module 2. Per-phase content (massing → openings → full callouts) is common-practice synthesis._


- SD: massing and fenestration intent, material zones, north arrow on key plan
- DD: openings sized and located, material callouts, key vertical dimensions (FFE, parapet, sill heights)
- CD: + every dimension and material change, all callouts to wall sections and details, expansion joint locations, signage zones
- IFC: + revisions

**Common missing items:** elevation key plan showing which face is shown, ground line and finish grade indication, true material extents (not just "metal panel").

---

## A-4xx — Building Sections

_Source: A-discipline + 4-series (sections) per NCS v6 Module 2. Section-cut and content expectations are common-practice synthesis._


- SD: 1-2 key sections, floor-to-floor, parapet/roof line
- DD: structural depth zones, ceiling plenum, MEP shaft callouts
- CD: + every distinct vertical condition cut, callouts to wall sections, enlarged sections at stairs/elevators
- IFC: + revisions

---

## A-5xx — Wall Sections

_Source: A-discipline + 5-series (large-scale views / wall sections) per NCS v6 Module 2. Per-phase scope is common-practice synthesis._


- SD: not typically issued
- DD: typical exterior wall section foundation-to-roof, key dimensions
- CD: wall sections at every distinct exterior condition (typical, parapet, base, window head/jamb/sill, roof termination, expansion joint), full assembly callouts referenced to detail sheets
- IFC: + revisions

---

## A-6xx — Enlarged Plans

_Source: A-discipline + 6-series (details / enlarged views) per NCS v6 Module 2. Note: NCS designates 6-series for details, but US offices commonly route enlarged plans through 6xx; verify against firm sheet-numbering standard._


- SD: not typically issued
- DD: stairs, elevators, restrooms, kitchens at 1/4" or 1/2"
- CD: + every special program area, all dimensions, fixture/equipment tags, finish callouts
- IFC: + revisions

---

## A-7xx — Schedules

_Source: A-discipline + 7-series (schedules / diagrams) per NCS v6 Module 2. Door / window / partition / finish schedule structure is common-practice synthesis._


- SD: not typically issued
- DD: door, window, partition schedules in preliminary form (types defined, count approximate)
- CD: + finish schedule, hardware schedule (or by spec), equipment schedule, accessory schedule; every entry referenced from a tag on a plan
- IFC: + revisions

---

## A-8xx — Details

_Source: A-discipline + 8-series (user-defined / project-specific) per NCS v6 Module 2. US offices commonly use 8-series for typical details; verify against firm standard._


- SD: not typically issued
- DD: typical exterior wall details (head, jamb, sill, base, parapet), typical partition types
- CD: + every transition, penetration, termination; interior details (casework, ceiling transitions, floor transitions, expansion joints); roof details (drains, penetrations, parapets, equipment curbs); every detail callout from plans/sections/elevations lands on a real detail
- IFC: + revisions

---

## A-9xx — Interior Elevations

_Source: A-discipline + 9-series (3D representations / interior elevations in NCS Module 2) per NCS v6. Some offices route interior elevations through A-9xx, others through A-6xx with enlarged plans; verify against firm standard._


- DD: key wet areas, feature walls
- CD: every wet area, every casework run, every significant feature wall; all dimensions, finish callouts, fixture/accessory tags
- IFC: + revisions

---

## Cross-sheet hygiene (every phase from DD onward)

_Source: Sheet-numbering, title-block, and revision conventions per NCS v6 Module 2 (Uniform Drawing System) + AIA G-series administrative documents (G701 Change Order, G710 ASI). Specific QA/QC items (north-arrow consistency, match-line alignment) are common-practice synthesis from AIA Best Practices and firm QA standards._


- Sheet numbering follows the office or NCS standard, no gaps without intent
- Title block consistent across the set: project name, address, sheet name, sheet number, scale, date, revision
- North arrow orientation consistent across all plans
- Grid letters/numbers consistent across all plans, sections, and elevations
- Detail callouts use the office's standard bubble; the referenced detail exists on the called sheet
- Section cuts on plans match the section drawing's view direction
- Match lines align between adjacent sheets
- Revision clouds + delta tags on every changed item from DD onward
