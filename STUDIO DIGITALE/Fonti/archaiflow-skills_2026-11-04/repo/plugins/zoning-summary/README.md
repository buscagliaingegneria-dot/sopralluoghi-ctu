# Zoning Summary

Turn a parcel lookup into a zoning summary for early design.

This skill should be used when the user provides a site address, parcel info, or zoning lookup text and needs a structured zoning summary for early design. Trigger on 'zoning summary', 'zoning lookup', 'site zoning for [address]', or pasted zoning portal output. Targets North American projects (US + Canada). Generates a worksheet markdown in `docs/zoning/` and updates the project zoning index.

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **zoning-summary**.

In Claude Code:

```
/plugin install zoning-summary --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/zoning-summary
