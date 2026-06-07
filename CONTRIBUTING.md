# Contributing to tilinthecloud.com

Short version: nothing lives in limbo. Every bug or idea becomes a tracked item, and every real
decision becomes an ADR.

Read [CLAUDE.md](./CLAUDE.md) (hard rules), [BACKLOG.md](./BACKLOG.md) (the live board), and
[docs/decisions/](./docs/decisions/) (decisions) first.

## Source of truth

`BACKLOG.md` is the **single prioritized plan**: what we work on and in what order. GitHub Issues
are the **inbox**: where work is reported and discussed. They are not two competing lists.

Triage moves an issue onto the board as a `T##` task and **cross-links the two**: the task
references the issue (`#12`), the issue references the task (`T31`). The issue stays open as the
durable record and discussion; the `T##` is the planned, prioritized unit of work. When the work
ships, close the issue and check off the task.

Priority lives on both. Every task and issue is **Now**, **Next**, or **Later** (issue labels
`priority: now` / `priority: next` / `priority: later`):

- **Now** = pick up next.
- **Next** = soon, after the Now items.
- **Later** = someday, or v2.

"What's next?" means: read the **Now** group in `BACKLOG.md` (after triaging any new issues into it).

## Report a bug or request a feature

Open a [GitHub Issue](https://github.com/thiagoavadore/tilinthecloud-site/issues/new/choose) and
pick a template:

- **Bug report** for something broken or wrong.
- **Feature request** for a change or addition.

Anything that is not a bug or a feature: email info@tilinthecloud.com.

## What happens next (triage)

Every new issue arrives labeled `triage`. Triage (an agent or Thiago):

1. Turns it into a `T##` task on the BACKLOG board, or declines it with a one-line reason and closes it.
2. Sets a priority (`priority: now` / `next` / `later`) and removes the `triage` label once it is on
   the board (keeps `bug` / `feature`).
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
