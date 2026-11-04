# Test FAR

Check floor area ratio, coverage, setback, and height.

Single-parcel zoning gut-check (FAR / lot coverage / setback / height) — for each topic the command WebFetches the operative § live from the jurisdiction's published zoning portal (or accepts a paste) and math-checks provided dimensions against the verbatim source. Carries no zoning values internally. Single base district only — overlays / bonuses / variances are out-of-scope.

This is a command. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **test-far**.

In Claude Code:

```
/plugin install test-far --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/commands/test-far
