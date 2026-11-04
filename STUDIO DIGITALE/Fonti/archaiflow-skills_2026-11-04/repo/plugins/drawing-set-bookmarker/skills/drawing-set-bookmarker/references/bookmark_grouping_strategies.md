# Bookmark Grouping Strategies

The bookmark tree is the navigation contract for the bookmarked PDF. The tree's top level should match how the user expects to look up a sheet. There are three workable strategies; the default is **discipline-grouped**.

## Strategy 1: Discipline-grouped (DEFAULT)

Top level groups sheets by US NCS Level-1 discipline letter. Within each discipline, sheets are sorted by sheet number (sheet-type digit ascending, then sequence).

```
General (G)
  ├── G-001 — COVER SHEET
  ├── G-002 — DRAWING INDEX
  └── G-003 — ABBREVIATIONS & SYMBOLS
Architectural (A)
  ├── A-001 — GENERAL NOTES
  ├── A-101 — FIRST FLOOR PLAN
  ├── A-102 — SECOND FLOOR PLAN
  ├── A-201 — NORTH ELEVATION
  ├── A-301 — BUILDING SECTION A
  └── A-501 — WALL DETAILS
Structural (S)
  ├── S-001 — GENERAL NOTES
  ├── S-101 — FOUNDATION PLAN
  └── ...
Mechanical (M)
  └── ...
```

When to use: **always, unless the user explicitly asks otherwise**. This is what every NA office expects when opening a CD set in Bluebeam or Adobe.

## Strategy 2: Sheet-type-grouped

Top level groups by sheet-type digit (Plans / Elevations / Sections / Details / Schedules), with discipline as a sub-group.

```
Plans (1)
  ├── A-101 — FIRST FLOOR PLAN
  ├── A-102 — SECOND FLOOR PLAN
  ├── S-101 — FOUNDATION PLAN
  └── M-101 — FIRST FLOOR MECH PLAN
Elevations (2)
  ├── A-201 — NORTH ELEVATION
  └── A-202 — SOUTH ELEVATION
Sections (3)
  ├── A-301 — BUILDING SECTION A
  └── ...
```

When to use: QC review, where the reviewer wants to compare all plans across disciplines side-by-side, or all sections together. Less natural for daily lookup.

## Strategy 3: Flat-by-number

No grouping — every sheet is a top-level bookmark in sheet-number order.

```
G-001 — COVER SHEET
A-001 — GENERAL NOTES
A-101 — FIRST FLOOR PLAN
A-102 — SECOND FLOOR PLAN
A-201 — NORTH ELEVATION
S-001 — GENERAL NOTES
S-101 — FOUNDATION PLAN
```

When to use: very small sets (< 20 sheets) or single-discipline sets where grouping adds no value.

## Special cases

### Phase mixing

If the input set contains multiple phases (e.g. an addendum bound with the original IFC set), add a top-level group **above** discipline:

```
IFC (issued 2026-03-15)
  └── Architectural
      └── A-101 — FIRST FLOOR PLAN
ASI #03 (issued 2026-04-22)
  └── Architectural
      └── A-101A — FIRST FLOOR PLAN — REVISED PARTITION
```

### Unknown sheets

Sheets where the title block could not be read get a separate top-level group `UNKNOWN` so the user can find them quickly to verify manually:

```
Architectural (A)
  └── ...
UNKNOWN
  ├── UNKNOWN-47 — page 47
  └── UNKNOWN-83 — page 83
```

Do not bury unknowns inside a discipline group based on guessing — leave them visibly flagged.

### Collision-suffixed sheets

`-rev2` / `-rev3` suffixed sheets sort within their parent discipline group, immediately after the unsuffixed sheet:

```
Architectural (A)
  ├── A-101 — FIRST FLOOR PLAN  (page 12)
  └── A-101-rev2 — FIRST FLOOR PLAN  (page 213, addendum copy)
```

## Bookmark label format

Each leaf bookmark label uses this format:

```
<sheet_number> — <sheet_name>
```

The em-dash (`—`, U+2014) separator is consistent across NA practice; do not use a hyphen-minus. If `sheet_name` is empty (rare), use just the sheet number.
