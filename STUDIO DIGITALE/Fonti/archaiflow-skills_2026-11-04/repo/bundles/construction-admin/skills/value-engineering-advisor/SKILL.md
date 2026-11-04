---
name: value-engineering-advisor
description: "Sorts a cost-cutting list against an issued design into accept, accept with an alternate, and block, with the reasoning written out per item across design intent, performance, lifecycle cost, schedule, risk transfer, and reversibility. Trigger on \"VE review\", \"value engineering\", \"review this VE list\", \"where can we cut\", \"cost reduction options\", \"VE round 2\", or a pasted contractor proposal with substitutions and savings figures. Works with any contract and any specification format. Performance requirements come from the user's own specification and contract; the skill supplies the sorting method and never a code threshold or a performance value from memory. Produces a recommendation memo, not a directive."
license: MIT
metadata:
  title: "Value Engineering"
  summary: "Sort a cost-cutting list into accept, alternate, and block"
  discipline: "construction-admin"
  tags: "Construction Admin, Project Management, AIA A201, AIA B101, Construction"
---

## Overview


Review a value-engineering (VE) list submitted by a CM, GC, or owner — typically post-bid, late-DD, or any moment when the project budget has slipped — and produce a categorized recommendation memo per item. Output lives in `docs/value-engineering/`. Each item is classified ✅ ACCEPT / ⚠️ ALTERNATE / ❌ BLOCK with a one-line "why" naming the design-intent, performance, lifecycle, code, schedule, or risk-transfer concern.


This skill is for the architect / AOR / owner's-rep perspective. The memo is a recommendation that the AOR, owner, and CM/GC discuss at the next VE workshop or OAC meeting; it is not a binding directive and does not replace the AOR's stamp on subsequent CDs / ASIs / change orders.


