# Design Duct

Size a duct run from the airflow and the limits you set.

Sizes a duct segment from an airflow and the limits you set: area from the velocity limit you state, rectangular dimensions within your aspect ratio, the equivalent-diameter arithmetic between round and rectangular, and a pressure-drop tally over a run when you supply the loss values, every step shown. Trigger on "duct size", "duct sizing", "duct velocity", "equivalent diameter", "static pressure", "cfm to duct size", "design-duct", or a pasted airflow with a size question. Works in either unit system, as given. The user supplies the airflow, the velocity or friction-rate limit with where it came from, aspect ratio limits, and any fitting loss values, cited; the skill never supplies a velocity limit, a friction rate, or a loss coefficient from memory or from web search. Geometry and arithmetic only: fan selection, system effect, acoustics, and leakage class are the mechanical engineer's calls. Preliminary, never a substitute for the mechanical Engineer of Record.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **design-duct**.

In Claude Code:

```
/plugin install design-duct --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/design-duct
