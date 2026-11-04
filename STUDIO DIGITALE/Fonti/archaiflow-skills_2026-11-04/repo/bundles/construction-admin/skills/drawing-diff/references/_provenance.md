# Provenance — Drawing Diff References

## Primary sources

**US National CAD Standard (NCS) v6**
- Publisher: National Institute of Building Sciences (NIBS), in coordination with AIA + CSI
- Edition: **v6** (current as of 2026-08-12)
- Public information: https://www.nationalcadstandard.org
- Used for one thing only: the shape of a sheet number (discipline designator +
  sheet-type digit + sequence), which is what `match_sheets.py` pattern-matches
  on. Discipline meaning is not interpreted by this skill.

**AIA G-Series**
- Publisher: American Institute of Architects
- Documents referenced: AIA G701 (Change Order), G710 (Supplemental
  Instructions). Named only as the vehicles a re-issue arrives on. This skill
  compares the drawings, not the instrument.

## Coverage of this skill

| Reference file | Covers |
|----------------|--------|
| `diff_methods.md` | What the text engine and the overlay each see and miss, the tolerances behind both, and the methods note every report ends with |

**Out of bundled scope** (refer to authoritative sources):

- **Revision cloud and delta conventions per jurisdiction or office standard.**
  Clouds are read as drawn and compared against detected changes. No rule about
  how a cloud should be shaped or tagged is bundled.
- **Whether a change is acceptable.** Code, clearance, and coordination
  judgement belong to `code-compliance-review`, `design-egress`, `design-stair`, and
  `constructability-review`.
- **Non-NA sheet numbering** (BS 1192 / ISO 19650 field-based names such as
  `PRJ-ZZ-00-DR-A-1001`). The pattern in `match_sheets.py` does not recognise
  these. Pair those sets with `--override` until a profile covers them.
- **Native model comparison** (RVT, IFC, DWG). PDF only.

## Verification status

- **Last verified against NCS v6 + AIA**: 2026-08-12
- **Update trigger**: When NIBS publishes NCS v7, or when the sheet-number
  pattern misses a numbering scheme a user actually has.

## How to verify

1. Run `match_sheets.py` against a real set and check the unreadable count. A
   count above zero on a vector set means the pattern needs widening, not that
   the sheets are bad.
2. Compare the pattern's assumptions against NCS v6's published sheet
   identification system.
3. If conventions differ, file an issue against `archtmpl`.

## Version pin warning

NCS revisions are decade-scale, but the pattern this skill depends on is
narrower than the standard and can be broken by an office numbering scheme long
before NIBS changes anything. Re-verify when:

- A new NCS edition publishes,
- A set arrives whose sheet numbers do not match `SHEET_RE`,
- A jurisdiction or client imposes its own CAD standard.

Update the **Last verified** date above on each verification. That date is the
record.
