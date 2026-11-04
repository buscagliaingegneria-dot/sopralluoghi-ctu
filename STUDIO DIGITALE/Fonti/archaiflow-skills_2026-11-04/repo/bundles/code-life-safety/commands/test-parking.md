---
title: Test Parking
summary: Check required parking count and accessible spaces
discipline: code-life-safety
tags: ["Compliance"]
description: Single-parcel parking gut-check (required count vs provided + accessible-space allocation per 2010 ADA §208) — user pastes or authorizes fetch of zoning + ADA text; PASS / FAIL / MARGINAL with explicit attribution. Carries no values internally.
argument-hint: <use-or-occupancy> <provided-count> [district-and-jurisdiction]
---

# Test Parking

Single-parcel parking gut-check — required count by zoning, accessible-space minimum per `2010 ADA §208 Table 208.2`, van-accessible ratio, and aisle / signage references — against zoning resolution + ADA text the **user supplies**.

**This command does not carry zoning or ADA values.** Every limit cited in the output is a verbatim quote from text the user pasted, or text the command fetched from an explicitly-named official URL with the user's authorization. Parking minima vary by district within a single municipality and many cities (NYC, SF, LA portions) have eliminated or capped minima recently.

For ADA single-space slope / aisle dimension checks, use `/test-ada` with `space = parking`.

## Inputs the command needs

1. **Use / occupancy** — name the use as the zoning resolution categorizes it (residential by unit count, commercial by `sf` or per-employee, school by classroom, hospital by bed). Mixed uses tested per use.
2. **Provided counts** — labeled:
   - Total spaces
   - Accessible spaces (standard + van)
   - Compact spaces (where allowed)
   - Loading berths (where required)
3. **Project metrics** — area `sf`, dwelling units, classrooms, beds, seats — whichever drives the zoning ratio.
4. **Zoning district** — explicit AHJ + district code:
   - NYC ZR district (`R6A`, `M1-2`, etc.)
   - LA LAMC use category
   - SF Planning Code district + parking-controlled-zone status
   - Toronto Zoning By-law 569-2013 zone category
   - Other cities — paste applicable code
5. **Jurisdiction** — name the jurisdiction + governing zoning instrument:
   - NYC DCP (NYC ZR — note many districts now have no minimum)
   - LA City Planning (LAMC)
   - SF Planning (Planning Code — most of city has no minimum)
   - Boston BPDA (Boston Zoning Code)
   - Chicago Zoning (Chicago Zoning Ordinance)
   - Toronto City Planning (Bylaw 569-2013)
   - State / county zoning where unincorporated
6. **Source for zoning § + ADA §208 text** — paste / fetch:
   - Paste verbatim zoning § for the district + use, with citation header.
   - Paste verbatim `2010 ADA §208 Table 208.2` (federal accessible-space minimum).
   - Fetch from AHJ portal (NYC DCP, LA City Planning, etc.) and `https://www.ada.gov/law-and-regs/design-standards/2010-stds/`.

The command refuses to compute against recalled minima. Many cities have eliminated parking minima in recent amendments; recall is unreliable.

## Workflow

1. Echo parsed inputs: use / metrics / provided counts / district / jurisdiction.
2. Identify reference areas:
   - Zoning: AHJ-specific article / chapter (NYC ZR Article II/III/IV — district-specific parking; LAMC §12.21.A.4; etc.).
   - ADA: `2010 ADA §208 — Parking Spaces`, `Table 208.2`, `§502 — Parking Spaces` for dimensions.
   Do not claim specific § from recall.
3. Acquire source text — both the zoning § for the district and `ADA §208`.
4. Math against verbatim sources:
   - Required total per zoning ratio.
   - Required accessible per ADA `Table 208.2` based on total provided.
   - Van-accessible per `§208.2.4` (1 in every 6, minimum 1).
5. Output table + attribution + caveats.

## Output template

