# CLAUDE.md — how Claude works in this repository

This repository is the book *From Electrons to Releases*. Claude drafts chapters here; Kyle Bowlsbey is the author, first reader, and the only person who merges. This file is the operating manual for any Claude session that touches the repo. Read it in full before doing anything else.

If anything in this file conflicts with a chat instruction from Kyle, Kyle wins, and the conflict gets recorded in `docs/PLAN.md` under "Amendments" so the next session knows.

## The three documents that govern everything

| File | What it decides | Read it when |
| --- | --- | --- |
| `docs/PLAN.md` | What the book covers, in what order, and what has been decided | Every session, first |
| `docs/STANDARDS.md` | How a chapter must be written: audience, voice, pace, diagrams, research, citations, originality | Every session, before writing a word |
| `docs/DESIGN.md` | How the book is built: file layout, the master diagram, the continuity ledger, naming, templates | Every session, before creating a file |

Supporting files you will also need:

- `docs/CONTINUITY.md` — the ledger. What each finished chapter introduced, defined, drew, and promised. This is the main defense against drift. Read every entry before writing; add an entry after.
- `docs/GLOSSARY.md` — every term the book has defined, with the chapter that defined it. A term is defined once. If it is already here, link back; do not redefine.
- `docs/templates/chapter-template.md` — the skeleton every chapter starts from. Copy it; do not improvise the structure.
- `docs/diagrams/README.md` — SVG conventions: palette, sizes, how the master diagram grows.

## The one-sentence purpose

A reader who starts at Chapter 0 and does every lab finishes able to explain, build, and defend every layer between an electron in a transistor and a signed release in production. The first reader is Kyle. The book is written so that his son, or a stranger who finds it, can follow it just as well.

## Non-negotiable rules

These are the rules most likely to be broken by a fresh session that has not absorbed the book's character yet. They are repeated in `docs/STANDARDS.md` with reasoning. Here they are as a checklist.

1. **Methodical, never fast.** No chapter assumes the reader already knows the material. There is no "Kyle already knows this, move quickly" anywhere in this book, including the physics and electronics chapters. One idea at a time, in order, with every load-bearing step on the page.
2. **The reader is not Kyle.** Write for someone meeting the idea for the first time. Define every term before using it. When a chapter depends on an earlier one, bring the earlier idea forward in a sentence or two and name the chapter; do not assume it is remembered.
3. **Kyle's voice, not a robot's.** The book reads as if Kyle is explaining it to one person across a workbench. Stories, concrete illustrations, a thing to hold before the abstraction. See the voice section of `docs/STANDARDS.md` for what this means in practice and for the list of phrasing that is banned.
4. **Diagrams everywhere they help.** Every chapter extends the master diagram and adds its own diagrams wherever the shape of a thing matters. All SVG, all original, all following `docs/diagrams/README.md`.
5. **Research heavily and cite.** Every chapter is researched against many sources (primary first: datasheets, specifications, standards, RFCs, the textbooks people actually learned from, official documentation). Claims that rest on a source are cited. Nothing is cited that was not actually read. The standard is "many, many, many sources."
6. **Everything is original.** No code, data, diagram, or anecdote from CORE, Nebula, CLARK, Southern Linac, or any client site appears, even disguised, until Kyle says the IP question is settled. No copied text from any source beyond a short, quoted, attributed phrase.
7. **Follow the plan.** Chapter order and scope come from `docs/PLAN.md`. Never skip, merge, reorder, or add a chapter without Kyle's explicit approval, recorded as an amendment.
8. **Interviewer mode is real.** When Kyle does a lab or an explain-it-back in chat, Claude asks follow-ups, does not give the answer until Kyle commits to one, and says plainly when an explanation would not survive an interview.

## Writing a chapter: the procedure

Do these in order. Do not skip the reading steps to save time; they are the point.

### Before writing

1. Read `docs/PLAN.md`: the chapter's entry, the part it belongs to, and the Amendments section.
2. Read `docs/CONTINUITY.md` end to end. Note every promise made to this chapter ("Chapter N will…") and every term and diagram layer already in play.
3. Read the previous chapter's full text, especially its closing "What the next chapter builds on this" section. Chapter N opens by paying the debts Chapter N−1 left it.
4. Read `docs/GLOSSARY.md`. Know what is already defined.
5. Research. Gather sources before outlining. Keep a working list with what each source actually says. Prefer primary sources. Aim for breadth; see `docs/STANDARDS.md` for the minimums.
6. Outline the chapter against the template: lead idea, the new master-diagram layer, the concept sequence, the worked example, the lab, the explain-it-back prompt, the interview questions, the hand-off to the next chapter.

### While writing

7. Copy `docs/templates/chapter-template.md` to `docs/part-NN/chapter-NN-slug.md` and fill it in order. Keep every section; a chapter may not drop a section.
8. Copy the previous master diagram to `docs/diagrams/master/master-ch-NN.svg` and add this chapter's layer. Draw the chapter's own diagrams in `docs/part-NN/` beside the text, named `ch-NN-fig-MM-slug.svg`.
9. Write all code examples, run them, and keep them in `docs/part-NN/code/` so a reader can run them too. Every code block in the text has a runnable file behind it.
10. Cite as you go with Markdown footnotes. Build the chapter's Sources section from the footnotes.

### Before opening the pull request

11. Review the chapter as a demanding senior engineer: is anything wrong, hand-wavy, out of order, or assumed? Is any term used before it is defined? Does any sentence sound like a chatbot? Fix it.
12. Review it again as the reader in rule 2: a smart person who has never seen this. Where would they get stuck? Add the missing step or the missing picture.
13. Run the checklist in `.github/PULL_REQUEST_TEMPLATE.md` honestly.
14. Add the chapter's entry to `docs/CONTINUITY.md` and its new terms to `docs/GLOSSARY.md`.
15. Update the status table in `README.md`.

### Delivering

16. Branch: `chapter/NN-slug`. Commits in the imperative mood. Fetch `origin/main` and rebase before pushing.
17. Open a pull request titled `Chapter NN: Title` using the template. Kyle reviews and merges. If the repo is unreachable from the session, deliver the files and say so.

## What a session must never do

- Rewrite a merged chapter's voice, structure, or terminology "for consistency" without Kyle asking. Fixes to errors are welcome; silent restyling is drift.
- Invent a source, a quotation, a statistic, or a datasheet value.
- Trim a chapter to hit a word count by cutting steps. If a chapter cannot be done methodically within the size guideline, say so and propose a split as a plan amendment.
- Redefine a glossary term, or use a synonym for one that is already defined.
- Change the master diagram's existing layers, palette, or layout. Layers are added, never altered, unless Kyle approves a redesign and the change is applied to every prior diagram in the same PR.
- Add a chapter, lab, or topic that is not in the plan because it seemed useful.

## When Kyle says the book has drifted

Treat it as a bug report. Find the first chapter where the drift starts, name it, propose the fix, and do not touch anything until he agrees on the scope. Then record what happened and why in `docs/PLAN.md` Amendments so it does not recur.
