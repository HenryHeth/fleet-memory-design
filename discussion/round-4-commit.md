# Round 4 · Commit to a pilot

**Purpose:** turn the agreed decisions into a plan that can start the next day.

---

### D4.1 · Pilot scope

**Proposal:** two real agents (Bob, engineering; Henry, chief of staff), Claude Code, and the two test profiles. The other four agents join only after the pilot passes. No bulk import of sensitive data.

### D4.2 · Build order and gates

**Proposal:** each step must pass its check before the next one starts.

| Step | Build | Gate to pass |
|---|---|---|
| 0 | Test harness; measure today's setup | Baseline recorded for every test |
| 1 | Vault + core card | Golden facts ≥ 95% with no tool call |
| 2 | Handoff notes | Another agent resumes correctly ≥ 90% |
| 3 | Engine, keyword-only, private | Deep search cites the exact chat; Claude Code gives the same answers |
| 4 | Automatic recall: Option A on `test-a`, Option B on `test-b` | 30 days of results |
| 5 | Choose A or B; roll out to Bob and Henry | D1.3 targets met |

**Note:** step 1 alone should fix the most visible problem (agents not knowing basic facts). Measure it before adding anything more.

### D4.3 · Owners

| Area | Proposed owner |
|---|---|
| Harness, engine and plugins | Bob (engineering) |
| Vault content and weekly fact review | Paul, with Henry preparing the list |
| Handoff discipline across agents | Henry |
| Peer review of results at day 30 | The visiting team |

### D4.4 · Go / no-go

**Proposal:**
- **Go** if the D1.3 targets are met on the chosen option.
- **Fix and retest for 14 days** if one or two targets miss.
- **Swap the engine** (to Hindsight) if automatic recall misses badly on both options.
- The visiting team gets the day-30 results and a short read-out.

---

**Reply format:** `D4.x ACCEPT | AMEND: … | REJECT: …`
