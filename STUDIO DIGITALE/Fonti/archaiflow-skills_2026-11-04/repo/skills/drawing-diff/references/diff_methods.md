# What each engine sees, and what it misses

Two engines run against every sheet pair. They fail in different directions, and
neither one's silence is an answer on its own. This file exists so the report
always says which one produced a finding and which one could not have.

## Text extraction

Pulls every text line out of both PDFs with its position, then compares by
position.

**Sees:** dimension values, room names and numbers, door and window tags, general
and keyed notes, fire ratings, spec section references, keynote legends, title
block fields, revision block entries, anything typed into a schedule cell.

**Misses:**

- Any change with no text in it. A wall that moved, a door swing reversed, a
  hatch pattern swapped, a detail bubble relocated, a line weight changed.
- Text baked into an image. A scanned sheet, a screenshot pasted into a detail,
  a flattened consultant background.
- Text that reflowed. A note re-wrapped from two lines to three reads as three
  changes, not one.

**Turns itself off when either side has no extractable text.** Diffing a vector
sheet against a scan of the same sheet would report every line on the vector
side as deleted: a large, confident, entirely false finding. One unreadable side
means no text comparison for that pair, and the report names the side.

**Reports as `edited`** when text at the same spot reads differently. This is the
highest-value output of the engine, because that is the shape a dimension change
takes.

**Normalises the sheet before comparing.** Two things move every line at once
and neither is a change: a re-plot that shifts the sheet a few points, and a
re-issue at a different paper size. The engine measures both from the lines that
read the same on both sides, takes them out, and records them as
`sheet_shift_pt` and `sheet_scale`. Without that step a shifted sheet reports
every note as moved and scatters a real dimension change into one addition plus
one removal, which is the finding you most wanted to see.

**Position tolerance is 3 points by default.** Above about 6 points, two
adjacent notes start collapsing onto one spot. Raise it with `--text-tol` only
when a sheet comes back with many paired add/remove findings that are plainly
the same line.

## Rendered overlay

Renders both pages to grayscale at 50 DPI, finds the whole-sheet offset a
re-plot introduced, removes it, then compares tile by tile.

**Sees:** anything that changed the printed image. Geometry, hatches, line
weights, symbols, clouds, and text, though text is better read by the other
engine.

**Misses:**

- Changes smaller than the tile threshold. At 50 DPI a tile is about 0.64 inch
  square, and a change has to move at least 1% of its pixels. A dimension line
  extended by an eighth of an inch can fall under that.
- Anything outside the search inset. The outermost 6 pixels of the sheet are not
  compared, because that band is what the offset search needs.

**Handles a different paper size** when it is one ratio applied to the whole
sheet, which is what a half-size print is. The new page renders at a DPI
carrying the ratio, so both land on the same pixel grid. A changed aspect ratio
is not a re-scale, and the run stops with `aspect-mismatch`.

**Gives false positives on:**

- A sub-pixel shift the whole-pixel offset search cannot remove. The symptom is
  `residual_pct` above about 40 with regions scattered evenly over the sheet.
  That is not a set of changes, it is a misalignment, and the report has to say
  so instead of listing them.
- A re-plot from a different CAD version, where every line rebuilds slightly
  differently.

## Revision clouds

Compared in both directions, never used as the change list.

Consultants forget to cloud, and the sheets where they forgot are the reason
this comparison is worth running. Clouds also survive into the next revision
when nobody clears them, so a cloud with nothing inside it is its own finding.

## Methods note to paste into the report

Edit to match the run. Do not ship it unedited.

> Two engines ran on each sheet: text extraction, which reports exact values but
> sees nothing that is not typed, and a rendered overlay at 50 DPI, which sees
> printed geometry but cannot read intent. On {{SHEETS}} the text engine was
> skipped because the {{SIDE}} side carries no extractable text (a scan), so any
> note or dimension change on those sheets is not in this report. On {{SHEETS}}
> the overlay was skipped because the two revisions are different shapes.
> {{SHEETS}} did not align well enough to trust the geometry findings. Region
> lists on {{SHEETS}} were capped at {{N}}, so there are more changes than are
> listed. Revision clouds were compared against detected changes and were not
> used as the source of this list.
