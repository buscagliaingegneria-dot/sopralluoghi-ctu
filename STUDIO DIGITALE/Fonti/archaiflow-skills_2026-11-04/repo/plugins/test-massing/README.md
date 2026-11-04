# Test Massing

Compare massing options by computed GFA, height, and net area.

Runs the massing arithmetic for one or more schemes: floor plate area times floor count gives GFA, floor count times floor-to-floor gives height, and an optional net-to-gross factor gives net area, all compared side by side and against targets the user supplies. Trigger on "massing options", "massing study", "how many floors do I need", "GFA check", "compare schemes", "test-massing", or a pasted list of plate areas and floor counts. Pure arithmetic: it carries no zoning limits, no typical floor heights, and no typical efficiency factors. Targets come from the user's own zoning check or brief. For whether a massing is legal, use /test-far; this command answers what each option adds up to.

This is a command. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **test-massing**.

In Claude Code:

```
/plugin install test-massing --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/commands/test-massing
