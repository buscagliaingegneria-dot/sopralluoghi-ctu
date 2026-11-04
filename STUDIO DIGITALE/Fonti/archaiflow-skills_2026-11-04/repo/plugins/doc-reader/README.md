# Doc Reader

Read and interpret a specification, report, or contract PDF.

Reads a non-drawing project PDF and answers questions about it: a specification, a code excerpt, a contract, a consultant report, or correspondence from an authority. Summarises, locates a clause, extracts values, or lists comments, and cites section and page for every claim it makes. Trigger on "read this spec", "what does this document say", "summarize this report", "find clause X", "what is the authority asking for", or a pasted path to a non-drawing project PDF. For drawing sheets use drawing-reader instead. Detects the document type, asks what is wanted before reading at length, and never answers from what a document of that kind usually says. Writes a per-read summary that points back at the source.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **doc-reader**.

In Claude Code:

```
/plugin install doc-reader --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/doc-reader
