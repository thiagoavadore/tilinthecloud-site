# 0020: Count booking and email clicks by source with GoatCounter, not GA4

- **Status:** Accepted
- **Date:** 2026-09-15
- **Deciders:** thiago, claude
- **Relates to:** T38, T39, ADR 0002 (no build step), ADR 0009 (booking via Google Calendar)

## Context and problem statement

Eleven weeks of newsletter and LinkedIn content produced zero bookings through the site, and
nothing on the site could say which channel sent a visitor who clicked "Talk to me". The board
had a GA4 plan (T38). GA4 loads third-party JS from Google, sets cookies, and for an EU audience
needs a consent banner and a privacy line before it loads. That cuts against CLAUDE.md's "no
external runtime deps where avoidable" and the "privacy-light" stance, for a site whose only
measurement need is two numbers: clicks on the booking button and on the email link, split by
where the visitor came from. The lead itself completes off-site (Google Calendar, the inbox), so
the site can only ever see the click, never the booking.

## Considered options

- **Option A** (chosen): GoatCounter, cookieless, plus per-channel calendar links.
- **Option B**: GA4 with Consent Mode v2 and a consent banner.
- **Option C**: no script at all; per-channel calendar links only (bookings by source, no click counts).
- **Option D**: Plausible (paid) or Cloudflare Web Analytics (no custom events, so it cannot count a button).

## Decision

Load GoatCounter (one `<script>` tag, no cookies, no GDPR notice per its own docs, free hosted) on
all pages and count exactly three events, `click-book`, `click-email` and `submit-form`, each
suffixed with the source. The source is `utm_source` from the landing URL, kept in
`sessionStorage` for the visit, falling back to the referrer host (linkedin, substack, google,
referral), else `direct`. A shared `assets/js/clicks.js` also swaps every booking link to the
channel's own Google Calendar appointment schedule (three schedules, identical to the visitor,
different URLs), so the booked event carries the channel without asking the person anything.
The contact form gets a hidden `source` field for the same reason. Every inbound link we control
carries `utm` tags per the vault's Distribution & Growth note.

This is the one recorded exception to "no external runtime dependencies": about 9 KB of script
from `gc.zgo.at`. It supersedes the "privacy-light pageview counter (only if trivial)" note in
CLAUDE.md, which now reads as this decision.

## Consequences

- **Good:** no consent banner, no cookies, no personal data on the site. Clicks by source in one
  dashboard, bookings by source in the calendar, and the two agree by construction. The tagging
  convention lives in one place (the vault) and the channel-to-calendar map in one file.
- **Cost / risk:** one external script; if `gc.zgo.at` is blocked the page still works and the
  booking swap still runs (counting is a no-op). A visitor who types the URL lands on the `site`
  schedule, which is the honest default. GoatCounter's free hosted plan is donation-supported;
  self-hosting is the fallback.
- **Follow-ups:** T38 (this change), T39 parked. Review the GoatCounter dashboard at the
  bi-weekly slot; after eight weeks decide whether bookings by source justify anything more.
