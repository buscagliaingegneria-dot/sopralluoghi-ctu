---
name: passive-house-tracker
description: "This skill should be used when the user wants to track a Passive House project against the published certification thresholds — PHIUS+ 2021 (PHIUS, North American climate-specific targets) or PHI (Passive House Institute, fixed metric criteria — Classic / Plus / Premium). The user supplies modeled values (annual heating demand, annual cooling+dehumidification demand, source / primary energy, air leakage, peak loads, overheating frequency) from WUFI Passive or PHPP; the skill compares against published targets and emits a pass/fail-per-metric scorecard. Trigger on \"PHIUS+ score\", \"Passive House tracker\", \"PHI Classic check\", \"compare WUFI/PHPP results to PHIUS+ targets\", or pasted modeling outputs. Reads bundled PHIUS+ 2021 methodology + PHI fixed criteria from `references/` and outputs CSV + markdown summary in `docs/passive-house/`. Does NOT generate climate-specific PHIUS+ targets — user must fetch project-specific targets from the PHIUS portal (phius.org/phius-source-zero) before scoring."
license: MIT
metadata:
  title: "Passive House Tracker"
  summary: "Track modeled performance against certification thresholds"
  discipline: "envelope-performance"
  tags: "Compliance"
---


# Passive House Tracker


## Overview


Track a Passive House project against the published certification thresholds for either PHIUS+ 2021 (PHIUS, North American climate-specific) or PHI (Passive House Institute, fixed metric criteria — Classic / Plus / Premium). The user provides modeled values from WUFI Passive (PHIUS workflow) or PHPP (PHI workflow); the skill compares against published targets and reports pass/fail per metric. Output is a CSV (one row per metric) plus a markdown summary in `docs/passive-house/`. This replaces the manual cross-check pass at every PH project's modeling milestones (early SD, DD pre-cert, CD final).


This skill **does not** decide whether the project _will_ certify — that is a strategy + verifier call. The skill organizes the structure, performs the compare, cites target values verbatim from `references/`, and flags any failing metric with the published gap.


## Scope and limits — read first


This skill covers:

- **PHIUS+ 2021** — climate-specific targets (annual heating, annual cooling+dehum, source energy, peak loads), air-leakage, overheating frequency. Targets are climate-specific; the skill compares user-supplied targets to user-supplied actuals.
- **PHI Classic / Plus / Premium** — fixed metric criteria (annual heating ≤ 15 kWh/m²·a ≈ 4.75 kBtu/sf·yr; airtightness ≤ 0.6 ACH50; etc.) with published values bundled.
- **Output format**: per-metric pass / fail / pending, with computed gap (actual − target) for each metric.

This skill does **NOT** cover:

- **Generating PHIUS+ 2021 climate-specific targets** for a project. PHIUS publishes per-ZIP targets via its Source Zero portal at phius.org. Users must fetch their project's targets there before running this skill.
- **Energy modeling** itself. The skill consumes modeled values from WUFI Passive or PHPP; it does not run the model.
- **PHIUS+ 2018 / 2015 / 2012 / pre-2021**. Earlier targets differ; out of scope.
- **PHIUS 2024** (post-2021 PHIUS revision). When PHIUS 2024 supersedes 2021 in the field, update `references/` and the **Last verified** date in `references/_provenance.md`.
- **EnerPHit** (PHI retrofit standard). Different criteria; out of scope.
- **Costing, embodied carbon, daylighting, IAQ** — these belong to LEED / WELL / LBC / Phius+CO2 trackers.
- **Regional certifier acceptance**. Some AHJs / utility-rebate programs accept PHIUS+; some accept PHI; some accept either. The skill does not make that determination.

For any user-supplied target, the skill records the user's stated source (PHIUS portal export, PHI standard table) — it does not validate that the target matches the user's project ZIP.


## When to use


Trigger on:

- "Make a PHIUS+ scorecard from my WUFI run."
- "Compare these PHPP results to PHI Classic."
- "Track our Passive House project — DD modeling milestone."
- Pasted WUFI Passive or PHPP output ("annual heating demand 4.2 kBtu/sf·yr, source energy 36 kBtu/sf·yr, ACH50 0.42 …").

Do NOT trigger on:

- "Generate the PHIUS+ targets for my project ZIP" — out of scope; user must fetch from PHIUS portal.
- "Run the energy model" — out of scope; skill is post-modeling check.
- LEED / WELL / LBC / EnerPHit scoring — separate trackers.
- ASHRAE 90.1 / IECC envelope checks — use `climate-zone-mapper`.

## Workflow


### Step 1 — Bootstrap if needed


Check whether `docs/passive-house/index.md` exists. If not, run:


```bash
python scripts/init_workspace.py
```


The script creates `docs/passive-house/` and an empty tracker log. No external Python dependencies.


### Step 2 — Confirm certification path


State explicitly to the user:

> "This skill compares modeled results to published Passive House targets. Choose your certification path: **PHIUS+ 2021** (PHIUS, climate-specific targets — you must supply targets from your PHIUS Source Zero export); or **PHI Classic / Plus / Premium** (Passive House Institute, fixed metric criteria — bundled). EnerPHit (PHI retrofit) is out of scope. Continue?"

Do not proceed silently. The certification path determines which references are used.


### Step 3 — Gather project context


Read `docs/project.md` if present. Otherwise ask the user for:

- `project_name`
- `project_slug`
- `cert_path` — `phius_2021` or `phi_classic` or `phi_plus` or `phi_premium`
- `phase` — `early_sd` / `dd_pre_cert` / `cd_final` / `post_occupancy`
- `floor_area_sf` — conditioned floor area (interior conditioned area, ICFA for PHIUS)
- For PHIUS+ 2021 only: a path to the user's PHIUS Source Zero target export (CSV or pasted values for the metrics: annual heating, annual cooling+dehum, source energy, peak heating, peak cooling).

