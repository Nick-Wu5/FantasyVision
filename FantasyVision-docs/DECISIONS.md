# Decisions, assumptions, and questions to resolve

## Source-of-truth decisions from the team plan
- Product is **FantasyVision**, fantasy-personalized overlays rather than a general-purpose tactical AI Match Director.
- Event source is a **deterministic synthetic timeline**, not computer vision.
- Footage is self-recorded/licensed or replaced by synthetic animation; keep attribution records.
- FPL credentials and browser cookies are never collected.
- Scoring, relevance, cooldown, and rank calculation are deterministic.
- Foundry produces narrative text only, validated before display; templates are fallback.
- Target experience: transparent 1080p overlay in OBS plus QR/mobile viewer setup.
- Deployment goal: Azure Container Apps, Foundry, Application Insights; Blob Storage where helpful.

## Confirm together BEFORE generating code
- [ ] **Personalization delivery model:** one broadcast overlay for a selected demo viewer, or a different browser overlay per viewer? **Proposed MVP:** one active persona controlled by demo panel, plus independent mobile preview. A single broadcast feed cannot simultaneously display unique graphics to everyone.
- [ ] **Fantasy scoring rules:** exact subset, positions, clean-sheet conditions, minutes played, and captain handling. **Proposed MVP:** goals by position, assists, saves, cards, clean-sheet-loss event, captain multiplier; document simplified rules.
- [ ] **Event-to-video sync:** `videoTimeMs` measures milliseconds from the beginning of the demo clip. **Proposed MVP:** replay starts with video at t=0 using one explicit start command; resync/reset supported.
- [ ] **Clock and SSE behavior:** replay emits original ordered events and graphics with sequence numbers; late subscribers receive current snapshot then new messages.
- [ ] **Team ownership:** four workstreams are defined in the PDF; confirm actual names and whether all four people are available.
- [ ] **Real FPL adapter:** optional only after core demo; default to local fixtures.
- [ ] **Footage asset/license:** owner and source; if unresolved by Oct 23, use synthetic pitch animation.
- [ ] **Cloud credentials/budget:** Azure access, Foundry model deployment, who owns secrets and cost controls.

## Scope change protocol
Any new feature must name (a) user-visible demo value, (b) owner, (c) integration contract, (d) time cost, and (e) what gets cut. No CV or unrelated fantasy product features before the end-to-end demo passes.
