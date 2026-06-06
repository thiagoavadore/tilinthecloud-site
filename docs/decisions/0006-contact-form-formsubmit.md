# 0006: Contact form via FormSubmit, no backend

- **Status:** Accepted
- **Date:** 2026-06-06
- **Deciders:** thiago, claude
- **Relates to:** BACKLOG.md T21

## Context and problem statement

The contact section must wire a form to info@tilinthecloud.com, but the site is static on
GitHub Pages with no server and no build. We need form delivery without standing up a backend.

## Considered options

- **FormSubmit** (chosen): form POSTs to FormSubmit, which emails the submission to the address.
- **Formspree**: similar hosted form backend.
- **Own serverless endpoint** (e.g. a function): full control, more setup.
- **mailto-only**: a link, no form; depends on the visitor having a mail client.

## Decision

Wire the `<form>` action to FormSubmit, delivering to info@tilinthecloud.com, with a visible
`mailto:` link alongside as a fallback. The provider is swappable by changing only the form
action.

## Consequences

- **Good:** zero backend, works on Pages today, spam honeypot included, trivial to swap.
- **Cost / risk:** leads route through a third party; FormSubmit needs a one-time confirmation
  click on the first real submission before it delivers.
- **Follow-ups:** activation is BACKLOG T21. Revisit if leads must never touch a third party
  (would move to an own serverless endpoint).
