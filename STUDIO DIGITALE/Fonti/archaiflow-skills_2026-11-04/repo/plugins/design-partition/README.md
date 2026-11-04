# Design Partition

Build up an interior partition and decide where it stops.

Builds an interior partition type from what the partition has to do rather than from a wall type legend copied forward: takes the acoustic separation, the fire rating, the structural condition above and what has to be fixed to it, then works the build-up and the two decisions that decide whether it performs — how far up it goes, and what happens at the head where the structure above moves. Trigger on "partition type", "interior wall build-up", "does this wall go to deck", "STC between these rooms", "deflection head detail", "wall type legend", "design-partition", or a room adjacency with a question about the wall between. Carries no ratings, no STC values, no stud spacings and no listings; performance comes from the specification or the acoustician and every rated assembly is a tested system you cite. For an exterior wall use `design-wall-assembly`; for a rated assembly's continuity use `design-fire-barrier`. It does not replace the Architect of Record.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **design-partition**.

In Claude Code:

```
/plugin install design-partition --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/design-partition
