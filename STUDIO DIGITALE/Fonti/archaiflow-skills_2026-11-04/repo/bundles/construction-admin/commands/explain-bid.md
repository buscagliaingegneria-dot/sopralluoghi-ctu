---
title: Explain Bid
summary: Separate real costs from risk-shifting in bid language
discipline: construction-admin
tags: ["AIA A201", "Construction Admin"]
description: Decode bid qualification language (AIA A101/A102/A103 + A305 + A701) — separate cost items from risk-shifting and schedule assumptions
argument-hint: <bid-qualification-or-paste>
---

# Explain Bid

Interpret bid qualification language — exclusions, allowances, alternates, unit prices, contingencies — and separate true cost items from risk-shifting and schedule assumptions. Output is an inline interpretation citing AIA bid form context. For full bid leveling or multi-bidder comparison, use the `bid-review` skill.

## Input you need

Before interpreting, gather:

- **Bid form / contract pairing**:
  - `A101-2017` (Stipulated Sum) — bid is a fixed lump sum; qualifications shift cost or risk away from the bidder.
  - `A102-2017` (CMc Cost Plus with GMP) — bid is a GMP; qualifications shift the GMP buyout boundary.
  - `A103-2017` (CMc Cost Plus, no GMP) — qualifications shift open-book cost categories.
  - `A104-2017` (Small Projects) — simplified base form.
  - `A701-2018` (Instructions to Bidders) — governs bid submission and qualification rules.
  - `A305-2020` (Contractor's Qualification Statement) — pre-bid qualification, not project-specific.
- **Qualification text** — verbatim paste of the bidder's qualification, exclusion, allowance, alternate, unit price, or contingency line. Bid qualifications rely on exact wording; paraphrase masks scope.
- **Project context** — public vs private owner. Public owners (`NYC SCA`, `NYC DDC`, `GSA`, `USACE`, `state DGS`, `port authority`, `school district`) restrict qualifications by statute; private commercial / institutional accept more.
- **Bid type** — `sealed bid`, `open bid`, `RFP`, `Design-Build proposal`, `negotiated CMc selection`. Sealed-bid public work generally cannot accept qualifications.
- **Specific question** — Examples: "Is 'permit fees by Owner' standard?", "Does this $50,000 weather-day allowance represent risk transfer or carry?", "Why is the bidder excluding rock excavation when the soils report shows clay?"

If the qualification text is paraphrased, ask for verbatim before interpreting.

## Output structure

```markdown
# Explain Bid — [qualification line, short title]

**Bid form:** [A101-2017 / A102-2017 / A103-2017 / A104-2017]
**Bidder:** [GC / CMc / DB entity]
**Owner:** [Public — NYC SCA / GSA / USACE — or Private — name]
**Bid type:** [Sealed / Open / RFP / Negotiated]
**Question:** [the user's specific question]

---

## What the qualification says (literal)

> [Verbatim quote of the qualification line as printed in the bid.]

## Plain-English meaning

[2–4 sentences. What the bidder is shifting, excluding, carrying, or pre-pricing. Distinguish: cost item (real $ in the base bid), risk-transfer (contingency or exclusion of unknown), schedule assumption (production rate, weather days, sequencing).]

## Cost vs risk vs schedule classification

- **Cost** — [If this represents a real $ item already in the base bid. e.g., "Allowance of $25,000 for ceramic tile selection — Owner pays at actual cost ± reconciliation under A201-2017 §3.8."]
- **Risk transfer** — [If the bidder is excluding scope or shifting an unknown to the Owner. e.g., "'Excludes rock excavation' transfers subsurface risk to Owner — verify against the geotech recommendation and `A201-2017 §3.7.4` (compliance with laws and regulations)."]
- **Schedule assumption** — [If a duration / weather day / production rate is embedded. e.g., "'Bid assumes 200 working days from NTP' makes Substantial Completion contingent on no Owner-caused delays — verify against `A101-2017 §5.1.2` schedule."]

## A701-2018 / A101 conformance

- [Bullet — Does this qualification violate `A701-2018 §3.4` (qualified bids)?]
- [Bullet — On a public bid (NYC SCA, GSA, USACE, state DGS, NYC DDC), qualifications routinely disqualify the bid. Flag explicitly.]
- [Bullet — Reference the project-specific Instructions to Bidders if it is non-A701 (federal FAR, GSA solicitation, NYC PPB rules).]

## What to do next

- [Bullet — clarify with bidder pre-award via Owner / AOR (RFI to bidder).]
- [Bullet — accept, reject, or negotiate the qualification before award.]
- [Bullet — if accepted, fold into `A101-2017 §1` (Contract Sum), `A102-2017 §2.3` (assumptions and clarifications schedule attached to the GMP), or A101 §3.3 alternates schedule.]

## Caveats

- Bid leveling requires apples-to-apples qualification analysis across all bidders. Single-bid review can mislead. Use `bid-review` skill for multi-bidder comparison.
- Public-owner bids may have statutory rules superseding A701-2018. Verify with the Owner's procurement office (NYC SCA Office of Contracts, GSA Acquisition, USACE Contracting).
- This is not legal advice. Engage Owner's counsel for contested qualifications and any allowance / contingency / alternate that may convert to a change order.
```

## NA AEC conventions (enforce)

- **English only.** No Hangul anywhere.
- **Bid form citation** — `A101-2017 §X.Y`, `A102-2017 §X.Y`, `A701-2018 §X.Y`. Always include edition.
- **Cost convention** — USD `$/sf`, lump sum `$`, allowances per `A201-2017 §3.8`. Never KRW, never `$/m²`.
- **Roles** — `Owner`, `Owner's Representative`, `Owner's Counsel`, `Architect of Record (AOR)`, `General Contractor (GC)`, `Construction Manager as Constructor (CMc)`, `Construction Manager as Adviser (CMa)`, `Subcontractor`, `Bidder`. Never use `Director` as a project role.
- **Public AHJs** — `NYC SCA`, `NYC DDC`, `GSA`, `USACE`, `state DGS`, `port authority`, `school district`. Never `the AHJ`, `the city`, or `local authority` generically.
- **Codes referenced** — IBC / IRC / NFPA / 2010 ADA / ASCE 7. Never `KBC`, `KS`, `EN`, `BS`, `JIS`, `DIN`.
- **Imperial-first** units (`sf`, `cy`, `lf`); metric in parens only when useful.
- **Floor labels** — `L3`, `Level 3`, `3rd floor`. Never `3F`.

## Constraints

- Do not invent qualification language. Verbatim paste required; paraphrase changes scope.
- Distinguish cost vs risk vs schedule explicitly. Mixed-bag interpretations dilute the analysis.
- Always cite `A701-2018` conformance for public-owner bids — qualified bids often disqualify on public work.
- This is not legal advice. Always include the **Caveats** section with that disclaimer.
- Coexists with `bid-review` skill (multi-bidder leveling). For comparison across bidders, redirect.
- Markdown only. No Word / PDF output, no `aec-doc-gen` dependency.

## Workflow

1. Echo back: bid form + edition, bidder type, owner type (public / private + name), bid type, question. One line.
2. If qualification text is paraphrased, ask for verbatim before proceeding.
3. Produce the response in one shot.
4. Flag adjacent qualifications when visible (allowance + exclusion + unit price often interact — e.g., "Exclusion of permit fees combined with a $50,000 allowance for unforeseen — check whether the allowance covers the excluded scope or double-counts").
5. If the bid is public, surface the A701 / FAR / NYC PPB disqualification risk explicitly before any acceptance recommendation.
