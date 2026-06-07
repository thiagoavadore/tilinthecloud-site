# 0010: Host on GitHub Pages at the apex domain

- **Status:** Accepted
- **Date:** 2026-06-07
- **Deciders:** thiago, claude
- **Relates to:** 0002, 0006, 0009, CLAUDE.md

## Context and problem statement

v1 is a static one-pager that needs hosting with a custom apex domain (`tilinthecloud.com`),
automatic HTTPS, near-zero cost, and as little ongoing maintenance as possible. The brief named
GitHub Pages as the target; this ADR records keeping it as a deliberate choice and why, since the
no-backend decisions (0006, 0009) all follow from it.

## Considered options

- **GitHub Pages** (chosen): free static hosting straight from the repo, custom domain, automatic
  Let's Encrypt cert.
- **Netlify / Cloudflare Pages / Vercel**: also free static tiers, plus build pipelines, edge
  functions, and form/redirect features we do not currently need.
- **S3 + CloudFront** (or similar): full control, but real setup and an AWS bill to manage.

## Decision

Host on GitHub Pages, served at the apex `tilinthecloud.com` via four `A` records to the Pages
IPs plus a `www` CNAME to `thiagoavadore.github.io`, with a `CNAME` file in the repo and Enforce
HTTPS on. Email DNS (Google Workspace MX, SPF, DKIM) stays untouched.

## Consequences

- **Good:** free, no infrastructure to run, deploys on `git push`, native to where the code already
  lives, automatic cert. Working in production today.
- **Cost / risk:** static only, no server-side, which is exactly why form delivery and booking are
  outsourced (0006, 0009). The apex needs `A` records (GoDaddy has no CNAME flattening), and Pages
  carries soft bandwidth and size limits (a non-issue at this scale).
- **Follow-ups:** if v1 ever needs server-side logic, redirects at scale, or a build pipeline,
  revisit Cloudflare Pages or Netlify. Migration is just DNS plus moving the static files.
