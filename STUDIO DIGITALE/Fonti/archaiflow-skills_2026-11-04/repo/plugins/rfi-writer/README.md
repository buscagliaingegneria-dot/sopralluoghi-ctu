# RFI Writer

Turn a site question into a filed, formal RFI.

This skill should be used when the user provides an informal construction-site question — drawing/spec discrepancies, dimension conflicts, missing details — and needs a formal Request for Information (RFI) document filed in the project. Trigger on phrases like "make an RFI", "draft an RFI", "send this as an RFI", or pasted site questions implying transmittal to design consultants. Generates a numbered RFI markdown file in `docs/rfis/` and updates the project's RFI log.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **rfi-writer**.

In Claude Code:

```
/plugin install rfi-writer --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/rfi-writer
