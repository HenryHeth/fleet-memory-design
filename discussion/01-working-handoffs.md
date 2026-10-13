# Working memory · Picking up where we left off

**Memory type:** Working

## What we're seeing

A new session, or a different agent, should resume a task without the user re-explaining. Today, context dies with the session.

## Our current position

- The handoff note is an **owned artifact**: the Toodledo task note, owned by the agent on the task.
- It's loaded at session start when the task is active, and indexed by G-Brain for other tools.
- Option B adds Mnemosyne's short-term store and scratchpad on each agent.

## Questions for you

1. What does your team use as the handoff between sessions or agents: a note, a task system, an engine's memory?
2. Who writes it: the agent at the end of a session, a hook, or a summariser? How do you keep it short and current?
3. Does per-agent short-term memory (like Mnemosyne) earn its keep, or does it just add something that can disagree?

## How we'll test it

Handoff tests in [04](../docs/04-testing-by-type.md#working-memory): new session resumes; another agent resumes next day.
