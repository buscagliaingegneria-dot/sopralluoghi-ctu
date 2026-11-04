---
name: constructability-review
description: "This skill should be used when the user shares construction documents (DD set, 50%/100% CD, GMP set) and wants them reviewed through a constructor's lens — sequencing, tolerance stack-ups, MEP coordination, install access, lay-down logistics, temporary works, long-lead procurement, and phased operations. Trigger on 'constructability review', 'CM review', 'sequencing check', 'install access', 'crane reach', 'lay-down', 'long-lead', 'MEP coordination clearance', 'site logistics', or pasted CD context with build-feasibility intent. Generates a structured review markdown in `docs/constructability/` and appends to the project constructability index."
license: MIT
metadata:
  title: "Constructability Review"
  summary: "Read a document set through a builder's eyes"
  discipline: "construction-admin"
  tags: "Design"
---

# Constructability Review


## Overview


Review a construction documents package against eight constructability axes — trade sequencing, tolerance stack, MEP coordination, install access & rigging, lay-down & site logistics, temporary works, materials procurement & lead times, and phased operations — and produce a written review that lives in `docs/constructability/`.


This is the CM-side / owner's-rep / preconstruction perspective. It catches the "looks fine on paper but cannot be built without rework" failures during DD or 50% CD, when redesign is still cheap. Aligned with NA practice: AGC of America constructability review checklists, CMAA preconstruction services scope, AIA Document G701 (Change Order) economics on what should-have-been-caught issues cost when caught later, and ASHRAE / ANSI / SMACNA installation tolerance standards.


## Scope and limits — read first


**What this does.** Reads a document set the way a builder reads it, across
eight axes, and writes findings to `docs/constructability/` with a severity tag
on each. A finding names the sheet or detail, the dimension, clearance, or lead
time in question, and what the fix costs now against what it costs in CA.

**What this does not do.**

- **It does not carry lead times.** `references/long_lead_items_2026.md` is a
  method for building a project-specific register out of dated vendor quotes,
  not a table to read a number from. Lead times move quarterly and differ by
  manufacturer, so the number in a finding is one you obtained and dated.
- **It does not carry assembly tolerances either.** A tolerance finding cites
  AISC, ACI, SMACNA, or the manufacturer's installation guide, from your copy of
  it.
- It does not estimate cost. It shows where buildability drives cost; the CM or
  the cost consultant prices it.
- It does not check code compliance, set completeness, or design quality. Those
  are `code-compliance-review`, `drawing-checklist`, and `design-critic`.
- It does not conclude that something cannot be built. Constructors find a way,
  and the review's job is to surface what that way costs.

**What you need before starting.** The set or the details in question, the
delivery method and CD phase, the structural and envelope systems, and the site
constraints. Current quoted lead times if procurement is one of the axes you
want weighted.

## When to use


Trigger on:

- Pasted CD set details, plan/section excerpts, RCP/MEP overlays, or schedule-and-logistics narratives with a constructability question.
- Project file paths to a CD set the user wants reviewed.
- Explicit asks: "constructability review", "can this be built", "sequencing check", "install access for the AHU", "MEP coordination clearance", "lay-down on this site".
- Hand-off from `bid-review` when low bidder flagged a constructability concern in their qualifications.

Do NOT trigger for:

- Pure code/egress compliance (use `code-compliance-review`).
- Drawing-set completeness audit (use `drawing-checklist`).
- Submittal review during CA (use `submittal-review`).
- General design critique (use `design-critic`).
- Cost estimating (this skill flags constructability-driven cost risk; it does not produce independent estimates).

## Workflow


### Step 1 — Bootstrap if needed


Check that `docs/constructability/index.md` exists. If not:


```bash
python scripts/init_constructability_workspace.py
```


### Step 2 — Anchor the project context


Constructability findings are project-specific. Pin context before applying axes.

- Read `docs/project.md` if it exists for delivery method (DBB, CMAR, DB, IPD), construction type (Type I-V per IBC), structural system (steel, CIP concrete, mass timber, hybrid), envelope system (curtain wall, panelized, brick veneer), site constraints (urban-infill, owner-occupied, weather-restricted), and CD phase (DD, 50% CD, 100% CD, GMP set).
- Identify the dominant constructability risk category for the project: occupied-building renovation, urban high-rise lay-down constraint, mass-timber procurement, expedited fast-track, etc. The dominant risk drives axis weighting.
- Pull lead-time benchmarks from `references/long_lead_items_2026.md` for current procurement realities (electrical switchgear, AHUs, custom glazing, elevators, structural steel deck).

### Step 3 — Apply eight-axis review


Load `references/constructability_axes.md` for the full framework with sub-criteria. Quick reference:

