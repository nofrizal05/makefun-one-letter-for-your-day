"""One Letter for Your Day — make.fun entry.

Writes exactly one letter to /output/entry.txt.

The letter is "Z", standing for "zero sleep": a day with zero sleep is
vivid (a sharp picture), funny (everyone knows that day), and true (an
honest report, not a performance). Z is the most distinctive initial
of the examples the competition itself gives, and "zero sleep" is the
most specific day-word among them — sharper than A for "amazing",
softer rivals like E for "exhausted" or S for "sleepless" name a mood,
while Z names the cause.
"""

import os

LETTER = "Z"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
