---
name: code-compliance-review
description: "Audits a floor plan, schematic set, or program layout across eight egress and accessibility axes: use and occupant load, egress capacity and exit count, common path of travel, travel distance, exit access and door width, exit separation, accessibility, and fire-resistance assemblies. Trigger on \"code review\", \"egress check\", \"life safety review\", \"plan check\", \"check egress\", \"accessibility check\", \"exit count\", \"travel distance\", or a pasted plan with a code question. Works in any jurisdiction. The user names the governing code and edition and supplies each limit by typing it, pasting the clause, or naming a file to read. The skill never supplies a limit from memory or from web search. Writes a dated review file and appends to a project index, with every unverified axis counted on the face of the review. Does not replace the Architect of Record or the AHJ."
license: MIT
metadata:
  title: "Code Compliance Review"
  summary: "Audit a plan across eight egress and accessibility axes"
  discipline: "code-life-safety"
  tags: "Compliance, Design"
---

# Code Review

Audit a plan across eight axes, in the order the analysis actually runs, and
write the result to a dated file that says what was checked and what was not.
The axes are the same everywhere. The limits are not, so the limits come from
you.

## Scope and limits — read first

**What this does.** Walks a plan through eight egress and accessibility axes,
compares what the plan shows against limits you supply, and writes a review file
with a citation on every finding. An axis with no limits comes out as
`unverified` and is counted on the face of the review, so a partial audit never
reads as a full one.

**What this does not do.**

- **It does not tell you what your code requires.** Every limit comes from you.
  An axis you supply nothing for stays unverified. That is the design, not a gap.
- It does not measure your drawing. Travel distances, diagonals, and widths are
  numbers you take off the plan.
- It does not classify the building or decide the construction type. You name
  them; it records what you named and what you cited.
- It does not check structure, energy, mechanical, plumbing, or zoning.
- It does not produce a stamped review, and it does not anticipate the AHJ.
- It does not go deep on one axis. This is the wide pass: eight axes, one page
  each. When an axis comes back failed or unverified and you need the full
  treatment, that is a different skill: `design-occupancy-load` for the load
  itself, `design-egress` for the eleven means-of-egress items,
  `design-stair` for flight geometry, `ada-tracker` for a checklist you keep
  through the project. Stair riser, tread, headroom and handrail are not among
  the eight axes at all, so a stair only gets checked by running
  `design-stair`.

**About the bundled reference files.** `references/egress_axes.md` carries the
axis framework: sub-criteria, failure modes, and how a finding should be worded.
Use it for the method. Any code value that appears in it, or in
`references/ibc_egress_quick_ref.md`, is a North American transcription that has
not been verified line by line and may be from a superseded edition. Treat those
values the same as any other unsourced number: confirm against your own code
before it reaches a finding, or leave the axis unverified.

**What you need before starting.** The governing code and edition, the plan, and
the clause text for whichever axes you want checked.

## Workflow

### Step 1. Bootstrap if needed

Check that `docs/code-reviews/index.md` exists. If not:

```bash
python scripts/init_code_review_workspace.py
```

### Step 2. Establish the code basis

An egress finding without a code basis is an opinion. Pin these before any axis.

- Read `docs/project.md` if it exists, for jurisdiction, AHJ, code and edition,
  and use classification.
- Otherwise ask once for: address, which code governs and which edition, use
  classification, construction type, sprinkler condition and the standard the
  system follows, and storeys above grade.
- **Confirm the edition explicitly.** A code name alone is not a basis. Get the
  cycle, and any local amendment layered on top.
- If a second standard applies alongside the base code, note it and say which
  one governs where they diverge.
- Ask how limits will be supplied: typed, pasted clause text, or a file to read.
- **Read `docs/jurisdiction.md` first if it exists**, and report which axes it
  already carries limits for. Match on the Key column so a row keyed to another
  use or sprinkler condition is not borrowed for this one. A row marked
  `not cited` carries that word through to the finding rather than being
  promoted. Where the file is absent nothing changes; `jurisdiction-profile`
  writes and extends it, and every limit that arrives here without being in it
  is worth offering back to it with its clause.

### Step 3. Apply the eight axes

