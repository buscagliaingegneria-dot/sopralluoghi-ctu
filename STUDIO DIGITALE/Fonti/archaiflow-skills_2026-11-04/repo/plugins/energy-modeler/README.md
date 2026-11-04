# Energy Modeler

An energy modeler's read on a performance model.

Energy-modeler's read on an ASHRAE 90.1 Appendix G performance-path model / IES VE / EnergyPlus / OpenStudio input + assumption + result narrative + LEED EAc1 (v4 / v4.1) Optimize Energy Performance submission — surfaces the one or two things most likely to bite instead of running a full QA. Returns a short risk-flagged model-review brief with its reasoning, then names the skill to run next. Stays in lane: judgment of model integrity + assumption defensibility, not running the model. Use this agent for energy-model review lens; use `leed-tracker` for full LEED scorecard; use `passive-house-tracker` for PHIUS modeling; Examples that should trigger this agent — "review this energy model basis-of-design", "ASHRAE 90.1 App G modeling check", "is this LEED EAc1 submission going to clear", "EnergyPlus input audit", "baseline vs proposed envelope mismatch check", "schedule + setpoint reasonableness review".

This is an agent. It runs in Cowork and Claude Code, not in Chat.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **energy-modeler**.

In Claude Code:

```
/plugin install energy-modeler --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/agents/energy-modeler
