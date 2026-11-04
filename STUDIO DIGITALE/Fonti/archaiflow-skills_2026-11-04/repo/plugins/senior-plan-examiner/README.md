# Senior Plan Examiner

Reads your set the way the person who can reject it will read it.

Reads a drawing set from the other side of the counter — as the plan examiner who will issue the correction letter rather than as the consultant hired to get it through. Predicts the comments the set will attract, in the order an examiner works, flags every place the set makes the reviewer hunt for something, and separates the comments that are the examiner's job to raise from the ones the set invited. Returns the likely correction letter with a short reason for each item. Stays in lane: prediction of review, not redesign and not a compliance opinion. Use this agent before a submission; use `senior-code-consultant` for the compliance path itself; use `code-compliance-review` for a clause-level audit; use `plan-check-response-builder` once the real comments arrive. Examples that should trigger this agent — "what will the plan checker say about this set", "read this like a reviewer", "are we going to get a correction letter", "what comments should we expect", "pre-submission review of this set".

This is an agent. It runs in Cowork and Claude Code, not in Chat.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **senior-plan-examiner**.

In Claude Code:

```
/plugin install senior-plan-examiner --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/agents/senior-plan-examiner
