# Non-Drawing AEC Document Types — Recognition Signals

Five types of non-drawing AEC document PDFs commonly hit the architect's inbox in NA practice. Each has distinct visual signals and triggers different reading patterns.

> **Format note**: This file is read by Claude when the user drops a non-drawing AEC PDF. The "Recognition signals" rows are the first-pass clues; the "Typical user requests" rows tell Claude what users normally want from each type.

---

## 1. Specification (CSI section)

A spec section formatted per CSI MasterFormat 2020.

**Recognition signals**:
- Page header / footer with **6-digit MasterFormat number** (e.g. `08 14 16` Wood Doors, `09 91 23` Interior Painting).
- 3-part organization: **Part 1 — General**, **Part 2 — Products**, **Part 3 — Execution**.
- Numbered articles within each part (`1.01 SUMMARY`, `1.02 RELATED REQUIREMENTS`, etc.).
- Page count: typically 3–15 pages per section. A full spec book is 100–500+ pages.
- Specifier signature block / project info on first page.
- May reference CSI SectionFormat™ structure.

**Typical user requests**:
- "Summarize this spec section."
- "What products are listed in Part 2?"
- "What's in the Submittals article?"
- "Find the warranty requirements."
- "List the related sections referenced."
- "Translate this for a contractor" → delegate to `client-translator`.

**Default handling**: direct vision read. For full spec books (100+ pages), confirm scope with user — tell them to point to specific section number or topic.

---

## 2. Code excerpt

A chapter, section, or subset of a building code (IBC, IRC, IECC, NFPA, ADA, ICC A117.1, ASCE 7).

**Recognition signals**:
- Chapter header (e.g. `Chapter 10 — Means of Egress`, `Chapter 7 — Fire and Smoke Protection Features`).
- Hierarchical numbering: §X.Y.Z (e.g. `1006.2.1 Spaces with one exit or exit access doorway`).
- Code edition / year on cover or page footer (e.g. `2024 International Building Code`).
- ICC Digital Codes watermark / footer pattern.
- Tables with sequence numbers (e.g. `TABLE 1006.3.3(2) STORIES WITH ONE EXIT...`).
- Strict section/subsection cross-references ("see §1004").

**Typical user requests**:
- "What does §1006 say about egress?"
- "Quote the table for stories with one exit."
- "What's the requirement for a Group A-3 occupancy?"
- "Find every reference to `automatic sprinkler system`."
- "Compare 2024 to 2021 edition" → out of scope here; user must supply both editions.

**Default handling**: direct vision read with strict §X.Y.Z citations. Verbatim quote rule applies — never paraphrase code text without flagging it.

---

## 3. AIA contract

An AIA Contract Document — owner-architect agreement, general conditions, consultant agreement, or administrative form.

**Recognition signals**:
- AIA logo on title page.
- Document code (e.g. `AIA Document B101™ – 2017`, `AIA Document A201™ – 2017`, `AIA Document G704™ – 2017`).
- Owner / Architect / Contractor signature blocks at end.
- Standardized article structure (e.g. A201 has 15 articles; B101 has 11 articles).
- Footer text "AIA Document <code> – <year>. Copyright © …"
- Often customized in §X.Y for project-specific terms, with edits tracked in tracked-changes mode.

**Typical user requests**:
- "Find clause 3.10 in the contract."
- "What does the contract say about substantial completion?"
- "What are the architect's basic services?"
- "Quote A201 §9.8 (Substantial Completion)."
- "List the additional services in Article 4."

**Default handling**: direct vision read with AIA section + paragraph citations. Verbatim quote rule applies — contracts are legally binding text.

---

## 4. Report

A consultant or in-house technical report — geotech, structural calc, energy modeling output, daylight study, acoustic study, environmental site assessment, mechanical study, traffic study, etc.

**Recognition signals**:
- Cover page: project name, report title (e.g. "Geotechnical Investigation Report", "Energy Modeling Summary"), preparer firm logo, date, project number.
- Table of contents on page 2 or 3.
- Section structure: typically Executive Summary → Scope / Methodology → Findings → Recommendations → Appendices.
- Tables and figures with consultant-signed boring logs / load calculations / energy bins / chart outputs.
- Often has consultant's PE / GE / LEED-AP credentials in signature block.

**Typical user requests**:
- "Summarize this geotech report."
- "What's the soil bearing capacity?"
- "Pull the recommended foundation type."
- "What's the building's projected EUI?"
- "Extract the seismic design parameters" → may delegate to `seismic-design-category-tracker` (when shipped).

**Default handling**: direct vision read. Reports vary widely in format — read TOC first, then jump to user-requested section. Numerical extractions require `medium` confidence flag (vision-approximated for tables).

---

## 5. AHJ correspondence

A letter or PDF from an Authority Having Jurisdiction — plan-check comment letter, NOTC (Notice of Completion / Final Construction), permit conditions, or RFI response from agency.

**Recognition signals**:
- Agency letterhead: NYC DOB, FDNY, NYC SCA, CA HCAI, DSA, GSA, USACE, FEMA region, state DEP/DEC, local building department.
- Often numbered comment list (e.g. `Comment 1: …`, `Comment 2: …`) with `Status: Open / Closed / Resolved` per comment.
- Reference to plan-check submission number, BIN (NYC), permit application #.
- AHJ examiner / plan reviewer signature + license #.
- May include "Action Required" column or numbered response template.

**Typical user requests**:
- "What does the AHJ want me to fix?"
- "Tabulate the plan-check comments."
- "List unresolved comments."
- "What did NYC DOB say about egress?"
- "Pair each comment with the affected sheet."

**Default handling**: direct vision read. Output a comment-tracking CSV: `comment_id, agency, comment_text, status, action_required, sheet_affected, due_date, source_page`.

---

## Coverage and out-of-scope

This file covers:

- The 5 most common non-drawing AEC PDF types in NA practice.
- Recognition signals + typical user requests per type.

This file does NOT cover:

- **Drawing PDFs** — use `drawing-reader`.
- **DWG / RVT / IFC native files** — PDF-only.
- **Scorecard exports** (LEED scorecard, WELL scorecard, PHIUS portal export) — these are tracker inputs, not standalone reads. Use the relevant tracker.
- **Hand sketches / non-formatted notes** — out of scope; readable but no recognition pattern applies.
- **Foreign / non-NA standards** (BS, EU, JIS, KS) — NA AEC focus only.

For doc types not listed (e.g. RFP / proposal, owner program, marketing brochure), default to "report" handling and ask the user for context.
