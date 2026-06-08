# CLAUDE.md: tilinthecloud.com

Source for **tilinthecloud.com**, the website for **TilinTheCloud BV** (Thiago de Faria's independent consulting practice, Netherlands).

> **Coordination:** This repo is worked on by multiple agents. Before doing anything, read [BACKLOG.md](./BACKLOG.md) (the central task board) and follow its working agreement: claim tasks before starting, and record significant decisions as ADRs in [docs/decisions/](./docs/decisions/) (MADR format, one file per decision, append-only). New bugs and feature requests arrive as GitHub Issues labeled `triage`; triage them into the board per [CONTRIBUTING.md](./CONTRIBUTING.md). This CLAUDE.md holds the hard rules; BACKLOG.md holds the live state; the ADRs hold the durable decisions.

## What this is

v1 is a **single static one-pager**. It has exactly three jobs:

1. **Legitimacy**: read as credible to a cold buyer who just googled the name.
2. **State the offer**: what Thiago does, in his voice.
3. **Give a way to book**: a call link and `info@tilinthecloud.com`.

It is a **front door and conversion surface, NOT a content channel**. The writing lives on Substack ("The Recovering CTO"). Do not turn this into a blog.

It **replaces a redirect** that currently sends tilinthecloud.com → Thiago's personal LinkedIn (a credibility leak for cold buyers).

**Timebox: a weekend. Do not gold-plate.** Ship-fastest wins.

## Build & stack

- **Plain HTML + CSS**, no framework, no build step. Fastest path to ship a one-pager and deploy straight to GitHub Pages. (Astro was on the table; rejected as overkill for a single page with no content pipeline.)
- No JS unless a section genuinely needs it (e.g. wiring the contact form). Keep it minimal.
- One page, self-contained assets. No external runtime dependencies / CDNs where avoidable.

## Audience

**Senior technical decision-makers: CTO, VP of Engineering, Head of Architecture.** They are the buyers. Tone must read as credible to *them*, not as a futurist.

## Positioning (the thesis)

Thiago runs **modernization, team redesign, and GenAI adoption as ONE program**. Sequencing them the old way is how enterprises fall behind. The method is **"The Three-Body Program"**: three bodies (architecture, teams, AI capability) moving together. Persona: **a recovering CTO who still writes the code.**

## Voice constraints (HARD RULES)

- Voice: **direct, warm-professional.**
- **NO em dashes anywhere.** Use commas, parentheses, colons, or "but"/"and".
- **No corporate jargon**: never "leverage", "synergy", "align on", "double-click".
- **Never the futurist**: every claim anchors to something hands-on with **a number on the outcome**.
- No arrows-and-boxes consultant fluff.

## Confidentiality (DO NOT VIOLATE)

- **This entire repo is public.** GitHub Pages serves the whole tree (not just `index.html`), and the
  git history is public too. Anything committed here, drafts in `assets/`, notes in `docs/`, anywhere,
  is publicly fetchable. **Never commit internal, sensitive, or pre-announcement material.** Keep
  drafts and private notes local and gitignored (`drafts-local/`, `CLAUDE.local.md`).
- **Never name the two confidential former employers** on the site, in copy, comments, commit
  messages, or alt text. Their names are deliberately kept out of this public repo; they live in the
  gitignored `CLAUDE.local.md` for local enforcement.
- Quotable proof that IS allowed: **GRESB, Nike, LINKIT, and "as a CTO".** Use only these for the proof strip.

## v1 sections

1. **Hero**: the thesis + one-line positioning + two buttons (Talk to me / Read the writing).
2. **What I do**: the three-bodies framing, who it is for, the "hands-on, with a number" promise.
3. **Proof strip**: anonymized outcomes (GRESB, Nike, the CTO seat).
4. **Writing**: link out to Substack ("The Recovering CTO", at `writing.tilinthecloud.com` once live).
5. **Contact**: a book-a-call link + `info@tilinthecloud.com` (wire the contact form to that address).

## Landing copy (Thiago's voice: refine wording, keep the meaning)

> I run modernization, team redesign, and GenAI adoption as one program.
> In the AI era, sequencing them is how you fall behind.
>
> [Talk to me] · [Read the writing]
>
> Most enterprises modernize the architecture, reorganize the teams, and adopt GenAI as three separate programs. The gaps between them are where the program stalls. I close those gaps: one operator, three bodies (architecture, teams, AI capability), moving together. Hands-on, and with a number on the outcome.
>
> Twenty years from statistician to CTO to hands-on architect. I have run these from the inside at GRESB, Nike, and as a CTO.
>
> If your architecture is six months ahead of your teams, and your GenAI strategy is a deck instead of a system, that is the gap I close. Let's talk: info@tilinthecloud.com

## Deploy target

- **GitHub Pages**, served at the **apex domain `tilinthecloud.com`**.
- Keep a **`CNAME`** file in the repo root containing `tilinthecloud.com`.
- **DNS** (configured at the registrar, not in this repo):
  - Four `A` records for the apex → GitHub Pages IPs: `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`.
  - One `www` `CNAME` → the GitHub Pages host.
  - One `writing` `CNAME` → Substack (`target.substack-custom-domains.com`) for the newsletter ("The Recovering CTO"). See ADR 0016.
- **The apex stays on GitHub Pages. NEVER point `tilinthecloud.com` at Substack, and never enable Substack's "root domain redirect" (it would hijack the front-page site, the exact failure this project undoes).**
- **Email MX is independent. DO NOT TOUCH email DNS.**

## Out of scope for v1

Blog/content pages, CMS, analytics beyond a privacy-light pageview counter (only if trivial), newsletter capture, multi-page nav, dark/light toggles, animations beyond subtle. If it is not one of the five sections above, it waits for v2.
