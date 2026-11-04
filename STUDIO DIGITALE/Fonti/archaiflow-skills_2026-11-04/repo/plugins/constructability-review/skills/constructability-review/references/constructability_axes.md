# Constructability Review — Eight Axes

Detailed framework for auditing construction documents through a CM / preconstruction / owner's-rep lens. Each axis carries sub-criteria, common failure modes, and example findings phrased the way they should appear in the review file.

Severity tagging: **High** (will cause a CO or schedule slip if not addressed before CD), **Medium** (likely to surface as RFI in CA), **Low** (worth noting, resolvable without redesign).

The 8-axis structure is an internal synthesis informed by AGC of America preconstruction publications, CMAA *Construction Management Standards of Practice* (preconstruction services chapter), and the published tolerance / clearance / safety standards cited per axis below (AISC 303-22, ACI 117, SMACNA, NEC 2023, NFPA 241-22, IBC 2024, OSHA 1926, ASHRAE 170-2021, FGI 2022). **Note:** AGC and CMAA do not publish a numbered constructability rubric with this exact axis decomposition — see `_provenance.md` for the framework disclaimer and the verification list of practice references.

---

## 1. Trade sequencing & critical path

**Sub-criteria:**

- Implied sequence physically possible — predecessors completed before successors require them.
- Out-of-sequence work flagged (e.g., framing before MEP rough-in inside a tight cavity).
- Concurrent work in the same volume — physical conflicts during install.
- Hand-off cleanliness — when Trade A leaves and Trade B starts, what condition is the surface in?
- Protection requirements during follow-on work.

**Common failure modes:**

- Spec calls for sealed concrete floor to receive resilient flooring, but the floor is the staging area for steel deck topping — protection cost not in scope.
- Curtain-wall install requires the slab to be cured 28 days; schedule shows install at day 21.
- Drywall before MEP rough-in tested — coordination meetings the only place this surfaces, and not always.

**Example finding:**

> [High] Detail 5/A8.04 shows acoustic ceiling tile installed before final MEP testing. Light fixtures on the AV signal path require de-mount and re-mount for fixture-by-fixture testing. Recommend revising Section 09 51 13 sequencing language to require ACT install after MEP commissioning, or accept the de-mount cost in CA contingency. Estimated CO if surfaced in CA: $35-50K.

---

## 2. Tolerance stack-up

**Sub-criteria:**

- Cumulative tolerance from structure to finish vs. detail accommodation.
- Steel ±¼" (AISC 303), CIP concrete ±¼" to ±¾" (ACI 117), masonry ±¼" plumb 10 ft, sheet metal ±⅛" (SMACNA), glazing manufacturer's installation tolerance.
- Detail "reveals" and "shadow gaps" sized to absorb tolerance — typical 3/8"+ reveal absorbs 3/8" of variance.
- Adjustability of attached assembly (shimming range, slotted holes, gasketed joints).

**Common failure modes:**

- Steel + deck + topping + acoustic substrate stack adds to ¾" of variance; detail shows 1/8" reveal.
- Curtain-wall manufacturer's installation tolerance is ±1/4" but the wall returns into a punched opening with 1/16" reveal callout.
- Granite cladding pinned to steel with no adjustability — survey deviation forces shop-rework.

**Example finding:**

> [High] Detail 7/A8.21 storefront-to-slab transition: 1/8" reveal callout at slab edge. Stack: AISC 303 steel ±¼" + topping ±⅛" + storefront install ±¼" = ±5/8" cumulative. Detail accommodates ±1/8". Either widen reveal to 3/8"+ or specify shimming range and slotted attachment in Section 08 41 13. Estimated CO if surfaced as RFI in CA: $25-45K plus 2-3 weeks of redesign.

---

## 3. MEP coordination & rack space

**Sub-criteria:**

- Above-ceiling clear height accommodates duct + sprinkler + cable tray + lighting in real coordination, not just BIM-clashed.
- Riser stack alignment story-to-story.
- Shaft enclosure penetrations within rated-assembly limits per IBC.
- Equipment-room dimensions accommodate install AND future replacement.
- Service clearance for code (NEC 110.26 for electrical), maintenance, and removal route.

