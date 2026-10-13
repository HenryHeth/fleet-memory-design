# Fleet memory: evidence-backed comparison

**Scope:** six Hermes profiles today; a portable memory chain for coding tools and other agents later. Research review, not a product installation or a live Homebase performance test.

## What the four layers really require

1. **Working:** model's live context is wrapper-owned. A portable *handoff* (task, decision, next action, evidence link) is a separate artifact. Hermes has live context; Mnemosyne adds a persistent short-lived working store and scratchpad, but its `sleep()` consolidation is explicit, not an automatic timer. Honcho offers recent messages and session summaries for reinjection.[8][4][3]
2. **Semantic:** distinguish **verified/current** facts from stated and inferred ones. Mnemosyne labels sources such as stated/inferred/tool/imported, but that does not prove truth. Hindsight consolidates evidence-linked observations; Supermemory down-weights inferred claims and offers approve/decline/undo. A current home address still needs an independently checked, authoritative record.[5][2][7]
3. **Episodic:** retain original conversation evidence **and** distilled experiences/decisions. Hermes has per-profile session transcripts; Honcho stores attributed messages and derived session context; Hindsight usually extracts typed memories rather than serving as a transcript archive. Supermemory stores source documents separately from extracted graph memories.[8][3][2][16]
4. **Procedural:** tested skills and runbooks remain versioned outside the memory engine. A retrieved suggestion is not an approved procedure. Mnemosyne's skill/SOP automation is a roadmap target, not a substitute for our existing skills.[10][8]

## Where each product actually differentiates

- **Hermes out of the box:** strong live context, built-in skills, exact per-profile transcripts/FTS search; tiny per-profile injected files (2,200/1,375 characters), no shared fleet fact store by default.[8]
- **Hindsight:** deep semantic/episodic *synthesis*: typed facts, entity/time-aware four-way recall, evidence-linked observations, mental models and `reflect`. Hermes can auto-retain/recall; it also has API and per-bank MCP. It does not replace original transcripts or a verified-fact register. Local processing is possible but requires model and database operations.[2][14][23]
- **Honcho:** strongest session/participant model: attributed messages, summaries, peer cards, conclusions and reasoning across a shared workspace. Especially relevant to multi-agent relationship continuity, but broad derived context can become contradictory and self-hosting has more moving parts.[3][1]
- **Mnemosyne:** strongest *local-first breadth*: SQLite working notes, episodic recall, structured facts, veracity labels, MCP/SDK and optional sync. However `sleep` needs invocation, evidence for current-version accuracy is limited, and automatic tested-skill promotion is not established. The repository's own benchmark notes 20% Recall@10 in a retrieval-only table and withdraws an unsupported earlier LongMemEval claim.[4][5][10]
- **Mem0:** focused extracted facts/preferences and query-time search. The current OSS algorithm is ADD-only, so changed facts can coexist until retrieval chooses among them; Graph Memory is Platform-only. Hosted MCP does not by itself record every external agent conversation.[6][18]
- **Supermemory:** source documents + graph-derived facts and user profiles; uniquely explicit inferred-fact review queue. Hosted MCP/connectors are not part of its local binary, so the cloud and local deployment designs differ.[16][7][17]

## What outside tests say—and do not say

The most useful shared-setup study I found is an **independent practitioner** comparison of seven self-hosted Hermes configurations: 30 simulated users, 71,060 dialogue turns and 3,750 questions per provider about changing facts, false claims and conditional preferences. It held the answer model and judge constant. Honcho led on complicated personal histories; Mem0 led on conditional preferences; Hindsight was comparatively good on changed facts at less model-token workload than Honcho. None reliably rejected planted false claims.[1]

That is *one* simulated workload, not a production guarantee: it did not test durability, privacy, access control, cross-wrapper capture or support. It used specific older versions/configurations, and some ground-truth labels themselves are questionable. Hindsight's 0.281 and Supermemory's 0.288 macro scores were within the report's judge-noise band; treating their order as a winner would be false precision.[1]

Vendor benchmark numbers (LongMemEval, LoCoMo, BEAM) often mix datasets, readers, judges and scoring rules. Hindsight's paper compared some independently run results against copied baseline reports; the original LongMemEval benchmark also distinguishes answer accuracy from evidence retrieval. These are useful signals about methods, not a verified all-product ranking.[9][19][20]

**Reddit/practitioner signal, lower confidence:** a Hermes Hindsight user disabled auto-retain after interpretations polluted memory; a Honcho self-host user reported duplicated and misattributed observations; a Mnemosyne NAS user encountered non-English and recall/tool-use problems, with creator acknowledgement. A short multi-layer trial found Honcho useful for relational continuity but still needed exact Hermes transcript search for a title. These are environment-specific reports, not controlled comparisons. Reddit live pages blocked retrieval during this review; complete post/comment text was checked in an archival copy and original permalinks are listed here.[11][12][13][21]

## Current recommendation (updated 2026-10-13)

**No single product covers all four layers well.** Recommended stack, highest authority first:

1. **Verified facts:** a small fact register we own (address, family, standing rules). Changes only on Paul's confirmation and overrides every other layer.
2. **Skills:** Hermes skills (SKILL.md), versioned and patched after real wins and mistakes.
3. **Raw history:** Hermes session transcripts plus Toodledo task notes (these already act as handoffs).
4. **Recall engine:** Hindsight, the only new service. It distills decisions and patterns from conversations and *proposes* new facts; it cannot change layer 1 on its own.

Only layer 4 is replaceable. If faithful multi-party history becomes the gap, test Honcho in that slot. Layers 1–3 stay in owned formats, so switching engines loses nothing.[1][2][3]

