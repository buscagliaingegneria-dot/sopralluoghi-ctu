# Option Compare

Build a side-by-side comparison of design options for a decision.

Builds a side-by-side comparison of design options in docs/design/options.md: the criteria you choose, one column per scheme, every cell filled from what you supply, and a tradeoff summary that stops short of picking the winner. Trigger on "compare options", "option A or B", "scheme comparison", "comparison matrix", "which scheme", "options for the client", "option-compare", or pasted facts about two or more schemes. Areas can be read from a space-program file where one exists, costs arrive from you or a cited benchmark, and empty cells stay visibly empty rather than estimated. Weighted scoring runs only if you supply the weights, arithmetic shown. The decision is the client's and yours; the skill structures it and does not make it. Renders to Word or PDF through aec-doc-gen when the meeting needs a handout.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **option-compare**.

In Claude Code:

```
/plugin install option-compare --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/option-compare
