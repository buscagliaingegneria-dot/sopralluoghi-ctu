# Drawing Log

Track every sheet's revision and issue history in one log.

Maintains a drawing issue log in docs/drawings/log.md: every sheet in the set, its current revision, and every dated issuance with its purpose. Trigger on "drawing log", "issue log", "sheet log", "revision log", "what rev is", "when did we issue", "drawing register", "drawing-log", or a request to record that a set went out. The sheet list can be seeded from a drawing-set-bookmarker index or typed; revisions and issue dates come from you, never from a guess. Superseded sheets are marked, not deleted, so the log answers what was in force on any past date. It records what was issued to whom; the cover sheet for a package is create-transmittal's job, and what changed inside a sheet is drawing-diff's.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **drawing-log**.

In Claude Code:

```
/plugin install drawing-log --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/drawing-log
