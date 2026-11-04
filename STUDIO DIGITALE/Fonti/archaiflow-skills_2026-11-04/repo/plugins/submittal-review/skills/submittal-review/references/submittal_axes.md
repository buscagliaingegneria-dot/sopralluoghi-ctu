# Submittal Review — Eight Axes

Detailed framework for reviewing contractor submittals (shop drawings, product data, samples, mockups, schedules) during construction administration. Each axis carries sub-criteria, common failure modes, and example findings phrased the way they should appear in the review file.

Aligned with AIA A201-2017 §3.12, AIA G712 (Shop Drawing & Sample Record), AIA B101-2017 §3.6.4, and CSI MasterFormat / SectionFormat conventions.

---

## 1. Contract-document conformance

The core review question: does the submitted item match what the contract drawings and specifications require?

**Sub-criteria:**

- Sheet/detail references on the submittal resolve to the actual contract drawings.
- Spec-section references on the submittal resolve to the actual spec section issued for construction.
- Product matches basis-of-design or qualifies as an "or equal" with comparison data.
- Dimensions, finishes, materials, and methods match the contract documents.

**Common failure modes:**

- Submittal references "as shown on contract drawings" without specific sheet/detail callouts.
- Contractor markups silently change a contract dimension or detail (e.g., reveal width changed from 1/2" to 3/4" with no annotation).
- Drawings reference an old spec section number that has been superseded.

**Example finding:**

> Submittal sheet S2.01 shows storefront vertical mullion at 6 in profile, but contract Detail 3/A8.21 calls for 4 in profile per Section 08 41 13 Part 2.2.B. Contractor must conform to the 4 in profile or submit a substitution form per Section 01 25 00.

---

## 2. Completeness against spec submittal article

Each spec section's submittal article (typically Part 1.04 or 1.05) lists what must be submitted. Confirm each item.

**Sub-criteria:**

- Shop drawings (where required) — plans, elevations, sections, details.
- Product data — manufacturer's printed data sheets with the proposed model highlighted.
- Samples — physical samples for color, finish, texture per spec.
- Mockup confirmation — for sections requiring mockups, evidence of mockup approval.
- Test reports — UL listings, ICC-ES reports, ASTM test data, NFPA listings, AAMA performance.
- Calculations — engineering calculations stamped by a licensed engineer (e.g., guardrail loads, anchor design).
- Warranties — sample warranty form per the spec warranty article.
- Maintenance / O&M data — at the closeout phase per Section 01 78 23.
- LEED / certification documentation — per Section 01 81 13 (or Section 01 35 16 in some masters).

**Common failure modes:**

- Submittal includes shop drawings but omits the product data sheet — contract requires both.
- Sample submitted but not the size or quantity specified.
- Engineering calcs unstamped or stamped by an engineer without license in the project's jurisdiction.

**Example finding:**

> Section 07 27 26 Part 1.05.B requires submission of (1) product data, (2) shop drawings showing transitions and terminations, (3) full-size mockup confirmation, and (4) manufacturer's installer certification. Submittal Rev 0 includes only product data. Recommend C-stamp (revise & resubmit) — fabrication should not start with a missing-installer-certification gap.

---

## 3. Dimensions & coordination

**Sub-criteria:**

