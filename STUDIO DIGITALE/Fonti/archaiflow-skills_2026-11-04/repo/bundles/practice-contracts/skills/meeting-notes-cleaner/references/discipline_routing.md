# Discipline Routing for Meeting To-dos

Map the verb + topic in a meeting to the right owner role. Without this, a To-do gets assigned to "the team" — useless.

## Verb-based routing

| Verb                          | Default owner                              |
|-------------------------------|--------------------------------------------|
| review                        | Design consultant for that discipline      |
| confirm / approve             | Owner / Client                             |
| procure / purchase            | Contractor (procurement)                   |
| install / construct           | Contractor (field)                         |
| respond                       | Recipient of an RFI or query               |
| coordinate                    | Both parties — split into 2 To-dos         |
| submit                        | Whoever holds the deliverable              |
| draft drawing / draft detail  | Design consultant for that discipline      |

## Topic-based routing (discipline)

When a To-do is about a topic, assign to the discipline that owns the topic:

### Architecture
Partition layouts, doors/windows/hardware, finishes, RCP, casework, code/egress on plans, roof system, wet-wall waterproofing.

### Structural
Beam/column sizing, foundation/slab, rebar, steel connections, load-bearing changes, cantilever/deflection, structural penetrations.

### MEP — Mechanical
HVAC duct sizing/routing, equipment schedules, diffusers/returns, thermal zoning, refrigerant.

### MEP — Electrical
Panel schedules, circuits/loads, lighting + switching, receptacles, low-voltage/data, fire alarm, emergency power.

### MEP — Plumbing
Fixture schedules, hot/cold water routing, sanitary/vent, floor/roof drains, water heater.

### Civil
Site grading/drainage, utility tie-ins, paving/curbs, retaining walls.

### Landscape
Planting, irrigation, hardscape, site furniture, site lighting (often shared with Electrical).

### Interior
FF&E, decorative finishes, drapery, signage graphics, decorative lighting.

### External (permits / approvals)
Building permit, design review, traffic impact assessment, environmental review, parking review.

## Owner classification rules

When routing a To-do:

1. If the verb implies a single owner type (confirm → Owner), prefer that.
2. Else, if the topic implies a discipline, assign to that discipline.
3. If both verb and topic are ambiguous, the To-do is an **Issue**, not a To-do — move it to the Issues section with a question for clarification.
4. Never assign to a generic "the team" or "TBD" — that's a sign the To-do isn't actionable.

## Cross-discipline conventions

- Penetrations through structural elements: Primary = MEP requesting, CC Structural.
- Roof coordination: Primary = Architecture, CC Structural for connection.
- Wet wall: Primary = Architecture, CC Plumbing.
- Mechanical room layout: Primary = MEP, CC Architecture for clearances.
- Curtain wall: Primary = Architecture, CC Structural for embedded plates.
- Site lighting: Primary = Landscape if pole/fixture aesthetic; Primary = Electrical if circuiting/control.

## Common role labels (North America)

When transcripts include role names, normalize to:

- Owner / Client → Owner
- Architect / AOR (Architect of Record) → Design (Architecture)
- Structural Engineer / SEOR → Design (Structural)
- MEP Engineer / MEPOR → Design (MEP)
- General Contractor / GC → Contractor
- Site Superintendent → Contractor (field)
- Project Manager (GC) → Contractor (project mgmt)
- Subcontractor → Subcontractor (specify trade if known)
- Construction Administrator / CA → CA / Construction Administration
- Owner's Representative / Owner's Rep → Owner (delegated)
