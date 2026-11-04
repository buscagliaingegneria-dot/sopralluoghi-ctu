# NYC ZR Citation Format Reference

> **Era note.** Section numbers below reflect the **post-2024 NYC Zoning Resolution** (City of Yes amendments — Housing Opportunity / Carbon Neutrality / Economic Opportunity). Pre-2024 numbers are preserved in parentheses where they differ, for users working on permits filed before the amendment effective date. **Always verify against the current ZR PDF at zoningresolution.planning.nyc.gov before citing** — the references files are orientation only, not a substitute for reading the live document. See `_provenance.md` for the verification protocol.

## Section Numbering Scheme

The NYC Zoning Resolution uses the pattern `§AB-CDE` where:

- `A` (or `AB` for Articles X–XIV) — Article number
- `B` (or following digit) — Chapter within the Article
- `CDE` — Section within the Chapter (typically 2–3 digits)

Examples (post-2024 numbering; pre-2024 in parens where renumbered):

| Citation | Meaning |
|---|---|
| `§11-00` | Article I, Chapter 1, §00 (Title section) |
| `§12-10` | Article I, Chapter 2, §10 (Definitions — the definitions section) |
| `§23-22` (pre-2024: `§23-14X`) | Article II, Chapter 3 — R6–R12 floor area regulations (post-2024 consolidated FAR location) |
| `§23-21` | Article II, Chapter 3 — R1–R5 floor area regulations |
| `§32-15` | Article III, Chapter 2, §15 (Commercial use group regulations) `[verify post-2024]` |
| `§42-13` | Article IV, Chapter 2, §13 (Manufacturing use regulations) `[verify post-2024]` |
| `§74-71` | Article VII, Chapter 4, §71 (Special Permits, with reference to BSA / CPC) `[verify post-2024]` |
| `§93-21` | Article IX, Chapter 3, §21 (Special Hudson Yards District provisions) `[verify post-2024]` |

`[verify post-2024]` means the bundle author did not confirm whether the section number changed under the City of Yes amendments. Read the current ZR PDF and the City of Yes amendment text before citing.

For Articles X–XIV (Special Districts), section numbers continue with two-digit Article prefixes (`§104-XX`, `§142-XX`, etc.).

## Citation Format Convention

Every quoted value must be followed by:

```
— §AB-CDE, p.N
```

Examples:

- `— §23-22, p.N` — single section, single page (post-2024 R6–R12 FAR; was `§23-145` pre-2024)
- `— §23-22(a)(2), p.N` — specific paragraph within a section
- `— §23-22, pp.N–N+2` — multi-page section, full range
- `— §23-22, p.N; §23-32, p.N'` — multiple sources

Use an em dash (`—`) before the citation, not a hyphen.

When citing a section that is materially different between pre-2024 and post-2024 ZR (e.g., R6–R12 FAR), include the pre-2024 number on first reference within an answer:

- `— §23-22, p.N (post-2024; pre-2024: §23-145)`

This helps a user with an older permit application cross-reference the rule.

## Quote-and-Cite Block Format

Every numerical or normative value from the ZR is quoted in a blockquote and immediately followed by its citation on the next line, also inside the quote:

```markdown
> "the maximum floor area ratio shall be 2.43, except as provided in Section 23-15"
>
> — §23-22, p.N (post-2024; pre-2024: §23-145)
```

Keep the quoted text **verbatim** — preserve capitalization, punctuation, and units exactly as printed. If the live ZR PDF uses different language than this example illustrates, the live PDF wins; the example is illustrative.

## Special District Citations

Special District provisions live in Articles VIII–XIV. Cite the District name plus the section:

- `— Special Hudson Yards District, §93-21, p.N` `[verify post-2024]`
- `— Special West Chelsea District, §98-22, p.N` `[verify post-2024]`
- `— Special Midtown District, §81-21, p.N` `[verify post-2024]`

Naming the District alongside the section helps the reader confirm scope, since Special District provisions override the underlying R/C/M district rules. The City of Yes amendments primarily restructured Articles II–IV (base district regulations); Special District section numbers in Articles VIII–XIV may or may not have shifted. Read the current ZR before citing — do not assume the pre-2024 number is still valid.

## Definitions (§12-10)

Term definitions live almost entirely in **§12-10** (Article I, Chapter 2 — Construction of Language and Definitions). The §12-10 location is unchanged across the 2024 amendments, but individual definitions may have been added, revised, or moved within §12-10 — verify before quoting.

When a quoted clause depends on a defined term whose meaning materially affects the answer:

1. Quote the operative clause with its citation.
2. Quote the definition from §12-10 with its citation.
3. Format example:

   > "lot coverage shall not exceed 60 percent of the lot area"
   >
   > — §23-22, p.N (post-2024; pre-2024: §23-145)

   where "lot coverage" is defined as:

   > "that percentage of the lot area which, when viewed directly from above, would be covered by the aggregate of the building areas..."
   >
   > — §12-10, p.N

Skip the definition lookup when the term is unambiguous in plain English (e.g., "feet", "percent").

## Cross-References

When a clause says "as provided in §23-32" or "subject to §23-22", the referenced section is **normative** — its content materially affects the rule being quoted.

Procedure:

1. Identify the cross-reference in the quoted clause.
2. Read the referenced section (one more Read call).
3. Quote both sections in the answer.
4. Do not paraphrase the cross-referenced rule — quote it.

If a clause has 3+ cross-references, list them all and follow the most-restrictive one first.

Cross-references inside the **post-2024 ZR** point to **post-2024 section numbers**. Do not chase a cross-reference to a pre-2024 section number from the live PDF — if you see one, you are reading a stale document.

## Common Citation Errors to Avoid

- **Section without page**: `§23-22` alone is incomplete. Always append `, p.N`.
- **Invented section numbers**: If the targeted pages did not contain the §X-XX needed, expand the read once, then report "not found in [list]". Never guess section numbers.
- **Mixing eras silently**: Quoting `§23-145` from a permit application but reading from the post-2024 PDF (where R6–R12 FAR is `§23-22`) will produce the wrong text. Identify which era the user's question is in. If unclear, ask. The default for new work is post-2024.
- **Wrong document**: Do not confuse with NYC Administrative Code (cited differently, e.g., "NYC Admin. Code §27-XXX"), NYC Building Code (Title 28, cited as "BC §XXXX.X.X"), or Multiple Dwelling Law (cited as "MDL §X").
- **Bare "ZR"**: "Per the ZR" is not a citation. Use `§X-XX, p.N` (the "ZR" prefix is implicit within an answer that has established context).
- **Paraphrased values**: Never round or simplify a FAR (`2.43` is not `~2.4`), a yard depth (`8 feet` is not `~8 ft`), or a use group number.
- **Page numbers from a different print edition**: All page numbers refer to the locally cached `zr-complete.pdf`. If the user asks about a different printing or PDF version, mention the cache date and the source URL.
