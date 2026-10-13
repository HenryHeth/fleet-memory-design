# 03 · Research findings

Sources are listed in [../research/sources.md](../research/sources.md). The detailed, citation-numbered brief is in [../research/evidence-brief-2026-10-13.md](../research/evidence-brief-2026-10-13.md).

## Framework

We used the common four-type split of agent memory (from the CoALA paper and an IBM explainer video):

- **Working:** the live context of the current conversation.
- **Semantic:** facts. Split into *confirmed* and *inferred*.
- **Episodic:** what happened. Split into *original conversation* and *distilled events and decisions*.
- **Procedural:** how to do things (skills, runbooks).

No product covers all four well. Procedural memory stays in versioned skills. Working memory belongs to each agent, with a portable handoff note.

## What each product actually does (from vendor docs)

- **Hermes (as installed):** strong live context and skills; exact per-agent chat search. Only a small note (2,200 + 1,375 characters) loads automatically. No shared memory across agents. One optional external memory provider per agent.
- **Hindsight:** distills conversations into typed facts and evidence-linked observations. Recalls by entity and time. API plus MCP. Not a transcript archive. Can run local models.
- **Honcho:** stores attributed messages and models each participant. Strongest for multi-party continuity; heaviest to self-host.
- **Mem0:** extracts facts and preferences. The current open-source version only adds, so old and new facts can sit side by side.
- **Supermemory:** keeps source documents separate from extracted facts, with an explicit approve/decline review queue for inferred facts. Its MCP is cloud-only.
- **Mnemosyne:** local SQLite, short-term working memory with time-to-live, episodic recall, "stated vs inferred" source labels. MCP plus native Hermes plugin. Consolidation must be invoked. Weakest evidence.
- **G-Brain:** stores facts with sources, supports corrections and withdrawal, and shares one memory across agents. Guides exist for Claude Code, Codex, Grok Bot and Muse. Has a Tailscale publish command, a keyword-first start, and answers with sources plus "what I don't know yet." Built and used in production by its author on OpenClaw/Hermes. *Read from docs only; not tested by us.*
- **Obsidian:** a plain-Markdown notebook. A good human-editable home for confirmed facts. A common pattern is Obsidian as source of truth, G-Brain indexing it, and every agent querying G-Brain over one MCP endpoint.

## Outside testing

- **One independent, same-setup Hermes study** (7 configurations, 30 simulated users, about 71k turns, 3,750 questions per provider): Honcho led on complicated personal histories, Mem0 on conditional preferences, and Hindsight did comparatively well on changed facts. **None reliably rejected planted false claims.** Some scores sat within judge noise. It's one simulated workload with specific versions, not a production guarantee.
- **Vendor benchmarks** (LongMemEval, LoCoMo, BEAM) often mix datasets, readers and judges. Treat them as method signals, not a ranking.

## Index as you go vs on query (LongMemEval)

The LongMemEval paper (ICLR 2025) splits memory into **indexing, retrieval and reading**. Findings that shaped our design:

- **Pulling facts out as the conversation happens, and attaching them as extra search keys on the original text** ("fact-augmented key expansion"), improved recall by about 9.4% and final accuracy by about 5.4% on average.
- **Time-stamping facts** and narrowing search to the relevant time range improved recall on "when did we…" questions by about 7–11%.
- **Even with perfect recall, reading is hard.** Structured, note-taking reading improved accuracy by up to 10 points.
- Commercial assistants showed large drops versus reading the full history. ChatGPT **overwrote important information** as chats went on; another assistant **missed things mentioned only in passing**.

**Design rule we took from this:** extract as you go, but as **signposts that point to the original**, never as a replacement. Answer from the source. Only confirmed items become authoritative. That is how you avoid locking in bad facts.

## User reports (lower confidence)

- A Hermes + Hindsight user turned off auto-save after interpretations polluted memory.
- A Honcho self-hoster reported duplicated and misattributed observations.
- A Mnemosyne user hit recall and tool-use problems (acknowledged by its creator).
- A user found Honcho good for relationship continuity but still needed exact Hermes chat search for specifics.
- A Hermes user runs Obsidian as source of truth, G-Brain as the index, with Claude Code, Codex, Grok and Hermes all on one MCP endpoint.

## What we got wrong first

1. **We rated features, not outcomes.** Our first scorecard gave Hermes credit for "has chat history" and "has skills," which made it look strong. The real failure is that the right memory doesn't show up unless an agent decides to search. Re-scored on results, Hermes today is the weakest row.
2. **We treated automatic recall as something to watch for.** It's the core requirement. A memory that only works when you say "look it up" doesn't restore trust.
3. **We missed G-Brain**, the product closest to our brief.
4. **We overstated the network barrier.** Cloudflare Tunnel + Access solves cloud-app access with a proper login.
