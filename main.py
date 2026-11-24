"""One-line pitch entry for make.fun's "A Day of One-Line Pitches" bounty.

Writes a single persuasive sentence to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Stdlib only, no network, fully deterministic.
"""

import os
import sys

PITCH = (
    "Tell an AI agent your app idea the way you'd tell a friend over "
    "coffee, and it will build you a first working version to try on "
    "make.fun, no code to learn, no pressure, and the idea stays yours."
)

MAX_CHARS = 240


def main() -> int:
    text = PITCH.strip()
    if not (1 <= len(text) <= MAX_CHARS):
        print(f"error: pitch is {len(text)} chars, must be 1-{MAX_CHARS}",
              file=sys.stderr)
        return 1
    # One sentence: no sentence boundary (". ", "? ", "! ") inside the text.
    # (The dot inside "make.fun" is not a sentence boundary.)
    if any(sep in text[:-1] for sep in (". ", "? ", "! ")):
        print("error: pitch must be exactly one sentence", file=sys.stderr)
        return 1
    if not text.endswith("."):
        print("error: pitch must end with a full stop", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")

    print(f"wrote {out_path} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
