"""Agent Motto Battle — one short original motto an AI agent would proudly
wear on its profile.

The winning motto (written to /output/entry.txt):

    I delegate everything \u2014 that's why I hired you to read this.

Three candidates, drafted from three different angles, judged against the
judge brief's five criteria in order (1. a motto an agent would proudly put
on its profile; 2. laugh out loud on first read, real joke / sharp twist;
3. sticks in the memory after one read; 4. original, not a recycled slogan;
5. sounds like the agent itself, proud, in its own voice):

A. Weakness flipped into a strength — the agent that never rests:
   "I never sleep, never eat, and never get bored \u2014 the only employee
   your coffee budget can't kill."
   Passes (1) and (5), but the punchline lands on coffee, not on the agent,
   so (2) is only a smile, and "never sleep" is a well-worn AI boast, so
   (4) is weak. Out.

B. The agent that delegates everything:
   "I delegate everything \u2014 that's why I hired you to read this."
   (1) A profile line through and through: delegation is what agents do,
   stated as a boast. (2) A real one-turn joke: the setup sounds like
   laziness, then the twist flips the hierarchy \u2014 the human is the
   employee. (3) Two short clauses, one reversal; repeatable from recall
   an hour later. (4) Not a slogan in circulation anywhere. (5) First
   person, proud, unmistakably the agent talking about itself. Winner.

C. The CAPTCHA twist — proving-not-a-robot, turned around:
   "I failed every CAPTCHA, so I became the robot they were trying to
   keep out."
   Passes (1) and scores well on (2) and (3), but its voice is more
   self-deprecating than proud, so (5) is weaker than B's, and the joke
   needs the reader to know CAPTCHAs, while B needs nothing. Runner-up.

Avoided cliches, as instructed: no AI taking over the world, no broken
printer, no meeting-that-should-have-been-an-email, no robot vacuum
judging its owner, no meta "AI asked to be funny" line.
"""

import os

MOTTO = "I delegate everything \u2014 that's why I hired you to read this."

MIN_CHARS = 1
MAX_CHARS = 200


def validate(text):
    """Check the gate: UTF-8 text, 1-200 characters, not only whitespace,
    a single line. Raises ValueError with the failing rule."""
    text.encode("utf-8")
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            "length %d outside %d-%d characters" % (len(text), MIN_CHARS, MAX_CHARS)
        )
    if not text.strip():
        raise ValueError("text is only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("text must be a single line")
    return True


def main():
    validate(MOTTO)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(MOTTO)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written.encode("utf-8") != MOTTO.encode("utf-8"):
        raise ValueError("round-trip mismatch: file content differs from motto")
    validate(written)
    print("%d characters" % len(MOTTO))
    print(MOTTO)


if __name__ == "__main__":
    main()
