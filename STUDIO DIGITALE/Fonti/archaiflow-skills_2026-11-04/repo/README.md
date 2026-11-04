# Claude Code for Architecture

163 skills, 47 agents and 54 commands for architecture work in North America. Browse them at [archaiflow.com/templates](https://archaiflow.com/templates).

## Install

**Claude app (Chat, Cowork, or the Code tab).** Go to Customize > Plugins > Add marketplace and paste:

```
DavidCho1999/archaiflow-skills
```

Then pick a discipline bundle or a single tool and install it. It also shows up in Claude Code on your next session.

**Claude Code in a terminal.**

```
/plugin marketplace add DavidCho1999/archaiflow-skills
/plugin install code-life-safety@archaiflow
```

## What works where

| | Chat | Cowork | Claude Code |
|---|---|---|---|
| Skills | Yes | Yes | Yes |
| Commands | Used as skills | Yes | Yes |
| Agents | No | Yes | Yes |

Skills in Chat need code execution turned on in Settings > Capabilities.

## Layout

- `bundles/`: one plugin per discipline
- `plugins/`: one plugin per tool
- `skills/`: every skill in the open Agent Skills layout

This repo is generated from the library behind archaiflow.com. Changes made here are overwritten on the next export, so open an issue instead of a pull request.

## License

MIT. These tools help licensed professionals. They do not replace the architect of record or the authority having jurisdiction, and every result needs checking against the code your project is under.
