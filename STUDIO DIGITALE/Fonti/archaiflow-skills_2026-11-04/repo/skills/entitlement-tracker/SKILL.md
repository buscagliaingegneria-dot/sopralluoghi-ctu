---
name: entitlement-tracker
description: "Keeps one dated record of a discretionary land use approval, which behaves nothing like a permit: the decision-maker is a body that meets on a calendar, the outcome is negotiated rather than checked, and the conditions attached at the end become obligations the project carries for its life. Logs every submission, every hearing, every commitment made in a room, and every condition with what discharges it and who owns it. Trigger on \"entitlement tracker\", \"track the rezoning\", \"planning approval log\", \"what did we commit to at the hearing\", \"conditions of approval\", \"entitlement-tracker\", or a discretionary application handed over to keep track of. Carries no process, no timelines and no hearing calendars; all come from the jurisdiction. It does not track building permits — `permit-tracker` does — and does not replace the land use attorney, the planner, or the Architect of Record."
license: MIT
metadata:
  title: "Entitlement Tracker"
  summary: "Track a discretionary approval from application through hearings to conditions"
  discipline: "code-life-safety"
  tags: "Tracking"
---

# Entitlement Tracker

A building permit is checked against rules. An entitlement is decided by people
in a room, on a calendar, after a negotiation, and the record of what was
promised to get it is usually nobody's job. Two years later the conditions
arrive as obligations and half of them are a surprise.

## Scope and limits — read first

**What this does.** Keeps one dated log per application. Records the process as
the jurisdiction defines it, every submission and hearing, every commitment made
verbally or in writing, and every condition of approval with what discharges it
and who owns it.

**What this does not do.**

- **It carries no process and no timelines.** What approvals exist, who decides,
  how notice works, what the appeal period is: all from the jurisdiction, and
  they vary between adjacent municipalities.
- **It predicts no outcome.** Discretionary means discretionary. A previous
  approval for a similar project is not a forecast and does not go in the log as
  one.
- It does not track building permits. `permit-tracker` does, and this records
  where an entitlement gates one.
- It does not write the application or the findings.
  `variance-request-builder` builds a case; this records what happened to it.
- It does not give legal advice or advise on appeal.
- It does not replace the land use attorney, the planner, or the Architect of
  Record.

**What you need before starting.** The jurisdiction and which approvals are
sought. The process as the jurisdiction publishes it. Who represents the project.
Whether there is opposition. The target dates.

## Workflow

### Step 1. Record the process as the jurisdiction defines it

Ask, in one message:

> 1. Which approvals are sought, and which body decides each?
> 2. What is the published process for each: submission, completeness review,
>    staff report, notice, hearing, decision, appeal period?
> 3. What is the hearing calendar, and what is the cut-off for an item to reach
>    a given meeting? Missing a cut-off costs a full cycle.
> 4. Who represents the project: attorney, planner, architect, owner?
> 5. Is there known opposition, an interested neighbourhood group, or a prior
>    application on this site?
> 6. What does each approval gate?

The cut-off dates in question 3 are the thing this log is most useful for. They
are published, they are inflexible, and they are missed.

### Step 2. Log submissions and staff interaction

| # | Event | Date | With whom | What was said | Written? | Reference |
|---|---|---|---|---|---|---|

Include pre-application meetings, completeness letters, staff comments, and
every call. **Mark verbal separately from written**, always. Staff positions
given verbally change, and a project that relied on one needs to know it was
verbal.

Log the staff report when it comes, and log its recommendation.

### Step 3. Log every hearing, and every commitment made in one

For each hearing:

- Date, body, agenda item, who attended for the project.
- What the project presented, and what changed from the submission.
- What was said by the body, by staff, and by the public.
- **Every commitment the project made in the room.** This is the entry that
  matters. Design changes offered under questioning, operational promises,
  community benefits, phasing commitments: each becomes a condition or an
  expectation, and none of them is in any drawing.
- The outcome: approved, approved with conditions, continued, denied.

A continuance gets logged with why and what has to happen before the next date.

### Step 4. Log every condition, with what discharges it

| # | Condition | Quoted | Discharged by | Owner | When due | Status |
|---|---|---|---|---|---|---|

Conditions come in kinds that behave differently and the log separates them:

- **Before permit.** Gates the building permit. `permit-tracker` needs these.
- **Before occupancy.** Discovered late, expensively.
- **Ongoing.** Operational obligations that run for the life of the building and
  bind an owner who may not be this one.
- **Recorded.** Attached to the land, surviving sale.

Every condition has exactly one owner. **Two owners means none.**

### Step 5. Track the expiry and what restarts it

Entitlements lapse. Record the expiry, what constitutes commencement, whether an
extension is available and what it requires, and what happens to the approval if
it lapses. Where phased, record each phase's expiry separately.

### Step 6. Read back

On request and at every milestone:

- Next cut-off date and what has to be submitted for it.
- Conditions by kind, with `before permit` first.
- Conditions with no owner.
- Every commitment made in a hearing that has not become a condition or a
  drawing. These are the ones that get forgotten and then remembered by
  somebody else.
- Verbal staff positions the project is relying on.
- Expiry dates approaching.

Report elapsed time only. Never predict an outcome or a date.

### Step 7. Write the log

One dated file per application, appended to rather than rewritten. Ask where it
lives on the first run and use the same path after.

## Rules

- **Never supply a process, a timeline, or a hearing calendar.**
- **Never predict an outcome.** Discretionary approvals are not forecastable and
  a prior approval is not precedent.
- Mark every verbal position as verbal.
- Log every commitment made in a hearing, in the room's words.
- Every condition has one owner, or is flagged as having none.
- Separate conditions by kind, and lead with `before permit`.
- Append; never rewrite an earlier entry.

## Anti-patterns

- Logging only written correspondence.
- Treating a staff recommendation as the decision.
- Losing the design change offered under questioning at a hearing.
- Recording conditions as one list with no kinds.
- Missing a hearing cut-off because the log tracked the hearing date.
- Predicting approval from a similar project.
- Assuming an ongoing condition ends at occupancy.
- Rewriting a condition entry when it is renegotiated. Log the change.

## Resources

None. This skill is one file. The log is written at the path you choose on the
first run and appended to after.
