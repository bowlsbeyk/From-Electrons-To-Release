# From Electrons to Releases

A textbook from the electron to the signed release: hardware, wires, assembly, operating systems, software, data, networks, trust, shipping, and the AI that now sits on top of all of it.

It is written for someone meeting each idea for the first time. Nothing is assumed. Every chapter stands on the ones before it, and one diagram grows across the whole book until you can point at a GitHub Actions run and trace it down to a flip-flop.

## How to read it

Start with [Chapter 0](part-00/chapter-00-how-to-study-this-book.md). It is the one chapter about *how* to use the rest, and the labs in every later chapter assume you did it.

Every chapter has the same shape:

- **Where we are** — the master diagram with this chapter's layer lit, and the bridge from the last chapter
- **The idea** — the whole chapter in one sentence
- **The concept** — built up slowly, with pictures
- **A worked example** — carried all the way through
- **Lab** — about an hour, done with no AI assistant open
- **Explain it back** — a prompt to teach it to someone, out loud
- **Interview questions** — two or three real ones, with answers and the follow-up
- **What the next chapter builds on this**
- **Sources** — every number in the chapter traced to where it came from

Reading takes about half an hour. The lab takes about an hour. The labs are the point: reading alone will make you recognize these ideas, and the labs make them yours. Chapter 0 explains why that distinction matters more than it sounds.

## What you need

A laptop, Python 3, Git, and for the hardware chapters a kit that costs under eighty dollars (a Raspberry Pi Pico or Arduino, a cheap logic analyzer, a breadboard, a small OLED, a pair of CAN transceivers). Every hardware lab also gives you a way to do it without the hardware. Chapter 0's lab checks your setup and tells you what's missing.

## Where things stand

Chapters appear in the sidebar as they are finished. Greyed titles are planned but not yet written. The source, the figures, and the runnable code for every lab are in the [GitHub repository](https://github.com/bowlsbeyk/From-Electrons-To-Release); if something is wrong, or a chapter lost you, [open an issue](https://github.com/bowlsbeyk/From-Electrons-To-Release/issues). Getting lost is a bug in the chapter, not in you.

The book is MIT licensed. Take it, teach from it, fix it.
