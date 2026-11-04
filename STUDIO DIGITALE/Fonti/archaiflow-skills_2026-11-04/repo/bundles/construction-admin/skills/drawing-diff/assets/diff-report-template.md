# Drawing Diff — {{OLD_LABEL}} to {{NEW_LABEL}}

**Old file:** {{OLD_FILE}}
**New file:** {{NEW_FILE}}
**Compared:** {{DATE}}
**Sheets:** {{N_COMPARED}} compared, {{N_CHANGED}} changed, {{N_ADDED}} added, {{N_REMOVED}} removed

---

## Read this first

{{UNCLOUDED_SUMMARY — the changes carrying no revision cloud, by sheet, one line
each. If there are none, say "every detected change is clouded" rather than
leaving this empty. This section is why the comparison was run.}}

---

## Sheets added and removed

{{ADDED_REMOVED — sheet number and name for each, or "none". A sheet that
disappeared between revisions is a finding, not a formatting detail.}}

---

## {{SHEET_NUMBER}} — {{SHEET_NAME}}

**Revision block says:** {{REV_BLOCK_CLAIM}}
**Engines:** {{ENGINES_RUN — e.g. "text + overlay" / "overlay only (scan)"}}

### Changed, not clouded

{{FINDINGS_UNCLOUDED — location, what changed, both values. Empty means none
were found, and say that.}}

### Text changes

| Location | Was | Now |
|----------|-----|-----|
| {{WHERE}} | {{WAS}} | {{NOW}} |

{{ADDED_REMOVED_TEXT — notes and tags that appeared or disappeared, with where.}}

### Geometry changes

{{GEOMETRY_FINDINGS — one line per region: where it is on the sheet, what moved,
and the crop filenames behind the reading. Say "unclear from the crop" where it
is unclear rather than guessing.}}

### Clouded, nothing detected

{{STALE_CLOUDS — clouds with no change inside them, usually left over from the
previous revision. Or "none".}}

<!-- Repeat the block above per sheet. Sheets with changes first. -->

---

## Sheets with no detected change

{{UNCHANGED_LIST — sheet numbers only. Qualify with the engine that ran: a scan
with no text engine is not the same as a clean vector sheet.}}

---

## Method and limits

{{METHOD_NOTE — paste from references/diff_methods.md and edit to match this
run: which engines ran, which sheets skipped one, which sheets failed to align,
whether any region list was capped.}}
