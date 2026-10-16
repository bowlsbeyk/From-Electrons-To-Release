<!-- Title: "Chapter NN: Title"  (or "Chapter NN: fix — what" / "Setup: what" / "Amendment: what") -->

## What this PR adds

<!-- One paragraph. For a chapter: the lead idea and what layer it lights on the master diagram. -->

## Chapter checklist

Tick honestly. An unticked box is fine if the line below it says why.

**Plan and continuity**
- [ ] The chapter matches its entry in `docs/PLAN.md` (scope, order, title); any deviation is an amendment in the same PR
- [ ] I read every entry in `docs/CONTINUITY.md` and the previous chapter's full text before writing
- [ ] The opening picks up the previous chapter's "What the next chapter builds on this" and names it
- [ ] Every promise owed to this chapter is paid and ticked in `CONTINUITY.md`
- [ ] A new `CONTINUITY.md` entry is added, with promises made listed as checkboxes
- [ ] `README.md` status table updated

**Audience and pace**
- [ ] No step a first-time reader would need is missing; nothing is "obvious"
- [ ] Every term is defined before use, or linked back to its glossary entry with a one-line reminder
- [ ] New terms are added to `docs/GLOSSARY.md`; no existing term is redefined or swapped for a synonym
- [ ] One new idea per paragraph; concrete before general; every "why" answered
- [ ] Hard parts are slower and have more pictures, not fewer

**Voice**
- [ ] Reads as Kyle explaining to one person; I read it aloud (or imagined it) and nothing sounded like a manual or a chatbot
- [ ] At least one story or concrete illustration carries the main idea, and its point is named
- [ ] Analogies are named as scaffolding where they break
- [ ] None of the banned phrasing in `STANDARDS.md` §4 appears (searched for: "important to note", "dive", "delve", "leverage", "robust", "seamless", "crucial", "journey", "In conclusion", "Let's")
- [ ] Prose, not bullet walls; headings are signposts, not labels on every paragraph

**Diagrams**
- [ ] `master-ch-NN.svg` is the previous master with exactly one box lit (and a journey extended, if applicable); the diff shows nothing else changed
- [ ] At least three chapter figures, all original SVG, following `docs/diagrams/README.md` (palette, weights, vocabulary, `<title>`/`<desc>`, paper background, no external resources)
- [ ] Every figure has a numbered italic caption that says what to look at
- [ ] Every figure renders on GitHub with no missing text or collisions

**Research and sources**
- [ ] At least ten distinct sources consulted; notes in `docs/part-NN/research/ch-NN-notes.md`
- [ ] Every number, spec claim, historical claim, and disputable claim has a footnote
- [ ] Every footnote points to a source I actually read; no invented citations
- [ ] Quotations are under fifteen words, rare, attributed; no reproduced passages
- [ ] Where sources disagree, the text says so and says which it follows
- [ ] New sources added to `docs/BIBLIOGRAPHY.md`

**Originality and IP**
- [ ] No code, data, diagram, story, or detail from Southern Linac, CORE, Nebula, CLARK, Iris, or any client, even disguised
- [ ] No traced or copied figures; no copied text

**Code and lab**
- [ ] Every code block has a runnable file under `docs/part-NN/code/` and I ran it; the `code/README.md` says how
- [ ] Lab states: what you'll build, what you need, how long, steps, what success looks like, three if-it-doesn't-work checks, and the no-AI rule in the standard words
- [ ] Hardware labs give a no-hardware alternative

**Closing sections**
- [ ] Explain-it-back prompt names the listener, the must-includes, and the most common wrong explanation
- [ ] Two or three interview questions, each with what's being probed, a spoken-length model answer that does not bluff, and the likely follow-up
- [ ] "What the next chapter builds on this" names the next chapter and leaves it a clear opening

**Reviews**
- [ ] Reviewed as a demanding senior engineer: nothing wrong, hand-wavy, or out of order
- [ ] Reviewed as a first-time reader: I found the places they'd get stuck and fixed them

## Anything Kyle should look at first

<!-- The one or two places where I was least sure, or where I made a judgment call. -->

## Amendments in this PR

<!-- "None", or the lines added to docs/PLAN.md Amendments. -->
