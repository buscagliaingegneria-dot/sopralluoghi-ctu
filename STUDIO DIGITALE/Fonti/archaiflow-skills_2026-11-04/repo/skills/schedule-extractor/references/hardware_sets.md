# Hardware Sets — Common Abbreviations

Door schedules cite hardware via a shorthand tag (`HW-1`, `HW-2A`, etc.) that resolves either in a footnote on the schedule or in the project specifications, typically CSI section 08 71 00 (Door Hardware). **This file is a glossary for what a tag *typically* means in NA practice — it is NOT a substitute for the project's own hardware-set definitions.** Always cite the project spec book; the schedule is the legal contract value.

## Why this matters for schedule extraction

When extracting a door schedule, the `HardwareSet` cell is just an opaque tag (`HW-1`). The Step 7 cross-reference check should:

1. **Confirm the tag is defined somewhere** — in the schedule footnotes, on a separate hardware schedule sheet, or in the spec book. If not defined anywhere visible, flag.
2. **Not expand the tag** in the CSV cell. The cell stays `HW-1`. Expansion goes in a separate report only if the user asks.

This file lets the skill recognize *common* abbreviations seen inside a hardware-set definition (the footnote / spec text, not the schedule cell), so it can validate that a definition makes sense.

## Common abbreviations inside hardware-set definitions

| Abbreviation | Meaning |
|--------------|---------|
| `HG` / `BB` | Hinge / Ball-bearing hinge |
| `CH` | Continuous hinge |
| `LS` / `LK` | Lockset |
| `EL` | Electric latch / strike |
| `EH` | Electric hinge (power transfer) |
| `MK` / `MORT` | Mortise lock |
| `CYL` | Cylindrical lock |
| `DB` | Deadbolt |
| `EX` / `EX DEV` | Exit device (panic / fire exit hardware) |
| `CL` / `CLOSER` | Door closer |
| `OH STOP` | Overhead stop |
| `WS` | Wall stop / Weatherstrip (context-dependent) |
| `ASTRAGAL` | Astragal (paired-door seal) |
| `THR` | Threshold |
| `KP` | Kickplate |
| `PUSH/PULL` | Push plate / Pull bar |
| `SIL` | Silencer |
| `FL` / `FB` | Flush bolt (for inactive leaf) |
| `MAG HOLD` | Magnetic hold-open |
| `CR` / `CARD` | Card reader (electronic access) |
| `REX` | Request-to-exit sensor |
| `DOG` | Dogging device (allows panic to stay retracted) |

## ANSI / BHMA grade references

Hardware quality is graded under ANSI/BHMA standards. Common citations on plans:

- `Grade 1` — heaviest duty (commercial / institutional). Most CD sets specify Grade 1 throughout for non-residential.
- `Grade 2` — medium duty (light commercial, multifamily common areas).
- `Grade 3` — residential / light duty.

Specific BHMA standards by hardware category:

- ANSI/BHMA A156.1 — Butt hinges
- ANSI/BHMA A156.2 — Bored locks
- ANSI/BHMA A156.3 — Exit devices
- ANSI/BHMA A156.4 — Door closers
- ANSI/BHMA A156.13 — Mortise locks
- ANSI/BHMA A156.18 — Materials and finishes (also defines the 600-series finish codes like `US26D` / `626`)

## Finish codes

Hardware finishes are usually noted with the BHMA 600-series number AND/OR the older US-prefix code:

| BHMA | US code | Description |
|------|---------|-------------|
| `605` | `US3`   | Bright brass |
| `606` | `US4`   | Satin brass |
| `612` | `US10`  | Satin bronze |
| `613` | `US10B` | Oil-rubbed bronze |
| `622` | `US19`  | Flat black |
| `626` | `US26D` | Satin chrome (most common in NA commercial) |
| `630` | `US32D` | Satin stainless steel |

If a hardware-set definition cites a finish like `626 / US26D`, that is internally consistent (same finish, two codes).

## Reference

- CSI MasterFormat 2020, Division 08 — Openings (08 71 00 Door Hardware, 08 74 00 Access Control Hardware).
- ANSI/BHMA A156 series (American National Standards Institute / Builders Hardware Manufacturers Association).
- Door and Hardware Institute (DHI) — *Hardware for Buildings* training materials.
