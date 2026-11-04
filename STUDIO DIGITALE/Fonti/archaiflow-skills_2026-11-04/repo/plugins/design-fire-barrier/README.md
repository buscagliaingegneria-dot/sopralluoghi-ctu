# Design Fire Barrier

Follow a rated assembly from floor to deck and find where the rating stops.

Follows one rated assembly as a continuous surface rather than as a wall type on a plan: establishes what kind of separation it is and therefore what continuity the code demands, traces it from floor slab to deck above and along its full length, and works every place the rating is interrupted by a penetration, a joint, a duct, a door, a glazed opening or the structure it is attached to. Trigger on "fire barrier detail", "rated wall continuity", "does this wall go to deck", "firestopping at the top of wall", "fire partition versus fire barrier", "rated assembly penetrations", "design-fire-barrier", or a rated wall named with a question about how it is built. Carries no hourly ratings, no opening limits, no tested assembly numbers and no firestop listings; the required rating comes from `/test-fire-rating` or your code analysis, and every assembly and firestop is a tested and listed system you cite. It does not replace the fire protection engineer, the code consultant, or the Architect of Record.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **design-fire-barrier**.

In Claude Code:

```
/plugin install design-fire-barrier --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/design-fire-barrier
