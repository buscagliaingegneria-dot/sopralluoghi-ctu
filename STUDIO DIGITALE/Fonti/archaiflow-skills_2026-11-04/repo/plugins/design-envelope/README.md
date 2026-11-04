# Design Envelope

Decide what each face of the building has to be, before detailing any.

The door into envelope work, and the step usually skipped: before any assembly is built up, decide how many envelope types the building actually has, which face gets which, where the junctions between them fall, and what each one has to achieve. Produces the schedule of types and junctions that the assembly and junction skills then execute against, and hands each part off by name. Trigger on "design the envelope", "how many wall types do we need", "what should this facade be", "envelope strategy", "where do the assemblies change", "design-envelope", or an envelope scope with no strategy behind it. Carries no R-values, no assemblies and no code minimums; performance requirements come from the code and the brief you quote. It builds nothing itself — `design-wall-assembly`, `design-roof-assembly` and the junction skills do — and does not replace the enclosure consultant or the Architect of Record.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **design-envelope**.

In Claude Code:

```
/plugin install design-envelope --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/design-envelope
