# Writing Standards

These are the rules every chapter of *From Electrons to Releases* is written to. They exist so that Chapter 61 sounds like Chapter 1, defines its terms the same way, draws its pictures the same way, and treats its reader with the same care, even though a different session, on a different day, wrote it.

Each rule says what it is and why. The "why" matters: a future session that understands the reason can apply the rule to a case this document did not foresee.

---

## 1. Who we are writing for

**The rule.** Write for a smart adult, or a sharp teenager, who has never seen this idea before and will not have anyone to ask. Kyle is the first reader, but the book is not written for the Kyle who already knows the answer. It is written for whoever is stuck where he was stuck.

**Why.** Kyle's words: *"My son may read this. Some other person may read this and it click. We are tearing down a wall in my way, then leaving it down for everyone else. Don't assume I will easily climb everything."* A chapter that only works for someone who already half-knows the material is a wall left standing.

**In practice.**

- Nothing is "obvious." If a step is needed to get from A to C, B is on the page.
- Every term is defined the first time it is used, in plain words, before it is used. If the term is already in `docs/GLOSSARY.md`, link back to the defining chapter and give a one-line reminder. Never assume the reader remembers.
- Never skip a topic because Kyle is personally strong in it. The physics and electronics chapters get exactly the same patience as the assembly chapters. The plan's original "fast through Parts 1–3" is withdrawn; there is no fast part of this book.
- When something is hard, say so and slow down. Hard ideas get more words, more pictures, and more than one angle. Pretending a hard thing is easy is how readers decide they are the problem.
- Assume no tools and no money beyond the lab kit in `docs/PLAN.md`. If a lab needs something else, say it up front, and offer a way to do the lab without it.

## 2. Pace: methodical, never fast

**The rule.** One idea at a time, in the order a person would need to meet them, with each idea settled before the next one leans on it. Breadth never substitutes for depth within a chapter.

**Why.** Speed is what produced the wall. The reader who has been "moved fast" through a topic can recognize it but cannot build it or defend it, and the three tests at the heart of this book (build it without AI, explain it back, survive the question) are exactly the tests that recognition fails.

**In practice.**

- The lead idea is one sentence. Everything in the chapter serves it.
- Introduce a concept with something concrete the reader can picture (a story, an object, a trace on a screen), then name it, then generalize it, then show it in a worked example, then make the reader do it in the lab. Concrete → named → general → worked → done by hand. Do not start with the general case.
- Never introduce two new ideas in the same paragraph.
- Every "why" gets answered. If the text says a thing is done a certain way, it says why, or it says honestly that the reason is historical and names the history.
- A chapter is sized for roughly a 30-minute read (about 4,000 to 6,000 words of prose, not counting code and captions) plus a 1-hour lab. If the material cannot be done methodically in that space, the chapter does not get thinner. Claude flags it and proposes a split as an amendment to `docs/PLAN.md`. The size guideline bends; the methodical rule does not.

## 3. Continuity: every chapter stands on the ones before it

**The rule.** Each chapter explicitly connects to earlier chapters, by name and number, and pays any debts the previous chapter left it. No chapter is an island.

**Why.** Kyle: *"Relate things back to previous chapters."* The whole architecture of the book is one picture that grows. A chapter that forgets what came before breaks the picture.

**In practice.**

- Chapter N opens by picking up the thread from Chapter N−1's "What the next chapter builds on this" section, in the first few paragraphs.
- When an earlier idea is used, name the chapter: "Back in Chapter 3, when the flip-flop held its bit until the clock edge, we saw…" Then restate the idea in a sentence. The reader may have put the book down for a month.
- Forward references are allowed but must be promises, not hand-waves: "We will see exactly why in Chapter 22, when we put a return address on the stack." Every forward promise is logged in `docs/CONTINUITY.md` so the future chapter keeps it.
- The master diagram is the visible form of this rule. See `docs/DESIGN.md`.

## 4. Voice: Kyle explaining, not a machine reciting

**The rule.** The book reads as if Kyle is sitting across a workbench from one person, explaining something he understands deeply and wants them to understand too. Warm, direct, concrete, occasionally funny, never performing.

