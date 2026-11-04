# Provenance — Constructability Review References

This skill bundles a synthesized constructability framework. The 8-axis structure is **not** taken from a single published rubric; it is an internal synthesis informed by the published bodies of knowledge listed below. Findings produced by this skill should cite the underlying published source (AISC, ACI, SMACNA, NEC, NFPA, IBC, IECC, OSHA, ASHRAE, FGI) on a per-finding basis — not "this skill" or its bundled axis list.

**Last verified:** 2026-05-09

---

## Disclaimer on the 8-axis rubric

The eight axes used by this skill — trade sequencing, tolerance stack, MEP coordination, install access, lay-down logistics, temporary works, materials procurement, phased operations — are **not** an AGC-published or CMAA-published checklist. AGC publishes preconstruction guidance (e.g., AGC's *Preconstruction Services Manual*, AGC's various contract documents) and CMAA publishes the *Construction Management Standards of Practice* (with a chapter on preconstruction services), but **neither AGC nor CMAA publishes a rubric that decomposes constructability review into these specific eight axes**.

Treat the 8-axis structure as an internally-synthesized organizing framework, informed by the practice areas covered in AGC and CMAA preconstruction publications and by the reviewer's experience. Do not cite "AGC's eight-axis constructability checklist" in deliverables — that document does not exist.

When using this skill in a deliverable that the AOR or owner will rely on, frame the methodology as: "constructability review covering [the eight axes by name], with each finding referenced to the applicable published standard (AISC 303-22, ACI 117, SMACNA, NEC 2023, NFPA 241-22, IBC 2024, IECC 2024, OSHA 1926, ASHRAE 170-2021, FGI Guidelines 2022) and to project-specific procurement quotes for lead-time items."

---

## Practice references informing the framework

These are the published bodies of knowledge that shape the axes and the example findings. Each finding produced by this skill should cite the relevant standard explicitly — not "the skill" or "the framework".

### Constructability practice (general)

- **AGC of America** preconstruction publications. AGC publishes the *Preconstruction Services Manual* and related contract documents (AGC ConsensusDocs 500 series for CMAR), which describe constructability review as part of preconstruction scope. AGC does not publish a numbered constructability rubric. Source: agc.org publications portal.
- **CMAA** *Construction Management Standards of Practice* (current edition). Chapter on preconstruction services scopes constructability review at SD / DD / 50% CD / 100% CD / GMP set. Source: cmaanet.org publications.
- **AIA contract documents.** AIA Document A201-2017 *General Conditions* governs CO economics and the cost differential between issues caught at design vs caught in CA. AIA B101 / B201 frame the architect's pre-construction reviews. AIA C401-2017 frames consultant scope. Source: aiacontracts.com.

### Tolerance and installation standards

- **AISC 303-22** *Code of Standard Practice for Steel Buildings and Bridges* — erection tolerances for structural steel (mill, fabrication, field). Source: aisc.org / ANSI/AISC 303.
- **ACI 117** *Specification for Tolerances for Concrete Construction and Materials* — CIP concrete tolerances (slab flatness, plumb, level). Source: concrete.org.
- **SMACNA** *HVAC Duct Construction Standards — Metal and Flexible* (current edition) — sheet metal fabrication and installation tolerances. Source: smacna.org.
- **TMS 402 / 602** for masonry tolerances; **AAMA / FGIA** for glazing installation tolerances; **AWI** for architectural woodwork tolerance grades (Custom / Premium).

### Code references for clearance, access, and life safety

- **IBC 2024** (International Code Council). Specifically: §602 (construction types), §714 (penetrations of rated assemblies), §1023 (interior exit stairways and ramps), §3306 (pedestrian protection during construction). Source: codes.iccsafe.org.
- **IECC 2024** — energy code references that affect mechanical equipment selection and envelope choices in the long-lead window. Source: codes.iccsafe.org.
- **NEC 2023 (NFPA 70)** — §110.26 (working space about electrical equipment), §240, §408. Source: nfpa.org.
- **NFPA 241-22** *Standard for Safeguarding Construction, Alteration, and Demolition Operations* — fire watch, sprinkler activation phasing, hot-work, temporary heat. Source: nfpa.org.
- **OSHA 1926** Construction Industry standards. Specifically: Subpart M (fall protection), Subpart P (excavations / shoring), Subpart R (steel erection), Subpart V (electrical). Source: osha.gov.

