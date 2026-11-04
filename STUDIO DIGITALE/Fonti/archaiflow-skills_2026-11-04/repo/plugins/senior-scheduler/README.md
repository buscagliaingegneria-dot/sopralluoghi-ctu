# Senior Scheduler

A planner's read on what actually controls the date, and who controls it.

Construction planner's read on a programme — traces what genuinely controls the completion date rather than what the bars suggest, finds the near-critical paths that turn a small slip into a claim, checks whether the design team's own review durations were honoured in the logic, and says plainly where the schedule is optimistic and where it is defensive. Returns a short memo naming the controlling chain, two to four risks, and what to ask the contractor. Stays in lane: planning judgment, not means and methods, not a delay analysis, not a re-plan. Use this agent for a read on a programme; use the `schedule-review` skill to work through a submitted schedule systematically; use `senior-contractor` for buildability; use `senior-cost-estimator` for money. Examples that should trigger this agent — "is this programme realistic", "what's really driving the completion date", "read this baseline for me", "are we exposed on submittal durations", "what would a scheduler say about this update".

This is an agent. It runs in Cowork and Claude Code, not in Chat.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **senior-scheduler**.

In Claude Code:

```
/plugin install senior-scheduler --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/agents/senior-scheduler
