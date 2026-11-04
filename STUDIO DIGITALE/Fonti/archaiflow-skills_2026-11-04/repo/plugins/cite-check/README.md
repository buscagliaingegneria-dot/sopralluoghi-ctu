# Cite Check

Check whether a citation someone gave you is real and current.

Takes a citation somebody handed you — in a review comment, a consultant's report, a contractor's letter, a manufacturer's claim, or your own earlier drawing — and checks the three things that make it usable: does the document exist and in which edition, does the section number resolve inside it, and does the text actually say what it is being used to say. Reports which of the three could be verified and which could not, rather than a yes or a no. Trigger on "is this citation right", "check this code reference", "they quoted a section at us", "does this clause say that", "cite-check", or a section number pasted with a claim attached. Carries no code text: verification comes from the document you supply or from the jurisdiction's own published source, never from recall and never from a search result that is not the publisher. It does not interpret the clause — `explain-code` does — and does not replace the code consultant or the Architect of Record.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **cite-check**.

In Claude Code:

```
/plugin install cite-check --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/cite-check
