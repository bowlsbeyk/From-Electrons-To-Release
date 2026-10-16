# From Electrons to Releases — Textbook Plan

Started Oct 16, 2026 · Kyle Bowlsbey

This is the source of truth for what the book covers and in what order. It changes only by amendment (see the end of this file). `STANDARDS.md` says how each chapter is written; `DESIGN.md` says how the book is assembled.

## Goal

When Kyle finishes this book he can explain, from first principles, everything between an electron moving in a transistor and a signed release running in production, and he can build and defend each layer himself in an interview.

The standard for every chapter is the same three tests, and reading alone passes none of them:

1. **Build it without AI.** A lab Kyle completes with no assistant open. Small, but his own.
2. **Explain it back.** He teaches the chapter's core idea to Claude in his own words, and Claude pushes until the explanation holds.
3. **Survive the question.** One or two realistic interview questions on that layer, answered out loud.

Kyle is the first reader, not the only one. The book is written so that his son, or a stranger who finds one chapter, can follow it from the first sentence. In Kyle's words: *"We are tearing down a wall in my way, then leaving it down for everyone else."*

Secondary goals: the finished book is publishable on GitHub and LinkedIn as a serialized guide, so every example is original or generic (nothing from CORE, Nebula, CLARK, or other Southern Linac work), and every diagram is built on the one before it.

## How the book works

Twelve parts, 73 chapters (0–72), written one at a time, in order.

| Element | Decision |
| --- | --- |
| Anchor language | Python for Parts 4–10; RISC-V assembly and C for Parts 4–5, where you must see registers and memory; a little TypeScript where the web demands it |
| Hardware lab kit | One Raspberry Pi Pico or Arduino, a cheap logic analyzer, a breadboard, an OLED display, a CAN transceiver pair. Under $80 total. Every hardware lab gives a no-hardware alternative |
| Software lab kit | Python 3, Git, Docker, a free GitHub account, a Pi or NUC as the deploy target |
| The master diagram | One diagram that grows every chapter: transistor → gate → CPU → bus → peripherals → OS → process → network → service → pipeline. By Part 10 you can trace a GitHub Actions run down to a flip-flop. Geometry and palette are fixed in `diagrams/README.md` |
| Chapter format | Where we are (master diagram + bridge from the last chapter) · the idea in one sentence · the concept · a worked example · the lab (no AI) · explain-it-back prompt · interview questions · what the next chapter builds on this · sources. Template in `templates/chapter-template.md` |
| Pace | **Methodical throughout.** There is no fast part of this book. No chapter assumes the reader already knows the material, including the physics and electronics chapters where Kyle is strongest. One idea at a time, every step on the page. *(Amended Oct 16, 2026; see Amendments.)* |
| Size | About a 30-minute read (roughly 4,000–6,000 words of prose) plus a 1-hour lab. If a chapter cannot be done methodically in that space, it is split by amendment, never thinned |
| Voice | Kyle explaining to one person across a workbench: stories, concrete illustrations, plain words, no machine phrasing. Details in `STANDARDS.md` §4 |
| Research | Many sources per chapter, primary first, cited in footnotes. Details in `STANDARDS.md` §6 |
| Format | Each chapter is its own Markdown file with its SVGs beside it; this plan and `README.md` link them as they are merged |

## Parts and chapters

**Chapter 0 — How to study this book.** Spaced repetition for the vocabulary (use the FSRS app Kyle already built, or any flashcard tool), a learning journal, a glossary you keep yourself, how to run a lab with no AI open and when to let it back in, how to tell real understanding from recognition, and the three tests. Produces `master-ch-00.svg`: the whole stack, unlit, so the reader sees the climb before the first step.

**Part 1 — Physics to logic** (where many readers feel most at home; written with the same patience as everything else)

1. **The electron and the switch.** Semiconductors, doping, the MOSFET as a voltage-controlled switch. Why "1" and "0" are really voltage bands and noise margins.
2. **Gates and truth.** NAND builds everything; Boolean algebra; propagation delay as the reason computers have a speed limit.
3. **Remembering a bit.** Latches, flip-flops, the clock edge. SRAM vs DRAM vs flash: why refresh exists and why your SSD wears out.
4. **Adding, comparing, choosing.** Adders, ALU, multiplexers. Two's complement and why integers overflow.
5. **The CPU.** Registers, program counter, fetch-decode-execute, the control unit. A 4-instruction CPU you can trace by hand.
6. **Interrupts, timers, and the real world.** Polling vs interrupts, timers, DMA. Why a late interrupt is a crashed drone and a dropped video frame alike. *(Example domain changed from the original "linac fault"; see Amendments.)*

