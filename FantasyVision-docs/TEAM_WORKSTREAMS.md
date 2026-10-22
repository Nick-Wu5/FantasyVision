# Parallel workstreams and handoffs

The PDF assigns **four** members; replace member numbers with GitHub handles in kickoff. Each member must first produce a working mock matching `CONTRACTS.md`.

## A — Product, footage, demo (Member 1)
**Own:** 90–110 second script/storyboard, licensed clip or synthetic animation, timestamps in event timeline, 3–4 fictional managers/mini-league, OBS scene, recording/submission.
**Deliver:** `fixtures/match-events.json`, `fixtures/personas.json`, footage attribution record, demo runbook and video. **Unblocks:** backend and frontend.

## B — Overlay and viewer experience (Member 2)
**Own:** transparent 1920×1080 overlay, watchlist/player-points/rank-swing/recap templates, animation queue, QR/mobile setup, manual rehearsal panel.
**Develop against:** mock `OverlayGraphic` events. **Deliver:** browser-source URL and setup page; no graphic overlap; transparent background.

## C — Replay, fantasy scoring, relevance (Member 3)
**Own:** event replay clock, fantasy scoring and standings, impact calculation, priority/cooldown (~20s major graphics), SSE, session/replay controls, tests. Optional public FPL adapter with cached fallback.
**Develop against:** mock event/persona files. **Deliver:** deterministic API with reproducible reset behavior and documented endpoints.

## D — Foundry, narrative, cloud (Member 4)
**Own:** prompts, constrained narrative outputs, validator/fallback, Foundry provisioning, Container Apps, telemetry, secrets, CI/CD. Pre-generate pre-match and recap when possible.
**Develop against:** mock `FantasyImpact`. **Deliver:** function `renderNarrative(impact, facts) -> validated graphic` plus deployed environment and monitoring.

## Handoff rules
1. Contract change requires an explicit PR and approval from both producer and consumer.
2. Each PR includes sample input/output, test command, and screenshot for UI work.
3. Never block waiting for a teammate: use checked-in fixtures and adapter interfaces.
4. Integration order: `A fixtures → C replay/scoring → D narrative/fallback → B overlay`.
5. Each owner documents their section of README; A compiles submission, D owns architecture diagram, C reviews.
