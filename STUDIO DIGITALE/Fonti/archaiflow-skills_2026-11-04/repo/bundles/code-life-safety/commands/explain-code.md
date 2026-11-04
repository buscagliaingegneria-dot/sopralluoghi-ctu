---
title: Explain Code
summary: Put a code section in plain English
discipline: code-life-safety
tags: ["Compliance", "Construction Admin"]
description: Interpret an IBC/IECC/NFPA/ADA section in plain English with §-level citation and jurisdictional amendment flags
argument-hint: <code-section-or-paste>
---

# Explain Code

Interpret a single code section — paste the text or cite the §, get plain-English meaning plus jurisdictional amendment flags. Output is an inline interpretation with §-level citation. For a multi-section compliance audit use the `code-compliance-review` skill.

## Input you need

Before interpreting, gather:

- **Code + edition** — exact code and adopted edition:
  - **IBC** — `IBC 2024`, `IBC 2021`, `IBC 2018`. Adopted edition varies by jurisdiction — confirm with the AHJ.
  - **IECC** — `IECC 2024`, `IECC 2021`, `IECC 2018`. Climate-zone aware.
  - **NFPA** — `NFPA 101 2024` (Life Safety), `NFPA 1 2024` (Fire Code), `NFPA 13 2025` (Sprinklers), `NFPA 72 2025` (Fire Alarm).
  - **ADA** — `2010 ADA Standards for Accessible Design`. Companion: `ANSI A117.1-2017`. Some states overlay (`CA Title 24 Part 2 Ch. 11B` is stricter on several clauses).
  - **IRC** — `IRC 2024` for 1- and 2-family dwellings and townhouses.
  - **NBC (Canada)** — `NBC 2020` plus provincial code (`OBC 2024`, `BCBC 2024`, `Quebec Construction Code Ch. I`).
- **Section reference** — `§X.Y.Z` form: `IBC 2024 §1006.3.4` (egress from stories), `IECC 2024 §C402.1.4` (R-value alternative), `NFPA 101 2024 §7.2.1.6` (door egress), `2010 ADA §404.2.4` (door maneuvering clearance).
- **Code text** — provide one of:
  - A paste of the section text (preferred — exact wording matters).
  - The § + edition, with the code PDF indexed in a local RAG; retrieve the section from the index, then interpret.
  - Do not paraphrase or reconstruct code text from memory across editions.
- **Jurisdiction** — name a specific NA AHJ when amendments matter: `NYC DOB`, `FDNY`, `LADBS`, `DSA`, `CA HCAI`, `Toronto Building`, `Boston ISD`, `Chicago DOB`, `Houston Public Works`, `Miami-Dade RER`, `GSA`, `USACE`. Many jurisdictions amend the I-code base (NYC has its own `NYC BC` overlay; California publishes `CBC / CMC / CEC / CRC`; Florida publishes `FBC`).
- **Project context** — occupancy group (`B`, `R-2`, `A-3`, `E`, `I-2`, `S-1`), construction type (`I-A` … `V-B`), height and area, sprinklered status, and existing-vs-new. The same § often reads differently across these dimensions.
- **Specific question** — what the user wants to know. Examples: "Does this require a 1-hour rated corridor?", "Is travel distance 200 ft or 250 ft for B occupancy?", "What triggers an area of refuge?"

If any required input is missing, list the gap and stop. Do not interpret a § without seeing the actual code text.

## Output structure

Produce a single Markdown response in this layout:

