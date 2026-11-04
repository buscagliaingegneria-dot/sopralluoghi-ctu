# Explain Panel Schedule

Read an electrical panel schedule and say what it means for the architecture.

Reads an electrical panel schedule in plain English for someone who is not an electrical engineer: what each column is, how the circuits map to spaces, what the connected and demand loads mean, whether the panel has spare capacity and what spare actually means, and what the schedule implies for the architecture — where the panel has to go, how much wall it takes, what clearance in front of it cannot be built on, and what feeds it. Carries no clearance dimensions, no demand factors and no code requirements; those come from the code text you quote or from the engineer. It does not check the electrical design and does not replace the electrical engineer. For totalling a panel's load use the `design-panel-load` skill.

This is a command. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **explain-panel-schedule**.

In Claude Code:

```
/plugin install explain-panel-schedule --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/commands/explain-panel-schedule
