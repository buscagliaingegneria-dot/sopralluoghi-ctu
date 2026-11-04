---
name: climate-zone-mapper
description: "Records the climate or thermal zone a project sits in, then builds the envelope requirement scorecard component by component: roof, walls above and below grade, floors, slab edge, fenestration thermal, fenestration solar gain, and air leakage. Trigger on \"what climate zone is this\", \"climate zone for this site\", \"envelope requirements for zone X\", \"energy code envelope scorecard\", \"climate-zone-mapper\", or a pasted project address with an envelope question. Works with any energy code. The zone determination and every requirement value come from the user, typed, pasted, or read from a file they name. The skill never supplies a zone, an R-value, a U-factor, or a solar gain figure from memory or from web search, and any component without a supplied requirement is reported as unverified. Writes a CSV scorecard and a summary."
license: MIT
metadata:
  title: "Climate Zone Mapper"
  summary: "Record a site's climate zone and its envelope requirements"
  discipline: "code-life-safety"
  tags: "Compliance"
---

# Climate Zone Mapper

Every energy code asks the same question of a building envelope: what is
required at each component, for this site's zone. The component list is the
same everywhere. The zone names and the numbers are not, so both come from you.

## Scope and limits — read first

**What this does.** Records the zone and its source, walks the eight envelope
components, records the requirement you supply for each, compares it against
your proposed assembly, and writes a scorecard plus a summary. Components with
no requirement supplied come out `unverified` and are counted on the scorecard.

**What this does not do.**

- **It does not determine the zone.** It has no zone map, no county list, and no
  station data. You give the zone and where it came from. That is the design,
  not a gap.
- **It does not know any envelope requirement.** No R-values, no U-factors, no
  solar gain figures, no air leakage rates. Every one comes from you.
- It does not compute an assembly's performance. Your proposed value is one you
  calculated or took from a manufacturer.
- It does not do trade-off, component performance, or whole-building performance
  compliance paths. It covers the prescriptive component route, which is the one
  a scorecard fits.
- It does not layer a local amendment over a base code on its own. If two
  documents apply, you say which governs each row.
- It does not replace the Architect of Record, the energy modeller, or the
  authority.

**What you need before starting.** The governing energy code and edition, the
zone with its source, and the requirement for each component you want scored.

## Workflow

### Step 1. Bootstrap if needed

```bash
python scripts/init_workspace.py
```

Confirm before creating `docs/` in a project that does not have one.

### Step 2. Establish the code and the zone

Ask, in one message:

> 1. Which energy code governs, and which edition? Name any local amendment
>    layered on top, and say which governs where they differ.
> 2. What zone is the site in, and where did that come from? A county listing in
>    the code, a map, a climate data standard, or a letter from the authority.
>    Name it; the source prints on the scorecard.
> 3. Is this scored as commercial or residential, in your code's sense of those
>    words?
> 4. How will you supply the requirements? Type them, paste the table row, or
>    name a file I should read.

If the zone is unknown, stop. Everything downstream is keyed to it, and a
scorecard built on a guessed zone is wrong in a way that looks entirely normal.

### Step 3. Collect the proposed assemblies

For each component, ask what is proposed and in what units. Never fill one in
from a typical construction.

### Step 4. Collect one requirement per component

Work the list below. For each, accept a typed value with its clause, a pasted
table row to read it out of, or a file to read. If none arrives, the component
is `unverified`.

| # | Component | Usually expressed as |
|---|-----------|----------------------|
| 1 | Roof | thermal resistance, or assembly transmittance |
| 2 | Walls above grade | thermal resistance, or assembly transmittance |
| 3 | Walls below grade | thermal resistance, and the depth it applies to |
| 4 | Floors over unconditioned space | thermal resistance |
| 5 | Slab on grade edge | thermal resistance, and the depth or width |
| 6 | Fenestration, thermal | assembly transmittance |
| 7 | Fenestration, solar | solar heat gain coefficient |
| 8 | Air leakage | rate, and the pressure it is tested at |

State which row you took, since these tables are keyed by zone and by commercial
against residential, and a right number off the wrong row reads exactly like a
right answer.

### Step 5. Score

| # | Component | Required | Cited as | Row taken | Proposed | Status |
|---|-----------|----------|----------|-----------|----------|--------|

`Status` is `pass`, `fail`, `unverified` (no requirement supplied), `missing`
(no assembly supplied), or `n/a`.

Write the CSV to `docs/climate-zone/<project>-envelope.csv` and the summary from
`assets/climate-zone-summary-template.md`. Both carry the code, the edition, the
zone, and the zone's source at the head, and the unverified count at the foot.

### Step 6. Update the index

```bash
python scripts/append_to_index.py \
  --project <slug> \
  --location "<as supplied>" \
  --county-state "<as supplied>" \
  --zone "<as supplied>" \
  --occupancy "<Commercial | Residential>" \
  --csv <file>.csv \
  --summary <file>.md
```

Do not edit `docs/climate-zone/index.md` by hand; the table alignment breaks.

### Step 7. Report

Counts by status, the unverified list with what each needs, and:

> The zone and every requirement here came from you. I compared numbers and
> supplied none. Unverified components were not scored at all.

## Rules

- **Never supply a zone or a requirement.** Not from memory, not from a search,
  not from a figure in this file. There are none in this file.
- **Record where the zone came from**, on the scorecard, every time. A zone
  without a source cannot be defended a year later.
- **Name the row every requirement came from**, including the commercial or
  residential split.
- **Never convert units** and never round a requirement or a proposed value.
- **Stop if the zone is unknown.** Do not score against a guess.
- Where a base code and a local amendment both apply, the user says which
  governs each row; never merge them.

## Anti-patterns

- Naming the zone for a city because the answer feels obvious. Zone boundaries
  are drawn at county lines and get redrawn between editions.
- Filling a thermal resistance or a transmittance from recall because the
  combination is a common one.
- Searching the web for a table row and scoring against what comes back.
- Reporting only the components that could be scored.
- Scoring a residential assembly against a commercial row, or the reverse.
- Editing `docs/climate-zone/index.md` directly instead of using the script.
- Bundling a zone list or an envelope table into this skill later. It had both.
  An audit found the original tables had been generated from model recall rather
  than read from the publication, and every cell was replaced with a
  verification placeholder; the tables and the script that parsed them were
  removed rather than filled back in.

## Resources

- `assets/climate-zone-summary-template.md` — the summary structure.
- `assets/climate-zone-index-template.md` — the project index structure.
- `scripts/init_workspace.py` — bootstrap `docs/climate-zone/`.
- `scripts/append_to_index.py` — append a row to the index.

No reference files. The zone and the requirements come from your code.