**Common failure modes:**

- 8'-0" finish ceiling with 24" round duct + 8" sprinkler + 8" tray + 8" lighting requires 14'-0" structure-to-ceiling. Not provided.
- AHU room sized for install but no removal path through corridor doors.
- Riser shaft sized for risers but no maintenance access door at each floor.

**Example finding:**

> [High] AHU-3 mechanical room (Sheet M2.04) door is 36 in wide. AHU-3 specified is 38 in wide. Removal route blocked. Either widen door, change AHU type, or accept AHU is not removable without wall demo. Same condition at AHU-5 and AHU-7. Recommend coordinated revision before 100% CD.

---

## 4. Install access & rigging

**Sub-criteria:**

- Crane / boom-truck reach for steel and pre-cast erection.
- Hoisting paths through future façade openings (or via exterior crane).
- Equipment-room dimensions for AHU / chiller / switchgear installation.
- Future-replacement removal route (the "30-year question" — when this AHU dies, can the next one come in).
- Site access for delivery vehicles (turning radius, vertical clearance, weight capacity of overhead structure).

**Common failure modes:**

- Crane swing radius required but neighbor airspace not yet negotiated.
- Switchgear room access through a stair hall that turns — gear cannot make the turn.
- Roof-mounted chiller scheduled for placement after parapet is built.

**Example finding:**

> [High] Roof chiller delivery: schedule shows chiller hoisting on day 145 (per CPM); parapet wall placement is day 130. After parapet is in, chiller hoisting requires either (a) lift over the parapet (additional crane mobilization $40K), or (b) leaving a parapet panel out, hoisting, then closing. Recommend revising sequence to hoist chiller before parapet completion — saves $40K.

---

## 5. Lay-down & site logistics

**Sub-criteria:**

- Material storage area on-site or off-site lease cost.
- Truck deliveries: frequency, time-of-day restrictions, restricted streets.
- Crane swing radius respects neighbor airspace; airspace easements negotiated where required.
- Pedestrian protection per IBC, OSHA 1926 Subpart M, local DOB / DSA / agency requirements.
- Construction parking, worker access, lunch break logistics.
- Neighbor noise / vibration limits per local ordinance and AHJ.

**Common failure modes:**

- Urban infill site has zero lay-down — every delivery is just-in-time, weather-dependent, escalates GC.
- Crane swing over neighbor parcel without airspace easement — neighbor blocks operation.
- Loading dock adjacent to a daycare with noise restrictions during specific hours.

**Example finding:**

> [Medium] Zero on-site lay-down; existing parking and adjacent vacant lot (off-site lease pending owner negotiation). Without lay-down lease secured before NTP, deliveries become just-in-time and labor productivity reduces ~10-15%. Estimated cost increase if lay-down not secured: $200-400K over 18-month build. Recommend adding lay-down lease to the owner pre-construction commitments.

---

## 6. Temporary works

**Sub-criteria:**

- Shoring for excavation per OSHA 1926 Subpart P, local DOB / DSA / agency requirements.
- Dewatering capacity vs. groundwater rate.
- Weather enclosure for winter concrete or interior finishes.
- Life-safety path during construction — egress paths, sprinkler activation phasing, fire watch per NFPA 241.
- Temporary heating, lighting, and power.
- Snow removal and ice management on the site.

**Common failure modes:**

- Excavation shown in February in a freezing climate with no winter-concrete provisions in the spec.
- Dewatering requires a discharge permit that has 4-month lead time; not flagged.
- Sprinkler activation deferred until 90% completion; OSHA 1926 / NFPA 241 require operational system or fire watch from materials-installation start.

**Example finding:**

> [High] Schedule shows concrete pour from December through February in Climate Zone 5A. Section 03 30 00 contains no winter-concrete provisions (heated enclosure, blanket cure, accelerator, hot mix). Either add winter-concrete spec language or shift the pour window to March-November. Estimated cost of winter provisions if retained: $80-150K.

---

