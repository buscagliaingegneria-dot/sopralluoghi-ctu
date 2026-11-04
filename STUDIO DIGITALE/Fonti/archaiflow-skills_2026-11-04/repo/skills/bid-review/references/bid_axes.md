# Bid Review — Eight Axes

Detailed framework for reviewing contractor bids (GC base bids, sub-bids, design-build proposals, alternates) during the procurement phase. Each axis carries sub-criteria, common failure modes, and example findings phrased the way they should appear in the review file.

Aligned with AIA A101 / A102 / A103 / A201, AIA A305 Contractor's Qualification Statement, AIA A312 Performance Bond, EJCDC C-410 Bid Form, and standard ITB / Division 00 / 01 conventions.

---

## 1. Base-bid scope completeness

**Sub-criteria:**

- All scopes in the ITB / drawings / specs reflected in the bidder's bid form.
- "By others" or "NIC" tags consistent with what the contract scope says is by others.
- Allowance items separately identified with cap.
- Owner-furnished, contractor-installed (OFCI) items coordinated.
- Soft-cost items (permits, fees, testing, third-party inspections) per the ITB.

**Common failure modes:**

- Bidder excludes "site utilities beyond 5 ft of building" but ITB calls site utilities through the project boundary.
- "By others" used for a scope clearly drawn (e.g., interior signage shown on A-series drawings is excluded as "owner signage package").
- Allowances stated without unit-price adjustment mechanism.

**Example finding:**

> Bidder ABC Page 6 Item 3: "Site work limited to 5 ft outside the building footprint; utilities beyond by owner." ITB §01 11 00 Part 1.03.B explicitly includes "all utilities to the property line." Estimated impact: $185K based on the engineer's estimate for the omitted scope. Add to leveling table.

---

## 2. Qualifications & exclusions

**Sub-criteria:**

- Bidder's clarifications reasonable — assumptions about hazardous materials, unsuitable soils, owner-furnished items, weather, supply chain, escalation.
- Exclusions itemized vs. buried in cover letter.
- Assumptions transferred risk back to owner (e.g., "assumes existing slab is sound") — each is a contingency the owner now carries.

**Common failure modes:**

- "Excludes hazardous materials of any kind" with no Phase I ESA result. Risk fully on owner.
- "Assumes 30 inches of frost penetration" — if local frost line is 42 in, the foundation cost is light.
- Boilerplate "subject to mutually acceptable contract" — every contract term is open.

**Example finding:**

> Bidder DEF cover letter qualifies bid as "subject to existing slab being sound and not requiring removal beyond cosmetic patching." Phase II testing (per Section 02 21 00 testing report dated 2026-04-15) found 12% of the slab area requires partial-depth removal. Estimated removal cost from engineer: $94K. Add to leveling table; include in pre-award negotiation list.

---

## 3. Alternates

**Sub-criteria:**

- Add/deduct alternates priced individually and clearly.
- Pricing internally consistent — Alt 1 deduct vs Alt 2 add for the same area shouldn't double-count.
- Alternate selection sensitivity documented — which combination of alternates gives the best owner value.
- Alternate language matches Section 01 23 00 alternates schedule.

**Common failure modes:**

- Alternate pricing very different across bidders (signal that the alternate is poorly defined in the spec).
- Alternates include scope that should have been base-bid (loading the alternate to make base-bid look low).
- Combined alternates priced together without unit-by-unit breakout.

**Example finding:**

> Alternate 3 (deduct exterior insulated metal panel rainscreen, substitute brick veneer): Bidder ABC -$82K, Bidder DEF -$310K, Bidder GHI -$45K. The 7× spread suggests the alternate spec scope is ambiguous. Recommend issuing a clarification addendum re-pricing Alt 3 against a tight scope before award.

---

## 4. Unit prices & allowances

**Sub-criteria:**

- Unit prices for items the ITB requires (rock excavation per CY, structural-steel adjustment per ton, finish-upgrade adjustment per sf).
- Unit prices defensible against `bid_benchmarks.md` ranges for the region.
- Allowances stated with cap and unit-price adjustment mechanism.

**Common failure modes:**

- Unit prices loaded high (e.g., rock excavation quoted well above the published regional range) — contractor wagering on overrun-recovery. Pull the published range from RSMeans / regional firm before deciding "too high."
- Unit prices loaded low (e.g., structural-steel adjustment quoted well below published $/lb) — contractor wagering on no-overrun or misreading scope. Pull the published range before deciding "too low."

**Example finding:**

> Bidder ABC unit price for rock excavation: $400/CY. Regional benchmark from RSMeans 2026 Q1 RCI-adjusted for the project MSA (pulled into `docs/bids/<slug>-benchmarks.md`): [low]-[high] $/CY. If the geotech indicates 200 CY of probable rock, the delta between bidder unit price and the published mid-range × probable quantity is the owner's exposure if rock is encountered. Recommend negotiation toward the published range or accept with a written cap. **Pull the published range from RSMeans / regional firm before sending — do not fill in numbers from recall.** See `references/bid_benchmarks.md` for the publisher list and worked-example format.

