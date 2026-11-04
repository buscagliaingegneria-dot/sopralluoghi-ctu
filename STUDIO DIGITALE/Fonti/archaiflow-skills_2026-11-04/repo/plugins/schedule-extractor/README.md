# Schedule Extractor

Pull door, window, and finish schedules out of a PDF into CSV.

This skill should be used when the user has a drawing-set PDF containing one or more tabular schedules (door schedule, window schedule, room finish schedule, equipment schedule) and wants the rows pulled out as a normalized CSV for cross-checking, takeoff, or import into Excel/Revit. Trigger on "extract the door schedule", "pull the finish schedule", "tabulate this schedule", "schedule to CSV", or a pasted PDF path with mention of a schedule type. Reads schedule pages via vision, normalizes columns to the AIA / NCS Section A6 conventions, and writes CSV + markdown preview to `docs/schedules/`.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **schedule-extractor**.

In Claude Code:

```
/plugin install schedule-extractor --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/schedule-extractor
