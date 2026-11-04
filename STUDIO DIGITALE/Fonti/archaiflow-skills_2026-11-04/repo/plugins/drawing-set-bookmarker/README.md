# Drawing Bookmarks

Bookmark a flat drawing-set PDF and index its sheets.

This skill should be used when the user has a multi-sheet architectural drawing-set PDF (typically 50–300 sheets) with no bookmarks or a flat/incorrect bookmark tree, and wants a properly bookmarked PDF plus a CSV sheet index. Trigger on "bookmark this drawing set", "add bookmarks to this PDF", "tabulate sheets", "make a sheet index", or a pasted path to a multi-sheet drawing PDF. Reads each page's title block via vision, extracts sheet number/name/discipline, groups by discipline per US National CAD Standard, and writes the bookmarked PDF + index to `docs/drawing-sets/`.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **drawing-set-bookmarker**.

In Claude Code:

```
/plugin install drawing-set-bookmarker --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/drawing-set-bookmarker