**Part 2 — Wires: how chips talk**

7. **Signals on wires.** Logic levels, rise time, ringing, pull-ups, open-drain. Reading a bus on a scope and a logic analyzer.
8. **UART and serial.** Start/stop bits, baud, framing errors, RS-232 vs RS-485, why your console cable works.
9. **SPI.** Clock polarity and phase, chip select, daisy chains. Talking to a display and a flash chip.
10. **I²C.** SDA/SCL, addressing, ACK/NACK, clock stretching, multi-master, and why a stuck bus happens.
11. **CAN.** Differential signaling, arbitration by ID, error frames, why it survives noise. CAN FD and J1939 in brief.
12. **USB.** Host and device, descriptors, endpoints, enumeration. The moment you plug in a keyboard, traced step by step.
13. **The fast buses.** PCIe lanes, DDR memory channels, and memory-mapped I/O: how a register in a device becomes an address the CPU can write.

**Part 3 — Peripherals: in and out**

14. **Input.** Key matrix scanning, debouncing, USB HID reports, the OS input stack, the event your program finally sees.
15. **From a pixel to the panel.** Framebuffer, color depth, scanout, pixel clock, HDMI and DisplayPort, LCD and OLED panel timing, refresh rate and tearing.
16. **The GPU.** Why graphics went parallel; shaders; the pipeline from triangle to pixel; what a window manager and a browser ask the GPU to do.
17. **Storage.** Sectors, controllers, NVMe queues, wear leveling, and what a filesystem adds on top.
18. **Audio and sensors.** ADC/DAC, sample rate, I²S, and reading an IMU — the bridge to the reader's own hardware projects.

**Part 4 — Logic to language** (the critical jump: heavy on machine code and assembly, taken slowly)

19. **Everything is bytes.** Integers, two's complement again, IEEE 754 floats, characters, endianness, bit fields. Reading a hex dump and knowing what you are looking at.
20. **The instruction set.** What an ISA is, opcode and operand encoding, RISC-V as the teaching ISA (open and clean) with x86-64 and ARM side by side. Hand-assemble five instructions to hex and run them on the Chapter 5 CPU.
21. **Assembly I: moving and deciding.** Registers, load and store, arithmetic, compare and branch, loops. Ten small programs in a RISC-V emulator, each traced register by register.
22. **Assembly II: the stack and procedures.** Memory addressing, the stack pointer, call and return, calling conventions, local variables, recursion in assembly. Why a stack overflow is literal.
23. **Assemblers, linkers, loaders.** Symbols, object files, sections, relocations, ELF, static vs dynamic linking. What "undefined reference" and "shared library not found" actually mean.
24. **From C to assembly.** The compiler as translator: write C, read its disassembly, map every line. Pointers are addresses, structs are offsets, the ABI is a contract. Optimization levels and what they change.
25. **Compilers, interpreters, bytecode.** Lexing, parsing, ASTs, code generation, virtual machines, JIT. Build a 200-line interpreter for a tiny language in Python.
26. **Memory and types from above.** Stack vs heap, allocation, leaks, garbage collection, reference counting; static vs dynamic and strong vs weak typing. What a type system buys you and what it costs.

**Part 5 — Operating systems, boot, and runtimes** (how software becomes a running application)

27. **Bare metal and the RTOS.** Startup code, the vector table, bare-metal firmware with no OS at all, then FreeRTOS and Zephyr: tasks, priorities, scheduling, and timing guarantees. The layer embedded engineers already live in, named — and the reason the Linux kernel makes the choices it does.
28. **Power on.** Reset vector, firmware (BIOS and UEFI), the bootloader, kernel load, init and systemd, the first user process. Traced on a Raspberry Pi and on a PC, with the master diagram gaining its first software layer.
29. **The kernel.** User mode vs kernel mode, system calls, the scheduler, context switches, signals. strace a real program and read every call.
30. **Virtual memory.** Pages, page tables, the TLB, process isolation, mmap, swap. Why a segfault happens and why two programs can both think they own address 0x400000.
31. **Drivers and peripherals, revisited.** The keystroke and the pixel from Part 3 again, now through software: interrupt handler → driver → input subsystem → compositor → your program; framebuffer → DRM/KMS → GPU driver → display. Both journeys on the master diagram are now complete end to end.
32. **Files, descriptors, and everything-is-a-file.** Filesystems, inodes, the VFS, permissions, file descriptors, pipes, sockets as files. The storage chapter from Part 3 gains its software half.
33. **The shell.** Bash, pipes and redirection, grep/awk/sed, find, ssh, tmux, scripting, environment variables, exit codes. Every lab from here on assumes this chapter.
34. **Processes, threads, and async.** fork and exec, threads, the GIL, race conditions, locks, event loops. When to use each, and how to prove a race exists.
35. **Runtimes and applications.** What a runtime is (CPython, the JVM, V8 and Node, .NET, WebAssembly), JIT compilation, standard libraries. How an application is born: executable formats, dynamic libraries, packaging, sandboxes, and the full path from double-click to main(). The jump from "software" to "an app".
36. **The browser as a runtime, and user interfaces.** HTML, CSS, JavaScript, the DOM, the browser event loop, layout and painting down to the GPU of Chapter 16. How mobile and desktop UI frameworks (Android, Compose, SwiftUI, Qt) do the same job. The pixel's journey finally ends at the thing a user clicks.

