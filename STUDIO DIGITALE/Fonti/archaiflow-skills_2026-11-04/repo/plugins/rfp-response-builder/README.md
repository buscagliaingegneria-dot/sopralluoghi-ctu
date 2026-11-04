# RFP Response Builder

Build a response that answers what was asked, in their order.

Builds an RFP or RFQ response around the evaluation criteria rather than around the practice's usual material: pulls every requirement and every question out of the document into a compliance matrix, follows the issuer's structure and numbering exactly, and checks before submission that every requirement has an answer and every page limit and format rule is met. Trigger on "respond to this RFP", "RFQ response", "build the proposal response", "do we answer everything in this RFP", "rfp-response-builder", or a solicitation handed over to answer. Carries no boilerplate and no standard firm material; everything comes from the practice's own content. For a federal qualifications package use `sf330-builder`; to decide whether to respond at all use `go-no-go-review` first. It does not decide the fee and does not replace the principal.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **rfp-response-builder**.

In Claude Code:

```
/plugin install rfp-response-builder --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/rfp-response-builder
