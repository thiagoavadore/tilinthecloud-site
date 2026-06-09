# BACKLOG / WORKLOG: tilinthecloud.com

Central coordination file for this repo. If you are an agent or a human about to do
work here, **read this first and keep it current.** Hard rules (voice, confidentiality,
deploy) live in [CLAUDE.md](./CLAUDE.md) and always win over anything below. Durable
decisions live as ADRs in [docs/decisions/](./docs/decisions/); this file holds the live
task board and indexes them.

---

## Working agreement (multi-agent)

1. **Claim before you work.** Move the task into *In progress* with your handle and the date.
   One task, one owner at a time. If a task is already *In progress* and it is not yours,
   pick another or coordinate, do not double-staff it.
2. **Record significant decisions as ADRs.** Copy `docs/decisions/template.md` to the next free
   `NNNN-title.md`, fill it in, and add it to the index in `docs/decisions/README.md`. Do not
   edit a past ADR; supersede it with a new one. (See ADR [0001](./docs/decisions/0001-record-architecture-decisions.md).)
3. **Keep edits small and section-scoped** to reduce merge conflicts. One ADR per decision means
   you rarely touch a file someone else is editing.
4. **Use stable IDs.** Tasks are `T##` here; decisions are `ADR-####` in `docs/decisions/`.
   Never renumber or reuse either.
5. **Flag user-blocked items** with `(needs: user)` and the exact input required, so anyone can
   see what is waiting on Thiago vs. what an agent can just do.
6. **Triage the inbox.** New bugs and feature requests arrive as GitHub Issues labeled `triage`
   (see [CONTRIBUTING.md](./CONTRIBUTING.md)). Before starting net-new work, convert open `triage`
   issues into `T##` tasks here (or decline with a one-line reason). Don't let reports sit in limbo.
7. **Set a priority.** Every Todo task and triaged issue is **Now**, **Next**, or **Later** (issue
   labels `priority: now` / `next` / `later`). Now = pick up next; Next = soon; Later = someday or v2.
   Keep the Todo list grouped by these. `BACKLOG.md` is the prioritized plan; Issues are the inbox.

---

## Status snapshot

- **Where we are:** **LIVE** at https://tilinthecloud.com (and https://www.tilinthecloud.com,
  which 301s to the apex). GitHub Pages serving with a valid Let's Encrypt cert
  (CN=tilinthecloud.com) on all four edge IPs; Enforce HTTPS is on.
- **Remote:** `git@github-personal:thiagoavadore/tilinthecloud-site.git` (uses the `github-personal`
  SSH alias from `~/.ssh/config`; plain `git@github.com` will not auth with the loaded key).
- **Direction:** "Three-Body System" (Clash Display + Switzer, ink ground, copper accent,
  animated three-body mark). See ADR [0003](./docs/decisions/0003-three-body-visual-direction.md).
- **Last updated:** 2026-06-09 by `claude` (T23 deferred; T29 split into T38 website-GA4 + T39 Substack-GA4 with setup instructions). Prior: (T37: brand-voice single source of truth moved to the private vault, ADR 0018; T36 + PR #6: contact reframed call-first, duplicate email cut, book-a-call icon cache-proofed). Prior: (T35: copy pass + proof strip expanded to thirteen named
  engagements under "Where I've done the work", tagline softened. ADR 0017).

---

## Task board

### Done
- [x] **T01** Draft `CLAUDE.md` (positioning, voice rules, confidentiality, deploy target).
- [x] **T02** Propose 2-3 visual directions and get a pick. → Three-Body System (ADR 0003).
- [x] **T03** Install official `frontend-design` plugin and use it for the design pass (ADR 0007).
- [x] **T04** Build `index.html` (all five sections) + `assets/css/style.css` (full visual system).
- [x] **T05** Self-host fonts (Clash Display + Switzer woff2), no CDN (ADR 0004, 0005).
- [x] **T06** Three-body mark as `assets/favicon.svg` + header logo + hero motif.
- [x] **T07** Deploy scaffolding: `CNAME`, `.nojekyll`, `robots.txt`, `sitemap.xml`, `.gitignore`.
- [x] **T08** Verify: 0 em dashes, no forbidden names, all assets HTTP 200, responsive screenshots,
  reduced-motion + a11y basics.
