# 04 · Network access for outside tools

## Who can do what

| Tool | Read memory | Feed conversations back | Notes |
|---|---|---|---|
| Hermes agents | Yes | Yes (memory-provider slot) | Pre-reply recall possible |
| Claude Code, Codex | Yes (MCP) | Yes, via nightly import of local logs | G-Brain documents pre-turn hooks |
| Self-built Grok bot (xAI API) | Yes (remote MCP documented) | Only if we build it | |
| Sesame | Read-only at best | No, each assistant keeps separate memory | Login flow untested |
| Muse, consumer Grok app, Dot | Unconfirmed | Unconfirmed | G-Brain claims Grok Bot / Muse guides; unverified by us |

**Key point:** connecting a tool over MCP lets it *read* memory. It doesn't send its conversations back. That's true of every product reviewed.

## Paths

- **Tailscale Serve (private):** only devices on our tailnet. Use for our agents, coding tools and phones. Nothing public.
- **Tailscale Funnel (public):** public, but **adds no login**. Not suitable for personal facts.
- **Cloudflare Tunnel + Access (public, with login):** public address without opening router ports. Access puts a login in front and supports the MCP OAuth flow, so cloud apps get a normal "sign in to connect" step.

## Decision

- Tailscale Serve for our own tools.
- Cloudflare Tunnel + Access for cloud apps, exposing **read-only, non-sensitive** memory by default.
- Sensitive facts stay on the private path.
- **Unverified:** whether Sesame completes the Cloudflare Access login. It counts as working only after a real connection test.
