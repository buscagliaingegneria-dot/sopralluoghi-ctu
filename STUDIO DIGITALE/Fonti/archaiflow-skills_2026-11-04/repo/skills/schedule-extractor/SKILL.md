---
name: schedule-extractor
description: "This skill should be used when the user has a drawing-set PDF containing one or more tabular schedules (door schedule, window schedule, room finish schedule, equipment schedule) and wants the rows pulled out as a normalized CSV for cross-checking, takeoff, or import into Excel/Revit. Trigger on \"extract the door schedule\", \"pull the finish schedule\", \"tabulate this schedule\", \"schedule to CSV\", or a pasted PDF path with mention of a schedule type. Reads schedule pages via vision, normalizes columns to the AIA / NCS Section A6 conventions, and writes CSV + markdown preview to `docs/schedules/`."
license: MIT
metadata:
  title: "Schedule Extractor"
  summary: "Pull door, window, and finish schedules out of a PDF into CSV"
  discipline: "construction-admin"
  tags: "Design"
---


# Schedule Extractor


## Overview


Pull tabular drawing-set schedules (doors, windows, room finishes, equipment) out of a PDF as a normalized CSV plus a markdown preview, and log them to a per-project schedule index in `docs/schedules/`. This replaces the hand-typing pass that happens every time a consultant ships a CD set without the live Revit schedules attached.


## Scope and limits — read first


**What this does.** Reads schedule pages out of a drawing set by vision, keeps
every cell exactly as printed, maps the captured column names onto a standard
schema, and writes a CSV plus a twenty-row markdown preview into
`docs/schedules/`. Rows in the table equal rows in the CSV.

**What this does not do.**

- **It does not fill an illegible cell.** A cell it cannot read stays empty and
  the row is flagged low confidence for you to check against the sheet. A
  plausible door width is still an invented door width.
- **It does not convert or reformat.** `3'-0"` stays `3'-0"`, fractions stay
  fractions, and `HW-1` stays `HW-1` rather than expanding into the hardware
  list behind it.
- It does not drop a column it cannot place. Unmapped columns carry through to
  the end of the CSV under the names they were printed with.
- It does not check the schedule against the drawings, the spec, or a submittal.
  It reports what the table says.
- It does not open a native Revit or AutoCAD file, and it does not write
  anything back into one.

**What you need before starting.** The PDF and which schedule you want out of
it. Page or sheet numbers if you know them; otherwise the skill probes title
blocks, or reads the sheet index `drawing-set-bookmarker` already wrote.

## When to use


Trigger on:

- Pasted path to a drawing-set PDF together with a schedule type ("extract the door schedule from this set", "pull the finish schedule").
- Explicit asks: "schedule to CSV", "tabulate the door schedule", "give me a finish schedule spreadsheet".
- Cross-checking values against a separate consultant submission ("compare the architect's door schedule to the contractor's submittal").

Do NOT trigger on:

- Bookmark/index requests for the entire set — use `drawing-set-bookmarker` instead.
- Drawing-set completeness review — use `drawing-checklist`.
- Marked-up/redlined schedules needing field-question handling — use `rfi-writer`.
- General questions about what a finish schedule should contain — answer directly without invoking this skill.

## Workflow


### Step 1 — Bootstrap if needed


Check whether `docs/schedules/index.md` exists. If not, run:


```bash
python scripts/init_workspace.py
```


The script creates `docs/schedules/` from `assets/schedules-index-template.md`. No external Python deps are required for this skill — extraction uses the Read tool directly. If the project has no `docs/` folder at all, confirm with the user before bootstrapping.


### Step 2 — Identify schedule type and locate pages


Determine which schedule(s) the user wants:

- `door` — keyed off Mark / Type / W / H / Frame / HW Set columns.
- `window` — keyed off Mark / Type / W / H / Glazing / Operation columns.
- `finish` — room finish schedule, keyed off Room # / Floor / Base / Wall / Ceiling.
- `equipment` — keyed off Tag / Description / Mfr / Model.

If the schedule type is ambiguous, ask the user before proceeding.


Locate the schedule pages either by:

- Page range supplied by the user ("schedule is on sheets A-601 to A-603").
- Sheet index from `drawing-set-bookmarker` if available (`docs/drawing-sets/<base>-index.csv` filtered to `Discipline=A` and `SheetType=6`).
- Direct probe: read sheet titles via the Read tool, looking for the literal phrase "DOOR SCHEDULE" / "WINDOW SCHEDULE" / "ROOM FINISH SCHEDULE" / "EQUIPMENT SCHEDULE" in the title block.

### Step 3 — Vision read of schedule pages


Read the schedule pages with the Read tool, chunking 5–10 pages per call. For each page:

1. Capture the table header row verbatim (column names exactly as printed).
2. Capture every body row as a list of cells, in column order.
3. Note any merged cells, sub-headers, or continuation indicators ("CONT'D ON A-602").
4. Note any footnotes / "Notes:" blocks below the table — these often contain hardware abbreviations or fire-rating overrides referenced by row.

Persist the raw extraction as JSON at `docs/schedules/.cache/<schedule-type>-raw.json`:


