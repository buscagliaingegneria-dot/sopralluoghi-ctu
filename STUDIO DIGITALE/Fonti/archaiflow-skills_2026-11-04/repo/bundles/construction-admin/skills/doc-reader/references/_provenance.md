# Provenance — Doc Reader References

## Primary sources

**CSI MasterFormat 2020**
- Publisher: Construction Specifications Institute (CSI)
- Edition: **2020** (current)
- Public information: https://www.csiresources.org/standards/masterformat
- Reference: 6-digit section numbering convention (Division 03 Concrete, 08 Openings, 09 Finishes, etc.)

**Building Codes** (IBC, IRC, IECC, NFPA, ADA, ICC A117.1, ASCE 7)
- Publishers: ICC (IBC, IRC, IECC, A117.1), NFPA (NFPA standards), DOJ (ADA), ASCE (ASCE 7)
- Public access: ICC Digital Codes (https://codes.iccsafe.org/), NFPA LiNK, DOJ/ADA.gov, ASCE Library
- Reference convention: §X.Y.Z chapter.section.subsection citations

**AIA Contract Documents**
- Publisher: American Institute of Architects
- Editions referenced: B101-2017 (Owner-Architect), A201-2017 (General Conditions), C401-2017 (Architect-Consultant), G-series administrative forms (G701, G702, G704, G707, G710, G714, G807)
- Public information: https://www.aiacontracts.com
- Reference convention: AIA section + paragraph (e.g. AIA A201-2017 §3.10.1)

## Coverage of this skill

| Reference file | Covers |
|----------------|--------|
| `document-types.md` | Recognition signals for 5 non-drawing AEC PDF types (spec / code / contract / report / AHJ letter) + typical user requests per type |
| `read-patterns.md` | User-intent → handling-pattern mapping; delegation rules to other archtmpl skills (`leed-tracker`, `ada-tracker`, `client-translator`, etc.) |

**Out of bundled scope** (refer to authoritative sources):

- **Verbatim CSI MasterFormat 2020 section list** — the section numbering convention is bundled, but the full title list is not. For unfamiliar sections, the user must consult CSI MasterFormat directly.
- **Verbatim code text** — codes are licensed; this skill quotes from the user's own document, not from a bundled code library.
- **AIA contract text** — AIA contracts are copyrighted by AIA; this skill quotes from the user's own contract PDF, not from a bundled AIA library.
- **Drawing PDFs** — use `drawing-reader`.
- **Foreign / non-NA standards** (BS, EU, JIS, KS) — NA AEC focus only.

## Verification status

- **Last verified against CSI / ICC / AIA conventions**: 2026-05-08
- **Update trigger**: When CSI publishes MasterFormat 2025+, when ICC publishes new code editions, or when AIA revises contract documents (most recently 2017; next major revision expected 2027).

## How to verify

1. Compare CSI section recognition signals in `document-types.md` against CSI MasterFormat 2020 published guide.
2. Compare AIA document codes (B101-2017, A201-2017, etc.) against current AIA Contract Documents catalog.
3. Compare IBC chapter / section reference syntax (`§X.Y.Z`) against ICC published code text.
4. If conventions differ, file an issue against `archtmpl`.

## Version pin warning

Document-type conventions (CSI / ICC / AIA) are stable at decade-scale, but always re-verify when:
- CSI publishes a new MasterFormat edition,
- ICC publishes new code year (IBC / IRC / IECC),
- AIA revises contract documents,
- A jurisdiction (e.g. NYC DOB, CA HCAI) issues a custom contract or code amendment that changes naming.

Update the **Last verified** date above on each verification. That date is the record. This line used to name a `Version` and a `Last Verified` property in a Notion database; that database was removed on 2026-07-28 and this file is now the only place the date lives.
