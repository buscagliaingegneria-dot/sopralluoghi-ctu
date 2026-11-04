# Explain Riser Diagram

Read an MEP riser diagram and find where it disagrees with the plans.

Reads a plumbing, electrical, fire protection or mechanical riser diagram in plain English and then does the check nobody runs: comparing it against the architectural plans floor by floor, since a riser diagram is a schematic with no geometry and it is routinely drawn for a building whose shafts, floor levels or floor count have since changed. Explains what the diagram is showing, what it deliberately does not show, and every place it assumes something the plans do not provide. Carries no pipe or conduit sizes, no slopes and no code requirements. It does not check the engineering and does not replace the MEP engineer. For adding up the shaft space use `/size-shaft`.

This is a command. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **explain-riser-diagram**.

In Claude Code:

```
/plugin install explain-riser-diagram --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/commands/explain-riser-diagram
