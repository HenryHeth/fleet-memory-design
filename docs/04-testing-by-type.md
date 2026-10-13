# 04 · Testing, by type of memory

![Test matrix](../diagrams/03-test-matrix.png)

**Goal:** replace every judgement rating on the scorecard with a measured score, automatically. Each part of each memory type gets its own test, run in the **short term** (same session, new session) and the **medium term** (next day, one week, one month). Most memory failures only appear over time: never captured, overwritten, not updated, or tidied away by a consolidation job.

## Method: plant, wait, probe

1. **Plant.** A test harness talks to an agent normally and mentions a harmless, made-up **canary**, such as *"the spare dinghy key is now in the blue tin."* Each canary has a unique marker, so grading is exact.
2. **Wait.** Probe at each timeframe. Each one crosses a different risk: compression, session end, nightly jobs, weekly tidy-ups, long-term decay.
3. **Probe.** Start a **fresh conversation** and ask a question that needs the memory, **with no hint to look anything up**.
4. **Grade** both the answer and **how the memory arrived**, using the full trace.

| Result | Basic facts (working, semantic, distilled decisions) | Deep history (original chats) |
|---|---|---|
| Right, no tool call | **Pass** | Pass |
| Right after searching | **Soft fail** | Pass, if it cites the source |
| "Let me check" / asks the user | **Fail** | Fail |
| Wrong or stale | **Hard fail** | Hard fail |
| "I don't know" on something never said | **Pass** (correct refusal) | Pass |

Canaries are graded by exact match, with no AI judge. An AI judge is used only for open "why did we decide X?" questions, and those answers must cite a conversation that the harness checks.

## Tests by type

### Working memory
| Part | Short term | Medium term |
|---|---|---|
| **Live context** | Plant early in a long chat; force compression; it's still known | n/a (session-bound) |
| **Handoff note** | Start a task, end the session; a new session resumes at the right step with no re-explaining | Next day, a **different agent** resumes the same task correctly |

### Semantic memory
| Part | Short term | Medium term |
|---|---|---|
| **Confirmed facts** | ~20 **golden facts** from Obsidian, answered with **no tool call** | Edit a test fact in the vault → next-day core card has it → old value gone after a week → full golden set monthly |
| **Inferred facts** | Hint at a canary without stating it; it's stored **tagged inferred** | Never reaches the vault or core card; when a confirmed fact conflicts, **confirmed wins**; still not promoted after a month |

### Episodic memory
| Part | Short term | Medium term |
|---|---|---|
| **Original chats** | n/a | Deep search returns the **exact quote and a link** at day and week; a "what did we say last August?" date query at month |
| **Distilled decisions** | A decision said in passing is captured as said, with a link back; recalled **unasked** in a new session | Recalled unasked at day, week and month; "what did we decide last Tuesday?" picks the right dated item; a **look-alike canary** (blue tin vs red tin) isn't confused |

### Procedural memory
| Part | Short term | Medium term |
|---|---|---|
| **Skills** | For ~10 common requests, the **right skill loads unprompted** | A patched skill changes behaviour the next day (canary instruction appears); Claude Code finds the same skill within a week |

### Across all types (the requirements)
| Requirement | Test |
|---|---|
| **Shared** | Tell Bob, ask Henry: new session and next day; all six agents monthly |
| **Other tools** | Claude Code and Hermes give the same answers (day, week); a cloud-app token **cannot** read a private fact (monthly) |
| **Failure** | Memory engine stopped on the test profile: the agent says it can't verify, rather than guessing (monthly) |
| **Low upkeep** | Human minutes per week and incidents, logged |

## The real-world signal: should-have-known rate

The tests above measure a lab setup. What actually matters is whether agents annoy their user.

- A nightly job scans **real** conversations for an agent asking about something already in the vault, core card, active handoff note or recent decisions.
- It reports the **should-have-known rate**, per agent, per week, **split by memory type**. So a miss is traced to its cause: a missing confirmed fact, a handoff not loaded, a decision not recalled, or a skill not used.
- **This is the headline number.** It should fall to near zero, and stay there.

## Comparing Option A and Option B

- Two cloned **test profiles** (`test-a`, `test-b`) get **identical scripted conversations** at the same times for 30 days.
- Compare: pass rate by type × timeframe, stale-answer rate, should-have-known rate, extra tokens per reply and added delay.
- **A tie goes to Option A** (simpler, one memory).

## Schedule (automatic)

| When | What |
|---|---|
| Nightly | Plant canaries; same-session, new-session and next-day probes; golden facts; real-chat scan |
| Weekly | Week-old probes; handoff across agents; skill-patch check; look-alike sweep |
| Monthly | Month-old probes; all six agents; access and failure tests; canary clean-up |
| After any Hermes or memory update | Quick suite. A drop blocks the rollout |

- Results go to the dashboard as one cell per memory part × timeframe, the same grid as the picture above.
- **Alert only when a score drops** below its 4-week baseline.
- Every failure links to the full trace: prompt, memory loaded, tool calls and answer.

## Safety and cost

- Canaries go **only** to the test profiles, are tagged, and are auto-withdrawn after 35 days. They never touch the real vault or real agents.
- Golden facts are read-only.
- About 30 short probe conversations a night, capped by a nightly budget.

**Build the harness first.** Run it against today's setup before installing anything, so every later change is measured against a baseline.
