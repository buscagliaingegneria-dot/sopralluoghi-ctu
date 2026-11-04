---
name: meeting-notes-cleaner
description: "This skill should be used when the user provides raw architectural project meeting notes — transcripts, STT output, .vtt/.srt files, or jotted text — and needs structured action items. Trigger on 'clean up meeting notes', 'meeting summary', 'process this transcript', or pasted multi-speaker content covering project decisions, schedule, or scope. Generates a structured meeting markdown in `docs/meetings/` and merges new To-dos into the project's `docs/todos.md`."
license: MIT
metadata:
  title: "Meeting Notes"
  summary: "Turn raw meeting notes into structured action items"
  discipline: "practice-contracts"
  tags: "Pre-Design"
---


# Meeting Notes Cleaner


## Overview


Turn raw meeting content into a clean post-meeting document and propagate the action items into the project's todo list.


## Scope and limits — read first


**What this does.** Turns a transcript or a page of notes into a structured
record in `docs/meetings/`: attendees, decisions, to-dos with owners and dates,
open issues, and the next agenda. Each to-do is merged into `docs/todos.md` with
a link back to the meeting it came from.

**What this does not do.**

- **It does not assign an owner or a date nobody said.** A to-do with no clear
  owner becomes an issue instead, and a to-do with no date is due at the next
  meeting. Neither is inferred from who usually does that kind of work.
- It does not summarise the discussion. Decisions and tasks come out; the
  narrative does not.
- It does not add analysis, advice, or a view on what was decided.
- It does not transcribe audio. It takes text: a transcript, an STT export, a
  `.vtt` or `.srt` file, or typed notes.
- It does not circulate the minutes or notify anyone. It writes files.

**What you need before starting.** The meeting text, and the meeting date if the
file does not carry one. Attendee roles help route the to-dos, and where a role
is not stated the task stays unassigned rather than being guessed at.

## When to use


Trigger on:

- Pasted meeting transcripts (multi-speaker text).
- STT output from a recording.
- File path to a `.vtt`, `.srt`, or `.txt` transcript.
- Explicit asks: "clean up meeting notes", "meeting summary", "process this transcript".

Do NOT trigger for general meeting questions ("how should I run this meeting"). This skill processes existing meeting content.


## Workflow


### Step 1 — Bootstrap if needed


Check `docs/meetings/index.md` and `docs/todos.md` exist. If not:


```bash
python scripts/init_meetings_workspace.py
```


### Step 2 — Read the transcript


If the user gave a file path, use `Read` to load it. `.vtt`/`.srt` files include timecodes — strip them while reading. If the user pasted text directly, use it as-is.


### Step 3 — Identify


Pull from the transcript:

- **Date** of meeting (or use today if unknown)
- **Attendees** (with roles where stated)
- **Decisions** (statements confirmed in the meeting)
- **To-dos** (with discipline-routed owner — see `references/discipline_routing.md`)
- **Issues / Risks** (open items, cross-discipline conflicts, external dependencies)
- **Next meeting agenda** (items implied as needing follow-up)

Convert all relative dates ("next Tuesday", "by end of next week") to absolute ISO dates from today.


### Step 4 — Write the meeting note


Read `assets/meeting-template.md`. Fill placeholders. Filename:


`docs/meetings/<YYYY-MM-DD>-<topic-slug>.md`


Slug rule: lowercase, `[^a-z0-9-]` removed, max 40 chars, derived from the meeting subject (`design-coordination`, `milestone-review-3`). If duplicate, suffix `-<n>`.


### Step 5 — Merge To-dos into the project todo list


For each To-do extracted, run:


```bash
python scripts/append_todos.py \
  --meeting 2026-05-06-design-coordination \
  --owner "MEP lead" \
  --task "Review Level 3 ceiling height" \
  --due 2026-05-12
```


The script appends each To-do to `docs/todos.md` with a back-reference to the source meeting file. Skips duplicates idempotently.


### Step 6 — Update the meeting index


```bash
python scripts/append_to_index.py \
  --date 2026-05-06 \
  --slug design-coordination \
  --attendees "Architect, Contractor, Owner" \
  --decision-count 3 \
  --todo-count 5
```


### Step 7 — Report


Tell the user:

- Path to the meeting note
- Path to the updated todos file
- The headline decision
- The most time-critical To-do

## Rules

- Strip filler from STT input ("uh...", "you know", "um", repeated half-sentences).
- Convert relative dates to absolute ISO dates based on today.
- A To-do without a clear owner is an Issue — move to the Issues section rather than guessing the owner.
- A To-do without a clear date defaults to "next meeting" — never invent specific dates.
- Do not assign tasks to people whose role is not explicit in the transcript.

## Anti-patterns

- Summarizing the meeting narratively ("the team discussed..."). The user wants decisions and tasks, not a story.
- Adding commentary or analysis. This skill transcribes structure, it does not coach.
- Editing `index.md` or `todos.md` manually with the Edit tool. Use the scripts.

## Resources

- `scripts/init_meetings_workspace.py` — bootstrap `docs/meetings/`, the meetings index, and `docs/todos.md`
- `scripts/append_to_index.py` — append a row to `docs/meetings/index.md`
- `scripts/append_todos.py` — merge a To-do into `docs/todos.md` with meeting back-reference
- `references/discipline_routing.md` — map verbs/topics to the right owner role
- `assets/meeting-template.md` — meeting markdown template
