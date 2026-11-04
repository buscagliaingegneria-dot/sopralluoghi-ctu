# Markup Reader

Read a marked-up drawing and turn it into a list somebody can act on.

Reads a marked-up drawing — a redline, a scanned sketch over a print, a PDF with comments, a photograph of a drawing somebody wrote on — and turns it into a numbered list of what each mark asks for, who it is for, and whether it can be acted on as drawn. Separates the marks that instruct from the marks that ask, and flags every mark whose meaning cannot be determined, because a guessed markup is worse than an unread one. Trigger on "read this redline", "they marked up the drawing", "what does this markup say", "turn these comments into a list", "markup-reader", or a marked drawing handed over. Carries no conventions: what a colour or a symbol means is the office's or the marker's, and it is asked rather than assumed. `drawing-diff` compares two issued revisions; this reads what somebody wrote on one. It does not replace the Architect of Record.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **markup-reader**.

In Claude Code:

```
/plugin install markup-reader --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/markup-reader