### Step 4 — Initialize a fresh scorecard, or update an existing one


If a scorecard CSV exists at `docs/passive-house/<project-slug>-ph-scorecard.csv`, load it. Otherwise initialize from `assets/passive-house-scorecard-template.csv`, which is pre-seeded with the metric rows for the chosen `cert_path`:

- For PHIUS+ 2021: metrics = annual heating demand, annual cooling+dehum demand, source energy, peak heating load, peak cooling load, air leakage, limited overheating frequency. Target column is empty — user fills from PHIUS portal export.
- For PHI Classic / Plus / Premium: metrics + target values are pre-seeded from `references/phi_classic_criteria.md`. User only fills `Actual`.

### Step 5 — Capture modeled values


Walk the metric list with the user. For each metric, the user provides:

- `Target` (PHIUS+ only — from PHIUS Source Zero portal export)
- `Actual` — from WUFI Passive or PHPP modeling
- `Source` — file path or screenshot reference of the modeling output
- `ConfidenceFlag` — `high` (final certified-modeler run), `medium` (mid-design check), `low` (rough early-SD estimate)

For metrics not applicable to the project (e.g. cooling+dehum in extreme cold climate), mark `N/A`.


### Step 6 — Compute pass/fail


Run:


```bash
python scripts/compute_score.py \
  --scorecard docs/passive-house/<project-slug>-ph-scorecard.csv \
  --cert-path <phius_2021|phi_classic|phi_plus|phi_premium> \
  --out docs/passive-house/.cache/<project-slug>-score.json
```


The script computes:

- Per-metric `Status` = `pass` / `fail` / `pending` / `N/A` (pass = `Actual ≤ Target` for `lower_is_better` metrics).
- Per-metric `Gap` = `Actual - Target` (positive = over-target, negative = under-target / passing).
- Overall certification compatibility — `all_pass` / `failures: [...]` / `pending_required: [...]`.

The script reads target methodology / fixed values from `references/` — never hard-coded.


### Step 7 — Write the markdown summary


Write `docs/passive-house/<project-slug>-ph-summary.md`:

- Header: project + cert path + phase + ICFA + last-updated date.
- Per-metric pass/fail table with target, actual, gap, status, source, confidence.
- Failures list (top decisions for the design team).
- Pending-metric list (to capture before next milestone).
- Citation footer: PHIUS+ 2021 / PHI source, reference file paths, last-verified date.

### Step 8 — Update the project Passive House index


Run:


```bash
python scripts/append_to_index.py \
  --date 2026-05-09 \
  --project "<project-slug>" \
  --cert-path "<cert-path>" \
  --phase "<phase>" \
  --pass-count <N> \
  --fail-count <N> \
  --pending-count <N> \
  --csv "<project-slug>-ph-scorecard.csv" \
  --summary "<project-slug>-ph-summary.md"
```


Appends a row to `docs/passive-house/index.md`. Do NOT edit `index.md` with Edit.


### Step 9 — Report


Tell the user:

- Path to scorecard CSV + summary.
- Pass / fail / pending counts.
- Failure list with computed gap (e.g. "Annual heating demand: 5.2 kBtu/sf·yr (target 4.5; over by 0.7)").
- Pending list — metrics user has not yet entered.
- Reminder: this is a structural compare against published targets — final certification depends on PHIUS / PHI verifier review.

## Rules

- For PHIUS+ 2021, the `Target` column must be populated from the user's PHIUS Source Zero portal export. The skill does NOT generate climate-specific targets and does NOT trust training data for them. If the user lacks targets, the skill halts and tells them to fetch from phius.org.
- For PHI Classic / Plus / Premium, target values are quoted verbatim from `references/phi_classic_criteria.md`. No modification by Claude.
- `Actual` cells must come from a stated modeling tool (WUFI Passive or PHPP). The Source cell records the model file or screenshot reference — never blank.
- Pass/fail evaluation is computed by `compute_score.py`, never by Claude inline.
- All outputs live in `docs/passive-house/` of the user's project.
- Standard version (PHIUS+ 2021 or PHI 2025-edition) and last-verified date are reported in every summary.

## Anti-patterns

- Inventing climate-specific PHIUS+ 2021 target values from training data. PHIUS targets are per-ZIP; only the user's portal export is authoritative.
- Reproducing PHI fixed values from memory rather than `references/phi_classic_criteria.md`. References are the single source.
- Computing pass/fail by hand (Claude doing arithmetic). The script runs the compare.
- Treating PHIUS 2024 / EnerPHit / pre-2021 PHIUS as scoreable here.
- Mixing units. Imperial-first (kBtu/sf·yr, CFM50/sf, °F); metric in parens for PHI source values.
- Editing `docs/passive-house/index.md` directly with Edit. Use `append_to_index.py`.

## Resources

- `scripts/init_workspace.py` — bootstrap `docs/passive-house/`
- `scripts/compute_score.py` — compare actuals to targets, emit pass/fail JSON
- `scripts/append_to_index.py` — append a row to `docs/passive-house/index.md`
- `references/_provenance.md` — PHIUS + PHI source pointers, last-verified
- `references/phius_2021_targets.md` — PHIUS+ 2021 methodology + sample climate-specific targets (illustrative only — user must fetch project targets from PHIUS portal)
- `references/phi_classic_criteria.md` — PHI Classic / Plus / Premium fixed criteria with imperial conversions
- `assets/passive-house-scorecard-template.csv` — pre-seeded metric rows
- `assets/passive-house-index-template.md` — header table for `docs/passive-house/index.md`
