---
title: Draft Letter
summary: Write a letter to the building department
discipline: code-life-safety
tags: ["Compliance", "Document Generation", "Construction Admin"]
description: Draft AHJ correspondence — response to plan-check comments, alternative-method request, code-interpretation request. NA AHJs only (NYC DOB, FDNY, LADBS, CA DSA, CA HCAI). Use the rfi-writer skill for contractor RFIs; use the code-compliance-review skill for full code audit.
argument-hint: <ahj-name-and-comment-number>
---

# Draft Letter

Draft an AHJ-correspondence letter — typically a response to plan-check comments (NYC DOB Notice of Objections / NOTC, LADBS Plan Check Correction Sheet, CA DSA Back-Check Letter, FDNY pre-app letter), or an alternative-method request, or a code-interpretation request. Output is Markdown ready to paste into Word for letterhead transmittal to the AHJ.

The user owns the AHJ comment language, Information Bulletin numbers, and any local code modification application form text — this command orchestrates the response, it does not invent AHJ regulatory references.

## Input you need

Before drafting, gather:

1. **AHJ name** — specific (`NYC DOB`, `FDNY`, `LADBS`, `CA DSA`, `CA HCAI`, `NYC SCA`, `Toronto Building`, `GSA Region 2`, `USACE Buffalo District`, etc.). Generic "the city" is not acceptable.
2. **AHJ project identifier** — `BIN` (NYC), `Job #` (LADBS), `DSA App #`, `HCAI Project #`, `Permit #`, `Plan Check #`. Whatever the AHJ uses to track the application.
3. **Letter type** — one of:
   - `Plan-check response` — answering specific comments / objections from a Notice of Objections / Plan Check Correction Sheet / Back-Check Letter
   - `Alternative method request` — requesting AHJ acceptance of an alternative material, design, or method (e.g., IBC §104.11 — but verify the IBC edition the AHJ has adopted)
   - `Code-interpretation request` — asking the AHJ to issue an interpretation
   - `Pre-application meeting request` — formal request for a pre-app meeting (FDNY, GSA, etc.)
4. **AHJ comment language** — for plan-check responses, the **verbatim** comment text from the AHJ document. User must paste — do not paraphrase comment language from training.
5. **Comment number(s)** — as numbered by the AHJ (e.g., `Comment 7`, `Objection #14`, `Item 3.b`).
6. **Project info** — name, address, BIN / Job #, AOR firm, AOR PIC name + license #.
7. **Response strategy per comment** — `Compliance` (will revise to comply), `Clarification` (already compliant; clarifying), `Alternative method` (proposing an alternate per `IBC §104.11` or AHJ-specific bulletin — user names the bulletin), `Withdrawal` (withdrawing the affected item).
8. **Supporting documents** — revised drawing # + revision tag, code analysis sheet, structural calculations, accessibility narrative, fire-protection narrative.
9. **Information Bulletin / Code Modification numbers** — only if the user is citing a specific AHJ bulletin (e.g., `NYC DOB Buildings Bulletin 2014-026`, `LADBS IB-P/BC 2020-066`, `DSA IR 16-3`). User must paste / supply these — do not recall from training.

If any of the above is missing or ambiguous, ask the user before drafting. Do not invent AHJ comment text, Bulletin / IR numbers, or comment numbers.

## Output template

```markdown
# [AHJ-Letter Type] — [Project Name]

**[Letter rendered on AOR firm letterhead]**

[Date — Month DD, YYYY]

[AHJ name]
[AHJ unit / division — e.g., NYC DOB Plan Examination Unit, LADBS Plan Check]
[AHJ address]

**Re:** [Project Name]
[Project address]
[AHJ identifier — BIN ######### / Job # / DSA App # / Plan Check #]
[AOR project number]
[Letter type — Response to Notice of Objections #X / Alternative Method Request / etc.]

---

Dear [AHJ contact name or "Plan Examiner"]:

This letter responds to [the Notice of Objections dated <Month DD, YYYY> / the Plan Check Correction Sheet dated <Month DD, YYYY> / etc.] for the above-referenced project. Each comment is addressed below, with reference to the revised documents enclosed.

---

## Per-Comment Response

### Comment [#] — [AHJ-comment subject as titled in the AHJ document]

**AHJ comment (quoted verbatim from [source document, dated Month DD, YYYY]):**
> [User-pasted comment text. Do not paraphrase.]

**Response strategy:** [Compliance / Clarification / Alternative method / Withdrawal]

**Response:**
[Plain-language response. For Compliance: identify what was revised, on which sheet, at which revision. For Clarification: explain why the existing design already complies, citing the specific drawing / spec evidence. For Alternative method: state the alternative, cite the basis (e.g., `IBC §104.11` if the AHJ has adopted that edition, or the specific AHJ bulletin the user provided), enclose supporting analysis. For Withdrawal: state what is withdrawn and what replaces it.]

**Reference documents (enclosed):**
- Sheet [A-301] Rev [4], dated [Month DD, YYYY]
- Code analysis sheet [G-001] Rev [3]
- [Supporting narrative / calculation, dated Month DD, YYYY]

---

### Comment [#+1] — [next subject]

[repeat structure]

---

## Closing

We trust the enclosed responses and revised documents resolve the above comments. Please contact the undersigned with any questions or to schedule a back-check meeting.

Sincerely,

[PIC Name], [AIA / RA / PE], License # [######]
[Title]
[Firm legal name]
[Phone] · [Email]

**Enclosures:** [bulleted list — sheets, narratives, calculations, prior-correspondence references]

**cc:** [Owner / Owner's Rep / CM / Code Consultant / consultants]
```

