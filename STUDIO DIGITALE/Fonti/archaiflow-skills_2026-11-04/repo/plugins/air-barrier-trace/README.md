# Air Barrier Trace

Follow the air, water, vapor, and thermal layers around a section for breaks.

Traces each of the four enclosure control layers, air first, then water, vapor, and thermal, around a building section as one continuous line, and reports every joint where that line changes material, changes plane, or is crossed by something: foundation, slab edge, wall base, floor lines, window and door openings, corners and cladding changes, parapets and eaves, roof level changes, and every penetration. Each joint records what carries the layer on either side, what makes the connection, and which drawing shows it. Trigger on "air barrier continuity", "trace the air barrier", "control layer check", "where does the air barrier break", "is the WRB continuous", "air-barrier-trace", or a wall section handed over with a continuity question. The drawings, the layer assignments, and any airtightness target come from the user; the skill supplies the joint sequence and the questions asked at each one, and never names a membrane, tape, sealant, or leakage rate.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **air-barrier-trace**.

In Claude Code:

```
/plugin install air-barrier-trace --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/air-barrier-trace
