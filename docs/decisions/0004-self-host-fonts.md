# 0004: Self-host fonts, no CDN

- **Status:** Accepted
- **Date:** 2026-06-06
- **Deciders:** thiago, claude
- **Relates to:** 0002, 0005

## Context and problem statement

The design uses Clash Display and Switzer (see 0005). CLAUDE.md says no external runtime
dependencies or CDNs where avoidable. Fonts are the main temptation to call out to a CDN.

## Considered options

- **Self-host the woff2 files** in `assets/fonts/` (chosen)
- Link the Fontshare or Google Fonts CSS / CDN at runtime

## Decision

Download the exact weights used (Clash Display 500/600/700, Switzer 400/500/600) as woff2 and
serve them from `assets/fonts/`, declared with `@font-face` and `font-display: swap`. The two
above-the-fold weights are preloaded.

## Consequences

- **Good:** no third-party request, no CDN dependency, faster and more private, works offline,
  immune to a CDN changing or disappearing. Total font weight is ~100KB.
- **Cost / risk:** updating a font means re-downloading the file by hand; the woff2 binaries live
  in the repo.
- **License:** Clash Display and Switzer are Fontshare fonts, free for commercial and web use.
