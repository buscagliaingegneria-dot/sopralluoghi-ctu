# Compare Structural System

Put structural systems side by side on what each does to the architecture.

Compares two or more structural systems — steel, cast-in-place concrete, mass timber, bearing wall, whatever is on the table — on the criteria you name, using values you and your engineer supply for each one. This is the architect's side of the decision: what each system does to floor depth and floor-to-floor height, to the grid and the spans, to fire protection strategy, to acoustics, to whether the structure can be the finish, to MEP routing, and to schedule. Builds the comparison matrix, holds every system to the same criteria, and marks any cell where one system has a figure and another does not, because that asymmetry is where a comparison quietly decides itself. Carries no spans, no depths, no costs, no carbon figures; every number comes from the engineer, the estimator, or a source you name. The engineer owns and stamps the system itself — `explain-load-path` traces how one works, `design-beam` and `design-column` check single members, and `compare-assembly` is the same matrix for envelope build-ups.

This is a command. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **compare-structural-system**.

In Claude Code:

```
/plugin install compare-structural-system --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/commands/compare-structural-system
