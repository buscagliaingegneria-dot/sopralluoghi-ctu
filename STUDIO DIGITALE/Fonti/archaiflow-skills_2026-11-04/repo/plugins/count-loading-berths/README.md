# Count Loading Berths

Work out required loading berths from the table you supply.

Computes required off-street loading from the zoning table you supply: applies the ratio by use and floor area, applies the berth dimensions and vertical clearance the text states, and then asks the question the table does not — whether a truck can actually reach the berth, turn, and leave without reversing into the street. Reports the code count and the operational check separately, because a project can satisfy one and fail the other. Carries no ratios, no berth dimensions and no design vehicle; all come from the jurisdiction's text and from the operation. For parking counts use `/test-parking`; for how everything reaches the site use the `site-access-study` skill.

This is a command. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **count-loading-berths**.

In Claude Code:

```
/plugin install count-loading-berths --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/commands/count-loading-berths
