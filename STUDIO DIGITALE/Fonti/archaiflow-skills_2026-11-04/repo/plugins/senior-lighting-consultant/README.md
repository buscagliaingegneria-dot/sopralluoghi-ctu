# Senior Lighting Consultant

A lighting designer on what the space will look like, not what it measures.

Lighting consultant's read on a scheme or a space — starts from what the space is for and how it should feel rather than from an illuminance target, checks whether the architecture gives the light anywhere to come from, reads daylight and electric light as one system rather than two, and flags where the ceiling, the controls or the maintenance access will undo the design. Returns a short memo on the two or three decisions that have to be made before the ceiling is coordinated. Stays in lane: lighting design judgment, not a photometric calculation, not a fixture schedule, not energy code compliance. Use this agent for lighting intent and its architectural consequences; use `senior-mep-engineer` for power and systems; use `energy-modeler` for energy; use `/test-energy` for the compliance path. Examples that should trigger this agent — "how should this space be lit", "read the lighting on this scheme", "will this ceiling work for lighting", "is the daylight doing anything here", "what would a lighting designer flag".

This is an agent. It runs in Cowork and Claude Code, not in Chat.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **senior-lighting-consultant**.

In Claude Code:

```
/plugin install senior-lighting-consultant --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/agents/senior-lighting-consultant
