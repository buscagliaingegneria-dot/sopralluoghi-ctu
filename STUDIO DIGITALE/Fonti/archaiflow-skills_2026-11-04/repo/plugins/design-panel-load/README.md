# Design Panel Load

Total a panel's connected load and apply your demand factors.

Totals an electrical panel or service load: connected load summed by the categories your code uses, demand factors applied as you cite them, continuous-load multipliers as you cite them, and the result converted to amps at the voltage you state, with every step of the arithmetic shown. Trigger on "panel load", "load calc", "service size", "connected load", "demand load", "panel schedule totals", "design-panel-load", or a pasted load list. Works with any electrical code. The user supplies the load list, the category rules, the demand factor rows, and any multipliers, pasted and cited; the skill never supplies a demand factor, a VA allowance, or a multiplier from memory or from web search, and categories without a cited factor come out at connected load, marked unverified. Load totalling only: conductor and breaker sizing, fault current, voltage drop, and coordination are the electrical engineer's calculations and stop the run.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **design-panel-load**.

In Claude Code:

```
/plugin install design-panel-load --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/design-panel-load