---

## 5. Schedule & milestones

**Sub-criteria:**

- Substantial completion date acknowledged and matches the ITB.
- Liquidated-damages rate accepted (per AIA A101-2017 §5.1.5 / Supplementary Conditions, or as negotiated). Note: A101 §6 covers termination, not LDs — do not cite §6.5 for liquidated damages.
- Weather-day allowance reasonable for the region and season.
- Phased turnover dates if owner needs partial occupancy.
- Long-lead procurement commitments — bidder's plan to release procurement at NTP.

**Common failure modes:**

- Bidder schedule 30 days longer than ITB target with no explanation; LDs at $5K/day = $150K not in bid.
- Weather-day allowance excessive ("up to 60 weather days") in a region averaging 12.
- Long-lead releases tied to "owner approval of submittals" without an SLA on owner — schedule risk on owner.

**Example finding:**

> Bidder DEF schedule: substantial completion 30 calendar days after ITB-required date. Liquidated damages per AIA A101-2017 §5.1.5 / Supplementary Conditions: $4,500/day. Net schedule cost: $135K. Add to leveling. Confirm whether the schedule slip is structural (long lead) or aggressive bidding (compressed schedule the bidder cannot actually meet).

---

## 6. Contractor qualifications

**Sub-criteria:**

- AIA A305 Contractor's Qualification Statement or equivalent submitted.
- Bonding capacity ≥ contract value × the multiple required by ITB (typical 1.5×-2×).
- Insurance limits per A201 §11 / Division 01 — general liability, auto, umbrella, workers comp, builders risk.
- Similar-project experience: 3+ projects of similar size, type, region, recency (last 5 years).
- Key personnel committed — superintendent and project manager named, with résumés showing relevant experience.
- Subcontractor list with each sub's pre-qual status (current bond, insurance, license).

**Common failure modes:**

- Bonding capacity letter dated >90 days old.
- Similar projects listed are 12 years old or different building type.
- Superintendent named but committed to two concurrent projects.

**Example finding:**

> Bidder GHI bonding capacity letter dated 2025-11-04 (6+ months old). Contract value $24M. ITB §00 21 00 requires current bonding letter ≤90 days old. Request updated letter before award; if capacity has tightened, this may flip the recommendation.

---

## 7. Bid form completeness & responsiveness

**Sub-criteria:**

- All addenda acknowledged on the bid form.
- Bid bond / cashier's check attached at correct percentage (typical 5% public, 10% some private).
- Required signatures and notarization.
- MWBE / DBE goal met or good-faith documentation included.
- Non-collusion affidavit and any agency-required certifications.
- On public projects, anything making the bid non-responsive is fatal.

**Common failure modes:**

- Addendum 4 missing from acknowledgment list — bid is non-responsive on public projects.
- Bid bond at 5% on a private project that required 10%.
- MWBE goal of 25% missed and no good-faith documentation.

**Example finding:**

> Bidder ABC bid form acknowledges Addenda 1, 2, 3 (Addendum 4 issued 2026-04-22 not listed). Per ITB §00 21 00 Part 1.05.D, failure to acknowledge all addenda renders the bid non-responsive on this public project. Procurement counsel must determine whether this is a curable defect or fatal. If fatal, the apparent low award shifts to Bidder DEF.

---

## 8. Contract-terms alignment

**Sub-criteria:**

- Bidder accepting the AIA A101 / A102 / A103 / agency form as-is, or proposing exceptions.
- Insurance limits matching A201 / Division 01 — both umbrella and primary.
- Indemnification clause acceptance.
- Retainage % and reduction milestone (typical 10% reduced to 5% at substantial completion).
- Payment terms (net days from approved pay app).
- Dispute resolution (mediation per A201 §15.3, arbitration per §15.4 if elected, litigation otherwise).
- Warranty terms — contract calls for 1-year general warranty per A201 §3.5; bidder may have proposed shorter or longer.
- LD / bonus structure if any.

**Common failure modes:**

- "Subject to mutually acceptable contract" — every term open.
- Insurance limits proposed lower than A201 baseline (e.g., $1M umbrella vs. $5M required).
- Indemnification "to extent of bidder's negligence" with no joint-and-several language.
- Retainage proposed at 5% throughout — contractor finance preference, owner exposure increase.

**Example finding:**

> Bidder DEF proposed contract exception: "Retainage at 5% throughout, no reduction trigger." A101-2017 §5 baseline is 10% reduced at substantial completion. The 5% reduction throughout is a $1.2M owner exposure increase on a $24M project. Either negotiate to A101 baseline or price the exposure into the leveling.
