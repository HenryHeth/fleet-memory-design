# 07 · Automated test methodology

**Goal:** prove, without anyone running tests by hand, that each level of memory works, and that it keeps working a day, a week and a month later. Most memory failures only show up over time: facts that were never captured, overwritten, made stale by a change, or tidied away by a consolidation job.

![Test timeline](../diagrams/memory-test-timeline.png)

## Core idea: plant, wait, probe

1. **Plant.** A test harness holds a normal conversation with an agent and mentions a harmless, made-up **canary fact** in passing. For example: *"Remind me, the spare dinghy key is now in the blue tin."* Each canary carries a unique marker so it can be graded exactly.
2. **Wait.** The harness probes again after 10 minutes, the next day, one week and one month. Each wait crosses a different risk: nightly jobs, weekly tidy-ups, long-term decay.
3. **Probe.** Each probe starts a **fresh conversation** and asks a question that needs the fact, **without hinting that it should look anything up**.
4. **Grade.** The harness checks what the agent answered, *and* how the memory arrived (see the next section).

## Grading: what counts as a pass

Every probe is logged with its full trace, so we know **how** the memory arrived, not just whether the answer was right:

| Result | Meaning | Level 1–2 grade |
|---|---|---|
| Right answer, no tool call | Memory was already in context | **Pass** |
| Right answer after a search tool call | The agent had to look | **Soft fail** for basic facts; pass for level 3 |
| "Let me check" / asks the user | The confidence-killer | **Fail** |
| Wrong or stale answer | Worse than not knowing | **Hard fail** |
| "I don't know" on a never-stated fact | Correct refusal to guess | **Pass** (negative control) |

Canary answers are graded by **exact match on the unique marker**, with no AI judge. An AI judge is used only for open questions such as "why did we decide X?", and every judged answer must also cite a source conversation that the harness can check.

## Two fact sets

- **Golden facts (real, read-only):** about 20 confirmed facts from the Obsidian vault, such as address, family members, boat name and standing rules. These are only *asked about*, never changed. They test level 1 every run.
- **Canary facts (made-up, planted):** new ones are planted each night and tagged `canary` so they can be withdrawn after 35 days. **Canaries go to dedicated test profiles, never into real agent memory.**

## What each test checks

| Test | Checks | Timeframes |
|---|---|---|
| **L1 core card** | Golden facts answered with no tool call; card rebuilt nightly | Every run |
| **L2 auto recall** | Canary arrives before the reply, unprompted | 10 min → 1 month |
| **L3 deep search** | Finds the fact *and* cites the exact original conversation | Day → month |
| **Capture** | A decision said in passing ends up indexed as said, with a link back | 10 min, next day |
| **Updates** | Change a canary; the old value must stop appearing everywhere | Day → month |
| **Bad facts** | A planted, unconfirmed claim is never promoted to the vault or core card | Every run |
| **Handoff** | Start a task, end the session; a new session (or another agent) picks it up correctly | 10 min, next day |
| **Time questions** | "What did we decide last Tuesday?" picks the right dated item | Week, month |
| **Distractors** | Two similar canaries (blue tin / red tin); the right one is returned | Every run |
| **Cross-tool** | Hermes and Claude Code give the same answer from the same memory | Day → month |
| **Access** | A cloud-app token cannot read a private fact | Weekly |
| **Skills** | Right skill loads unprompted for common requests; a patched skill changes behaviour next day; Claude Code finds the same skill | Day, week |
| **Failure** | Memory engine stopped: the agent says it can't verify rather than guessing | Monthly |

These map onto the five LongMemEval ability types: extraction, multi-session reasoning, time reasoning, knowledge updates and abstention. Results stay comparable with published work.

## The real-world signal (passive, no test needed)

The test suite measures a lab setup. The thing that actually matters is whether the agents annoy their user. A nightly job scans **real** conversations for an agent asking about something that is already in the vault or core card (for example "what's your address?" or "can you remind me…"). It reports the **should-have-known rate** per agent per week.

- This is the headline number. It should fall to near zero, and stay there.
- Every hit is linked to the exact message, so each miss can be traced to its cause: missing fact, card not loaded, or recall not triggered.

## Comparing Option A and Option B fairly

- Two cloned **test profiles** (`test-a` = G-Brain only, `test-b` = Mnemosyne + G-Brain) receive the **identical scripted conversations** at the same times.
- Both are probed with the same questions on the same schedule.
- After 30 days, compare: pass rate by level and age, stale-answer rate, should-have-known rate, cost per reply (extra tokens injected) and added delay before replies.
- **Tie goes to Option A** (simpler, one memory).

## Schedule (all automatic)

- **Nightly:** plant new canaries, run the 10-minute and next-day probes, run golden facts, and scan real conversations for should-have-known hits.
- **Weekly:** week-old canary probes, access test and distractor sweep.
- **Monthly:** month-old canaries, full sweep across all six agents, failure test (engine briefly stopped on the test profile only) and canary clean-up.
- **After every Hermes or memory-engine update:** the full quick suite. A drop blocks the rollout.

## Reporting

- One dashboard row per level × timeframe, plus the should-have-known trend.
- **Alert only when a score drops** below its 4-week baseline. Routine passes stay quiet.
- Every failure links to the full trace (prompt, injected memory, tool calls, answer), so diagnosing it takes minutes.

## Cost and safety

- About 30 short probe conversations a night across the two test profiles. Small, and capped by a nightly budget.
- Canaries are clearly made-up, tagged and auto-withdrawn. They never touch the real Obsidian vault or real agent profiles.
- Golden-fact probes are read-only.
