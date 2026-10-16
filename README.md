# From Electrons to Releases

A textbook from the electron to the signed release: hardware, wires, assembly, operating systems, software, data, networks, trust, shipping, and the AI that now sits on top of all of it.

I spent seventeen years fixing machines whose electronics I understood down to the transistor, and then spent a few more shipping software that I mostly directed an AI to write. I could make things work. I could not always say *why* they worked, and I knew it. This book is me tearing down that wall, one layer at a time, and leaving it down for whoever comes next: my son, a technician who wants to become an engineer, a developer who has never seen a scope, or anyone who has ever felt the gap between "I can use this" and "I understand this."

It is written for someone meeting each idea for the first time. Nothing is assumed. Every chapter stands on the ones before it, and one diagram grows across the whole book until you can point at a GitHub Actions run and trace it down to a flip-flop.

## How to read it

Start at [Chapter 0](docs/part-00/chapter-00-how-to-study-this-book.md). It is short and it tells you how to get the most out of the rest.

Every chapter has the same shape: where we are on the map, the one idea in a sentence, the concept built up slowly with pictures, a worked example, a lab you do with no AI assistant open, a prompt to explain it back to someone, two or three real interview questions with answers, and a hand-off to the next chapter. Reading time is about half an hour; the lab is about an hour. The labs are the point. Reading alone will make you recognize these ideas; the labs make them yours.

What you need: a laptop, Python 3, Git, and for the hardware chapters a kit that costs under eighty dollars (a Raspberry Pi Pico or Arduino, a cheap logic analyzer, a breadboard, a small OLED, a pair of CAN transceivers). Every hardware lab also gives you a way to do it without the hardware.

## Status

Written one chapter at a time, in order. ✅ merged · 🚧 in progress · — not started

| # | Chapter | Status |
| --- | --- | --- |
| 0 | How to study this book | — |
| **Part 1 — Physics to logic** | | |
| 1 | The electron and the switch | — |
| 2 | Gates and truth | — |
| 3 | Remembering a bit | — |
| 4 | Adding, comparing, choosing | — |
| 5 | The CPU | — |
| 6 | Interrupts, timers, and the real world | — |
| **Part 2 — Wires: how chips talk** | | |
| 7 | Signals on wires | — |
| 8 | UART and serial | — |
| 9 | SPI | — |
| 10 | I²C | — |
| 11 | CAN | — |
| 12 | USB | — |
| 13 | The fast buses | — |
| **Part 3 — Peripherals: in and out** | | |
| 14 | Input | — |
| 15 | From a pixel to the panel | — |
| 16 | The GPU | — |
| 17 | Storage | — |
| 18 | Audio and sensors | — |
| **Part 4 — Logic to language** | | |
| 19 | Everything is bytes | — |
| 20 | The instruction set | — |
| 21 | Assembly I: moving and deciding | — |
| 22 | Assembly II: the stack and procedures | — |
| 23 | Assemblers, linkers, loaders | — |
| 24 | From C to assembly | — |
| 25 | Compilers, interpreters, bytecode | — |
| 26 | Memory and types from above | — |
| **Part 5 — Operating systems, boot, and runtimes** | | |
| 27 | Bare metal and the RTOS | — |
| 28 | Power on | — |
| 29 | The kernel | — |
| 30 | Virtual memory | — |
| 31 | Drivers and peripherals, revisited | — |
| 32 | Files, descriptors, and everything-is-a-file | — |
| 33 | The shell | — |
| 34 | Processes, threads, and async | — |
| 35 | Runtimes and applications | — |
| 36 | The browser as a runtime, and user interfaces | — |
| **Part 6 — Programming for real** | | |
| 37 | Python from the inside | — |
| 38 | Data structures | — |
| 39 | Algorithms that matter | — |
| 40 | Writing code others can read | — |
| 41 | Errors and edge cases | — |
| 42 | Testing | — |
| 43 | Debugging and reading unfamiliar code | — |
| 44 | AI pair programming | — |
| **Part 7 — Data and networks** | | |
| 45 | Files and serialization | — |
| 46 | Relational databases | — |
| 47 | Other stores | — |
| 48 | The network stack | — |
| 49 | HTTP and TLS | — |
| 50 | A request's full journey | — |
| **Part 8 — Systems** | | |
| 51 | Architecture | — |
| 52 | API design | — |
| 53 | State at scale | — |
| 54 | Observability | — |
| 55 | Enterprise integration | — |
| 56 | Git, properly | — |
| 57 | GitHub and working in the open | — |
| 58 | Working on a software team | — |
| 59 | System design interviews | — |
| **Part 9 — Trust** | | |
| 60 | Cryptography you actually use | — |
| 61 | Authentication | — |
| 62 | Authorization and secrets | — |
| 63 | Memory safety and why Rust exists | — |
| 64 | Signing and supply chain | — |
| **Part 10 — Shipping** | | |
| 65 | Builds, packaging, and versioning | — |
| 66 | CI/CD | — |
| 67 | Running it | — |
| **Part 11 — AI** | | |
| 68 | What AI actually is | — |
| 69 | Claude explained | — |
| 70 | Integrating AI into applications | — |
| 71 | MCP server design | — |
| **Part 12 — Landing it** | | |
| 72 | The interview itself | — |

The full plan, with what each chapter covers, is in [docs/PLAN.md](docs/PLAN.md).

## How it's made

The chapters are drafted with Claude and reviewed, tested, and merged by me. The rules that keep seventy-three chapters sounding like one book are public: [docs/STANDARDS.md](docs/STANDARDS.md) (how a chapter is written), [docs/DESIGN.md](docs/DESIGN.md) (how the book is assembled), and [CLAUDE.md](CLAUDE.md) (the operating manual for the drafting sessions). Every chapter's sources are listed at its end and collected in [docs/BIBLIOGRAPHY.md](docs/BIBLIOGRAPHY.md). Every example, figure, and dataset is original.

If something is wrong, or a chapter lost you, [open an issue](../../issues). Getting lost is a bug in the chapter, not in you. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT. Take it, teach from it, fix it.

— Kyle Bowlsbey
