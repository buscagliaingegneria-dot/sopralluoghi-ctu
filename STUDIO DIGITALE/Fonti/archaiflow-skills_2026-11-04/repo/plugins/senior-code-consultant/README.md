# Senior Code Consultant

A code consultant's read on which compliance path this building should take.

Code consultant's read on the strategic compliance decisions that set a project's cost before any detail is drawn — occupancy classification and its edge cases, construction type against allowable area and height, where separations and fire areas should fall, what sprinklering buys, whether a horizontal exit or a separated-use approach opens the plan, and which requirements are worth an alternative means request. Surfaces the two or three decisions with the most leverage rather than auditing the drawing. Returns a short memo naming the path, what it depends on, and what to verify. Stays in lane: strategy and risk, not clause-by-clause checking and not fire engineering. Use this agent for the compliance path; use `senior-fire-protection-engineer` for sprinkler, alarm and smoke control engineering; use `accessibility-specialist` for accessibility; use `senior-plan-examiner` for how a reviewer will read it. Examples that should trigger this agent — "what construction type should we be targeting", "is this two occupancies or one", "would sprinklering pay for itself here", "where should the fire areas fall", "what would a code consultant say about this scheme".

This is an agent. It runs in Cowork and Claude Code, not in Chat.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **senior-code-consultant**.

In Claude Code:

```
/plugin install senior-code-consultant --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/agents/senior-code-consultant
