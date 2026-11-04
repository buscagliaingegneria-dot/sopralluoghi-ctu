# Test Occupant Load

Compute occupant load when you already have the table row.

Single-shot occupant-load math against IBC §1004 + Table 1004.5 source text the user has already in hand. Lighter than the `design-occupancy-load` skill — `/test-occupant-load` is for "I have the Table row and the SF, just compute it" while `design-occupancy-load` walks the full multi-turn fetch + multi-use sum workflow. Carries no IBC values internally. Federal IBC only.

This is a command. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **test-occupant-load**.

In Claude Code:

```
/plugin install test-occupant-load --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/commands/test-occupant-load
