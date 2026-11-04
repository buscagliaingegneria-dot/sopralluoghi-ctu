# Equipment Reader

Read a cut sheet for what the building has to give the equipment.

Reads any product or equipment data sheet and pulls out the six things a building has to provide for it: the space it occupies, the clearance it needs on each side to be serviced, the route to get it in and out, the services it needs and from where, what it weighs and what carries it, and what it does to the room around it in heat, noise and vibration. Works for a rooftop unit, a lift, a range, a transformer, a door closer or a light fitting. Trigger on "read this cut sheet", "what does this unit need", "they sent product data", "will this fit", "equipment-reader", or a data sheet handed over with a question about space. Carries no dimensions or clearances of its own: every figure comes off the sheet, and a figure absent from the sheet is reported missing rather than assumed from a similar product. It does not select or size equipment and does not replace the engineers or the Architect of Record.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **equipment-reader**.

In Claude Code:

```
/plugin install equipment-reader --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/equipment-reader
