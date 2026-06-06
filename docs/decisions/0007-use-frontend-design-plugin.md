# 0007: Use the official frontend-design plugin

- **Status:** Accepted
- **Date:** 2026-06-06
- **Deciders:** thiago, claude
- **Relates to:** 0003, 0005

## Context and problem statement

We wanted the visual work to commit to a bold, intentional aesthetic and to avoid generic
AI-generated looks, rather than defaulting to a safe template. Anthropic ships an official
plugin for exactly this.

## Considered options

- **Install and use `frontend-design@claude-plugins-official`** (chosen)
- Design ad hoc without a guiding skill

## Decision

Install the official `frontend-design` plugin from the `claude-plugins-official` marketplace and
use it for the design pass. Commit the project opt-in (`.claude/settings.json`, which enables the
plugin for this repo) so every agent and session inherits the same design intent. Only
`.claude/settings.local.json` is gitignored.

## Consequences

- **Good:** consistent, distinctive design direction across agents and sessions; the opt-in is
  version-controlled, so a new clone is set up the same way.
- **Cost / risk:** the plugin must stay available in the marketplace; the opt-in pins the plugin
  by name, not by version.
