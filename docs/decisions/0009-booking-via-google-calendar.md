# 0009: Booking via Google Calendar appointment scheduling

- **Status:** Accepted
- **Date:** 2026-06-07
- **Deciders:** thiago, claude
- **Relates to:** 0006, BACKLOG.md T20

## Context and problem statement

The site needs a book-a-call path for senior buyers. It is static with no backend, so the
scheduler must handle availability, timezones, confirmations, and a meeting link on its own.
Thiago already runs on Google Workspace (the domain's MX records are Google).

## Considered options

- **Google Calendar appointment scheduling** (chosen): native to the existing Workspace, free,
  public booking link.
- **Cal.com / Calendly / SavvyCal**: dedicated schedulers, more features, another tool and subscription.
- **mailto / "email me to book"**: cheapest to build, highest friction for the buyer.

## Decision

Use Google Calendar appointment scheduling. The public link is wired into the "Book a 30-minute
call" button and opens in a new tab. Configured as a free 30-minute intro (no payment), weekday
business hours Amsterdam with buffers and a daily cap, roughly one business day minimum notice so
Thiago can prep, and a short qualifying question (company + role, where architecture / teams / AI
are out of step). The hero "Talk to me" button scrolls to the contact section (booking, email, and
form together); only the explicit booking line opens Calendar.

## Consequences

- **Good:** no new tool or subscription, native to the existing Workspace, auto Google Meet link
  and reminders, qualifying questions give prep context before each call.
- **Cost / risk:** the booking URL is an opaque Google link (not on-brand), and the scheduling
  settings live in Google, not the repo, so they are not version-controlled.
- **Follow-ups:** revisit a dedicated scheduler if booking grows (paid sessions, routing, branding).
