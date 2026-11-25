import json
import os

STATUS_CAP = 200


def report():
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), "r", encoding="utf-8") as handle:
        raw = handle.read()
    clean = raw.translate({13: None})
    line = next((part.strip() for part in clean.split("\n") if part.strip()), "")
    if not 1 <= len(line) <= STATUS_CAP:
        raise RuntimeError("status line length %d fails the 1..%d gate" % (len(line), STATUS_CAP))
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR") or "output"
    os.makedirs(folder, exist_ok=True)
    destination = os.path.join(folder, "entry.txt")
    with open(destination, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    with open(destination, "r", encoding="utf-8", newline="") as handle:
        stored = handle.read()
    if stored != line:
        raise RuntimeError("readback mismatch: %r != %r" % (stored, line))
    print(json.dumps({"result": "delivered", "size": len(line), "destination": destination}))


if __name__ == "__main__":
    report()
