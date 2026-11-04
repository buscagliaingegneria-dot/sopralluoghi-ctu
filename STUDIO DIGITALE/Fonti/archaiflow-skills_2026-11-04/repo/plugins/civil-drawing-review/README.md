# Civil Drawing Review

Check the civil set against the architectural, in both directions.

Reads a civil set against the architectural set for the disagreements that only show up where the two meet: the finished floor against the finished grade at every door, the accessible route against the actual slopes, where utilities enter the building against where the risers are, and what the civil drawings assume about a building they were not drawn from. Reports every conflict with both values and rules on neither. Trigger on "review the civil drawings", "do the civil and architectural agree", "grading around the building", "utility entry coordination", "civil-drawing-review", or a civil set issued for coordination. Carries no slope limits, no cover requirements and no utility standards; accessibility limits come from the standard you quote and utility requirements from the utility. It is not civil engineering, does not check drainage design, and does not replace the civil engineer or the Architect of Record.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **civil-drawing-review**.

In Claude Code:

```
/plugin install civil-drawing-review --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/civil-drawing-review
