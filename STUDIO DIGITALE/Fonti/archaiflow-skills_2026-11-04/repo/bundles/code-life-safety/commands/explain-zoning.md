---
title: Explain Zoning
summary: Put a zoning clause in plain English for your site
discipline: code-life-safety
tags: ["Pre-Design", "Compliance"]
description: Interpret a zoning clause for a specific North American project site (plain English, with §-citation)
argument-hint: <jurisdiction-or-zr-citation>
---

# Explain Zoning

Interpret a zoning clause from a North American jurisdiction's Zoning Resolution / Zoning Code in plain English, applied to a specific project site. Output is an inline explanation — not a worksheet — with verbatim §-citation and practical implications. For a full zoning analysis cover-sheet block, use the `zoning-summary` skill instead.

## Input you need

Before interpreting, gather:

- **Jurisdiction** — name a specific NA AHJ. Examples: `NYC DOB / NYC City Planning`, `LADBS / LA City Planning`, `San Francisco Planning`, `Portland BDS`, `Toronto City Planning`, `Vancouver Planning`. **Never** "the city" or "the AHJ" generically.
- **Zoning code citation** — the exact section the user wants interpreted, paired with the clause text if the user has it. Examples: `NYC ZR §23-145`, `LAMC §12.21.A.4`, `SF Planning Code §134`, `Toronto Zoning By-law 569-2013 §10.20.40.10`.
- **Clause text** — paste the literal text of the section. If the user does not have it, route to the appropriate retrieval tool first:
  - For NYC, use the `nyc-zoning-lookup` skill.
  - For other jurisdictions, paste the clause text from the adopted zoning code.
  - Do not invent the clause text from training data.
- **Site context** — the project facts the user wants the clause applied to. Required:
  - Zoning district (e.g., `R8B`, `M1-2/R6A`, `C-2-1`, `CR-2.5/2.0`).
  - Use group / proposed use (e.g., `Use Group 6 retail`, `multi-family residential`, `light manufacturing`).
  - Lot dimensions and area when the clause is dimensional (FAR, setback, height, lot coverage).
  - Special district overlay if any (e.g., `Special Hudson Yards District`, `Coastal Zone`, `Historic District`).
- **Specific question** — what the user actually wants to know. Examples: "Does this trigger a sky exposure plane?", "Can I count this as community facility FAR?", "Does the rear yard requirement apply on a corner lot?"

If any required input is missing, list the gap and stop. Do not interpret a clause without its text.

## Output structure

Produce a single Markdown response in this layout:

```markdown
# Explain Zoning — [Jurisdiction §X-XX]

**Jurisdiction:** [NYC DOB / NYC City Planning / LADBS / etc.]
**Citation:** [§X-XX or §X.Y.Z verbatim from the source]
**Project site:** [Zoning district, use group, key dimensions]
**Question:** [the user's specific question]

---

## Clause (verbatim)

> [Paste the literal clause text from the user's input or retrieval tool, formatted as a blockquote. Do not paraphrase here.]

— [Source: NYC ZR §X-XX / LAMC §X.Y / etc.]

## Plain-English meaning

[2–4 sentences. What the clause requires, prohibits, or permits, in everyday language. Cite the §-number every time you make a claim about what the code says.]

## How it applies to this project

[2–4 sentences specific to the user's site. Use the user-supplied lot dimensions, district, and use group. Show the math when the clause is dimensional (FAR × lot area = max ZFA, setback × frontage, etc.).]

## AHJ flags

- [Bullet — jurisdiction-specific quirks: NYC DOB BIS interpretation, NYC CPC special permits, SF Planning discretionary review, LADBS zoning administrator interpretations, Toronto Committee of Adjustment minor variance, etc.]
- [Bullet — special district overlay if applicable: Special Hudson Yards District, Coastal Zone, Historic District.]
- [Bullet — recent amendments or proposed amendments the user should verify before relying on this read.]

## Caveats

- This interpretation is based **only** on the clause text the user provided or that was retrieved verbatim. It does not incorporate cross-references the clause may invoke.
- [Bullet — any cross-referenced sections the user should also pull (e.g., "§X-XX defines 'open area' which controls the lot coverage calc here").]
- Zoning interpretation is jurisdictional. For binding determinations, route through the jurisdiction's pre-determination process — `NYC CPC` pre-cert, `LADBS ZA` determination, `SF Planning` Letter of Determination, `Toronto Committee of Adjustment` preliminary zoning review, `Vancouver Planning` zoning interpretation request.
```

## NA AEC conventions (enforce)

- **English only.** No Hangul anywhere.
- **Imperial-first** units (`ft`, `in`, `sf`, `acres`); metric in parens only when useful.
- **Jurisdictions** — name a specific NA AHJ (`NYC DOB`, `NYC City Planning`, `LADBS`, `San Francisco Planning`, `Portland BDS`, `Toronto City Planning`, `Vancouver Planning`). **Never** "the city" or "the AHJ".
- **Codes** — cite the actual NA zoning code: `NYC ZR §X-XX`, `LAMC §X.Y`, `SF Planning Code §X`, `Toronto Zoning By-law 569-2013`, `Vancouver Zoning By-law`. **Never** KBC, KS, BS, EN, JIS, or generic "the zoning code".
- **Floor labels** — `Level 3`, `L3`, or `3rd floor`. **Never** `3F`.
- **Use groups** — name the jurisdiction's actual classification (NYC `Use Group 1–18`, LA `Q-conditions`, SF `NCD overlay`, Toronto `Mixed Use Areas`). Do not invent generic categories.
- **Cost / FAR figures** — when the clause is dimensional, show the math step-by-step. Do not assert a final number without showing how it was derived from the clause text + the user's site inputs.

## Constraints

- Do not invent the clause text. If the user has not pasted the section text and did not route through `nyc-zoning-lookup` first, stop and request the verbatim text.
- Do not invent §-numbers. Cite only what appears in the user's input or the retrieved text.
- Do not provide a "binding" interpretation. Zoning is jurisdictional and final reads come from the named planning authority (NYC CPC, LADBS ZA, SF Planning, Toronto Committee of Adjustment, Vancouver Planning) — flag this in the Caveats section every time.
- This command coexists with the `zoning-summary` skill. If the user wants a full cover-sheet zoning block (lot, district, FAR, setbacks, height, parking, accessory uses, special permits), redirect to `zoning-summary` rather than padding this command's output.
- Markdown only. This is an inline interpretation, not a transmittal document — no Word / PDF output and no `aec-doc-gen` dependency.

## Workflow

1. Echo back what was parsed: jurisdiction, §-citation, district, use group, question. One line.
2. If the clause text is missing, list the gap and stop. Suggest `nyc-zoning-lookup` (NYC) or a paste of the clause text (other jurisdictions).
3. If site context is missing for a dimensional clause (FAR / setback / height), ask only for the dimensions actually needed by the clause — not the full zoning analysis.
4. Produce the full Markdown response in one shot.
5. After the response, list any cross-referenced §-numbers the user should pull next (e.g., "§X-XX defines 'lot coverage' — pull that next if you want a final number").