**Improvement loops:** a weekly 5-minute review of proposed facts; skill patches after real outcomes; a monthly 20-question recall test that alerts only when the score drops.

## Portability to other tools (operational driver)

Requirement: the same memory must be usable from Claude Code, Codex and other agents (Sesame, Muse, Grok bots, Dot), not just Hermes.

- **One shared front door:** expose the fact register *and* the recall engine through a single MCP/API endpoint with its own login and per-tool permissions. If only Hindsight is exposed, outside tools get recollections but not confirmed facts.[14][24]
- **Reading is easy; writing back is not.** Connecting a tool over MCP lets it *read* memory. It does not send that tool's conversations back. This applies to every product reviewed, including Hindsight and Mnemosyne.[10][14]
- **Fit by tool:**
  - *Claude Code and Codex:* full fit. They read over MCP, and their local chat logs can be fed into Hindsight by a nightly job.
  - *A Grok bot we build on xAI's API:* good fit. xAI documents remote MCP support.[25]
  - *Sesame:* read-only at best. It documents connecting outside apps, but each assistant keeps separate memory; conversations will not flow back.[26]
  - *Muse, the consumer Grok app, Dot:* unconfirmed. No evidence found of outside-memory connections. Treat as "maybe later."
- **Product effect:** the core pick does not change. Hindsight remains suitable because it can be self-hosted and offers both MCP and an API.[14] Supermemory would be the easiest path to consumer apps because it is already hosted, at the cost of storing memories in its cloud; keep it as a fallback, not the first choice.[17]

## Network access: Tailscale vs Cloudflare

Cloud apps such as Sesame run on their vendor's servers and cannot reach Homebase's private network. Two access paths are needed:

- **Tailscale Serve (private):** only devices on our Tailscale network can connect. Use for Claude Code, Codex, the six agents and Paul's phone. Nothing is exposed publicly. Already in use for the Hermes dashboard.
- **Tailscale Funnel (public):** puts the service on the open internet but adds **no login**; we would have to build and maintain authentication ourselves. Not recommended for personal facts.[27]
- **Cloudflare Tunnel + Cloudflare Access (public, with login):** gives Homebase a public address without opening router ports. Access puts a login in front of it and supports the standard OAuth flow MCP clients use, so cloud apps get a normal "sign in to connect" step. Less security code for us to own.[28][29]

**Decision:** Tailscale Serve for our own tools; Cloudflare Tunnel + Access for cloud apps, exposing **read-only, non-sensitive** memory by default. Sensitive facts stay on the private path.

**Unverified:** whether Sesame completes the Cloudflare Access login. Its documentation indicates the right login type; count it as working only after a real connection test.

## First design and substitute gate

Preserve raw transcripts, approved facts and versioned skills in owned formats. Start with a narrow pilot: **Bob + Henry + Claude Code**, scoped identities, no sensitive blanket ingestion. Hindsight is the first engine because evidence-linked consolidation of changing facts and decisions is the priority. Honcho is the alternative if faithful multi-party continuity becomes the priority; Mnemosyne if local/offline operation outweighs current recall confidence. No product removes the need for a verified-fact gate or an explicit handoff contract.[1][2][3][4]

**Pilot order:**
1. Fact register + Hindsight behind one front door, private via Tailscale Serve.
2. Connect Bob, Henry and Claude Code; add the nightly Claude Code/Codex chat import.
3. Run the 20-question test from both Hermes and Claude Code — answers must match.
4. Add Cloudflare Tunnel + Access with read-only scope; final step is a real Sesame connection test.

Use one frozen set of our real questions (fact changes, disputed claims, decision provenance, handoff, conditional preference, permission isolation). Test capture → retrieval → final answer separately; also read back correction/deletion and inspect export/import. Only substitute the middle engine if it fails a requirement. Do not rerun a four-vendor bake-off by default.[1][19]

## Sources

[1] https://engturtle.github.io/hermes-memconflict/report
[2] https://hindsight.vectorize.io
[3] https://honcho.dev/docs/v3/documentation/core-concepts/architecture
[4] https://docs.mnemosyne.site/architecture/beam-overview
[5] https://docs.mnemosyne.site/architecture/veracity-signal
[6] https://docs.mem0.ai/migration/oss-v2-to-v3
[7] https://supermemory.ai/docs/recall/memory-review
[8] https://hermes-agent.nousresearch.com/docs/user-guide/features/memory
[9] https://arxiv.org/html/2512.12818v1
[10] https://github.com/mnemosyne-oss/mnemosyne
[11] https://www.reddit.com/r/hermesagent/comments/1txfg3j
[12] https://www.reddit.com/r/hermesagent/comments/1t766jo
[13] https://www.reddit.com/r/hermesagent/comments/1tsonau
[14] https://hindsight.vectorize.io/developer/mcp-server
[16] https://supermemory.ai/docs/concepts/graph-memory
[17] https://supermemory.ai/docs/self-hosting/overview
[18] https://docs.mem0.ai/platform/mem0-mcp
[19] https://github.com/xiaowu0162/longmemeval
[20] https://arxiv.org/html/2510.27246v1
[21] https://www.reddit.com/r/hermesagent/comments/1v47wa9/comment/oz945iy
[23] https://hindsight.vectorize.io/developer/models
[24] https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
[25] https://docs.x.ai/developers/tools/remote-mcp
[26] https://www.sesame.com/journal/getting-started
[27] https://tailscale.com/docs/features/tailscale-funnel
[28] https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/secure-mcp-servers/
[29] https://developers.cloudflare.com/changelog/post/2025-08-26-access-mcp-oauth/
