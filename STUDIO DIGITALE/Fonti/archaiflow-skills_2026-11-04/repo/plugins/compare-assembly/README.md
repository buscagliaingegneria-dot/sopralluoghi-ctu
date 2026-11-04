# Compare Assembly

Put two or more envelope build-ups side by side on criteria you name.

Compares two or more envelope assemblies — wall, roof, or below-grade build-ups — on the criteria you name, using values you supply for each one. Builds the comparison matrix, holds every assembly to the same criteria, and marks any cell where one assembly has a figure and another does not, because that asymmetry is where a comparison quietly decides itself. Carries no material properties, no code minimums, and no cost data; every number in the table comes from you or from a source you name. For comparing design options generally rather than build-ups specifically use the `option-compare` skill; for the arithmetic inside one assembly use `condensation-check`; for laying out a new assembly use `design-wall-assembly` or `design-roof-assembly`.

This is a command. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **compare-assembly**.

In Claude Code:

```
/plugin install compare-assembly --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/commands/compare-assembly
