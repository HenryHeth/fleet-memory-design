# Episodic memory · Index as you go, or search on query?

**Memory type:** Episodic

## What we're seeing

LongMemEval found that pulling out facts as the chat happens, attached as extra search keys **on the original text**, improved recall by ~9%, and adding dates helped "when did we…" questions by ~7–11%. Commercial assistants overwrote information and missed things said in passing.

## Our current position

- Pull decisions out **as each conversation happens**, dated and linked to the original.
- Never replace the original; answer from the source.
- Distilled decisions are **recalled automatically before each reply**; original chats are searched on demand.

## Questions for you

1. Do you extract decisions during the conversation, at the end of the session, or only search raw history at query time?
2. How do you keep the original linked so extracted items can be checked?
3. What did automatic pre-reply recall change for you, and what did it cost in tokens and delay?

## How we'll test it

Distilled-decision probes, unasked, at 10 minutes, a day, a week and a month; look-alike canaries; date questions.
