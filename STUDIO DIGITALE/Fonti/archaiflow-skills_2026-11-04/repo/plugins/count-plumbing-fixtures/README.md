# Count Plumbing Fixtures

Work out required fixture counts from the table you supply.

Computes required plumbing fixture counts for a building from the occupant load and the fixture ratio table you supply: splits the occupant load by use and by sex where the table does, applies each ratio, rounds the way the table says to round, and reports the count per fixture type per sex alongside what was provided. Carries no ratios, no occupant load factors and no rounding rules — every one of those is code text you quote or paste, because fixture tables differ between the plumbing code, the building code and local amendments, and they are amended often. For the occupant load itself use `/test-occupant-load` or the `design-occupancy-load` skill first. Does not size drainage, does not lay out the rooms, and does not decide accessibility counts beyond what the pasted table states.

This is a command. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **count-plumbing-fixtures**.

In Claude Code:

```
/plugin install count-plumbing-fixtures --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/commands/count-plumbing-fixtures
