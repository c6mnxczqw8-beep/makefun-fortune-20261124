#!/usr/bin/env python3
"""Entry program for "Fortune Cookie Wisdom for Developers" (program/v1).

Writes one original fortune-cookie line for a software developer, at
most 120 characters, to the output directory (MAKEFUN_OUTPUT_DIR,
default /output) as entry.txt, with no trailing newline.

Candidate fortunes drafted for this entry (first pass):
  1. A bug you meet tonight was introduced by you, in a past sprint.
  2. The code you refuse to delete will outlive the feature it was
     written for, and then you.
  3. Tonight you will fix the bug in five minutes -- the same five
     minutes you promised this morning.
  4. A stranger will save your deploy tonight: past you, in a comment
     you have scrolled past a hundred times.
  5. The test you skip today will run tonight in production, before
     an audience.
  6. You will meet the author of the legacy code you curse; the
     mirror is already on your calendar.
  7. The deploy you fear on Friday fears you more; ship it Thursday
     and disappoint it.
  8. An old TODO will come true: not the task, but its age -- it
     turns three this spring.
  9. The bug is not in the last place you look; it is in the place
     you swore you already checked.
 10. Your estimate will be exactly right once, in the only language
     no stakeholder speaks: hindsight.
 11. A green build approaches, but it has read your commit message
     and knows you are lying.
 12. The one-line fix you seek is already written -- in the branch
     you force-pushed over.

Candidate 4 was picked: it opens like a real fortune, turns on the
quiet twist that the "stranger" is past you, and is true about every
developer who has ever scrolled past their own comment.

Second pass: "Tonight" moved to the front, where a fortune cookie
puts its prophecy, and the duplicated "tonight" after "deploy" cut,
so the line lands in one balanced breath -- a stranger is promised,
then revealed to be past you, in the comment you keep ignoring.
"""

import os
import sys

LINE = (
    "Tonight a stranger will save your deploy: past you, in a comment "
    "you have scrolled past a hundred times."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.txt")
    with open(dst, "w", encoding="utf-8") as fh:
        fh.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
