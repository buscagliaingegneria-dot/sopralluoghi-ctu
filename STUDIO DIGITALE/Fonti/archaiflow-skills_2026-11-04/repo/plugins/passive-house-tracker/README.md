# Passive House Tracker

Track modeled performance against certification thresholds.

This skill should be used when the user wants to track a Passive House project against the published certification thresholds — PHIUS+ 2021 (PHIUS, North American climate-specific targets) or PHI (Passive House Institute, fixed metric criteria — Classic / Plus / Premium). The user supplies modeled values (annual heating demand, annual cooling+dehumidification demand, source / primary energy, air leakage, peak loads, overheating frequency) from WUFI Passive or PHPP; the skill compares against published targets and emits a pass/fail-per-metric scorecard. Trigger on "PHIUS+ score", "Passive House tracker", "PHI Classic check", "compare WUFI/PHPP results to PHIUS+ targets", or pasted modeling outputs. Reads bundled PHIUS+ 2021 methodology + PHI fixed criteria from `references/` and outputs CSV + markdown summary in `docs/passive-house/`. Does NOT generate climate-specific PHIUS+ targets — user must fetch project-specific targets from the PHIUS portal (phius.org/phius-source-zero) before scoring.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **passive-house-tracker**.

In Claude Code:

```
/plugin install passive-house-tracker --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/passive-house-tracker
