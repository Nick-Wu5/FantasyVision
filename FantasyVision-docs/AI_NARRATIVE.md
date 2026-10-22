# Foundry narrative design

## Principle
**Deterministic code decides what happened, how many points changed, who moved in the league, and whether/when to show it.** Foundry writes *how to say it*, never invents facts.

## Input (proposed narrative request)
```json
{"viewerId":"demo_alex","eventId":"evt_041","template":"rank_swing","facts":{"playerName":"Alex Striker","pointsDelta":5,"rankBefore":4,"rankAfter":2,"isCaptain":false},"audience":"fantasy_fan"}
```
Only use facts produced by backend. If player names are synthetic, label them as such.

## Output
```json
{"headline":"Up to second!","explanation":"Five points from Alex Striker lift you from fourth to second."}
```

## Validation
- Strict JSON parse and schema; short max lengths (proposed 70-char headline, 150-char explanation).
- Verify referenced numbers and player names appear in supplied facts; reject unsupported claims.
- No real-time event facts outside input; no invented injuries, intent, or tactics.
- Timeout (proposed 2 seconds for live copy), fallback on errors, telemetry on failures.
- Pre-generate watchlist and recap where possible; cache repeatable output by event/viewer.

## Fallback examples
- `player_points`: `+{pointsDelta} fantasy points for {playerName}`.
- `rank_swing`: `You move from #{rankBefore} to #{rankAfter}`.
- `watchlist`: `Your players to watch today`.
- `recap`: `Your match recap is ready`.

## Evaluation
Test positive/negative points, captain, irrelevant rival event, rank tie, invalid JSON, slow response, missing name, and retry. Measure latency, fallback rate, validation rejection, and event-to-overlay delay.
