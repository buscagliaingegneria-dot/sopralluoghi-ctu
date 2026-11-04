# Provenance — code editions and bundled scope

What this skill is pinned against, what is and isn't bundled, and how to verify before quoting a value in a review.

**Last verified:** 2026-05-09.

---

## Codes pinned (as of last verification)

This skill assumes the user is working under one of the following code bases. State amendments can override any base-code value; the per-jurisdiction lookup lives in `code_editions_by_jurisdiction.md`.

| Code | Edition pinned | Notes |
|---|---|---|
| International Building Code (IBC) | **2021** primary; **2024** noted where it differs | Many AHJs are still on IBC 2021 even though IBC 2024 is published. ICC publishes on a 3-year cycle; transitions are slow. |
| International Fire Code (IFC) | **2021** primary; **2024** noted where it differs | Travels with IBC. |
| International Existing Building Code (IEBC) | 2021 | Use for renovation / change-of-use scope. |
| ICC A117.1 — Accessible & Usable Buildings and Facilities | **2017** | Referenced by IBC Ch. 11. ICC A117.1-2009 is still cited in some legacy AHJ contexts (e.g., older NYC); verify edition. |
| ADA 2010 Standards for Accessible Design (DOJ) | **2010** (effective 2012-03-15) | Federal Title II / III obligations. Distinct from IBC Ch. 11; both can apply. |
| ABA Accessibility Standards (federal-funded buildings) | 2015 update to ABA Standards (USABA) | USACE, GSA, Postal Service, etc. |
| NFPA 101 Life Safety Code | **2021** primary | Required by CMS for Joint Commission–accredited healthcare. AHJ may use instead of or with IBC. |
| NFPA 13 / 13R / 13D (sprinklers) | 2022 | Typical adoption; verify against AHJ-adopted year. |
| NFPA 72 (alarm) | 2022 | |
| NFPA 110 (emergency power) | 2022 | |
| NFPA 99 (healthcare facilities) | 2024 | |
| ASCE 7 (Minimum Design Loads) | **7-22** | Referenced by IBC 2021 (which cites 7-16) and IBC 2024 (which cites 7-22); state amendments vary. |
| IECC (energy) | 2021 primary | Touches life-safety for emergency lighting circuits, not occupancy classification. |
| ASHRAE 90.1 | 2019 / 2022 | Energy alternate path. |
| FGI Guidelines | 2022 | Hospital / outpatient — referenced by many state DOH. |
| California Title 24 Part 2 (CBC) | **2022** primary; **2025** transition note | CBC 2025 effective 2026-01-01 in most jurisdictions; some allow 2022 through a transition window. |
| New York City Building Code (NYC BC) | **2022** | IBC 2018 base + NYC amendments. NYC Energy Conservation Code (NYC ECC) 2020 is the energy companion. |
| Massachusetts State Building Code (780 CMR) | **9th Edition** (IBC 2015 base, rolling updates) | MA Stretch Energy Code overlays. |
| Ontario Building Code (OBC) | **OBC 2024** (NBC 2020 base) | Effective 2024-01-01. |

---

## What this skill bundles

The references in this folder are **orientation aids**, not authoritative tables. They exist to help the analyst frame a question, not to provide values for a code submission.

- `egress_axes.md` — eight-axis framework with sub-criteria, common failure modes, example finding language. Discusses values without quoting per-row table cells as authoritative.
- `ibc_egress_quick_ref.md` — condensed lookup of common occupant-load factors, common-path limits, travel-distance limits, exit-count thresholds. **Each table marked `[verify per IBC ed.]` where the value shifts between 2021 and 2024 or where recall is not high-confidence.** The file's own footer explicitly warns it is not authoritative.
- `code_editions_by_jurisdiction.md` — per-state / per-province code edition lookup as of 2026 Q2.
- `_provenance.md` — this file.

## What this skill deliberately does NOT bundle

- A comprehensive IBC table lookup (Table 1004.5 in full, Table 1006.2.1 in full, Table 1017.2 in full, Table 508.4, Table 716.1(2), Table 716.1(3), Table 1020.2, Table 506.2 height/area, etc.). Bundling such tables from recall is a known anti-pattern (`feedback_standards_verification`): per-row values drift from authoritative source on a multi-year recall horizon, and a tracker / lookup that looks comprehensive will be quoted as if it were authoritative. A condensed quick-ref (with explicit `[verify per IBC ed.]` markers and a non-authoritative warning in the file footer) is acceptable; a full table lookup is not.
- Verbatim code text. Pull verbatim language from the AHJ-adopted PDF.
- AHJ-specific amendments at the row level (NYC LL126, CBC §1505 WUI, NYS amendments). The `code_editions_by_jurisdiction.md` lists which amendment package applies; the analyst must verify the specific amendment value via the AHJ portal or a code-edition PDF in the RAG index.
- Cost / fee / permit-process information. That belongs in a different skill.

## How to verify a value before quoting it in a review

In rough order of reliability:

1. **AHJ portal — the actual adopted code.** ICC Digital Codes (`codes.iccsafe.org`) hosts the IBC base text and the published state amendments. NYC DOB `BIS` / `DOB NOW`, FDNY Code on `nyc.gov/fdny`, CA HCAI on `hcai.ca.gov`, DSA on `dgs.ca.gov/DSA`, Mass.gov for 780 CMR, etc.
2. **A local RAG index over the AHJ-adopted PDF.** If the project's IBC + state-amendment PDFs are indexed, query for the section and quote the returned text. Always confirm the edition the chunk is from.
3. **Hard-copy / licensed PDF of the adopted code.** ICC-published or AHJ-published. Avoid third-party summaries for verbatim quoting.
4. **Manufacturer / standards-org documentation** for product-specific compliance (e.g., a fire-rated assembly UL listing, an A117.1 compliant grab-bar fixture cut sheet).

Do **not** rely on the references in this skill folder for the value that goes in the review. Use them to know which section to look up; then look it up.

## Audit / refresh cadence

Recommend re-verifying this provenance and the per-state lookup at the start of each major IBC cycle (2027 review for IBC 2027 publication) and quarterly during state transition periods (CBC 2025 transition, NYC BC 2022 → next, OBC 2024 → next). Mark the date at the top of this file when re-verifying.
