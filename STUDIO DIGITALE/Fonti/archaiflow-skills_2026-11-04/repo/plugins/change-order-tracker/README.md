# Change Order Tracker

Track every change from first mention to executed, including the ones that stall.

Keeps one dated log of every change from the moment it is first raised, not from the moment it becomes a change order: records where each one came from, what instrument carried it, its cost and time position at every stage, and who it is sitting with, so that the work directed but not yet priced and the changes stalled between proposal and execution are both visible. Reports the running total against the contingency and the count of changes proceeding on direction alone. Trigger on "change order log", "track changes", "how much have we spent of the contingency", "what changes are outstanding", "work proceeding without a change order", "change-order-tracker", or a change register handed over to keep. Carries no cost data, no markup rates and no contract periods; all come from the contract and the proposals. It does not price, review, or negotiate a change — `change-order-review` does that for one — and does not replace the Architect of Record.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **change-order-tracker**.

In Claude Code:

```
/plugin install change-order-tracker --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/change-order-tracker
