# Drawing Diff

See what changed between two drawing revisions.

Compares two revisions of the same sheet or drawing set and reports what actually changed. Trigger on "what changed between these revisions", "compare Rev C and Rev D", "diff these drawings", "did they change anything", "check this against the last issue", or two pasted PDF paths of the same sheet or set. Matches pages by the sheet number printed in the title block rather than by page order, diffs extracted text to catch dimension, note, and tag edits, overlays the rendered pages to find linework that moved, then reads the changed regions to describe them. Flags changes carrying no revision cloud, and clouds carrying no change. Writes one report per comparison to `docs/drawing-diffs/`.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **drawing-diff**.

In Claude Code:

```
/plugin install drawing-diff --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/drawing-diff
