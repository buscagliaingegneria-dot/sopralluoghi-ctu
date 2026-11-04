---
title: Create Transmittal
summary: Make a cover sheet for a document package
discipline: construction-admin
tags: ["Project Management"]
description: Create a transmittal cover sheet for AEC document distribution (PDF default, NA conventions)
argument-hint: <recipient-or-package-name>
---

# Create Transmittal

Create a transmittal cover sheet listing documents being sent to a project party (Owner, GC, consultant, AHJ). Output is Markdown ready to render to PDF for email attachment or signed hard-copy distribution.

## Input you need

Before drafting, gather:

- **Project name** and **project number**.
- **Date** in `Month DD, YYYY`.
- **From** — sender (name, role, firm).
- **To** — recipient (name, role, firm); add **Cc** distribution if relevant.
- **Transmittal number** — sequential project log number (e.g., `T-014`).
- **Items** — each with: number, title, sheet/spec reference, revision, date, copies.
- **Purpose** — one of: `For Review`, `For Approval`, `For Construction`, `For Bidding`, `For Permit`, `For Your Files`, `As Requested`.
- **Method of delivery** — `Email (PDF)`, `Courier`, `In person`, `FTP / shared drive`, `Procore` / `BIM 360` / `Newforma`.
- **Notes** — optional, e.g., "supersedes Bulletin #3" or "AHJ stamp required".

If any of the above is missing or ambiguous, ask the user before drafting. Do not invent drawing numbers, revisions, or recipients.

## Output structure

```markdown
# Transmittal — T-XXX

**Project:** [Name] (Project No. [######])
**Date:** [Month DD, YYYY]
**Transmittal No.:** T-XXX
**From:** [Name, Role, Firm]
**To:** [Name, Role, Firm]
**Cc:** [list, or `None`]
**Method:** [Email (PDF) / Courier / etc.]
**Purpose:** [For Review / For Approval / For Construction / etc.]

---

## Items Transmitted

| # | Title | Reference | Rev | Date | Copies |
|---|-------|-----------|-----|------|--------|
| 1 | Architectural Plans | A-001 — A-401 | 3 | 2026-05-09 | 1 set |
| 2 | Specifications | Vol. 1, Div. 00–14 | 3 | 2026-05-09 | 1 ea. |

## Notes

[Free-text notes, or `None`.]

---

**Issued by:** [Name, Title, Firm]
**Signature:** ______________________________
**Date received:** ______________________ (recipient to fill)
```

## NA AEC conventions

- **English only.** No Hangul.
- **Imperial-first** units; metric in parens only.
- **Dates** use `Month DD, YYYY`.
- **Roles** — `AOR`, `Owner`, `CM`, `MEP Engineer`, `SE`, `GC`. Never `Director` as a project role.
- **Firms** — full legal name on first reference.
- **AIA reference** — `AIA B101 §3.6.4` (architect's submittal review obligation when the transmittal is from contractor).
- **AHJs** — name specifically when transmitting permit / approval documents (`NYC DOB`, `FDNY`, `LADBS`, `DSA`, `CA HCAI`, `NYC SCA`).
- **Date format on items** — ISO `YYYY-MM-DD` is acceptable in tables for compactness; cover-sheet `Date:` field stays `Month DD, YYYY`.

## Constraints

- Do not fabricate drawing numbers, revisions, or copy counts. If the user lists items by name only, ask for sheet/spec references and revs.
- The `Purpose` field is required and must be one of the canonical values listed in *Input you need*. Free-text purposes invite contract disputes.
- PDF output requires the `aec-doc-gen` companion skill. If unavailable, output Markdown and instruct the user.
- The signature block at the bottom must remain (it documents acknowledgement of receipt).

## Workflow

1. Echo back: project, transmittal number, recipient, item count, purpose. One line.
2. If any required input is missing, list the gap and stop.
3. Otherwise, produce the full Transmittal Markdown.
4. If PDF output was asked for, hand the Markdown to the `aec-doc-gen` skill and ask it for `.pdf`. Surface the output path.
5. After the draft, remind the user to log the transmittal in the project's transmittal log (number must be unique).
