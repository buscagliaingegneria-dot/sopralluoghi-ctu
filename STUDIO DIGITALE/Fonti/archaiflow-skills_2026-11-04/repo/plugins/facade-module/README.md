# Facade Module

Divide an elevation into panels and lay out the leftover, option by option.

Divides elevation lengths and heights by a panel module and works the remainder into explicit options: resize every panel equally, absorb the leftover in end or corner panels, or take it in one feature bay, with the arithmetic for each and a check of where mullions land against the structural grid. Trigger on "panelize", "curtain wall module", "facade module", "mullion spacing", "panel layout", "facade-module", or an elevation length paired with a module. Every dimension comes from the user: elevation lengths and floor heights from their drawings, the module and any panel size limits from the manufacturer's literature, the grid from their structural plans. The skill never supplies a manufacturer's maximum panel size or a standard module from memory, does not size mullions or check wind load, does not judge thermal or glare performance, and does not choose between the options it lays out.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **facade-module**.

In Claude Code:

```
/plugin install facade-module --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/facade-module
