# Thread Reader

Read an email or message thread for what was actually decided.

Reads a thread of emails or messages and answers the question that starts most disputes: what did we actually agree. Separates what was decided from what was proposed and never answered, tracks who was on the thread at each point since a decision made after somebody dropped off is a decision they never saw, finds the requests that were never replied to, and flags anything that quietly accepted scope, cost or time. Trigger on "read this thread", "what did we agree on this", "go through this email chain", "did we ever answer this", "thread-reader", or a chain of correspondence handed over. Carries no contract terms; whether something is binding comes from the agreement. `draft-email` writes one message; this reads a chain of them. It does not replace the Architect of Record.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **thread-reader**.

In Claude Code:

```
/plugin install thread-reader --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/thread-reader
