# Issue tracker: GitHub

Issues and PRDs for this repo live as GitHub issues. Use the `gh` CLI for all operations.

## Conventions

- **Create an issue**: `gh issue create --title "..." --body "..."`.
- **Read an issue**: `gh issue view <number> --comments`, including its labels.
- **List issues**: `gh issue list --state open --json number,title,body,labels,comments` with appropriate label and state filters.
- **Comment on an issue**: `gh issue comment <number> --body "..."`.
- **Apply or remove labels**: `gh issue edit <number> --add-label "..."` or `--remove-label "..."`.
- **Close an issue**: `gh issue close <number> --comment "..."`.

Infer the repository from `git remote -v`; `gh` does this automatically inside the clone.

## Pull requests as a triage surface

**PRs as a request surface: no.** Set this to `yes` if external PRs should enter the same triage queue as issues.

GitHub shares a number space across issues and pull requests. When `#42` is ambiguous, try `gh pr view 42` and fall back to `gh issue view 42`.

## Skill operations

- When a skill says "publish to the issue tracker", create a GitHub issue.
- When a skill says "fetch the relevant ticket", run `gh issue view <number> --comments`.

## Wayfinding

For `/wayfinder`, use one issue labelled `wayfinder:map` as the map and link child issues as GitHub sub-issues. Label child tickets `wayfinder:<type>` (`research`, `prototype`, `grilling`, or `task`). Represent blocking with GitHub's native issue dependencies when available, and fall back to a `Blocked by: #<n>` line. Claim work by assigning the issue to the current user; resolve it by commenting with the result and closing it.
