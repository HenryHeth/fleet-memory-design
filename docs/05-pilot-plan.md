# 05 · Pilot plan (draft)

**Scope:** two Hermes agents (engineering + chief of staff), Claude Code and two test profiles. No blanket import of sensitive data. Nothing installed yet.

| Step | What | Memory type | Exit check |
|---|---|---|---|
| 0 | **Build the test harness**; run it against today's setup | All | Baseline scores on every grid cell + should-have-known rate |
| 1 | Obsidian vault of confirmed facts + nightly core card | Semantic | Golden facts pass with no tool call |
| 2 | Handoff note from the Toodledo task note, loaded when a task is active | Working | Handoff tests pass, new session and other agent |
| 3 | G-Brain, keyword-only (no AI keys), private over Tailscale; index vault, chats, skills | Episodic, procedural | Deep search cites the exact chat; Claude Code gets the same answers |
| 4 | **Option A:** G-Brain in the Hermes pre-reply slot (or a small plugin) | Episodic, semantic | Distilled-decision probes pass unasked |
| 5 | **Option B:** add Mnemosyne on `test-b` | Working, episodic | Same suite, same 30 days |
| 6 | Decide A vs B | — | Rules in [03](03-design-by-type.md#two-options-to-vet) |
| 7 | Expand: other four agents → local embeddings → Cloudflare + Access (read-only) → Sesame connection test | All | No score drops at any step |

**Ongoing upkeep target:** a weekly 5-minute review of proposed facts. Everything else is automatic, and alerts fire only on a drop.
