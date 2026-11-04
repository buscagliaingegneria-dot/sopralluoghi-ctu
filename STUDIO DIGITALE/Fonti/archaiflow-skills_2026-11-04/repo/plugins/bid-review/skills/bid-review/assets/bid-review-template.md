---
project: "{{PROJECT_NAME}}"
date: "{{REVIEW_DATE}}"
reviewer: "{{REVIEWER}}"
bid_package: "{{BID_PACKAGE}}"
bidders_count: {{N}}
---

# Bid Review — {{PROJECT_NAME}} — {{BID_PACKAGE}}

**Bid package:** {{BID_PACKAGE — e.g., "GC base bid", "Trade pkg 03 (concrete)", "Alternate 3 only"}}
**Delivery method:** {{DELIVERY — DBB / CMAR / DB / IPD}}
**Procurement type:** {{TYPE — public sealed / private negotiated / RFP-based}}
**Bid opening date:** {{BID_OPEN_DATE}}
**Reviewer:** {{REVIEWER}}
**Review date:** {{REVIEW_DATE}}
**Engineer's estimate:** ${{EE_AMOUNT}}
**Number of bidders:** {{N}}
**Jurisdiction / AHJ:** {{AHJ — e.g., "NYC DOB / FDNY", "CA HCAI", "USACE Norfolk District"}}

---

## Summary

