# Jurisdiction Profile

Every value in this file was put here by a person reading a code, and carries
the clause it came from. Nothing in it was recalled, inferred, or looked up on
the web. An empty row means nobody has filled it in yet, and the skills that
read this file will ask rather than assume.

## The code in force

| | |
|---|---|
| Project | |
| Governing code | |
| Edition | |
| Accessibility standard | |
| Accessibility edition | |
| Local amendments | |
| Where the amendment text lives | |
| AHJ | |
| Profile started | |

A blank edition makes every row below unusable. Fill this block first.

## Columns

| Column | Means |
|--------|-------|
| Item | The thing being limited |
| Key | What the code splits the row by (use group, sprinklered, occupancy, construction type). Blank if unconditional |
| Limit | The value as the code states it. A range stays a range |
| Unit | The code's own unit. Never converted |
| Clause | Code, edition, and clause number; or file and line; or `not cited` |
| Recorded | The date the row was filled |

## Stair

Used by `design-stair`.

| Item | Key | Limit | Unit | Clause | Recorded |
|------|-----|-------|------|--------|----------|
| Clear width | | | | | |
| Headroom | | | | | |
| Riser height, maximum | | | | | |
| Riser height, minimum | | | | | |
| Tread depth, minimum | | | | | |
| Riser and tread uniformity tolerance | | | | | |
| Nosing projection | | | | | |
| Nosing radius | | | | | |
| Nosing underside angle | | | | | |
| Landing depth | | | | | |
| Vertical rise between landings | | | | | |
| Handrail height above nosing line | | | | | |
| Handrail clearance from wall | | | | | |
| Handrail cross section, circular diameter | | | | | |
| Handrail cross section, non-circular perimeter | | | | | |
| Handrail cross section, non-circular maximum dimension | | | | | |
| Handrail extension beyond top riser | | | | | |
| Handrail extension beyond bottom riser | | | | | |
| Handrails required on both sides | | | | | |
| Open risers permitted | | | | | |
| Slip resistance | | | | | |

## Egress

Used by `design-egress`. Most of these live in tables keyed by use and by
sprinkler condition. Add one row per key you need; the same item appearing
several times with different keys is expected.

| Item | Key | Limit | Unit | Clause | Recorded |
|------|-----|-------|------|--------|----------|
| Egress capacity factor, stairs | | | | | |
| Egress capacity factor, level components | | | | | |
| Number of exits required for the load | | | | | |
| Single exit allowance limit | | | | | |
| Common path of travel limit | | | | | |
| Exit separation, as a fraction of the diagonal | | | | | |
| Travel distance limit | | | | | |
| Corridor minimum width | | | | | |
| Dead-end corridor maximum | | | | | |
| Door clear width minimum | | | | | |
| Door swing threshold by occupant load | | | | | |

## Occupancy load factors

Used by `design-occupancy-load`. Open by design: one row per use and function
in this building, not a fixed list. Record whether the factor is on gross or
net area in the Key column, because the two differ enough to halve or double a
count.

| Item | Key | Limit | Unit | Clause | Recorded |
|------|-----|-------|------|--------|----------|
| | | | | | |

## Accessibility

Used by `code-compliance-review` and `ada-tracker`. Add rows as the review reaches them.

| Item | Key | Limit | Unit | Clause | Recorded |
|------|-----|-------|------|--------|----------|
| | | | | | |

## Anything else

Rows that do not belong to a section above. Move them into one when a section
gains that item.

| Item | Key | Limit | Unit | Clause | Recorded |
|------|-----|-------|------|--------|----------|
| | | | | | |