Read `references/egress_axes.md` for the framework. The axes, in the order the
analysis proceeds, because everything downstream depends on the first:

1. **Use and occupant load.** Classification per space, load factor, aggregation
   per storey, mixed-use treatment.
2. **Egress capacity and exit count.** Capacity factor per occupant for stairs
   and for level components, required exit count for the load, single-exit
   conditions.
3. **Common path of travel.** Limit, and where the two-direction choice begins.
4. **Travel distance.** Limit, measured along the path of travel.
5. **Exit access width and door clear width.** Door clear width, leaf maximum,
   corridor width, dead-end limit.
6. **Exit separation.** The required fraction of the diagonal, verified
   geometrically on the plan rather than asserted.
7. **Accessibility.** Accessible route from arrival to required spaces,
   accessible means of egress, unit counts where residential.
8. **Fire-resistance assemblies and opening protectives.** Separations, corridor
   walls, shaft enclosures, opening protective ratings. Note where the plan
   implies an assembly the spec must carry.

For each axis, ask for the limits it needs before writing any finding. Accept
exactly three kinds of answer: a typed limit with its clause, a pasted clause to
read the limit out of, or a file to read. If none arrives, the axis is
`unverified` and no finding is written for it.

Focus on the three to five axes with real signal for the plan in front of you.
An axis that is clearly fine gets one line. An axis with no limits gets
`unverified`, which is not the same thing and must never be written as the same
thing.

### Step 4. Write the review

Read `assets/code-review-template.md` and fill it in. Filename:

`docs/code-reviews/<YYYY-MM-DD>-<slug>-egress.md`

Slug rule: lowercase, `[^a-z0-9-]` removed, max 40 characters, from project plus
the level or area reviewed. Suffix `-<n>` if the date and slug already exist.

Every finding carries the limit, the citation it came from, and what the plan
shows. The head of the review states the code and edition. The foot states how
many axes were checked and how many were unverified.

### Step 5. Update the index

```bash
python scripts/append_to_index.py \
  --date <YYYY-MM-DD> \
  --slug <slug> \
  --use-group <as classified by the user> \
  --code-edition "<code and edition as supplied>" \
  --primary-axes "occupant-load,common-path,exit-separation"
```

The script appends a row. Do not edit the index by hand; the table alignment
breaks easily.

### Step 6. Report

Give the counts: axes checked, findings raised, axes unverified. List the
unverified ones with what each needs to close. Close with:

> Limits in this review came from you, not from me. Unverified axes were not
> checked at all.

## Rules

- **Never supply a code limit.** Not from memory, not from a search, not from a
  bundled reference file. A bundled value is unsourced until you confirm it
  against your own edition.
- **No finding without a citation.** A finding whose limit has no source is an
  unverified axis instead.
- **Unverified is not a pass.** They are counted separately, on the face of the
  review, every time.
- **Confirm the edition before any axis.** A clause number without an edition is
  not a citation.
- Verify exit separation on the geometry rather than accepting an assertion.
- Never convert units, and never round a measured distance to a neater figure.

## Anti-patterns

- Writing a finding from a limit recalled because it is a familiar one. Familiar
  limits are the ones that survive an edition change unnoticed.
- Searching the web for a clause and using it as the limit. Search finds which
  code governs; it does not quote it reliably.
- Quoting `references/egress_axes.md` or `ibc_egress_quick_ref.md` as the code.
  They are a framework and an unverified transcription, not an authority.
- Reporting only the axes that could be checked, so a three-axis review reads
  like a full one.
- Scoring all eight axes on every plan to look thorough, rather than the three
  to five that carry signal.
- Editing `docs/code-reviews/index.md` by hand instead of using the script.

## Resources

- `references/egress_axes.md` — the eight-axis framework, sub-criteria, failure
  modes, and finding wording. Method, not authority.
- `references/code_editions_by_jurisdiction.md` — which edition a North American
  jurisdiction has adopted. A starting point for the edition question, to be
  confirmed with the AHJ.
- `references/ibc_egress_quick_ref.md` — an unverified North American
  transcription, carried for orientation only.
- `assets/code-review-template.md` — the review file structure.
- `scripts/init_code_review_workspace.py`, `scripts/append_to_index.py`.