Aligned with ASTM E1699 (VE Job Plan), CSI MasterFormat 2020 (cuts organized by division), AIA A201-2017 §7 (Changes in the Work) + G701 (Change Order), AIA B101-2017 §3.6.1.5 (architect's cost review), CMAA preconstruction services scope.


## Scope and limits — read first


**What this does.** Takes a cut list and sorts it item by item into accept,
accept with an alternate, and block, working each item through six axes and
writing one line of reasoning per item into a memo in
`docs/value-engineering/`. The memo also carries the downstream work an accepted
cut creates: spec edits, sheet revisions, re-review, certification impact.

**What this does not do.**

- **It does not supply a performance requirement or a code threshold.**
  R-values, fire ratings, STC, and accessibility dimensions come from your own
  specification and the code in force. `references/csi_division_heuristics.md`
  carries the shape of each trade-off rather than its number, and project
  context overrides it.
- **It does not produce savings figures.** Only what the CM or GC quoted is
  used. A missing figure is marked as one to request, never estimated.
- It does not direct anything. The memo is a recommendation for the VE workshop
  or the OAC meeting, and it does not stand in for the stamp on the ASI, CCD, or
  change order that follows.
- It does not re-check the design once cuts are accepted. Anything touching
  egress, fire resistance, accessibility, or the envelope goes to `code-compliance-review`,
  and anything touching sequencing to `constructability-review`.
- It does not decide a certification target can be dropped. It names the loss;
  the owner signs off on it.

**What you need before starting.** The VE list with the CM or GC's own savings
figures, the issued design the cuts are against, the phase, and the performance
targets the project committed to, in the specification's own words.

## When to use


Trigger on:

- Pasted VE lists (CSI division, item, current spec, proposed substitution, $ savings).
- Project file paths to a VE workshop package.
- Explicit asks: "VE review", "value engineering", "where can we cut", "review VE round 2", "what should we accept from the CM's VE list".
- Hand-off from `bid-review` when the low bid exceeds budget or qualifications include "VE assumed".

Do NOT trigger for:

- Cost estimating from scratch (this skill assesses proposed cuts; it does not generate $ values — use the CM/GC quote).
- Constructability review (use `constructability-review`).
- Bid leveling (use `bid-review`).
- Spec-section completeness review (use `spec-review`).
- Final code / egress / energy check after VE accepted (use `code-compliance-review`).

## Workflow


### Step 1 — Bootstrap if needed


Check that `docs/value-engineering/index.md` exists. If not:


```bash
python scripts/init_ve_workspace.py
```


### Step 2 — Anchor the project context


Read `docs/project.md` if it exists. Pull:

- **Phase** (SD / DD / CD / post-bid / CA — the later the phase, the more expensive the redesign triggered by an accepted cut).
- **Delivery method** (DBB / CMAR / DB / IPD — affects who carries VE risk and who proposes alternates).
- **Budget gap** ($ over budget; the size of the gap drives how aggressive cuts must be).
- **Owner type** (institutional / commercial / public / healthcare / K-12 — affects risk tolerance and approval process; e.g., CA HCAI rejects many envelope cuts, NYC SCA rejects many finish cuts).
- **Project type** (the heuristics in `references/csi_division_heuristics.md` distinguish public/identity vs. back-of-house — a lobby cut hits differently than a mech-room cut).
- **Code / certification anchors** (LEED Gold pursued? Passive House? LL97 carbon cap? IECC stretch? Each constrains what can be cut without losing the target).
- **Named AHJ** (NYC DOB, FDNY, CA HCAI, DSA, GSA, USACE, FEMA region, state DEP/DEC — the AHJ controls what alternates require re-review).

### Step 3 — Apply per-item assessment


For each VE item, work through the six-axis decision tree in `references/ve_assessment_axes.md`:

1. Design intent impact (concept identity, public vs. back-of-house).
2. Performance / code impact (envelope R-value, fire rating, STC, ADA, IECC, NFPA).
3. Lifecycle cost (upfront savings vs. O&M penalty over 20–30 yr).
4. Schedule impact (does the cut actually save schedule, or trigger redesign + re-permit + AHJ re-review?).
5. Risk transfer (does the cut shift risk back to owner — e.g., reducing waterproofing transfers leak risk).
6. Reversibility (can this be reinstated later in CA, or once gone is it gone?).

For division-specific cuts, consult `references/csi_division_heuristics.md` keyed to the CSI MasterFormat division. Heuristics name the typical impact — but the project-context anchors from Step 2 override generic heuristics.


Classify per the rule:

- **✅ ACCEPT** if design-neutral + no performance hit + lifecycle neutral-or-positive + no risk transfer.
- **⚠️ ALTERNATE** if minor impact on one axis — propose a modified approach (e.g., "specify equivalent product line by alt manufacturer" or "reduce spec rather than eliminate").
- **❌ BLOCK** if any of: kills design intent in a public/identity space, code or performance failure, unacceptable risk transfer, irreversible loss, or voids a tracked certification target without owner sign-off.

Each item gets a one-line "why" that names the axis it failed/passed and cites the reference (e.g., `csi_division_heuristics.md §07 27 26` or `IBC §720` for fire rating).


### Step 4 — Aggregate into the recommendation memo


Use the template at `assets/ve_memo_template.md`. The memo includes:

- **Header** — project, phase, VE round, date, gap $ vs. accepted savings $.
- **Categorized table** — three sections (Accept / Alternate / Block) with per-item one-liners and citation column.
- **Downstream impacts** — follow-on actions: spec revisions (Section #), drawing revisions (sheet #), schedule impact (days), code re-review needed (egress / energy / accessibility / fire), CA-phase tracking (LEED point loss, warranty length change, certification target risk).
- **Open questions** — items that need owner / AHJ input before classifying (e.g., "is LEED Gold still hard target if MR credit drops 2 pts?").

Write the memo to `docs/value-engineering/<round-number>-<YYYY-MM-DD>.md` and append a row to `docs/value-engineering/index.md`.


### Step 5 — Hand off


The memo is a recommendation, not a directive. Hand off to:

- **AOR** for stamp on accepted items. Any ⚠️ accepted as alternate must roll into ASI per AIA G710 or CCD per AIA G714.
- `spec-review` to verify spec-section consistency on accepted alternates (especially Part 2 product/manufacturer changes).
- `code-compliance-review` if any accepted cut touches egress, fire-resistance, accessibility, or envelope thermal.
- `constructability-review` if any accepted alternate changes sequencing, trade interface, or installation tolerance.
- `submittal-review` later in CA when the substituted product's submittal arrives.

## Anti-patterns

- **Never invent $ savings.** Use only what the CM/GC quoted. If a number is missing, mark "TBD — request from CM" — do not estimate.
- **Never accept a cut that drops below code minimum.** Even if "the AHJ has approved similar," the AOR carries the stamp; default to ❌ and require AHJ alt-means letter on file before re-classifying.
- **Never recommend a cut that voids a tracked certification target** (LEED, WELL, PHIUS, Title 24 above-code, LL97 cap) without explicit owner sign-off on the loss. The memo names the certification impact in the "downstream" column.
- **Never present this skill's six-axis framework as a published industry standard.** ASTM E1699 publishes the VE Job Plan (Information → Function → Creative → Evaluation → Development → Presentation); the six-axis classification used here is a structured review heuristic synthesized to surface obligations from ASTM E1699, AIA contracts, and CSI MasterFormat.
- **Never skip the "Reversibility" axis on irreversible scope** (envelope assemblies, structural waterproofing, in-slab radiant, embedded blocking). Once gone, retrofit cost typically exceeds 5–10× the original install cost.

## Resources

- `scripts/init_ve_workspace.py` — bootstrap `docs/value-engineering/` and `index.md`.
- `references/ve_assessment_axes.md` — six-axis decision framework with sub-criteria, common failure modes, example findings.
- `references/csi_division_heuristics.md` — CSI MasterFormat 2020 division-keyed cuts with design / performance / lifecycle / risk impact heuristics.
- `references/astm_e1699_methodology.md` — VE Job Plan outline (six phases) for context on industry-standard methodology.
- `assets/ve_memo_template.md` — recommendation memo template for `docs/value-engineering/`.
