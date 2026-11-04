# User-Intent → Read-Pattern Mapping

When the user drops a drawing PDF and states an intent, this file maps the intent to the right handling — either direct vision read or delegation to a specialized archtmpl skill.

> **Format note**: This file is read by Claude after the user has stated their intent. The "Direct read" rows describe what to do inline; the "Delegate to" rows tell Claude to stop and recommend a specialized skill instead of doing the work here.

---

## Sheet location ("show me sheet X")

User asks: "Show me sheet A-301", "where's the egress plan", "find the door schedule sheet".

**Direct read**:
1. Inventory the PDF (page count, first-page sheet identifier).
2. Iterate page-by-page reading just the titleblock until the requested sheet is found.
3. Render that page; output a 3–5 sentence summary of the sheet's content.
4. Cite: page number + sheet number.

**Stop signals**: if 3 passes through the document don't find the sheet, tell the user the sheet isn't in this PDF.

---

## Set summary ("summarize this set")

User asks: "Summarize this set", "what's in this PDF", "give me an overview".

**Direct read**:
1. Read the cover sheet (page 1) for sheet index + project info.
2. Sample 3–5 pages across disciplines to confirm content.
3. Output: project name, set issue date, sheet count, disciplines present, key sheets per discipline.

**Delegate to `drawing-set-bookmarker`** if the user wants a *tabulated* sheet list (CSV index + bookmarked PDF).

---

## Single-sheet summary ("what's on this sheet")

User asks: "What's on sheet X", "summarize this sheet", "explain this drawing".

**Direct read**:
1. Read the entire single page.
2. Output: sheet number + title, scale(s), key drawings (plan + sections + details), general notes presence/absence, schedule presence.
3. Cite: page number + every callout / note quoted.

---

## Detail explanation ("explain this detail")

User asks: "Explain this detail", "what materials", "what's this construction".

**Direct read**:
1. Read the single detail.
2. Identify: assembly type (e.g. wall section, parapet, sill), components (with material name verbatim from the drawing), callouts referenced (sheet/detail #), key dimensions (with `low` confidence — vision is approximate).
3. Cite: every component callout's exact text from the drawing.

**Caveat**: explicitly tell the user dimensions are vision-approximated and to verify against the source PDF for any dimension that matters.

---

## Schedule extraction ("get the door schedule")

User asks: "Extract the door schedule", "give me the finish schedule as CSV", "pull the equipment schedule".

**Delegate to `schedule-extractor`**. Stop. Do not partially do the extraction inline.

If `schedule-extractor` is not installed: `npx archtmpl@latest --skill schedule-extractor`.

---

## Set tabulation / bookmarking ("bookmark this set")

User asks: "Bookmark this set", "make a sheet index from this PDF", "tabulate every sheet".

**Delegate to `drawing-set-bookmarker`**. Stop.

If not installed: `npx archtmpl@latest --skill drawing-set-bookmarker`.

---

## QA / completeness ("review this DD set")

User asks: "QA this set", "DD checklist on this", "what's missing from CD".

**Delegate to `drawing-checklist`**. Stop.

If not installed: `npx archtmpl@latest --skill drawing-checklist`.

---

## Code analysis ("what's the code analysis")

User asks: "Pull the code analysis from this set", "what occupancy / construction type / allowable area".

**Read** the cover sheet code-analysis block (typically `G-001` or `G-002`) and quote it verbatim.

If the user wants the code analysis *built from scratch* from program data, **delegate to `code-analysis-builder`**.

---

## Egress / fire / accessibility ("show me the egress")

User asks: "Show me the egress plan", "where are the fire-rated walls", "is this accessible".

**Direct read**:
1. Locate the relevant code-analysis sheet (`G-001` / `G-002` / `LS-101` for life safety).
2. Read the legend + plan diagrams.
3. Output: the egress strategy (number of stairs, travel distance, common path), fire-rated wall locations, accessibility provisions — with sheet+page citations.
4. Confidence: `medium` for plan diagrams (vision-read), `high` for verbatim notes / legend.

**Caveat**: tell the user this is a structural read, not a code-compliance verification. For compliance checking, use `ada-tracker`, `code-analysis-builder`, etc.

---

## Markup / redline aggregation ("what does this redline say")

User asks: "Tabulate the redline comments", "what does the AHJ want", "list every comment".

**Direct read**:
1. Iterate page-by-page identifying comment bubbles + cloud locations.
2. Output a CSV: `comment_id, sheet, location, comment_text, raised_by, action_required`.
3. Confidence: `high` for verbatim comment text, `medium` for inferred location.

---

## Compare versions ("addendum 1 vs addendum 2")

User asks: "Compare these two sets", "what changed in addendum 2", "diff this CD set".

**Out of scope here**. Redirect to `issue-set-comparison` when shipped, or tell the user to do a manual sheet-by-sheet read for now.

---

## Default — unrecognized intent

If the user's intent doesn't match any of the patterns above:

1. Ask the user to clarify what they want.
2. Offer 3 candidate handlings (e.g. "I can: (a) summarize the whole set, (b) find a specific sheet, (c) extract a schedule. Which?").
3. Wait for confirmation before reading.

Never read 200 pages of a set without explicit user authorization — vision reads are token-heavy.