**Part 6 — Programming for real** (Python, deeply)

37. **Python from the inside.** Objects, names, mutability, scope, modules, the import system, virtual environments. Built on the CPython runtime from Chapter 35.
38. **Data structures.** Arrays, linked lists, hash maps, trees, graphs. Big-O as a budget, not a quiz, and what each one costs in memory from Chapter 26.
39. **Algorithms that matter.** Sorting, searching, recursion, dynamic programming once, graph traversal. The 15 patterns behind most interview questions.
40. **Writing code others can read.** Naming, functions, modules, SOLID without the dogma, code smells, refactoring. Reviewing a real pull request.
41. **Errors and edge cases.** Exceptions, failure modes, defensive vs offensive programming, logging that helps at 2 a.m.
42. **Testing.** Unit, integration, end-to-end, property-based. TDD honestly. Mocks and when they lie.
43. **Debugging and reading unfamiliar code.** Debuggers, bisecting, tracing, profiling. Dropping into a 50k-line codebase and finding the thing.
44. **AI pair programming.** Prompting as specification, plan-then-code, review discipline, when to say no to the model, keeping ownership of code you did not type. Claude Code and MCP-driven workflows done well.

**Part 7 — Data and networks**

45. **Files and serialization.** Bytes, encodings, JSON, Protobuf, binary formats. Why UTF-8 won.
46. **Relational databases.** Tables, SQL, joins, normalization, indexes (B-trees), query plans, transactions and ACID.
47. **Other stores.** Key-value, document, time-series, search. Picking one for a reason.
48. **The network stack.** Ethernet, IP, routing, TCP vs UDP, DNS, NAT. Traced with Wireshark, and tied back to the serial framing of Chapter 8.
49. **HTTP and TLS.** Requests, status codes, headers, cookies, HTTP/2 and 3, the TLS handshake, certificates.
50. **A request's full journey.** Browser → DNS → TLS → load balancer → app → database → back. One diagram, every hop.

**Part 8 — Systems**

51. **Architecture.** Monolith, modular monolith, services, event-driven. Trade-offs, not fashion.
52. **API design.** REST, GraphQL, gRPC, versioning, pagination, idempotency, errors as contract.
53. **State at scale.** Caching, queues, background jobs, consistency, idempotent retries.
54. **Observability.** Logs, metrics, traces, alerting, SLOs. Debugging production without SSH.
55. **Enterprise integration.** SSO (SAML and OIDC), ETL and data pipelines, message buses, legacy and ERP systems, flat-file interfaces, data governance. Unglamorous, and the literal job description of integration and forward-deployed engineering roles.
56. **Git, properly.** The object model, branching strategies, rebasing, bisect, hooks, and recovering from disasters.
57. **GitHub and working in the open.** Repos, forks, pull requests, code review etiquette, issues and projects, branch protection, CODEOWNERS, releases and tags, GitHub Actions as a platform, licenses (MIT vs Apache vs GPL), CONTRIBUTING and governance of an open-source project. Lab: contribute a real PR to someone else's repo.
58. **Working on a software team.** Sprints, tickets, standups, estimation, design docs and ADRs, RFCs, code review as a social skill, postmortems, on-call, how to ask for help without looking lost, and how to be the new senior-ish person who has never done this in a team before.
59. **System design interviews.** The method: requirements, estimation, high-level design, deep dives, trade-offs. Three worked problems.

**Part 9 — Trust**

