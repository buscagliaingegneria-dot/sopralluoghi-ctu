# Provenance — spec-review bundle

This file pins the editions and authoritative sources for content bundled with the `spec-review` skill, and documents the design decision to keep one expected file out of the bundle. Update the "last verified" dates when the bundled references are refreshed against publisher sources.

---

## Bundled references

### `references/csi_masterformat_2020_index.md`

- **Standard:** CSI MasterFormat, 2020 Edition.
- **Publisher:** Construction Specifications Institute (CSI).
- **Authoritative source:** csiresources.org/standards/masterformat.
- **Last verified against publisher:** 2026-05-09.
- **Scope of bundling:** level-1 division titles (00 Procurement through 49 Power Generation) and a curated set of common level-2 section titles. Level-3 / level-4 sub-section titles (e.g., 08 41 13.16) are intentionally not enumerated — they drift across editions and would be a recall-vs-source-of-truth risk.
- **Refresh trigger:** when CSI publishes a new MasterFormat edition (announced at csinet.org / csiresources.org), or every 2 years on a calendar reminder, whichever is sooner.

### `references/spec_axes.md`

- **Framework:** internal to this skill — eight-axis spec audit framework derived from CSI SectionFormat / PageFormat conventions and AIA B101-2017 §3.4.5 (architect's specification responsibility).
- **Aligned standards (cited at top of file):** CSI MasterFormat 2020, CSI SectionFormat / PageFormat, AIA MasterSpec / SpecLink / ARCAT-derived office masters, ConsensusDOCS, agency masters (UFGS for USACE, P-100 for GSA, OSP for CA HCAI, NYC SCA spec).
- **AIA contract reference:** AIA B101-2017, Standard Form of Agreement Between Owner and Architect, §3.4.5 (specifications). Verify the contract on the project — some projects use AIA C401, B132, or owner-supplied agreements that re-allocate spec responsibility.
- **AIA MasterSpec:** AIA MasterSpec is published by Deltek; the platform issues content updates rolling. The skill does not pin a specific MasterSpec release — it assumes whatever release the project's spec writer has licensed. Treat references in `spec_axes.md` to MasterSpec as conventions, not pinned editions.
- **Last verified:** 2026-05-09.

### `assets/spec-review-template.md`

- Internal template — no external standard pinned. References AIA / CSI / publisher conventions named above.

---

## Intentionally NOT bundled

### `reference_standards_currency_2026.md`

`SKILL.md` (line 159, "Resources" section) lists `references/reference_standards_currency_2026.md` as a resource and the bootstrap step for axis 5 (reference-standard currency). **This file is intentionally not present in the bundle.**

**Why this file is omitted:**

- Standards (ASTM, ACI, ASHRAE, NFPA, UL, AISC, ASCE, AAMA, ANSI, ICC) revise on rolling cycles — typically 3 to 10 years per standard, but the cadence is per-publisher and not synchronized. A bundled "current edition" lookup table is fresh on the day it is written and progressively wrong from that day forward.
- A stale bundled lookup is *worse* than no lookup — it creates the appearance of a verified citation while injecting outdated edition years into review findings. A finding like "spec cites ASTM C39-21; current edition is C39-25" carries the implicit promise that "C39-25" was checked. If "C39-25" came from a bundled table that was last refreshed 18 months ago, the promise is false and the next reviewer downstream cannot tell.
- This is the well-tracker pattern (see `feedback_standards_verification.md` in the user's auto-memory): a bundled scorecard / lookup that recalled values without row-by-row diff against publisher source produced wrong values for every concept. The 2026-05-09 incident is the rule, not the exception.

**Correct pattern (what the skill's Step 3, axis 5 should do):**

For each standard cited in the spec section under review, verify the current edition at review time against the publisher:

- ASTM → astm.org (search by designation; product page shows current designation with year)
- ACI → concrete.org/store
- ASHRAE → ashrae.org/technical-resources/standards-and-guidelines
- NFPA → nfpa.org/codes-and-standards
- UL → shopulstandards.com (or ulstandards.ul.com)
- AISC → aisc.org/publications
- ASCE → asce.org/publications-and-news/asce-7
- AAMA / FGIA → fgiaonline.org/store
- ANSI → ansi.org / standard-setter (ANSI is a federation; the actual publisher varies — Z535 from NEMA, A117.1 from ICC, etc.)
- ICC → iccsafe.org/products-and-services

Record the verification source and access date in the review's "Reference-standard updates" table (the template column is `Verified via`). This makes the citation auditable and the next reviewer can confirm or refute.

**If a standard's current edition is not easily verifiable:** flag in the finding ("ASTM Cxxx — could not verify current edition at review time; recommend the spec writer confirm with ASTM"). Do not guess.

### `code_editions_by_jurisdiction.md`

Mentioned in passing in the deleted standards-currency file ("see `code_editions_by_jurisdiction.md` in `code-compliance-review/references/`"). Not bundled with `spec-review` either — code adoption by jurisdiction (which IBC year a state has adopted, with what local amendments) drifts on the AHJ's own schedule and is the responsibility of the `code-compliance-review` skill, not `spec-review`. If `code-compliance-review` exists in the catalog and bundles a jurisdiction table, that table has the same staleness risk and should be similarly verified at review time.

---

## SKILL.md drift

`SKILL.md` in this folder is the source. Edit it directly.

This section used to say that local edits were overwritten by the next Notion sync, so the items below were logged here to be fixed in Notion instead. That database was removed on 2026-07-28 and nothing overwrites `SKILL.md` any more. Status re-checked 2026-08-11:

- **Items 1 through 4 are done.** `SKILL.md` now points at `csi_masterformat_2020_index.md` (lines 38, 92, 172), `reference_standards_currency_2026.md` no longer appears in it, and the "(the 2018 update titling that holds through 2026)" parenthetical was dropped from line 172 on 2026-08-11 because it was not a CSI-published claim.
- **Item 5 is open** and was never blocking.

None of these stop the skill from running. The original text of each is kept below.

1. **Line 69 (Step 2) — file name drift.** SKILL.md says: *"Pull MasterFormat division titles from `references/csi_masterformat_2018_index.md` for completeness checking."* The bundled file is `csi_masterformat_2020_index.md` (renamed 2026-05-09). The "2018" name was incorrect because the current published edition is MasterFormat 2020; the 2018 reference appears to be a confused reference to a 2018 *update* of the 2020-cycle titling. Fix: change the SKILL.md filename reference to `csi_masterformat_2020_index.md`.

2. **Line 158 (Resources) — same file name drift.** SKILL.md lists: *"`references/csi_masterformat_2018_index.md` — Division and major-section titles per MasterFormat 2020 (the 2018 update titling that holds through 2026), for completeness checking."* The descriptor itself says "MasterFormat 2020" while the filename says "2018" — internally inconsistent. Fix: rename to `csi_masterformat_2020_index.md` and drop the parenthetical "(the 2018 update titling that holds through 2026)" — that phrasing is not a CSI-published claim and risks fabrication.

3. **Line 159 (Resources) — non-existent file.** SKILL.md lists: *"`references/reference_standards_currency_2026.md` — currency check on commonly-cited ASTM / ANSI / NFPA / ASHRAE / AISC / ACI / ASCE / ICC standards as of 2026 Q2; flags standards revised since the typical office-master baseline."* This file is **intentionally not bundled** (see above). Fix: remove this bullet from the Resources list, or replace with a pointer to verifying standards at review time per publisher (see "Correct pattern" above).

4. **Line 82 (Step 3, axis 5) — same non-existent file.** Same fix: replace *"the year is current per `references/reference_standards_currency_2026.md`"* with *"the year is current per the publisher (ASTM, ACI, ASHRAE, NFPA, UL, etc.) verified at review time"*.

5. **Line 121 (Step 5 example) — primary-axes example.** Minor: the example `--primary-axes "drawing-coordination,reference-standards,opr-alignment"` includes `reference-standards`, which is fine, but the README on the workspace-init script (created by `init_spec_review_workspace.py`) does not enumerate axis tags. Consider adding an "Axis tags" reference list to the index header so reviewers use consistent slugs. Not blocking.

---

Last updated: 2026-05-09.
