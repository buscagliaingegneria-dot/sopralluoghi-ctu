# Long-Lead Items — Sourcing Methodology (NA)

This is **not** a lookup table. It is a methodology for building a project-specific long-lead register against current, vendor-quoted lead times.

---

## Why bundled lead-time numbers are dangerous

Lead times for construction-procured equipment in North America move quarterly — sometimes monthly. Any bundled "lead time = N weeks" table inside a Skill is wrong by the time it ships, and is often wrong by a margin that breaks schedules.

Specific reasons not to trust a baked-in number:

- **Rapid drift.** Switchgear lead times moved from ~12 weeks (2019) to 50-70 weeks (2022-2023) to a partial recovery (2024-2026) that varies by manufacturer and voltage class. Any single number captures one snapshot of one vendor.
- **Manufacturer-specific.** Eaton, Schneider Electric (Square D), ABB, Siemens, GE all publish independent customer letters; lead times often differ by 8-20 weeks at the same moment for the same product class.
- **Regional.** Coastal vs inland fabricators, Canadian vs US sourcing, port-of-entry status, and freight availability all shift delivered lead times for the same factory lead time.
- **Project-spec-dependent.** Custom voltage / breaker layout / NEMA enclosure / arc-flash labeling / harmonic-mitigation transformer pairs all push lead times beyond catalog. A 30-week catalog AHU becomes a 50-week unit when stainless-steel cabinet, MERV-16, custom coil count, and seismic restraint package are added.
- **Allocations and order books.** Some manufacturers throttle order intake when their book is full; lead time at quote can differ from lead time at PO release by 4-12 weeks.

**Anti-pattern statement:** Do not paste lead-time figures from training-data recall, prior projects, or stale references into a constructability finding. The 2026-05-09 well-tracker incident in this catalog was caused by exactly that pattern — bundled numbers from recall presented as current truth, then found to be wrong row-by-row when diffed against the publisher source. A lead-time number that affects a procurement decision must come from a current, dated, named-source quote.

---

## Sources to consult, by category

For each category below, the goal is the same: get a written, dated quote (manufacturer customer letter, rep email, or fabricator proposal) tied to **the project's actual specification**, not a generic catalog number.

### Electrical equipment

- **Low-voltage switchgear (≤600 V), MV switchgear (≥5 kV), MCCs, panelboards.** Sources: Eaton, Schneider Electric (Square D), ABB, Siemens, General Electric / GE Industrial Solutions. Method: ask the project electrical engineer or electrical sub to pull the manufacturer's most recent **customer lead-time letter** (issued quarterly or after major price/lead changes) for the specific product family the project specs. Cross-check with two manufacturers when possible — sole-source has historically been the source of the worst lead-time surprises.
- **Generators.** Sources: Cummins, Caterpillar (CAT), Kohler, MTU / Rolls-Royce Power. Diesel vs natural-gas vs bi-fuel availability differs; ask the rep specifically about fuel-type lead time, not a generic "genset" number.
- **Transformers (oil-filled and dry-type, ≥500 kVA).** Sources: Eaton, ABB, Siemens, Square D, ERMCO, Howard Industries. DOE 2016 efficiency rules and the 2024 DOE proposed amendment have moved lead times — confirm the unit complies with current DOE efficiency at quote time.
- **ATS, motor starters, VFDs.** Sources: ASCO (Vertiv), Eaton, Cutler-Hammer, Schneider, ABB.
- **Lighting controls (network), LED fixtures (custom).** Sources: Lutron, Crestron, Acuity Brands, Cooper Lighting, Philips Color Kinetics for custom architectural.

### Mechanical equipment

- **Air handling units (custom and catalog).** Sources: Trane, Daikin Applied, Carrier, York (Johnson Controls), Greenheck (smaller / DOAS), AAON. Method: most have **procurement portals** or rep-issued lead-time advisories; the engineer of record's mechanical sub should hold a current dated number tied to the project's tag list (cabinet size, coil count, finish, controls).
- **Chillers (water-cooled centrifugal, air-cooled scroll, magnetic-bearing).** Sources: Trane, York, Carrier, Daikin Applied, Multistack, Smardt. Refrigerant transition (R-410A phase-down, low-GWP refrigerants under AIM Act) is moving lead times — confirm refrigerant choice and SNAP compliance at quote time.
- **Boilers, cooling towers, pumps, heat exchangers.** Sources: Cleaver-Brooks, Burnham, Aerco for boilers; BAC, Marley (SPX), EVAPCO for cooling towers; Bell & Gossett, Armstrong, Taco for pumps; Bell & Gossett, Alfa Laval for heat exchangers.
- **VRF / VRV systems.** Sources: Daikin, Mitsubishi Electric / Trane, LG, Samsung HVAC.

