# NYC Zoning Lookup

Answer NYC zoning questions with citations.

This skill should be used when the user asks NYC-specific zoning questions and wants citation-backed answers from the NYC Zoning Resolution. Trigger on NYC zoning terms (FAR, lot coverage, setback, side/rear yard, sky exposure plane, height factor, dwelling unit factor, use group, accessory use), district codes (R1-R10, C1-C8, M1-M3), Special Districts (Special Hudson Yards District, Special West Chelsea District, etc.), or direct §X-XX citation requests. Downloads the official NYC ZR Complete PDF (~100 MB) on first use, caches a section-to-page outline at ~/.archtmpl/pdfs/nyc-zoning/, and answers each query by reading targeted pages and citing them as `§X-XX, p.N`. Operates with zero external dependencies — no Python, no embeddings, no API key beyond Claude Code subscription. Do NOT trigger for non-NYC zoning (use zoning-summary) or NYC Building Code questions (different document).

This is a skill. It runs in Chat, Cowork and Claude Code.

## Install

In the Claude app: Customize > Plugins > Add marketplace, paste `DavidCho1999/archaiflow-skills`, then install **nyc-zoning-lookup**.

In Claude Code:

```
/plugin install nyc-zoning-lookup --marketplace DavidCho1999/archaiflow-skills
```

Full page: https://archaiflow.com/templates/skills/nyc-zoning-lookup
