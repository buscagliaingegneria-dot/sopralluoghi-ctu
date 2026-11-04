# LEED Tracker

Score a project scorecard and predict its certification level.

This skill should be used when the user wants to build, update, or score a LEED v4.1 BD+C New Construction scorecard for an architectural project — by walking the credit list, declaring pursuit status (Yes / Maybe / No / N/A) for each credit, and summing points to predict certification level (Certified / Silver / Gold / Platinum). Trigger on "LEED scorecard", "LEED v4.1 score", "score this project for LEED", "LEED tracker", or pasted project program with sustainability goals. Reads bundled credit-by-credit point matrix from USGBC LEED v4.1 BD+C and outputs a CSV scorecard plus a markdown summary in `docs/leed/`. Does NOT make LEED eligibility judgments — the user declares what they intend to pursue; this skill organizes and scores.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **leed-tracker**.

In Claude Code:

```
/plugin install leed-tracker --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/leed-tracker
