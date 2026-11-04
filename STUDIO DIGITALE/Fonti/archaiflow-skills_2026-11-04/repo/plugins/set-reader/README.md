# Set Reader

Read a whole drawing set and say what kind of set it is.

Reads a complete drawing set rather than a drawing: works out what phase it actually is regardless of what the title block claims, what is in it and what is missing for that phase, which disciplines are present and at what revision, how the set is organised, and what somebody receiving it would have to ask about first. Built for the set that arrives from somewhere else — a previous architect, a client, a design-build partner, a project you are taking over. Trigger on "read this set", "what have we been given", "we are taking over this project", "is this set complete", "set-reader", or a whole set handed over. Carries no standards and no phase definitions; completeness is judged against what the set itself claims to be. `drawing-reader` reads one sheet, `plan-review` reads a plan, `drawing-standards-audit` sweeps for conventions. It does not replace the Architect of Record.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **set-reader**.

In Claude Code:

```
/plugin install set-reader --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/set-reader
