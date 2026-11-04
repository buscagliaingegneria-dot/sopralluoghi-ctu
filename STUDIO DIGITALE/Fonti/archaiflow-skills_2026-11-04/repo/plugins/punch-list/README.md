# Punch List

Keep a punch list with location, trade, owner, and status per item.

Maintains a project punch list in docs/construction/punch-list.md. Trigger on "punch list", "punch item", "snag list", "deficiency list", "defect list", "punch walk", "punch-list", or a pasted site visit report whose observations should become tracked items. Each item carries a location, a description, the responsible trade, the date raised, its source, and a status that separates completed from verified, because a contractor marking work done is not the same as the architect seeing it done. The skill never invents an item, a responsible party, or a completion; what it was not told stays open. Feeds on create-site-visit-report output. It does not decide substantial completion and does not certify anything; those are contract acts.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **punch-list**.

In Claude Code:

```
/plugin install punch-list --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/punch-list
