# Design Parking Layout

Lay out parking around the bay, the aisle, and the ramp.

Lays out a parking floor from the module rather than from the space left over: settles the bay and aisle dimensions and the column grid that follows from them, works the ramp against the floor-to-floor it has to climb, places accessible spaces where the standard requires them rather than where they fit, and reports the count achieved against the count required. Trigger on "parking layout", "how many cars fit", "parking bay module", "ramp slope and transitions", "where do the accessible spaces go", "design-parking-layout", or a garage floor plate with a count to hit. Carries no bay dimensions, no aisle widths, no ramp slopes, no headroom and no accessible ratios; every one comes from the jurisdiction's standard or the accessibility standard you quote. `/test-parking` counts what is required. It does not do traffic or structural engineering and does not replace the Architect of Record.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **design-parking-layout**.

In Claude Code:

```
/plugin install design-parking-layout --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/design-parking-layout
