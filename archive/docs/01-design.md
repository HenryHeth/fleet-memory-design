# 01 · Recommended design

## Principle

**Owned core, swappable engine.** Facts, skills and history live in plain files we control. The memory engine indexes them and recalls from them, but is never the only copy of anything.

## Three levels of recall

| Level | What | When it loads | Can it be missed? |
|---|---|---|---|
| 1. Always known | Core card: address, family, standing rules, active projects | Start of every conversation | No. No search or AI step. |
| 2. Recalled automatically | Relevant decisions, past conversations, people, projects | Before every reply, triggered by the system | Rarely. Depends on retrieval quality. |
| 3. Searched on demand | Older or detailed history, with links to the exact conversation | When the agent calls a search tool | Yes, if the agent doesn't search. Acceptable for deep history only. |

**Why level 1 exists:** basic facts should never depend on a search succeeding. The core card is built nightly from confirmed facts. Trade-off: when a fact changes, agents pick it up at their next new conversation.

**Why level 2 must be system-triggered:** Hermes has a memory-provider slot that runs a lookup automatically before each reply. A memory reached only through a tool the agent may or may not call doesn't fix the "should have known" problem.

## Config layers (top to bottom)

1. **Who connects:** six Hermes agents (pilot: two), Claude Code and Codex. Cloud apps (Sesame, Grok bot, Muse) come last, read-only.
2. **How they reach it:** Tailscale Serve (private) for our own tools; Cloudflare Tunnel + Access (public, with login) for cloud apps. One scoped token per agent.
3. **Front door:** one G-Brain MCP endpoint, so facts and recall come through the same door and every tool gets the same answer.
4. **Recall engine:** G-Brain. Start with keyword search and no AI keys, then add local embeddings (Ollama), then synthesis and overnight tidy-up, one at a time, each only after the test passes.
5. **Capture:** pull out decisions and facts as each conversation happens, each linked to the exact chat. Claude Code and Codex logs are imported nightly.
6. **Sources of truth:** Obsidian vault (confirmed facts), Hermes skills (how-to), Hermes chats + Toodledo task notes (evidence). Kept in git and backed up nightly to the NAS.

## Trust rules

- **Who wins when sources disagree:** confirmed fact > skill > original conversation > recalled summary.
- **New facts:** the engine *proposes*; the human confirms in a weekly 5-minute review. Inferred facts never become authoritative on their own.
- **Capture is signposting, not replacement.** Extracted facts point back to the original text; the original is never thrown away. This is what keeps one bad extraction from locking in a bad fact.
- **Sensitive facts** are tagged private and only go out over the private network.
- **Swap rule:** only the front door and engine (layers 3–4) are replaceable. Hindsight is the backup engine.

## Why not one product?

No product reviewed covers all of this. Engines that save and recall automatically (Hindsight, Honcho, Mem0, Supermemory) are weakest at keeping bad facts out. G-Brain is strongest at sharing, sources and corrections, but carries more upkeep and less outside evidence. Obsidian is a trustworthy notebook but recalls nothing by itself. See the scorecard in the README.
