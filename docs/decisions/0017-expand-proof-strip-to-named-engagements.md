# 0017: Expand the proof strip to named past engagements under "Where I've done the work"

- **Status:** Accepted
- **Date:** 2026-06-09
- **Deciders:** thiago, claude
- **Relates to:** ADR 0008 (no invented outcome metrics), ADR 0015 (keep internal material out of the public repo)

## Context and problem statement

The proof strip shipped with four nameable credibility tokens (GRESB, Nike, LINKIT, "as a CTO")
and the line "I have run these from the inside" (ADR 0008). Two problems with that line as the
client base grew:

1. **It undersold the track record.** Thiago has worked with a much longer list of recognizable
   organizations across twenty years.
2. **"From the inside" is not true for all of them.** The engagements are a mix: some were direct
   employment, others were consulting or advisory work done while at TilinTheCloud, LINKIT, or AWS.
   A blanket "from the inside" / internal-employee framing would misrepresent the advisory ones.

We want a stronger, honest credibility strip for a cold senior-technical buyer, without claiming
employee status we did not have and without touching the confidentiality rule.

## Considered options

- **Named text strip under an honest umbrella label** (chosen): list the organizations as plain
  text wordmarks in a static wrapped row, headed "Where I've done the work" so the framing is true
  whether the relationship was employment, consulting, or advisory.
- **Real brand logos in a carousel**: rejected for v1. No third-party logo assets exist in the repo;
  sourcing 12 official logos raises trademark-usage questions (especially for advisory clients) and
  cuts against the project's ship-fast, no-external-dependency ethos.
- **Keep the four-name strip**: rejected. It undersells a genuinely strong list.
- **Two-bucket split (employed vs advised)**: rejected as heavier than needed and unnecessarily
  granular for a one-pager; the umbrella label resolves the honesty problem without it.

## Decision

The proof strip lists, recognizable-brand-first:

> AWS / Nike / ASML / KLM / Rabobank / KBC / FC Utrecht / GRESB / LINKIT / Ticketscript / Icemobile / CHDR / INEP

headed by the eyebrow label **"Where I've done the work"**. It is a static, wrapped, text-only row
(no logos, no motion). "as a CTO" is dropped as a row item; the CTO seat is already carried by the
lead sentence ("from statistician to CTO to hands-on architect").

This **extends ADR 0008**: that ADR's core rule (no fabricated outcome numbers, and never name the
two confidential former employers) stays fully in force. The expanded list contains none of the
confidential names. Because the page still shows no published metric, in the same change the
"Hands-on, and with a number on the outcome" tagline was softened to **"Hands-on, and on the hook
for the outcome"** (hero meta tags + the What-I-do foot), which keeps the accountability/anti-futurist
edge without promising a number the page does not display. CLAUDE.md's allowed-proof rule and the
landing-copy spec block were updated to match.

## Amendment (2026-06-09)

Three refinements after seeing the strip on the live page:

1. **Added two Dutch banks**, ABN AMRO and de Volksbank, placed next to Rabobank and KBC so the row
   reads as a deliberate finance/banking cluster. Both supplied by Thiago; neither is a confidential
   former employer, so the rule above is untouched.
2. **Added a muted, italic "and more" at the end of the row** so the list reads as representative
   rather than exhaustive (removes the "is that all?" read and the pressure to be complete).
3. **Moved the proof strip below "What I do"** (it now sits between the Three-Body Program section and
   Writing). Rationale: a cold buyer should meet the claim and the method first, then the evidence for
   it. Logos landing after the explanation hit harder because the reader knows what they are proof of.
   The hero's eyebrow and thesis already carry the first legitimacy beat. Easily reversible if the
   immediate-logo-wall placement tests better.

## Consequences

- **Good:** a markedly stronger, recognizable credibility strip; the umbrella label is honest across
  all three relationship types; no trademark/asset/permission burden (text only); zero new
  dependencies and effectively zero layout cost (the existing `.proof-row` already wraps).
- **Cost / risk:** named clients are now public. They were supplied by Thiago and are plain text
  (lower risk than logos), but if any advisory client objects to being named publicly, pull that name.
  ADR 0008's follow-up still stands: real, approved outcome numbers would strengthen this further.
- **Follow-ups:** if/when publishable figures land, work a number back in (and the tagline can harden
  again). Keep the confidential former employers off this list permanently.
