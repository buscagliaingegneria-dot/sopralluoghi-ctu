# Document Export

Render Markdown into Word, Excel, or PDF for transmittal.

Converts structured Markdown into Word, Excel, or PDF for issue to a client, contractor, or authority: meeting minutes, RFIs, transmittals, change orders, punchlists, decision logs, payment applications. Trigger on "render this as Word", "export to Excel", "save as PDF", "make this a transmittal", or when a slash command in this catalog reaches its output step with a non-Markdown format declared. One direction only, Markdown to file. Carries the conversion recipes and the rules that stop a converter from quietly rewriting project content: units are never converted, dates are never re-localised, clause symbols and authority names survive intact, and a table stays a real table rather than becoming an image or a block of text.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **aec-doc-gen**.

In Claude Code:

```
/plugin install aec-doc-gen --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/aec-doc-gen
