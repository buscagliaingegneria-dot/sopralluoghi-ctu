# Title Block Locations

The title block is the area of a drawing sheet that contains the sheet number, sheet name, project info, revision history, north arrow callouts, and seal. The vision read in Step 4 must look at this region — knowing where to look improves accuracy and lets large sets be processed by cropped image rather than full-page reads.

## Standard sheet sizes (NA practice)

| Designator | Size (inches) | Common use                     |
|------------|---------------|--------------------------------|
| ANSI A     | 8.5 × 11      | Sketches, RFIs, supplements    |
| ANSI B     | 11 × 17       | Half-size CD set prints        |
| ARCH C     | 18 × 24       | Small-project full-size        |
| ARCH D     | 24 × 36       | Standard NA full-size CD set   |
| ARCH E     | 36 × 48       | Large civil / institutional    |
| ARCH E1    | 30 × 42       | Common alternative to E        |

PDFs from Revit or AutoCAD usually preserve the sheet size in points (72 pt = 1 inch). `pdfinfo` reports this as `Page size: 2592 x 1728 pts (ARCH D)` etc.

## Common title block layouts

### 1. Right-edge strip (most common in NA practice)

Title block occupies a vertical strip along the right edge, full sheet height, ~6–8 inches wide. The sheet number and sheet name typically sit at the bottom of this strip in the largest text on the sheet.

- Region: right ~20–25% of sheet width, full height.
- Sheet number focus zone: bottom-right corner, bottom ~15% of height.
- Used by: most large architectural firms (SOM, HOK, Gensler-style standards).

### 2. Bottom strip

Title block runs the full bottom width of the sheet, ~3–4 inches tall. Sheet number is in the bottom-right cell.

- Region: bottom ~15% of sheet height, full width.
- Sheet number focus zone: bottom-right corner.
- Used by: many engineering consultants, smaller offices.

### 3. Bottom-right block (compact)

A roughly square title block in the bottom-right corner only, with project info / drawn-by / scale stacked vertically and the sheet number at the bottom.

- Region: bottom-right ~25% width × ~25% height.
- Sheet number focus zone: bottom-most cell of the block.
- Used by: small-project sheets, ARCH C/B sizes.

### 4. ISO bottom strip

Per ISO 7200 (Title blocks for technical drawings). Less common in NA but appears on international or federal-with-foreign-collaborator projects.

- Region: bottom of sheet, full width, with mandatory fields in fixed cells.
- Sheet number in the rightmost cell.

## Heuristics for first-pass detection

When examining the sample pages in Step 3:

1. The sheet number is usually the **largest text** on the sheet outside of titles within drawings themselves.
2. The sheet number sits **near** the sheet name, with the name above and the number below — or both in the same cell.
3. The seal/stamp (usually circular) is a strong landmark — it sits adjacent to the title block in NA practice.
4. Revision history (a small table with rev #, date, description) is almost always within or directly above the title block.

If two or more of these landmarks are visible in the same region, that is the title block.

## When sample pages disagree

Sometimes a single set has different title block layouts (e.g. consultant sheets bound into an architect's set). When sample pages show different layouts, switch to per-page detection: read each page individually rather than relying on a fixed crop.

## Crop-coordinate guidance (optional optimization)

For very large sets where vision throughput matters, crop the title block region with `pdftoppm` before vision read. Coordinates as fractions of page width (W) and height (H):

| Layout                | x_start | y_start | x_end | y_end |
|-----------------------|---------|---------|-------|-------|
| Right-edge strip      | 0.75 W  | 0.00 H  | 1.00 W| 1.00 H|
| Bottom strip          | 0.00 W  | 0.85 H  | 1.00 W| 1.00 H|
| Bottom-right block    | 0.75 W  | 0.75 H  | 1.00 W| 1.00 H|
| ISO bottom strip      | 0.00 W  | 0.92 H  | 1.00 W| 1.00 H|

Cropping is optional — the `Read` tool with full pages also works but uses more tokens per page.
