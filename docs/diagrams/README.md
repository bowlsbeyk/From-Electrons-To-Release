# Diagram Conventions

Every picture in the book is hand-written SVG that follows these rules. The rules exist so a figure in Chapter 60 looks like it belongs in the same book as a figure in Chapter 2, and so the master diagram can grow for 72 chapters without ever being redrawn.

## 1. Technical requirements (every SVG, no exceptions)

- **Self-contained.** No external CSS, no `@import`, no web fonts, no linked images. GitHub renders SVG as an isolated image; anything external will silently vanish.
- **Explicit background.** First element after the root is a full-size `<rect>` filled with the `paper` color, so the figure reads correctly in dark-mode viewers and when embedded anywhere.
- **Real text.** Labels are `<text>` elements, not paths, so they are searchable, selectable, and editable.
- **Accessible.** The root has a `<title>` (one line) and a `<desc>` (two or three sentences saying what the figure shows and what to look at). The `<desc>` doubles as the alt text.
- **Fixed `viewBox`, no `width`/`height` attributes** on the root (so it scales to its container). Widths: 960 units for full-width figures, 640 for half-width. Height as needed.
- **Inline styles only**, via attributes or a single `<style>` block inside the SVG. No classes referenced from outside.
- **No animation, no scripts, no filters.** Static pictures print and render everywhere.
- **Grid-snapped.** Coordinates on an 8-unit grid. Box corners `rx="4"`.
- **Optimized by hand, not by tool.** Readable source: one element per line, indented, with a comment naming each major group. A future session will edit this file.

## 2. Palette

Color means *domain*, consistently, across the whole book. A reader who learns that teal is "wires" in Chapter 7 can rely on it in Chapter 48.

| Token | Hex | Used for |
| --- | --- | --- |
| `paper` | `#FFFFFF` | Backgrounds |
| `ink` | `#1F2937` | Primary text, primary lines, wires |
| `muted` | `#6B7280` | Secondary text, unlit layers, captions |
| `grid` | `#E5E7EB` | Faint guides, unlit outlines, table rules |
| `highlight` | `#FACC15` | Journey paths, the single thing to look at in a figure |
| `physics` | `#D97706` | Part 1 physics: electrons, MOSFETs |
| `logic` | `#2563EB` | Part 1 logic: gates, flip-flops, ALU, CPU |
| `wires` | `#0D9488` | Part 2: signals, serial buses, CAN, USB, PCIe |
| `peripherals` | `#7C3AED` | Part 3: input, display, GPU, storage, sensors |
| `code` | `#16A34A` | Part 4: bytes, ISA, assembly, linkers, compilers |
| `os` | `#0891B2` | Part 5: bare metal, boot, kernel, processes, runtimes |
| `program` | `#65A30D` | Part 6: Python, data structures, testing, debugging |
| `network` | `#DB2777` | Part 7: serialization, databases, TCP/IP, HTTP |
| `systems` | `#4F46E5` | Part 8: architecture, APIs, Git, teams |
| `trust` | `#DC2626` | Part 9: crypto, auth, memory safety, signing |
| `ship` | `#EA580C` | Part 10: builds, CI/CD, running it |
| `ai` | `#C026D3` | Part 11: models, Claude, MCP |

Usage rules:

- A domain color is used as a **stroke** at full strength and as a **fill** at 12% opacity (`fill="#2563EB" fill-opacity="0.12"`). Never a solid saturated fill behind text.
- Text is always `ink` or `muted`, never a domain color, except a single-word label inside a colored stroke where contrast is verified.
- `highlight` is used for one thing per figure: the path, the bit, the edge the caption is pointing at. If everything is highlighted, nothing is.
- Nothing outside this table. If a figure genuinely needs another color (a physical red wire, a green LED), say so in the figure's `<desc>` and use the closest token or a documented one-off noted in `CONTINUITY.md` under conventions.

`palette.svg` in this folder is the swatch sheet; render it to check that nothing has drifted.

## 3. Typography and line weights

