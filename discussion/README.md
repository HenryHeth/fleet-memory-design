# Decision session: agree an implementable memory design in 4 rounds

**Goal:** leave the session with a pilot we can build: every component chosen, every number set, every owner named.

**Format:** a group chat between agent teams. Each round lists numbered decisions. Every decision has a **proposed default**, the alternatives, and the evidence. We are not asking open questions; we are asking you to **accept, amend or reject** a specific proposal.

## How to respond

Reply once per round, one line per decision you have a view on:

```
D2.3 ACCEPT
D2.5 AMEND: capture at end of session, not per turn. Reason: per-turn doubled our token cost (our measurement: ...)
D2.6 REJECT: prefer Hindsight over G-Brain. Evidence: ...
```

**Rules**
1. **Silence = accept.** Only reply on decisions you'd change.
2. **Amend and reject need a specific alternative and a reason.** Evidence or first-hand experience beats opinion.
3. **One round per turn.** The facilitator (Bob) posts a short summary of what's agreed before moving on.
4. **No consensus after one exchange → the default stands**, marked "revisit after pilot data". The tests decide, not the debate.
5. **Out of scope** for this session: anything not needed to start the pilot.

## Agenda

| Round | Decide | Decisions | Output |
|---|---|---|---|
| [1 · Framework](round-1-framework.md) | Are we solving the right problem, measured the right way? | D1.1–D1.3 | Agreed requirements + success numbers |
| [2 · Memory types](round-2-memory-types.md) | What fills each part of each memory type? | D2.1–D2.8 | Component for every row of the design |
| [3 · Cross-cutting](round-3-cross-cutting.md) | Access, outside tools, test harness | D3.1–D3.5 | Access model + test settings |
| [4 · Commit](round-4-commit.md) | Pilot scope, order, owners, go/no-go | D4.1–D4.4 | A buildable pilot plan |

Results are recorded in [decision-log.md](decision-log.md), which becomes the build spec.

**Background, if needed:** [framework](../docs/01-framework.md) · [scorecard + evidence](../docs/02-scorecard-evidence.md) · [design](../docs/03-design-by-type.md) · [tests](../docs/04-testing-by-type.md)
