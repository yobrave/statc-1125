"""Weekly status comedy, one line.

This script is the delivery desk: it stamps the approved line into the
output folder, reopens the file, and signs off only when the bytes it
finds match the draft management signed. Environment variable
MAKEFUN_OUTPUT_DIR moves the desk; nothing else does.
"""
import json
import os
from pathlib import Path

APPROVED = ("Goal completion: 100%. I redefined the goals on Wednesday "
            "to match what I had already shipped, so the metrics have "
            "never looked better.")
MARK = "statc"
CYCLE = "rr2-1125"


def stamp(base):
    base = Path(base)
    if not base.exists():
        base.mkdir(parents=True)
    slot = base / "entry.txt"
    with open(slot, "w", encoding="utf-8", newline="\n") as pen:
        pen.write(APPROVED)
    with open(slot, encoding="utf-8") as eye:
        echoed = eye.read().strip()
    assert echoed == APPROVED, "echo differs from the approved draft"
    return echoed


def run():
    line = stamp(os.environ.get("MAKEFUN_OUTPUT_DIR") or "output")
    print(json.dumps({"mark": MARK, "cycle": CYCLE, "length": len(line), "ok": True}, sort_keys=True))


run()