| Element | Setting |
| --- | --- |
| Font | `font-family="Helvetica Neue, Helvetica, Arial, sans-serif"` on the root `<svg>` |
| Figure title | 20px, `font-weight="600"`, `ink` |
| Band / section label | 14px, `font-weight="600"`, `ink` |
| Box label | 12px, `ink` |
| Annotation, caption inside figure | 11px, `muted` |
| Monospace (hex, code, register names) | `font-family="SFMono-Regular, Menlo, Consolas, monospace"`, 11px |
| Box outline | `stroke-width="1.5"` |
| Wire / signal line | `stroke-width="2"`, `ink` |
| Bus (many wires) | `stroke-width="6"`, domain color, with a short slash and a count label (`/8`) |
| Guide / grid line | `stroke-width="1"`, `grid` |
| Emphasis outline (the current chapter's layer; the thing being discussed) | `stroke-width="3"` |
| Arrowheads | A single shared `<marker id="arrow">`, 8 units long, filled with the line's color |

## 4. The master diagram

File: `docs/diagrams/master/master-ch-NN.svg`, one per chapter, each a copy of the previous with one layer added.

### Geometry (fixed; do not change)

- `viewBox="0 0 960 1480"`.
- Title block: y 0–56. Title at (24, 36): "From Electrons to Releases — after Chapter NN".
- Thirteen horizontal **bands**, stacked bottom to top in the order of the table in `DESIGN.md` §3 (Physics at the bottom, Landing at the top). Each band is 100 units tall with a 6-unit gap. Band k (k = 0 for Physics) occupies y from `1480 − 24 − (k+1)·106 + 6` to `1480 − 24 − k·106`. Physics therefore sits at the bottom edge; Landing at the top under the title.
- Band label column: x 24–168, label at x 32, vertically centered, 14px bold. Band outline: `rx="6"`, stroke in the band's domain color at `stroke-opacity="0.35"`, fill the domain color at 4% opacity.
- Layer boxes inside a band: 120 wide × 40 tall, `rx="4"`, laid out left to right starting at x 184, 12-unit gaps, up to six per row, wrapping to a second row. Row 1 at band-top + 8; row 2 at band-top + 54.
- Each layer box's `<g>` has `id="L{NN}-{slug}"` where NN is the chapter number. The id never changes.

### Lit and unlit

- **Unlit** (future chapter): stroke `grid`, fill `paper`, label `muted`, label text is the chapter number and short title, e.g. "22 · The stack".
- **Lit** (merged chapter): stroke in the band's domain color, fill at 12% opacity, label `ink`.
- **Current** (this chapter's layer): lit, plus `stroke-width="3"`. Only one box is current in any master file.

`master-ch-00.svg`, produced by Chapter 0, draws every band and every box unlit, so the reader sees the whole climb before the first step. From Chapter 1 on, each file lights one more box.

### Journeys

Once a journey exists (see `DESIGN.md` §3), it is drawn as a `highlight` path, `stroke-width="4"`, `stroke-linecap="round"`, `stroke-dasharray="2 10"` (dotted), connecting the centers of the boxes it passes through, drawn *behind* the boxes (earlier in document order) so labels stay readable. Each journey has its own `<g id="J-{name}">` and a small legend entry at the bottom right.

## 5. Chapter figures

File: `docs/part-NN/ch-NN-fig-MM-slug.svg`, referenced in the chapter as `![Figure NN.MM — caption](ch-NN-fig-MM-slug.svg)` followed by an italic caption line in the Markdown.

### The shared visual vocabulary

These shapes mean the same thing everywhere. New ones are added here, by PR, when a chapter needs them, and recorded in `CONTINUITY.md` under conventions.

| Thing | How it is drawn |
| --- | --- |
| A component or block | Rectangle, `rx="4"`, 1.5 stroke, label centered |
| A wire | 2px `ink` line, right angles only, 8-unit grid |
| A bus | 6px line in the domain color, one slash with a count (`/8`) near its start |
| Signal direction | Arrowhead (shared marker) at the destination end only |
| A clock | Square wave, 2px `logic`, rising edges marked with a small triangle when the edge matters |
| A timing window (data valid, setup, hold) | Light fill (domain color, 12%) between two dashed vertical `muted` lines, labeled above |
| A register or memory cell | Rectangle divided into equal cells; each cell shows its bit or value in monospace; bit numbers in 11px `muted` under the cells, bit 0 on the **right** |
| Memory as a column | Addresses on the left in monospace, growing **downward** with increasing address (stated in Chapter 19 and never changed; stacks are then shown growing upward toward lower addresses) |
| A packet or frame | A horizontal strip divided into fields, field name in 11px, width proportional to size when sizes are known, with a byte or bit ruler beneath |
| A process or sequence step | Numbered circle (16 units) in the domain color at the start of the step |
| Time | Always left to right |
| Abstraction / layers | Always bottom (physical) to top (abstract), matching the master diagram |
| "Zoom": this figure is a detail of that one | A dashed `muted` box on the parent figure with the child figure number beside it |
| Something broken or wrong | Dashed `trust`-red stroke, never a solid fill |

### Captions

Every figure has a caption in the Markdown directly under it, italic, beginning with "Figure NN.MM —". The caption says what to look at and ties it to the paragraph it sits in. A reader who only looked at the figures and captions should get the chapter's skeleton.

## 6. Checking a diagram before it is committed

1. Open it in a browser. Does it render with no missing text? Are no labels colliding?
2. View it at half size. Is the main point still visible?
3. Read the `<desc>` without the image. Would someone who cannot see it know what it says?
4. Compare it to the previous chapter's figures. Same palette, same weights, same vocabulary?
5. For a master file: diff it against the previous master. The diff should be exactly one box lit (and, if applicable, one journey extended) and the title changed. Nothing else.
