# GitHub + Kiro agent collaboration rules

Kiro and other AI IDEs see the **local checkout**, not teammates' unpushed edits. Fetch/pull or merge a PR before asking the agent to review teammate changes.

## Branch strategy
- `main` is demo-stable; protect it where practical.
- `feature/overlay-*`, `feature/replay-*`, `feature/narrative-*`, `feature/demo-*`.
- Small PRs; one teammate reviews integration-impacting changes. Avoid concurrent edits to contracts.
- Before merging: unit tests, sample fixture replay, and contract validation must pass.

## Before every agent coding session
1. `git status` and `git fetch origin`.
2. Rebase/merge your feature branch onto updated `main` **when safe**; never discard uncommitted work.
3. Ask the agent to inspect `README.md`, `DECISIONS.md`, `CONTRACTS.md`, and your workstream.
4. Ask for a brief file-change plan **before** implementing.
5. Constrain edits to your owned component; do not rewrite another member's module to make integration easier.
6. Run tests, inspect `git diff`, and commit intentionally.

## Shared agent instruction (copy into Kiro steering / repository instructions)
> Build FantasyVision according to `docs/README.md`, `docs/DECISIONS.md`, and `docs/CONTRACTS.md`. The source is deterministic synthetic events, not video inference. Never invent scoring facts or use an LLM to calculate points, ranks, priority, or timing. Do not introduce CV, FPL credentials/cookies, or extra Azure services. Preserve public interfaces. If a contract is missing or ambiguous, stop and request a team decision instead of silently inventing one. Use fixtures, typed validation, tests, and fallback paths. Make the smallest change that fulfills the requested workstream.

## Example Kiro kickoff prompt
> Read all files in `docs/` and inspect the repo. I own Workstream [B/C/D]. First summarize the contracts I consume and produce, identify gaps, and propose a file-level implementation plan. Do not write code until I approve the plan. Do not modify files outside my workstream without asking.

## Sync prompt after teammate merges
> Compare my branch with updated `main`, identify API/schema changes, run contract tests, and propose adapter changes. Do not modify teammates' implementation without permission.

## Safety
No secrets in git or AI prompts. `.env` ignored; `.env.example` documents names only. Keep replay and demo mode working if Foundry or FPL APIs are down. Require review for agent-generated sweeping refactors.
