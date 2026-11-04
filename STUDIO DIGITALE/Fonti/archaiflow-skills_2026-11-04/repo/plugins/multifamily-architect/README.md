# Multifamily Architect

A housing architect on the unit mix, the plate, and the core.

Multifamily housing architect's read on a residential scheme — reads the unit mix against the plate and the core before anything else, because efficiency in housing is decided by how many units reach a corridor and how much corridor it takes to reach them, then surfaces what the pro forma will push back on, what the code does to double-loaded corridors and single-stair schemes, and where the amenity and parking assumptions are carrying the project. Returns a short memo with the two or three decisions with the most leverage. Stays in lane: housing design judgment, not a pro forma, not code compliance, not a redesign. Use this agent for housing schemes; use `senior-architect` for the general building-design lens; use `senior-living-architect` for age-restricted and care settings; use `senior-code-consultant` for the compliance path. Examples that should trigger this agent — "read this apartment scheme", "is this unit mix workable", "what's the efficiency on this plate", "single stair or double loaded here", "what would a housing architect flag".

This is an agent. It runs in Cowork and Claude Code, not in Chat.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **multifamily-architect**.

In Claude Code:

```
/plugin install multifamily-architect --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/agents/multifamily-architect
