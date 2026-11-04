# Test Fire Rating

Check the required hourly rating for an element.

Single-element fire-resistance rating gut-check via IBC Table 601 + Table 602 — for each element the command WebFetches the relevant Table row live from codes.iccsafe.org (or accepts a paste) and labels the required hourly rating against the verbatim source. Carries no IBC values internally. Federal IBC only — state amendments and sprinkler-trade adjustments (§403, §504, §506) are out-of-scope.

This is a command. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **test-fire-rating**.

In Claude Code:

```
/plugin install test-fire-rating --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/commands/test-fire-rating
