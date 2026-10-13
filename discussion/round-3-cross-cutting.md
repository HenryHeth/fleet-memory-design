# Round 3 · Access, outside tools and the test harness

**Purpose:** settle the decisions that apply across all memory types.

---

### D3.1 · Network access

**Proposal:**
- **Tailscale Serve** (private) for our agents, Claude Code, Codex and phones.
- **Cloudflare Tunnel + Access** (public, with login) for cloud apps, added after the pilot.
- **Not Tailscale Funnel:** it's public with no login.

### D3.2 · What cloud apps can see

**Proposal:** cloud apps get **read-only** access to facts tagged `shareable`. There's no access to chats, inferred facts or anything tagged `private`. Each app gets its own token, which can be revoked on its own.

**Decide:** is read-only right, or should some cloud apps be allowed to propose facts?

### D3.3 · Order of authority when sources disagree

**Proposal:** confirmed fact > skill > original chat > recalled summary > inferred fact. This order is written into every agent's instructions and into the recall engine's ranking.

### D3.4 · Test harness

**Proposal:**
- Two cloned test profiles (`test-a`, `test-b`) receive identical scripted conversations.
- Made-up "canary" facts are probed at 5 checkpoints: same session, new session, next day, one week, one month.
- About 30 probes a night, capped by a nightly cost budget.
- Canaries never touch real agents or the real vault, and are deleted after 35 days.
- Exact-match grading for canaries; an AI judge only for "why did we decide X?" questions, which must cite a source.

**Decide:** is 30 probes a night enough? Any test you'd add or cut? Full matrix: [../docs/04-testing-by-type.md](../docs/04-testing-by-type.md)

### D3.5 · Alerts

**Proposal:** results go to the existing dashboard. Alert only when a score drops below its 4-week average. Real chats are scanned nightly for "should have known" misses, reported weekly.

---

**Reply format:** `D3.x ACCEPT | AMEND: … | REJECT: …`
