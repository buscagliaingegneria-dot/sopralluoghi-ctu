# Design Column

Check an axially loaded column with the values your standard gives.

Checks a single axially loaded, braced column against the capacity your standard's values produce, with every step of the arithmetic shown: slenderness from your effective length factor, capacity from the expression or table row you supply, demand over capacity at the end. Trigger on "column check", "column size", "post size", "axial capacity", "slenderness check", "KL/r", "design-column", or a pasted column load with a trial section. Works with any design standard. The user names the standard and method and supplies the load combinations, the effective length factor, the section and material properties, and the capacity expression or its tabulated value, by typing, pasting, or naming a file; the skill never supplies an engineering value, a buckling curve, or a section from memory or web search. Concentric axial load on a braced member only; combined bending needs your interaction equation or it stops. Preliminary sizing, never a substitute for the Engineer of Record.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **design-column**.

In Claude Code:

```
/plugin install design-column --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/design-column
