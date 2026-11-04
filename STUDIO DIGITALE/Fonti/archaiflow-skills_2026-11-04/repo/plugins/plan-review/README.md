# Plan Review

Read a plan for what is on it, what is missing, and what it implies.

Reads any floor plan you hand it and reports three things separately: what is drawn, what a plan of this kind should show and does not, and what the plan commits to without saying so. Works whatever the project type, whatever the phase, and whether the plan is yours, a consultant's, a client's previous architect's, or one found in a property listing. Trigger on "read this plan", "what do you make of this floor plan", "review this layout", "they sent us a plan", "plan-review", or a plan handed over with no particular question attached. Carries no dimensions and no standards; anything measured comes from what is on the drawing. `design-critic` judges a design, `code-compliance-review` audits against eight code axes, and `circulation-study` traces the journeys; this reads the drawing first, which is what the other three assume has happened. It does not replace the Architect of Record.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **plan-review**.

In Claude Code:

```
/plugin install plan-review --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/plan-review
