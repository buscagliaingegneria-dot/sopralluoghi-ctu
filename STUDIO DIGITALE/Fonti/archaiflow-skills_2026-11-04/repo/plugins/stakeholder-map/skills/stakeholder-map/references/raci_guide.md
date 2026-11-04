# RACI for AEC — Application Guide

How to apply RACI (Responsible / Accountable / Consulted / Informed) to AEC project decisions across AIA-aligned project phases. Includes common pitfalls and worked examples.

---

## Definitions (strict)

- **R — Responsible** — does the work. Multiple R's on one decision is fine and common (e.g., AOR + structural + MEP all R on coordination).
- **A — Accountable** — single owner of the decision. Has authority to commit. **Exactly one A per decision.** If two people claim sign-off, that is the conflict to resolve.
- **C — Consulted** — two-way input *before* the decision is made. The C must give substantive input; if they only react after the fact, they are I, not C.
- **I — Informed** — one-way notification *after* the decision. No expectation of feedback that changes the decision.

If a stakeholder is none of the above for a given decision, the cell stays empty. Do not pad RACI matrices with C or I to make rows look full.

---

## AIA-aligned project phases

| Phase | AIA reference | Typical % design complete | Key decisions |
|---|---|---|---|
| Pre-design / Programming | A201 0% | 0 | Brief, program, site, delivery method |
| Schematic Design (SD) | B101 §3.2 | 15-30% | Concept, massing, code path, system selection |
| Design Development (DD) | B101 §3.3 | 50-65% | Detailed layouts, system sizing, material selection, cost validation |
| Construction Documents (CD) | B101 §3.4 | 95-100% | Drawings + specs sufficient for permit + bid |
| Bidding / Procurement | B101 §3.5 | 100% | Bid evaluation, contract award |
| Construction Administration (CA) | B101 §3.6 | — | RFI / submittal / change order management |
| Closeout | B101 §3.6.6 | — | Punch list, FCA, O&M, warranty |

---

## Worked RACI example: Curtain wall system selection

Decision: which curtain wall system goes on the project (unitized vs stick-built, vendor / line, performance class).

| Stakeholder | Pre-design | SD | DD | CD | Bid | CA |
|---|---|---|---|---|---|---|
| Owner (executive) | | | A | I | | |
| Owner's rep | | C | C | I | | I |
| AOR (design lead) | | R | R | A | C | C |
| Façade consultant | | C | R | R | C | C |
| Structural | | C | C | C | | |
| MEP | | I | C | C | | |
| Cost consultant | | C | C | I | | |
| GC / CMAR (if engaged) | | I | C | C | A | R |
| Curtain wall sub | | | I | I | R | R |
| Building department | | | | I | | |

Notes:
- Owner is **A** in DD because that is when the system is committed (cost, schedule, aesthetic implications).
- AOR is **A** in CD because that is when the documentation is the AOR's responsibility.
- GC is **A** at Bid because the procurement decision is theirs.
- Building department is **I**, never C — they are reactive at submission, not pre-decision.

---

## Common pitfalls

### 1. Multiple A's

Two parties both signing off on one decision creates ambiguity. If both must sign, name the structure: "A — owner board (vote of 5 trustees)" rather than listing each trustee as A.

### 2. Confusing R and A

R does the work; A owns the decision. The AOR is R on most design work, but A only when the decision is internal (e.g., specification of door hardware). The owner is A on system selections that drive cost/schedule/program.

### 3. Promiscuous C

Marking everyone as C feels safe but means consultation is meaningless. Limit C to stakeholders whose input genuinely could change the decision. The rest are I (or blank).

### 4. Omitting AHJ

In jurisdictions where pre-application consultation is standard (NYC DOB pre-app, CA HCAI back-check), the AHJ is C in DD or earlier. Treating AHJ only as a code-compliance check at permit submission misses meaningful early input.

### 5. Confusing AOR contractual responsibility with internal role

AIA B101 makes the AOR responsible for design documents. But within the design team, a sub-consultant may be R (and possibly A) for their discipline's content. The AOR's accountability rolls up at the document set level, not at every sub-decision.

### 6. Forgetting CxA

If commissioning is in scope (LEED EAp1, ASHRAE Guideline 0), the CxA is C on system selection in DD and R on commissioning execution in CA. CxA cells are commonly forgotten.

### 7. Forgetting facilities / operations

The future facility manager has standing on FF&E selection, controls strategy, and serviceability — they should be C in DD on these. Excluding them produces buildings the operator cannot maintain.

---

## Decision-type RACI defaults

These are starting points; project specifics override.

### Brief / program changes

A: Owner. R: AOR + owner's rep. C: end users, finance. I: design team.

### Site selection

A: Owner. R: AOR + civil + cost. C: legal, geotech, owner's rep. I: end users.

### Major system selection (structural type, façade, primary HVAC)

A: Owner (in SD/DD). R: AOR + relevant engineer + cost. C: GC (if engaged), CxA, FM. I: end users.

### Specification of finishes / FF&E

A: AOR or interior designer. R: design team. C: FM, custodial, end users (sometimes). I: owner.

### Code path / alternate means

A: AOR. R: code consultant. C: AHJ. I: owner, GC.

### Change orders during CA

A: Owner. R: GC + AOR. C: cost consultant, owner's rep, CxA (if MEP scope). I: CxA, FM.

### Substantial completion

A: AOR (per AIA B101). R: AOR + GC + CxA. C: owner. I: AHJ.

### Acceptance / move-in

A: Owner. R: GC + FM + IT. C: AOR, CxA. I: end users (notification of move date).

---

## Format for output

In the stakeholder map deliverable, present RACI as a table with phases as columns and stakeholders as rows. Cells may contain R / A / C / I or remain blank. For complex projects, build separate matrices for separate decision categories (program, design, procurement, change management) rather than one giant matrix that becomes unreadable.
