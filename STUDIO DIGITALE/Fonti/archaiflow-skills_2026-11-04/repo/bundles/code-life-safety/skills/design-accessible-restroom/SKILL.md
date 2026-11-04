---
name: design-accessible-restroom
description: "Lays out an accessible restroom or toilet room as a set of overlapping clearances rather than as a list of items to tick: establishes which clearances may overlap and which may not from the standard you quote, places the fixtures in the order that constrains the plan most, works the door swing against the clear floor space it eats, and reports every dimension as a question rather than an answer. Trigger on \"accessible restroom layout\", \"toilet room won't fit\", \"ADA bathroom\", \"single-user accessible washroom\", \"turning circle in the toilet\", \"design-accessible-restroom\", or a toilet room plan with a request for whether it works. Carries no dimensions, no clearances and no reach ranges; every one is text you quote from the standard your jurisdiction adopts, which is not always the one you expect. For checking one clearance already dimensioned use `/test-ada`; for a project-wide record use `ada-tracker`. It does not replace the accessibility consultant or the Architect of Record."
license: MIT
metadata:
  title: "Design Accessible Restroom"
  summary: "Lay out an accessible restroom from clearances that overlap, not a checklist"
  discipline: "code-life-safety"
  tags: "Design"
---

# Design Accessible Restroom

Accessible restrooms fail as plans, not as checklists. Every item on the list
can be present and the room can still be unusable, because the clearances
overlap each other and the door and the fixtures compete for the same floor.
This lays the room out in the order that the constraints actually bind.

## Scope and limits — read first

**What this does.** Takes the standard your jurisdiction adopts, quoted, and the
room you have. Establishes which clearances are permitted to overlap and which
are not, because that is the rule the whole layout turns on. Places the elements
in order of how much they constrain the plan, works the door against the floor
space it consumes, and reports what does not fit and by how much, in terms of
the dimensions you supplied.

**What this does not do.**

- **It carries no dimensions.** No clear floor space, no turning space, no
  centreline distances, no grab bar lengths or heights, no reach ranges, no door
  manoeuvring clearances. Every one comes from the standard you quote.
- **It does not know which standard applies to you.** The federal standard, a
  state or provincial one, a local amendment and the referenced technical
  standard in your building code can all differ, and a project can be subject to
  more than one at once. Name yours; the skill will not choose.
- It does not check a dimension already drawn. `/test-ada` does that for one
  clearance against a quoted source.
- It does not track the project. `ada-tracker` keeps the record.
- It does not decide how many accessible rooms are required, or how they are
  distributed. That is scoping, and it is a different part of the standard.
- It does not cover ambulatory stalls, children's dimensions, or specialised
  rooms unless you supply that part of the standard too.
- It does not replace the accessibility consultant or the Architect of Record.

**What you need before starting.** The standard, named and with the relevant
sections quoted or pasted. The room: its dimensions, its structure, where the
door has to be and which way it can swing. The fixture schedule. Whether this is
a single-user room or a multi-stall room, because the rules differ. Any
constraint already fixed: a shaft, a beam, a chase, a corridor line.

## Workflow

### Step 1. Establish the standard and the room

Ask, in one message:

> 1. Which standard applies, and is more than one in play? Quote or paste the
>    sections for clear floor space, turning space, fixture clearances, grab
>    bars, door manoeuvring and reach.
> 2. Single-user or multi-stall?
> 3. The room dimensions, structure and ceiling, with anything already fixed.
> 4. Where must the door be, which way can it swing, and is it in or out?
> 5. The fixtures required, from the count and from the programme.
> 6. Anything already committed: a chase location, a corridor wall, a window.

If no standard is quoted, stop. Say plainly that a layout produced without the
text is a drawing that has not been checked against anything.

### Step 2. Establish the overlap rule before placing anything

This is the step that decides the room. From the quoted text, state:

- Which clearances may overlap one another.
- Which may not.
- Whether the turning space may overlap the fixtures' clear floor spaces, and
  under what conditions.
- Whether the door swing may enter any of them.

Present as a table:

| Clearance | May overlap | May not overlap | Source quoted |
|---|---|---|---|

A room laid out on the assumption that everything may overlap will be too small
by exactly the amount nobody noticed.

### Step 3. Place in order of constraint, not in order of the checklist

Work in this order and say why each placement was forced:

1. **Turning space.** Largest single demand; it decides the room's shape.
2. **The water closet and its clear floor space.** Second most constrained, and
   its side approach fixes the wall it sits on.
3. **Grab bars.** They fix the walls behind and beside the water closet, which
   means they fix the structure and any chase.
4. **The lavatory and its clear floor space and knee clearance.** Knee clearance
   competes with the plumbing behind it.
5. **The door and its manoeuvring clearance**, both sides, plus what the swing
   consumes if it swings in.
6. **Everything else**: dispensers, mirrors, hooks, the mounted heights that
   come from reach ranges.

At each placement, name the dimension needed and leave it as a question. Do not
fill it.

### Step 4. Work the door against the floor it eats

The door gets its own step because it is the most common reason a room that
passes on paper fails in use. Report:

- What the manoeuvring clearance is on each side, and what fixes it: swing
  direction, approach side, whether the door is latched or closer-equipped.
- Whether the swing enters any clear floor space, and whether the standard
  permits that here.
- What happens if the door has to swing out: does it obstruct the corridor, an
  egress path, or another door?
- Whether the room can be exited by someone who has transferred, which is a
  usability question the standard may not fully answer.

### Step 5. Report what does not fit, and by how much

| Element | Required (quoted) | Available in this room | Short by | Source |
|---|---|---|---|---|

Then:

- The shortfalls, largest first, with what would resolve each: more room, a
  different door swing, a moved chase, a different fixture.
- Every dimension still open, counted.
- Whether the room is subject to more than one standard, and whether the stricter
  one was applied throughout or only in places.

Close with the standing limits: the standard was quoted rather than known, the
scoping question was not addressed, and this is not accessibility review.

### Step 6. Save, if asked

Ask whether to write the layout notes to a file and where.

## Rules

- **Never supply a dimension.** Not a clearance, not a height, not a reach, not
  as a placeholder that looks like a number.
- **Never choose the standard for the user**, and never assume one standard when
  two may apply.
- Establish the overlap rule before placing anything.
- Place in order of constraint, and say what forced each placement.
- The door gets its own pass, every run.
- Report shortfalls as measurements against quoted requirements, never as a
  verdict on compliance.
- Quoting a clause found by web search is not quoting the standard. Search
  identifies which document governs; it does not verify its text.

## Anti-patterns

- Working from a checklist of items rather than from overlapping clearances.
- Recalling a turning diameter or a grab bar height because the figure is
  familiar.
- Assuming the federal standard applies without asking about state, provincial
  or local ones.
- Placing the lavatory before the water closet, which produces a room that
  cannot be fixed later without moving a chase.
- Treating the door as trim to be resolved at the end.
- Declaring the room compliant. It is measured against what you quoted.
- Applying multi-stall rules to a single-user room, or the reverse.

## Resources

None. This skill is one file. Output is written directly at the path you choose.