```json
{
  "schedule_type": "door",
  "source_pdf": "<basename>.pdf",
  "pages": [
    {
      "page_index": 142,
      "sheet_number": "A-601",
      "headers": ["Mark", "Type", "Width", "Height", "Frame", "HW Set", "Fire", "Notes"],
      "rows": [
        ["101A", "F1", "3'-0\"", "7'-0\"", "HM", "HW-1", "20 min", ""],
        ...
      ],
      "footnotes": ["HW-1: lockset, closer, hinges (3)"]
    }
  ]
}
```


If a row is illegible or has a missing cell, write the cell value as `""` (empty string) and add `confidence: low` to that row entry. Never invent values.


### Step 4 — Normalize columns to standard schema


Run:


```bash
python scripts/normalize_schedule.py \
  --raw "docs/schedules/.cache/<schedule-type>-raw.json" \
  --type <door|window|finish|equipment> \
  --out "docs/schedules/<basename>-<schedule-type>-schedule.csv"
```


The script maps captured header names to the standard schema using a header-synonym table. Columns it cannot map are appended at the end with their captured names preserved. The script never silently drops columns.


Door, window, and finish each have a schema reference in `references/`, listing the column meanings and the type codes behind them. Equipment has no reference file; its columns are the inline list below and the header row in `assets/equipment-schedule-template.csv`.


Standard schemas (full detail in references):

- **Door**: `Mark, Type, Width, Height, Thickness, Material, Frame, HardwareSet, FireRating, Remarks`
- **Window**: `Mark, Type, Width, Height, Material, Glazing, Operation, Remarks`
- **Finish (room)**: `RoomNumber, RoomName, Floor, Base, NorthWall, EastWall, SouthWall, WestWall, Ceiling, Remarks`
- **Equipment**: `Tag, Description, Manufacturer, Model, Power, Remarks`

For dimensional fields, preserve the imperial format as printed (`3'-0"`, `7'-0"`). Do NOT silently convert to decimal feet or metric.


### Step 5 — Write a markdown preview


Beside the CSV, write a markdown table preview at `docs/schedules/<basename>-<schedule-type>-schedule.md`. The preview shows the first 20 rows for quick visual review before the user opens the CSV. Use the same column order as the CSV.


### Step 6 — Update the project index


Run:


```bash
python scripts/append_to_index.py \
  --date 2026-05-08 \
  --source "<basename>.pdf" \
  --type <schedule-type> \
  --row-count <N> \
  --csv "<basename>-<schedule-type>-schedule.csv" \
  --preview "<basename>-<schedule-type>-schedule.md"
```


Appends a row to `docs/schedules/index.md`. Do NOT edit `index.md` directly with Edit — table alignment breaks.


### Step 7 — Report


Tell the user:

- Path to the CSV and the markdown preview.
- Row count, broken down by `confidence: low` rows that need manual verification (with their Mark / Tag).
- Any captured columns that did not map to the standard schema (preserved at the end of the CSV).
- Cross-reference flags: hardware sets referenced but not defined in the table footnotes; fire ratings inconsistent with NCS sheet-type series; missing Mark values.

## Rules

- Cell values are quoted verbatim from the PDF — never normalize dimensions, never reformat fractions, never expand abbreviations on output.
- Every row visible in the table must produce a row in the CSV. Page row count in equals output row count out.
- Standard column schema is per `references/<type>_schedule_schema.md`. Unknown columns are preserved at the end with original names.
- Output files live in `docs/schedules/` of the user's project, never in the skill folder or `/tmp`.
- Vision-extracted rows with `confidence: low` are reported to the user, not silently merged.
- Cache JSON in `docs/schedules/.cache/` is treated as resumable state, not deliverable — do not surface it as an artifact.

## Anti-patterns

- Filling in missing cells from "common sense" (e.g. assuming a 3'-0" door if Width is illegible). Mark `confidence: low` and leave the cell empty.
- Converting dimensions ("3'-0"" → 36" → 0.9144 m"). The schedule is the contract drawing — keep verbatim.
- Expanding hardware-set abbreviations ("HW-1" → "lockset, closer, hinges (3)") in the cell. The footnote stays in `references/hardware_sets.md` guidance, but the cell value stays "HW-1".
- Editing `docs/schedules/index.md` with the Edit tool. Use `append_to_index.py`.
- Skipping the markdown preview step. The user reviews the preview first; the CSV is downstream.
- Treating tabula-py / camelot output as authoritative without vision verification — those PDF table extractors silently misalign cells on dense schedules. Vision read is the source of truth here.

## Resources

- `scripts/init_workspace.py` — bootstrap `docs/schedules/`
- `scripts/normalize_schedule.py` — map raw extracted JSON to standard CSV per schedule type
- `scripts/append_to_index.py` — append a processed-schedule row to `docs/schedules/index.md`
- `references/door_schedule_schema.md` — door schedule columns + type codes (NCS / industry)
- `references/window_schedule_schema.md` — window schedule columns
- `references/finish_schedule_schema.md` — room finish schedule columns (CSI format)
- `references/hardware_sets.md` — common HW-set abbreviation glossary (project-specific caveat)
- `assets/door-schedule-template.csv` — header row for door CSV
- `assets/window-schedule-template.csv` — header row for window CSV
- `assets/finish-schedule-template.csv` — header row for room finish CSV
- `assets/equipment-schedule-template.csv` — header row for equipment CSV
- `assets/schedules-index-template.md` — initial markdown table for the project-wide schedules index
