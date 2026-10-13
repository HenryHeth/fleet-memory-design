# Sources

Grouped by type. Confidence: **vendor** = the product's own claims; **independent** = third-party testing; **field** = individual user reports.

## Frameworks and peer-reviewed research
- CoALA, Cognitive Architectures for Language Agents (memory taxonomy): https://arxiv.org/abs/2309.02427
- LongMemEval (ICLR 2025): indexing / retrieval / reading; fact-augmented key expansion: https://arxiv.org/abs/2410.10813 · code: https://github.com/xiaowu0162/longmemeval
- Hindsight paper: https://arxiv.org/html/2512.12818v1
- Related benchmark discussion: https://arxiv.org/html/2510.27246v1
- IBM, "AI agent memory" explainer: https://www.ibm.com/think/topics/ai-agent-memory · video: https://www.youtube.com/watch?v=BacJ6sEhqMo

## Independent testing
- Hermes memory-conflict comparison (7 providers, same setup): https://engturtle.github.io/hermes-memconflict/report/

## Vendor documentation
- Hermes memory: https://hermes-agent.nousresearch.com/docs/user-guide/features/memory
- Hermes memory providers: https://hermes-agent.nousresearch.com/docs/user-guide/features/memory-providers
- Hermes sessions / search: https://hermes-agent.nousresearch.com/docs/user-guide/sessions
- Hermes MCP: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- G-Brain: https://github.com/garrytan/gbrain
- Hindsight: https://hindsight.vectorize.io/ · MCP: https://hindsight.vectorize.io/developer/mcp-server · models: https://hindsight.vectorize.io/developer/models · observations: https://hindsight.vectorize.io/developer/observations
- Honcho architecture: https://honcho.dev/docs/v3/documentation/core-concepts/architecture · evals: https://honcho.dev/evals/
- Mem0 OSS v3 migration: https://docs.mem0.ai/migration/oss-v2-to-v3 · MCP: https://docs.mem0.ai/platform/mem0-mcp
- Supermemory memory review: https://supermemory.ai/docs/recall/memory-review · graph memory: https://supermemory.ai/docs/concepts/graph-memory · self-hosting: https://supermemory.ai/docs/self-hosting/overview
- Mnemosyne repo: https://github.com/mnemosyne-oss/mnemosyne · architecture: https://docs.mnemosyne.site/architecture/beam-overview · veracity labels: https://docs.mnemosyne.site/architecture/veracity-signal
  - Note: `mnemosyne-oss/mnemosyne` is an independent MIT project. `Mnemosyne-OS/MnemoHermes` is a different project. Check repo names before following install instructions.
- Obsidian MCP server example: https://github.com/eugeniughelbur/obsidian-second-brain/tree/main/integrations/obsidian-mcp-server

## Network and access
- Tailscale Funnel: https://tailscale.com/docs/features/tailscale-funnel
- Cloudflare, secure MCP servers: https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/secure-mcp-servers/
- Cloudflare Access MCP OAuth changelog: https://developers.cloudflare.com/changelog/post/2025-08-26-access-mcp-oauth/
- xAI remote MCP: https://docs.x.ai/developers/tools/remote-mcp
- Sesame getting started: https://www.sesame.com/journal/getting-started

## Field reports (Reddit)
- r/hermesagent, Obsidian + G-Brain shared by four agents: https://www.reddit.com/r/hermesagent/comments/1u45ywh
- r/hermesagent, Hindsight auto-retain pollution: https://www.reddit.com/r/hermesagent/comments/1txfg3j
- r/hermesagent, Honcho self-host issues: https://www.reddit.com/r/hermesagent/comments/1t766jo
- r/hermesagent, Mnemosyne experience: https://www.reddit.com/r/hermesagent/comments/1tsonau
- r/hermesagent, multi-layer trial: https://www.reddit.com/r/hermesagent/comments/1v47wa9/comment/oz945iy
- r/AI_Agents: https://www.reddit.com/r/AI_Agents/comments/1szwjat
- r/LangChain: https://www.reddit.com/r/LangChain/comments/1o080oz
