# Elevation Review

Read an elevation for what it decides and what it flattens away.

Reads any elevation for the two things it is doing at once: composing a facade, and hiding the depth that makes it buildable. An elevation is a flat drawing of something that is not flat, so joints, reveals, returns, thicknesses and everything behind the surface are all drawn as lines of equal weight or not at all. Checks what it commits to, what it leaves to a section, and where it disagrees with the plan. Trigger on "read this elevation", "does this facade work", "they sent elevations", "check this elevation against the plan", "elevation-review", or any elevation handed over. Carries no dimensions or module sizes; anything measured is read at the stated scale. `facade-module` divides an elevation into panels and `design-envelope` decides what each face has to be; this reads the drawing. It does not replace the Architect of Record.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **elevation-review**.

In Claude Code:

```
/plugin install elevation-review --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/elevation-review
