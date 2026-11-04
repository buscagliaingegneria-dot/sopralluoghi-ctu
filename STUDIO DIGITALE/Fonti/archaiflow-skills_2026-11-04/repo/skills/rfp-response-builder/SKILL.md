---
name: rfp-response-builder
description: "Builds an RFP or RFQ response around the evaluation criteria rather than around the practice's usual material: pulls every requirement and every question out of the document into a compliance matrix, follows the issuer's structure and numbering exactly, and checks before submission that every requirement has an answer and every page limit and format rule is met. Trigger on \"respond to this RFP\", \"RFQ response\", \"build the proposal response\", \"do we answer everything in this RFP\", \"rfp-response-builder\", or a solicitation handed over to answer. Carries no boilerplate and no standard firm material; everything comes from the practice's own content. For a federal qualifications package use `sf330-builder`; to decide whether to respond at all use `go-no-go-review` first. It does not decide the fee and does not replace the principal."
license: MIT
metadata:
  title: "RFP Response Builder"
  summary: "Build a response that answers what was asked, in their order"
  discipline: "practice-contracts"
  tags: "Documentation"
---

# RFP Response Builder

Responses are eliminated before they are read on merit. A missing form, an
exceeded page count, an unanswered sub-question, a section in the wrong order:
each one is a reason to set the submission aside, and the evaluator has forty
others.

## Scope and limits — read first

**What this does.** Extracts every requirement and every question into a matrix,
builds the response in the issuer's own structure and numbering, and runs a
compliance check before submission.

**What this does not do.**

- **It carries no boilerplate.** Firm description, approach, project sheets and
  résumés come from the practice. Generic content written to fill a section is
  visible to an evaluator who reads twenty of them.
- It does not decide whether to respond. `go-no-go-review` does.
- It does not set the fee. `fee-estimator` does.
- It does not build a federal qualifications package. `sf330-builder` does.
- It does not write the technical approach for you. It structures it, asks the
  questions the criteria imply, and checks it answers them.
- It does not replace the principal, who signs.

**What you need before starting.** The solicitation, complete, with every
addendum. The evaluation criteria. The submission requirements: format, page
limits, file naming, delivery method, deadline. Your firm material. The team.

## Workflow

### Step 1. Read the solicitation for its rules before its questions

Ask, in one message:

> 1. Do you have the complete document and every addendum? Addenda change
>    requirements and are missed.
> 2. What are the evaluation criteria, and are they weighted?
> 3. What are the submission mechanics: format, page limit, font and margin
>    rules, file naming, number of copies, portal or email, deadline and time
>    zone?
> 4. Is there a questions deadline, and has it passed?
> 5. Are there mandatory forms, certifications, or acknowledgements?
> 6. Is there a mandatory pre-submission meeting or site visit?

**Mechanics before content, every time.** A response that cannot be submitted is
worth nothing, and the mechanics are where most eliminations happen.

### Step 2. Build the compliance matrix

Go through the document line by line and extract every requirement, including
the ones embedded in prose and the ones in the sample contract.

| # | Requirement or question | Where in RFP | Type | Answer location | Status |
|---|---|---|---|---|---|

`Type` is `mandatory form`, `question to answer`, `document to provide`,
`certification`, or `format rule`.

**Split every multi-part question.** A question asking about approach, team and
schedule in one sentence is three requirements, and an answer covering two of
them scores as an answer covering two of them.

Report the count of requirements found. It is always more than anyone expects.

### Step 3. Map the evaluation criteria onto the response

The criteria are what the evaluator scores. For each:

| Criterion | Weight | Where we address it | How strongly |
|---|---|---|---|

Where a criterion is weighted heavily and addressed briefly, say so. Practices
routinely write most about what they find most interesting, which is rarely what
is weighted most.

### Step 4. Build in the issuer's structure, not the practice's

Follow their section order and their numbering exactly, even where it is
illogical. An evaluator scores with the criteria in front of them and looks for
each answer where the RFP said it would be.

For each section:

- Answer the question asked, first sentence.
- Then the evidence: a project, a name, a number, a result.
- Then, if it fits, what is distinctive.

Never open a section with firm history. Never answer a question the RFP did not
ask because the material was to hand.

### Step 5. Check the specifics that get generalised

Three places responses go generic and evaluators notice:

- **Approach.** Does it name anything about this project, this site, this
  client? An approach that would fit any project in the sector is scored as one.
- **Team.** Are the named people actually available, and does the response say
  what each one will do on this project rather than what they have done?
- **Project sheets.** Does each one relate to a criterion? A project included
  because it is impressive, rather than because it is relevant, spends a page.

### Step 6. Run the compliance check before submission

Against the matrix:

- Every requirement with a status. `not addressed` listed first.
- Every mandatory form, signed and included.
- Page count against the limit, per section where sectional limits apply.
- Format rules: font, margins, file naming, file size, number of copies.
- Every addendum acknowledged.
- Deadline, time zone, and delivery method confirmed.
- Every question in the matrix traced to a location in the response.

**Report the unaddressed count before anything else.** This is the check that
saves submissions.

### Step 7. Save

Ask where. Keep the matrix beside the response; it becomes the debrief document
and the starting point for the next one from the same issuer.

## Rules

- **Never supply boilerplate.**
- Read the mechanics before the questions.
- Extract every requirement, including those embedded in prose and in the sample
  contract.
- Split every multi-part question.
- Follow the issuer's structure and numbering exactly.
- Report the `not addressed` count first in the compliance check.
- Never answer a question that was not asked.

## Anti-patterns

- Starting with the firm's standard proposal and editing it toward the RFP.
- Reorganising the response into a more logical order.
- Missing an addendum.
- Answering a three-part question in one paragraph.
- Including a project because it is the best work rather than the most relevant.
- Naming people who will not be available.
- Exceeding a page limit and hoping.
- Submitting without tracing every matrix row to a location.

## Resources

None. This skill is one file. Output is written directly at the path you choose.
