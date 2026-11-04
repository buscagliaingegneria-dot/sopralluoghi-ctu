# Provenance — Design Critic References

This file records the lineage of the six-axis critique framework in `references/six_axes.md` and the relationship between the in-thread `design-critic` skill and the fresh-context `independent-critic` agent. It is also the place to flag what is *not* a published external standard so future readers don't mistake the framework for one.

## What the six-axis framework is — and is not

The six axes (Concept consistency, Scale & proportion, Circulation & program, Material & detail, Context, Innovation vs feasibility) are an **internal, synthesized framework** authored for this skill. They are not a transcription of any single published critique standard, accreditation rubric, or rating system.

Concretely:

- The framework is **not** drawn verbatim from any AIA, NCARB, ACSA, NAAB, ASCA, or RIBA document.
- It is **not** a published critique heuristic associated with a named critic, school, or theorist (it is not Norberg-Schulz, Frampton, Tschumi, Eisenman, etc.).
- It is **not** a transcription of any building-code, zoning, or rating-system rubric.

The framework can be informally **anchored to** several established traditions, in the sense that the axes overlap with concepts those traditions emphasize:

- **Vitruvian triad** (`firmitas`, `utilitas`, `venustas`) — Material & detail and Innovation vs feasibility map onto firmitas; Circulation & program and Scale & proportion map onto utilitas; Concept consistency and Context map onto venustas + the building's situatedness. This is a loose conceptual lineage, not a derivation.
- **NCARB ARE divisions** — Project Management (PjM), Project Planning & Design (PPD), and Project Development & Documentation (PDD) divide architectural practice along axes that partially overlap with this framework's Circulation & program, Scale & proportion, and Material & detail axes. Again, conceptual overlap, not transcription.
- **Design-studio critique heuristics** — the six axes broadly track how senior critics in NA architecture studios separate concerns when reviewing student or staff work. No single source defines the set.

The specific six-axis decomposition, the sub-criteria under each axis, and the "tells" of a weak project on each axis are **the skill's own synthesis**. They should be presented to users as a working framework — useful as a checklist to focus a critique — not as a published standard with the authority of code or rating-system text.

## Relationship to `independent-critic` agent

The same six-axis framework is also used by the `independent-critic` agent at `/.claude/agents/independent-critic.md` (also synced to `claude-code-architecture-templates/agents/independent-critic.md` for installation via curl). The two share a framework but differ in invocation pattern, and that distinction is the entire reason both exist:

| | `design-critic` (skill) | `independent-critic` (agent) |
|---|---|---|
| **Invocation** | In-thread; runs in the parent's context window. | Sub-agent; runs in a fresh context window with no carryover from the parent's framing. |
| **Framing carryover** | Anchors to the conversation's prior framing. The reviewer sees what the parent has already said about the project, including the parent's stated concerns and concept narrative. | Anti-anchoring is the explicit design goal. The agent sees only the artifact and does not see the parent's prior judgments. If the parent said "the entry is the strong move", the agent forms its own view from the artifact alone. |
| **Tools** | Full skill toolset, can write `docs/reviews/<date>-<slug>.md` and append to the review index. | Read-only (`Read, Grep, Glob`). Returns critique text to the parent; the parent decides what to do with it. |
| **Best when** | Iterating with a designer who has already framed the project for you. You want a critique that engages with that framing — accepts what's been resolved, focuses critique on what hasn't. | You want an unanchored second opinion. The parent has been close to the project for a long time and wants critique that doesn't soften because of what's already been discussed. Or: the parent's framing is suspect and you want a view formed from the artifact alone. |
| **Output destination** | Markdown file in `docs/reviews/` + index row. | Returned to parent as text; parent integrates or discards. |

**Reader of `design-critic/SKILL.md` should pick:**

- **`design-critic`** when iterating with prior context, when the critique needs to land in `docs/reviews/`, or when the in-thread parent is the right author of the eventual critique file.
- **`independent-critic`** when seeking an unanchored second opinion, when the parent's framing has accumulated enough that anchoring is now a real risk, or when the goal is "fresh eyes" rather than "continuation of an in-progress critique".

The two are complementary, not redundant. A common pattern: run `design-critic` for the working critique, then invoke `independent-critic` on the same artifact to surface what the in-thread critique anchored on or missed. Compare and reconcile.

## Six-axis sources of authority — at the sub-criterion level

Where the six axes themselves are synthesized, several sub-criteria within them do anchor to external NA conventions and should be cited that way in finished critiques:

- **Scale & proportion → human scale (doors, ceilings, thresholds):** anchor to IBC ceiling-height minimums (and analogs in IRC for residential), ADA reach ranges and doorway clearances (2010 ADA §308, §404), and ANSI A117.1 where the AHJ adopts it.
- **Circulation & program → entry sequence, vertical circulation:** anchor to IBC means of egress (IBC Ch 10), accessible route requirements (2010 ADA §402, §405-407), and any local AHJ overrides (NYC DOB, CA HCAI for healthcare, DSA for K-12).
- **Material & detail → weathering, joint logic:** anchor to ASTM envelope-test methods (E331, E547, E1105), ASHRAE 160 for moisture-control analysis, and AAMA / WDMA fenestration ratings.
- **Context → climate response:** anchor to ASHRAE 90.1 / IECC envelope baseline, ASHRAE 169 climate zones, and any local NA AHJ climate-specific overlays (e.g., CA Title 24 Part 6).
- **Innovation vs feasibility → structural feasibility:** anchor to ASCE 7-22 design loads, ACI / AISC / NDS material-specific design standards as applicable to the structural system claimed.

The skill does not require every critique to cite these — the six axes are a conversation framework, not a code-compliance checklist. But when a critique makes a specific quantitative claim (a span, a load, a clearance, an envelope rating), the claim should be traceable to one of the standards above.

## Verification status

- **Last verified**: 2026-05-09. Six-axis framework reviewed against the audit; "12m glass wall" / "30m cantilever" metric-only examples in `references/six_axes.md` corrected to imperial-first ("40 ft glass wall", "100 ft cantilever") in the same audit pass.
- **Verifier**: skill author. The framework is the skill's own; there is no external publisher to verify against.
- **Update trigger**: when the framework is meaningfully revised (axes added/removed/renamed, sub-criteria materially changed). Also update when the relationship to `independent-critic` changes (e.g., agent toolset changes, output format changes), so this provenance file remains the canonical "which one do I pick" reference.

## Where this file is published

There is no second copy to update. This file is the source: the site reads it off
disk from the repo, and the CLI ships it inside the skill folder. Editing it here
is the whole update.

It used to say that a Notion page body was the source of truth and had to be
edited alongside this file. That database was removed on 2026-07-28.

## Audience scope

`design-critic` (and `independent-critic`) target North American AEC projects. Examples in `references/six_axes.md` use NA conventions and imperial-first units. International precedents (Ando, Zumthor, Sejima, etc.) are welcome as critique reference material — but quantitative claims (spans, clearances, loads, envelope performance) should anchor to NA standards (IBC, ASCE, ASHRAE, 2010 ADA, ANSI A117.1) rather than Eurocode / KBC / BS / EN / JIS.
