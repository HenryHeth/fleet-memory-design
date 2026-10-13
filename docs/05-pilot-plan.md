# 05 · Pilot plan (draft)

**Scope:** two Hermes agents (engineering + chief of staff) and Claude Code. No blanket import of sensitive data.

## Steps

1. **Sources of truth:** create the Obsidian fact register (confirmed facts only) in git; write the nightly core-card build.
2. **Level 1:** load the core card into both pilot agents. Run the "should already know" test. This alone should fix the basic-facts problem; measure it before adding anything else.
3. **G-Brain, private:** install keyword-only (no AI keys), index the vault, chats and skills, and expose it over Tailscale Serve. Connect both agents and Claude Code.
4. **Level 2, Option A:** wire G-Brain into the Hermes pre-reply slot (or write a small plugin). Run the full test set.
5. **Level 2, Option B:** add Mnemosyne on the same agents. Run the same test set.
6. **Decide** using the rules in [02-options-to-vet.md](02-options-to-vet.md).
7. **Expand:** the remaining four agents, then local embeddings, then Cloudflare + Access with read-only scope, ending with a real Sesame connection test.

## Test set (frozen before step 2)

Full automated method: [07-test-methodology.md](07-test-methodology.md). Build the test harness **before** installing anything, so step 2 has a baseline. Minimum set:

- 20 "should already know" questions (fresh conversation, no hint to look things up)
- Changed fact: the old value must disappear
- Planted false claim: it must not be adopted
- Decision provenance: "why did we decide X?" must cite the original conversation
- Permission boundary: a cloud-app token can't read private facts
- Cross-tool: Hermes and Claude Code give the same answers
- Failure behaviour: if memory is down, the agent says it can't verify rather than guessing

## Ongoing upkeep target

- Weekly: 5-minute review of proposed facts
- Nightly / weekly / monthly automated suite; alert only on a drop
- Headline number: the **should-have-known rate** from real conversations
- Skills are patched after real wins and mistakes