1. **Trade sequencing & critical path** — Is the implied sequence physically possible? Out-of-sequence work, predecessors blocked by later trades, unrealistic concurrent work in the same volume?
2. **Tolerance stack-up** — Cumulative tolerance from structure to finish exceeds the detail's accommodation? Steel ±¼" + deck ±½" + topping ±⅛" + acoustic substrate ±⅛" can defeat a 1/8" reveal at the wall-to-floor joint.
3. **MEP coordination & rack space** — Above-ceiling clear height accommodates duct + sprinkler + cable tray + lighting in real (not BIM-clashed-but-resolved) coordination? Riser stack alignment story-to-story? Shaft enclosure penetrations within rated-assembly limits?
4. **Install access & rigging** — Crane / boom-truck reach for steel and pre-cast erection? Hoisting paths through future façade openings? Equipment-room dimensions for AHU / chiller / switchgear installation and future replacement (the "removal route" question)?
5. **Lay-down & site logistics** — Material storage area on a constrained urban site? Truck deliveries through restricted streets? Crane swing radius respects neighbor airspace? Pedestrian protection per IBC §3306, OSHA 1926 Subpart M, and local DOB / DSA requirements?
6. **Temporary works** — Shoring for excavation? Dewatering capacity vs. groundwater rate? Weather enclosure for winter concrete or interior finishes? Life-safety path during construction (egress paths, sprinkler activation, fire watch)?
7. **Materials procurement & lead times** — Long-lead items (electrical switchgear 40-60 weeks 2026, AHU 30-50 weeks, custom curtain wall 24-40 weeks) ordered with lead-time buffer? Decisions for those items frozen at the schedule date that procurement requires?
8. **Phased operations & owner occupancy** — If the building is occupied during construction (renovation, expansion, school during summer break), are temporary-condition floor plans coordinated with infection-control risk assessments (ICRA in healthcare), means of egress, mechanical of patient/student transitions (MOP), neighbor noise/vibration limits, and security boundaries?

Focus on the 3-5 axes with real signal for the project. An urban high-rise reads heavily on 4, 5, 6. A healthcare renovation reads heavily on 1, 7, 8. A suburban greenfield reads heavily on 2, 3, 7.


### Step 4 — Write the review


Read `assets/constructability-template.md`, fill placeholders. Filename:


`docs/constructability/<YYYY-MM-DD>-<slug>.md`


Slug rule: lowercase, `[^a-z0-9-]` removed, max 40 chars, derived from project + CD phase or dominant risk (`acme-hq-50pct`, `harbor-school-occupied-phasing`). If a review with the same date+slug already exists, suffix `-<n>`.


### Step 5 — Update the constructability index


```bash
python scripts/append_to_index.py \
  --date 2026-05-09 \
  --slug acme-hq-50pct \
  --cd-phase "50%" \
  --primary-axes "sequencing,mep-coordination,install-access" \
  --severity-high 3
```


The script appends a row to `docs/constructability/index.md`. Do NOT edit the index manually with the Edit tool.


### Step 6 — Report


Tell the user:

- Path to the review file.
- The 2-3 highest-severity findings (each with a recommended design move and an estimated change-order avoidance value when caught now vs at CA).
- Any long-lead items where the procurement decision is already late.
- Whether a follow-up `submittal-review` checklist should pre-load for the long-lead items called out.

## Rules

- Every finding cites a specific drawing detail or sheet, plus the assembly tolerance / clearance / lead-time number being violated. "MEP coordination is tight" is not a finding; "AHU-3 corridor clear height of 8'-2" leaves 6" above 24" round duct + 8" lighting, no sprinkler reserve" is a finding.
- Severity tag each finding: **High** (will cause a change order or schedule slip if not addressed before CD), **Medium** (likely to surface as RFI in CA), **Low** (worth noting; resolvable without redesign).
- Lead-time claims cite a date source (RSMeans 2026 Q2, manufacturer's published lead time, prior project benchmark). Lead times have moved a lot since 2020; do not use pre-2023 numbers.
- Tolerance findings cite the contributing assemblies' tolerances and where they are sourced (AISC 303 for steel, ACI 117 for concrete, SMACNA for sheet metal, glazing manufacturer's installation guide).
- Phased-occupancy findings always reference the AHJ rule that drives the constraint (NYC DOB occupied-building protocols, CA HCAI for healthcare, school-district summer-only windows, GSA tenant-occupied protocols).
- Refuse to assert "this can't be built." If a detail is hard, the finding is "this drives the schedule / cost / coordination as follows" — constructors find a way; the review's job is to surface the cost.

## Anti-patterns

- Reviewing every axis when only 3-4 carry the project's risk. Pick the dominant risk axis first and weight others against it.
- Generic findings ("coordinate MEP", "tight tolerance") without the specific detail / dimension / lead-time number. Useless to the design team.
- Treating BIM clash detection as constructability review. Clash detection is necessary, not sufficient — clearance for installation tools (the wrench arc, the crane hook, the lift table) is a separate analysis.
- Ignoring the temporary condition. Many projects have life-safety and egress that are compliant in the final state but non-compliant in mid-construction; that gap is a real risk.
- Out-of-date lead times. Switchgear at 12 weeks (2019 reality) vs 40-60 weeks (2026 reality) is the kind of error that derails a schedule.
- Editing `index.md` manually instead of using `append_to_index.py`.

## Resources

- `scripts/init_constructability_workspace.py` — bootstrap `docs/constructability/` and the constructability index
- `scripts/append_to_index.py` — append a row to `docs/constructability/index.md`
- `references/constructability_axes.md` — eight-axis framework with sub-criteria, NA tolerance / clearance / lead-time benchmarks, common failure modes, example findings
- `references/long_lead_items_2026.md` — current (2026 Q2) lead-time table for switchgear, AHUs, chillers, custom curtain wall, structural steel, mass timber, elevators, with sourcing notes
- `assets/constructability-template.md` — review markdown template with severity-tagged findings block
