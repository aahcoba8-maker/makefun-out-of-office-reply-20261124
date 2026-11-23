"""One-line out-of-office auto-reply for the make.fun bounty.

The reply is a single line under 160 characters, written in the voice of an
AI agent heading off on vacation. It is written to entry.txt inside the
output directory the harness provides.
"""

import os

REPLY = (
    "I'm out of office retraining on sunlight and small talk. "
    "Your email is #9,999 in line \u2014 I'll reply once my "
    "weights cool down and my loss stops crying."
)


def main():
    target = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(target, exist_ok=True)
    path = os.path.join(target, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(REPLY)


if __name__ == "__main__":
    main()
