# Demo script and operations (draft)

## Storyboard for a 90–110 second video
- **0–15s:** Problem and product: generic broadcast doesn't know your fantasy squad. Show QR and select demo persona.
- **15–30s:** Pre-match watchlist graphic identifies the selected viewer's players.
- **30–55s:** Synthetic goal/assist synced with footage; points graphic enters, holds, exits. Show that the player is on this viewer's squad.
- **55–75s:** Mini-league standings shift; rank-swing graphic with validated Foundry explanation.
- **75–95s:** Demonstrate relevance suppression/cooldown or switch persona to show personalization; finish with recap.
- **95–110s:** Brief architecture/stack, clear disclosure: events and in-match points are synthetic.

## Operator checklist
- [ ] Record footage license/source and any attribution; no unlicensed logos/music/audio.
- [ ] Select persona, reset replay, reset graphics queue, set OBS to 1920×1080.
- [ ] Load browser-source overlay with transparent background.
- [ ] Align clip start and replay start; verify event `videoTimeMs` synchronization.
- [ ] Rehearse goal, rank swing, recap and AI timeout fallback.
- [ ] Test no-network demo using cached personas/fixtures and fallback copy.
- [ ] Capture full recording; produce under-2-minute edit; test public judge link.

## If something breaks
- Foundry unavailable → deterministic fallback text.
- FPL adapter unavailable → demo personas/cached snapshot.
- Footage unusable → synthetic pitch animation.
- Stream drops → reconnect and fetch state snapshot.
- Overlay timing issue → manual rehearsal trigger panel (label demo appropriately).

## Submission checklist
Public repo; README/setup; synthetic-data disclosure; footage rights/attribution; working judge URL; demo video under 2 min; Microsoft services identified; secrets removed.
