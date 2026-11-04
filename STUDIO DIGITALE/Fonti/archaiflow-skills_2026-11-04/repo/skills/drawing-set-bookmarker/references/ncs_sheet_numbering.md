# US National CAD Standard — Sheet Numbering

The US National CAD Standard (NCS), published by the National Institute of Building Sciences, is the de-facto convention for sheet identification on North American architectural and engineering drawing sets. NCS Module 2 (Sheet Identification) defines the structure used here.

A complete sheet number has three parts:

```
A - 1 0 1
│   │ │ │
│   │ └─┴── Sequence number within sheet type
│   └────── Sheet type (one digit, 0–9)
└────────── Discipline designator (one or more letters)
```

Example: `A-101` = Architectural, Plan (1), sequence 01.

## Discipline designators (Level 1)

Single-letter primary designator. Use these as the top level when grouping by discipline.

| Letter | Discipline                |
|--------|---------------------------|
| `G`    | General                   |
| `H`    | Hazardous Materials       |
| `V`    | Survey / Mapping          |
| `B`    | Geotechnical              |
| `C`    | Civil                     |
| `L`    | Landscape                 |
| `S`    | Structural                |
| `A`    | Architectural             |
| `I`    | Interiors                 |
| `Q`    | Equipment                 |
| `F`    | Fire Protection           |
| `P`    | Plumbing                  |
| `D`    | Process                   |
| `M`    | Mechanical                |
| `E`    | Electrical                |
| `W`    | Distributed Energy        |
| `T`    | Telecommunications        |
| `R`    | Resource                  |
| `X`    | Other Disciplines         |
| `Z`    | Contractor / Shop Drawings|
| `O`    | Operations                |

A second letter narrows the discipline (e.g. `AS` = Architectural Site, `SD` = Structural Demolition, `MH` = Mechanical HVAC). When grouping bookmarks, group on the **first** letter only and treat the second letter as part of the sheet number string.

## Sheet type digit (Level 2)

The first digit after the discipline indicates the sheet type:

| Digit | Sheet Type                                                        |
|-------|-------------------------------------------------------------------|
| `0`   | General (cover sheets, drawing index, abbreviations, symbols)     |
| `1`   | Plans (horizontal views — floor plans, site plans, framing plans) |
| `2`   | Elevations (vertical exterior or interior views)                  |
| `3`   | Sections (building sections, wall sections)                       |
| `4`   | Large-scale views (enlarged plans, enlarged elevations)           |
| `5`   | Details                                                           |
| `6`   | Schedules and diagrams                                            |
| `7`   | User-defined                                                      |
| `8`   | User-defined (commonly 3D / axonometric / perspective)            |
| `9`   | 3D representations (BIM views, isometrics) — varies by office     |

So `A-101` is an Architectural Plan, `A-501` is an Architectural Detail, `S-201` is a Structural Elevation, `M-601` is a Mechanical Schedule.

## Common deviations to expect

Real-world sets often deviate slightly. Recognize but do not normalize:

- **Decimal sequence** (`A2.04`, `A5.12`) — older CSI format, still common in legacy offices. Treat the part before the decimal as discipline+sheet-type, the part after as sequence.
- **Three-digit prefixes** (`A001`, `S001`) — cover/general sheets without a hyphen.
- **Letter suffixes** (`A-101A`, `A-101.1`) — sheet additions issued by addendum or bulletin.
- **Phase prefixes** (`SD-A-101`) — uncommon but seen on phased submissions.
- **Federal projects** (`G-001`, `G-002`) — heavy use of General-discipline sheets.

## Sorting rule

Within a discipline group, sort by the natural order of the sheet number string with these rules:

1. Sheet-type digit ascending (0 → 9).
2. Sequence ascending within each sheet type.
3. Alphabetic suffix sorts after the unsuffixed sheet (`A-101` then `A-101A` then `A-101B`).
4. `-rev2`, `-rev3` collision suffixes sort last within their base number.

## References

- US National CAD Standard, Version 6 — Module 2: Sheet Identification (National Institute of Building Sciences, 2014).
- AIA CAD Layer Guidelines (related, used for layer naming inside CAD files — not sheet numbering).
- CSI Uniform Drawing System (UDS), Module 1: Drawing Set Organization.
