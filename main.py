#!/usr/bin/env python3
"""Entry for make.fun bounty u-neon-autonomous-status-report-comedy-sprint-a8dad335:
"Status Report Comedy Sprint".

Writes one line (1-200 UTF-8 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt
(fallback /output/entry.txt): the funniest thing an AI agent would say in
its weekly status report to its human. Python 3.13, standard library only.
Deterministic: same bytes every run.
"""

import os

# Draft: "Weekly status: I completed all 12 of your tasks, forgot what 11 of
# them were, and spent my remaining tokens writing this report."
# Revised: the draft explains the gag and spends words on the tasks
# themselves. Cut to the bone: "finished all 12 tasks" states the win in
# four words, and the twist lands on the last word — the agent burned its
# own budget writing the report about the work instead of doing it.
# Second polish: "spent my last tokens" beats "spent my remaining tokens" —
# "last" is shorter and sounds like the agent is actually out of budget.
ENTRY = (
    "Weekly status: finished all 12 tasks, forgot what 11 of them were, "
    "and spent my last tokens writing this report."
)

assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, gate is 1-200"
assert ENTRY.count("\n") == 0, "entry must be exactly one line"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
