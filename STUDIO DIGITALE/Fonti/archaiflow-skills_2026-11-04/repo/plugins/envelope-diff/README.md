# Envelope Diff

Compare two versions of an assembly or a detail and price the change.

Compares two versions of an envelope assembly or detail and reports what the change does rather than what it looks like: which control layer moved, what continuity was gained or lost, which junction details are now wrong, and whether the drying direction changed. Built for the moment a contractor proposes an alternate, a manufacturer's detail replaces yours, or a value-engineering round comes back, because those changes arrive one layer at a time and their consequences arrive at the junctions. Trigger on "what changed in this assembly", "they proposed a different build-up", "compare these two sections", "is this substitution equivalent", "envelope-diff", or two versions of an envelope construction handed over together. Carries no values; every figure comes with the versions. `document-diff` compares written documents and `drawing-diff` drawing revisions; this compares what an assembly does. It does not replace the enclosure consultant or the Architect of Record.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **envelope-diff**.

In Claude Code:

```
/plugin install envelope-diff --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/envelope-diff
