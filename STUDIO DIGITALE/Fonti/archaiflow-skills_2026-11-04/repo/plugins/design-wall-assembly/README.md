# Design Wall Assembly

Build up an exterior wall layer by layer and place its four control layers.

Builds an exterior wall assembly from what the wall has to do rather than from a remembered stack: takes the cladding, the structure, the climate, the fire and acoustic demands and the drying direction you state, then places the four control layers (water, air, vapor, thermal) in an order, gives every layer a stated job, and works each interface where two layers meet and each transition where the wall stops. Trigger on "design a wall assembly", "wall build-up", "what goes in this wall", "layer the exterior wall", "where does the air barrier go", "rainscreen build-up", "design-wall-assembly", or a cladding and a structure named with a request for what sits between them. Supplies the ordering logic and the questions each interface has to answer; supplies no R-value, no permeance, no code minimum and no proprietary product. The arithmetic on the finished stack belongs to condensation-check and the continuity audit to air-barrier-trace, both of which this hands off to.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **design-wall-assembly**.

In Claude Code:

```
/plugin install design-wall-assembly --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/design-wall-assembly