60. **Cryptography you actually use.** Hashing, symmetric and asymmetric encryption, signatures, key exchange, randomness. No math beyond what you need.
61. **Authentication.** Passwords done right, sessions, JWTs, OAuth 2 and OIDC, MFA, passkeys. Building a login flow and attacking it.
62. **Authorization and secrets.** RBAC, ABAC, least privilege, secret storage, rotation, the OWASP Top 10 as a checklist.
63. **Memory safety and why Rust exists.** Buffer overflows, use-after-free, how an exploit actually works on the Chapter 22 stack, mitigations (ASLR, stack canaries, NX), and the language-level answers: Rust's ownership model, and why governments now ask for memory-safe languages.
64. **Signing and supply chain.** PKI, certificates, code signing, release signing (Sigstore, GPG, Apple and Windows signing), SBOMs, reproducible builds.

**Part 10 — Shipping**

65. **Builds, packaging, and versioning.** Build systems, semantic versioning, lockfiles, wheels and containers, release notes. The linker from Chapter 23 and the runtime from Chapter 35 explain every build error.
66. **CI/CD.** Pipelines, GitHub Actions, test gates, artifacts, environments, deployment strategies (blue-green, canary, rollback).
67. **Running it.** Containers (namespaces and cgroups from the kernel chapters), orchestration basics, infrastructure as code, config, scaling, cost. Deploying to a Pi and to a cloud.

**Part 11 — AI** (the capstone, built on everything above)

68. **What AI actually is.** From a neuron to a transformer: tokens, embeddings, attention, training vs inference, why models hallucinate. Where the matrix multiplies run (back to the GPU in Chapter 16).
69. **Claude explained.** Context windows, system prompts, tool use, structured output, extended thinking, cost and latency. How to read a model card.
70. **Integrating AI into applications.** Prompts as code, evaluation, RAG, agents and tool loops, guardrails, observability for LLM features, when not to use a model.
71. **MCP server design.** Protocol, tools, resources, prompts, transport, auth, error contracts. The capstone project: a production-grade MCP server, signed, tested, and shipped through the pipeline from Part 10.

**Part 12 — Landing it**

72. **The interview itself.** Behavioral questions, talking about your own projects without underselling or overselling, the take-home, the live-coding session, what to do when you don't know, reference checks, and the salary conversation. The chapter to reread the night before.

## Open decisions

Chapter 0 does not depend on these. Chapter 1 starts when the first four are ticked.

- [ ] Confirm the anchor language (Python) and the 30-minute read + 1-hour lab chapter size
- [ ] Confirm the hardware lab kit, or name what Kyle already owns
- [ ] Study cadence: how many chapters a week, and whether labs happen at a desk or on the road
- [ ] Order of attack: straight through, or Parts 5–7 first because interviews are near, then back to Part 1
- [ ] LinkedIn release: one chapter per post, or one part per week
- [ ] Static site for the book (mdBook or Docusaurus) once a few chapters exist; CONTRIBUTING guide and issue templates so readers can fix errors and add labs. Building that doubles as the lab for Chapters 56–57 and 65–66

Publishing rule: every code example, dataset, and diagram in the book is original. Nothing from CORE, Nebula, CLARK, Iris, or client sites appears, even disguised, until the IP question on that work is settled. Client details never appear.

## Amendments

Dated, newest last. Every change to this plan, `STANDARDS.md`, `DESIGN.md`, or `diagrams/README.md` gets a line here saying what changed, why, and who approved it.

- **2026-10-16 — Pace.** Removed "fast through Parts 1–3 (your turf)" and "move fast where Kyle is already strong." The book is methodical throughout; no chapter assumes prior knowledge. Reason: Kyle's instruction that the book is for his son and for strangers as much as for him, and that he is not to be assumed able to climb everything easily. Approved by Kyle in chat.
- **2026-10-16 — Voice, diagrams, research.** Added the voice rule (Kyle explaining, not a robot; stories and illustrations), the diagrams-everywhere rule, and the many-sources-with-citations rule to this plan and to `STANDARDS.md`. Approved by Kyle in chat.
- **2026-10-16 — Repository structure.** Added `CLAUDE.md`, `STANDARDS.md`, `DESIGN.md`, `CONTINUITY.md`, `GLOSSARY.md`, `BIBLIOGRAPHY.md`, templates, diagram conventions, and the PR checklist as the anti-drift mechanism. Requested by Kyle in chat; approved on merge of the setup PR.
- **2026-10-16 — Chapter 6 example domain (proposed, pending Kyle's approval on the setup PR).** Changed "a late interrupt is a linac fault" to "a crashed drone" in the chapter summary, so the plan itself follows the no-linac-examples rule. If Kyle prefers the original wording in the plan (the chapter text will use a generic example either way), revert this line.
