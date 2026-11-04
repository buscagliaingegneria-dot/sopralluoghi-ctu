# Wind Snow Lookup

Assemble the site hazard criteria a design needs.

Assembles the site environmental criteria block a project needs before any structural or envelope design starts: wind, snow, seismic, ice, rain, and flood parameters, each recorded with the source it came from. Trigger on "wind speed for this site", "ground snow load", "site hazard parameters", "design criteria block", "seismic parameters", "rainfall intensity", "wind-snow-lookup", or a pasted site location with a request for design values. Works in any jurisdiction. The skill knows which parameters a design needs and what each one feeds; the values come from the user's own code maps, official hazard tool, or authority, supplied by typing, pasting, or naming a file. It never supplies a hazard value from memory or from web search, and reports every parameter it could not source as a gap. Returns mapped parameters only, never design pressures or loads.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **wind-snow-lookup**.

In Claude Code:

```
/plugin install wind-snow-lookup --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/wind-snow-lookup
