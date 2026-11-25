"""Status Report Comedy Sprint builder: gate-check entry.txt, export, print receipt."""
import json
import os
import shutil
from pathlib import Path

LIMIT = 200
SOURCE = Path(__file__).with_name("entry.txt")
STAMP = "sta4-status-comedy-r4"


def within_gate(text):
    body = text.strip()
    return 1 <= len(body) <= LIMIT


def ship():
    raw = SOURCE.read_text(encoding="utf-8")
    if not within_gate(raw):
        raise SystemExit("entry outside gate range")
    target = os.environ.get("MAKEFUN_OUTPUT_DIR") or "out"
    dest = Path(target) / "entry.txt"
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, dest)
    receipt = {"verdict": "ok", "stamp": STAMP, "chars": len(raw.strip())}
    receipt["gate_limit"] = LIMIT
    print(json.dumps(receipt))


if __name__ == "__main__":
    ship()
