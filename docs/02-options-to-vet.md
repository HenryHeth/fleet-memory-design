# 02 · Two options for automatic recall (level 2)

Both options share levels 1 and 3, the config layers and the trust rules. They differ only in what fills the "before every reply" slot.

## Option A: G-Brain only

- One shared memory for every agent and tool.
- G-Brain fills the Hermes pre-reply memory slot directly.
- **For:** fewer moving parts; one memory, so nothing can disagree; one thing to back up.
- **Against:** G-Brain's own docs describe MCP and Claude Code/Codex hooks. Whether its Hermes setup fills the pre-reply slot is **unverified**. If not, we write a small plugin.
- **Against:** the full always-on version needs a server with 8GB+ of RAM and pay-per-use model costs for enrichment. It changes very fast (frequent releases).

## Option B: Mnemosyne + G-Brain

- **Mnemosyne:** local, per-agent short-term memory. It captures each turn and loads relevant recent context before every reply through the native Hermes memory-provider plugin.
- **G-Brain:** shared facts and deep search, same as Option A.
- **For:** a proven-shape path to "on the fly" recall inside Hermes; local and fast.
- **Against:** two memories that can disagree, so Mnemosyne must rank below confirmed facts and forget old material quickly.
- **Against:** per agent, not shared. One more component on every agent.
- **Against:** weakest published evidence. The repo's own retrieval-only benchmark table shows about 20% Recall@10, and it withdrew an earlier LongMemEval claim. Users report recall and tool-use problems.
- **Note:** Mnemosyne's consolidation (`sleep()`) must be invoked; it isn't on a timer. Profile isolation is off by default.

## How we decide

Run both against the **same frozen question set**, on the same two pilot agents:

1. **"Should already know" test (the deciding one):** fresh conversation, 20 questions the agents should know, with no instruction to look anything up. Any "let me check" or question back to the user is a fail.
2. **Changed-fact test:** change a fact; the old value must stop appearing.
3. **Planted-false-claim test:** the system must not adopt a claim nobody confirmed.
4. **Cross-tool test:** same answers from Hermes and from Claude Code.
5. **Upkeep log:** human minutes per week and incidents.

**Default if tied:** Option A, because it's simpler and nothing can disagree. Option B wins only if it clearly beats A on test 1 without failing tests 2–3.
