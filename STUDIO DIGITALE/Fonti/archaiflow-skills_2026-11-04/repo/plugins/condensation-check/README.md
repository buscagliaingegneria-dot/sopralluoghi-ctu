# Condensation Check

Trace the temperature gradient through an assembly and find the dew point.

Works out where water condenses inside a wall, roof, or floor assembly: the temperature at every layer boundary from the layer R-values and the design conditions, the dew point of the indoor air from its temperature and relative humidity, and which boundary is the first to fall below it. Then walks the layers in order of vapor permeance to flag a vapor-tight layer sitting on the cold side of the insulation, or two of them sealing the assembly from both directions. Trigger on "condensation check", "dew point in this wall", "will this assembly condense", "vapor retarder on the wrong side", "sheathing temperature", "condensation-check", or an assembly listed layer by layer with indoor and outdoor conditions. Every R-value, permeance, design temperature, and humidity comes from the user, out of manufacturer data, a climate data set, or the project's own documents; the skill supplies the heat-flow and psychrometric relations and never a material property.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **condensation-check**.

In Claude Code:

```
/plugin install condensation-check --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/condensation-check
