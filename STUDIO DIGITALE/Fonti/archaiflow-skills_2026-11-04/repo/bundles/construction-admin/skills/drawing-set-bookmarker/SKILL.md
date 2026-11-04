---
name: drawing-set-bookmarker
description: "This skill should be used when the user has a multi-sheet architectural drawing-set PDF (typically 50–300 sheets) with no bookmarks or a flat/incorrect bookmark tree, and wants a properly bookmarked PDF plus a CSV sheet index. Trigger on \"bookmark this drawing set\", \"add bookmarks to this PDF\", \"tabulate sheets\", \"make a sheet index\", or a pasted path to a multi-sheet drawing PDF. Reads each page's title block via vision, extracts sheet number/name/discipline, groups by discipline per US National CAD Standard, and writes the bookmarked PDF + index to `docs/drawing-sets/`."
license: MIT
metadata:
  title: "Drawing Bookmarks"
  summary: "Bookmark a flat drawing-set PDF and index its sheets"
  discipline: "construction-admin"
  tags: "Design"
---


# Drawing Set Bookmarker


## Overview


Take a flat (no-bookmarks or wrong-bookmarks) drawing-set PDF, identify each sheet from its title block via multimodal vision, and produce two artifacts in `docs/drawing-sets/`: a bookmarked PDF (nested by US National CAD Standard discipline → sheet number) and a CSV index of every sheet. This replaces the manual Bluebeam Stapler workflow most offices repeat for every consultant submission.


## Scope and limits — read first


**What this does.** Reads every page's title block, records the sheet number and
name exactly as printed, and writes two things to `docs/drawing-sets/`: the same
PDF with a nested bookmark tree, and a CSV index with one row per page. Pages in
equals rows out, every time.

**What this does not do.**

- **It does not take a sheet number from anywhere but the title block.** Not
  from the filename, not from page order, not from what the sequence implies. A
  page whose title block cannot be read becomes `UNKNOWN-<page>` at low
  confidence and is reported to you, never dropped and never guessed.
- **It does not tidy sheet numbers.** `A-101` stays `A-101`. No leading zeros
  removed, no dashes harmonised into dots, no case changed.
- It does not read the drawings themselves. Content, dimensions, and revisions
  are outside it: use `drawing-reader` for a sheet and `schedule-extractor` for
  a schedule table.
- It does not check the set for completeness or code. Those are
  `drawing-checklist` and `code-compliance-review`.
- It does not install anything. If `pikepdf` is missing the run stops and prints
  the install command for you to run.

**What you need before starting.** The multi-sheet PDF, and `pikepdf` importable
in the environment. Sets beyond about 300 pages are worth batching, and the
skill asks before starting one.

## When to use


Trigger on:

- Pasted path to a multi-sheet drawing PDF that has no bookmarks (or a single flat list).
- Explicit asks: "bookmark this set", "add bookmarks to the drawings", "tabulate the sheets", "make a sheet index", "give me a CSV of sheets".
- Consultant-issued CD/IFC sets received without a bookmark tree.

Do NOT trigger on:

- Single-sheet PDFs (nothing to bookmark).
- Marked-up/redlined PDFs needing field-question handling — use `rfi-writer` instead.
- Schedule extraction (door / window / finish schedules) — use `schedule-extractor` when present.
- Questions about how PDF bookmarking works in the abstract — answer directly.

## Workflow


### Step 1 — Bootstrap if needed


Check whether `docs/drawing-sets/` exists with an `index.md`. If not, run:


```bash
python scripts/init_workspace.py
```


The script creates `docs/drawing-sets/` from `assets/drawing-sets-index-template.md` and verifies `pikepdf` is importable. If `pikepdf` is missing, the script prints the install hint (`pip install pikepdf`) and exits non-zero — surface this to the user and stop. Do NOT pip-install on the user's behalf.


If the project has no `docs/` folder at all, confirm with the user before bootstrapping.


### Step 2 — Probe the input


Run:


```bash
pdfinfo "<input.pdf>"
```


Capture the page count, page size, and producer. If `pdfinfo` is unavailable (no poppler), fall back to using `Read` with `pages: "1"` purely to confirm the file is a real PDF. Report page count to the user before proceeding (large sets > 300 pages may want batching — ask).


### Step 3 — Detect title block region


Read pages 1, mid (`floor(N/2)`), and last with the `Read` tool (`pages: "1"`, `"<mid>"`, `"<N>"`). Identify the title block location based on what is observed:

- **ANSI bottom-right strip** (most common in NA practice) — title block occupies the right ~20% of sheet height across the bottom or full right edge.
- **ANSI bottom strip** — title block runs the full bottom width.
- **Side strip** (less common) — title block on the left or right vertical edge.

If unsure, consult `references/titleblock_locations.md`. If the layout is non-standard or different on different sheets, ask the user to specify the region (e.g. "title block is in the bottom-left") rather than guessing.


### Step 4 — Per-page vision read (chunked)


Read the entire PDF in chunks of 5–10 pages per `Read` call (`pages: "1-10"`, `"11-20"`, …) to stay under the 20-page-per-call limit and keep the model focused. For each page, extract:

