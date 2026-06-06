# 0005: Typography: Clash Display + Switzer

- **Status:** Accepted
- **Date:** 2026-06-06
- **Deciders:** thiago, claude
- **Relates to:** 0003, 0004

## Context and problem statement

The Three-Body direction (0003) needs a distinctive display face paired with a refined body
face. The frontend-design skill is explicit about avoiding generic, overused families (Inter,
Roboto, Arial, system fonts, and Space Grotesk).

## Considered options

- **Clash Display (display) + Switzer (body)** (chosen)
- A serif pairing (e.g. Fraunces + Newsreader), which belonged to the Editorial direction
- A monospace-led pairing, which belonged to the Operator's Console direction

## Decision

Clash Display for headings and the wordmark; Switzer for body, labels, and UI text. Both from
Fontshare.

## Consequences

- **Good:** characterful and architectural up top, clean and legible in body; credible to a
  technical reader without looking like a default template.
- **Cost / risk:** two families to load (mitigated by self-hosting only the needed weights, 0004).
  If load weight ever matters more, subset the woff2 to the glyphs actually used.
