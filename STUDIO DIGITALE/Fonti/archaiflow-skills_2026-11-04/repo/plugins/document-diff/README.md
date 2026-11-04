# Document Diff

Compare two versions of a document and find what nobody mentioned.

Compares two versions of a written document — an agreement, a specification section, a programme, a code analysis, an owner's requirements — and reports every change, not the ones the covering note listed. Separates a wording change from a change in obligation, flags every deletion because deletions are what a redline is worst at showing, and reports what moved rather than changed, since relocated text reads as unchanged in most comparisons. Trigger on "what changed between these two versions", "compare these contracts", "diff this spec section", "they sent a revised agreement", "document-diff", or two versions of anything written handed over together. Carries no view on what any clause should say; `contract-review` and `spec-review` read one version on its merits. It is not legal advice and does not replace the attorney or the Architect of Record. For drawings use `drawing-diff`.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **document-diff**.

In Claude Code:

```
/plugin install document-diff --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/document-diff
