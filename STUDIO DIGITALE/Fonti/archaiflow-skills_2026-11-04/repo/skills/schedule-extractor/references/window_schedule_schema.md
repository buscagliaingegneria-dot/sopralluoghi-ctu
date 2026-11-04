# Window Schedule — Standard Schema

Window schedules in NA architectural CD sets are normally simpler than door schedules — most projects have a smaller window-type vocabulary that's defined on a window-type elevation sheet, with the schedule cross-referencing those types. The schema below is the normalized output of `normalize_schedule.py`.

## Standard columns

| Column | Required | Description |
|--------|----------|-------------|
| `Mark` | yes | Window tag as printed on plans (e.g. `W-01`, `103`). Verbatim. |
| `Type` | yes | Window type code (e.g. `A`, `B`, `B1`). Defined on a window type sheet. |
| `Width` | yes | Rough opening or unit width as printed (`4'-0"`, `6'-2"`). Whether RO or unit varies — preserve the value, do not interpret. |
| `Height` | yes | Same convention as Width. |
| `Material` | yes | Frame material (`AL` = aluminum storefront / curtain wall, `WD` = wood, `VYL` = vinyl, `STL` = steel, `FBG` = fiberglass). |
| `Glazing` | yes | Glazing make-up (`1" IGU`, `1-1/8" IGU LowE`, `Tempered`, `Lam-Tempered`). Spec sections 08 80 00 and 08 81 00 define the assemblies. |
| `Operation` | recommended | `Fixed`, `Casement`, `Awning`, `DH` (double-hung), `SH` (single-hung), `Slider`, `Hopper`, `Pivot`. |
| `Remarks` | optional | Free text. Often contains energy code requirements (U-value, SHGC), egress dimension verifications, or hardware notes. |

## Type code conventions

Window types are project-specific; the schedule's "Type" column maps to a window-type elevation sheet (typically `A-6XX` series, sheet-type 6) where each type's frame, mullion, and glazing layout is drawn at scale. Common type-naming patterns:

- Single capital letter (`A`, `B`, `C`) — small project with few types.
- Letter + numeric suffix (`A1`, `A2`) — same family, different size or configuration.
- `W-##` numeric — large project with many unique units.

## Common header synonyms

| Standard | Synonyms seen in practice |
|----------|--------------------------|
| `Mark` | `Window No`, `Window #`, `WIN No`, `Tag`, `No.` |
| `Type` | `Window Type`, `WIN Type`, `Unit Type`, `T` |
| `Width` | `W`, `RO W`, `Unit W`, `Nom W`, `Width (RO)` |
| `Height` | `H`, `RO H`, `Unit H`, `Nom H` |
| `Material` | `Mat`, `Mat'l`, `Frame Mat`, `Frame` |
| `Glazing` | `Glass`, `Glaz`, `IG`, `IGU`, `Lite Make-Up` |
| `Operation` | `Op`, `Operation Type`, `Action`, `Function` |
| `Remarks` | `Notes`, `Comments`, `Rmks` |

## Energy-code & egress flags (Step 7 reporting)

Flag without auto-correcting:

1. **U-value / SHGC missing on conditioned-envelope windows** — IECC and most state energy codes require these to be on the schedule or on the unit type elevation. If the user has indicated the project is in a jurisdiction with a state energy code (CA Title 24, NY ECCCNYS, MA Stretch Code, WA Energy Code), and the Remarks column has no U-value, flag.
2. **Bedroom window egress** — IBC §1030.2 / IRC R310 requires a minimum 5.7 sf clear opening (5.0 sf for grade-floor units), 24" min clear height, 20" min clear width, max 44" sill height. If any window is tagged "BEDROOM" or "BR" in remarks/sheet location, flag the row for egress check.
3. **Tempered-glazing locations** — IBC §2406.4 hazardous locations (within 24" of doors, < 18" from finished floor in 9 sf+ panes, etc.) — flag if Glazing column doesn't note "Temp" / "Tempered" for typical hazardous-location windows.

## Reference

- AIA Architectural Graphic Standards (12th ed.), Chapter 8 — Windows.
- CSI MasterFormat 2020, Division 08 — Openings (08 50 00 Windows, 08 51 13 Aluminum Windows, 08 80 00 Glazing).
- IBC 2024 §1030 (Emergency Escape and Rescue Openings), §2406 (Safety Glazing).
- IECC 2024 / ASHRAE 90.1-2022 — fenestration U-value and SHGC limits.
