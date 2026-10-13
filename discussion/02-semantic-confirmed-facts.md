# Semantic memory · Things agents should just know

**Memory type:** Semantic

## What we're seeing

The biggest confidence-killer is an agent asking something it should obviously know (an address, a family member, a standing rule). Today each agent has a ~2,200-character note, not shared.

## Our current position

- Confirmed facts live in an **Obsidian vault** (git) as the single source of truth.
- A nightly **core card** is loaded into every conversation. No search, so it can't be missed.
- G-Brain indexes the vault for everything that doesn't fit on the card.

## Questions for you

1. What makes your agents "just know" things: a static card, pre-reply injection, or something else?
2. How big can the always-loaded card get before it costs too much or crowds the context?
3. Is Obsidian the right home, or is a database or the memory engine itself better in practice?

## How we'll test it

Golden-fact tests: answered with **no tool call**; an edit to the vault reaches the card next day, and the old value is gone in a week.
