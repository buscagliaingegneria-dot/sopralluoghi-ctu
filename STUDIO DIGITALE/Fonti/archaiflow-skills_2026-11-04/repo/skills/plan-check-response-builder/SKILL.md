---
name: plan-check-response-builder
description: "Turns a plan check or plan review comment set into a response matrix that answers every comment individually and on the record: splits comments that contain more than one question, sorts each into agreed, clarification, or disagreement, points every response at the specific sheet and detail that changed, and keeps the disagreements civil and evidenced because those are the ones that get read twice. Trigger on \"plan check comments\", \"respond to the plan reviewer\", \"correction letter\", \"plan review response\", \"resubmittal response matrix\", \"plan-check-response-builder\", or a set of reviewer comments pasted with a request to answer them. Carries no code positions of its own and never argues a clause from memory; every response either cites the drawing that changed or quotes the code text you supply. For a letter to the department rather than a comment matrix use `/draft-letter`; for tracking the submission itself use `permit-tracker`."
license: MIT
metadata:
  title: "Plan Check Response Builder"
  summary: "Turn a reviewer's comments into a matrix that answers each one on the record"
  discipline: "code-life-safety"
  tags: "Documentation"
---

# Plan Check Response Builder

A resubmittal is judged on whether every comment was answered, not on whether
the design is right. One comment answered in a paragraph that covers three
others leaves two of them looking ignored, and the set comes back.

## Scope and limits — read first

**What this does.** Takes the reviewer's comment set, splits it into individually
numbered items, sorts each into one of three kinds of response, and builds the
matrix. For each response it names the sheet, detail or document that
substantiates it, so the reviewer can find the change without hunting.

**What this does not do.**

- **It holds no code positions.** Where a response depends on what the code says,
  the code text comes from you, quoted. It will not argue a clause from
  recollection, and a disagreement built on a remembered clause is how a
  resubmittal turns into three.
- It does not decide whether to agree. Whether to make the change or to argue is
  a professional judgement with cost and schedule behind it. The skill sorts,
  drafts and makes sure nothing is missed.
- It does not make the drawing changes. It records which sheet has to change and
  flags any response pointing at a change that has not been made yet.
- It does not write a letter. `/draft-letter` does that where a letter is what
  is wanted.
- It does not submit, and it does not track the submission. `permit-tracker`
  holds the record.
- It does not replace the code consultant or the Architect of Record.

**What you need before starting.** The comment set as issued, complete and
unedited. The submission it responds to. Any code text you intend to rely on,
quoted. Who owns each discipline's response. Whether there is a resubmittal
deadline.

## Workflow

### Step 1. Take the comments exactly as issued

Ask for the comment set verbatim, with its reference and date. Then:

- Number every comment as the reviewer numbered it. **Never renumber.** The
  reviewer will read down their own list.
- **Split any comment containing more than one question** into sub-items, keeping
  the reviewer's number and adding a letter. A comment asking about both the
  rating and the door in one sentence is two comments and one of them will be
  missed.
- Flag any comment you cannot parse, and say it will be asked about rather than
  guessed at.

Report the count of comments as issued and the count after splitting. The
difference is usually where resubmittals get lost.

### Step 2. Sort every item into one of three

| Kind | What it means | What the response must carry |
|---|---|---|
| Agreed | The change is being made | The sheet and detail where it appears |
| Clarification | Nothing changes; the information was already there or was misread | Where it already is, and why it was hard to find |
| Disagreement | The comment is being contested | The quoted code text, and the argument |

Sort every item. Anything unsorted is a comment nobody has decided about, and it
gets reported as such rather than drafted.

Say plainly how many disagreements there are. A response matrix that disagrees
with most of the set is a conversation to have with the reviewer before it is
submitted, not after.

### Step 3. Draft each response to its own kind

**Agreed.** One or two sentences. What changed, and where. Name the sheet
number, the detail reference, the revision cloud. Do not explain why the
reviewer was right; it reads as padding.

**Clarification.** Say where the information is, in sheet and detail. Then say
what made it hard to find, and whether anything has been done about that. A
clarification that blames the reviewer for not looking is a clarification that
gets a second comment.

**Disagreement.** The longest and the most careful:

- State the reviewer's position accurately first, in your own words, so it is
  clear it was understood.
- Quote the code text relied on, with its section, verbatim from what you
  supplied.
- State the argument, in order.
- Say what would change if the reviewer maintains the position.
- Offer the conversation. A disagreement with no route to resolution costs a
  full review cycle.

Never characterise the reviewer or the review. The matrix is read by the person
it is about.

### Step 4. Point every response at something real

For each response, name the substantiating document and check it exists:

| # | Kind | Response points at | Exists? | Owner |
|---|---|---|---|---|

Flag every row where the response points at a change that has not been made yet.
This is the failure that produces a second correction letter: a matrix promising
a sheet that went out unchanged.

### Step 5. Report and assemble

- The comment count as issued and after splitting.
- Counts by kind, disagreements stated first.
- Every unsorted item.
- Every response pointing at a change that does not yet exist.
- Every disagreement whose code text was not supplied, listed individually,
  because those cannot be drafted.
- The matrix itself, in the reviewer's numbering order.

### Step 6. Save, if asked

Ask whether to write the matrix to a file and where. Ask about format: many
departments require their own, and a matrix in the wrong format is returned
without being read.

## Rules

- **Never renumber the reviewer's comments.**
- **Split every multi-part comment**, and report the count difference.
- **Never argue a code position from memory.** Quoted text or no argument.
- Every response names the sheet or document that substantiates it.
- Flag every response that points at a change not yet made.
- Never characterise the reviewer, the department, or the quality of the review.
- Unsorted items are reported, never drafted around.

## Anti-patterns

- Answering three comments in one paragraph.
- Renumbering into a tidier order.
- Writing "see revised drawings" with no sheet number.
- Building a disagreement on a recalled clause.
- Quoting a code section found by web search rather than from the text supplied.
- Explaining at length why an agreed comment was correct.
- Submitting a matrix that promises changes the set does not contain.
- Any sentence that reads as annoyed. It will be read by the person reviewing
  the resubmittal.

## Resources

None. This skill is one file. Output is written directly at the path you choose.
