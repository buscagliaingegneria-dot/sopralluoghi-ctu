# Structure & MEP

Every Structure & MEP tool in one plugin: 18 skills, 7 agents and 5 commands for North American architecture practice.

## Skills

- **Calculation Reader**: Read an engineer's calculation for its inputs, not its arithmetic
- **Consultant Drawing Review**: Read any consultant's drawing against the architectural set
- **Design Acoustic Separation**: Build a separation for sound, where the flanking path decides the result
- **Design Beam**: Size a simply-supported beam in steel, wood, or concrete
- **Design Ceiling**: Set the ceiling height by what has to fit above it
- **Design Column**: Check an axially loaded column with the values your standard gives
- **Design Duct**: Size a duct run from the airflow and the limits you set
- **Design Electrical Room**: Lay out an electrical room around the clearances that cannot be built on
- **Design Elevator**: Hold space for the shaft, the pit, the overrun, and the machine
- **Design Footing**: Check a spread footing against the bearing value your report gives
- **Design Mechanical Room**: Size a plant room for the equipment, the air, and getting it back out again
- **Design Panel Load**: Total a panel's connected load and apply your demand factors
- **Design Ventilation**: Compute zone outdoor-air rates from the table you supply
- **Equipment Reader**: Read a cut sheet for what the building has to give the equipment
- **MEP Review**: Read an MEP set for space, routing, and coordination conflicts
- **Penetration Review**: Find every hole through an assembly and say what closes it, and to what
- **Schedule Reader**: Read an engineer's schedule for what it means to the architecture
- **Structural Drawing Review**: Read a structural set against the architectural, from the architect's side

## Agents

- **Senior Acoustic Engineer**: An acoustician's gut-check on an assembly or noise study
- **Senior Commissioning Consultant**: A commissioning agent on whether the building will do what the drawings claim
- **Senior Elevator Consultant**: A vertical transportation consultant on whether the cars and the shafts work
- **Senior Fire Protection Engineer**: A fire-protection engineer's gut-check on sprinkler and alarm design
- **Senior Lighting Consultant**: A lighting designer on what the space will look like, not what it measures
- **Senior MEP Engineer**: A senior MEP engineer's gut-check on drawings and schedules
- **Senior Structural Engineer**: A senior structural engineer's gut-check on load path and lateral

## Commands

- **Compare Structural System**: Put structural systems side by side on what each does to the architecture
- **Explain Load Path**: Trace how load travels from roof to foundation
- **Explain Panel Schedule**: Read an electrical panel schedule and say what it means for the architecture
- **Explain Riser Diagram**: Read an MEP riser diagram and find where it disagrees with the plans
- **Size Shaft**: Add up what has to fit in a shaft, plus the room to install and reach it

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **structure-mep**.

In Claude Code:

```
/plugin install structure-mep --marketplace DavidCho1999/archaiflow-skills
```

Browse and read each one at https://archaiflow.com/templates/structure-mep.
