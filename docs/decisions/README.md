# Architecture Decision Records

This directory holds the durable decisions for tilinthecloud.com, one file per decision,
in [MADR](https://adr.github.io/madr/) style. The task board and live status live in
[../../BACKLOG.md](../../BACKLOG.md); the hard rules live in [../../CLAUDE.md](../../CLAUDE.md).

## Why one-file-per-decision

Multiple agents work this repo at once. A single shared decision log is a merge-conflict
magnet. Separate, numbered, append-only files mean two agents can each add a decision in the
same session without touching the same file.

## How to add an ADR

1. Copy [`template.md`](./template.md) to `NNNN-short-kebab-title.md`, where `NNNN` is the
   next free zero-padded number. **Never reuse or renumber** an existing number.
2. Fill it in. Keep it short: context, the options you weighed, the decision, the consequences.
3. Set **Status** to `Accepted` (or `Proposed` if you want review first).
4. Add a row to the index below and reference the ADR from any related task in `BACKLOG.md`.
5. To change a past decision, do **not** edit it. Write a new ADR and set the old one's status
   to `Superseded by NNNN`, and the new one's `Supersedes NNNN`.

## Status values

`Proposed` · `Accepted` · `Rejected` · `Deprecated` · `Superseded by NNNN`

## Index

| ADR | Title | Status |
|-----|-------|--------|
| [0001](./0001-record-architecture-decisions.md) | Record architecture decisions in MADR format | Accepted |
| [0002](./0002-plain-html-css-no-framework.md) | Plain HTML + CSS, no framework | Accepted |
| [0003](./0003-three-body-visual-direction.md) | "Three-Body System" visual direction | Accepted |
| [0004](./0004-self-host-fonts.md) | Self-host fonts, no CDN | Accepted |
| [0005](./0005-typography-clash-display-switzer.md) | Typography: Clash Display + Switzer | Accepted |
| [0006](./0006-contact-form-formsubmit.md) | Contact form via FormSubmit, no backend | Accepted |
| [0007](./0007-use-frontend-design-plugin.md) | Use the official frontend-design plugin | Accepted |
| [0008](./0008-no-invented-outcome-metrics.md) | No invented outcome metrics on the proof strip | Accepted |
| [0009](./0009-booking-via-google-calendar.md) | Booking via Google Calendar appointment scheduling | Accepted |
| [0010](./0010-host-on-github-pages-apex.md) | Host on GitHub Pages at the apex domain | Accepted |
| [0011](./0011-issue-based-intake-triage.md) | Issue-based intake, triaged into the backlog | Accepted |
| [0012](./0012-three-body-mark-treatment.md) | Three-body mark visual treatment | Accepted |
| [0013](./0013-merged-logo-nexa-wordmark.md) | Merged logo (three-body mark + Nexa wordmark) | Accepted |
