# Drawing Reader

Read and interpret an architectural drawing PDF.

Reads an architectural drawing PDF and answers questions about it: a single sheet, a full set, a redline, a record drawing, a shop drawing, or a detail. Summarises, finds a sheet, explains a detail, lists disciplines, or pulls a callout. Trigger on "read this drawing", "what is in this set", "summarize this drawing", "show me sheet X", "what is on this sheet", or a pasted path to a drawing PDF. For specifications, codes, contracts, and reports use doc-reader instead. Detects the drawing type, asks what is wanted before reading at length, and hands off to schedule-extractor, drawing-set-bookmarker, or drawing-checklist when one of those fits better. Never reports a dimension or a note it did not read off the sheet.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **drawing-reader**.

In Claude Code:

```
/plugin install drawing-reader --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/drawing-reader
