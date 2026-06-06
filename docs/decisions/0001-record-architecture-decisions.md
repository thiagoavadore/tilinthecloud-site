# 0001: Record architecture decisions in MADR format

- **Status:** Accepted
- **Date:** 2026-06-06
- **Deciders:** thiago, claude
- **Relates to:** BACKLOG.md

## Context and problem statement

This repo is worked on by multiple agents at the same time. We need a durable record of why
things are the way they are, so a fresh agent does not re-litigate settled choices, and so two
agents adding a decision in the same session do not collide on one file.

## Considered options

- **One file per decision (MADR) in `docs/decisions/`** (chosen)
- **A single inline decision log** in BACKLOG.md
- **No formal record**, rely on git history and code comments

## Decision

Use MADR-style ADRs: one numbered, append-only Markdown file per decision in
`docs/decisions/`. BACKLOG.md keeps the live task board and an index of ADRs. Changing a past
decision means writing a new ADR that supersedes the old one, never editing history.

## Consequences

- **Good:** near-zero merge conflicts (separate files), traceable rationale, low ceremony.
- **Cost / risk:** a small per-decision overhead; numbers must be allocated carefully and never reused.
- **Follow-ups:** index lives in `docs/decisions/README.md`.
