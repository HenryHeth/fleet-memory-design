# 01 · The framework: four types of memory

Everything in this repo is organised around one framework, so every design choice, score and test can be traced to the same structure.

## The four types

Taken from the CoALA paper (*Cognitive Architectures for Language Agents*) and IBM's explainer on agent memory. Each type is split into the parts that behave differently, because they need different storage, trust rules and tests.

| Type | Part | What it is | Why split it |
|---|---|---|---|
| **Working** | Live context | The current conversation | Owned by each agent; lost when the session ends |
| | Handoff note | Where a task was left: status, blockers, next step | Must survive the session and pass between agents |
| **Semantic** | Confirmed facts | Facts a person has confirmed (address, family, standing rules) | Must be authoritative |
| | Inferred facts | Facts a system worked out from conversations | Useful, but can be wrong. Must never become "true" on their own |
| **Episodic** | Original chats | The exact record of what was said | The evidence; never replaced |
| | Distilled decisions | Decisions and events pulled out of chats, with dates | Makes the past findable; must link back to the original |
| **Procedural** | Skills | How to do things: tested, versioned runbooks | Improves behaviour, not knowledge |

## The requirements

Six requirements cut across all four types. They came out of the discussion and are what turned this from a feature comparison into a design:

1. **Shows up unasked.** Agents already know the basics, with no "let me check." Being asked something an agent should obviously know is what kills confidence.
2. **Shared by all agents.** Tell one agent, and every agent knows.
3. **Works from other tools.** Claude Code and Codex now; Sesame, Grok bots, Muse and Dot where possible.
4. **Blocks bad facts.** Changed facts replace old ones; guesses are never promoted on their own.
5. **Low upkeep.** About 5 minutes a week from the human.
6. **Outside evidence.** Prefer what has been independently tested.

Plus one design constraint: **portable.** Facts, skills and history stay in files we own, so the memory engine can be swapped.

## How the rest of the repo uses this

- [02 · Scorecard](02-scorecard-evidence.md): every tool rated on each part of each type, plus the requirements.
- [03 · Design](03-design-by-type.md): what fills each part, and how it reaches the agent.
- [04 · Testing](04-testing-by-type.md): an automated test for each part, over short and medium timeframes.
- [Discussion topics](../discussion/README.md): open questions, grouped the same way.
