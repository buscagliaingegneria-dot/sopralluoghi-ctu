# Code Review — Eight Egress & Accessibility Axes

Detailed framework for auditing a North American building plan against IBC egress, accessibility, and life-safety requirements. Each axis carries sub-criteria, code citations (IBC 2021 / 2024, ADA 2010, ICC A117.1-2017), common failure modes, and example findings phrased the way they should appear in the review file.

The axes are ordered the way the analysis usually proceeds: pin the use group and occupant load first; everything downstream depends on it.

---

## 1. Use group & occupant load

The foundation of egress analysis. Get this wrong and every downstream calculation is wrong.

**Sub-criteria:**

- Use group classification per IBC §302 (A-1 through A-5, B, E, F-1/F-2, H-1 through H-5, I-1 through I-4, M, R-1 through R-4, S-1/S-2, U).
- Mixed-occupancy strategy: accessory (§508.2 — accessory ≤10% of story area, governed as principal occupancy), non-separated (§508.3 — most restrictive applies, no rated separations between), separated (§508.4 — rated separations per Table 508.4).
- Occupant-load factors per IBC Table 1004.5 applied to actual square footage (gross or net per the table's footnote). Examples: business 150 gross, assembly unconcentrated 15 net, assembly fixed-seat = number of seats, mercantile 60 gross, educational 20 net (classroom), I-2 patient sleeping 240 gross.
- Egress design occupant load per IBC §1004.2 — the actual occupant load OR the AHJ-permitted higher load if posted (§1004.2).
- Increase per fixed seating (§1004.6), bleachers (§1004.7), outdoor areas (§1004.9).

**Common failure modes:**

- Conference rooms scored as "business" at 150 gross when the table footnote routes meeting rooms to assembly at 15 net. A 1,200 sf conference room flips from 8 to 80 occupants — entire egress design changes.
- Mixed-use strategy not declared. Applying separated-occupancies tables without rated separations.
- Outdoor assembly (terraces, plazas) ignored in load calculation.
- Storage/mechanical rooms over-counted (Table 1004.5 lists them at 300-500 gross — they rarely drive design).

**Example finding:**

> Floor plan labels Level 3 conference area "Business — 150 gross" but the spaces are open-plan meeting rooms (no fixed seats, table-and-chairs configuration). Per IBC 2021 Table 1004.5 footnote a, conference rooms / meeting rooms are scored as Assembly Unconcentrated at 15 net. Recalculating: 1,840 nsf at 15 net = 123 occupants (not 13 occupants at 150 gross). Required exit count and capacity must be revised — see Axis 2.

---

## 2. Egress capacity & number of exits

**Sub-criteria:**

- Capacity factors per IBC §1005.3.1 (stairways) / §1005.3.2 (other egress components). Default: **0.3 in/occupant stairways**, **0.2 in/occupant other egress components** (level, ramps ≤1:12, doors). Reduced — for buildings sprinklered with NFPA 13 (or NFPA 13 per §903.3.1.2) **and** an emergency voice/alarm communication system per §907.5.2.2, **excluding Group H and I-2** — to **0.2 in/occupant stairways**, **0.15 in/occupant other** [verify per IBC ed.]. Multiplied by the occupant load served.
- Number of exits per story per IBC §1006: ≤49 occupants 1 exit (subject to common-path & travel-distance limits in §1006.3 and Table 1006.3.3); 50-500 occupants 2 exits; 501-1000 occupants 3 exits; >1000 occupants 4 exits.
- Single-exit conditions per IBC §1006.3 (residential limited stories, R-2 limited dwelling-units-per-story, B/F-1/M/S-1 with travel distance ≤75 ft sprinklered).
- Distribution of exit access doorways — at least the required number serve the room or area, not just the building (§1006.2 spaces).
- Exit-access stair vs exit stair vs interior-exit-stair (§1019): rated, unrated, or open. Open exit-access stairways limited to 2 stories communicating per §1019.3.

**Common failure modes:**

- Exit count counted at the building level, missing room-level exit-access doorway requirements (§1006.2).
- Capacity counted in "doors" instead of "inches of clear width" — capacity is inches ÷ (in/occupant factor), not "the door is 36 in so it's fine."
- Reduced (sprinklered) factor used without confirming NFPA 13 + voice/alarm + non-H/non-I-2. The reduction from 0.3 stairways / 0.2 other to 0.2 stairways / 0.15 other requires *all three* conditions [verify per IBC ed.].
- Stair capacity sized for the "other components" factor (0.2 default / 0.15 reduced) instead of the stairway factor (0.3 default / 0.2 reduced).
- Open exit-access stair claimed but the stair connects more than 2 stories.

**Example finding:**

> Level 3 occupant load = 540 (per revised count Axis 1). Required: 3 exits per IBC 2021 §1006.2.1. Building is unsprinklered Group B, so capacity factor for other-than-stairways is 0.2 in/occupant per §1005.3.2 (default). Required egress door capacity = 540 × 0.2 = 108 in clear width across all exits at the level of exit discharge. Plan shows 2 exits at 36 in clear (72 in total) — short on both count and capacity. Add a third exit door and increase total clear width to ≥108 in. If sprinklers + voice/alarm are added later, factor reduces to 0.15 in/occupant for non-H/I-2 per §1005.3.2 exception (= 81 in required) [verify per IBC ed.]. If a third exit is geometrically blocked, request a code-modification or reduce occupant load via space planning.

---

## 3. Common path of egress travel

The distance from any point in a space to where two distinct directions of egress travel become available.

**Sub-criteria:**

- Common-path limits per IBC Table 1006.2.1 by occupancy and sprinklered status. Examples: B/F-1/M/S-1 sprinklered 100 ft (or 75 ft in some editions); B unsprinklered 75 ft; A unsprinklered 75 ft.
- Measured along the natural path of egress travel from the most remote point — not straight-line.
- For dwelling units (R), measured within the unit per §1006.2.1 with separate limits.
- Special common-path limits in I-2 (§1006.2.1 footnotes) and H occupancies (§1006.2.1 H-row).

**Common failure modes:**

- Measured straight-line through walls. Common path follows aisles, around furniture, along the corridor.
- Sprinklered limit used when only NFPA 13R is provided (R-2 specific).
- Common path within a space measured to the corridor entry rather than to the point of two-direction choice in the corridor.
- Workstation pods and breakout rooms ignored — they extend common path inside the space.

**Example finding:**

> Most remote workstation in open office, Level 3 east wing, common path measured 92 ft to the point where Corridor C and the elevator lobby cross-corridor offer two directions. IBC 2021 Table 1006.2.1 limits B sprinklered common path to 100 ft, so this is compliant by 8 ft. Note: any future furniture move that lengthens the path to the corridor will close the margin — flag for tenant fit-out review.

---

## 4. Travel distance

The total distance from the most remote occupiable point to the closest exit.

**Sub-criteria:**

- Travel-distance limits per IBC Table 1017.2 by occupancy and sprinklered status. Examples: B sprinklered 300 ft (some editions 250 ft); B unsprinklered 200 ft; A sprinklered 250 ft; I-2 sprinklered 200 ft; H occupancies short.
- Measured along the natural path of egress travel; through enclosed exit access stairways the measurement ends at the door to the exit (not at the discharge).
- Increased travel distance for atriums per §404 / §1029 (specific allowances).
- Open exit-access stair extends travel-distance accumulation into the stair (§1006.3) — counts as floor area for the distance, not as exit.

**Common failure modes:**

- Measured to the property line / discharge instead of to the exit (interior exit stair door, exterior exit door at level of exit discharge, or horizontal exit).
- Sprinklered limit applied without confirming the system meets the table's sprinkler standard.
- Two-story open-stair accumulation ignored — Level 3 travel distance claimed as Level 3 only, missing the Level 2 portion to the stair plus the stair run.

**Example finding:**

> Furthest point in Level 3 west wing measured 260 ft along the corridor to the door of Stair 2 (interior exit stair). IBC 2021 Table 1017.2 limits sprinklered B to 300 ft (assuming NFPA 13 throughout, confirmed). Compliant by 40 ft. Note that the travel path crosses the open exit-access stair to Level 2 — confirm the open stair is limited to the 2-story communication allowed in §1019.3 and not used as an exit stair.

---

## 5. Exit access width & door clear width

**Sub-criteria:**

- Door clear width per IBC §1010.1.1: 32 in minimum (measured between the face of the door and the stop with door open 90°), 48 in maximum single leaf with hardware. ADA / A117.1 align at 32 in.
- Stairs per IBC §1011: minimum width by occupant load (0.3 in/occ sprinklered); minimum 44 in if serving >50 occupants, 36 in serving ≤50; tread 11 in min, riser 4-7 in.
- Corridor width per IBC §1020.3: 44 in min (most B), 36 in (≤50 occ), 72 in (E with >100 occ), 96 in (I-2 patient corridors), 60 in (R-2 with > 50 occ at certain conditions).
- Door swing direction per §1010.1.2: into direction of egress when serving 50+ occ or H-occupancy.
- Dead-end corridors per §1020.4: 20 ft sprinklered B; longer in some sprinklered conditions; 50 ft in some B; 0 in H-1.
- Accessible door clear width: 32 in clear (matches IBC). Maneuvering clearances on push/pull side per A117.1 §404.

**Common failure modes:**

- 36 in nominal door labeled as compliant — at hardware/stop, clear is often 33-34 in, which still meets 32 in but may fail accessible maneuvering clearance.
- Corridor width measured wall-to-wall including projecting trim, casework, drinking fountains beyond the 4-in projection limit (§1003.3.3 / §1018).
- Doors swinging into the egress path occupying egress width when open.
- Dead-end corridor: alcoves with doors counted as "not a corridor" when they are.

**Example finding:**

> Corridor C between Stair 1 and the lobby: drinking fountain projects 6½ in into the corridor at 38 in AFF (within the 27-80 in zone where projections >4 in encroach on accessible route per A117.1 §307.2). Per IBC §1003.3.3, projections >4 in into the egress path reduce the corridor's usable width. Reduce projection to ≤4 in or recess the fountain.

---

## 6. Exit separation

**Sub-criteria:**

- Exit-access doorway separation per IBC §1007.1.1: ≥1/2 the diagonal of the area served (unsprinklered) or ≥1/3 the diagonal (sprinklered with NFPA 13). Measured as a straight line between exit-access doorway centerlines.
- Where 3 or more exits required, two are placed per §1007.1.1; the additional exits "reasonably distributed" (§1007.1.1).
- Interlocking and scissor stairs per §1007.1.2 — with conditions.
- Horizontal exits per §1026 — count as part of required exits with conditions.

**Common failure modes:**

- Verbal "exits are well distributed" without measuring the diagonal.
- Sprinklered 1/3 used when sprinkler system is NFPA 13R or partial.
- Diagonal measured of the building footprint instead of the actual area served by the exits.

**Example finding:**

> Level 3 floor plate diagonal measured 142 ft. Exit-access doorways at Stair 1 (NW corner) and Stair 2 (SE corner) measure 132 ft apart. Required separation (sprinklered 1/3): 47.3 ft. Compliant by 84.7 ft.

---

## 7. Accessibility

**Sub-criteria:**

- Accessible route from site arrival to all required spaces per ADA 2010 §206 and IBC §1104. Slope ≤1:20 or ramp per A117.1 §405. No steps in the required accessible route.
- Accessible means of egress per IBC §1009: one required accessible means of egress per accessible space, two when ≥2 means of egress are required for the space. Includes accessible route to area of refuge, horizontal exit, or exit discharge.
- Areas of refuge per IBC §1009.6 — required when accessible-means-of-egress count requires (most multi-story above level of exit discharge that is not sprinklered, or where elevators are not part of the accessible MOE per §1009.4).
- Type A and Type B dwelling unit thresholds per IBC §1107 — varies by R-occupancy, story count, and unit count. Type A is fully accessible; Type B is "adaptable."
- Accessible parking per ADA §208 and A117.1 — count by total parking, van-accessible 1 per 6 accessible.
- Drinking fountains, restrooms, signage, elevators (stretcher requirement in I/R-1 per §1009.4 and §3002.4).

**Common failure modes:**

- Accessible route includes a 5% slope claimed as "not a ramp." If slope >1:20 it is a ramp and needs handrails / landings per A117.1 §405.
- Area of refuge omitted on a non-sprinklered multi-story building because the elevator is "the accessible route" — elevator must qualify as accessible MOE per §1009.4 (limited cases).
- Stretcher-size elevator omitted in I-2 / R-1 — required per IBC §3002.4 (minimum 80 in × 54 in clear inside).
- Type B dwelling unit count short on R-2 buildings ≥4 units per §1107.6.4. Common error: counting Type A only.

**Example finding:**

> Level 3 has 8 wheelchair-accessible spaces in the open office. IBC 2021 §1009.1 requires accessible MOE serve all accessible spaces. Plan shows accessible route to Stair 1 (with area of refuge at landing) and Stair 2 (no refuge, no elevator-as-MOE compliance). One of the two paths must add an area of refuge or qualify the elevator as accessible MOE per §1009.4.5 (standby power, signage, monitoring). Recommend area of refuge at Stair 2 landing.

---

## 8. Fire-resistance assemblies & opening protectives

**Sub-criteria:**

- Occupancy separations per IBC Table 508.4 (fire-rated walls and floors between separated occupancies).
- Corridor walls per IBC Table 1020.2 — typical 1-hr in non-sprinklered B, 0-hr in sprinklered B with the §1020.1 exception, varies by occupancy.
- Shaft enclosures per §713 — typically 2-hr for shafts connecting 4+ stories, 1-hr for fewer.
- Opening protective ratings per Table 716.1(2) (fire doors) and 716.1(3) (fire windows). Ratings: 20-min, 45-min, 60-min, 90-min — match the assembly's required hour minus credits.
- Penetrations (firestop) per §714, joints per §715, ducts per §717 (smoke and fire dampers).

**Common failure modes:**

- Plan shows "1-hr corridor" notation but the assembly type called out is non-rated GWB.
- Door rating notation absent — assembly hour shown but door label not.
- Shaft penetrations unaddressed (e.g., fire damper at duct penetration omitted).
- "Sprinklered with §1020.1 exception" claimed on a building where §1020.1 exceptions don't apply (e.g., institutional occupancies excluded).

**Example finding:**

> Plan tag "Corridor C — 1-hr rated walls" with door schedule showing standard non-labeled doors. Per IBC 2021 Table 716.1(2), a 1-hr corridor wall requires a 20-min door label minimum. Update door schedule to 20-min labeled with self-closing hardware, smoke-and-draft control where required by §716.2.6.
