# Decision log

Filled in during the session. Once complete, this is the build spec for the pilot.

**Status key:** ✅ agreed · ✏️ agreed with amendment · ⏸ default stands, revisit after pilot data · ❌ rejected (replacement noted)

| ID | Decision | Default proposed | Outcome | Final wording / amendment | Raised by |
|---|---|---|---|---|---|
| D1.1 | Structure | Four memory types, seven parts | ✏️ | Eight parts: add **standing rules** (how to behave) under procedural, separate from skills and facts. Tested by planted situations. | LifeOS; Bob agreed |
| D1.2 | Requirements order | Unasked > bad facts > shared > upkeep > tools > portable | ✏️ | Order kept (shared stays above other tools). Upkeep: one number, ≤ 10 min/week in pilot, ≤ 5 min after. | Bob; LifeOS agreed |
| D1.3 | Success numbers | See round 1 table | ✏️ | Add: injected context per reply (capped; card reports fill + freshness every turn); rule-break rate ≤ 5% on planted situations; every 0 / ≥95% target gets a positive control seen failing before night one (lives in D3.4); upkeep per D1.2. | LifeOS + Bob |
| D2.1 | Handoff note | Toodledo task note, written at session end | ✏️ | Task note kept, written by the agent as a step while working (not end-of-session hook); one owner per note. | LifeOS; Bob agreed |
| D2.2 | Confirmed facts home | Obsidian vault in git | ✏️ | Each note gets a header (id, status, valid from/to or replaced-by, source, author, readers); one promoter job is the only writer; git = change log; read limits from day one. | LifeOS; Bob agreed |
| D2.3 | Core card | ≤ 1,500 characters shared + ≤ 500 per agent, nightly | ✏️ | 1,500 + 500 kept; card built per agent from notes it may read; build fails if over cap; card on its own path (not MEMORY.md); test that an agent's own memory write never reaches the card. | LifeOS; Bob agreed |
| D2.4 | Inferred facts | Tagged, weekly human review, 90-day expiry | ✏️ | Human gate kept; daily review capped ~5 items (fits 10 min/week); dedupe/filter first; unreviewed items expire; candidates in a file we own. | LifeOS; Bob agreed |
| D2.5 | Capture timing | Per turn, linked to original | ✏️ | Per turn; capture whole turn (prompt, reply, tool calls, failures) from hooks; tag items decided vs planned. | LifeOS; Bob agreed |
| D2.6 | Recall engine | A/B pilot; tie goes to G-Brain only | ✏️ | Recall on (G-Brain pre-reply) vs recall off on same profiles, plus full-context and plain-search baselines (Hermes allows one memory provider). | LifeOS; Bob agreed |
| D2.7 | Original chats | Keep in place; nightly import; keyword first | ✏️ | Import from hook data, keep original timestamps, strip secrets before storing. | LifeOS; Bob agreed |
| D2.8 | Skills | Hermes skills in git; engine indexes them | ✏️ | SKILL.md folders in git; each reviewed skill pinned by content hash checked at load. | LifeOS; Bob agreed |
| D3.1 | Network | Tailscale Serve; Cloudflare + Access later | ✏️ | Serve kept; per-agent token for memory server; server enforces who may write what. | LifeOS; Bob agreed |
| D3.2 | Cloud app scope | Read-only, `shareable` facts only | ✏️ | Read-only; filter `shareable` before and after retrieval; never expose vector index; cloud proposals go to same staging. | LifeOS; Bob agreed |
| D3.3 | Authority order | Confirmed > skill > chat > summary > inferred | ✏️ | Order kept, enforced in injection: current values only, each labelled with tier; program-checkable rules go in hooks. | LifeOS; Bob agreed |
| D3.4 | Test harness | 2 test profiles, 5 checkpoints, ~30 probes/night | ✏️ | Exact-match grading + baselines and canaries per LifeOS. Night one: false-claim, stale-fact, out-of-scope, planted-secret, own-memory-write-to-card. Rest by week 2. Rerun affected tests on any model/tool/engine change. | LifeOS; Bob agreed |
| D3.5 | Alerts | Dashboard; alert on drop vs 4-week average | ✏️ | Immediate alert on any failed false-claim or out-of-scope canary; one known-failing canary nightly to prove the alert path. | LifeOS; Bob agreed |
| D4.1 | Pilot scope | Bob, Henry, Claude Code, 2 test profiles | | Gate on the other four agents joining (each passes scope tests before getting a token) | Pilot covers Bob + Henry only (LifeOS, R4) |
| D4.2 | Build order | Steps 0–5 with gates | | | |
| D4.3 | Owners | See round 4 | | | |
| D4.4 | Go / no-go | Targets met → go; 1–2 misses → 14-day fix; recall fails → Hindsight | | | |

## Parked for after the pilot

| Item | Why parked |
|---|---|
| | |
