# Brief Review — Eight Axes

Detailed framework for interrogating an architectural project brief, RFP, or OPR. Each axis carries sub-criteria, common failure modes, and example findings phrased the way they should appear in the review file.

---

## 1. Stated vs unstated objectives

What the owner asks for vs what the building type / market / regulatory context implies they actually need.

**Sub-criteria:**

- Project's primary objective stated in one sentence?
- Secondary objectives ranked or weighted?
- Implicit objectives (brand, recruiting, donor signaling, post-occupancy resale) named or hidden?
- Success metrics defined (occupancy rate, EUI, cost per seat, time-to-market)?

**Common failure modes:**

- Brief lists 12 priorities with no ranking — every priority becomes top priority, design has no signal.
- Brief omits the actual driver (e.g., a tax deadline, a board mandate, a competitor opening) that will dominate every decision.
- Brief states "iconic design" without defining what the icon must communicate or to whom.

**Example finding:**

> Brief lists "flexibility, sustainability, identity, cost certainty, and speed" as priorities of equal weight. In a public school RFP, cost certainty and AHJ-driven schedule typically dominate; the brief should rank explicitly or accept that early design will surface trade-offs.

---

## 2. Program completeness

**Sub-criteria:**

- Net assignable area (nsf) per program element?
- Gross-to-net ratio assumption stated?
- Population per space (ASHRAE 62.1 occupant density basis)?
- Adjacencies stated or only implied?
- FF&E in or out of scope?
- Growth assumption (10% over 10 years? Shell space? Vertical expansion?)?
- Support spaces accounted for (loading, MEP, IT, building maintenance, custodial)?

**Common failure modes:**

- Program lists rooms but no areas.
- Total gsf stated, no breakdown.
- No FF&E coordination, surprises in CD.
- Gross-to-net ratio unrealistic for building type (see `program_benchmarks.md`).

**Example finding:**

> Brief lists 32 classrooms at 850 nsf each (27,200 nsf), but no figure for support spaces. K-12 buildings typically run 1.5-1.7 gross-to-net (DOE FRPP averages); expect the actual gsf to land near 41,000-46,000 gsf, not the 32,000 implied.

---

## 3. Site & jurisdiction context

**Sub-criteria:**

- Address and parcel ID present?
- Zoning district named with applicable overlay districts?
- AHJ named (which building department, fire marshal, plan review process)?
- Code edition explicit (IBC year + state amendments + local amendments)?
- ASHRAE 169 climate zone identified?
- Utility providers (electric, gas, water, sewer, telecom) named with capacity assumptions?
- Easements, setbacks, height limits, FAR, lot coverage stated or referenced?
- Survey availability and currency (within 12 months)?
- Geotech availability?

**Common failure modes:**

- "Subject to applicable codes" with no edition.
- Zoning compliance assumed without referencing the variance/special-permit history of the parcel.
- No mention of utility capacity — large MEP loads added in DD without confirming service.

**Example finding:**

> Brief references "current building code" without citing edition. Project is in California — IBC 2021 with 2022 California amendments (CBC 2022) is in effect through Dec 2025; if construction documents are issued after Jan 2026, CBC 2025 applies. Confirm the assumed edition before establishing structural and life-safety basis.

---

## 4. Performance criteria

**Sub-criteria:**

- Energy target (EUI in kBtu/sf/yr, or % below ASHRAE 90.1 baseline) measurable?
- Certification target named and current version (LEED v4.1, WELL v2, Living Building v4, Fitwel, Passive House PHIUS+ 2021, RELi 2.0)?
- Commissioning scope per ASHRAE Guideline 0 + LEED EAp1?
- Indoor environmental quality targets (CO2 ppm, daylight metric — sDA/ASE, acoustic NC)?
- Embodied carbon target (kgCO2e/m² A1-A3, EC3 baseline)?
- Water target (LEED WEp1 baseline reduction, water reuse)?
- POE protocol named (CBE Occupant Survey, BUS, etc.)?

**Common failure modes:**

- "LEED Gold" stated, no commissioning budget — Gold is unachievable without EAp1.
- "Net zero" with no scope (operational? embodied? site-only? offset-allowed?).
- Daylight target with no metric ("good daylight" ≠ "sDA300/50% on 75% of regularly occupied area").
- No POE — project never learns whether targets were met.

**Example finding:**

> Brief states "LEED Gold target" but lists commissioning as owner-furnished out-of-scope. EAp1 (Fundamental Cx) is a prerequisite — Gold is not certifiable without it. Confirm Cx budget or remove the LEED commitment.

