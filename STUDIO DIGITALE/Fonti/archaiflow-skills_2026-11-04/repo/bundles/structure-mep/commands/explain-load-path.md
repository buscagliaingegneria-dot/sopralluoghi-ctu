---
title: Explain Load Path
summary: Trace how load travels from roof to foundation
discipline: structure-mep
tags: ["Compliance", "Design"]
description: Trace a structural load path (gravity → lateral → foundation) on a section, plan, or framing element per ASCE 7-22 / IBC 2024 Ch. 16
argument-hint: <section-or-paste-and-load-question>
---

# Explain Load Path

Trace a structural load path on a section, plan, or framing element through gravity → lateral → foundation per `ASCE 7-22` / `IBC 2024 Ch. 16`. Output is an inline interpretation identifying the path, transfer points, and discontinuities. For full structural analysis or member design, engage the Engineer of Record.

## Input you need

Before tracing, gather:

- **Section or framing element** — paste a description, sketch reference, or text. Identify:
  - **Building system** — `steel moment frame`, `concrete shear wall`, `CLT panel`, `light-frame wood`, `steel braced frame`, `mass-timber post-and-beam`, `precast tilt-up`, `composite steel + concrete`.
  - **Element of interest** — column, beam, transfer beam, shear wall, brace, diaphragm, drag strut / collector, foundation.
  - **Section / sheet** — NCS-6 form: `Section A-A on S-201`, `Detail 4/S-301`. Never "drawing 201" generically.
- **Load type** — gravity (`dead`, `live`, `snow`, `rain`, `dead+live`, `dead+live+snow`), lateral (`wind W`, `seismic E`, `lateral earth pressure H`), special (`crane`, `vehicular impact`, `hydrostatic`, `vibration`, `blast`).
- **Load value or design intent** — `100 psf live`, `30 psf snow`, `Sds = 0.50`, `Risk Category II`, `Wind Exposure C, V = 110 mph`, `lateral earth at-rest pressure 60 pcf`. If unknown, pull from `S-001` General Notes via `drawing-reader` or ask the EOR.
- **Code edition** — confirm jurisdiction's adopted IBC edition with the AHJ.
- **AHJ + project context** — `NYC DOB`, `LADBS`, `DSA` (CA K-12), `CA HCAI` (CA hospitals), `Toronto Building`, `Boston ISD`, `Chicago DOB`. Risk Category from `IBC 2024 §1604.5`. Special inspections per `IBC 2024 Ch. 17` may apply.
- **Specific question** — Examples: "Does the L3 transfer beam carry the lateral or only gravity?", "Where does the shear from the L4 corridor wall go to foundation?", "Is this collector continuous to the diaphragm boundary?"

If section or framing intent is unclear, route through `drawing-reader` skill or ask for the S-series sheet path. Do not invent design loads.

## Output structure

```markdown
# Explain Load Path — [Element, Section reference]

**Building system:** [Steel moment frame / Concrete shear wall / CLT panel / Light-frame wood]
**Element:** [Transfer beam, Section A-A on S-201]
**Load type:** [Gravity dead+live / Lateral seismic E / Wind Y-direction]
**Risk Category:** [I / II / III / IV per IBC 2024 §1604.5]
**Code:** [IBC 2024 Ch. 16 / ASCE 7-22]
**SDC:** [B / C / D / E per ASCE 7-22 §11.6]
**Question:** [the user's specific question]

---

## Path trace (load source → ground)

1. **Source** — [Where the load originates: roof, floor, exterior wall, equipment.]
2. **Distribution element** — [Diaphragm or beam that distributes the load to vertical elements.]
3. **Vertical element** — [Column / shear wall / brace that carries the load down through stories.]
4. **Transfer (if any)** — [Transfer beam, transfer truss, podium slab — where the path discontinues and re-routes.]
5. **Foundation interface** — [Base plate / shoe / footing / pile cap / mat.]
6. **Foundation to soil** — [Bearing, friction, end-bearing — per the geotech recommendation.]

## Code references

- **Gravity loads** — `ASCE 7-22 Table 4.3-1` (live load by occupancy), `Ch. 7` (snow), `Ch. 8` (rain), `IBC 2024 §1607` (live load).
- **Lateral loads** — `ASCE 7-22 Ch. 26-30` (wind), `Ch. 11-12` (seismic), `IBC 2024 §1609` (wind), `§1613` (seismic).
- **Combinations** — `ASCE 7-22 Ch. 2`: LRFD `§2.3`, ASD `§2.4`.
- **Diaphragms / chords / collectors** — `ASCE 7-22 §12.10` (seismic), `§12.10.2` (collector continuity to diaphragm boundary).
- **Special inspections** — `IBC 2024 Ch. 17` if Risk Category triggers.
- **Existing buildings** — `IEBC 2024` (code path) and `ASCE 41-23` (seismic evaluation and retrofit) if existing.

## Discontinuities and risks

- [Bullet — transfer-beam concentration: lateral load through a transfer increases ductility demand per `ASCE 7-22 §12.3.3` (vertical irregularity Type 4).]
- [Bullet — collector continuity: collectors must be continuous to the diaphragm boundary per `ASCE 7-22 §12.10.2`. Flag if the section shows a gap.]
- [Bullet — soft-story / weak-story risk per `ASCE 7-22 §12.3.2.1` (vertical irregularity Type 1 or 5) if the L1 / L2 stiffness ratio drops below threshold.]
- [Bullet — re-entrant corners / diaphragm openings per `ASCE 7-22 §12.3.2.2` (horizontal irregularity Type 2 or 3).]

## What to do next

- [Bullet — flag to the Engineer of Record: load-path discontinuities and transfer beams require explicit detailing and capacity-design rules.]
- [Bullet — reference the Structural General Notes (`S-001`) for design loads, material specifications, and special-inspection scope.]
- [Bullet — if the question is about an existing structure, route to a structural condition assessment (per `ASCE 41-23` for seismic retrofit) and `IEBC 2024` for code path.]

## Caveats

- This is a path trace, not member design. The Engineer of Record's stamped calculations and detailing govern; this command does not size members.
- Lateral load distribution assumes a rigid or flexible diaphragm classification per `ASCE 7-22 §12.3.1` — confirm with the EOR which model applies.
- For seismic-demand-controlled elements (collectors, drag struts, struts in chevron-braced frames), capacity-design rules apply. Do not use this command's trace as a substitute for `§12.10` / `§16.5` detailing.
- For existing buildings, `ASCE 41-23` (seismic) and `IEBC 2024` govern, not new-design IBC chapters. The existing-vs-new distinction changes the entire path-evaluation framework.
```

