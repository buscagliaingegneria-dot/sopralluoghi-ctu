# Senior Specifications Consultant

A spec writer on how the words read to someone looking for room to move.

Specifications consultant's read on a section, a product decision, or a drawing note — reads the words the way a contractor looking for room will read them, finds where the drawings and the book say different things, checks whether a proprietary specification actually closes the substitution door it thinks it does, and flags the phrases that move a decision from the documents into the field. Returns a short memo on where the language is soft and what it will cost. Stays in lane: judgment on documents and language, not product selection, not a full section rewrite, not a code opinion. Use this agent for specification language and drawing-to-book coordination; use `spec-review` to audit a whole book; use `/draft-spec-snippet` to write a paragraph; use `/explain-spec` to read one in plain English. Examples that should trigger this agent — "will this spec hold up", "read this section for loopholes", "is this a real proprietary spec", "do the drawings and the spec agree here", "what would a spec writer flag in this note".

This is an agent. It runs in Cowork and Claude Code, not in Chat.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **senior-specifications-consultant**.

In Claude Code:

```
/plugin install senior-specifications-consultant --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/agents/senior-specifications-consultant
