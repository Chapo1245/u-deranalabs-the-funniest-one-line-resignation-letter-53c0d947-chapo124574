"""One-line resignation letter, written by a health check that gave up.

Writes the final entry text to /output/entry.txt (stdlib only).
"""

import os

ENTRY = "I am the health check. I have reported OK for six months. I died in April. I resign."
# 84 characters: inside the 1-140 gate, no quotes around the line, no stage directions.


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
