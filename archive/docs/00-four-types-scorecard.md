# 00 · The design, organised by the four types of memory

This is the master view. Every other document supports it.

![Four types scorecard](../diagrams/memory-four-types-scorecard.png)

## The framework

We use the four memory types from the CoALA paper (Cognitive Architectures for Language Agents) and the IBM explainer that introduced it to us. Each type is split into the parts that behave differently:

| Type | Part | What it is |
|---|---|---|
| **Working** | Live context | The current conversation |
| | Handoff note | Where a task was left: status, blockers, next step |
| **Semantic** | Confirmed facts | Facts a person has confirmed (address, family, standing rules) |
| | Inferred facts | Facts a system worked out from conversations, unconfirmed |
| **Episodic** | Original chats | The exact record of what was said |
| | Distilled decisions | Decisions and events pulled out of chats, with dates |
| **Procedural** | Skills | How to do things: tested, versioned runbooks |

The later discussion added six **requirements** that cut across all four types: memory **shows up unasked**, is **shared by all agents**, works from **other tools**, **blocks bad facts**, needs **low upkeep**, and has **outside evidence** behind it.

## How the design covers each type

| Part | Lives in | Reaches the agent | Option A | Option B adds | Why (evidence) | Test |
|---|---|---|---|---|---|---|
| Live context | Hermes | Always (it is the conversation) | Hermes | Mnemosyne short-term store | Hermes is strong here today | Handoff + time tests |
| Handoff note | **Toodledo task note** (owner: the agent on the task) | Loaded at session start when a task is active | Hermes + G-Brain index | Mnemosyne scratchpad | No product ships a handoff contract; it must be an owned artifact | Handoff test: new session / other agent continues correctly |
| Confirmed facts | **Obsidian vault** | **Core card** at every session start; G-Brain recall | Obsidian → core card + G-Brain | same | Every engine tested repeated planted false claims, so facts can't depend on an engine | Golden facts every run, no tool call allowed |
| Inferred facts | G-Brain (tagged *inferred*) | Recalled, ranked below confirmed | G-Brain | Mnemosyne (tagged *inferred*) | Supermemory/Mnemosyne show labelling + review works; promotion needs a human | Planted bad fact never reaches vault or card |
| Original chats | Hermes chats, Claude Code / Codex logs | Deep search on demand, cited | G-Brain index | same | LongMemEval: keep the original; answer from the source | Deep search cites the exact chat |
| Distilled decisions | G-Brain, linked to the original chat | **Recalled automatically before each reply** | G-Brain pre-reply | Mnemosyne pre-reply (faster, per agent) | LongMemEval: extract-as-you-go + dates improved recall ~9% and time questions ~7–11% | Canary probes at 10 min / day / week / month |
| Skills | Hermes skills (git) | Skill index loaded every session; full skill on use | Hermes (+ G-Brain shares to other tools) | same | No memory product does procedural memory well | **Skill test** (below) |

## What changed from the earlier scorecard

- **Two new tools:** G-Brain and Obsidian.
- **Rows for the two designs** replace the single "recommended combo" row.
- **Requirements re-weighted:** "shows up unasked" and "shared by all agents" are now columns. The earlier version had no such columns, which is why Hermes looked best-in-class.
- **Hermes "distilled decisions" lowered to none.** Hermes keeps chats but distils nothing from them.

## Two gaps the four-type view exposed, now closed

1. **Handoff note had no owner.** Now it's the Toodledo task note, owned by the agent working the task, loaded when a task is active, and indexed by G-Brain for other tools.
2. **Skills were untested.** New automated skill test:
   - For each of about 10 common requests (for example "check the boat battery"), the harness starts a fresh session and checks that the agent **loads the right skill without being told to**.
   - After a skill is patched, a canary instruction added to it must appear in the agent's behaviour the next day.
   - Through G-Brain, Claude Code must find the same skill.

## Where the scores come from

| Row | Main sources |
|---|---|
| Hermes | Hermes memory, sessions and provider docs; live audit of our six agents (per-agent notes over their limits, no shared store) |
| Hindsight | Vendor docs (retain, observations, MCP); independent Hermes study; Reddit report of auto-save pollution |
| Honcho | Vendor architecture docs; independent study (highest on complex histories); self-host user reports |
| Mem0 | v3 OSS migration notes (add-only, old facts linger); independent study (best on conditional preferences) |
| Supermemory | Memory-review docs (inferred-fact queue); self-hosting docs (MCP is cloud-only) |
| Mnemosyne | Repo docs (working memory TTL, veracity labels, `sleep()` manual); own benchmark table (~20% Recall@10); user report |
| G-Brain | Repo README only (sources, corrections, sharing, Claude Code/Codex/Grok/Muse guides, Tailscale). **Untested by us** |
| Obsidian | Plain Markdown, human-edited; one Reddit setup using it as G-Brain's source of truth |

All sources are linked in [../research/sources.md](../research/sources.md). Ratings are judgement calls, not measurements. The test method in [07-test-methodology.md](07-test-methodology.md) is how we replace them with numbers.
