# Calculation Reader

Read an engineer's calculation for its inputs, not its arithmetic.

Reads any calculation an architect is handed — structural, thermal, egress, drainage, load, acoustic — and checks the part an architect can and should check: the inputs, the assumptions, the standard it was worked to, and the version of the design it was worked from. The arithmetic is sealed by somebody and is not the architect's to verify; the inputs frequently describe a building that has changed since. Trigger on "read this calculation", "they sent calcs", "what did the engineer assume here", "is this calc still valid", "calculation-reader", or any calculation handed over. Carries no formulas, values or code limits. It verifies no arithmetic, has no engineering opinion, and does not replace the engineer of record or the Architect of Record.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **calculation-reader**.

In Claude Code:

```
/plugin install calculation-reader --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/calculation-reader
