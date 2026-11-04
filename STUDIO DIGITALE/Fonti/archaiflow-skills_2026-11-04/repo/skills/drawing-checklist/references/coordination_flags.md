# Coordination Flags

Common architectural-to-structural and architectural-to-MEP coordination items. Use as a checklist of interfaces to verify before issuing a set.

> **Provenance note.** This 100-item coordination list is a synthesis of common AEC coordination touchpoints — sourced from architectural / structural / MEP coordination practice (AIA Best Practices, AISC 303 Code of Standard Practice for Steel Buildings and Bridges, ASHRAE HVAC Design Guides, MEP coordination guides, NCS v6). It is **not** a published checklist from a single authority. Use as a starting point; supplement with the project-specific coordination matrix from the BIM execution plan and any firm QA/QC checklists. See `_provenance.md` for source authorities and verification status.

---

## Architectural ↔ Structural

### Grid alignment

- Architectural column locations match structural grid on every plan
- Grid letters/numbers identical across A and S sheets
- Grid extends to plan edges on architectural sheets
- Column sizes shown on architectural plans match structural sizing (DD onward)

### Floor-to-floor and structural depth

- Floor-to-floor dimensions match between A sections and S framing plans
- Structural depth zone (joist + slab + topping) accommodates ceiling plenum + MEP
- Slab depressions for wet areas, terraces, and equipment shown on both A and S
- Slab edge conditions at perimeter walls coordinated (overhang, recess, flush)

### Openings in structure

- Slab openings for stairs, elevators, shafts, and skylights match between A and S
- Beam penetrations for ducts/pipes flagged on A and confirmed structurally feasible
- Wall openings in shear walls and load-bearing walls reviewed by structural

### Roof and parapet

- Parapet height and structural backup coordinated (especially at tall parapets)
- Roof equipment loads transferred to structural
- Expansion joints aligned between A and S

### Foundations and below-grade

- Building footprint matches foundation extents
- Basement wall thickness coordinated with site retaining strategy
- Elevator pit and sump locations coordinated

---

## Architectural ↔ MEP

### Ceiling plenum

- Plenum depth in A sections accommodates the deepest MEP run
- Soffit/bulkhead locations on RCP align with mechanical duct routing
- Ceiling height tags consistent between A RCP and M layout

### Shafts and chases

- Vertical shafts (mechanical, electrical, plumbing, exhaust) sized for routing on every floor
- Chase locations consistent floor-to-floor on architectural plans
- Wall thickness around chases accommodates rated construction where required

### Equipment locations

- Mechanical room sizes confirmed against equipment list and service clearances
- Electrical room locations and sizes confirmed against gear list
- Roof equipment (RTUs, condensers, exhaust fans) located on A roof plan and M plan, with screening if required
- Floor drains coordinated with plumbing layout and slab slope

### Penetrations

- Roof penetrations (vents, exhausts, plumbing stacks, conduit) shown on A roof plan
- Wall penetrations through rated assemblies flagged for firestopping
- Slab penetrations coordinated with structural

### RCP fixtures

- Diffusers, returns, sprinklers, lights, speakers, sensors, smoke detectors all located on RCP
- Fixture-to-fixture clearances respected
- Access panels located for equipment requiring service

### Plumbing fixtures

- Fixture counts on A schedules match P schedules
- Fixture locations on enlarged plans align with P rough-in
- Accessibility clearances at fixtures verified

### Electrical

- Switch locations on A plans match E plans
- Receptacle locations match E plans (or "by E" noted clearly)
- Panel locations and clearances coordinated with A

---

## Common conflicts to flag explicitly

- Ceiling height too low for MEP plenum at corridors and back-of-house
- Beam depth at exterior bay conflicts with window head height
- Mechanical shaft moves between floors and breaks vertical alignment
- RTU on roof lands over a column-free interior space (no support)
- Plumbing wall thickness insufficient for stacks at residential bathrooms
- Electrical panel located in a finished public area
- Sprinkler heads conflict with linear lighting in RCP
- Floor drain locations don't align with slab slope direction

---

## When to raise

- **SD:** strategy-level only — major shaft locations, structural grid, mechanical room footprint
- **DD:** every interface above should be reviewed and documented in coordination meetings
- **CD:** every conflict resolved or formally accepted; clash detection complete if BIM
- **IFC:** zero outstanding conflicts; any remaining items become RFIs after issue
