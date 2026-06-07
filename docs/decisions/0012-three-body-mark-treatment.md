# 0012: Three-body mark visual treatment

- **Status:** Accepted
- **Date:** 2026-06-07
- **Deciders:** thiago, claude
- **Relates to:** 0003 (refines the mark; the Three-Body direction itself is unchanged)

## Context and problem statement

Issue #1 flagged the hero mark: the orbit rings were too faint on the ink ground (thin dark gray
on near-black), and the three orbiting bodies were an arbitrary mix (two bone, one light copper),
with an open question of whether to name the four objects.

## Considered options

- **Brighten the rings and unify the three bodies** (chosen)
- Leave the mark as-is
- Label the four objects directly in the hero

## Decision

- **Rings:** raise the stroke to `#4E596B` at width `1.6` so the motion reads on the ink ground.
- **Bodies:** make the three orbiting bodies identical (bone fill, copper rim, equal radius) so they
  read as equal partners "moving together"; the center stays the glowing copper core (the operator,
  the one program). This replaces the arbitrary two-vs-one split.
- **No labels in the hero.** Rotating labels read poorly, and explicit labels tip toward the
  arrows-and-boxes consultant look the brief rules out. The mapping to architecture / teams / AI
  capability stays in the "What I do" section.

## Consequences

- **Good:** the orbital motion is visible, the mark is balanced and on-thesis (one core, three
  equals), and the copper rim ties the bodies to the brand accent.
- **Cost / risk:** slightly more visual weight on the right of the hero (acceptable).
- **Follow-ups:** subtle labels remain a possible future enhancement if Thiago wants them (raised in
  issue #1); deferred, not part of this change.
