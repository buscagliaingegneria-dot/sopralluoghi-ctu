# Cost Reader

Read any cost document for what it excludes and what it assumed.

Reads any document with money in it — an estimate, a budget, a cost plan, a supplier quote, a contractor's proposal, a client's own number — and does the part an architect can do without being an estimator: establish what it covers, what it excludes, what it assumed, and what date it is on. Those four decide almost every argument about a price, and none of them require checking the arithmetic. Trigger on "read this estimate", "what does this quote actually include", "the budget came back", "is this number comparable", "cost-reader", or any priced document handed over. Carries no rates, no benchmarks and no cost data; `/lookup-cost` quotes a benchmark with its source and `senior-cost-estimator` gives judgement. It checks no arithmetic, prices nothing, and does not replace the estimator, the contractor, or the Architect of Record.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **cost-reader**.

In Claude Code:

```
/plugin install cost-reader --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/cost-reader
