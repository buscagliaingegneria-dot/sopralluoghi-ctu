# Schedule Review

Read a contractor's schedule for what it assumes about you.

Reads a contractor's construction schedule from the design team's side rather than as a planner: finds every activity that depends on the architect, the consultants or the owner and checks whether the durations allowed match the contract, traces the critical path to see what actually controls the end date, looks for the logic that makes a delay claim inevitable, and separates what is a genuine concern from what is only unfamiliar. Trigger on "review the contractor's schedule", "CPM schedule review", "is this baseline reasonable", "submittal durations in the schedule", "schedule update review", "schedule-review", or a programme submitted for comment. Carries no durations, no productivity rates and no float conventions; the contract sets the review periods and the schedule specification sets the rules. It is not planning software, does not re-plan the work, does not opine on means and methods, and does not replace the scheduler or the Architect of Record.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **schedule-review**.

In Claude Code:

```
/plugin install schedule-review --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/schedule-review
