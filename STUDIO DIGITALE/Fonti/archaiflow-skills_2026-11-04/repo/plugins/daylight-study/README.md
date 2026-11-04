# Daylight Study

Work out how deep daylight reaches into each room, and which rooms stay dark.

Checks each room's depth against how far sidelight can reach it, from the window head heights, room depths, and glazing areas the user supplies: daylit depth by a stated convention, glazing-to-floor arithmetic held against a code minimum the user quotes, and the no-sky line when a facing building is in the way. Trigger on "daylight study", "how deep does daylight reach", "is this room too deep for daylight", "no-sky line", "daylight-study", or room depths paired with window head heights. The depth convention and the obstruction geometry are the only things this skill supplies itself; every dimension, glazing area, and code minimum comes from the user. It is a plan-stage tool for comparing layouts, not a daylighting simulation: no daylight factor, no illuminance, no glare, no LEED credit documentation, all of which come from a model. Exterior shadows on neighbors belong to shadow-study; energy-code glazing checks belong to test-glazing.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **daylight-study**.

In Claude Code:

```
/plugin install daylight-study --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/daylight-study