## NA AEC conventions (enforce)

- **English only.** No Hangul anywhere.
- **Imperial-first** units (`psf`, `pcf`, `kip`, `kip-ft`, `ksf`, `mph`, `ft`, `in`, `°F`). Metric in parens only when useful.
- **Codes cited** — `IBC 2024 Ch. 16` (Loads), `Ch. 17` (Special Inspections), `Ch. 18` (Foundations), `Ch. 19` (Concrete), `Ch. 22` (Steel); `ASCE 7-22`, `ASCE 41-23`, `ACI 318-19`, `AISC 360-22`, `AWC NDS-24` (wood), `TMS 402-22` (masonry); `IEBC 2024` (existing); `NBC 2020 Part 4` for Canada. Never `KBC`, `KS`, `EN`, `BS`, `JIS`, `DIN` — out of catalog scope.
- **Section / sheet identifiers** — NCS-6: `S-201`, `S-301`, `Section A-A`, `Detail 4/S-301`. Never "drawing 201" or "sheet S2" generically.
- **Roles** — `Engineer of Record (EOR)`, `Architect of Record (AOR)`, `Geotechnical Engineer of Record (GEOR)`, `Special Inspector` (per `IBC 2024 Ch. 17`), `Owner's Peer Reviewer` (`CA HCAI`). Never use `Director` as a project role.
- **AHJs** — `NYC DOB`, `LADBS`, `DSA`, `CA HCAI`, `Toronto Building`, `Boston ISD`, `Chicago DOB`. Never `the AHJ`, `the city`, or `local authority` generically.
- **Risk Category and SDC** — `IBC 2024 §1604.5` (RC), `ASCE 7-22 §11.6` (SDC). Always cite explicitly.
- **Floor labels** — `L3`, `Level 3`, `3rd floor`. Never `3F`.

## Constraints

- Do not size members or compute capacities. This is a path trace, not design.
- Do not invent design loads. Pull from `S-001` General Notes via `drawing-reader`, or ask the EOR.
- Distinguish gravity vs lateral vs special load paths explicitly. The same element often carries multiple paths with different code chapters governing.
- Always flag transfer beams, soft / weak stories, collector discontinuities, and irregular diaphragm conditions — these are EOR escalations.
- Coexists with `drawing-reader` (S-sheet retrieval) and the planned `foundation-design` skill. For full structural analysis, engage the EOR.
- Markdown only. No Word / PDF output, no `aec-doc-gen` dependency.

## Workflow

1. Echo back: building system, element, load type, Risk Category, code chapter, question. One line.
2. If design load values are unknown, route to `S-001` General Notes via `drawing-reader` or ask the EOR.
3. If the question implicates seismic demand-controlled elements (collectors, struts, transfer-beam-as-lateral), flag the `ASCE 7-22 §12.10` capacity-design requirement.
4. Produce the response in one shot.
5. Surface next-step EOR coordination explicitly (e.g., "Transfer beam carries both gravity and lateral → flag to EOR for capacity-design check per `ASCE 7-22 §12.3.3` and special inspection scope per `IBC 2024 Ch. 17`").
