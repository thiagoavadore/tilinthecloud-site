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

- **One accent color everywhere: copper `#CC7A3B`** (with charcoal `#414042` for "thecloud" on
  light backgrounds, bone on dark). The brand asset files (`assets/brand/`), the on-site header
  logo, the favicon, and the rest of the site all use copper, so the identity is unified across the
  website, the logo files, and social.
- The original Fiverr wordmark was bright orange `#F7941D`; that is **superseded here by the site's
  copper**. The orange originals remain in Thiago's source files if ever needed.
- Header (`index.html` + `404.html`) and the favicon use the new mark; UI type stays Clash Display +
  Switzer (ADR 0005 unchanged), Nexa is logo-only.

## Consequences

- **Good:** brand continuity (the original wordmark returns), one accent color across every
  touchpoint (no website-vs-logo mismatch), and a self-contained outlined logo with no font
  dependency or license issue on the web.
- **Cost / risk:** the logo drops the original bright orange. Accepted: copper reads more premium
  for the CTO audience (ADR 0003), and one unified color beats matching the legacy tone.
- **Follow-ups:** none required.
