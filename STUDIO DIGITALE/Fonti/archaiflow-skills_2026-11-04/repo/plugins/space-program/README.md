# Space Program

Track the room list, target areas, and designed areas as they move.

Maintains a space program in docs/program/program.md: every space the project must contain, its required quantity and target area from the brief, the area the current plan gives it, and the delta. Trigger on "space program", "program of requirements", "room list", "area program", "programming", "target area", "are we over program", "space-program", or a pasted brief with a room schedule to capture. Targets come from the brief or the client, measured areas come from your plan, and the grossing factor comes from you; the skill supplies none of them and computes only the arithmetic between them, shown. Works in the unit system the brief uses. Reports name every space still missing a target or a measured area rather than hiding them in totals. Interrogating the brief itself is brief-review's job.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **space-program**.

In Claude Code:

```
/plugin install space-program --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/space-program
