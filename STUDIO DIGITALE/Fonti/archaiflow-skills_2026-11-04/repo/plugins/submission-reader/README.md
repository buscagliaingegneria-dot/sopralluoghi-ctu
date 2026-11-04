# Submission Reader

Read what an authority sent back and say what it actually requires.

Reads a letter from an authority — a correction letter, a completeness notice, a staff report, a conditional approval, a denial — and separates the four things inside it that behave differently: what must change, what must be shown, what must be answered, and what is a comment with nothing to do. Then finds the parts that carry a clock, since a response period or an appeal window is usually one line in the middle of a page. Trigger on "they sent this back", "read this correction letter", "what does the city actually want", "plan check comments came in", "submission-reader", or any letter from an authority handed over to work out. Carries no procedures and no periods; every deadline comes from the letter or from the jurisdiction. `plan-check-response-builder` writes the response; this works out what the letter asked. It does not replace the code consultant, the expeditor, or the Architect of Record.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **submission-reader**.

In Claude Code:

```
/plugin install submission-reader --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/submission-reader
