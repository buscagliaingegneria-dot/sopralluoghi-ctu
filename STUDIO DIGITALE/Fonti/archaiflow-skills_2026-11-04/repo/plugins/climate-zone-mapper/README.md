# Climate Zone Mapper

Record a site's climate zone and its envelope requirements.

Records the climate or thermal zone a project sits in, then builds the envelope requirement scorecard component by component: roof, walls above and below grade, floors, slab edge, fenestration thermal, fenestration solar gain, and air leakage. Trigger on "what climate zone is this", "climate zone for this site", "envelope requirements for zone X", "energy code envelope scorecard", "climate-zone-mapper", or a pasted project address with an envelope question. Works with any energy code. The zone determination and every requirement value come from the user, typed, pasted, or read from a file they name. The skill never supplies a zone, an R-value, a U-factor, or a solar gain figure from memory or from web search, and any component without a supplied requirement is reported as unverified. Writes a CSV scorecard and a summary.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **climate-zone-mapper**.

In Claude Code:

```
/plugin install climate-zone-mapper --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/climate-zone-mapper
