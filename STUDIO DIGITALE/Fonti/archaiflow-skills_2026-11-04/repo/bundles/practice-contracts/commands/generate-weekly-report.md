---
title: Generate Weekly Report
summary: Generate a weekly project status report
discipline: practice-contracts
tags: ["Project Management"]
description: Generate a weekly project status report (Markdown internal / PDF owner-facing, NA conventions)
argument-hint: <project-name-or-week-ending-date>
---

# Generate Weekly Report

Compile a weekly project status report from the user's running notes. Output is Markdown by default for internal team distribution; render to PDF when transmitting to Owner / Owner's Rep.

## Input you need

Before drafting, gather:

- **Project name** and **project number**.
- **Week ending** date in `Month DD, YYYY` (typically Friday).
- **Author** — name, role, firm.
- **Audience** — `Internal` (Markdown) or `Owner` (PDF).
- **This week's accomplishments** — list of completed items.
- **In progress** — list of active items with % complete or status.
- **Blockers / open issues** — items requiring decision, additional info, or escalation.
- **Look-ahead** — items planned for the next 1–2 weeks.
- **Schedule status** — on track, days ahead/behind, critical path notes.
- **Budget status** — current vs. baseline, any flagged variances.
- **Photos** — optional, for owner-facing PDF version.

If any of the above is missing or ambiguous, ask the user before drafting. Do not invent percentages, dates, or budget figures.

## Output structure

```markdown
# Weekly Report — Week Ending [Month DD, YYYY]

**Project:** [Name] (Project No. [######])
**Author:** [Name, Role, Firm]
**Audience:** [Internal / Owner]

---

## Schedule

**Status:** [On track / X days ahead / X days behind]
**Critical path:** [item, target date]
**Notes:** [free text or `None`]

## Budget

**Status:** [On budget / variance summary]
**Notes:** [free text or `None`]

---

## This Week's Accomplishments

- [item]
- [item]
- ...

## In Progress

| Item | Owner | % Complete | Target |
|------|-------|-----------|--------|
| ... | Name, Firm | 60% | YYYY-MM-DD |

## Blockers / Open Issues

| # | Item | Owner | Action needed | By |
|---|------|-------|---------------|-----|
| 1 | ... | Name, Firm | ... | YYYY-MM-DD |

## Look-Ahead (next 1–2 weeks)

- [item]
- [item]

---

**Distribution:** [list]
**Next report:** Week ending [Month DD, YYYY]
```

## NA AEC conventions

- **English only.** No Hangul.
- **Imperial-first** units; metric in parens only.
- **Dates** use `Month DD, YYYY` for cover fields; ISO `YYYY-MM-DD` is acceptable in tables.
- **Roles** — `AOR`, `Owner`, `Owner's Rep`, `CM`, `MEP Engineer`, `SE`, `GC`. Never `Director` as a project role.
- **Firms** — full legal name on first reference.
- **Schedule terms** — `critical path`, `float`, `LOE` (level of effort) — not informal substitutes.
- **Budget terms** — `baseline`, `variance`, `EAC` (estimate at completion) — not "expected".
- **AHJs** when relevant — name specifically (`NYC DOB`, `LADBS`, `DSA`).

## Constraints

- Do not fabricate percentages, dates, or budget figures. If the user reports "about 60%", record it as `~60%` literally.
- Owner-facing PDF version should omit internal candor (interpersonal blockers, billing detail) — if Audience is `Owner`, skip or sanitize accordingly. Confirm with the user if uncertain.
- PDF output requires the `aec-doc-gen` companion skill. If unavailable and Audience=Owner, output Markdown and instruct the user.
- Variance flags (>5% schedule, >3% budget) should be highlighted with bold text and a brief root-cause note.

## Workflow

1. Echo back: project, week ending, audience (Internal/Owner), accomplishments count, blockers count. One line.
2. If any required input is missing, list the gap and stop.
3. Otherwise, produce the full report Markdown.
4. If Audience=Owner and PDF was asked for, hand the Markdown to the `aec-doc-gen` skill and ask it for `.pdf`.
5. After the draft, list any items flagged for follow-up (variance items, missing % values, items without an owner).
