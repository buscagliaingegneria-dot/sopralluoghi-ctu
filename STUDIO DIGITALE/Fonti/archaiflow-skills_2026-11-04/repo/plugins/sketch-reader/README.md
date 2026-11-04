# Sketch Reader

Read a sketch, an image, or a model view and say what it commits to.

Reads the drawings that are not drawings: a hand sketch, a napkin diagram, a photograph of a whiteboard, a rendered view, a screenshot of a model. Separates what is decided from what is drawn loosely and what is placeholder, since the three look alike in a sketch and the difference is the whole content. Then names what the sketch has already committed to without anybody deciding it. Trigger on "read this sketch", "what does this diagram say", "the client sent a drawing they did", "read this rendering", "what does this model view show", "sketch-reader", or any informal drawing handed over. Carries no dimensions and reads no scale off an unscaled drawing. `drawing-reader` reads a measured PDF; this reads the ones drawn by hand or produced to look convincing. It does not judge the design and does not replace the Architect of Record.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **sketch-reader**.

In Claude Code:

```
/plugin install sketch-reader --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/sketch-reader
