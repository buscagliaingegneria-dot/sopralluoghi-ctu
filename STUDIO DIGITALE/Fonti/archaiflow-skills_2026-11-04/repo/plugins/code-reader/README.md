# Code Reader

Turn a code section into the requirements it actually contains.

Takes a code section, a standard, or an ordinance you paste and pulls it apart into the separate requirements inside it: what each one applies to, what it demands, what triggers it, what exempts it, and which other section it hands off to. A single paragraph routinely contains four requirements and two exceptions, and reading it as one sentence is how half of it gets missed. Trigger on "read this code section", "what does this clause actually require", "pull the requirements out of this", "code-reader", or a pasted section that has to be worked through. Carries no code text and recalls no section: everything comes from what you paste or from the jurisdiction's own published source. `explain-code` puts one clause in plain English; this takes the clause apart into a table you can check a design against. It does not check the design — `compliance-check` does — and does not replace the code consultant or the Architect of Record.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **code-reader**.

In Claude Code:

```
/plugin install code-reader --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/code-reader
