# Provenance — Drawing Reader References

## Primary sources

**US National CAD Standard (NCS) v6**
- Publisher: National Institute of Building Sciences (NIBS), in coordination with AIA + CSI
- Edition: **v6** (current as of 2026-05-08)
- Public information: https://www.nationalcadstandard.org
- Sections referenced:
  - Sheet identification system (discipline designator + sheet-type digit + sheet sequence)
  - Standard discipline designators (G/A/S/M/E/P/L/C/T/Q/F/I)

**AIA G-Series**
- Publisher: American Institute of Architects
- Documents referenced: AIA G707 (Consent of Surety), G704 (Substantial Completion)
- Sheet-list / drawing index conventions

## Coverage of this skill

| Reference file | Covers |
|----------------|--------|
| `drawing-types.md` | Recognition signals for 6 drawing-PDF types (single / set / redline / record / shop / detail) + typical user requests per type |
| `read-patterns.md` | User-intent → handling-pattern mapping; delegation rules to other archtmpl skills (`schedule-extractor`, `drawing-set-bookmarker`, `drawing-checklist`) |

**Out of bundled scope** (refer to authoritative sources):

- **Full NCS v6 specification** — only the discipline + sheet-type system is bundled. Layer / line / hatch conventions are not bundled.
- **DWG / RVT / IFC native conventions** — this skill is PDF-only.
- **Non-NA drawing standards** (BS 1192, ISO 19650, EU CAD conventions) — NA AEC focus only.
- **Spec books, code excerpts, contracts, reports, AHJ correspondence** — non-drawing AEC PDFs are out of scope. A future `doc-reader` may cover those.

## Verification status

- **Last verified against NCS v6 + AIA**: 2026-05-08
- **Update trigger**: When NIBS publishes NCS v7 or AIA revises sheet-list standards.

## How to verify

1. Compare discipline designators in `drawing-types.md` against NCS v6 published guide.
2. If conventions differ, file an issue against `archtmpl`.

## Version pin warning

NCS revisions are infrequent (decade-scale) but always re-verify when:
- A new NCS edition publishes,
- AIA revises its drawing-issuance G-series documents,
- A jurisdiction (e.g. NYC SCA) issues an internal CAD standard amending NCS.

Update the **Last verified** date above on each verification. That date is the record. This line used to name a `Version` and a `Last Verified` property in a Notion database; that database was removed on 2026-07-28 and this file is now the only place the date lives.
