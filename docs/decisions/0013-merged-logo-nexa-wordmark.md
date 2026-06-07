# 0013: Merged logo (three-body mark + Nexa wordmark)

- **Status:** Accepted
- **Date:** 2026-06-07
- **Deciders:** thiago, claude
- **Relates to:** 0003, 0005, 0012

## Context and problem statement

The site shipped with the wordmark set in Clash Display next to the three-body mark. Thiago also
has an earlier logo (a cloud icon with the wordmark "tilin the cloud" in **Nexa Bold**, orange and
charcoal). He wants to merge the two: keep the three-body mark, but bring back the original Nexa
wordmark, closed up to one word **tilinthecloud**.

## Considered options

- **Merge: three-body mark + Nexa Bold wordmark, outlined to vector** (chosen)
- Keep the Clash Display wordmark (status quo)
- Revert to the old cloud logo

## Decision

Adopt a merged logo: the three-body mark joined to **tilinthecloud** in Nexa Bold. The wordmark is
**outlined to vector paths** (via the installed font, through PDF, to SVG), so the logo is
self-contained and needs no Nexa webfont (which also avoids web font-licensing).

- **Brand asset files** (`assets/brand/`) use the **true brand colors**: orange `#F7941D`,
  charcoal `#414042`. Primary, reversed, and mark-only, as SVG + PNG.
- **On the site**, the logo is **recolored to the site palette** (copper `#CC7A3B` + bone) so it
  fits the dark header. This keeps the muted, premium site identity from ADR 0003; the logo adapts
  to the site rather than the site adopting the brighter brand orange.
- Header (`index.html` + `404.html`) and the favicon now use the new mark; UI type stays Clash
  Display + Switzer (ADR 0005 unchanged), Nexa is logo-only.

## Consequences

- **Good:** brand continuity (the original wordmark returns), a reusable brand asset set, and a
  self-contained outlined logo with no font dependency or license issue on the web.
- **Cost / risk:** the on-site logo color (copper) differs from the brand files (orange). This is a
  deliberate, accepted mismatch. If we later unify, switch the site's `--copper` token to `#F7941D`.
- **Follow-ups:** none required.
