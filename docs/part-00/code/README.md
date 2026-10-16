# Chapter 0 — code

Three small Python scripts. They use only the standard library; nothing to install. Python 3.12 or newer.

| File | What it does | How to run |
| --- | --- | --- |
| `bench_check.py` | Checks that Python and Git are installed and recent enough, then creates your study folder (`~/electrons-study/` by default) with `journal.md`, `glossary.md`, and `cards.tsv`. Safe to run again; it never overwrites files that exist. | `python3 bench_check.py` or `python3 bench_check.py path/to/folder` |
| `recall_check.py` | The lab's recall check. With the chapter closed, you type what you remember, one idea per line, then `done`. It appends the list, a timestamp, and a count to your journal. | `python3 recall_check.py` or `python3 recall_check.py path/to/journal.md` |
| `master_diagram.py` | Generates the book's master diagram for any chapter number. Chapter 0 produces the unlit frame; each later chapter re-runs it with its own number and gets exactly one more box lit. You don't need this for the lab; it's here so you can see how the picture is made and reproduce it. | `python3 master_diagram.py 0 master-ch-00.svg` |

On Windows the command may be `python` or `py` instead of `python3`.