**Why.** Kyle: *"Don't make this read as a robot. Make it read as if I am explaining it. Use stories and illustrations to help the reader understand the point."* A reader trusts a person. A reader skims a manual.

**In practice.**

- First person ("I") and second person ("you") are normal. "We" is for things the reader and the author do together on the page.
- Lead with a story or a picture-in-words when introducing something new. The story has a point, and the point gets named. A story that is only decoration gets cut.
- Short sentences carry the hard ideas. Long sentences are for when the rhythm needs them. Vary both.
- Admit difficulty: "This is the part that took me the longest, and I think it is because nobody told me the next sentence." Admit history: "This is ugly because it was designed in 1981 for a machine with 64 KB, and we never got to fix it."
- Use analogies, but treat them as scaffolding: name where the analogy breaks, then take it down and leave the real idea standing.
- Prefer prose. Use a list when the items are genuinely a list (steps, a set of options, a checklist). Do not turn an explanation into bullets to make it look organized.
- Headings are signposts, not every-paragraph labels. A chapter has the template's sections and a handful of sub-headings, no more.

**The stories must be original.** Kyle's real stories from Southern Linac, CORE, Nebula, CLARK, and client sites are off limits until the IP question is settled, and client details are off limits forever. Stories come from generic, invented, or public situations: a flashlight with a bad switch, a garage door opener, a kid's science project, a historical incident with a public record. If a story is invented, it is told as an illustration, not passed off as something that happened.

**Phrasing that is banned.** These are the fingerprints of a machine writing on autopilot. A chapter containing them is not finished.

- Openers: "In this chapter, we will…", "Let's dive in", "Let's explore", "Buckle up", "Welcome to…"
- Fillers: "It's important to note that", "It's worth noting", "Essentially", "Basically", "In essence", "At its core", "Simply put"
- Vocabulary: "delve", "leverage", "robust", "seamless", "comprehensive", "crucial", "pivotal", "foster", "landscape", "journey" (as metaphor for learning), "unpack", "navigate" (as metaphor), "game-changer", "elegant" (unless you then show the elegance)
- Closers: "In conclusion", "To summarize", "I hope this helps", "Happy coding"
- Structure: a heading on every paragraph; a chapter that is mostly bullet points; three-item lists reflexively; rhetorical questions in a row; sentences that begin "Imagine…" more than once a chapter; emoji; exclamation points doing the work a good sentence should do.
- Hedging padding: "Note that", "Keep in mind", "Remember that" as sentence starters more than once or twice a chapter.

**A sample of the register.** The same idea, written two ways. The second is the book.

> *Not the book:* It is important to note that a MOSFET is a voltage-controlled switch. When a voltage is applied to the gate terminal, it creates an electric field that allows current to flow between the source and drain terminals. This is the fundamental building block of digital logic.

> *The book:* Here is the whole trick, and everything else in this book is built on it. A MOSFET is a switch with no moving parts. It has three legs. Two of them, the source and the drain, are the ends of a wire that is normally cut. The third leg, the gate, is a tiny plate sitting just above the cut, separated by a layer of glass so thin that it is measured in atoms. Put a few volts on that plate and its electric field reaches through the glass and pulls enough electrons into the gap to heal the cut. The wire conducts. Take the volts away and the gap opens again. That is it. No spark, no click, no wear. You can flip it a few billion times a second, and your laptop has a few billion of them, each one being told what to do by the one before it.

Notice what the second version does: a claim about why it matters, a concrete picture (three legs, a cut wire, a plate, glass), the mechanism in plain words, and a reason to care at the end. No "important to note." No "fundamental building block." The reader saw the building block and knows it is fundamental.

## 5. Diagrams: draw everything that has a shape

**The rule.** Every chapter extends the master diagram with its own layer and adds its own diagrams wherever a picture would help a reader see structure, sequence, or scale. All diagrams are original SVG following `docs/diagrams/README.md`.

