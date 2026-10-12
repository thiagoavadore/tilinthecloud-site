# 0022: Newsletter renamed "Thiago de Faria"; persona retired

- **Status:** Accepted
- **Date:** 2026-10-12
- **Deciders:** thiago, claude
- **Relates to:** ADR 0016, ADR 0018, ADR 0021, ADR 0014, T43

## Context and problem statement

The vault (Decisions Log #36) renamed the newsletter from "The Recovering CTO" to "Thiago de Faria" and retired the "recovering CTO" persona. The vault governs brand voice (ADR 0018). This repo still names the old masthead in `CLAUDE.md`, the home-page writing card and the Substack cover. ADR 0016 binds the `writing.` subdomain to Substack; that DNS decision stays valid, only the name in its context paragraph is old.

## Considered options

- **Rename everywhere and retire the persona** (chosen)
- **Keep the persona on the site only**: contradicts the vault, which governs per ADR 0018.

## Decision

Masthead "Thiago de Faria", subtitle "Field notes on how teams ship with AI and keep it governed." The persona line in `CLAUDE.md` becomes "Thiago himself, a hands-on data and AI architect who still writes the code." The `writing.` subdomain and DNS are unchanged.

## Consequences

- **Good:** site, cover and vault say the same thing.
- **Cost / risk:** ADRs 0003, 0016 and 0018 keep the old name as historical context (append-only). The Substack settings must change before this ships.
- **Follow-ups:** writing card and Substack cover regenerated through the ADR 0014 pipeline (done in T43).
