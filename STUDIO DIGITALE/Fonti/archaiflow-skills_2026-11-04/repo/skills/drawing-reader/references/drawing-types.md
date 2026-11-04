# Drawing-PDF Types — Recognition Signals

Six types of drawing PDFs commonly hit the architect's inbox in NA AEC practice. Each has distinct visual signals and triggers different reading patterns.

> **Format note**: This file is read by Claude when the user drops a drawing PDF. The "Recognition signals" rows are the first-pass clues; the "Typical user requests" rows tell Claude what users normally want from each type.

---

## 1. Single sheet

A single drawing on a single page (or 1–3 pages if multi-page assembly drawing).

**Recognition signals**:
- Page count: 1–3.
- Page size: typically ANSI D (24×36 in.), ANSI E (36×48 in.), or 11×17 (half-size).
- Titleblock present in bottom-right or full-bottom strip with sheet number (e.g. `A-301`).
- Single drawing (plan, section, elevation, detail, schedule) fills the page.

**Typical user requests**:
- "Summarize this sheet."
- "What sheet number is this?"
- "Explain this detail."
- "What's the scale?"
- "Read the general notes on this sheet."

**Default handling**: direct vision read. No delegation.

---

## 2. Multi-sheet set

A complete drawing set — all disciplines for an issue (DD, CD, addendum, permit set).

**Recognition signals**:
- Page count: 10+ (typical sets are 50–300 sheets).
- NCS-style titleblock on every page.
- First page is a cover sheet (sheet `G-001` or similar) with sheet index.
- Multiple disciplines visible — sheet numbers like `A-101`, `S-201`, `M-301`, `E-401`.
- Issue date / revision block on every sheet.

**Typical user requests**:
- "Summarize this set."
- "What disciplines are in this set?"
- "Show me sheet A-301."
- "Tabulate the sheet list."
- "What's the egress plan?" / "Where's the wall section?"
- "Pull all the schedules."
- "Bookmark this set."

**Default handling**:
- Sheet-list / tabulation requests → delegate to `drawing-set-bookmarker`.
- Schedule extraction → delegate to `schedule-extractor`.
- QA / completeness → delegate to `drawing-checklist`.
- Topical search ("show me egress") → direct vision read with sheet-list inventory.

---

## 3. Redline markup

A drawing page (or set) with overlay markup — cloud + comment bubbles, redline strikethroughs, callout-with-arrow comments.

**Recognition signals**:
- Visible cloud-shape outlines (often red or pink) over portions of the drawing.
- Inline text comments in tooltip-style bubbles or annotation-style frames.
- Author signature / initials in titleblock or markup margin (e.g. "JL 2026-04-15").
- Line weight / color contrast between original drawing (printed) and markup (overlay).
- Often produced by Bluebeam, Adobe Acrobat, or AHJ plan-check PDF.

**Typical user requests**:
- "What does this AHJ redline say?"
- "Tabulate the comments."
- "Which sheets have markups?"
- "Pair each comment with the drawing area."

**Default handling**: direct vision read. Iterate page-by-page extracting the comment + the drawing area it points to. Output a CSV of `comment_id, sheet, location, comment_text, source`.

---

## 4. Record drawing / as-built

A drawing showing the as-installed condition, prepared by contractor or architect at project closeout.

**Recognition signals**:
- "RECORD DRAWING" or "AS-BUILT" stamp on titleblock.
- Revision clouds + small text notes calling out field changes.
- Sometimes a "Record Drawing Set" cover sheet (e.g. `G-002 Record`).
- Contractor stamp / initials on each modified sheet.

**Typical user requests**:
- "Summarize the field changes."
- "Compare to the original CD set" — out of scope here; redirect to `issue-set-comparison` when shipped.
- "Tabulate the as-built revisions per sheet."

**Default handling**: direct vision read. Tabulate revision clouds per sheet with brief description.

---

## 5. Shop drawing

A fabricator's drawing showing the means + methods for a specific assembly (steel, curtain wall, casework, etc.).

**Recognition signals**:
- "SHOP DRAWING" titleblock.
- Fabricator company logo / branding (not the architect's).
- Page size often 11×17 or 22×34 (one-quarter or half scale of CD format).
- Submittal stamp area (e.g. "Reviewed", "Reviewed as Noted", "Revise + Resubmit", "Rejected") for AOR markup.
- Heavy use of part numbers, fabrication tolerances, weld symbols, hardware schedules.

**Typical user requests**:
- "Summarize this shop drawing."
- "What's the scope of this submittal?"
- "Find the fabrication schedule."
- "Verify it matches CD sheet A-501 detail 3" — direct vision compare.

**Default handling**: direct vision read. Note: shop drawings reference contract drawings (CDs) — flag any discrepancy for AOR review, do not approve.

---

## 6. Detail page

A single drawing detail (wall section, column base, parapet, sill, etc.) extracted from a larger set or from a standard-detail library.

**Recognition signals**:
- Single-page PDF with one drawing.
- Titleblock smaller / abbreviated (or absent).
- Detail callout marker present (e.g. `3/A-501` indicating "detail 3, sheet A-501").
- Often pulled from manufacturer's standard-detail library or office detail library.

**Typical user requests**:
- "Explain this detail."
- "What materials are shown?"
- "What scale?"
- "Find the source — what sheet does it come from?"

**Default handling**: direct vision read. Identify components, callouts, materials, dimensions (with confidence caveat).

---

## Coverage and out-of-scope

This file covers:

- The 6 most common drawing-PDF types in NA AEC practice.
- Recognition signals + typical user requests per type.

This file does NOT cover:

- **Specification books, code excerpts, contracts, reports, AHJ letters** — non-drawing AEC PDFs.
- **DWG / RVT / IFC native files** — drawing PDFs only.
- **Hand sketches** — out of scope; while a hand sketch can be vision-read, it does not follow NCS or any titleblock convention, so the recognition signals here don't apply.
- **Foreign drawing standards** (BS, EU, JIS) — NA AEC focus only.

For drawing types not listed (e.g. boring log, coastal flood map, geotech profile), default to "single sheet" handling and ask the user for context.
