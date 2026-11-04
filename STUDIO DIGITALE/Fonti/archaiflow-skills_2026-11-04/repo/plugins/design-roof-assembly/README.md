# Design Roof Assembly

Build up a roof assembly and place the control layers a roof cannot dry through.

Builds a low-slope or steep-slope roof assembly from what the roof has to do rather than from a remembered stack: takes the membrane or covering, the deck, the climate, the interior humidity, the equipment landing on it and the slope you have to work with, then places the four control layers (water, air, vapor, thermal) in an order, gives every layer a stated job, and works the curbs, drains, penetrations and edges where roofs actually leak. Trigger on "design a roof assembly", "roof build-up", "compact roof", "what goes above the deck", "insulation above or below the deck", "vented or unvented roof", "design-roof-assembly", or a membrane and a deck named with a request for what sits between them. Supplies the ordering logic and the questions each condition has to answer; supplies no R-value, no permeance, no slope minimum, no code requirement and no proprietary product. The arithmetic belongs to condensation-check and the continuity audit to air-barrier-trace, both of which this hands off to.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **design-roof-assembly**.

In Claude Code:

```
/plugin install design-roof-assembly --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/design-roof-assembly
