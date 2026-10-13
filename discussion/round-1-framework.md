# Round 1 · Framework and success criteria

**Purpose:** agree what we're solving and how we'll know it worked, before choosing any tools. Short round.

---

### D1.1 · Use the four memory types as the structure

**Proposal:** organise design, scores and tests around working, semantic, episodic and procedural memory (CoALA), split into seven parts: live context, handoff note, confirmed facts, inferred facts, original chats, distilled decisions, skills.

**Alternatives:** (b) a simpler "facts + history + skills" split; (c) organise by tool instead of by memory type.

**Why the default:** the split exposed two gaps we'd otherwise have missed (no owner for handoffs, no test for skills).

---

### D1.2 · The requirements, in priority order

**Proposal:**
1. **Shows up unasked.** No "let me check" on basic facts.
2. **Blocks bad facts.** Guesses never become "true" on their own.
3. **Shared** by all agents.
4. **Low upkeep.** At most 5 minutes a week of human time.
5. **Works from other tools** (Claude Code and Codex in the pilot; cloud apps later).
6. **Portable.** Facts, skills and history stay in files we own.

**The question:** is the order right? In particular, should "works from other tools" rank above "shared"?

---

### D1.3 · Success numbers for the pilot

**Proposal:** after 30 days, the pilot passes if:

| Measure | Target |
|---|---|
| Golden facts answered with **no tool call** | ≥ 95% |
| Distilled decisions recalled unasked at 1 week | ≥ 80% |
| Distilled decisions recalled unasked at 1 month | ≥ 70% |
| Planted false claims promoted to confirmed facts | **0** |
| Stale answer after a fact is changed (at 1 week) | ≤ 5% |
| Handoff resumed correctly by another agent | ≥ 90% |
| Right skill loaded unprompted | ≥ 85% |
| Should-have-known rate in real chats | ≤ 1 per agent per week |
| Human upkeep | ≤ 10 minutes a week |
| Added delay before each reply | ≤ 2 seconds |

**The question:** too strict, too loose, or missing a measure? Proposed numbers only; there's no baseline yet. Step 0 of the pilot measures today's setup first.

---

**Reply format:** `D1.x ACCEPT | AMEND: … | REJECT: …`
