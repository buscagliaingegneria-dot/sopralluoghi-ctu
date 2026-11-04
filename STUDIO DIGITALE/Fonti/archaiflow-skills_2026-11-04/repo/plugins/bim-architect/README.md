# BIM Architect

A BIM lead's read on a model, family, or execution plan.

BIM architect's read on a Revit / IFC model snapshot, family content, BIM Execution Plan (BxP), worksharing setup, model-hygiene audit, view-template strategy, shared-coordinates / project-base-point setup, model-element-author (MEA) split, or coordination clash report — surfaces the one or two things most likely to bite rather than a full audit. Returns a short risk-flagged memo and names the skill to run next. Stays in lane: judgment, not family authoring or BxP rewrite. Use this agent for Revit/IFC/BIM-process lens; use `senior-architect` for design intent; use `interior-architect` for FF&E content; use `enclosure-architect` for envelope-detail Revit content. Examples that should trigger this agent — "what would a BIM architect say about this Revit model", "audit this BxP", "is this family parameter strategy sustainable", "worksharing setup review", "check the IFC export mapping", "shared coordinates / project base point sanity check".

This is an agent. It runs in Cowork and Claude Code, not in Chat.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **bim-architect**.

In Claude Code:

```
/plugin install bim-architect --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/agents/bim-architect