```markdown
# Explain Code — [Code §, plain title]

**Code:** [IBC 2024 / IECC 2024 / NFPA 101 2024 / 2010 ADA / NBC 2020]
**Section:** [§1006.3.4 — Egress from stories or occupied roofs]
**Jurisdiction:** [NYC DOB / LADBS / DSA / CA HCAI / Toronto Building / etc.]
**Occupancy / Type:** [B occupancy / Type II-B / sprinklered / 4 stories / 50 ft]
**Question:** [the user's specific question]

---

## What the section says (literal)

> [Verbatim quote of the operative language. If the section has numbered exceptions, list them as a sub-bullet.]

(IBC 2024 §1006.3.4)

## Plain-English meaning

[3–5 sentences. What the section requires, when it applies, what triggers the requirement. Use concrete examples sized to the project context. Translate code-speak ("means of egress", "in accordance with") into builder language without losing precision.]

## How it applies here

- [Bullet — apply to the project context. e.g., "For a B-occupancy 3-story sprinklered building, this means two exits from L3 are required because the occupant load on that floor exceeds 30."]
- [Bullet — adjacent sections that interact. e.g., "Cross-check IBC 2024 §1017 (travel distance) and §1020 (corridors) — the same exit count drives all three."]
- [Bullet — climate / sprinkler / occupancy condition that flips the answer.]

## Jurisdictional amendments to verify

- **[Specific AHJ]** — [Known local amendment. e.g., "NYC BC §1006 modifies the IBC base table — verify against the latest NYC DOB code revision before relying on the I-code answer."]
- **State / provincial layer** — [If applicable. e.g., "California amends to 2022 CBC §1006 with stricter limits in I-occupancy — verify with DSA for K-12 or CA HCAI for hospitals."]
- **Federal overlay** — [`GSA P-100`, `USACE UFC 3-600-01`, `VA Design Manual`, `FEMA P-2055` if the project is federally regulated.]
- If no jurisdiction-specific amendment is known, state that explicitly. Do not guess.

## Cross-references

- [Bullet — related § to pull next. e.g., "IBC 2024 §1004 (occupant load) — the trigger for §1006."]
- [Bullet — referenced standards. e.g., "NFPA 13 §8.15 referenced for sprinkler protection of the assembly."]
- [Bullet — companion code. e.g., "2010 ADA §404.2 governs door clearance; verify against IBC 2024 §1010 for egress door hardware."]

## Caveats

- This is an interpretation aid, not a code determination. The Architect of Record's stamped opinion governs, not this command. For binding interpretation, file the jurisdiction-specific clarification process — NYC DOB Code Determination, LADBS Information Bulletin, DSA Interpretation of Regulations, or equivalent — or engage a code consultant.
- Code editions and amendments change. Verify which edition the jurisdiction has adopted; many adopt 1–2 cycles behind ICC publication.
- For sweeps across multiple § use the `code-compliance-review` skill — this command does single-§ interpretation only.
- If the code text was not pasted, ask for a paste or retrieve verbatim from a locally indexed PDF. Do not interpret from memory.
```

## NA AEC conventions (enforce)

- **English only.** No Hangul anywhere.
- **Imperial-first** units (`ft`, `in`, `sf`, `°F`, `psf`, `Btu`, R-values). Metric in parens only when useful. Do not lead with `mm`, `m²`, `°C`, `W/m²K`. Use **R-values**, never metric U-values.
- **Codes cited** — IBC / IRC / IECC / NFPA / 2010 ADA / ANSI A117.1 / ASCE 7 / ASHRAE / NBC (Canada) and provincial codes. Never `KBC`, `KS`, `EN`, `BS`, `JIS`, `DIN` — out of catalog scope.
- **Section format** — always code + edition + `§X.Y.Z`: `IBC 2024 §1006.3.4`, `IECC 2024 §C402.1.4`, `NFPA 101 2024 §7.2.1.6`, `2010 ADA §404.2.4`. Never "section 1006" generically.
- **AHJs** — name specifically: `NYC DOB`, `FDNY`, `LADBS`, `DSA`, `CA HCAI`, `Toronto Building`, `Chicago DOB`, `Houston Public Works`, `Miami-Dade RER`, `GSA`, `USACE`. Never `the AHJ`, `the city`, or `local authority` generically.
- **Floor labels** — `Level 3`, `L3`, or `3rd floor`. Never `3F`.
- **Roles** — `Architect of Record (AOR)`, `Engineer of Record (EOR)`, `Owner`, `Owner's Representative`, `Code Consultant`, `Expediter` (NYC). Never use `Director` as a project role.
- **Climate zones** for IECC questions — pair with `climate-zone-mapper`, or cite the zone explicitly (e.g., `CZ 4A` for NYC, `CZ 3B` for LA, `CZ 6A` for Toronto, `CZ 2A` for Houston).

## Constraints

- Do not invent code text. If the user did not paste the §, either ask for the paste or retrieve verbatim from a locally indexed PDF. Memorized code text is unreliable across editions.
- Do not invent jurisdictional amendments. If the NYC / California / Toronto overlay on a § is not known, state that — do not fabricate amendment numbers.
- Distinguish **literal code text** (verbatim, blockquoted) from **interpretation** (plain English) — keep them in separate sections.
- Distinguish **base I-code requirement** from **AHJ amendment** — a NYC DOB or DSA answer can flip versus the IBC base.
- Coexists with `code-compliance-review` (multi-§ audit). Redirect there for scope larger than a single §.
- Markdown only. No Word / PDF output, no `aec-doc-gen` dependency.
- Always include the **Caveats** section. Code interpretation without an AOR stamp is non-binding by definition.

## Workflow

1. Echo back what was parsed: code + edition, §, jurisdiction, occupancy + type, question. One line.
2. If the code text is missing, list the gap and stop. Suggest a paste, a WebFetch, or retrieval from a locally indexed PDF.
3. If the jurisdiction is missing on a question where amendments matter (egress, sprinkler triggers, energy compliance, occupancy classification), ask before interpreting.
4. Produce the full Markdown response in one shot.
5. After the response, list cross-referenced § the user should pull next (e.g., "For occupant load, pull IBC 2024 §1004 — re-run `/explain-code`").
