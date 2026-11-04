---
name: security-design-review
description: "Reads a plan for security as a property of the layout rather than as equipment added later: who is meant to be where and how the building tells them, where somebody can be unobserved, where the boundary between public and controlled actually falls, and what happens to all of it after hours when the staff who make it work have gone home. Works the design questions first, because a camera is what gets bought when the plan did not answer them. Trigger on \"security review\", \"CPTED\", \"is this plan secure\", \"where do we put the access control\", \"how do we secure this after hours\", \"security-design-review\", or a plan for a building with a controlled boundary. Carries no standards, no ratings and no requirements; the client's security policy, the operator's rules and any regulation come from you. It does not design systems, does not do threat assessment, and does not replace the security consultant or the Architect of Record."
license: MIT
metadata:
  title: "Security Design Review"
  summary: "Read a plan for how it will be misused, not for what it is called"
  discipline: "design-building-types"
  tags: "Review, Design"
---

# Security Design Review

Security arrives late, as a schedule of cameras and card readers on a plan that
was never asked the question. Almost everything that works is in the layout:
who can see what, where the boundary is, and whether the building tells people
where they are allowed to be without anybody having to enforce it.

## Scope and limits — read first

**What this does.** Reads the plan for the design questions: the boundary
between public and controlled, natural surveillance and where it fails,
wayfinding as a security device, and the after-hours case. Names what equipment
would then be for, and what it cannot fix.

**What this does not do.**

- **It carries no standards or requirements.** The client's security policy, an
  operator's rules, a regulator's requirements and any rating come from you.
- **It is not a threat assessment.** What this building is at risk from, and how
  much, is the client's and a security consultant's. This reads the plan against
  whatever they have said.
- It does not design systems. Cameras, access control, intrusion detection and
  their specification are the security consultant's and the electrical engineer's.
- It does not do life safety. Egress must not be compromised by anything here,
  and where the two conflict, `design-egress` and the code govern. Point at
  `senior-code-consultant`.
- It does not replace the security consultant or the Architect of Record.

**What you need before starting.** The plans, including the site. Who uses the
building, when, and who is meant to be where. The client's policy or their
concerns. The hours of operation and what changes outside them.

## Workflow

### Step 1. Establish who is meant to be where, and when

Ask, in one message:

> 1. Who uses the building: public, staff, visitors, contractors, deliveries,
>    children, patients, students, residents? Point at `circulation-study`.
> 2. Where is each group meant to be, and where not?
> 3. What is the client actually worried about? Theft, violence, a specific
>    person, a specific asset, unauthorised access, or an incident that already
>    happened?
> 4. What are the hours, and who is on site outside them?
> 5. Is there a policy, an operator's standard, or a regulator's requirement?
>    Quote it.
> 6. Who staffs the boundary, if anyone, and at what times?

**Question 6 is the one that decides whether the plan works.** A layout that
depends on somebody at a desk is a layout that fails at six o'clock, and most
plans depend on one without saying so.

### Step 2. Find where the boundary actually falls

The public-to-controlled boundary is drawn somewhere, and it is rarely where the
plan implies:

| Boundary | Where the plan puts it | Where it actually falls | What holds it |
|---|---|---|---|

- What is the first controlled door, and what is in front of it?
- Can somebody reach the lift lobby, the stair, or the washrooms before being
  seen or stopped?
- Is there a place a visitor waits, and is it inside or outside the boundary?
- Where do deliveries cross, and does the goods route reach controlled space?
- Do the fire stairs discharge into controlled space, and does that create a way
  in? Egress wins over security here, always, and the answer is a design one.
- Does the boundary hold at every level, or only at the entrance?

**A boundary held by one door on one floor is not a boundary.** Report every
place it is bypassed.

### Step 3. Find where somebody can be unobserved

Natural surveillance is the part of this that is free, and it is a plan
question:

- Which spaces are overlooked by ordinary use, and which are not?
- Where can somebody stand, wait, or work without being seen: behind a
  projection, in a recessed entrance, at the back of a car park, in a service
  yard, in an unstaffed corridor, in a stair?
- Are the routes people take at night the ones that are overlooked, or the
  short ones that are not?
- What is dark? Point at `senior-lighting-consultant`, and note that lighting a
  place nobody overlooks does not make it safer, it just makes it visible.
- Do the desks and rooms with people in them face the places that need watching,
  or away from them?

### Step 4. Read the layout as a set of instructions

A building that tells people where they may go needs less enforcement:

- Is it obvious, without a sign, where the public may go and where they may not?
- Does the route to reception pass anything it should not?
- Are the controlled doors obviously controlled, or do they look like any other
  door?
- Is there a clear front, so that arriving anywhere else feels wrong?
- Where the plan relies on a sign, note it. **Signs are what get used when the
  layout did not answer the question.**

### Step 5. Work the after-hours case, separately

Almost every plan works when staffed. Run the whole building again as if nobody
is there:

- Which doors are locked, and what does that do to the routes people still take?
- Who is in the building alone, and how do they get to their car?
- What is accessible from outside: a roof reachable from a wall, a service yard,
  a window over a canopy, an unlocked stair?
- What does a cleaner's or a contractor's access look like, and does it defeat
  the boundary?
- Does locking anything compromise egress? If so it is not an option, and the
  answer has to be a design one.

### Step 6. Report

- Where the boundary actually falls, and every place it is bypassed.
- Every unobserved place, with what would resolve it in the layout.
- Every point where the plan depends on a person, and what happens when they are
  not there.
- The after-hours findings, separately.
- What is left for equipment, and what equipment cannot fix.
- Any conflict between security and egress, named for the code consultant.

Close by saying no threat assessment was made and no system was designed.

### Step 7. Save, if asked

Ask whether to write the review to a file and where.

## Rules

- **Ask who staffs the boundary and when**, every run.
- Work the layout before naming any equipment.
- Report every place the boundary is bypassed, not only where it holds.
- Run the whole building again for the after-hours case.
- **Egress wins over security.** Name every conflict for the code consultant and
  never propose locking an exit.
- Note every place the plan relies on a sign.
- Never assess threat or specify a system.

## Anti-patterns

- Answering with a camera and a card reader schedule.
- Assuming a reception desk is staffed at all times.
- Lighting a place nobody overlooks and calling it safer.
- A boundary held on the ground floor and open on every other.
- Ignoring the fire stair as a way in.
- Reviewing the staffed case only.
- Proposing anything that locks an exit.
- Relying on signage where the layout could have answered it.

## Resources

None. This skill is one file. Output is written directly at the path you choose.
