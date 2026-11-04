# Accessibility Tracker

Build an accessibility compliance checklist for a project.

Builds an accessibility compliance checklist for a project in two passes: scoping, meaning how many of each element must be accessible, and technical, meaning what each accessible element must measure. Trigger on "accessibility checklist", "ADA check", "accessibility compliance", "accessible parking count", "accessible toilet count", "barrier free check", "ada-tracker", or a pasted program with counts of parking, units, or toilet rooms. Works with any accessibility standard. The user names the standard and supplies both the scoping rule and each technical dimension, by typing them, pasting the clause, or naming a file to read. The skill never supplies an accessibility value from memory or from web search, and every row it could not source is reported as unverified rather than filled in. Writes a CSV checklist and appends to a project index.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **ada-tracker**.

In Claude Code:

```
/plugin install ada-tracker --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/ada-tracker
