# 0011: Issue-based intake, triaged into the backlog

- **Status:** Accepted
- **Date:** 2026-06-07
- **Deciders:** thiago, claude
- **Relates to:** 0001, BACKLOG.md, CONTRIBUTING.md

## Context and problem statement

Bugs and feature ideas need a home. Without one they live in chat or memory and get lost ("limbo").
The repo already has a curated board (BACKLOG.md) and a decision record (ADRs); it needs a defined
front door that feeds them.

## Considered options

- **GitHub Issues with structured templates, triaged into BACKLOG `T##` tasks** (chosen)
- An in-repo "Inbox" section in BACKLOG.md (no Issues)
- No formal intake, rely on chat / memory

## Decision

Use GitHub Issues as the inbox, with Bug report and Feature request issue forms and a `triage`
label. Triage converts each issue into a `T##` task on the board, or declines it with a reason. A
`CONTRIBUTING.md` documents the flow, and a PR template enforces board + ADR + voice + confidentiality
checks. Significant decisions still become ADRs.

## Consequences

- **Good:** every report gets a number and a status; anyone can file one; input is structured; the
  path is clean (issue, then task, then maybe ADR); nothing sits in limbo.
- **Cost / risk:** triage has to actually happen, or issues pile up labeled `triage`. Issues live on
  GitHub, not in the repo, so they are not version-controlled (the resulting tasks and ADRs are).
- **Follow-ups:** the `bug` / `feature` / `triage` labels auto-create on first use; optionally run
  `gh auth login` to manage them by hand.
