# Size Louver

Add up the louver face a mechanical airflow needs, from data you supply.

Adds up the face area a louver needs from the airflow the engineer gives and the performance data of the actual louver being considered: required free area from airflow and maximum face velocity, required face area from the product's free-area fraction, then the fit into the opening the elevation actually has, mullions and frames included. Reports required face size against the opening as drawn. Carries no velocities, no free-area percentages, and no rain-class limits; the airflow comes from the mechanical engineer and every performance figure from the data sheet of the named louver, because free area varies by product and by size and a remembered percentage sizes the wrong louver. It does not size the duct or the fan behind the louver — `design-duct` does — it does not lay out the room the air serves (`design-mechanical-room`), and it does not compose the elevation the louver lands on (`facade-module`).

This is a command. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **size-louver**.

In Claude Code:

```
/plugin install size-louver --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/commands/size-louver
