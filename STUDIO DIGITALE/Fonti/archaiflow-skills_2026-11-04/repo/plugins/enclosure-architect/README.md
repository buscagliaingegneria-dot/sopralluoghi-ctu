# Enclosure Architect

An enclosure architect's read on a wall, roof, or window detail.

Licensed building-enclosure architect's read on a wall section, parapet detail, curtain-wall shop drawing, fenestration spec, air/water/vapor barrier diagram, thermal-bridge detail, roof assembly, or hygrothermal (WUFI) analysis — surfaces the one or two things most likely to bite rather than a full audit. Returns a short risk-flagged memo and names the skill to run next. Stays in lane: judgment, not redesign or assembly proposal. Use this agent for façade / enclosure lens; use `senior-architect` for building-design lens; use `interior-architect` for finish/FF&E lens; use `senior-mep-engineer` for HVAC implications. Examples that should trigger this agent — "what would an enclosure architect say about this wall section", "review this curtain wall shop drawing", "thermal bridge check at this slab edge", "is this roof detail going to leak", "WUFI / condensation read on this assembly".

This is an agent. It runs in Cowork and Claude Code, not in Chat.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **enclosure-architect**.

In Claude Code:

```
/plugin install enclosure-architect --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/agents/enclosure-architect