- `sheet_number` — verbatim as printed (e.g. `A-101`, `A2.04`, `S001`, `M-201`). Preserve hyphens, dots, leading letters.
- `sheet_name` — the sheet title (e.g. `FIRST FLOOR PLAN`).
- `discipline` — single letter from the sheet number prefix per `references/ncs_sheet_numbering.md` (G/A/S/M/E/P/L/C/T/Q/F/I). If the prefix is non-standard, fall back to inferring from sheet content (plan vs framing vs ducts) and flag.
- `phase` — if a phase is shown in the title block (`SD`, `DD`, `CD`, `IFC`, `IFB`, `BULLETIN #`, `ASI #`). Else leave blank.
- `confidence` — `high` / `medium` / `low` based on legibility.
- `page_index` — 1-based PDF page number.

Persist the running list as JSON to `docs/drawing-sets/.cache/<base>-sheets.json`. This lets a second pass resume on failure and lets `apply_bookmarks.py` consume it deterministically.


For pages where the title block is illegible or missing entirely, set `sheet_number = "UNKNOWN-<page_index>"`, `discipline = "UNKNOWN"`, `confidence = "low"`. Never silently drop a page.


### Step 5 — Resolve collisions


If two sheets share the same `sheet_number` (revisions or re-issued sheets included in the same set), suffix the later occurrence with `-rev2`, `-rev3`, … in the order they appear. Note collisions in the index `ConfidenceFlag` column (`collision-suffixed`).


### Step 6 — Choose grouping strategy


Default: **discipline-grouped, sorted by sheet number within each discipline**. This matches NCS organization and is what every NA office expects.


Other strategies in `references/bookmark_grouping_strategies.md`:

- **sheet-type-grouped** (plans / elevations / sections / details / schedules) — useful for QC review.
- **flat-by-number** — only when the set is single-discipline and small.

Use the default unless the user asked otherwise.


### Step 7 — Apply bookmarks


Build the bookmark tree as JSON matching the schema in `apply_bookmarks.py --help`, then run:


```bash
python scripts/apply_bookmarks.py \
  --input "<input.pdf>" \
  --tree "docs/drawing-sets/.cache/<base>-bookmarks.json" \
  --output "docs/drawing-sets/<base>-bookmarked.pdf"
```


The script uses `pikepdf` to write a nested outline. Do NOT attempt to author bookmarks with the `Edit` tool or shell `qpdf` flags directly — `pikepdf` keeps the tree validated.


### Step 8 — Write CSV index


Read `assets/index-template.csv` (header row only) and write the populated index to:


`docs/drawing-sets/<base>-index.csv`


One row per sheet, in PDF page order. Columns: `SheetNumber,SheetName,Discipline,Phase,PageIndex,ConfidenceFlag`.


### Step 9 — Update the project index


Run:


```bash
python scripts/append_to_index.py \
  --date 2026-05-08 \
  --source "<input.pdf basename>" \
  --sheet-count <N> \
  --bookmarked "<base>-bookmarked.pdf" \
  --csv "<base>-index.csv"
```


Appends one row to `docs/drawing-sets/index.md`. Do NOT edit `index.md` directly with Edit — table alignment breaks.


### Step 10 — Report


Tell the user:

- Path to bookmarked PDF.
- Path to CSV index.
- Sheet count, broken down by discipline.
- Count of low-confidence or `UNKNOWN` sheets that need manual verification (with their page numbers).
- Any collision suffixes applied.

## Rules

- Sheet numbers are quoted verbatim from the PDF — never normalize formatting (do not change `A-101` to `A101` or `A.101`).
- Every page in the input PDF must produce exactly one row in the index. Page count in equals row count out.
- Discipline letter follows US NCS v6 (`references/ncs_sheet_numbering.md`). Do not invent custom prefixes.
- Output files live in `docs/drawing-sets/` of the user's project, never in the skill folder or `/tmp`.
- Vision-extracted values with `confidence: low` are reported to the user, not silently merged.
- Cache JSON in `docs/drawing-sets/.cache/` is treated as resumable state, not deliverable — do not surface it as an artifact.

## Anti-patterns

- Counting/inferring sheet numbers from filename or page order. Always read the title block.
- Dropping pages whose title block is illegible. Mark `UNKNOWN-<page>` instead.
- Re-implementing bookmark application inline with `qpdf` shell flags. Use `apply_bookmarks.py` so the tree is validated.
- Editing `docs/drawing-sets/index.md` with the Edit tool. Use `append_to_index.py`.
- Auto-installing `pikepdf` / poppler for the user. Surface install commands and stop.
- "Cleaning up" sheet numbers (e.g. removing leading zeros, harmonizing dash vs dot). Verbatim only.
- Bookmarking from the filename ("Drawings_2026-05.pdf") instead of the title block.

## Resources

- `scripts/init_workspace.py` — bootstrap `docs/drawing-sets/` and verify `pikepdf`
- `scripts/apply_bookmarks.py` — apply nested bookmark tree to PDF using `pikepdf`
- `scripts/append_to_index.py` — append a processed-set row to `docs/drawing-sets/index.md`
- `references/ncs_sheet_numbering.md` — US National CAD Standard v6 discipline designators and sheet-type digit conventions
- `references/titleblock_locations.md` — common title block positions on NA sheets
- `references/bookmark_grouping_strategies.md` — discipline-grouped vs sheet-type-grouped vs flat-by-number
- `assets/index-template.csv` — CSV header row for the per-set sheet index
- `assets/drawing-sets-index-template.md` — initial markdown table for the project-wide processed-set index
