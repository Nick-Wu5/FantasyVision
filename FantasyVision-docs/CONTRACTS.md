# Shared contracts v0.1 — freeze with team

All identifiers are opaque strings. JSON examples are **valid JSON** (no comments). Time fields have explicit units. Never let an LLM create numeric scoring facts.

## MatchEvent — replay engine output
```json
{"id":"evt_041","matchClock":"63:12","videoTimeMs":41200,"type":"goal","playerId":"p9","teamId":"home","metadata":{"assistBy":"p7","shotSpeedKph":92}}
```
Required: `id`, `matchClock`, `videoTimeMs` (integer >=0), `type`, `playerId`, `teamId`, `metadata` (object). `type`: `goal | assist | save | card | clean_sheet_lost | sub`. `metadata` is event-specific; a goal may reference `assistBy`, but **do not count the assist twice** if both a goal and an assist event exist. Decide the canonical convention before implementation. Events must have unique IDs and monotonic `videoTimeMs`.

## FantasyImpact — scoring/ranking output
```json
{"eventId":"evt_041","viewerId":"demo_alex","pointsDelta":5,"viewerOwnsPlayer":true,"isCaptain":false,"rivalsAffected":["demo_sam"],"leagueRankBefore":4,"leagueRankAfter":2,"priority":"high"}
```
Required: all keys above. `priority`: `high | medium | low | suppress`. **Contract clarification:** `priority` is best produced by the relevance module, not the pure scoring module; until agreed, treat this as a post-relevance `FantasyImpact` view. `pointsDelta` can be negative. Rankings must be computed from the same scoring snapshot, with a documented tie-break rule.

## OverlayGraphic — post-validation UI message
```json
{"graphicId":"g_017","template":"player_points","headline":"Your striker delivers","explanation":"Five points move you into second place.","playerId":"p9","pointsDelta":5,"displayMs":6000,"source":"ai"}
```
`template`: `watchlist | player_points | rank_swing | recap`; `source`: `ai | fallback`. `headline` and `explanation` must be short and consistent with scoring facts. For `watchlist` and `recap`, `playerId`/`pointsDelta` may be absent; UI must handle this. **Proposed:** add `eventId`, `viewerId`, `sequence` for deduplication and correct routing, after team agreement.

## Proposed SSE envelope (new integration convention, not specified in PDF)
```json
{"sequence":17,"kind":"overlay","viewerId":"demo_alex","emittedAt":"2026-10-22T18:00:00Z","payload":{"graphicId":"g_017","template":"player_points","headline":"Your striker delivers","explanation":"Five points move you into second place.","playerId":"p9","pointsDelta":5,"displayMs":6000,"source":"fallback"}}
```
`kind`: `event | impact | overlay | state`. Decide whether the frontend subscribes to only `overlay` or also `state`. For SSE, server sends `id: <sequence>`, `event: <kind>`, `data: <json>`. Clients dedupe by sequence and reconnect safely.

## Proposed HTTP endpoints (NOT yet implemented)
- `GET /health` — readiness.
- `GET /api/demo/personas` — list demo viewer profiles.
- `POST /api/session` — choose demo persona; returns session identifier.
- `GET /api/state?viewerId=...` — snapshot for late join.
- `GET /api/stream?viewerId=...` — SSE for selected viewer.
- `POST /api/replay/start`, `/pause`, `/reset` — protected demo controls.

## Contract freeze checklist
- [ ] One canonical event for assists; avoid duplicate points.
- [ ] All event types have validated metadata schemas.
- [ ] Define fantasy points for each position and event; define rank ties.
- [ ] Clarify `viewerId` scoping and active-persona model.
- [ ] Confirm UI fields for watchlist/rank_swing/recap beyond generic graphic fields.
- [ ] Generate JSON Schema/TypeScript types from the final contracts; do not maintain conflicting copies.
