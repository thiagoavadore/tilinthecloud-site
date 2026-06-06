# 0002: Plain HTML + CSS, no framework

- **Status:** Accepted
- **Date:** 2026-06-06
- **Deciders:** thiago, claude
- **Relates to:** 0004, 0005

## Context and problem statement

v1 is a single static one-pager deployed to GitHub Pages at the apex domain, with a weekend
timebox and an explicit "do not gold-plate, ship-fastest wins" instruction (CLAUDE.md). There
is no content pipeline; the writing lives on Substack.

## Considered options

- **Plain HTML + CSS, no build step** (chosen)
- **Astro** (or another static site generator)
- A component framework (React/Vue) with a build

## Decision

Build with hand-written HTML and CSS, a few lines of vanilla JS only where a section needs it.
No framework, no build, no toolchain. Files deploy to Pages as-is.

## Consequences

- **Good:** fastest path to ship, nothing to install or build, trivial Pages deploy, no dependency rot.
- **Cost / risk:** no component reuse / partials; if the site grows to multiple pages with shared
  layout, hand-maintenance gets old.
- **Follow-ups:** revisit (reconsider Astro) only if v2 becomes multi-page or gains a content feed.
