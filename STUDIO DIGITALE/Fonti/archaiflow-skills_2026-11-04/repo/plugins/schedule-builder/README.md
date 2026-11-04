# Schedule Builder

Build a door, window, finish, or room schedule that the drawings can survive.

Builds a drawing schedule of any type — door, window, finish, room, wall type, equipment — by settling the column set before any row is filled, since the columns are what the schedule is and adding one later means revisiting every row. Takes the items from your drawings or model, fills only what you supply, marks every gap rather than defaulting it, and checks the finished schedule against the plans for items scheduled but not drawn and drawn but not scheduled. Trigger on "build a door schedule", "window schedule", "finish schedule", "room data sheet", "wall type schedule", "make a schedule from these drawings", "schedule-builder", or a request to assemble any drawing schedule. Carries no default column sets, no hardware sets, no fire ratings and no product data; the columns come from your office standard and every value comes from you. For extracting a schedule that already exists in a PDF use `schedule-extractor`. It does not replace the Architect of Record.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **schedule-builder**.

In Claude Code:

```
/plugin install schedule-builder --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/schedule-builder
