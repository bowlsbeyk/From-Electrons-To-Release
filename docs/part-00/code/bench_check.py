"""Chapter 0 lab, step 1: set up your bench and prove it works.

Run this once. It checks that Python and Git are installed and recent
enough for the book, then creates your study folder with the three files
you will keep for the whole book: a journal, a glossary, and a cards file.

    python3 bench_check.py            # creates ~/electrons-study/
    python3 bench_check.py ~/study    # or put it somewhere else

It only uses Python's standard library, so there is nothing to install.
"""
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path

MIN_PYTHON = (3, 12)

JOURNAL_HEADER = """# Learning journal — From Electrons to Releases

One entry per study session. Write it before you close the book.
Four prompts, two or three sentences each. Honest beats tidy.

"""

JOURNAL_ENTRY = """## {today} — Chapter 0

**What I did:**
**What was hard, and where exactly I got stuck:**
**The sentence or picture that made it click (or: it hasn't yet):**
**What I predict will be hard next chapter:**

"""

GLOSSARY_HEADER = """# My glossary

One line per term, in MY words, not the book's. If I can't write it
without looking, it isn't mine yet. Format:

**term** — what it means, in a sentence I'd say out loud. (Ch. N)

"""

# The lines starting with # are Anki's file headers (Anki 2.1.54 and later
# read them): tab-separated, plain text, and column 3 holds the tags.
CARDS_HEADER = """#separator:tab
#html:false
#tags column:3
#columns:Front\tBack\tTags
"""


def check_python() -> bool:
    v = sys.version_info
    ok = (v.major, v.minor) >= MIN_PYTHON
    mark = "ok " if ok else "OLD"
    print(f"[{mark}] Python {v.major}.{v.minor}.{v.micro}  (book expects {MIN_PYTHON[0]}.{MIN_PYTHON[1]} or newer)")
    return ok


def check_git() -> bool:
    exe = shutil.which("git")
    if not exe:
        print("[MISSING] git  -> install it from https://git-scm.com/downloads")
        return False
    out = subprocess.run([exe, "--version"], capture_output=True, text=True).stdout.strip()
    print(f"[ok ] {out}")
    return True


def make_study_folder(root: Path) -> None:
    root.mkdir(parents=True, exist_ok=True)
    today = date.today().isoformat()

    journal = root / "journal.md"
    if not journal.exists():
        journal.write_text(JOURNAL_HEADER + JOURNAL_ENTRY.format(today=today))
        print(f"[new] {journal}")
    else:
        print(f"[kept] {journal} (already there, not touched)")

    glossary = root / "glossary.md"
    if not glossary.exists():
        glossary.write_text(GLOSSARY_HEADER)
        print(f"[new] {glossary}")
    else:
        print(f"[kept] {glossary}")

    cards = root / "cards.tsv"
    if not cards.exists():
        cards.write_text(CARDS_HEADER)
        print(f"[new] {cards}  (tab-separated; Anki can import this file directly)")
    else:
        print(f"[kept] {cards}")


def main() -> int:
    root = Path(sys.argv[1]).expanduser() if len(sys.argv) > 1 else Path.home() / "electrons-study"
    print("Bench check\n-----------")
    py_ok = check_python()
    git_ok = check_git()
    print()
    make_study_folder(root)
    print()
    if py_ok and git_ok:
        print("Bench is ready. Open journal.md and fill in today's entry before you do anything else.")
        return 0
    print("Fix the lines marked OLD or MISSING, then run this again.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
