# Door Schedule — Standard Schema

The door schedule is one of the most heavily cross-referenced documents in a CD set: doors are tagged on every floor plan, sized by architecture, framed by structure (rough opening), and hardware-specified by spec section 08 71 00. The schema below is the normalized format `normalize_schedule.py` writes; consultant submissions vary in column order and naming, but should map onto these fields.

## Standard columns

| Column | Required | Description |
|--------|----------|-------------|
| `Mark` | yes | Door tag as it appears on the plan (e.g. `101A`, `203`, `B-04`). Verbatim. |
| `Type` | yes | Door type code (e.g. `F1`, `G2`, `L1`). Cross-referenced with the door type elevations on a separate sheet. |
| `Width` | yes | Leaf width as printed (`3'-0"`, `2'-8"`). Pairs use `(2) 3'-0"` or `3'-0" PR` per office convention. |
| `Height` | yes | Leaf height (`7'-0"`, `8'-0"`). |
| `Thickness` | recommended | Leaf thickness (`1-3/4"`). Often missing on schematic-phase schedules. |
| `Material` | yes | Door material (`HM` = hollow metal, `WD` = wood, `AL` = aluminum, `GL` = glass / storefront). |
| `Frame` | yes | Frame material/type (`HM`, `AL`, `WD`). Sometimes broken into `FrameMaterial` + `FrameType`. |
| `HardwareSet` | yes | Hardware-set tag (`HW-1`, `HW-2A`). Defined in spec section 08 71 00 or in a footnote. |
| `FireRating` | conditional | Required for doors in fire-rated assemblies (`20 min`, `45 min`, `90 min`). Blank if non-rated. |
| `Remarks` | optional | Free text. Often contains glazing notes, magnetic-hold-open notes, electronic access notes. |

## Type code conventions (industry, not standardized)

These are common patterns; offices may differ:

| Code | Meaning |
|------|---------|
| `F`  | Flush (solid leaf, no glazing) |
| `G`  | Glazed (vision lite or fully glazed) |
| `L`  | Louvered (mechanical room doors) |
| `S`  | Sliding |
| `B`  | Bi-fold |
| `D`  | Dutch |
| `O`  | Overhead (sectional / coiling) |

Number suffixes (`F1`, `F2`, …) typically distinguish leaf size or vision-lite configuration within a type and are defined on a door-type elevation sheet (usually `A-6XX` series).

## Common header synonyms (used by `normalize_schedule.py`)

When reading consultant schedules, the same conceptual column appears under many names. The normalizer maps these to the standard column names above:

| Standard | Synonyms seen in practice |
|----------|--------------------------|
| `Mark` | `Door No`, `Door Number`, `Door Tag`, `No.`, `#`, `Mark No` |
| `Type` | `Door Type`, `DR Type`, `Type Mark`, `T` |
| `Width` | `W`, `Door W`, `Lf Width`, `Leaf W`, `Nom W` |
| `Height` | `H`, `Door H`, `Lf Height`, `Nom H` |
| `Thickness` | `Thk`, `T` (when distinct from Type), `Door Thk` |
| `Material` | `Mat`, `Mat'l`, `Door Mat`, `Lf Material` |
| `Frame` | `Frame Mat`, `Frame Type`, `Frm`, `Frame Mat'l` |
| `HardwareSet` | `HW`, `HW Set`, `Hdw`, `Hardware`, `HW Group` |
| `FireRating` | `Rating`, `Fire`, `FR`, `Lbl`, `Label` |
| `Remarks` | `Notes`, `Comments`, `R/M`, `Rmks` |

If a header name is novel and does not match any synonym, the normalizer preserves it at the end of the CSV with the original name and flags it in stderr.

## Cross-reference checks (Step 7 reporting)

The skill should flag, but not auto-correct, these inconsistencies:

1. **HW Set referenced but not defined** — `Mark 101A` cites `HW-7` but no `HW-7` definition appears in the schedule footnotes or referenced spec section.
2. **Fire-rated frame mismatch** — door rated 90 min but frame material listed as `WD` (wood) without an intumescent assembly note.
3. **Missing Mark** — a row exists with no Mark value (typically a continuation glyph that was misread).
4. **Duplicate Mark** — same Mark appears twice. May be a revision artifact or genuine duplication.

## Reference

- AIA Architectural Graphic Standards (12th ed.), Chapter 8 — Doors.
- CSI MasterFormat 2020, Division 08 — Openings (08 11 00 Metal Doors and Frames, 08 71 00 Door Hardware, 08 14 00 Wood Doors).
- US National CAD Standard v6 — sheet-type 6 conventions for schedules.
