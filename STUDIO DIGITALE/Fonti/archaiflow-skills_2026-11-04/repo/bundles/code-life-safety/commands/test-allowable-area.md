---
title: Test Allowable Area
summary: Check a building's allowable area
discipline: code-life-safety
tags: ["Compliance"]
description: Single-building allowable-area gut-check (Tabular base × frontage modifier × sprinkler factor) against IBC Ch. 5 — user pastes or authorizes fetch of operative IBC tables; PASS / FAIL / MARGINAL with explicit attribution. Carries no IBC values internally.
argument-hint: <occupancy> <construction-type> <provided-area-and-stories> [jurisdiction]
---

# Test Allowable Area

Single-building allowable-area gut-check — proposed building area and stories versus the IBC `Ch. 5` allowable area calculation (tabular base × open-frontage modifier × sprinkler factor) — against IBC text the **user supplies**.

**This command does not carry IBC values.** Every limit cited in the output is a verbatim quote from text the user pasted, or text the command fetched from an explicitly-named official URL with the user's authorization.

For a multi-occupancy / mixed-use Ch. 5 audit, use the `code-compliance-review` skill. For a single § interpretation use `/explain-code`.

## Inputs the command needs

1. **Occupancy group** — `IBC` Ch. 3: `A-1` … `S-2`. Mixed-occupancy must use `IBC §508` (separated / non-separated / accessory) — flag and route.
2. **Construction type** — `IBC` Ch. 6: `I-A`, `I-B`, `II-A`, `II-B`, `III-A`, `III-B`, `IV-A`, `IV-B`, `IV-C`, `IV-HT`, `V-A`, `V-B`. Drives base allowable from `Table 506.2`.
3. **Provided values** — labeled:
   - Total building area `sf` (sum of all stories in the area-calculation envelope per `§506.1.2`)
   - Largest single-story area `sf`
   - Number of stories above grade plane
   - Building height `ft` (top of roof per `§502`)
4. **Sprinklered status** — `non-sprinklered`, `NFPA 13` (commercial), `NFPA 13R` (low-rise residential), `NFPA 13D` (1-and-2-family). Sprinkler factor (`Is`) applies per `§506.3` only with `NFPA 13`.
5. **Open frontage** — perimeter `ft` open to public way / yard ≥ 20 ft, used for `If` factor per `§506.3.2`. State the `F/P × W` measurement.
6. **Jurisdiction** — base IBC always applies. Stricter overlays:
   - NYC BC (Ch. 5 amendments)
   - California Building Code Part 2
   - DSA (CA K-12)
   - CA HCAI (CA hospitals)
   - OBC 2024 (Toronto Building, different framework)
7. **Source for the operative tables / § text** — paste / fetch / local index:
   - Paste verbatim `IBC Table 506.2` row (occupancy + construction type) and `Table 504.3` (stories) and `Table 504.4` (height in `ft`), with citation headers.
   - Paste verbatim `§506.3` allowable area formula and `§506.3.2` open-frontage definition.
   - Fetch from AHJ amendment page where free.
   - a local RAG index if the IBC PDF is indexed locally.

The command refuses to compute against recalled allowable values.

## Workflow

1. Echo parsed inputs: occupancy / construction type / provided area + stories + height / sprinklered / open frontage / jurisdiction.
2. Identify reference area: `IBC Ch. 5 — General Building Heights and Areas`. Tables `504.3`, `504.4`, `506.2`. Calculation in `§506.3`. Do not claim specific values from recall.
3. Acquire source text (table rows + formula §).
4. For overlay jurisdictions, require overlay text or stop.
5. Math against verbatim source:
   - Apply the formula `Aa = (At + NS × If) × Sa` (or per the verbatim source — quote it)
   - Compute `If` from `(F/P − 0.25) × W/30` per `§506.3.2`.
6. Output table + attribution + caveats.

## Output template