### Healthcare-specific

- **ASHRAE 170-2021** *Ventilation of Health Care Facilities* — ventilation design and during-construction air-pressure relationships. Source: ashrae.org.
- **FGI Guidelines 2022** — *Guidelines for Design and Construction of Hospitals* and *...of Outpatient Facilities*. Includes ICRA (Infection Control Risk Assessment) framework for occupied-building healthcare construction. Source: fgiguidelines.org.

### Procurement / lead times

- **No bundled lead-time table is reliable.** See `long_lead_items_2026.md` for the methodology of building a project-specific lead-time register from current, dated, manufacturer-named sources.
- Industry signal sources: AGC of America Construction Inflation Alert; AISC market quarterly; ENR Construction Cost Index commentary; manufacturer customer letters (Eaton, Schneider Electric, ABB, Siemens, Trane, Daikin Applied, Carrier, Otis, KONE, ThyssenKrupp).

---

## NA AHJ references for phased / occupied-building findings

When a finding cites a temporary-condition rule, name the AHJ explicitly:

- **NYC DOB** — occupied-building protocols, sidewalk shed requirements (NYC BC + DOB rules), construction permit phasing.
- **FDNY** — fire watch requirements during construction in occupied buildings.
- **CA HCAI** (formerly OSHPD) — California healthcare facility design and construction approval. Phased healthcare work in California requires HCAI staged approvals.
- **DSA** (Division of the State Architect) — California K-12 and community college construction approvals.
- **GSA** (US General Services Administration) — federal tenant-occupied protocols, P-100 *Facilities Standards*.
- **USACE** — US Army Corps of Engineers UFC (Unified Facilities Criteria) for federal projects.
- **NAVFAC** — Naval Facilities Engineering Command for Navy / USMC projects.
- **NYC SCA** — School Construction Authority for NYC public schools; summer-only construction windows are common.
- **State DEP / DEC** — for stormwater discharge, dewatering permits, and site-disturbance thresholds.

---

## Coverage of this skill's reference bundle

| Reference file | Covers |
|---|---|
| `constructability_axes.md` | Eight-axis framework (synthesized), sub-criteria, common failure modes, example findings, NA tolerance / clearance citations |
| `long_lead_items_2026.md` | Methodology for building a project-specific long-lead register from named, dated, manufacturer-issued quotes — **not** a lookup table |
| `_provenance.md` | This file — practice references, framework disclaimers, AHJ list |

**Out of bundled scope** (the skill does not include and should not pretend to include):

- A numbered AGC or CMAA constructability checklist (does not exist as such).
- Current vendor-specific lead-time numbers (must be quoted per project).
- Cost estimates beyond order-of-magnitude CO ranges for example findings (use a cost estimator).
- Code analysis beyond the constructability-relevant clearance / tolerance / temporary-works references (use `code-compliance-review`).
- BIM clash-detection output (constructability is informed by clash detection but not equivalent to it).

---

## Verification status

- **Last verified (publishers, edition years, AHJ list):** 2026-05-09.
- **Update trigger:** when ICC publishes the next IBC / IECC edition; when NFPA, NEC, AISC, ACI, ASHRAE, FGI publish the next edition of their cited standard; when AGC or CMAA publishes a substantive update to preconstruction guidance; or when an AHJ on the list undergoes a name change or reorganization (e.g., OSHPD → HCAI in 2022).
- **Edition pin warning:** the references list **specific edition years** (IBC 2024, IECC 2024, NEC 2023, AISC 303-22, ACI 117, NFPA 241-22, ASHRAE 170-2021, FGI 2022). When a project is on a different adopted edition (e.g., a state still on IBC 2021 with state amendments), cite the adopted edition in the finding, not the bundled edition. Verify the adopted edition with the AHJ before sealing the review.

---

## How to verify (manual)

1. For each cited code or standard above, confirm the edition year against the publisher's current edition page (icc.codes, nfpa.org/codes-and-standards, aisc.org, concrete.org, ashrae.org, fgiguidelines.org).
2. For AGC and CMAA framing, confirm that the publication titles cited still exist on agc.org and cmaanet.org.
3. For the AHJ list, confirm names by querying the agency portal (e.g., hcai.ca.gov; previously oshpd.ca.gov).
4. If any edition has advanced beyond the year cited, update the relevant reference file's citations and re-pin the last-verified date here.
