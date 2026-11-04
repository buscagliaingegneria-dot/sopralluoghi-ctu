# Plan Check Response Builder

Turn a reviewer's comments into a matrix that answers each one on the record.

Turns a plan check or plan review comment set into a response matrix that answers every comment individually and on the record: splits comments that contain more than one question, sorts each into agreed, clarification, or disagreement, points every response at the specific sheet and detail that changed, and keeps the disagreements civil and evidenced because those are the ones that get read twice. Trigger on "plan check comments", "respond to the plan reviewer", "correction letter", "plan review response", "resubmittal response matrix", "plan-check-response-builder", or a set of reviewer comments pasted with a request to answer them. Carries no code positions of its own and never argues a clause from memory; every response either cites the drawing that changed or quotes the code text you supply. For a letter to the department rather than a comment matrix use `/draft-letter`; for tracking the submission itself use `permit-tracker`.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **plan-check-response-builder**.

In Claude Code:

```
/plugin install plan-check-response-builder --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/plan-check-response-builder
