# Spec Outline Builder

Build the section list this project needs from the drawings it has.

Builds a specification's section list from the drawings rather than from the last project's table of contents: walks the set for every material, system and scope shown, maps each to a section, then runs the check in both directions — work drawn with no section, and sections carried forward with no work. Marks each section's status so the book's real completeness is visible rather than implied by a full-looking contents page. Trigger on "what spec sections do we need", "build the table of contents", "spec outline", "do we have a section for this", "spec-outline-builder", or a drawing set handed over before the book is written. Carries no section numbers, no titles and no master list; numbering comes from the format your office uses and `/lookup-csi` finds one number. For auditing a book that exists use `spec-review`; for one paragraph use `/draft-spec-snippet`.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **spec-outline-builder**.

In Claude Code:

```
/plugin install spec-outline-builder --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/spec-outline-builder
