---
name: alternative-means-builder
description: "Assembles an alternative means and methods request as an argument rather than a form: establishes the prescriptive requirement that cannot be met and why, states the intent behind that requirement in the code's own words, sets out what is proposed and how it meets that intent, and gathers the evidence, the compensating measures and the conditions the applicant is willing to accept. Trigger on \"alternative means and methods\", \"AMMR\", \"code modification request\", \"equivalency request\", \"we cannot meet this section, what now\", \"alternative-means-builder\", or a prescriptive requirement named as unachievable with a request to make the case. Carries no code text, no precedent from other jurisdictions and no performance criteria; the requirement, its stated intent and any referenced standard all come from documents you supply. It does not approve anything, does not perform fire modelling or engineering analysis, and does not replace the fire protection engineer, the code consultant, or the Architect of Record."
license: MIT
metadata:
  title: "Alternative Means Builder"
  summary: "Make the case that an alternative meets the intent of a rule you cannot meet"
  discipline: "code-life-safety"
  tags: "Documentation"
---

# Alternative Means Builder

An alternative means request is refused for one of two reasons: it argues that
the requirement is inconvenient rather than that the intent is met another way,
or it asks the official to take the applicant's word for something. Both are
avoidable, and both are decided before anything is written.

## Scope and limits — read first

**What this does.** Builds the case in the order an official reads it: the
requirement, why it cannot be met, what the requirement is for, how the proposal
serves that purpose, what evidence supports it, what compensates for the
shortfall, and what conditions the applicant will accept. Then tests the case
against the objections it will meet.

**What this does not do.**

- **It carries no code text and no intent statements.** The section, the
  commentary or intent language, and any referenced standard all come from you,
  quoted. An intent argued from what the requirement seems to be for is the
  weakest kind of submission.
- **It carries no precedent.** What another jurisdiction accepted is not
  evidence in this one, and a recalled precedent is worse than none. Where you
  have a documented approval, it goes in as a document with a reference.
- **It performs no analysis.** Fire modelling, egress modelling, timed
  evacuation, smoke control calculation, structural analysis: all engineering,
  by a qualified engineer, and the request cites their report. This assembles;
  it does not compute.
- It does not decide whether to submit. Whether to seek an alternative or to
  redesign is a judgement about cost, programme and risk.
- It does not approve, and it does not predict approval.
- It does not replace the fire protection engineer, the code consultant, or the
  Architect of Record.

**What you need before starting.** The section that cannot be met, quoted in
full. Its intent or commentary, if the code publishes one. Why it cannot be met,
concretely. What is proposed instead. Any engineering analysis, with its author.
The authority's own procedure for these requests, because it usually prescribes
the format.

## Workflow

### Step 1. Establish the requirement and why it fails

Ask, in one message:

> 1. Quote the section that cannot be met, in full, with its edition.
> 2. Does the code publish intent or commentary for it? Quote that too.
> 3. Why can it not be met? Physically impossible, an existing building
>    condition, a conflict with another requirement, a preservation constraint,
>    or cost?
> 4. What is proposed instead?
> 5. What analysis exists, and who performed it?
> 6. What is the authority's own procedure and format for these requests?
> 7. Has the authority been approached informally, and what was said?

Question 3 decides whether there is a case. **Cost alone is rarely a basis.** If
that is the honest answer, say so plainly before anything is drafted, and say
that the request will be read as asking for relief rather than equivalency. That
is a conversation to have now.

### Step 2. State the intent in the code's words, not yours

Set out what the requirement exists to achieve, quoting the published intent or
commentary. If the code publishes none, say so explicitly and state the intent
as the applicant's reading, labelled as such.

This is the hinge of the whole request. Everything after is measured against it,
and an intent the applicant invented to be easy to meet is the objection the
reviewer will raise first.

### Step 3. Set out the proposal against the intent, point by point

| Intent element (quoted) | How the prescriptive requirement serves it | How the proposal serves it | Evidence |
|---|---|---|---|

One row per element of the intent. Not a general claim of equivalency; a
demonstration for each thing the requirement was doing.

Where a row has no evidence column filled, that row is a gap, and gaps get
counted rather than smoothed over.

### Step 4. Separate compensating measures from the proposal itself

Two different things that get merged:

- **The proposal.** What is being done instead, which meets the intent.
- **Compensating measures.** Additional provisions offered because the proposal
  does not fully meet the intent on some element.

State them separately. A request that presents compensating measures as though
they were the equivalency is a request that has conceded the argument without
noticing.

For each compensating measure, say who maintains it and for how long. A measure
that depends on an operational procedure needs an owner and a mechanism, or it
lapses at the first change of tenant.

### Step 5. Offer conditions, and test the case against its objections

**Conditions.** What the applicant will accept as a condition of approval:
recording on the certificate of occupancy, periodic testing, a maintenance
agreement, a restriction on use or occupant load, a limit on the approval's
transferability. Officials approve more readily when the applicant has already
named the constraints.

**Objections.** Then attack the case:

- Which element of the intent is least well served, and what is the answer to
  that?
- What does this set as a precedent in this jurisdiction, and would the official
  be comfortable with the next applicant citing it?
- What happens if the compensating measure fails or is removed?
- Is there a redesign that avoids the request entirely, and has it been costed?
  If not, the official will ask.

Report the weakest element by name. A request that does not know its own weak
point will be told what it is.

### Step 6. Assemble in the authority's format and report

- The request, in the order above, in the authority's format if one was given.
- The evidence list, with each item's author and reference.
- Counts: intent elements addressed, intent elements with no evidence,
  compensating measures, conditions offered.
- Every place the case rests on something not supplied, listed individually.

Close with the standing limits: nothing was recalled, no analysis was performed
here, no precedent was cited, and approval is the authority's alone.

### Step 7. Save, if asked

Ask whether to write the request to a file and where.

## Rules

- **Never supply code text, intent language, or a referenced standard.**
- **Never cite a precedent from another jurisdiction** unless the user supplies
  it as a document with a reference.
- **Never perform the analysis.** Cite the engineer's report or state that none
  exists.
- Say plainly when cost is the only reason the requirement cannot be met.
- Address the intent element by element, never as a general claim of
  equivalency.
- Keep compensating measures separate from the proposal.
- Name the weakest element of the case in the output, every run.
- Never predict approval.

## Anti-patterns

- Arguing that the requirement is unreasonable rather than that the intent is
  met.
- Stating the intent in the applicant's words when the code publishes its own.
- Presenting compensating measures as the equivalency argument.
- Citing what another jurisdiction accepted from recollection.
- Claiming a modelling result without the engineer's report behind it.
- Offering no conditions, which asks the official to take on the whole risk.
- Submitting in a format other than the one the authority prescribes.
- Hiding the weakest element rather than answering it.

## Resources

None. This skill is one file. Output is written directly at the path you choose.