### Structural

- **Structural steel (mill order + fabrication).** Sources: **AISC market quarterly** (publishes mill capacity, fabricator backlog snapshot). For project-specific number, get a **fabricator quote** — Schuff, SteelFab, Banker Steel, Walters Group, Canron, Adamson Industries, Owen Industries. The fabricator quote is the only number that matters; AISC quarterly is for sanity-check.
- **Mass timber (CLT / GLT / glulam, prefab panels).** Sources: StructureCraft, Nordic Structures, Element5, KLH (US-distributed), Mercer Mass Timber, Boise Cascade Timber Solutions, Vaagen Timbers. Mass timber is shop-drawing-heavy; quote-to-delivery includes engineering, shop drawings, fabrication, and panelization sequence — a single "lead time" hides 3-4 distinct durations.
- **Pre-cast concrete (custom).** Sources: regional pre-casters dominate — Coreslab Structures, Tindall, Gate Precast, Wells, High Concrete Group; ask the project structural engineer for the regional list.

### Envelope

- **Custom curtain wall (high-performance, oversized, unitized).** Sources: Permasteelisa, Walters & Wolf, Yost (Yost Architectural Curtain Walls), Crown Corr, Enclos, EFCO (Pella), Kawneer (Arconic). Custom curtain wall lead time is the **shop-drawing review + fabrication + sample approval + glass procurement** chain combined; ask for each segment, not a single number.
- **Catalog curtain wall, storefront.** Sources: Kawneer, EFCO, YKK AP, Tubelite, Vistawall, Wausau Window. Catalog systems still have configuration variables (finish, anchor type, glazing) that affect lead time.
- **Insulated glass (oversized, jumbo, high-performance coatings).** Sources: Viracon, Vitro (PPG), Guardian Glass, Cardinal CG, Saint-Gobain Glass.
- **Skylights, custom operable windows, decorative metal panels.** Sources: project-specific; ask the architect's specifier.

### Vertical transportation

- **Elevators (new construction, modernization).** Sources: Otis, KONE, Schindler, ThyssenKrupp / TK Elevator, Mitsubishi Electric. Elevator lead time is heavily dependent on whether the unit complies with current ASME A17.1 / CSA B44 amendment — code-revision-driven re-certifications have repeatedly extended manufacturer queues. Modernization is a separate quote logic from new install.

### Owner-furnished medical & lab equipment

These are typically owner-furnished and delivered through the owner's procurement, but the constructability review must still capture the install window because the receiving environment (shielding, vibration isolation, slab loading, MEP rough-in tolerances) is on the GC's critical path.

- **Linear accelerators (linacs).** Sources: **Varian (Siemens Healthineers)**, Elekta, Accuray. Lead time is manufacturer-quoted per unit and tied to the project's specific bunker design (shielding wall calcs, maze geometry, primary/secondary barrier).
- **MRI, CT, PET-CT.** Sources: **Siemens Healthineers**, GE HealthCare, Philips Healthcare, Canon Medical. Magnet ramp scheduling is part of the lead-time conversation, not separate.
- **Lab fume hoods, biosafety cabinets, autoclaves.** Sources: Labconco, Thermo Fisher, NuAire, Baker, Esco Lifesciences. Custom casework lead time should be quoted by the lab-furniture sub directly.
- **Imaging suite cabling, RF shielding, magnetic shielding.** Sources: ETS-Lindgren, IMEDCO, RF Window. Often a separate sub-trade quote.

### Specialty / interior

- **Architectural casework (custom millwork, AWI Premium grade).** Sources: regional millwork shops — get the project-specific millwork sub to quote.
- **Stone (natural).** Sources: regional fabricators with quarry relationships; Italian and Brazilian sources are slower than domestic.
- **Specialty doors (acoustic STC-rated, blast-resistant, lead-lined for radiology).** Sources: Krieger, Overly, Industrial Acoustics (acoustic); Ambico, Krieger (blast); Ray-Bar, Mar-Lead (lead-lined).

---

## Project lead-time register — blank template