- Field-verified dimensions noted per A201 §3.12.7 (contractor's responsibility).
- Coordination with adjacent work shown — structural attachments, MEP penetrations, FF&E backing, finish-to-finish transitions.
- Connections to backing / blocking / structure detailed.
- Tolerance to adjacent work within achievable construction tolerance.

**Common failure modes:**

- Dimensions shown to "rough opening" with no field-verification note — fabrication will mis-fit if structure varies from RO assumed.
- Storefront submittal shows attachment to "structural support by others" without backing detail — backing was supposed to be in this submittal scope.
- MEP penetrations through a curtain-wall mullion not coordinated with the MEP contractor's shop drawings.

**Example finding:**

> Submittal Detail 3/S1.01 shows storefront head attachment to "concrete by others" at +12'-0" AFF. Field condition (per RFI #042 response) is steel beam, not concrete. Submittal must be revised to show steel attachment per Section 05 12 00 anchor schedule, with field-verified dimension to top-of-steel.

---

## 4. Performance & product data

**Sub-criteria:**

- Performance criteria match the spec basis-of-design (U-factor, SHGC, VT, STC, fire rating, slip resistance, color fastness, IECC envelope continuity, ASHRAE 90.1 SHGC).
- Test reports current (within the period the standard requires — many ASTM/AAMA reports must be ≤5 years).
- Reference standards cited match the contract spec edition.

**Common failure modes:**

- Performance "meets or exceeds spec" with no test report attached.
- Test report cites an outdated edition of the standard.
- Product data sheet covers a product family; the proposed model isn't highlighted, so the actual performance is ambiguous.

---

## 5. Fabrication feasibility & lead time

**Sub-criteria:**

- Lead time stated and compatible with the construction schedule (procurement window from approval to delivery).
- Fabrication tolerance vs. the contract document tolerance (e.g., contract calls for ±1/16", manufacturer states ±1/8").
- Long-lead components (custom-pull glass sizes, factory-finish lead times) called out separately.
- Sequence-of-operations compatible with the construction schedule baseline.

**Common failure modes:**

- "Lead time 12-16 weeks" but the construction schedule has the install in 8 weeks.
- Manufacturer's tolerance silently looser than contract — joint reveals will read uneven.

**Example finding:**

> Submittal lists "approximate lead time 14 weeks from approval." Construction schedule (baseline rev. 4) places storefront installation 9 weeks after this submittal's approval target. Either accelerate this submittal (which means a B-stamp with no further markup) or update the schedule. Flag for owner / GC discussion before approval stamp.

---

## 6. Code & certification compliance

**Sub-criteria:**

- UL listings cited and current.
- ICC-ES evaluation reports cited with current ESR number.
- NFPA-listed components (sprinklers, fire dampers, fire-rated assemblies).
- IECC envelope criteria (U-factor, SHGC, AAMA test reports for air leakage).
- ADA / ANSI A117.1 dimensional compliance for accessible components (door hardware, lavatory mounting heights, drinking fountain knee/toe clearances).
- AHJ-required certifications (NYC DOB MEA / OTCR, CA OSHPD/HCAI OSP, FDNY COA, USACE UFGS specials).

**Common failure modes:**

- ESR number expired (ICC-ES reports renew on a 3-year cycle).
- UL listing covers a product family; the proposed model isn't covered.
- Fire-damper UL number cited but the application doesn't fall within the listing (e.g., dynamic damper used in static-listed application).

**Example finding:**

> Submittal cites "ICC-ES ESR-3784" for self-tapping anchors. ESR-3784 was reissued in 2023; the cited revision shows a 2019 issuance date. Submit current ESR-3784 (Rev 2023) or substitute another anchor with current ESR.

---

## 7. Deviations, substitutions & "or equal" claims

**Sub-criteria:**

- Substitutions explicitly flagged with side-by-side comparison vs. basis-of-design (per Section 01 25 00 substitution form).
- "Or equal" claims supported with performance data demonstrating equivalence.
- Deviation list at front of the submittal calling out every difference from contract documents.
- Per A201 §3.4.2, contractor warrants equivalent products only when so represented; hidden substitutions void this protection.

**Common failure modes:**

- Submittal product is a different manufacturer than the basis-of-design with no substitution form attached.
- "Equivalent" claimed without a comparison table on performance metrics that the spec actually called out.
- Deviation buried on page 47 of a 60-page product data set.

**Example finding:**

> Submittal product is "Manufacturer XYZ Model ABC" — Section 08 41 13 Part 2.1.B basis-of-design names Manufacturer DEF, "or equal." No substitution form per Section 01 25 00 is attached. This is a hidden substitution per A201 §3.4.2. Recommend C-stamp; require formal substitution form with side-by-side performance comparison before fabrication.

---

## 8. Owner-furnished, contractor-installed (OFCI) coordination

**Sub-criteria:**

- Items the owner is furnishing (FF&E, AV, signage, art, lab/medical equipment) coordinated with this submittal.
- Power / data / structural backing accommodated for OFCI items.
- Delivery coordination — when does owner deliver the OFCI item; when does contractor install.
- Warranty boundaries — owner-furnished warranty vs. contractor-installed warranty; who responds to a failure.

**Common failure modes:**

- Furniture submittal silent on the in-floor power required for the workstations (owner-furnished outlet box, contractor-installed conduit).
- AV mounting in the conference room: contractor's millwork submittal doesn't show the rough-in for the OFCI display.
- Lab equipment submittal shows the equipment but not the floor-loading or vibration-isolation backing required.

**Example finding:**

> Section 12 56 00 furniture submittal shows workstation locations on Level 3 east. In-floor power boxes are owner-furnished per Section 26 27 26 Part 1.04.D; contractor's electrical submittal (separate) must show the rough-in conduit at each workstation location. This furniture submittal should reference and coordinate with electrical Section 26 27 26 Submittal 26-005 (currently under review).
