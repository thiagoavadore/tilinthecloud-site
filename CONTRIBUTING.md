# Contributing to tilinthecloud.com

Short version: nothing lives in limbo. Every bug or idea becomes a tracked item, and every real
decision becomes an ADR.

Read [CLAUDE.md](./CLAUDE.md) (hard rules), [BACKLOG.md](./BACKLOG.md) (the live board), and
[docs/decisions/](./docs/decisions/) (decisions) first.

## Report a bug or request a feature

Open a [GitHub Issue](https://github.com/thiagoavadore/tilinthecloud-site/issues/new/choose) and
pick a template:

- **Bug report** for something broken or wrong.
- **Feature request** for a change or addition.

Anything that is not a bug or a feature: email info@tilinthecloud.com.

## What happens next (triage)

Every new issue arrives labeled `triage`. Triage (an agent or Thiago):

1. Turns it into a `T##` task on the BACKLOG board, or declines it with a one-line reason and closes it.
2. Removes the `triage` label once it is on the board (keeps `bug` / `feature`).
3. Cross-links the issue and the task so they track together.

Nothing stays untriaged. An open issue still labeled `triage` simply has not been picked up yet.

## When a change carries a decision

If the work involves a real tradeoff (a new tool, a direction change, dropping a constraint), record
an ADR:

1. Copy `docs/decisions/template.md` to the next free `NNNN-title.md`.
2. Fill it in, set Status to `Accepted`, and add it to the index in `docs/decisions/README.md` and
   the table in `BACKLOG.md`.
3. Reference the ADR from the task and the PR.

Never edit a past ADR. Supersede it with a new one.

## Open a pull request

- Keep it scoped to one task where you can.
- Fill in the PR checklist (it mirrors the rules above).
- Update `BACKLOG.md` in the same PR so the board never lags the code.

## For agents

- Treat open issues labeled `triage` as the inbox. Triage them before starting net-new work.
- Claim a task by moving it to *In progress* with your handle. One task, one owner.
- Follow the working agreement in `BACKLOG.md`.
