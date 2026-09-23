# 0021: Lead positioning: AI governance in practice

- **Status:** Accepted
- **Date:** 2026-09-23
- **Deciders:** thiago, claude
- **Relates to:** 0017 (named proof strip), 0018 (voice source of truth in the vault), 0019 (offer pages), T42

## Context and problem statement

The site led with "I run modernization, team redesign, and GenAI adoption as one program." The
canonical brand voice in the private vault changed on 2026-09-23 (vault Decisions Log #27): inbound
now asks mostly about AI governance and the impact of AI on the SDLC, and the newsletter already
writes there. The public `CLAUDE.md` mirrors the voice (ADR 0018), so its positioning, audience and
"never the futurist" lines were out of date, and the page copy with them.

The same mirror also still said "never name the two confidential former employers". The vault made
Booking nameable on 2026-07-24 (Decisions Log #22); only one name stays confidential. The gate's local
names file already lists only that one.

## Considered options

- **Lead with AI governance in practice, keep the Three-Body Program as the method underneath**
  (chosen)
- Keep "one program" as the lead and add governance as a fourth theme (dilutes the headline buyers
  now ask about)
- Lead with AI governance as compliance (crowded with the Big 4, GRC platforms and lawyers; the
  paper side belongs to a partner)

## Decision

1. The lead is **AI governance in practice: governance that runs in the delivery system, not policy
   on paper.** Engineering-side, never compliance or legal advice. Home hero, meta and share text
   derive from the vault's 30-second pitch.
2. The **Three-Body Program stays as the method**, framed as why governance fails when only one body
   (architecture, teams, AI capability) moves. The orbit mark stays.
3. The **Three-Body Delivery Lab** keeps its name and mechanics (ADR 0019); its outcome is reframed
   to "one real flow, governed and evidenced".
4. The public `CLAUDE.md` mirror follows the vault: widened audience, new positioning paragraph, and
   "never the futurist" refined (forward-looking framing is allowed when each forward claim pairs
   with a real implementation or a named source).
5. The confidentiality rule now says **one** confidential name, still never stored in this repo.
   This supersedes the positioning text and the "two employers" wording mirrored under ADR 0018; the
   mechanism of 0018 (vault canonical, local import, no names in the repo) is unchanged.

## Consequences

- **Good:** the front door matches what buyers ask about and what the newsletter already says; the
  mirror stops contradicting the vault on confidentiality.
- **Cost / risk:** "governance" can read as compliance consulting; the copy says engineering-side
  explicitly. The Lab has not run yet, so no outcome numbers go on the page (ADR 0008 still holds).
- **Follow-ups:** the OG cover image (`assets/brand/social/og-cover.png`) still carries the "one
  program, not three" line; regenerate it under ADR 0014 when the new card is designed.
