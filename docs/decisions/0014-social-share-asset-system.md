# 0014: Social / share asset system (OG card + LinkedIn assets)

- **Status:** Accepted
- **Date:** 2026-06-07
- **Deciders:** thiago, claude
- **Relates to:** 0003, 0012, 0013

## Context and problem statement

Two gaps in off-site presence:

1. **The site had no `og:image`.** Shared on LinkedIn/Slack/iMessage, tilinthecloud.com rendered a
   blank or scraper-guessed preview card, a small credibility leak for a site whose job is to read
   credible to a cold buyer. (This was backlog T27.)
2. **LinkedIn still carried the pre-rebrand logo.** The company page showed the old Fiverr cloud mark
   (orange `#F7941D`, superseded by ADR 0013), and the personal profile had no tilinthecloud
   signal or call to action at all.

We need a small set of raster brand surfaces that read as one system with the site.

## Considered options

- **One render pipeline, five raster cards on the site's dark treatment** (chosen)
- Hand-design each asset in a graphics tool (off-repo, not regenerable, drifts from the site)
- OG card only; leave LinkedIn for later (the cheaper half of T27, but leaves the dead logo live)

## Decision

Build five PNGs from HTML sources rendered with headless Chrome, all on the dark brand treatment
(ink `#0F1318` ground, the dual radial glow, three-body mark with `#4E596B` rings + bone bodies +
copper core, Clash Display + Switzer):

| Asset | Size | Notes |
|-------|------|-------|
| `og-cover.png` | 1200×630 | Wired as `og:image` + `twitter:image` in `index.html` and `404.html`. |
| `linkedin-company-logo.png` | 400×400 | Mark on ink, sized inside the circle crop. Replaces the old cloud logo. |
| `linkedin-company-cover.png` | 1128×191 | Left ~210px clear for LinkedIn's logo overlay. |
| `linkedin-personal-avatar.png` | 800×800 | Thiago's real headshot, brand-framed (copper ring + mark badge), composited (not generated). |
| `linkedin-personal-header.png` | 1584×396 | "Three bodies. One program." + triad + a "Let's talk → tilinthecloud.com" CTA. Bottom-left clear for the avatar. |

- **Raster, not SVG:** LinkedIn and OG scrapers only accept PNG/JPG.
- **Headless Chrome, not `rsvg-convert`:** the cards use the self-hosted woff2 fonts (Clash Display,
  Switzer) for brand-faithful type; `rsvg-convert` can't load woff2. Sources render at 2x and
  downsample to canonical size for clean anti-aliasing.
- **Regenerable in-repo:** sources live in `assets/brand/social/src/` with relative paths and a
  `render.sh`, matching how the rest of `assets/brand/` documents regeneration.
- **Copy stays in voice / within confidentiality:** no em dashes, no forbidden names; only the
  approved positioning lines.

## Consequences

- **Good:** shared links and both LinkedIn surfaces now read as one system with the site; the dead
  pre-rebrand logo is retired; the personal header finally states the offer and gives a destination;
  every asset is regenerable from the repo.
- **Cost / risk:** the avatar is a composite of Thiago's real photo (brand framing only), not novel
  imagery, the tilinthecloud signal is the copper ring + mark badge. The raw `src/headshot.jpg` is a
  public professional headshot committed for regen; remove it if that exposure is unwanted (the
  rendered avatar already carries the same likeness).
- **Follow-ups:** the LinkedIn assets must be uploaded by Thiago (manual, off-repo). The site OG tags
  ship with the site.
