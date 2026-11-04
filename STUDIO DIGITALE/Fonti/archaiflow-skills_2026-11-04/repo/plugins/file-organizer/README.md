# File Organizer

Sort a messy folder into a taxonomy you approve first.

Sorts a disorganized folder into a target tree, by writing a move plan you read and approve before any file is touched. Trigger on "organize this folder", "sort these files", "clean up this directory", "tidy this handoff folder", "file organizer", or a pasted path plus an organizing verb. Matches on filename, extension, size, and modified date, never on file contents. Finds duplicates by hash and routes them for review rather than deleting anything. Every run writes a plan first, executes only against the approved plan, and appends an audit log that a rollback can read backwards. The taxonomy is yours: the skill will draft one from what it finds, but it does not invent target folders you did not agree to.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **file-organizer**.

In Claude Code:

```
/plugin install file-organizer --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/file-organizer