## 7. Materials procurement & lead times

Reference: `long_lead_items_2026.md` for the methodology of building a project-specific long-lead register from current, dated, named-source quotes. That file is **not** a lookup table — it is a sourcing methodology. Lead-time values used in a finding must cite manufacturer + quote source + quote date, never a recalled or bundled number.

**Sub-criteria:**

- Long-lead items identified and their decision-freeze dates set in the schedule.
- Procurement releases at NTP for items that need it (not waiting for 100% submittal cycle).
- Backup vendors identified for single-source long-leads.
- Substitution risk if primary vendor slips.

**Common 2026 long-lead categories** (no specific lead-time numbers are listed here on purpose — see methodology note below):

- Electrical switchgear (LV and MV), MCCs, generators, transformers, ATS.
- AHUs (custom > catalog), chillers, cooling towers, boilers, VRF systems, large pumps.
- Custom unitized curtain wall, oversized IGUs, custom skylights, decorative metal panels.
- Elevators (new and modernization).
- Structural steel (mill + fab), mass timber (CLT / glulam), pre-cast concrete.
- Owner-furnished medical / lab equipment (linacs, MRI, fume hoods, biosafety cabinets).

**Methodology note — do not bake lead-time numbers into a finding from recall:** values listed in any reference document are illustrative only. Pull current, dated, named-source quotes per the methodology in `long_lead_items_2026.md`. Each lead-time number used in a constructability finding must cite the manufacturer + quote source + quote date — never a recalled or table-baked figure. Verify with the manufacturer (or fabricator, for steel and mass timber) at review time.

**Common failure modes:**

- Switchgear submittal scheduled at 100% CD; project NTP is 6 months later — switchgear arrives 6 months after needed.
- Custom curtain wall design coordinated with shop drawings during CA — fabrication doesn't start until shop approval, install slips.

**Example finding:**

> [High] Electrical switchgear: contract documents are at 75% CD. Per Eaton customer lead-time letter dated 2026-04-12 (entered into the project lead-time register), current lead time for the specified low-voltage switchgear is 48 weeks. Schedule places switchgear energization at month 16 from NTP. To make this work, the gear must be ordered no later than month 16 - 48 weeks ≈ month 4. Currently the schedule shows order release after submittal approval at month 9. Either accelerate switchgear procurement (release at month 4 against 75% CD with explicit redesign risk allocation) or reschedule energization to month 21+. Estimated cost of acceleration vs. reschedule: $0 vs. ~$300K (5 months of GC overhead). Re-confirm the Eaton number at order release — the 2026-04-12 letter will be ~120 days old by month 4. (Source-quote methodology: see `long_lead_items_2026.md`.)

---

## 8. Phased operations & owner occupancy

**Sub-criteria:**

- Owner-occupied phasing — temporary-condition floor plans coordinated.
- Means of egress maintained during all construction phases.
- Mechanical of patient/student transitions (MOP) documented.
- Infection-control risk assessment (ICRA) for healthcare per ASHRAE 170 / FGI Guidelines.
- Security boundaries between construction and occupied areas.
- Neighbor noise / vibration limits during operating hours.
- AHJ approval for temporary conditions (NYC DOB occupied-building protocols, CA HCAI for healthcare, school-district summer-only windows, GSA tenant-occupied protocols).

**Common failure modes:**

- Schedule assumes 24/7 site access; owner is a school with summer-only construction window.
- Healthcare project with no ICRA dust-control specification.
- Phased plan blocks one of the two required exit paths during the phase.

**Example finding:**

> [High] Phase 2 (Sheet G2.04): East corridor closed for renovation; remaining egress is West corridor only. Travel distance from Room 312 (Level 3) to West corridor exit is 232 ft per re-measurement. IBC 2021 Table 1017.2 sprinklered B limit is 250 ft, marginally compliant — but the West corridor also serves Phase 2 staging area, narrowing to 36 in clear width per the staging plan. Recalculate occupant load served and confirm ≥0.2 in/occupant capacity in the temporary condition. Recommend a phased life-safety plan reviewed by the AHJ before NTP.
