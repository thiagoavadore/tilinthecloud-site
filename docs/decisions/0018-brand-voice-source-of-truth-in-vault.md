# 0018: Brand-voice source of truth lives in the private vault; public repo mirrors it

- **Status:** Accepted
- **Date:** 2026-06-09
- **Deciders:** thiago, claude
- **Relates to:** 0015 (keep internal material out of the public repo), 0017 (named proof strip)

## Context and problem statement

The TilinTheCloud brand voice (tone, audience, positioning, confidentiality) drives more than this
website: it also governs LinkedIn, the Substack ("The Recovering CTO"), talks, and bios. Thiago's
primary workspace for that content is his private Obsidian vault (`~/dev/MyObsidianLife/`, in the
`TilinTheCloud/` folder, where new content is authored under `Content/`).

Until now the voice rules were split and drifting: the public `CLAUDE.md` here held voice + audience
+ positioning + the confidentiality rule, the gitignored `CLAUDE.local.md` held the two confidential
employer names, and the vault restated the same rules scattered across several strategy/content docs
with no single home. Two surfaces, no canonical source, and a vault note that pointed at this repo as
canonical (the wrong direction for where content is actually made).

We want one canonical source so the voice cannot diverge between the site and the content channels,
while keeping confidential names off the public surface (per ADR 0015).

## Considered options

- **Canonical doc in the private vault; public repo keeps a short mirror + pointer; confidential
  names move to the vault and are imported locally** (chosen)
- Keep this public repo as the canonical voice source and have the vault consult it (status quo;
  keeps the buyer-facing voice in a public repo and leaves content work pointing the wrong way)
- Strip voice from the public `CLAUDE.md` entirely and rely only on a local import (zero duplication,
  but cloud-review and external/cloned agents then get no voice guidance in the repo)

## Decision

1. **The canonical brand voice lives in the vault** at `TilinTheCloud/VOICE.md` (git-untracked there;
   it syncs only via Obsidian Sync, so it is private). It is the single source of truth for voice,
   audience, positioning, register, and the confidential-names rule. A `TilinTheCloud/CLAUDE.md`
   imports it so all vault content work loads it.
2. **This public `CLAUDE.md` keeps a short, stable mirror** of the hard rules (which are already
   public on the live site) plus a pointer noting the vault doc governs. This keeps the repo and
   cloud-review agents self-contained.
3. **The two confidential names move out of this repo entirely** into `TilinTheCloud/VOICE.md`. The
   gitignored `CLAUDE.local.md` here `@import`s that vault file, so the names are in context for local
   enforcement but are never stored in this repo. The import is runtime-only; nothing is copied in.
   The public `CLAUDE.md` keeps only the rule (never name them), not the names. This supersedes
   ADR 0015's point 2 detail that the names live in `CLAUDE.local.md` itself.

## Consequences

- **Good:** one canonical voice doc shared by the site and every content channel; confidential names
  leave this public repo's working tree altogether (a step beyond ADR 0015); the public file still
  carries the spine for anyone without the vault.
- **Cost / risk:** the canonical source now lives outside this repo, so a clone without the vault has
  only the mirror (acceptable: the mirror is the stable subset). The `@import` of an external path
  triggers a one-time approval dialog in Claude Code on this machine. The public mirror and the vault
  doc must be kept consistent; since the mirror is the small, rarely-changing hard-rules subset, the
  drift surface is minimal.
- **Follow-ups:** optionally de-duplicate the voice rules still restated in the vault's other strategy
  /content docs so they defer to `VOICE.md` too.
