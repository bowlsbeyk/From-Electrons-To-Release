# Design Document

How the book is built. `docs/STANDARDS.md` says how a chapter must be *written*; this document says how the book is *assembled* so that 73 chapters written across many sessions come out as one book. If `STANDARDS.md` is the style guide, this is the architecture.

---

## 1. The shape of the book

Twelve parts, 73 chapters numbered 0 through 72. The order is fixed in `docs/PLAN.md` and does not change without an amendment.

The book has one organizing device: **the master diagram**, a single picture that starts as a transistor and ends as a release pipeline, gaining exactly one layer per chapter. Every chapter also builds explicit bridges to earlier chapters in prose. The intended experience is that a reader who finishes Chapter 72 can point at any box in the final master diagram and trace downward until they reach a flip-flop, and trace upward until they reach a signed artifact, and explain every step.

The chapters are written one at a time, in order. A chapter is not started until the previous one is merged, because it depends on the merged chapter's closing section, its continuity entry, and its diagram.

## 2. Repository layout

```
/
├── CLAUDE.md                       Operating manual for Claude sessions
├── README.md                       Public front page: what this is, status, how to read
├── CONTRIBUTING.md                 How readers fix errors and add labs
├── LICENSE                         MIT
├── .github/
│   └── PULL_REQUEST_TEMPLATE.md    The chapter review checklist
└── docs/
    ├── PLAN.md                     The plan: parts, chapters, decisions, amendments
    ├── STANDARDS.md                Writing standards
    ├── DESIGN.md                   This file
    ├── CONTINUITY.md               The ledger: what each chapter introduced and promised
    ├── GLOSSARY.md                 Every defined term, with its defining chapter
    ├── BIBLIOGRAPHY.md             Every source cited anywhere, deduplicated
    ├── templates/
    │   ├── chapter-template.md     Skeleton every chapter starts from
    │   ├── continuity-entry.md     Skeleton for a CONTINUITY.md entry
    │   └── research-notes.md       Skeleton for a chapter's research notes
    ├── diagrams/
    │   ├── README.md               SVG conventions, palette, master diagram rules
    │   ├── palette.svg             The palette as a swatch sheet
    │   └── master/
    │       ├── master-ch-00.svg    Master diagram after Chapter 0 (the empty frame)
    │       ├── master-ch-01.svg    After Chapter 1
    │       └── ...
    └── part-NN/                    One folder per part, NN zero-padded (part-01 … part-12; Chapter 0 lives in part-00)
        ├── chapter-NN-slug.md      The chapter
        ├── ch-NN-fig-MM-slug.svg   The chapter's own figures
        ├── code/                   Runnable files behind every code block
        │   └── README.md
        └── research/
            └── ch-NN-notes.md      Sources consulted and what they said
```

Naming rules:

- Chapter numbers are two digits, zero-padded, everywhere: `chapter-05-the-cpu.md`, `master-ch-05.svg`, `ch-05-fig-02-fetch-decode-execute.svg`.
- Slugs are lowercase, hyphenated, drawn from the chapter title in `docs/PLAN.md`.
- Figure numbers restart at 01 in each chapter and are referenced in the text as "Figure 5.2" (chapter.figure).
- Nothing lives at the repo root except the files listed above. New top-level files need an amendment.

## 3. The master diagram

### What it is

One SVG, redrawn as a new file after every chapter by copying the previous file and adding a layer. It reads bottom to top: physics at the bottom, shipping at the top. By Chapter 72 it shows the full stack from electron to release.

### Layer registry

Each chapter adds exactly one layer, identified by a stable ID that never changes. The ID is used as the SVG group id (`<g id="L05-cpu">`) and is referenced in `CONTINUITY.md`. The registry is the plan's chapter list; a layer's label is the chapter's lead noun.

| Band (bottom → top) | Chapters | Color token | What the band holds |
| --- | --- | --- | --- |
| Physics | 1 | `physics` | The electron, the MOSFET |
| Logic | 2–6 | `logic` | Gates, memory cells, ALU, CPU, interrupt controller |
| Wires | 7–13 | `wires` | Signals, serial buses, CAN, USB, PCIe/DDR, MMIO |
| Peripherals | 14–18 | `peripherals` | Input, display, GPU, storage, audio/sensors |
| Code | 19–26 | `code` | Bytes, ISA, assembly, linker, compiler, interpreter, memory model |
| OS & runtimes | 27–36 | `os` | Bare metal/RTOS, boot, kernel, VM, drivers, files, shell, processes, runtimes, browser |
| Programming | 37–44 | `program` | Python internals, data structures, algorithms, style, errors, tests, debugging, AI pairing |
| Data & network | 45–50 | `network` | Serialization, databases, stores, network stack, HTTP/TLS, the request |
| Systems | 51–59 | `systems` | Architecture, APIs, state, observability, integration, Git, GitHub, teams, design interviews |
| Trust | 60–64 | `trust` | Crypto, authn, authz, memory safety, signing |
| Shipping | 65–67 | `ship` | Build, CI/CD, running it |
| AI | 68–71 | `ai` | Models, Claude, integration, MCP |
| Landing | 72 | `ink` | The interview (drawn as the reader, standing on the stack) |

Chapter 0 produces `master-ch-00.svg`: the empty frame with the twelve bands labeled and greyed, so the reader sees the whole shape of the climb before taking the first step. Each subsequent chapter lights up its layer within its band.

### Rules

