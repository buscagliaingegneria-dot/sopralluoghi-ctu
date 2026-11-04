# Delivery Method × Insurance Allocation Matrix

How insurance allocation differs across project delivery methods. Drives Builder's Risk carrier, wrap-up feasibility, professional liability stack, and flow-down structure.

---

## Design-Bid-Build (DBB)

| Coverage | Carried by |
|----------|------------|
| Owner CGL (Owner's Protective) | Owner |
| Architect / Engineer Professional Liability | Architect / EOR (per B101 §2.5 / E101 / equivalent) |
| Builder's Risk | **Owner** (most common) — owner controls until SC. Less common: GC carries, owner reimburses via change order. |
| Contractor CGL + Auto + WC + Umbrella | GC + each sub (flow-down via subcontract) |
| Contractor's Pollution Liability | GC if project has demo / hazmat / fuel handling |

**Notes:**

- Owner-carried Builder's Risk is the cleaner allocation — owner has most insurable interest in the structure under construction.
- DBB is the simplest insurance structure — each tier carries its own liability.
- Subcontractor flow-down via subcontract is critical; GC is the gatekeeper.

---

## Design-Build (DB)

| Coverage | Carried by |
|----------|------------|
| Design-Builder Professional Liability | **Design-Builder** — combined design + construction PL on a single policy or joint policy with separate design-builder PL behind it. |
| Owner CGL | Owner |
| Builder's Risk | Typically **Design-Builder** carries — single point of accountability matches single point of construction. Some owners still carry. |
| CGL + Auto + WC + Umbrella | Design-builder + each sub |

**Notes:**

- Design-Builder PL is more expensive than separate architect PL — combines design risk and construction risk in one carrier.
- Owner-carried Builder's Risk is feasible but contradicts the "single point of responsibility" DB premise.
- Design-build joint ventures (DB JV) require careful PL stacking — confirm whether the JV entity itself carries PL, or each JV member's PL responds.

---

## Construction Manager at Risk (CMAR)

| Coverage | Carried by |
|----------|------------|
| Architect Professional Liability | Architect (separate from CMAR). |
| CMAR Professional Liability | **CMAR** — preconstruction services + construction phase PL. Required by most owners. |
| Builder's Risk | **Negotiated.** Often owner. Sometimes CMAR. |
| CGL + Auto + WC + Umbrella | CMAR + subs |

**Notes:**

- CMAR carries PL because preconstruction services (estimating, constructability, scheduling) create design-influence exposure.
- CMAR + Architect both carry PL — owner decides whether to require co-defense provisions or independent counsel.
- Owner-controlled wrap-up (OCIP) common on CMAR > $25M.

---

## Integrated Project Delivery (IPD)

| Coverage | Carried by |
|----------|------------|
| All-party Professional Liability | **Single project policy** (Project Insurance Program / PIP) covers all signatory parties, including waiver of subrogation among signatories. |
| Builder's Risk | Project policy. |
| CGL + Auto + WC + Umbrella | Each signatory's primary; project umbrella may cover gap. |

**Notes:**

- IPD insurance is project-bound — the multi-party agreement (often AIA C191 or ConsensusDOCS 300) requires a project-specific PIP.
- IPD shared-risk-shared-reward dynamic requires waiver of subrogation among IPD signatories — eliminates intra-team litigation.
- IPD market is small; only a handful of carriers underwrite IPD PIP.

---

## Public-Private Partnership (P3)

| Coverage | Carried by |
|----------|------------|
| All construction-phase coverages | Per concessionaire's project agreement; typically combined with operations-phase coverage. |
| Operating-phase coverage (post-completion) | Concessionaire / SPV. |

**Notes:**

- P3 insurance is concession-agreement-driven; varies by deal.
- Long-term operations exposure (30–50 yr concessions) drives broader coverage including business interruption, environmental, cyber.

---

## Decision summary

When picking insurance program structure based on delivery method:

| Delivery | Default Builder's Risk | OCIP / CCIP feasible? | PL stack |
|----------|------------------------|------------------------|----------|
| DBB | Owner | Yes if > $25M | Architect + EOR |
| DB | Design-Builder | Yes — typically CCIP | Combined Design-Builder PL |
| CMAR | Negotiated (often Owner) | Yes — typically OCIP | Architect + CMAR |
| IPD | Project | Project Insurance Program (PIP) | Project PL |
| P3 | Concessionaire | Per concession agreement | Per concession agreement |

For wrap-up feasibility, see `ocip_ccip_decision.md`.
