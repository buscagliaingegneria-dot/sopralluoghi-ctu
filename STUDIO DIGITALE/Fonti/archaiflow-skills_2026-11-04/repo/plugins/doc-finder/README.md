# Project Search

Find an answer in your own files, with a citation.

Source-grounded research agent. Searches user-provided paths and workspace files (grep/glob), reads PDFs, and refuses to fabricate. Cites file:page or file:line for every claim. Returns "not found in provided sources" when the answer is not in scope rather than falling back to general knowledge or the web. Examples that should trigger this agent — "find what this PDF says about X", "search the project files for Y", "what does the attached spec say about Z", "look up the citation for X in these documents", "find every place in the workspace that mentions Y".

This is an agent. It runs in Cowork and Claude Code, not in Chat.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **doc-finder**.

In Claude Code:

```
/plugin install doc-finder --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/agents/doc-finder
