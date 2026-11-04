# Submittal Log

Build a submittal log from the spec book.

Reads a project specification section by section, pulls out every submittal each one calls for, classifies it, and assembles a submittal log ready to issue. Trigger on "build submittal log", "submittal log", "extract submittals from spec", "shop drawing log", "submittal register", "submittal-log-builder", or a pasted specification section list. Works with any specification format and any contract. The user supplies the spec text by pasting it, naming files to read, or pointing at an indexed PDF, and supplies the review durations from their own contract. The skill never invents a submittal, never carries a list of typical submittals, and never assumes a review duration: every row traces to a line in the user's spec, and anything it could not find is listed as a gap rather than filled in.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **submittal-log-builder**.

In Claude Code:

```
/plugin install submittal-log-builder --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/submittal-log-builder
