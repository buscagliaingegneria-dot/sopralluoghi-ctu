# Code Analysis Reader

Read somebody else's code analysis for what it assumed and never showed.

Reads a code analysis produced by somebody else — a previous architect, a code consultant, a design-build partner, an earlier phase of your own project — and separates its three layers: the determinations it made, the arithmetic it showed, and the conclusions it stated without either. A code analysis is a chain of decisions and the first link, the occupancy classification, silently sets everything after it. Trigger on "read this code analysis", "we inherited a code summary", "is this code sheet still right", "the consultant sent their analysis", "code-analysis-reader", or a code analysis handed over. Carries no code text and no limits; every figure in it is checked for whether it was cited, not for whether it is correct. `code-analysis-builder` assembles your own; this reads one you were given. It does not verify compliance and does not replace the code consultant or the Architect of Record.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **code-analysis-reader**.

In Claude Code:

```
/plugin install code-analysis-reader --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/code-analysis-reader
