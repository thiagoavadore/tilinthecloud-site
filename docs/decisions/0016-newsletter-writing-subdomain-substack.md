# 0016: Newsletter on `writing.tilinthecloud.com` via a Substack custom domain

- **Status:** Accepted
- **Date:** 2026-06-08
- **Deciders:** thiago, claude
- **Relates to:** T22, ADR 0010 (apex on GitHub Pages)

## Context and problem statement

The site's "Read the writing" links point at `https://writing.tilinthecloud.com` (hardcoded in
`index.html`). The writing lives on Substack ("The Recovering CTO"). We need that subdomain to serve
the Substack publication without disturbing the apex `tilinthecloud.com` (the GitHub Pages one-pager,
ADR 0010) or the independent email MX. The whole project exists to replace an apex -> personal-LinkedIn
redirect, so the apex must keep serving the front-page site.

## Considered options

- **Option A** (chosen): host the newsletter on Substack and bind it to the `writing.` subdomain via
  Substack's custom-domain feature (one-time $50), a single `writing` CNAME at the registrar.
- **Option B**: leave the newsletter on the default `tilinthecloud.substack.com` and point the site
  links there. Free, but leaks the Substack brand and weakens the owned-domain credibility loop.
- **Option C**: enable Substack's "root domain redirect" so the apex forwards to the newsletter.
  Rejected outright: it would hijack the front-page site, the exact failure this project undoes.

## Decision

Bind the Substack publication to `writing.tilinthecloud.com` with a single registrar CNAME
`writing` -> `target.substack-custom-domains.com`. The apex stays on GitHub Pages. Substack's
"root domain redirect" option is left OFF, permanently. Free tier (no paid subscriptions): the
newsletter is a pipeline / credibility channel, not a paid product.

## Consequences

- **Good:** owned-domain newsletter on the brand domain; the site <-> Substack credibility loop closes
  (site -> writing subdomain -> a homepage link back to tilinthecloud.com). Apex and email untouched.
- **Cost / risk:** $50 one-time fee; Substack's DNS-config bind can take up to 36h after the CNAME and
  cert are in place (the host 302s to substack.com until done). Custom domains slightly fragment
  Substack's native subscribe / discovery flow.
- **Follow-ups:** T22 closes when `https://writing.tilinthecloud.com` serves the publication (not the
  302). Never point the apex at Substack and never enable the root-domain redirect (also in CLAUDE.md).
