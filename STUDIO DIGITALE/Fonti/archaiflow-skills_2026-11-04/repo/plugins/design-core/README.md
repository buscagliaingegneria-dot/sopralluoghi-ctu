# Design Core

Add up the core from your own dimensions and check its share of the plate.

Aggregates the pieces of a building core (elevator shafts, stairs, toilets, mechanical and electrical shafts and rooms) from dimensions the user supplies, applies the user's own wall-and-circulation factor, and reports total core area and core-to-floor-plate ratio against the user's benchmark, showing every step. Trigger on "core sizing", "how big is my core", "core-to-floor ratio", "core efficiency", "design-core", or a floor plate paired with a list of core components. Every dimension comes from the user: shaft sizes from manufacturer cut sheets, stair footprints from the user's stair layout, room sizes from the user's plans, the grossing factor and the target ratio from the user's own benchmarks. The skill never supplies a typical shaft size, fixture count, or target ratio. It does not decide elevator count (the elevator consultant's traffic analysis does), does not check stair or fixture code compliance, and is not a substitute for the Architect of Record.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **design-core**.

In Claude Code:

```
/plugin install design-core --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/design-core
