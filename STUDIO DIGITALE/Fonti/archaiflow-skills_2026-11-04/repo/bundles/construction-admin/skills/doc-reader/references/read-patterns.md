# User-Intent → Read-Pattern Mapping

When the user drops a non-drawing AEC PDF and states an intent, this file maps the intent to the right handling — direct vision read or delegation to a specialized archtmpl skill.

> **Format note**: This file is read by Claude after the user has stated their intent. The "Direct read" rows describe what to do inline; the "Delegate to" rows tell Claude to stop and recommend a specialized skill instead.

---

## Section / clause location ("find clause 3.10" / "show me §1006.2")

User asks: "Find AIA A201 §9.8", "Quote IBC §1006.2.1", "What's in CSI 08 14 16 Part 2".

**Direct read**:
1. Inventory the PDF (page count, TOC).
2. Use TOC to locate the requested section.
3. Render that page; quote the requested clause / section verbatim.
4. Cite: page number + native reference (AIA §X.Y.Z, IBC §X.Y.Z, CSI section + Part).
5. Confidence: `high` for verbatim text.

---

## Document summary ("summarize this spec / report")

User asks: "Summarize this spec section", "Give me a 5-bullet rundown of the geotech", "Brief me on this contract".

**Direct read**:
1. Read first 3 pages (cover, TOC, executive summary if present).
2. Sample 1–2 pages from each major section.
3. Output: 3–7 bullet summary covering scope, key findings, key requirements, key recommendations.
4. Cite: page number + section name for each bullet.

---

## Verbatim quote ("quote what the code says")

User asks: "Quote what IBC §1004.5 requires", "What does AIA A201 §3.10 say", "Read me the warranty clause".

**Direct read**:
1. Locate the section (using TOC or page-by-page scan).
2. Quote the section verbatim, with section header + body.
3. Cite: page number + native reference.
4. Confidence: `high`.

**Anti-pattern**: paraphrasing code or contract text. Always verbatim, or flag it.

---

## Numerical extraction ("what's the bearing capacity" / "what's the EUI")

User asks: "What's the soil bearing capacity from the geotech", "Pull the EUI from the energy report", "What's the seismic design category".

**Direct read**:
1. Locate the section containing the value (TOC + targeted scan).
2. Extract the value verbatim with units.
3. Cite: page number + table/figure number.
4. Confidence: `medium` (vision-approximated table cells).
5. Tell the user to verify against the source PDF for legally-binding values.

**Delegate to specialist when applicable**:
- Seismic design parameters → `seismic-design-category-tracker` (when shipped).
- Energy modeling output → may be input to `passive-house-tracker`.
- Code compliance values → may be input to `code-analysis-builder`.

---

## AHJ comment tabulation ("list every plan-check comment")

User asks: "Tabulate the AHJ comments", "What does NYC DOB want", "Make a tracking sheet from this letter".

**Direct read**:
1. Read the letter end-to-end.
2. Identify comments (numbered list or paragraph-by-paragraph).
3. Output a CSV: `comment_id, agency, comment_text, status, action_required, sheet_affected, due_date, source_page`.
4. Cite: page + comment number.
5. Confidence: `high` for verbatim comment text, `medium` for inferred status / sheet-affected.

---

## Scorecard / tracker input ("here's the LEED export, score it")

User pastes / drops a sustainability rating system scorecard export.

**Delegate based on rating system**:
- LEED export → `leed-tracker`.
- PHIUS portal export → `passive-house-tracker`.
- ADA scoping → `ada-tracker`.

Stop. Do not partially score inline.

---

## Spec section → submittal list ("what submittals does this spec require")

User asks: "What submittals does this spec section require", "Pull the Part 1 submittals article".

**Delegate to `submittal-log-builder`**.

If not shipped: do a direct read of Part 1 — Article on Submittals (typically `1.04` or `1.05`) and quote verbatim. Output a CSV: `submittal_id, type (shop drawing / product data / sample / mock-up / closeout), description, response_required (Action / Information), source_clause`.

---

## Plain-English translation ("translate this for the contractor")

User asks: "Make this spec readable for a contractor", "Translate this code section for a client", "Plain-English-ify this contract clause".

**Delegate to `client-translator`**. Stop.

If not installed: `npx archtmpl@latest --skill client-translator`.

---

## Compliance verification ("does this spec meet ADA")

User asks: "Does this spec meet ADA", "Is this contract clause GSA-compliant", "Verify code compliance".

**Out of scope**. The skill quotes; specialized trackers verify. Redirect:
- ADA compliance → `ada-tracker`.
- LEED / WELL / Passive House → corresponding trackers.
- IBC code analysis → `code-analysis-builder`.

---

## Compare versions ("AIA 2007 vs 2017")

User asks: "Compare this contract to the 2007 version", "What changed between IBC 2021 and 2024".

**Out of scope here**. Tell the user to supply BOTH versions; current skill handles one PDF at a time.

---

## Default — unrecognized intent

If the user's intent doesn't match any of the patterns above:

1. Ask the user to clarify what they want.
2. Offer 3 candidate handlings (e.g. "I can: (a) summarize the whole document, (b) quote a specific section, (c) extract key values. Which?").
3. Wait for confirmation before reading.

Never read 500 pages of a spec book without explicit user authorization — vision reads are token-heavy.
