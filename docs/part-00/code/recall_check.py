"""Chapter 0 lab, step 4: the recall check.

Close the chapter. Run this. Type everything you can remember from the
chapter, one idea per line, for as long as you can. When you run dry,
type a line containing only  done  and press Enter.

The script timestamps what you wrote, counts the lines, and appends it
to your journal so you can compare it with the chapter afterwards. It
never shows you the chapter; that is the point.

    python3 recall_check.py                     # journal at ~/electrons-study/journal.md
    python3 recall_check.py ~/study/journal.md  # or name the journal file
"""
import sys
from datetime import datetime
from pathlib import Path


def collect() -> list[str]:
    print("Book closed? Good. Type what you remember, one idea per line.")
    print("Type  done  on its own line when you run dry.\n")
    lines: list[str] = []
    while True:
        try:
            line = input("> ").strip()
        except EOFError:
            break
        if line.lower() == "done":
            break
        if line:
            lines.append(line)
    return lines


def main() -> int:
    journal = Path(sys.argv[1]).expanduser() if len(sys.argv) > 1 else Path.home() / "electrons-study" / "journal.md"
    if not journal.exists():
        print(f"No journal at {journal}. Run bench_check.py first, or pass the path to your journal.")
        return 1

    lines = collect()
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    block = [f"\n### Recall check — {stamp}", "", f"{len(lines)} ideas recalled with the book closed:", ""]
    block += [f"- {ln}" for ln in lines] or ["- (nothing yet; that is useful information too)"]
    block += ["", "Now reopen the chapter and add below: what you missed, and what you got wrong.", ""]
    with journal.open("a") as f:
        f.write("\n".join(block))

    print(f"\nSaved {len(lines)} lines to {journal}.")
    print("Open the chapter now and write, under the entry, what you missed and what you had wrong.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
