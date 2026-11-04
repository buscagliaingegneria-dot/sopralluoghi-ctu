# Adjacency Matrix

Build the matrix from who actually moves, not from who says they are close.

Builds a programme adjacency matrix from movement and constraint rather than from stated preference: takes the room list, asks for each pair what actually travels between them and how often, separates a required adjacency from a desired one and from a required separation, then reads the finished matrix for the rooms that want to be everywhere at once and the conflicts that no plan can satisfy. Trigger on "adjacency matrix", "bubble diagram", "which rooms need to be near each other", "programme relationships", "adjacency-matrix", or a room list handed over with a request for how it should be organised. Carries no adjacency conventions for any building type, because who has to be near whom is the client's operation and not a rule. Reads a room list from `space-program` where one exists and does not duplicate its area tracking. It does not lay out a plan and does not replace the Architect of Record.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **adjacency-matrix**.

In Claude Code:

```
/plugin install adjacency-matrix --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/adjacency-matrix
