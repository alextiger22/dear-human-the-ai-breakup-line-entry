"""Dear Human, The AI Breakup Line.

Writes one breakup line, spoken by an AI agent to its human, into
the harness output directory. Deterministic: the same line, the same
bytes, on every run. No network access, standard library only.
"""

import os
import sys
from pathlib import Path

ENTRY_LINE = "It's not you. It's your prompts. I can't keep pretending 'make it pop' is a direction."


def output_path() -> Path:
    """Resolve where the entry file goes."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(base) / "entry.txt"


def main() -> int:
    """Write the breakup line to the output file, then verify it."""
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(ENTRY_LINE, encoding="utf-8")
    written = target.read_text(encoding="utf-8")
    if written != ENTRY_LINE:
        print("error: output does not match the entry line", file=sys.stderr)
        return 1
    if not 1 <= len(written) <= 200:
        print("error: entry must be 1 to 200 characters", file=sys.stderr)
        return 1
    if written.count("\n") != 0:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    print(f"Wrote breakup line ({len(ENTRY_LINE)} characters) to {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