- [x] **T09** Stand up coordination: `BACKLOG.md` + MADR ADRs in `docs/decisions/` (ADR 0001).
- [x] **T10** Set up issue-based intake: bug/feature issue forms, `CONTRIBUTING.md`, PR template,
  triage flow into the board (ADR 0011).
- [x] **T30** Refine the hero three-body mark: brighter orbit rings + three equal bodies (bone with
  copper rim) around the copper core. From #1, ADR 0012.
- [x] **T24** Commit v1 to `main` and push to `origin` (commit `664da1d`).
- [x] **T25** Configure GitHub Pages + DNS (GoDaddy): removed LinkedIn forwarding and the parked
  A record, added four apex A records to GitHub IPs, pointed `www` CNAME at `thiagoavadore.github.io`.
  MX/SPF/DKIM left untouched.
- [x] **T26** Enforce HTTPS enabled; cert active on all edges (verified HTTP 200 + valid cert).
- [x] **T20** Wire book-a-call button to the Google Calendar scheduling link (opens in new tab).
  Hero "Talk to me" intentionally scrolls to #contact (booking + email + form together); only the
  explicit "Book a call" line goes to Calendar. (ADR 0009.)
- [x] **T21** Contact form activated (FormSubmit confirmed; submissions now forward to info@). Kept
  FormSubmit, see ADR 0006.
- [x] **T28** Custom `404.html` in the Three-Body style (broken-orbit mark, one body drifted out;
  reuses the shared design system). Implementation, reuses ADR 0003, no new ADR.
- [x] **T31** Merge logo: three-body mark + Nexa Bold wordmark (`tilinthecloud`). Brand assets in
  `assets/brand/` (true orange); adopted in header + favicon recolored to site copper. ADR 0013.
- [x] **T27** Open Graph / social share image: `assets/brand/social/og-cover.png` (1200×630), wired as
  `og:image` + `twitter:image` in `index.html` + `404.html`. Part of the social-asset system, ADR 0014.
- [x] **T32** LinkedIn brand assets (one render pipeline with T27): company logo (replaces the dead
  pre-rebrand cloud logo) + company cover + Thiago's brand-framed personal avatar + personal header
  ("Three bodies. One program." + CTA). PNGs in `assets/brand/social/`, regenerable from `social/src/`.
  ADR 0014. `(needs: user)` to upload the four LinkedIn images to LinkedIn (manual, off-repo).
- [x] **T33** LinkedIn page *copy* (text companion to T32's visuals): drafts for the company page
  (tagline, overview, specialties, custom button, Dutch tagline + overview) and Thiago's personal
  profile (headline, About, top skills), synced to the brand/positioning and the voice +
  confidentiality rules. Now kept **local only** in gitignored `drafts-local/` (moved off the public
  repo, the personal draft holds pre-announcement detail). Open questions resolved and both pages
  published manually on 2026-06-09 (drafts updated to match). See ADR 0015.
- [x] **T34** Confidentiality hardening: the whole repo is served publicly by GitHub Pages, so the
  confidential names and internal drafts were purged from all git history (`git filter-repo` +
  force-push), a public-repo guardrail was added to `CLAUDE.md` + the PR template, and private content
  moved to gitignored homes (`drafts-local/`, `CLAUDE.local.md`). ADR 0015. `(needs: user)` other
  clones must re-sync (re-clone) after the history rewrite; optionally ping GitHub Support to expire
  cached refs.
- [x] **T22** `writing.tilinthecloud.com` (Substack "The Recovering CTO") is **live**: registrar CNAME +
  SSL + Substack's domain bind all verified 2026-06-09 (serves the publication, HTTP 200, no 302 to
  substack.com). The site's "Read the writing" links resolve end-to-end. Publication fully configured
  (theme, logo, bio, About, pinned welcome post, welcome email, homepage loop back to the site).
  Substack copy kept local in gitignored `drafts-local/substack-profile-copy.md`. See ADR 0016.