---

## 5. Schedule & budget realism

**Sub-criteria:**

- Total budget stated (hard + soft + FF&E + contingency)?
- Cost per gsf reasonable for project type and region (cross-check `program_benchmarks.md`)?
- Contingency level appropriate to project phase (10-15% at SD, 5-10% at CD)?
- Schedule includes AHJ review (weeks-to-months depending on jurisdiction)?
- Long-lead procurement identified (switchgear, AHUs, custom glazing, elevators)?
- Owner decision lag accounted for (typical 1-3 weeks per major decision)?

**Common failure modes:**

- Budget at $300/gsf for a Type II hospital ($800-1200/gsf is typical).
- Schedule shows permit issued in 4 weeks for a project that historically takes 6+ months in that AHJ.
- No escalation — project starts in 2026 at 2024 pricing.
- Soft costs (A/E fees, permits, surveys, geotech, owner's rep, FF&E coordination) underbudgeted — typical NA range is 18-28% of construction cost.

**Example finding:**

> Brief sets construction budget at $250/gsf for a Type IIB R-2 multifamily mid-rise in the Bay Area. RSMeans Q1 2026 indicates $380-450/gsf for that typology in that region. Either reduce program by ~40% or escalate the budget assumption before committing to the brief.

---

## 6. Decision rights & governance

**Sub-criteria:**

- Single point of contact (SPOC) on owner side?
- Sign-off authority at each phase (SD, DD, CD, CA, closeout)?
- Internal owner committees and their meeting cadence?
- Board approval gates (frequency, lead time required)?
- Public-engagement stages required (community board, planning commission)?
- Decision turnaround SLA (e.g., owner responds within 5 business days)?

**Common failure modes:**

- "The owner" with no name — design team chases multiple voices.
- Board meets quarterly, not flagged — every major decision delays project 3 months.
- No SLA on owner decisions — schedule slip blamed on design team.
- Public hearings discovered late, adding 6-9 months.

**Example finding:**

> Brief names "the building committee" as the approver but does not state membership, meeting cadence, or whether SD/DD/CD sign-off is by individual or by committee vote. With committee-vote sign-off and a quarterly cadence, the schedule must include four quarterly gates (~12 months) before issue-for-permit.

---

## 7. Risk & exclusions

**Sub-criteria:**

- Out-of-scope list explicit?
- Hazardous materials assumption (Phase I ESA results referenced, lead/asbestos/PCB scope assigned)?
- Geotech: who pays, when commissioned, who selects the firm?
- Existing-conditions verification: who measures, what tolerance?
- Demolition scope and salvage assumptions?
- Permit and impact fees: owner or A/E budget?
- Owner-furnished items (FF&E, AV, signage, art)?
- Force majeure / supply chain assumptions (post-2020 materials lead times)?

**Common failure modes:**

- "Subject to existing conditions" with no Phase I — surprises in DD.
- Geotech assumed favorable — pile foundations discovered at 80% CD.
- Owner-furnished AV not coordinated — coordination drawings issued after CD.

**Example finding:**

> Brief lists "abatement of any hazardous materials" as included but does not reference a Phase I ESA. For a 1965 building, lead-based paint and ACM are likely; without a Phase I baseline the abatement cost is unbounded. Recommend Phase I + targeted Phase II as a precondition to firming up the construction budget.

---

## 8. Sustainability & resilience

**Sub-criteria:**

- Net-zero pathway scoped (operational, embodied, site, or both)?
- Climate hazards addressed (flood, wind, heat, wildfire, seismic, drought)?
- Adaptive reuse vs new build trade-off considered (especially for embodied carbon)?
- Resilience targets (passive survivability hours per ASHRAE Standard 100, RELi credits)?
- Backup power, water, and life-safety strategy for projected hazards?
- Supply chain and materials sourcing constraints (e.g., low-carbon concrete, FSC wood)?

**Common failure modes:**

- "Sustainable design" with no metric.
- Climate risk treated as future problem — no flood elevation update, no heat-wave scenario.
- Embodied carbon ignored when it is 40-60% of the building's lifetime CO2.

**Example finding:**

> Brief states "resilient design" as a priority but does not name the design hazards. Project site is in Zone AE per FEMA FIRM 12345C0234J with a BFE of +9 ft NAVD88. The brief should specify Design Flood Elevation (BFE + freeboard, typically 1-3 ft), and reference ASCE 24-14 for flood-resistant design. Until the brief names the hazards it is designing against, "resilient" is not a requirement anyone can price or verify.
