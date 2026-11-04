# RFI Tracker

Keep the RFI log, and watch the pattern the individual answers hide.

Keeps one dated RFI log and reads what the log says that no single RFI does: every RFI with who owns it, when it arrived, when the contract required an answer, when the answer went, and how it was classified, plus the running counts that reveal a pattern — a sheet generating a stream of questions, a contractor sending already-answered ones, a consultant consistently late, a set of clarifications quietly accumulating into a change. Trigger on "RFI log", "RFI tracker", "how many RFIs are open", "are we late on RFI responses", "which drawings are generating RFIs", "rfi-tracker", or an RFI register handed over to keep. Carries no response periods and no classifications of its own; the contract sets the turnaround and each RFI's class comes from whoever answered it. It does not answer RFIs — `/draft-rfi-response` does — and does not replace the Architect of Record.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **rfi-tracker**.

In Claude Code:

```
/plugin install rfi-tracker --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/rfi-tracker
