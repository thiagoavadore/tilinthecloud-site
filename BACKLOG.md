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
- **Last updated:** 2026-06-07 by `claude` (v1 live: booking + form wired).

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

### In progress
| ID | Task | Owner | Since |
|----|------|-------|-------|
| -  | (none) | - | - |

### Todo / backlog

Grouped by priority (working-agreement rule 7). Triaged issues carry the matching `priority: *` label.

**Now**
- (nothing queued; the site is live and the rest is user-blocked or v2)

**Next**
- [ ] **T22** Confirm `writing.tilinthecloud.com` (Substack) resolves, then the "Read the writing" links go live. `(needs: user)`
- [ ] **T23** Add real proof-strip numbers (ADR 0008). `(needs: user)` publishable figures.

**Later**
- [ ] **T27** Open Graph / social share image (currently text-only OG tags). (v2)
- [ ] **T28** Custom `404.html` in the Three-Body style. (v2)
- [ ] **T29** Privacy-light analytics decision (none wired yet). (v2)

---

## Open questions (waiting on Thiago)

- Which outcome numbers are OK to publish, within the confidentiality rule (only GRESB, Nike,
  LINKIT, and "as a CTO" are nameable)? (T23)
- When does the Substack subdomain go live? (T22)

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
