# Seismic Lookup

Record a site's seismic design parameters and where each came from.

Records the seismic design parameters a project needs before structural design starts, one at a time, with the source of each: mapped accelerations, site coefficients, design accelerations, the design category, and the long-period transition. Trigger on "seismic design category", "what is the SDC for this site", "seismic parameters", "site class", "design spectral accelerations", "seismic-lookup", or a pasted site location with a seismic question. Works in any jurisdiction. The parameters come from the user's own hazard tool, code maps, or geotechnical report, and the site class comes from the geotechnical engineer. The skill never supplies a seismic value from memory or from web search, and reports every parameter it could not source as a gap. Writes a CSV and a summary.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **seismic-lookup**.

In Claude Code:

```
/plugin install seismic-lookup --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/seismic-lookup
