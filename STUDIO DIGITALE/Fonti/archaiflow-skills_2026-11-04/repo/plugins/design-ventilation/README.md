# Design Ventilation

Compute zone outdoor-air rates from the table you supply.

Computes outdoor-air ventilation rates zone by zone from the rate table you paste, with every step of the arithmetic shown: people component plus area component per zone, adjusted and summed the way your standard's procedure says. Trigger on "ventilation rate", "outdoor air", "OA calculation", "cfm per person", "air changes", "ventilation calc", "design-ventilation", or a pasted room schedule with occupancies. Works with any ventilation standard. The user names the standard and pastes its rate rows, occupant counts or the density rule, areas, and any effectiveness or system-level factors, each cited; the skill never supplies a rate, a density, or a factor from memory or from web search, and rows without a supplied rate come out unverified rather than filled. Supply-side outdoor air only: exhaust requirements, duct sizing, and energy are other calculations. Preliminary, never a substitute for the mechanical Engineer of Record.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **design-ventilation**.

In Claude Code:

```
/plugin install design-ventilation --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/design-ventilation
