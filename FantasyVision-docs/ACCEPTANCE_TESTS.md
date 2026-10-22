# MVP acceptance and integration tests

## Data/replay
- [ ] Fixture events validate and sort by `videoTimeMs`.
- [ ] Start/pause/reset reproducible; reset clears scores, ranks, cooldown, and UI queue.
- [ ] Duplicate event IDs do not double-score; reconnect does not duplicate graphics.
- [ ] Playback time corresponds to configured clip timeline.

## Fantasy calculations
- [ ] Goal points vary by position according to the **documented simplified rule table**.
- [ ] Assist scored exactly once, including goal metadata + separate assist-event edge case.
- [ ] Captain multiplier applied correctly; negative card points handled.
- [ ] Clean-sheet loss and saves handled only for eligible positions/events.
- [ ] Rank before/after reflects same league snapshot; ties deterministic.

## Relevance and AI
- [ ] Viewer-owned event high priority; irrelevant event suppressed or downgraded.
- [ ] ~20-second major-graphic cooldown enforced; important events queue or replace by policy.
- [ ] Foundry valid response renders; timeout, malformed JSON, unsupported numbers fall back.
- [ ] No unsupported AI facts; numeric fields remain from scoring engine.

## UI and operations
- [ ] Four templates render with mock inputs and do not overlap.
- [ ] Transparent 1080p OBS browser source works.
- [ ] QR/demo-persona selection works without credentials.
- [ ] Switching active persona updates the correct personalized output.
- [ ] Manual trigger is available for rehearsal; it does not corrupt scoring state.
- [ ] Judge-accessible hosted link loads; cold-start and SSE reconnect tested.

## Demo go/no-go
**Must pass before polish:** one fixture event → scoring/rank update → relevance → validated/fallback copy → SSE → visible OBS overlay, twice consecutively after reset.
