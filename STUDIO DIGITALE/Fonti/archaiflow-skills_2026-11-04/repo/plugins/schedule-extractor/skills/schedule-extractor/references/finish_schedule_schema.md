# Room Finish Schedule — Standard Schema

The room finish schedule is a cross-tab of room-by-room finishes for floor, base, walls (often each cardinal direction), and ceiling. Every project does it slightly differently — some compress walls to a single column, some explode them to four, some use abbreviation codes that map to a finish-legend on a separate sheet. The schema below is the normalized output of `normalize_schedule.py`.

## Standard columns

| Column | Required | Description |
|--------|----------|-------------|
| `RoomNumber` | yes | Room tag per the floor plan (e.g. `101`, `B-04`, `2.07`). Verbatim. |
| `RoomName` | yes | Room name (e.g. `OFFICE`, `CORRIDOR`, `JANITOR'S CLOSET`). |
| `Floor` | yes | Floor finish code (e.g. `CPT-1`, `VCT-3`, `PT-1`, `CONC SEALED`). |
| `Base` | yes | Base finish code (e.g. `RB-1`, `WD-1`, `TILE-2`). |
| `NorthWall` | conditional | North-facing wall finish code. Use `NorthWall`/`EastWall`/`SouthWall`/`WestWall` if the source schedule splits walls; if the source compresses to one `Wall` column, fill all four with the same value and note in Remarks. |
| `EastWall` | conditional | East-facing wall finish. |
| `SouthWall` | conditional | South-facing wall finish. |
| `WestWall` | conditional | West-facing wall finish. |
| `Ceiling` | yes | Ceiling finish code (e.g. `ACT-1`, `GWB-PT-1`, `EXPOSED`). |
| `Remarks` | optional | Free text. Often contains acoustic notes (NRC, STC), wainscot heights, "VIF", "Match existing", paint colors. |

## Finish code conventions

Codes are always project-specific and defined in a "FINISH LEGEND" or "MATERIAL LEGEND" sheet (commonly the cover sheet of the finish drawings, `A-9XX` series, sheet-type 6). Typical prefixes:

| Prefix | Material family |
|--------|-----------------|
| `CPT`  | Carpet |
| `VCT`  | Vinyl composition tile |
| `LVT`  | Luxury vinyl tile |
| `WD`   | Wood (flooring or base) |
| `RB`   | Resilient (rubber) base |
| `TILE` | Ceramic / porcelain / stone tile |
| `STN`  | Stone |
| `CONC` | Concrete (sealed, polished, stained) |
| `PT`   | Paint |
| `GWB`  | Gypsum wall board |
| `ACT`  | Acoustic ceiling tile |
| `WD-PNL` | Wood paneling |
| `MTL`  | Metal panel / cladding |

The numeric suffix (`PT-1`, `PT-2`) selects a specific product within the family; cross-referenced to spec section 09 90 00 (Painting and Coating) or the relevant finish division.

## Common header synonyms

| Standard | Synonyms seen in practice |
|----------|--------------------------|
| `RoomNumber` | `Room No`, `Room #`, `RM No`, `Room`, `No.` |
| `RoomName` | `Name`, `Room Name`, `RM Name`, `Description` |
| `Floor` | `Flr`, `Floor Finish`, `Flooring`, `FLR` |
| `Base` | `Bs`, `Base Finish` |
| `NorthWall` | `N Wall`, `Wall N`, `North`, `N` |
| `EastWall` | `E Wall`, `Wall E`, `East`, `E` |
| `SouthWall` | `S Wall`, `Wall S`, `South`, `S` |
| `WestWall` | `W Wall`, `Wall W`, `West`, `W` |
| `Ceiling` | `Clg`, `Ceiling Finish`, `CLG` |
| `Remarks` | `Notes`, `Comments`, `Rmks` |

When the source schedule has a single `Wall` column rather than four directional columns, the normalizer fills all four `*Wall` fields with the same value and adds `single-wall-source` to the Remarks.

## Cross-reference checks (Step 7 reporting)

Flag without auto-correcting:

1. **Code referenced but not legended** — `PT-7` cited in a row but no `PT-7` definition appears in the finish legend (if available).
2. **Wet-room finish coordination** — rooms with names matching `BATHROOM`, `RESTROOM`, `JANITOR`, `KITCHEN`, `LAUNDRY` should typically have non-absorbent floor and base; flag if `Floor` is `CPT-*` or `WD-*`.
3. **Missing room** — room number visible on a plan (if cross-referenced via drawing-set-bookmarker) but absent from the schedule.
4. **Plenum / above-ceiling rated assemblies** — rooms in fire-rated occupancy separations (corridor, exit enclosure) need to coordinate with the ceiling rating; flag if Ceiling is `EXPOSED` for a corridor in an R-2 building (likely a code issue).

## Reference

- AIA Architectural Graphic Standards (12th ed.), Chapter 9 — Finishes.
- CSI MasterFormat 2020, Division 09 — Finishes (09 22 00 Supports for Plaster and Gypsum Board, 09 51 00 Acoustical Ceilings, 09 65 00 Resilient Flooring, 09 90 00 Painting and Coating).
- US National CAD Standard v6 — sheet series A-9XX (Architectural finishes).