- A new layer is added. Existing layers are never moved, recolored, relabeled, or removed. If a redesign is ever approved, it is applied to every prior master file in one PR.
- The canvas size, band positions, palette, and fonts are fixed in `docs/diagrams/README.md`. Do not improvise.
- Every master file is self-contained SVG (no external CSS, fonts, or images) so GitHub renders it as an image identically everywhere.
- The chapter embeds its master diagram with a caption that names the new layer and says, in one sentence, how it sits on the layer below.
- Two "journeys" are tracked through the master diagram as highlighted paths once they exist: the keystroke's journey (Chapter 14 → 31 → 36) and the pixel's journey (15 → 16 → 31 → 36). Later, the request's journey (50) and the release's journey (64–67). `docs/diagrams/README.md` specifies how a journey is drawn.

## 4. The continuity ledger

`docs/CONTINUITY.md` is the book's memory across sessions. It is the primary mechanism against drift, and it is maintained with the same care as the chapters.

### One entry per merged chapter

Each entry, from `docs/templates/continuity-entry.md`:

- **Chapter number, title, status, merge date, PR link.**
- **Lead idea** — the one sentence.
- **Terms defined** — exactly the terms added to the glossary, with the one-line definition used.
- **Master diagram layer added** — the layer ID and label.
- **Figures** — list of the chapter's figures with one-line descriptions, so a later chapter can reuse the same visual language.
- **Code and tools introduced** — files, libraries, toolchains, with versions.
- **Debts paid** — which promises from earlier chapters this chapter fulfilled.
- **Promises made** — every forward reference ("Chapter 22 will show…"), as a checklist item the future chapter must tick.
- **Stories and analogies used** — so they are not repeated unknowingly, and so a later chapter can call back to one deliberately.
- **Conventions fixed** — any notation, unit, bit-ordering, naming, or style decision this chapter made that later chapters must keep.
- **Known simplifications** — anything the chapter said that is "true enough for now" and which chapter will make it fully true.

### Open promises

A section at the top of `CONTINUITY.md` lists every unticked promise across all chapters, sorted by the chapter that owes it. Before a chapter is written, the session reads this list and pays what is owed. When a promise is paid, it is ticked in both places.

## 5. The glossary

`docs/GLOSSARY.md` is alphabetical. Each entry: the term, the one-line definition as the book gave it, the chapter and section that defined it, and alternatives the field uses that the book does not. A term enters the glossary in the same PR as the chapter that defines it.

The glossary is also the book's terminology lock. If a session wants to use a different word for an existing entry, that is an amendment, not a stylistic choice.

## 6. The bibliography

`docs/BIBLIOGRAPHY.md` collects every source cited in any chapter, deduplicated, in a stable format (author or organization; title; edition or version; date; URL; license if open). Each entry lists the chapters that cite it. It grows in the same PR as the chapter.

## 7. The chapter template

Every chapter is `docs/templates/chapter-template.md` filled in, with all sections present and in this order:

1. Title block — number, title, part, reading time, lab time, what you need
2. **Where we are** — the master diagram with the new layer, and the bridge from the previous chapter
3. **The idea** — the one-sentence lead idea, set apart
4. **The concept** — the methodical build-up: story or concrete picture → the named idea → the general idea, with figures
5. **A worked example** — one example carried all the way through
6. **Lab** — no AI open; what you'll build, what you need, steps, what success looks like, if-it-doesn't-work
7. **Explain it back** — the prompt
8. **Interview questions** — two or three, each with what's being probed, a model answer, and the likely follow-up
9. **What the next chapter builds on this** — the hand-off, which becomes the next chapter's opening and the ledger's promises
10. **Sources** — the footnotes collected

A section may not be dropped. If a section genuinely does not apply (it should not happen), the section stays with one sentence saying why.

## 8. Workflow

1. Session starts: read `CLAUDE.md`, `PLAN.md`, `STANDARDS.md`, this file, `CONTINUITY.md` (all of it), `GLOSSARY.md`, and the previous chapter.
2. Research into `docs/part-NN/research/ch-NN-notes.md`.
3. Outline, then write from the template.
4. Draw: copy the previous master diagram, add the layer; draw the chapter figures.
5. Code: write, run, store under `code/`.
6. Review twice (senior engineer; first-time reader). Run the PR checklist.
7. Update `CONTINUITY.md`, `GLOSSARY.md`, `BIBLIOGRAPHY.md`, `README.md` status table.
8. Branch `chapter/NN-slug`, PR `Chapter NN: Title`, Kyle merges.
9. Kyle does the lab and the explain-it-back in chat; Claude is the interviewer. Anything that turns out wrong or unclear in the chapter is fixed by a follow-up PR titled `Chapter NN: fix — <what>`.

## 9. Change control

- `docs/PLAN.md` changes only by amendment: a dated line under "Amendments" saying what changed, why, and that Kyle approved it, in the same PR as the change.
- `docs/STANDARDS.md`, this file, and `docs/diagrams/README.md` change by PR approved by Kyle, with an amendment line.
- Merged chapters are not restyled. Errors are fixed; voice, structure, and terminology are left alone unless Kyle asks.
- Any session that believes the book has drifted names the first chapter where it happened and proposes a scoped fix before touching anything.

## 10. Publishing (decided in principle, details pending)

The book is public from the first commit under MIT. A static site (mdBook or similar) and a LinkedIn serialization are planned once a few chapters exist; the plan's open decisions cover the cadence. Nothing in a chapter depends on the site generator: chapters are plain Markdown with relative links and inline-referenced SVGs so they read correctly on GitHub, in an editor, and on a site.
