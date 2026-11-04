# Design Occupancy Load

Compute occupant load by use group and by space.

Computes occupant load space by space, then subtotals by use group and gives a building or floor total. Trigger on "occupant load", "calc occupants", "occupancy load", "how many occupants", "design-occupancy-load", "IBC 1004", "OBC 3.1.17", or a pasted program listing spaces with use and area. A foundation calculation: its output feeds egress, plumbing fixture counts, allowable area, and stair width. Works in any jurisdiction. The user names the governing code and edition and supplies each load factor by typing it, pasting the table row, or naming a file to read. The skill never supplies a factor from memory or from web search, and a space with no factor is reported as unverified rather than estimated. Does not count fixed seating, and does not replace the Architect of Record or the AHJ.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **design-occupancy-load**.

In Claude Code:

```
/plugin install design-occupancy-load --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/design-occupancy-load
