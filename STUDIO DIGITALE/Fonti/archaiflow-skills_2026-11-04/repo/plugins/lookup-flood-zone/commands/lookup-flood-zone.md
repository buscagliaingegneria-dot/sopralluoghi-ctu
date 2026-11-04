---
title: Lookup Flood Zone
summary: Find a parcel's flood zone and base flood elevation, with its source
discipline: code-life-safety
tags: ["Reference"]
description: "Looks up a parcel's flood hazard designation from the mapping authority's own published source and reports it with the map panel, its effective date and the URL, never from recall. Then does the part that gets missed: separates the mapped designation from what the local floodplain ordinance actually requires, since freeboard, the datum, and how the lowest floor is measured are local and routinely stricter than the federal map. Carries no elevations, no zone definitions and no freeboard requirements. It is a lookup and a pointer, not a determination — an elevation certificate is prepared by a licensed surveyor and the floodplain administrator makes the call."
argument-hint: <address-or-parcel> [jurisdiction]
---

# Lookup Flood Zone

The flood zone is the easy half. What it means for the building is set by the
local floodplain ordinance, which adds freeboard, may use a different datum, and
defines the lowest floor in a way that decides whether the parking level counts.
A project designed to the map and not to the ordinance is designed short.

## Scope and limits — read first

**What this does.** Fetches the designation from the mapping authority's own
portal, records the panel and its effective date, then names what the local
ordinance has to be read for. It reports a lookup and a list of questions.

**What this does not do.**

- It carries **no zone definitions, no elevations and no freeboard.** Every
  figure comes from the fetched source or from the ordinance you supply.
- It is **not a determination.** The floodplain administrator determines; a
  surveyor prepares an elevation certificate. This is preliminary information
  for design.
- It does not read the local ordinance for you unless you supply it. It names
  what to look for in it.
- It does not do stormwater. On-site drainage, detention and the civil design
  are separate.
- It does not check whether a map amendment or revision is in progress, which is
  common on developed parcels and changes the answer.

**What you need before starting.** The address or parcel identifier. The
jurisdiction. The local floodplain ordinance, if you want more than the mapped
designation.

## Inputs the command needs

1. **Address or parcel identifier**, precise enough to land on one parcel.
2. **Jurisdiction**, named specifically.
3. **The local floodplain ordinance**, pasted or referenced, if the local
   requirements are wanted.
4. **Authorisation to fetch** from the mapping authority's portal.

## Workflow

### Step 1 — Fetch from the authority's own source

Tell the user which source is about to be fetched and fetch on confirmation. Use
the mapping authority's published portal for the jurisdiction. Do not use a real
estate site, an insurance aggregator, or any convenience map service as the
source; they cache, they generalise, and they are not the record.

Record and report: the designation, the panel or map identifier, its effective
date, and the URL, plus the timestamp of the fetch.

### Step 2 — Report exactly what was found, and where the parcel sits

- The designation, quoted as the source states it.
- Whether the parcel is wholly within one zone or crosses a boundary. A parcel
  crossing a line is the common case and it is not resolved by picking the
  larger part.
- Whether a base flood elevation is published for this location, and in what
  datum.
- Whether a floodway is mapped on or adjacent to the parcel.
- The effective date, and a statement that maps are revised and that amendments
  or revisions may be pending.

If the parcel cannot be located precisely, say so and stop. A neighbouring
parcel's designation is not this parcel's.

### Step 3 — Name what the local ordinance decides

State plainly that the mapped designation is the floor, not the requirement, and
list what has to be read from the local ordinance:

- Freeboard above the base flood elevation, which is local and often
  substantial.
- The datum the ordinance uses, and whether it matches the map's. A datum
  mismatch is a silent and expensive error.
- How the lowest floor is defined, and whether enclosed areas below it,
  crawlspaces, or parking count.
- What is permitted below the design flood elevation, and what has to be flood
  resistant.
- Utility and mechanical equipment elevation requirements.
- Substantial improvement and substantial damage thresholds, which govern
  existing buildings.
- Whether a development permit is required, and from whom.

Where the ordinance was supplied, quote each. Where it was not, list them as
open.

### Step 4 — Report and point on

- The lookup, with panel, date and URL.
- The local questions, answered or open.
- What has to happen next and by whom: the surveyor for an elevation
  certificate, the floodplain administrator for a determination, the civil
  engineer for site drainage, the insurer for what this does to premiums.

Close with the standing limits: preliminary, not a determination, maps are
revised.

## Rules

- **Never state a zone, an elevation or a freeboard from recall.**
- **Only the mapping authority's own portal** counts as a source.
- Report the panel identifier and effective date with every designation.
- Say when a parcel crosses a zone boundary; never resolve it by area.
- Name the local ordinance questions on every run, whether or not it was
  supplied.
- Never call it a determination.

## Anti-patterns

- Quoting a flood zone from a real estate listing or an insurance site.
- Reporting a designation with no panel and no date.
- Treating the mapped base flood elevation as the design elevation.
- Assuming the ordinance uses the same datum as the map.
- Picking one zone for a parcel that crosses a boundary.
- Skipping the substantial improvement threshold on an existing building.
- Advising on insurance.