```markdown
# Test Parking — [Use, Provided count, plain title]

**Use:** [residential 24 du / office 5,000 sf / restaurant 80 seats]
**Provided:** [total = 30, accessible = 2 (1 van + 1 std)]
**District:** [R6A NYC / RH-2 SF / etc.]
**Jurisdiction:** [NYC DCP + 2010 ADA / LA City Planning + 2010 ADA]

## Reference area
- Zoning: [article / chapter pointer for the district].
- ADA: `2010 ADA §208 — Parking Spaces`, `Table 208.2`.

## Source text under test
> [Verbatim quote of zoning ratio for use + district.]

(Source: pasted by user / fetched from <zoning URL> on <YYYY-MM-DD>)

> [Verbatim quote of `2010 ADA §208 Table 208.2`.]

(Source: pasted by user / fetched from `https://www.ada.gov/law-and-regs/design-standards/2010-stds/` on <YYYY-MM-DD>)

## Comparison
| Value | Provided | Required (per quoted source) | Verdict | Margin |
|---|---|---|---|---|
| Total spaces | ... | "<verbatim zoning ratio applied>" | PASS / FAIL / MARGINAL | ... |
| Accessible spaces | ... | "<verbatim Table 208.2 row>" | ... | ... |
| Van-accessible | ... | "<verbatim §208.2.4>" | ... | ... |

## Jurisdictional flags
- [If district has eliminated parking minimum, the zoning ratio is `0` — verify against the latest AHJ amendment.]
- [Special-purpose districts, transit-oriented zones, and parking maxima — flag if applicable.]
- [State accessibility overlay (`CA Title 24 Part 2 Ch. 11B-208`, `MA AAB`) may have stricter accessible minima than federal.]

## Caveats
- Single-parcel gut-check; not a parking-design analysis. Accessible aisle width, signage, slope, and van-accessible aisle width are separate per `2010 ADA §502` — re-run via `/test-ada` for each.
- Many cities (NYC, SF, LA portions, Buffalo, Minneapolis) have eliminated parking minima; the zoning ratio may be `0` even if older sources show otherwise. Use the latest AHJ-published district text.
- All limit values come from the source the user pasted or the URLs fetched on <date>. The command did not recall any zoning or ADA value from training.
- Binding interpretation is the AOR's stamped zoning analysis plus AHJ review (DCP / LADBS / SF Planning).
```

## NA AEC conventions (enforce)

- English only.
- Imperial-first: spaces (count), `ft` aisle, `sf` site. Metric only if the source uses it (Toronto).
- Zoning instruments: NYC ZR, LAMC, SF Planning Code, Boston Zoning Code, Chicago Zoning Ordinance, Toronto Zoning By-law 569-2013. Reject `KBC`, `KS`, `EN`, `BS`, `JIS`, `DIN`.
- ADA: `2010 ADA Standards`, `ANSI A117.1-2017`, `CA Title 24 Part 2 Ch. 11B-208`, `MA AAB 521 CMR`.
- AHJs named: NYC DCP, LADBS / LA City Planning, SF Planning, Boston BPDA, Chicago Zoning, Toronto City Planning. Never `the AHJ` or `the city`.
- Floors: Level 3 / L3 / 3rd floor (parking levels: P1 / P2). Never `3F`.
- Roles: Architect of Record (AOR), Zoning Consultant, Accessibility Consultant, Civil Engineer (for site work), Owner, Owner's Representative. Never `Director` as a project role.

## Constraints

- Never invent zoning ratios or ADA accessible minima from recall.
- Never paraphrase district text or `Table 208.2` — verbatim only.
- Never claim a specific § number from recall.
- Distinguish federal `2010 ADA §208` from state overlays (`CA 11B-208`, `MA AAB`).
- Single parcel, single shot.
- No `docs/` artifact, no Word / PDF, no `aec-doc-gen`.
- Caveat block always present.
- Fetch only after explicit user authorization.

## Anti-patterns (never do)

- Stating ratios inline ("0.5 spaces per dwelling unit in R6A") — never. Numbers live only in the quoted source.
- Claiming `Table 208.2` row contents from recall — never.
- Treating eliminated-minimum districts as if old ratios still applied.
- Treating CA / MA projects as federal-ADA-only — state overlay required.
- Auto-fetching without explicit authorization.
- Hedging — verdicts are PASS / FAIL / MARGINAL.
- Running `/test-ada` from inside this command — pointer-only.
