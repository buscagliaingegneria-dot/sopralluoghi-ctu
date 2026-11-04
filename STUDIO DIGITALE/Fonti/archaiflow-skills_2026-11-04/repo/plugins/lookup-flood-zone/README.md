# Lookup Flood Zone

Find a parcel's flood zone and base flood elevation, with its source.

Looks up a parcel's flood hazard designation from the mapping authority's own published source and reports it with the map panel, its effective date and the URL, never from recall. Then does the part that gets missed: separates the mapped designation from what the local floodplain ordinance actually requires, since freeboard, the datum, and how the lowest floor is measured are local and routinely stricter than the federal map. Carries no elevations, no zone definitions and no freeboard requirements. It is a lookup and a pointer, not a determination — an elevation certificate is prepared by a licensed surveyor and the floodplain administrator makes the call.

This is a command. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **lookup-flood-zone**.

In Claude Code:

```
/plugin install lookup-flood-zone --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/commands/lookup-flood-zone