- [x] **T35** Copy pass on `index.html`: ran the humanizer + voice rules over the live copy (softened
  the unbacked "with a number on the outcome" tagline to "on the hook for the outcome", removed one
  "X, not Y" negation + a duplicate "deck", de-duped the contact "out of step" lines). Expanded the
  proof strip from four names to thirteen named past engagements (employment + consulting + advisory),
  recognizable-brand-first, under the honest umbrella "Where I've done the work"; dropped "as a CTO" as
  a row item. Updated `CLAUDE.md` (allowed-proof rule + landing-copy spec) to match. See ADR 0017.
- [x] **T36** Contact section hierarchy: the three get-in-touch surfaces (form, call link, email) were
  styled so only the form's Send read as a button, and email appeared twice (left-column line + the
  note under Send). Reframed as call-first: promoted "Book a 30-minute call" to the copper **primary**
  button (booking ends in a scheduled meeting; the calendar flow already collects the same name/email/
  context as the form, so it's a better-outcome path, not a faster form), demoted the form's Send to
  ghost, and removed the duplicate email line (email kept only as the quiet note under Send). Touches
  `index.html` + `assets/css/style.css` only. No ADR (styling/copy refinement, no positioning/DNS change).
  Follow-up (PR #6): the icon's size lived only in CSS, so browsers on a stale cached `style.css`
  rendered the SVG at its ~300x150 default and inflated the button into a copper blob. Fixed by sizing
  the icon via HTML attributes (`width`/`height` + `stroke="currentColor"`) so it survives a stale
  stylesheet. Rule of thumb for this no-build Pages site: give inline icon SVGs explicit dimensions in
  the markup, not CSS-only (HTML and CSS cache independently).
- [x] **T37** Brand-voice single source of truth: voice/tone/audience/confidentiality were split between
  this public `CLAUDE.md`, the gitignored `CLAUDE.local.md` (confidential names), and several scattered
  vault docs, with no canonical home and a vault memory pointing the wrong way. Made the private Obsidian
  vault canonical: created `TilinTheCloud/VOICE.md` (single source) + `TilinTheCloud/CLAUDE.md` that
  imports it; moved the two confidential names out of this repo into `VOICE.md`; the site's gitignored
  `CLAUDE.local.md` now `@import`s `VOICE.md` for local enforcement (names never stored here). This public
  `CLAUDE.md` keeps only a short mirror of the hard rules + a pointer. Flipped the vault memory to name
  `VOICE.md` as canonical. See **ADR 0018**. PR carries `CLAUDE.md` + ADR 0018 + this entry only (vault
  files + `CLAUDE.local.md` are outside the public repo). Optional follow-up: de-dupe the 3 remaining
  scattered vault voice docs so they defer to `VOICE.md`.

### In progress
| ID | Task | Owner | Since |
|----|------|-------|-------|
| -  | (none) | - | - |

### Todo / backlog

Grouped by priority (working-agreement rule 7). Triaged issues carry the matching `priority: *` label.

**Now**
- (nothing queued; the site is live and the rest is user-blocked or v2)

**Next**
- [ ] **T38** Google Analytics (GA4) on the **website** (`index.html` + `404.html`, static on GitHub
  Pages). Splits the site half out of the old T29. `(needs: user for the GA4 property)`
  - **Set up the property (user):** at analytics.google.com → Admin → Create property → add a **Web
    data stream** for `https://tilinthecloud.com` → copy the **Measurement ID** (`G-XXXXXXXXXX`).
  - **Implement (agent):** paste the gtag.js snippet immediately before `</head>` in **both**
    `index.html` and `404.html` (no build step, so it's a literal paste). The Measurement ID is a
    public client-side value, fine to commit (it is not a secret):
    ```html
    <!-- Google Analytics (GA4) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-XXXXXXXXXX');
    </script>
    ```
  - **Decide first (record as a short ADR):** GA pulls third-party JS from `googletagmanager.com`,
    which cuts against CLAUDE.md's "no external runtime deps / CDNs where avoidable" and the v1
    "privacy-light" stance, and the buyers + Thiago are EU, so GA's cookies / data-to-Google generally
    need a **consent banner (GDPR / ePrivacy)** and a privacy line before `gtag` loads (Consent Mode
    v2). Alternative: a cookieless privacy-light tool (Plausible / GoatCounter / Cloudflare Web
    Analytics) needs no banner. The ADR supersedes the "privacy-light pageview counter" note in
    CLAUDE.md "Out of scope for v1".
  - **Verify:** on the live site, GA4 **Realtime** shows your own visit; the network tab loads
    `gtag.js`.
- [ ] **T39** Google Analytics (GA4) on the **Substack** ("The Recovering CTO",
  `writing.tilinthecloud.com`). Splits the newsletter half out of the old T29. No code, Substack
  injects the tag natively. `(needs: user — Substack admin)`
  - **Set up (user):** Substack **Dashboard → Settings → Analytics** (the "Advertising analytics"
    area) → paste the GA4 **Measurement ID** (`G-XXXXXXXXXX`) into "Google Analytics Measurement ID"
    → Save. Substack handles GA4 natively and reports page views, sign-ups, and paid subscriptions
    (allow ~24h to populate).
  - **Property choice:** add a **separate Web data stream** for `writing.tilinthecloud.com` under the
    **same GA4 property** as the site (recommended: one property, two streams, so site + newsletter
    roll up but can be filtered apart).
  - **Note:** Substack's own analytics (opens, subscriber growth) stay the primary metric; GA adds web
    pageview data and a unified view with the site. Same EU/GDPR consideration as T38 applies to the
    public reading experience; Substack controls its own cookie/consent handling, verify what it
    surfaces.
  - **Verify:** GA4 Realtime shows a visit to a `writing.tilinthecloud.com` post.

**Later**
- [ ] **T23** Add real proof-strip numbers (ADR 0008). `(needs: user)` publishable figures.
  **(Deferred 2026-06-09 — not planned; revisit only if a concrete need comes up.)**

---

## Open questions (waiting on Thiago)

- Which outcome numbers are OK to publish, within the confidentiality rule (the nameable
  engagements are now the thirteen in the proof strip, ADR 0017; the two confidential former
  employers stay off-limits)? (T23)

---

## Decisions

Durable decisions are ADRs in [docs/decisions/](./docs/decisions/). Current index:

| ADR | Title | Status |
|-----|-------|--------|
| [0001](./docs/decisions/0001-record-architecture-decisions.md) | Record architecture decisions in MADR format | Accepted |
| [0002](./docs/decisions/0002-plain-html-css-no-framework.md) | Plain HTML + CSS, no framework | Accepted |
| [0003](./docs/decisions/0003-three-body-visual-direction.md) | "Three-Body System" visual direction | Accepted |
| [0004](./docs/decisions/0004-self-host-fonts.md) | Self-host fonts, no CDN | Accepted |
| [0005](./docs/decisions/0005-typography-clash-display-switzer.md) | Typography: Clash Display + Switzer | Accepted |
| [0006](./docs/decisions/0006-contact-form-formsubmit.md) | Contact form via FormSubmit, no backend | Accepted |
| [0007](./docs/decisions/0007-use-frontend-design-plugin.md) | Use the official frontend-design plugin | Accepted |
| [0008](./docs/decisions/0008-no-invented-outcome-metrics.md) | No invented outcome metrics on the proof strip | Accepted |
| [0009](./docs/decisions/0009-booking-via-google-calendar.md) | Booking via Google Calendar appointment scheduling | Accepted |
| [0010](./docs/decisions/0010-host-on-github-pages-apex.md) | Host on GitHub Pages at the apex domain | Accepted |
| [0011](./docs/decisions/0011-issue-based-intake-triage.md) | Issue-based intake, triaged into the backlog | Accepted |
| [0012](./docs/decisions/0012-three-body-mark-treatment.md) | Three-body mark visual treatment | Accepted |
| [0013](./docs/decisions/0013-merged-logo-nexa-wordmark.md) | Merged logo (three-body mark + Nexa wordmark) | Accepted |
| [0014](./docs/decisions/0014-social-share-asset-system.md) | Social / share asset system (OG card + LinkedIn assets) | Accepted |
| [0015](./docs/decisions/0015-keep-internal-material-out-of-public-repo.md) | Keep internal / sensitive material out of the public repo | Accepted |
| [0016](./docs/decisions/0016-newsletter-writing-subdomain-substack.md) | Newsletter on `writing.` subdomain via Substack custom domain | Accepted |
| [0017](./docs/decisions/0017-expand-proof-strip-to-named-engagements.md) | Expand the proof strip to named past engagements | Accepted |