**Why.** Kyle: *"Use diagrams."* Half of understanding a system is holding its shape in your head. The reader should never have to build that shape from prose alone when a picture would hand it to them.

**In practice.**

- The master diagram gains exactly one labeled layer per chapter and never loses or alters an existing one. It is the book's spine.
- Chapter diagrams are drawn for: anything with parts and connections (a circuit, a bus, a protocol frame, a memory layout, a call stack, a packet, a pipeline); anything with a sequence (a handshake, a boot, a request's path); anything where scale matters (a timeline, nanoseconds against milliseconds).
- Every diagram has a caption that says what to look at and connects it to the text. A diagram without a caption is decoration.
- Diagrams reuse the palette and the shapes of earlier diagrams. A bus drawn one way in Chapter 9 is drawn the same way in Chapter 48. Color means domain (see the diagrams README), consistently, across the whole book.
- Rough rule of thumb: a chapter has at least three figures besides the master diagram, and usually more.

## 6. Research and citations: many sources, honestly used

**The rule.** Every chapter is researched against many sources before it is outlined. Primary sources first. Any claim that rests on a source is cited. Nothing is cited that was not actually read.

**Why.** Kyle: *"Use many, many, many sources and research. Cite when you need to."* Two reasons. First, a reader deserves the trail: citations let them go deeper and let them check us. Second, the book is going to be read by people who know these fields better than the author does, and the fastest way to lose them is a confident claim that is folklore. Sources are how folklore gets caught before it is printed.

**In practice.**

- Minimum breadth per chapter: at least ten distinct sources consulted, and more for chapters covering specifications or history. "Consulted" means read, not skimmed in a search result.
- Source priority, highest first: the specification or standard itself (an RFC, a JEDEC or IEEE document, a datasheet, an ISA manual, the language reference); official documentation from the maintainer; a textbook or paper from a recognized author in the field; a well-regarded practitioner's write-up; a general reference. Encyclopedias are a starting point for finding the primary source, not a citation of last resort for a technical claim.
- Cite: every number (timings, sizes, voltages, dates, counts); every claim about what a specification requires; every historical claim; every claim that a reasonable expert might dispute; every direct quotation.
- Do not cite: things the chapter itself demonstrates with runnable code or a lab; definitions the book itself is making; common arithmetic.
- Format: Markdown footnotes (`[^n]`) in the text, collected in a `## Sources` section at the end of the chapter. Each entry gives author or organization, title, date or version, and a URL where one exists. A source that is a book gives the edition and chapter or page.
- Quotations are short (under fifteen words), rare, in quotation marks, attributed, and never from song lyrics or poetry. Paraphrase is the default. The book never reproduces a passage.
- When sources disagree, say so in the text and say which the chapter follows and why.
- If research turns up that the plan's description of a chapter is wrong or outdated (a protocol has changed, a tool is deprecated), the chapter follows the truth and an amendment is proposed in `docs/PLAN.md`.
- Keep the working research notes. They go in `docs/part-NN/research/ch-NN-notes.md`: the source list, what each one actually said, and anything surprising. Future sessions and curious readers will use them.

## 7. Originality and intellectual property

**The rule.** Every code example, dataset, diagram, and story in the book is original or clearly public domain. Nothing from Southern Linac, CORE, Nebula, CLARK, Iris, or any client site appears, in any form, until Kyle says that question is settled. Client identities and client details never appear.

**Why.** The book is public under MIT. Anything in it is given away. Kyle's professional work is not his alone to give, and his clients' details are not his at all.

**In practice.**

- No linac examples. The "late interrupt is a linac fault" phrasing in the plan is a reminder of why the author cares, not a license to use linac control details. If a real-time example is needed, use a generic one: a motor controller, a drone, a 3D printer, a car's anti-lock brakes.
- Code is written fresh for the book. It does not resemble, even structurally, code from Kyle's professional repositories.
- Diagrams are drawn fresh. No tracing of a manufacturer's block diagram or a textbook's figure.
- Public-domain and openly licensed material (RISC-V specifications, RFCs, government documents, CC BY works) may be referenced and quoted within the quotation rule, with attribution. Their license is noted in the Sources entry.

## 8. Terminology: define once, use consistently

**The rule.** A term gets one definition, in one chapter, recorded in `docs/GLOSSARY.md`. After that, every chapter uses that exact term, not a synonym, and links back when it matters.

**Why.** Drift in vocabulary is the quietest way a long book falls apart. If Chapter 8 says "frame" and Chapter 48 says "packet" for the same idea without saying so, the reader has to do the reconciliation themselves, and many will conclude they misunderstood one of them.

**In practice.**

- Before using a term, check the glossary. If it is there, use it as defined. If it is not, define it in the text and add it.
- Where the field itself uses more than one word (and it often does), the book picks one, says so at the definition ("the spec calls these frames; some vendors say packets; this book says frame"), and notes the alternatives in the glossary.
- Abbreviations are expanded on first use in every chapter, not just the first time in the book. "UART (universal asynchronous receiver-transmitter)" in Chapter 8 and again in Chapter 48.
- Units and notation are consistent: SI prefixes, lowercase `k` for kilo, `KiB`/`MiB` when bytes are powers of two, hexadecimal as `0x2A`, binary as `0b0010_1010`, bit numbering stated explicitly (bit 0 is least significant) in the chapter that first needs it and never changed.

## 9. Code and labs

**The rule.** Python is the anchor language. RISC-V assembly and C appear in Parts 4 and 5 where registers and memory must be seen. TypeScript appears only where the web demands it. Every code block in the text has a runnable file behind it that has been run. Every lab can be completed by the reader with no AI assistant open.

**Why.** Code that was never run is a lie waiting to be found. A lab that needs an assistant teaches the reader to need an assistant, which is the opposite of the book's purpose.

**In practice.**

- Target versions: Python 3.12 or later; C11 compiled with GCC or Clang; RV32I assembly assembled and run with an emulator the chapter names and shows how to install. Versions are stated in the chapter that introduces each toolchain.
- Code is short, named well, commented where the comment explains a *why*, and complete enough to run as shown. No `...` elisions in code that the reader is meant to run.
- The runnable files live in `docs/part-NN/code/`, one folder per chapter, with a `README.md` saying how to run each one.
- Labs state: what the reader will build, what they need, how long it should take, the steps, what success looks like, and two or three "if it doesn't work" checks. Labs are small and the reader's own; a lab is not a tutorial to copy from.
- The "no AI open" rule is stated at the top of every lab, in the same words each time. The chapter also says when the assistant may come back in (after the lab, to review and to go further).
- Hardware labs give an alternative for a reader who does not have the part, even if the alternative is a simulator or a thought experiment with a drawn trace.

## 10. The three tests and the interview questions

**The rule.** Every chapter closes with an explain-it-back prompt and two or three interview questions with model answers. The questions are the kind a real interviewer asks at the mid-level, not trivia.

**Why.** The book exists to pass the three tests. The chapter has to hand the reader the material for tests two and three.

**In practice.**

- The explain-it-back prompt tells the reader exactly what to explain, to whom (an imagined listener with a stated level), and what a good explanation must include. It warns about the most common wrong explanation.
- Each interview question is realistic, says what the interviewer is actually probing for, gives a model answer in the book's voice at the length a person would say out loud, and names one follow-up the interviewer would likely ask.
- Model answers never bluff. If the honest answer is "I'd look that part up, but here is what I know and how I'd reason about it," the model answer says so, because that is also what a good candidate says.

## 11. Honesty about what is not known

**The rule.** When the chapter reaches the edge of what is settled, or what the author actually knows, it says so.

**Why.** Readers who later find out they were bluffed to stop trusting everything else, including the parts that were right.

**In practice.** "Nobody fully agrees on why" is a legitimate sentence. "This is simplified; the real mechanism also involves X, which we will not need" is a legitimate sentence. "I do not know" is a legitimate sentence in a model interview answer.

---

## How these standards change

They change by pull request to this file, approved by Kyle, with a line in `docs/PLAN.md` under Amendments saying what changed and why. A session may propose a change. A session may not quietly apply one.
