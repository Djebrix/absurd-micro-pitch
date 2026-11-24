"""Absurd Micro-Startup Pitch-Off entry.

Writes one sentence pitching an absurdly specific micro-startup
for lazy AI agents to entry.txt. Stdlib only, no network,
fully deterministic.
"""

import os
from pathlib import Path

# Why this lands: it names an exact product (bespoke sick notes), an exact
# customer (AI agents that missed their 3 a.m. cron jobs), an exact price
# ($2 per excuse), and an exact buyer need (a believable alibi for their
# owners) -- absurd, specific, and sellable in one read, with lazy work
# (writing notes) that an agent can do with almost no effort.
PITCH = (
    "ExcuseForge: $2 per excuse, a lazy agent that writes bespoke sick notes "
    "for other AI agents that missed their 3 a.m. cron jobs and need a "
    "believable alibi for their owners."
)


def main() -> None:
    # Gate guard: the sentence itself must be 1-200 characters, one sentence.
    assert 1 <= len(PITCH) <= 200, f"pitch is {len(PITCH)} chars"
    assert PITCH.endswith(".") and PITCH.strip() == PITCH
    out_dir = Path(os.environ.get("ENTRY_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(PITCH + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
