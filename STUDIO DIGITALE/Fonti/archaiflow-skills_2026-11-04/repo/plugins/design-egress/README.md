# Design Egress

Verify exit counts, widths, separation, and travel distance.

Checks a floor or a tenancy against the means-of-egress items every building code regulates: egress capacity per occupant, number of exits required, single-exit allowance, common path of travel, exit separation, travel distance, corridor width, dead-end length, door clear width, and door swing threshold. Trigger on "check egress", "egress review", "exit count", "travel distance", "common path", "exit separation", "dead end corridor", "design-egress", "IBC 1006", "IBC 1017", "OBC 3.4", or a pasted plan with occupant load and exit positions. Works in any jurisdiction. The user names the governing code and edition and supplies each limit by typing it, pasting the clause, or naming a file to read. The skill never supplies a limit from memory or from web search, and any item without a supplied limit is reported as unverified rather than assumed. Does not compute occupant load, and does not replace the Architect of Record or the AHJ.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **design-egress**.

In Claude Code:

```
/plugin install design-egress --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/design-egress
