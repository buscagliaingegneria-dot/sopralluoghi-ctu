# Envelope Checklist

Get the envelope checklist for the phase and the assemblies you have.

Builds the envelope checklist for one project rather than handing over a generic one: takes the assemblies this building actually has and the phase it is at, and produces what should be resolved by now, what can still wait, and what is already late. Works from the junction list rather than from the assemblies, because assemblies get drawn and junctions get discovered. Trigger on "envelope checklist", "what should be resolved by DD", "are we ready to issue the envelope", "what have we missed on the facade", "envelope-checklist", or an envelope scope at a phase change. Carries no standard checklist and no performance values; the items come from the assemblies and junctions this project has. `drawing-checklist` covers the drawing set by phase; this covers the envelope by what it is made of. It does not replace the enclosure consultant or the Architect of Record.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **envelope-checklist**.

In Claude Code:

```
/plugin install envelope-checklist --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/envelope-checklist
