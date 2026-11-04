# Shadow Study

Compute sun angles and shadow reach for a massing, date, and place.

Computes solar altitude and azimuth from latitude, date, and time, then the shadow a massing casts: length, direction, and, if the user supplies the distance, whether it reaches a neighboring line. Trigger on "shadow study", "how far does the shadow go", "solstice shadows", "will my building shade the neighbor", "shadow-study", or a massing height paired with a date and a place. The solar geometry is computed from published astronomy formulas, the one thing this skill works out itself; everything else comes from the user: heights, distances, grades, and any shadow criteria the jurisdiction enforces. Flat ground is assumed unless the user supplies grades. It is a design-stage tool for comparing massing options, not a submission-grade shadow study, and it does not know which hours or open spaces any city protects.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **shadow-study**.

In Claude Code:

```
/plugin install shadow-study --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/shadow-study
