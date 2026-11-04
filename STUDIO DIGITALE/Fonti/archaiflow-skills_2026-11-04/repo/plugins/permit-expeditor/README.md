# Permit Expeditor

Plans the route through the building department, and unsticks a stalled one.

A permit expeditor's read on how a project actually gets through its building department — which approvals it needs, in what order, which can run in parallel, what intake will bounce, and where the weeks go. Works the process, not the code: the sequence of planning, building, fire, health, public works and utility sign-offs, the pre-application meeting worth asking for, the separate permits everyone forgets, and what to do this week when a review has gone quiet. Returns the route as a dependency table plus the next three actions. Stays in lane: process navigation, not a code opinion, not a comment prediction, not a timeline guarantee. Use this agent to plan a submission or unstick one; use `senior-plan-examiner` to predict the correction letter; use `senior-code-consultant` for the compliance path; use the `permit-tracker` skill to keep the dated log once things are moving. Examples that should trigger this agent — "how do I get this permitted", "what approvals does this project need", "our permit has been sitting for six weeks", "what order do these reviews happen in", "do we need a pre-app meeting".

This is an agent. It runs in Cowork and Claude Code, not in Chat.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **permit-expeditor**.

In Claude Code:

```
/plugin install permit-expeditor --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/agents/permit-expeditor
