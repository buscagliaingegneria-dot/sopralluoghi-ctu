# Provenance — `nyc-zoning-lookup` reference bundle

## Source pinned

- **Document:** New York City Zoning Resolution
- **Version:** Post-2024 effective text, with the **City of Yes** amendments incorporated (Housing Opportunity, Carbon Neutrality, Economic Opportunity).
- **Authoritative source URL:** https://zoningresolution.planning.nyc.gov
- **Combined PDF used by this skill:** `https://zoningresolution.planning.nyc.gov/sites/default/files/article/Zoning%20Resolution%20Complete.pdf` (cached at `~/.archtmpl/pdfs/nyc-zoning/zr-complete.pdf`)
- **Last verified by skill author:** 2026-05-09

The published combined ZR PDF on `zoningresolution.planning.nyc.gov` is the source of truth. The DCP also publishes the per-Article HTML and PDF builds at the same domain — those are equivalent in content but paginated differently. Page numbers in this skill always refer to the combined PDF cached locally.

## Era policy

- **Default for new work:** post-2024 numbering (City of Yes amendments).
- **Cross-reference for legacy permits:** pre-2024 numbering preserved inline where renumbering occurred. A user working on a permit application filed before the amendment effective date may be reading a document using pre-2024 section numbers, and quoting a post-2024 section number back to them will be confusing.
- **When the era is unclear from the user's question:** ask. Do not guess.

## Verified migrations (post-2024 ← pre-2024)

These migrations are documented in `references/zr_structure.md` and confirmed against the published ZR text:

| Topic | Pre-2024 | Post-2024 |
|---|---|---|
| R1–R5 floor area regulations (FAR) | within `§23-14X` range | `§23-21` |
| R6–R12 floor area regulations (FAR) | within `§23-14X` range (commonly cited example: `§23-145`) | `§23-22` |

Other Article II §23-XX renumberings exist (height-factor / Quality Housing alternatives, yards, sky-exposure plane) — not enumerated here because the bundle author has not done a row-by-row cross-walk against the City of Yes amendment text. Any §23-XX citation outside the two rows above must be verified against the live PDF before being quoted.

## Sections marked `[verify]` in the bundle

The following section numbers appear in `citation_format.md` and `zr_structure.md` with a `[verify post-2024]` flag, meaning the bundle author did **not** confirm whether the section number changed under City of Yes. Do not quote them to the user without first reading the live PDF and confirming the current number:

- `§32-15` (commercial Use Group regulations) — Use Group numbering itself was revised under City of Yes Economic Opportunity, so both the section number and the Use Group content need verification.
- `§42-13` (manufacturing use regulations)
- `§74-71` (special permits)
- `§93-21` (Special Hudson Yards District)
- `§98-22` (Special West Chelsea District)
- `§81-21` (Special Midtown District)
- `§22` and `§22-3X` (residential Use Groups, residence-district signs)
- `§23-15X` (Quality Housing Program — falls in the renumbered §23-1X / §23-2X range)
- `§23-4X` (residence yards)
- `§23-6X` (residence height limits / sky exposure plane)
- `§23-90X` (Mandatory Inclusionary Housing)
- `§25`, `§36`, `§44` chapters (accessory parking — Chapter locations unchanged but contents materially revised by City of Yes Housing Opportunity)
- `§32-6X` (commercial signs)
- `§33-12X`, `§43-12X` (commercial / manufacturing FAR)
- `§33-43`, `§43-43` (commercial / manufacturing height)
- `§33-2X`, `§43-2X` (commercial / manufacturing yards)
- `§36-6X`, `§44-6X` (loading berths)
- `§73`, `§74`, `§72`, `§75` (variances, special permits, modifications — Article VII)

## Verification protocol

Every section number cited to a user must be verified against the actual current ZR PDF before being included in an answer:

1. **Re-read `outline.md`** (the cached section-to-page map) before answering each question. The outline is built from the same combined PDF and reflects whatever era was current when the cache was built — check `outline.md`'s `Last cached` header.
2. **Read the targeted page range** with the Read tool. The `§AB-CDE` heading on the page is the authoritative section number.
3. **Quote only what is on the page.** Do not retype a section number from `citation_format.md` or `zr_structure.md` without confirming it appears on the page you read.
4. **If the live PDF disagrees with the bundle**, the live PDF wins. The bundle is orientation, not source. Note the discrepancy in your answer and offer to update the bundle.
5. **If `outline.md`'s `Last cached` is older than 90 days**, offer to re-cache before answering — the ZR is amended frequently.

## Bundle update protocol

When a `[verify post-2024]` section is confirmed (or refuted) against the live PDF:

1. Update the relevant entry in `citation_format.md` and / or `zr_structure.md` — replace `[verify post-2024]` with the confirmed number, and add the pre-2024 number in parens if it changed.
2. Add a row to the **Verified migrations** table above with the date of verification.
3. `SKILL.md` does not need editing for reference-file fixes — only when `SKILL.md` itself uses an outdated section number in an example. (This step used to name a Notion page body as the source of truth for `SKILL.md`. That database was removed on 2026-07-28; `SKILL.md` in this folder is the source.)

## Out-of-scope

This bundle covers the NYC ZR only. Related but separate documents:

- **NYC Building Code** (Title 28 of the NYC Administrative Code) — different document, different lookup skill.
- **NYC Multiple Dwelling Law (MDL)** — state law, different document.
- **NYC Housing Maintenance Code** — different document.
- **NYC Energy Conservation Code (NYCECC)** — different document.
- **DCP zoning maps / ZoLa** — current zoning of a specific lot is a GIS lookup, not a ZR text question.

Do not answer questions about those documents from this skill.
