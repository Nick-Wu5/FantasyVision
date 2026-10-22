# FantasyVision — team coding kickoff

**Working product definition:** A personalized football broadcast overlay driven by **synthetic match events**. A viewer chooses a demo fantasy manager (or optionally supplies a public manager ID); the system displays a pre-match watchlist, relevant fantasy point changes, mini-league rank swings, and a recap.

**Demo promise:** Watch a synchronized football clip or synthetic pitch animation while relevant, personalized graphics appear in an OBS browser source. The system **does not infer events from video**.

## Start here
1. Read `DECISIONS.md` and resolve the open questions with all four members.
2. Freeze `CONTRACTS.md` and `fixtures/` before parallel agent coding.
3. Each owner reads their workstream in `TEAM_WORKSTREAMS.md`.
4. Create feature branches and implement mocks first; see `COLLABORATION.md`.
5. Use `ACCEPTANCE_TESTS.md` to check integration and rehearse the demo.

## System
`synthetic timeline → replay clock → fantasy scoring/rankings → relevance & cooldown → Foundry narrative + validator/fallback → SSE → transparent OBS overlay`

Viewer setup supplies profile/picks/league snapshot; the clip runs in OBS alongside the browser overlay. **Code owns facts, scoring, ranking, timing and display eligibility. AI only writes bounded copy grounded in validated facts.**

## Proposed repo layout (agree before generating code)
```
apps/
  api/                 # replay, scoring, relevance, sessions, SSE
  overlay/             # transparent browser source and motion graphics
  viewer/              # mobile QR onboarding
packages/
  contracts/           # JSON schemas and shared types
  narrative/           # Foundry adapter, prompts, validator, fallbacks
fixtures/              # synthetic events, demo profiles, league snapshot
infra/                 # Azure deployment and CI
scripts/               # demo orchestration and checks
docs/                  # these kickoff documents
```

## Scope boundary
**In:** deterministic replay, FPL-style points, 3–4 demo personas, rank swings, four overlay templates, manual rehearsal controls, fallback text, Foundry integration, judge-accessible deployment.

**Out:** video event detection, player tracking, fantasy passwords/cookies, exact live bonus-point replication, OBS scene automation. Real FPL lookup is **optional** and must have permission/terms review and a cached fallback.

This document set translates the teammate's nine-page plan into executable collaboration instructions. It does not assert that any features are already implemented.
