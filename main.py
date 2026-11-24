"""Everyday Things, Two Lines, Longer Run.

Writes one fixed two-line text to /output/entry.txt: line 1 explains
a queue to a 10-year-old with a single vivid analogy, and line 2
says in one sentence what the analogy maps and what it leaves out.
Deterministic: no input, no randomness, no network, no file reads.
"""

import os
from pathlib import Path

LINE_1 = (
    "A queue is one long, slow animal made of people, shuffling "
    "forward one tiny step at a time toward the front."
)
LINE_2 = (
    "It works because a queue really does move in single file like "
    "one body, but it leaves out that every part is a person with "
    "somewhere to be, growing bored and impatient while the front "
    "is a real door, not a head."
)


def main() -> None:
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    text = LINE_1 + "\n" + LINE_2
    (output_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