```markdown
# Test Allowable Area — [Occupancy + Construction Type, plain title]

**Occupancy:** [B / R-2 / A-3 / mixed]
**Construction type:** [I-A / II-B / V-B]
**Provided:** [building area X sf / largest story Y sf / Z stories / height H ft]
**Sprinklered:** [NFPA 13 / NFPA 13R / NFPA 13D / non-sprinklered]
**Open frontage:** [F = ... ft, P = ... ft, W = ... ft, F/P = ...]
**Jurisdiction:** [base IBC 2024 / + NYC BC / + CBC / + OBC]

## Reference area
IBC Ch. 5 — General Building Heights and Areas. Tables `504.3` (allowable stories), `504.4` (allowable height in ft), `506.2` (allowable area factor `At`). Formula and frontage in `§506.3`.

## Source text under test
> [Verbatim quote of `Table 506.2` row for the occupancy + construction type.]

(Source: pasted by user / fetched from <URL> on <YYYY-MM-DD>)

> [Verbatim quote of `§506.3` allowable area formula and `§506.3.2` open-frontage definition.]

(Source: pasted by user / fetched from <URL> on <YYYY-MM-DD>)

## Comparison
| Value | Provided | Allowable (per quoted source + math) | Verdict | Margin |
|---|---|---|---|---|
| Allowable stories | ... | "<Table 504.3 row>" | PASS / FAIL / MARGINAL | ... |
| Allowable height (ft) | ... | "<Table 504.4 row>" | ... | ... |
| Allowable area per story | ... | "<§506.3 formula applied to verbatim factors>" | ... | ... |

## Jurisdictional flags
- [If overlay in scope and overlay source provided: include overlay rows.]
- [If overlay in scope but overlay source missing: list the overlay text the user must paste / fetch.]
- [Mixed-occupancy must apply `IBC §508` separated / non-separated / accessory rules — flag and route to `code-compliance-review`.]
- [Mezzanine / unlimited-area buildings (`§505`, `§507`) and high-rise (`§403`) trigger separate provisions — flag if applicable.]

## Caveats
- Single-building gut-check; not a stamped Ch. 5 analysis. Mixed-occupancy and special provisions (`§503` general, `§505` mezzanines, `§507` unlimited area, `§403` high-rise) require AOR / Code Consultant scoping.
- Open-frontage measurement is geometry-sensitive. The `F`, `P`, `W` definitions in `§506.3.2` must be applied carefully — many designs miscount frontage along non-qualifying boundaries.
- All limit values come from the source the user pasted or the URL fetched on <date>. The command did not recall any IBC value from training.
- IBC editions and AHJ amendments change. NYC DOB amendments to `Table 506.2` exist for some occupancies.
- Binding interpretation is the AOR's stamped Ch. 5 analysis plus AHJ review.
```

## NA AEC conventions (enforce)

- English only.
- Imperial-first: `sf`, `ft`, stories. Metric only if the source uses it (OBC).
- Codes: IBC, NFPA 13 / 13R / 13D, NFPA 101, NYC BC, CBC, OBC, NBC. Reject `KBC`, `KS`, `EN`, `BS`, `JIS`, `DIN`.
- AHJs named: NYC DOB, FDNY, LADBS, DSA, CA HCAI, NYC SCA, Toronto Building, Boston ISD, Chicago DOB. Never `the AHJ` or `the city`.
- Floors / stories: Level 3 / L3 / 3rd floor. Never `3F`.
- Roles: Architect of Record (AOR), Code Consultant, Fire Protection Engineer, Expediter (NYC). Never `Director` as a project role.

## Constraints

- Never invent allowable area / stories / height values from recall.
- Never paraphrase `Table 506.2` / `Table 504.3` / `Table 504.4` — verbatim only.
- Never claim a specific table number / row from recall.
- For mixed-occupancy, route to `code-compliance-review` — `§508` separated / non-separated / accessory rules are out of scope for this command.
- Distinguish `NFPA 13` (full sprinkler factor) from `13R` / `13D` (no `Is` credit per `§506.3`).
- Single building, single shot. Multi-building / phased scoping → `code-compliance-review`.
- No `docs/` artifact, no Word / PDF, no `aec-doc-gen`.
- Caveat block always present.
- Fetch only after explicit user authorization.

## Anti-patterns (never do)

- Stating allowable values inline ("Type II-B B occupancy = 23,000 sf base") — never. Numbers live only in the quoted source.
- Claiming `Table 506.2` row from recall — never.
- Auto-applying `Is` sprinkler factor without confirming `NFPA 13` (vs `13R` / `13D`).
- Counting frontage along boundaries that don't qualify under `§506.3.2` (e.g., neighbor-fence line ≤ 20 ft, internal lot lines).
- Treating mixed-occupancy as single-occupancy.
- Auto-fetching without explicit authorization.
- Hedging — verdicts are PASS / FAIL / MARGINAL.
- Running `code-compliance-review` from inside this command — pointer-only.
