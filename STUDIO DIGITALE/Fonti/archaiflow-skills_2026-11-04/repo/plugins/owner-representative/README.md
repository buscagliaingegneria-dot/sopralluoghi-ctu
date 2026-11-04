# Owner Representative

Reads your recommendation the way the person paying for it will.

Owner's representative read on a recommendation, a change proposal, a report, or a design decision — asks what it costs, what it does to the date, what happens if it is not done, and what the owner is being asked to decide versus merely told, then flags where the professional advice has been written for the profession rather than for the person signing. Returns a short memo with the decision restated as the owner would hear it, the questions that will be asked, and what is missing before it can be decided. Stays in lane: the owner's lens, not a redesign, not a cost estimate, not a decision. Use this agent before sending a recommendation to a client; use `client-translator` to rewrite technical language; use `senior-cost-estimator` for the number itself; use `senior-scheduler` for time. Examples that should trigger this agent — "how will the client read this", "what will the owner ask about this recommendation", "is this report ready to send", "read this change proposal from the owner's side", "what would an owner's rep push back on".

This is an agent. It runs in Cowork and Claude Code, not in Chat.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **owner-representative**.

In Claude Code:

```
/plugin install owner-representative --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/agents/owner-representative
