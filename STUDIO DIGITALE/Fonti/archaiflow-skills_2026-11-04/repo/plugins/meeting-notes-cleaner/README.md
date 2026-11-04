# Meeting Notes

Turn raw meeting notes into structured action items.

This skill should be used when the user provides raw architectural project meeting notes — transcripts, STT output, .vtt/.srt files, or jotted text — and needs structured action items. Trigger on 'clean up meeting notes', 'meeting summary', 'process this transcript', or pasted multi-speaker content covering project decisions, schedule, or scope. Generates a structured meeting markdown in `docs/meetings/` and merges new To-dos into the project's `docs/todos.md`.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **meeting-notes-cleaner**.

In Claude Code:

```
/plugin install meeting-notes-cleaner --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/meeting-notes-cleaner
