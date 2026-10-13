# 02 · Scorecard and evidence

![Four types scorecard](../diagrams/01-four-types-scorecard.png)

Ratings are judgement calls from vendor docs, one independent Hermes test and user reports. The two option rows are **targets, not measurements**. The [test plan](04-testing-by-type.md) replaces each circle with a measured score.

## What the scorecard says

- **No single tool fills its row.**
- **Hermes today** is strong on live context and skills, but fails "shared by all agents" and "shows up unasked". That's the gap users feel. It keeps chats but distils nothing from them.
- **Engines that save and recall by themselves** (Hindsight, Honcho, Mem0, Supermemory) are weakest at blocking bad facts.
- **G-Brain** is strongest on confirmed facts, sharing and other tools, but has more upkeep and the least outside evidence (docs only, untested by us).
- **Obsidian** is the most trustworthy home for confirmed facts, but recalls nothing by itself.

## Evidence by tool

| Tool | What it actually does (vendor docs) | Outside evidence |
|---|---|---|
| **Hermes** | Strong live context and skills; exact per-agent chat search. Only a small note (2,200 + 1,375 characters) loads automatically. Not shared across agents. One optional external memory provider per agent. | Live audit of our six agents: most notes over their limits, no shared store |
| **Hindsight** | Distils chats into typed facts and evidence-linked observations; entity- and time-aware recall; API + MCP; can run local models. Not a transcript archive. | Independent study: comparatively good on changed facts. Reddit: a user turned off auto-save after it polluted memory |
| **Honcho** | Stores attributed messages; models each participant; summaries and conclusions across a shared workspace. | Independent study: best on complex personal histories. Self-hosters report duplicated or misattributed observations |
| **Mem0** | Extracts facts and preferences. Current open-source version only adds, so old and new facts sit side by side. | Independent study: best on conditional preferences |
| **Supermemory** | Source documents kept separate from extracted facts; explicit approve/decline queue for inferred facts. MCP is cloud-only. | Limited |
| **Mnemosyne** | Local SQLite; short-term working memory with expiry; "stated vs inferred" labels; native Hermes plugin + MCP. Consolidation must be triggered. | Its own benchmark table shows ~20% Recall@10; it withdrew an earlier LongMemEval claim. User reports recall and tool-use problems |
| **G-Brain** | Facts with sources, corrections and withdrawal; one memory shared across agents; guides for Claude Code, Codex, Grok Bot and Muse; Tailscale publish; answers with sources and "what I don't know yet." Built and run by its author on OpenClaw/Hermes. | Docs only. One Reddit setup: Obsidian → G-Brain → four agents on one MCP endpoint |
| **Obsidian** | Plain-Markdown notebook, edited by people. | Common pattern as G-Brain's source of truth |

## Outside testing worth knowing

- **Independent Hermes study** (7 configurations, 30 simulated users, ~71k turns, 3,750 questions each). Honcho led on complex histories, Mem0 on conditional preferences, and Hindsight did well on changed facts. **None reliably rejected planted false claims.** It's one simulated workload; some scores sat within judge noise.
- **LongMemEval** (ICLR 2025) splits memory into indexing, retrieval and reading:
  - Pulling facts out as the conversation happens, and attaching them as extra search keys **on the original text**, improved recall by ~9% and accuracy by ~5%.
  - Adding dates improved "when did we…" questions by ~7–11%.
  - Commercial assistants **overwrote** important information and **missed** things said in passing.
  - **Design rule:** extract as you go, as signposts that point back to the original.
- **Vendor benchmarks** (LongMemEval, LoCoMo, BEAM) mix datasets and judges. Treat them as method signals, not a ranking.

## What we got wrong first

1. **We rated features, not outcomes.** "Has chat history" made Hermes look strong. The failure is that memory doesn't show up unless an agent searches.
2. **We treated automatic recall as nice-to-have.** It's the core requirement.
3. **We missed G-Brain**, the product closest to our brief.
4. **We drifted from the four types** into separate framings (layers, levels, outcomes). This version re-anchors everything on the four types.

Sources: [../research/sources.md](../research/sources.md). Detailed brief: [../research/evidence-brief-2026-10-13.md](../research/evidence-brief-2026-10-13.md).