Build one of these per project. Keep it in `docs/constructability-reviews/<project-slug>/lead-times.md` and re-quote any row whose source date is older than ~90 days.

```markdown
# Long-Lead Register — {{PROJECT}}

Last refreshed: {{YYYY-MM-DD}}

| Item (project tag) | Manufacturer | Quote source | Quote date | Lead time (weeks) | Confidence | Notes |
|---|---|---|---|---|---|---|
| Switchgear SWGR-1 | Eaton | Eaton customer lead-time letter | 2026-04-12 | 48 | High (named letter) | Includes 6-wk site-specific config |
| AHU-3 (custom, MERV-16, stainless coil) | Trane | Trane rep email to MEP sub | 2026-04-22 | 42 | High | Cabinet finish drives 4-wk premium |
| Curtain wall (unitized, 2 ft × 12 ft modules) | Walters | Walters fab proposal | 2026-03-30 | 38 (incl. shop drawings + fab) | Medium (single bid) | Re-quote at 50% CD |
| Mass timber CLT panels | StructureCraft | Verbal from rep | 2026-05-01 | 34 (engineering→delivery) | Low (verbal) | Get written quote before basing CPM |
| Linac bunker — Varian TrueBeam | Varian (Siemens Healthineers) | Owner-furnished delivery commitment | 2026-04-15 | 30 | High | Bunker rough-in must be ready 4 weeks ahead |

## Refresh log
- 2026-05-09: initial register, 5 items quoted.
```

**Confidence column legend:** High = written, dated, manufacturer or named-fabricator source. Medium = single bid or rep-issued advisory without project-specific tag list. Low = verbal, undated, or based on industry chatter / catalog reference.

**Required columns** (do not omit any):

1. **Item (project tag)** — match the schedule / spec tag, not a generic name.
2. **Manufacturer** — named manufacturer, not "TBD".
3. **Quote source** — what document did the number come from? "Eaton customer letter Q2 2026", "Trane rep email", "Walters fab proposal", not "the rep said".
4. **Quote date** — when was the source issued?
5. **Lead time (weeks)** — single number or a tight range (e.g., 42 or 40-44). If you have a range wider than ~6 weeks the number is too soft to base a schedule decision on; re-quote.
6. **Confidence** — High / Medium / Low (legend above).
7. **Notes** — what's special about the project's spec that affects lead time (custom finish, code amendment compliance, refrigerant choice, etc.).

Items with **Low** confidence cannot be used as the basis for a "switchgear is on critical path" finding. Re-quote first.

---

## How to use this in a constructability finding

Find the procurement-driven date the project schedule needs (e.g., "switchgear must be on-site at month 14, energization at month 16") and back-calculate from the **project-specific quote**, not from a recalled industry number.

Sample finding language:

> [High] Per the project lead-time register, Eaton low-voltage switchgear at 48 weeks (Eaton customer letter, 2026-04-12). Schedule places switchgear energization at month 16 from NTP. Order release must be at month 16 minus 48 weeks ≈ month 4 from NTP. Currently the spec basis-of-design is unfinalized at 75% CD with a planned submittal review at month 9. Recommend (a) finalizing switchgear basis-of-design now, (b) issuing a long-lead procurement package against 75% CD with explicit re-design risk allocation, and (c) re-confirming the Eaton lead time at order release — the 2026-04-12 letter will be ~120 days old by month 4.

Notice what the finding **does not do**:

- Does not cite "Switchgear: 40-60 weeks (2026 Q2)" from a bundled table.
- Does not estimate from prior project memory.
- Does not paraphrase a number from training-data recall.

Every number is sourced, dated, and tied to a named manufacturer.

---

## Update cadence

Refresh project registers quarterly at minimum, monthly during active long-lead procurement windows. Sources to monitor for general market signal (not for project-specific numbers):

- **AGC of America** Construction Inflation Alert and quarterly market reports.
- **AISC** market quarterly (steel mill capacity and fabricator backlog).
- **ENR** Construction Cost Index commentary and lead-time articles.
- **Major-manufacturer customer letters** (Eaton, Schneider Electric, Siemens, ABB, Trane, Daikin Applied, Carrier, Otis, KONE, ThyssenKrupp).
- **Procurement portals** where manufacturers publish dated lead-time advisories.

These sources tell you the **market is tight or loose**. They do **not** give you a number suitable for a project schedule. For that, get a project-specific quote.

Last verified (methodology): 2026-05-09.
