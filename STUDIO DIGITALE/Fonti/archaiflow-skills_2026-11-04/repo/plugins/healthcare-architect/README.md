# Healthcare Architect

A healthcare architect's read on a hospital or clinic plan.

Licensed healthcare architect's read on a hospital / outpatient / clinic floor plan, OR layout, patient-room headwall, clean-corridor pressurization diagram, ICRA phasing plan, med-gas zone-valve plan, imaging-suite shielding, behavioral-health unit, FGI compliance check, or HCAI submission package — surfaces the one or two things most likely to bite rather than a full audit. Returns a short risk-flagged memo and names the skill to run next. Stays in lane: judgment, not redesign or program revision. Use this agent for healthcare-specific (FGI / HCAI / NFPA 99 / ASHRAE 170) lens; use `senior-architect` for general building-shell lens; use `senior-mep-engineer` for med-gas/HVAC system sizing; use `code-compliance-review` for full IBC compliance audit. Examples that should trigger this agent — "FGI check on this OR layout", "HCAI submission readiness", "ICRA path coordination", "med-gas zone valve placement check", "healthcare RFI on patient-room headwall".

This is an agent. It runs in Cowork and Claude Code, not in Chat.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **healthcare-architect**.

In Claude Code:

```
/plugin install healthcare-architect --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/agents/healthcare-architect
