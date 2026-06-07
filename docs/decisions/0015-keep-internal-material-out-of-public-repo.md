# 0015: Keep internal / sensitive material out of the public repo

- **Status:** Accepted
- **Date:** 2026-06-07
- **Deciders:** thiago, claude
- **Relates to:** 0010 (GitHub Pages at the apex)

## Context and problem statement

This repo is deployed by GitHub Pages, which serves the **entire tree** (not just `index.html`), and
the git **history is public**. Internal working drafts and confidential references were committed
here and were therefore publicly fetchable for a period. The confidentiality rule in `CLAUDE.md` was
itself spelling out the confidential parties' names, which placed them in the public repo.

We need a durable rule, and a recovery procedure, so internal or pre-announcement material never sits
on the public surface.

## Considered options

- **Hard rule + gitignored local homes + history purge when needed** (chosen)
- Keep drafts in the repo but rely on people remembering not to push sensitive bits (status quo; failed)
- Move the site to a private deploy path so the repo can hold internal files (large change to ADR 0010; rejected)

## Decision

1. **Treat the whole repo as public.** Anything committed (files in `assets/`, `docs/`, anywhere, and
   all history) is publicly fetchable. Never commit internal, sensitive, or pre-announcement material.
2. **Local-only homes for private content, both gitignored:**
   - `drafts-local/` for internal working drafts (e.g. off-site copy not ready to publish).
   - `CLAUDE.local.md` for the confidential names the public `CLAUDE.md` rule refers to (so agents can
     still enforce the rule locally without the names living in the public repo).
3. **The public `CLAUDE.md` states the rule without naming the confidential parties**, and carries a
   guardrail describing the public-repo reality. The PR-template checklist mirrors it.
4. **Recovery when sensitive content has already been committed:** purge it from all history with
   `git filter-repo` (remove files via `--invert-paths`, redact strings via `--replace-text`), then
   `git push --force-with-lease`. Keep a full bundle backup first.

## Consequences

- **Good:** the public surface (current tree and rewritten history) no longer carries the drafts or
  the names; a written guardrail plus gitignored homes stop recurrence across the multi-agent setup.
- **Cost / risk:** a history rewrite changes every commit SHA, so any other clone must re-sync (re-clone)
  after a purge. A force-push **cannot recall data already exposed**: GitHub may retain unreachable
  commits by SHA in caches/forks/PRs until it GCs, and anything already scraped or indexed is out of
  reach. So a purge prevents future casual discovery, it does not guarantee the data was never seen.
- **Follow-ups:** for a thorough purge of already-exposed content, contact GitHub Support to expire
  cached refs; treat previously-public sensitive items as potentially seen.