{{ONE_PARAGRAPH_SUMMARY — bid count and spread vs. the engineer's estimate, the recommended award, and the 2-3 reasons that drive it.}}

---

## Bid tabulation (as submitted)

| Bidder | Base bid | Alt 1 | Alt 2 | Alt 3 | Bid bond | Addenda ack'd |
|---|---|---|---|---|---|---|
| {{B1}} | ${{B1_BASE}} | ${{B1_A1}} | ${{B1_A2}} | ${{B1_A3}} | {{B1_BOND}} | {{B1_ADD}} |
| {{B2}} | ${{B2_BASE}} | ${{B2_A1}} | ${{B2_A2}} | ${{B2_A3}} | {{B2_BOND}} | {{B2_ADD}} |
| {{B3}} | ${{B3_BASE}} | ${{B3_A1}} | ${{B3_A2}} | ${{B3_A3}} | {{B3_BOND}} | {{B3_ADD}} |

---

## Leveling worksheet — bidders × line items × clarification flags

For each line item that creates spread between bidders, capture: each bidder's value, the leveling adjustment to bring all bidders to a common scope, and any clarification flag that must be resolved before award.

| Line item | Source | {{B1}} | {{B2}} | {{B3}} | Adjustment basis | Clarification flag |
|---|---|---|---|---|---|---|
| Base bid (as submitted) | Bid form | ${{B1_BASE}} | ${{B2_BASE}} | ${{B3_BASE}} | n/a | — |
| Excluded scope: {{EXCL_1 — e.g., "Hazmat abatement"}} | {{B?}} cover Page X | + ${{B1_EXCL_1}} | + ${{B2_EXCL_1}} | + ${{B3_EXCL_1}} | Highest-bidder price; engineer's estimate | {{FLAG_1 — e.g., "Need Phase II ESA result before pricing"}} |
| Excluded scope: {{EXCL_2}} | {{B?}} Page Y Item Z | + ${{B1_EXCL_2}} | + ${{B2_EXCL_2}} | + ${{B3_EXCL_2}} | {{BASIS_2}} | {{FLAG_2}} |
| Unit-price delta: {{UP_1 — e.g., "Rock excavation × 200 CY probable"}} | Bid form unit-price schedule | ${{B1_UP_1}} | ${{B2_UP_1}} | ${{B3_UP_1}} | RSMeans / regional firm published range × probable qty | {{FLAG_3 — e.g., "Pull RSMeans 2026 Q1 RCI for MSA"}} |
| Schedule LD / finance carry | Bid form schedule + A101 §5.1.5 | ${{B1_SCH}} | ${{B2_SCH}} | ${{B3_SCH}} | LD rate × delta-days OR financing carry × delta-months | {{FLAG_4}} |
| Contract-terms exception: {{CT_1 — e.g., "Retainage 5% throughout"}} | {{B?}} cover letter | ${{B1_CT_1}} | ${{B2_CT_1}} | ${{B3_CT_1}} | Owner exposure or finance carry | {{FLAG_5}} |
| Contract-terms exception: {{CT_2 — e.g., "Insurance limits below A201"}} | {{B?}} cover letter | ${{B1_CT_2}} | ${{B2_CT_2}} | ${{B3_CT_2}} | Negotiation cost / risk transfer | {{FLAG_6}} |
| **Leveled total** | — | **${{B1_LEVELED}}** | **${{B2_LEVELED}}** | **${{B3_LEVELED}}** | — | — |

Public-project award must follow procurement law — leveling is advisory, not determinative. Reuse rows for as many line items as the bid package requires.

---

## Findings by axis

Note only the axes with real signal. For axes that are clearly fine, state so in one line.

### 1. Base-bid scope completeness

{{FINDING_SCOPE}}

### 2. Qualifications & exclusions

{{FINDING_EXCLUSIONS}}

### 3. Alternates

{{FINDING_ALTERNATES}}

### 4. Unit prices & allowances

{{FINDING_UNIT_PRICES}}

### 5. Schedule & milestones

{{FINDING_SCHEDULE}}

### 6. Contractor qualifications

{{FINDING_QUALIFICATIONS}}

### 7. Bid form completeness & responsiveness

{{FINDING_RESPONSIVENESS}}

### 8. Contract-terms alignment

{{FINDING_CONTRACT_TERMS}}

---

## Gap analysis

Items in the bid package that are missing, ambiguous, or inconsistent and must be resolved before award. Distinct from the leveling worksheet (which prices known deltas) — this table tracks unknowns.

| # | Gap | Affected bidder(s) | Source (bid sheet ref) | Owner exposure if unresolved | Resolution path |
|---|---|---|---|---|---|
| 1 | {{GAP_1 — e.g., "Bonding letter > 90 days old"}} | {{B?}} | A305 attachment | {{EXPOSURE_1}} | Request updated letter ≤ 90 days |
| 2 | {{GAP_2 — e.g., "Addendum 4 not acknowledged on bid form"}} | {{B?}} | Bid form §1 | Non-responsive on public project (fatal) | Procurement counsel determines curable vs fatal |
| 3 | {{GAP_3 — e.g., "Alternate 3 spread 7× across bidders"}} | All | Bid form alternates schedule | Re-bid risk; mis-priced alt | Issue clarification addendum re-pricing Alt 3 |
| 4 | {{GAP_4}} | {{B?}} | {{REF_4}} | {{EXPOSURE_4}} | {{RESOLUTION_4}} |

---

## Responsiveness defects (public-project critical)

For public sealed-bid procurement, items that may make a bid non-responsive (fatal) per the ITB. Distinct from gaps (above) which may be curable.

- [ ] {{RESP_1 — e.g., "Bidder ABC failed to acknowledge Addendum 4 (ITB §00 21 00 Part 1.05.D)"}}
- [ ] {{RESP_2 — e.g., "Bidder DEF bid bond at 4% on a project requiring 5% (Miller Act / Little Miller Act)"}}

(If empty, all bids are responsive. On public projects, procurement counsel signs off on this list before award.)

---

## Recommended-award memo

**Recommended bidder:** {{RECOMMENDED}}
**Award basis:** {{BASIS — e.g., "lowest leveled bid, all bids responsive, qualifications adequate"}}
**Submitted price:** ${{SUBMITTED_PRICE}}
**Leveled price (basis of recommendation on private projects):** ${{LEVELED_PRICE}}
**Contract value (proposed):** ${{CONTRACT_VALUE}}
**Contract form:** {{FORM — e.g., "AIA A101-2017 with Supplementary Conditions per ITB §00 73 00"}}
**Bonding:** {{BONDING — e.g., "P+P at 100% per AIA A312-2010"}}
**Anticipated NTP:** {{NTP_DATE}}
**Substantial completion:** {{SUB_COMPLETION_DATE}}

### Rationale (3-5 bullets)

- {{RATIONALE_1 — e.g., "Lowest leveled bid by $X over second-low after exclusions added back"}}
- {{RATIONALE_2 — e.g., "Bonding capacity verified within 30 days; surety AM Best A"}}
- {{RATIONALE_3 — e.g., "Comparable project portfolio: 3 K-12 schools in NYC SCA, last 4 years"}}
- {{RATIONALE_4}}

### Risk notes

- {{RISK_1 — e.g., "Schedule slip 14 days vs ITB; LD-priced into leveling at $63K"}}
- {{RISK_2 — e.g., "Two contract exceptions (retainage, insurance umbrella) carried at $X negotiation cost"}}

### Conditions of award

- [ ] {{COND_1 — e.g., "Updated bonding letter within 7 days"}}
- [ ] {{COND_2 — e.g., "Subcontractor list pre-qualified per ITB §00 21 00 Part 1.06"}}
- [ ] {{COND_3 — e.g., "Schedule submission within 14 days of NTP"}}

---

## Pre-award clarifications to issue

Items to clarify before contract signing. Each one references the bidder + the bid sheet location + an owner action.

1. {{CLARIFY_1 — e.g., "Bidder ABC, cover Page 4 Item 7: confirm scope of 'hazmat exclusion' against Phase II ESA dated 2026-04-15"}}
2. {{CLARIFY_2}}
3. {{CLARIFY_3}}

---

## Recommended next skills / actions

- {{NEXT_1 — e.g., "Run `submittal-review` for long-lead items in bidder's procurement plan"}}
- {{NEXT_2 — e.g., "Run `constructability-review` if bidder qualified phasing or schedule"}}

---

## References cited

- {{REF_1 — e.g., "ITB §00 21 00 Part 1.05.D (Instructions to Bidders, Addenda)"}}
- {{REF_2 — e.g., "AIA A101-2017 §5.1.5 (Liquidated Damages — fillable line; verify against executed Supplementary Conditions)"}}
- {{REF_3 — e.g., "AIA A201-2017 §11 (Insurance), §3.4.2 (Substitutions)"}}
- {{REF_4 — e.g., "RSMeans 2026 Q1 Square Foot Costs, RCI factor for project MSA"}}
- {{REF_5 — e.g., "GSA P-100 current edition (federal benchmark anchor)"}}
