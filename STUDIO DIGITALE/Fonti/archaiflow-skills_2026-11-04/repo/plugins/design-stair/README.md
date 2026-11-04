# Design Stair

Check a stair flight against the limits your code sets.

Checks one stair flight item by item: width, headroom, riser, tread, uniformity, nosing, landing, vertical rise between landings, handrail height, wall clearance, cross section, extensions, both-sides requirement, and open risers. Trigger on "check stair", "stair compliance", "stair dimension check", "riser tread check", "handrail extension", "stair code check", "IBC 1011", "ADA stair", "OBC stair", "NBC stair", or pasted stair geometry. Works in any jurisdiction. The user names the governing code and edition, then supplies each limit by typing it, pasting the clause, or naming a file to read. The skill never supplies a code value from memory or from web search, and any row without a supplied limit is reported as unverified rather than guessed. Does not replace the Architect or Engineer of Record, and does not cover curved, spiral, winder, or alternating tread stairs.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **design-stair**.

In Claude Code:

```
/plugin install design-stair --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/design-stair
