# VE Assessment — Six Axes

Detailed framework for classifying each proposed VE item as ✅ ACCEPT / ⚠️ ALTERNATE / ❌ BLOCK. Each axis carries sub-criteria, common failure modes, and example findings phrased the way they should appear in the recommendation memo.

The six-axis framework is **internal to this skill** (synthesized — not a published industry standard). It maps to obligations from ASTM E1699 (VE Job Plan), AIA A201-2017 §7 (Changes), AIA B101-2017 §3.6.1.5 (architect's cost review), and CSI MasterFormat 2020.

---

## Axis 1 — Design Intent Impact

**Sub-criteria:**

- Public / identity space vs. back-of-house. Lobby, elevator cab, main stair, conference center, façade — design-intent-loaded. Mech room, IT closet, BOH corridor — neutral.
- Concept-level moves vs. detail moves. Eliminating a wood ceiling in a "warm public lobby" concept = concept loss. Substituting one ACT manufacturer for another = detail.
- Owner brand / signature firm aesthetics. Firm trademarks (e.g., board-form concrete for a specific architect) carry firm risk if cut.

**Common failure modes:**

- VE list does not distinguish location (project-wide finish swap proposed without naming where).
- "Equivalent" substitution is equivalent in cost class but not visual class (custom millwork → stock casework).
- Concept renderings shown to owner depend on the cut item.

**Example finding:**

> Item 14: Substitute white oak veneer wall panels in main lobby with painted MDF. ❌ BLOCK. Lobby is the project's identity space and the owner-approved rendering (issued 2026-02-14) shows wood panels as the central material gesture. Substitution kills concept. *Why: design intent (Axis 1).* Reference: `csi_division_heuristics.md §06 64 00`.

---

## Axis 2 — Performance / Code Impact

**Sub-criteria:**

- IECC envelope (R-value, U-factor, SHGC, air leakage) — cuts to insulation, glazing, air barrier, vapor retarders.
- IBC fire rating (Tables 601, 602, 720) — cuts to gypsum layers, intumescent coatings, rated assemblies.
- IBC egress (Ch. 10) — cuts to door hardware, signage, emergency lighting.
- ADA / ANSI A117.1 — cuts to grab bars, signage, hardware, finishes (slip resistance), fixture types.
- ASCE 7 wind / seismic — cuts to anchorage, bracing, cladding attachment.
- NFPA 13 / 72 — sprinkler density, fire alarm device count.
- Acoustic STC / IIC (multifamily, healthcare, K-12) — cuts to assemblies, isolation pads.

**Common failure modes:**

- Cut drops a R-value below jurisdiction's IECC minimum (e.g., roof R-30 → R-25 in CZ 5).
- Cut eliminates a redundant fire-resistance layer that was required by tested assembly listing.
- Cut substitutes a generic hardware spec for an ADA-compliant set.
- Cut reduces glazing performance and breaks the energy-model COMcheck submitted to AHJ.

**Example finding:**

> Item 22: Substitute fluid-applied air barrier with mechanically-fastened housewrap. ❌ BLOCK. Energy model submitted to NYC DOB on 2026-03-01 assumed 0.04 cfm/sf air leakage achievable only with fluid-applied per NYCECC C402.5. Substitution requires re-submittal + likely rejection. *Why: code performance (Axis 2).* Reference: NYCECC 2020 C402.5.1.2.

---

## Axis 3 — Lifecycle Cost Impact

**Sub-criteria:**

- 20–30 yr O&M cost vs. upfront savings (filters, lamps, refrigerant, repaints, refinishes).
- Warranty length reduction (10-yr roof → 5-yr roof shifts $$$ to year 6).
- Energy / utility cost over the building life (low-eff equipment vs. high-eff).
- Replacement cost trapped behind finishes (waterproofing, blocking, in-slab radiant).

**Common failure modes:**

- VE accepted on equipment capital cost without lifecycle calc (LCCA per ASTM E917 or 10 CFR 436).
- Owner's facilities team not consulted on maintenance burden.
- Warranty change buried in submittal phase.

**Example finding:**

> Item 33: Substitute 20-yr modified bitumen roof with 10-yr 3-ply built-up. ⚠️ ALTERNATE. Upfront savings $48K. 10-yr warranty cost owner approximately $180K NPV in earlier replacement (per RSMeans roof life curves). Recommend owner review LCCA before accepting; if accepted, document reduced warranty in OPR. *Why: lifecycle (Axis 3).* Reference: `csi_division_heuristics.md §07 50 00`.

---

## Axis 4 — Schedule Impact

**Sub-criteria:**

- Does the cut actually save schedule, or trigger redesign (adds AOR / engineer hours), re-permit (AHJ re-review weeks), AHJ alt-means letter (4–8 weeks), shop drawing rework, sub re-pricing?
- Long-lead items already ordered or fabricated — cancellation fees and substitute lead time.
- Coordination cascade (one cut triggers MEP / structural / envelope re-work).

**Common failure modes:**

- VE cut on long-lead equipment (switchgear, custom curtainwall, specialty light fixtures) after release-for-fabrication.
- Cut that requires re-permit but project is in CA — re-permit blocks TCO.
- Cut that "saves $50K" but adds 6 weeks of redesign at $30K of design fees + $400K of GC GC's.

**Example finding:**

> Item 41: Substitute custom curtainwall with stock storefront in floors 2–8. ⚠️ ALTERNATE. Custom CW shop drawings already approved 2026-04-15 (per submittal log #082). Cancellation fee from CW sub = $130K against $310K stated savings. Net $180K savings only if substitute storefront ordered within 3 weeks. *Why: schedule (Axis 4).* Confirm cancellation fee with CM before classifying.

---

## Axis 5 — Risk Transfer

**Sub-criteria:**

- Does the cut shift performance risk from contractor / manufacturer back to owner?
- Does the cut reduce a tested / listed assembly to an unlisted assembly?
- Does the cut shorten warranty?
- Does the cut introduce single-source dependency on a less-creditworthy manufacturer?

**Common failure modes:**

- Eliminating waterproofing layer "because membrane is sufficient" — owner now carries leak risk.
- Substituting tested rated assembly with field-built equivalent — owner carries fire-test failure risk.
- Substituting branded equipment (specified for warranty) with generic — owner loses manufacturer's installation backing.

**Example finding:**

> Item 53: Eliminate redundant below-grade waterproofing layer (keep only sheet membrane). ❌ BLOCK. Below-grade waterproofing is by definition not maintainable post-occupancy. Failure cost (basement remediation + business interruption) typically 50–100× original install cost. Risk transfer to owner is unacceptable. *Why: risk transfer (Axis 5).* Reference: `csi_division_heuristics.md §07 13 00`.

---

## Axis 6 — Reversibility

**Sub-criteria:**

- Can the original spec be reinstated later in CA (some finishes, fixtures, equipment)?
- Or once installed / omitted, is it gone (envelope, structure, blocking, in-slab MEP)?
- Cost ratio of retrofit vs. original install (typically 3–10× for finishes, 5–10× for envelope/blocking, 10–50× for in-slab).

**Common failure modes:**

- Accepting an "irreversible" cut to chase cost — finish swaps are reversible, envelope/blocking/in-slab are not.
- Eliminating in-wall blocking (grab bars, TV mounts, art) because "owner can add later" — drywall demo + patch + repaint = 5–10× original blocking cost.
- Eliminating spare conduits in new construction — no future-proofing once slab pours.

**Example finding:**

> Item 67: Eliminate in-wall blocking for future grab bars in 12 unit bathrooms. ❌ BLOCK. Original install cost approximately $400/unit ($4,800 total). Retrofit (drywall demo + new blocking + patch + texture + paint) $2,500–$3,500/unit ($30K–$42K total). Reversibility cost ratio 6–9×. *Why: reversibility (Axis 6).* Reference: ANSI A117.1-2017 §609.

---

## Classification rule (summary)

| Axes triggered | Classification |
|----------------|----------------|
| None — design-neutral, no perf hit, lifecycle ≥, no risk transfer, reversible | ✅ ACCEPT |
| Minor impact on one axis — modified approach feasible | ⚠️ ALTERNATE (propose modified spec) |
| Any: kills design intent (Axis 1) in identity space; code/perf failure (Axis 2); large lifecycle penalty (Axis 3) without owner LCCA sign-off; cascade schedule cost > savings (Axis 4); unacceptable risk transfer (Axis 5); irreversible loss > 5× retrofit cost (Axis 6) | ❌ BLOCK |
| Voids tracked certification target without owner sign-off (any axis) | ❌ BLOCK pending owner sign-off |