## Workflow

1. Echo back: AHJ, project identifier, letter type, comment count, response-strategy mix. One line.
2. If any required input is missing — especially the **verbatim AHJ comment text** — list the gap and stop. Do **not** invent AHJ comment language from training.
3. If the user is citing an AHJ Information Bulletin / IR / Code Modification (`NYC DOB Buildings Bulletin 2014-026`, `LADBS IB-P/BC 2020-066`, `DSA IR 16-3`, etc.), confirm the exact number and current version with the user — do **not** recall from training. Optionally offer WebFetch from the AHJ's official portal:
   - NYC DOB Buildings Bulletins: `https://www.nyc.gov/site/buildings/codes/buildings-bulletins.page`
   - LADBS Information Bulletins: `https://www.ladbs.org/services/forms-publications/information-bulletins`
   - CA DSA Interpretations of Regulations: `https://www.dgs.ca.gov/DSA/Resources/page-content/resources-list-folder/interpretation-of-regulations-irs`
   Confirm with the user before fetching; the AHJ portal is the authoritative source.
4. If the user is invoking IBC §104.11 (Alternative Materials, Design and Methods), confirm the IBC edition adopted by the AHJ — `IBC 2024` is not universally adopted; many jurisdictions are still on `IBC 2018` or `IBC 2021`. Do **not** assume.
5. Produce the letter Markdown — one per-comment response block per AHJ comment.
6. After the draft, list any items flagged for follow-up (TBD revision tags, missing license #, missing Bulletin number, ambiguous AHJ contact name) so the user can resolve them before sending.

## NA AEC conventions

- **English only.** No Hangul.
- **Imperial-first** units (`ft`, `in`, `sf`); metric in parens only when useful.
- **Dates** use `Month DD, YYYY`.
- **AHJ names** — always specific. `NYC DOB`, `FDNY`, `LADBS`, `CA DSA`, `CA HCAI`, `NYC SCA`, `Toronto Building`, `GSA Region 2`, `USACE Buffalo District`. Never "the city" or "the AHJ".
- **AHJ identifiers** — match the AHJ's convention: `BIN` (NYC, 7 digits), `Job #` (LADBS), `DSA App #`, `HCAI Project #`, `Permit #`.
- **License #** — required for the signature block on AHJ correspondence in most NA jurisdictions. State + number (e.g., `NY 12345`, `CA C-67890`).
- **Roles** — `Architect of Record (AOR)`, `Project Architect`, `PIC`, `Code Consultant`, `Accessibility Consultant`. Never `Director` as a project role.
- **Code references** — `IBC 2018 §104.11` (verify AHJ-adopted edition), `IECC 2021 C402.1.3`, `ASCE 7-22 §11.4`, `2010 ADA §404`, `NFPA 101 §7.2`. Never invent edition years; ask the user for the AHJ-adopted edition.
- **Floor labels** — `Level 3`, `L3`, or `3rd floor`. Never `3F`.

## Constraints

- **AHJ comment text is user-supplied verbatim.** Never paraphrase or invent AHJ comment language. If the user has not pasted the comment, stop.
- **Information Bulletin / IR / Code Modification numbers are user-supplied or live-fetched.** Never recall AHJ bulletin numbers from training. NYC DOB, LADBS, DSA, FDNY all publish frequent updates.
- **IBC edition is user-confirmed.** AHJs adopt different editions (`IBC 2018` / `IBC 2021` / `IBC 2024`) on different schedules. Do not assume.
- **Alternative Materials / Design / Methods (AMM)** — `IBC §104.11` invocation must be explicitly authorized by the user; do not auto-classify a comment as an AMM request.
- **Code Modification application** — many AHJs require a separate application form (NYC DOB CMA, LADBS Modification, DSA Code Modification). This command does **not** generate the application form; it generates the cover letter. The user attaches the AHJ form.
- **License # required** — most NA AHJs require a stamped / signed letter from a licensed AOR. Flag if the user has not provided the license #.
- **Letterhead is implied** — the output template assumes the user pastes onto firm letterhead. Do not generate letterhead graphics.
- **Privileged / confidential markings** — do not add unless the user requests; AHJ correspondence is typically a public record under FOIL / FOIA / state public-records laws.

## Anti-patterns

- Inventing AHJ comment language. The AHJ wrote the comment; the user pastes it.
- Recalling NYC DOB / LADBS / DSA Bulletin numbers from training (`Buildings Bulletin 2014-026`, `IB-P/BC 2020-066`). User confirms; or live-fetch the AHJ portal.
- Assuming `IBC 2024` is adopted. Confirm with the user — many jurisdictions are still on `IBC 2018` / `2021`.
- Auto-classifying a comment as an Alternative Methods request (IBC §104.11). User decides response strategy.
- Generating an AHJ-specific Code Modification application (NYC CMA / LADBS Modification / DSA CM) form. Out of scope; user attaches the AHJ form.
- Drafting a letter without the AOR license # in the signature block. AHJs reject unsigned / unstamped correspondence.
- Paraphrasing AHJ comment text into "what they probably meant". Liability hazard.
- Using `Director` as a role.
- Using `3F` instead of `Level 3`.
- Using "the city" or "the AHJ" generically. Always name specifically.
