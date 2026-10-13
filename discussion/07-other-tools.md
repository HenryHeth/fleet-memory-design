# Across all types · Same memory in every tool

**Memory type:** All

## What we're seeing

Memory should work from Claude Code and Codex now, and from Sesame, Grok bots, Muse and Dot where possible. Connecting a tool lets it **read** memory; it doesn't send its conversations back.

## Our current position

- One G-Brain front door.
- Tailscale (private) for our tools; Cloudflare Tunnel + Access (login, read-only, non-sensitive) for cloud apps.
- Claude Code and Codex logs are imported nightly.

## Questions for you

1. Have you connected Sesame, Muse, Grok or Dot to your own memory? Did the login work?
2. How do you get conversations from outside tools back into memory?
3. How do you limit what a cloud app can see?

## How we'll test it

Cross-tool tests: Claude Code = Hermes answers; a cloud-app token can't read a private fact.
