---
title: Create Site Visit Report
summary: Write a field observation report with photos
discipline: construction-admin
tags: ["Construction Admin", "AIA B101"]
description: Create an architect's site visit / field observation report (Word + photos, AIA B101 §3.6.2)
argument-hint: <project-name-or-visit-date>
---

# Create Site Visit Report

Document an architect's site visit per AIA B101 §3.6.2 — observations of work in progress, conformance with contract documents, photos, and any issues raised. Output is Markdown that renders to Word (.docx) so photos embed and the AOR can sign.

## Input you need

Before drafting, gather:

- **Project name** and **project number**.
- **Date** of visit in `Month DD, YYYY`.
- **Time** on site (arrival → departure, with zone).
- **Weather** — temperature (°F), conditions, precipitation, wind.
- **Author** — AOR representative on site (name, role, firm).
- **Other attendees** — Owner, CM, GC, subs, consultants (name, firm).
- **Areas observed** — specific locations / floors / scopes (e.g., `Level 3 east wing — drywall and MEP rough`).
- **Observations** — what was seen. For each: location, description, photo references (optional), conformance status (`Conforming` / `Non-conforming` / `Observation only`), spec/drawing reference if applicable.
- **Action items** — issues raised, owner, due date.
- **Photos** — file paths or descriptions; will embed in Word output.

If any of the above is missing or ambiguous, ask the user before drafting. Do not invent observations, dimensions, or attendees.

## Output structure

```markdown
# Site Visit Report

**Project:** [Name] (Project No. [######])
**Date:** [Month DD, YYYY]
**Time on site:** [HH:MM AM/PM ET → HH:MM AM/PM ET]
**Weather:** [°F, conditions]
**Visit by:** [AOR rep name, role, firm]
**Per:** AIA B101 §3.6.2

---

## Attendees

| Name | Firm | Role |
|------|------|------|
| ... | ... | ... |

## Areas Observed

- [Level / scope / location 1]
- [Level / scope / location 2]

---

## Observations

### Obs. 1 — [Location]

**Description:** [what was seen]
**Conformance:** [Conforming / Non-conforming / Observation only]
**Reference:** [drawing / spec section, or `—`]
**Photo:** [filename or description, or `—`]

### Obs. 2 — [Location]

...

---

## Action Items

| # | Item | Owner | Due | Status |
|---|------|-------|-----|--------|
| 1 | ... | Name, Firm | YYYY-MM-DD | Open |

---

## Authorization Limit (AIA B101 §3.6.2.1)

The architect's site visits do not constitute exhaustive or continuous on-site inspection. Observations are limited to general conformance with the contract documents. The architect is not responsible for the contractor's means, methods, sequences, procedures, or for safety precautions in connection with the work.

---

**Signed:** [AOR PIC]
**Date:** [Month DD, YYYY]
```

## NA AEC conventions

- **English only.** No Hangul.
- **Imperial-first** units (`ft`, `in`, `sf`, `°F`); metric in parens only.
- **Dates** use `Month DD, YYYY` in cover; ISO `YYYY-MM-DD` acceptable in tables.
- **Time zones** explicit (`ET / CT / MT / PT`).
- **Roles** — `AOR`, `Owner`, `CM`, `GC`, `MEP Engineer`, `SE`, sub-trades by trade name (`Drywaller`, `Steel erector`). Never `Director` as a project role.
- **AIA reference** — `AIA B101 §3.6.2` (site visits), `§3.6.2.1` (limitation of architect's responsibility).
- **AHJs** — name specifically when observations implicate code interpretation (`NYC DOB`, `LADBS`, `DSA`, `FDNY`).
- **Floor labels** — `Level 3` / `L3` / `3rd floor`. Never `3F`.
- **Conformance terms** — use `Conforming`, `Non-conforming`, `Observation only` literally; do not paraphrase.

## Constraints

- Do not fabricate observations, dimensions, or attendees. If the user provides a one-line summary, surface gaps as questions rather than embellishing.
- The B101 §3.6.2.1 authorization-limit boilerplate must remain verbatim — it is the contractual scope of the architect's site presence and removing it expands liability.
- Photos: in Markdown, reference by filename or description; in Word output, `aec-doc-gen` embeds the image if a path is provided.
- Word output requires the `aec-doc-gen` companion skill. If unavailable, output Markdown and instruct the user.
- Non-conforming observations should reference the specific drawing or spec being violated, or be downgraded to `Observation only`.

## Workflow

1. Echo back: project, visit date, areas observed count, observations count, non-conforming count. One line.
2. If any required input is missing, list the gap and stop.
3. Otherwise, produce the full report Markdown.
4. If Word output was asked for, hand the Markdown to the `aec-doc-gen` skill and ask it for `.docx`, passing any photo paths so they are embedded rather than named.
5. After the draft, list items flagged for follow-up (TBD owners, photo references missing, non-conforming items without spec citation).
