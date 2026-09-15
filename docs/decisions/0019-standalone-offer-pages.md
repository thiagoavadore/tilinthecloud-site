# 0019: Offer pages as standalone static pages under `/<offer>/`

- **Status:** Accepted
- **Date:** 2026-09-14
- **Deciders:** thiago, claude
- **Relates to:** 0002, 0009, 0014, 0017, T40

## Context and problem statement

v1 is a one-pager whose only next step is "Talk to me". The first productized offer, the
Three-Body Delivery Lab, needs a public home before its launch post, and the v2 sitemap already
plans a page per offer. The question is where an offer lives: a section on the one-pager, a
separate page, or a templated multi-page setup. CLAUDE.md constraints that bear on it: plain
HTML and CSS with no build step (ADR 0002), the site is a front door and not a content channel,
and no outcome claims without measured proof (ADR 0008).

## Considered options

- **A standalone page per offer at `/<offer>/index.html`, sharing `style.css`, chrome copied by
  hand** (chosen)
- A section on the one-pager only
- A partials or templating step to share header and footer

## Decision

Each offer is a folder with an `index.html`, served by GitHub Pages at `/<offer>/`. The page
reuses the one stylesheet; page-specific rules are additive and namespaced (`.lab-` for the
Delivery Lab). Header, footer and the inline motion script are copied from `index.html` and held
identical by `scripts/check_pages.py`, which also checks forbidden strings, per-page share
metadata and asset references on every page. The home page links to an offer from the nav and
from one short teaser band. Internal links are root-relative so the same markup works from a
nested folder. Each offer page carries its own OG card rendered by the existing
`assets/brand/social/src/render.sh` pipeline (ADR 0014).

## Consequences

- **Good:** a shareable URL per offer, no build step, no change to the one-pager's role, and a
  repeatable check that replaces the manual T08 checklist for every future page.
- **Cost / risk:** shared chrome now exists in three files. The gate catches drift but does not
  remove the duplication. Offer copy carries no price and no outcome claim until there is
  measured proof (ADR 0008).
- **Follow-ups:** revisit a partials step when the page count reaches the v2 sitemap (about six
  pages); the meta description on `index.html` is 194 characters and the gate warns above 160.
