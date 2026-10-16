"""Generate the master diagram for From Electrons to Releases.

Geometry and palette follow DIAGRAMS.md (Project doc) exactly:
  viewBox 0 0 960 1480; 13 bands of 100 with 6 gaps, bottom = Physics;
  band label column x 24-168; boxes 116x40 from x 180, 8 gaps, 6 per row,
  row 1 at band-top+8, row 2 at band-top+54.

Usage: python3 master_diagram.py <chapter_number> <out.svg>
Lights every chapter <= N (N >= 1); the current chapter gets a 3px stroke.
Chapter 0 produces the all-unlit frame.
"""
import sys
from xml.sax.saxutils import escape

PALETTE = {
    "paper": "#FFFFFF", "ink": "#1F2937", "muted": "#6B7280", "grid": "#E5E7EB",
    "highlight": "#FACC15",
    "physics": "#D97706", "logic": "#2563EB", "wires": "#0D9488",
    "peripherals": "#7C3AED", "code": "#16A34A", "os": "#0891B2",
    "program": "#65A30D", "network": "#DB2777", "systems": "#4F46E5",
    "trust": "#DC2626", "ship": "#EA580C", "ai": "#C026D3",
}

# Bands bottom -> top: (label, color token, [(chapter, short label), ...])
BANDS = [
    ("Physics", "physics", [(1, "The switch")]),
    ("Logic", "logic", [(2, "Gates"), (3, "Memory cell"), (4, "ALU"), (5, "The CPU"), (6, "Interrupts")]),
    ("Wires", "wires", [(7, "Signals"), (8, "UART"), (9, "SPI"), (10, "I²C"), (11, "CAN"), (12, "USB"), (13, "Fast buses")]),
    ("Peripherals", "peripherals", [(14, "Input"), (15, "Pixel to panel"), (16, "GPU"), (17, "Storage"), (18, "Audio, sensors")]),
    ("Code", "code", [(19, "Bytes"), (20, "The ISA"), (21, "Assembly I"), (22, "Assembly II"), (23, "Linkers"), (24, "C to assembly"), (25, "Compilers"), (26, "Memory, types")]),
    ("OS & runtimes", "os", [(27, "Bare metal"), (28, "Power on"), (29, "The kernel"), (30, "Virtual memory"), (31, "Drivers"), (32, "Files"), (33, "The shell"), (34, "Processes"), (35, "Runtimes"), (36, "The browser")]),
    ("Programming", "program", [(37, "Python inside"), (38, "Data structures"), (39, "Algorithms"), (40, "Readable code"), (41, "Errors"), (42, "Testing"), (43, "Debugging"), (44, "AI pairing")]),
    ("Data & network", "network", [(45, "Serialization"), (46, "Relational DBs"), (47, "Other stores"), (48, "Network stack"), (49, "HTTP & TLS"), (50, "The request")]),
    ("Systems", "systems", [(51, "Architecture"), (52, "API design"), (53, "State at scale"), (54, "Observability"), (55, "Integration"), (56, "Git"), (57, "GitHub"), (58, "Teams"), (59, "System design")]),
    ("Trust", "trust", [(60, "Cryptography"), (61, "Authentication"), (62, "Authorization"), (63, "Memory safety"), (64, "Signing")]),
    ("Shipping", "ship", [(65, "Builds"), (66, "CI/CD"), (67, "Running it")]),
    ("AI", "ai", [(68, "What AI is"), (69, "Claude"), (70, "AI in apps"), (71, "MCP servers")]),
    ("Landing", "ink", [(72, "The interview")]),
]

SLUGS = {
    1: "switch", 2: "gates", 3: "memory-cell", 4: "alu", 5: "cpu", 6: "interrupts",
    7: "signals", 8: "uart", 9: "spi", 10: "i2c", 11: "can", 12: "usb", 13: "fast-buses",
    14: "input", 15: "pixel", 16: "gpu", 17: "storage", 18: "audio-sensors",
    19: "bytes", 20: "isa", 21: "assembly-1", 22: "assembly-2", 23: "linkers", 24: "c-to-asm", 25: "compilers", 26: "memory-types",
    27: "bare-metal", 28: "power-on", 29: "kernel", 30: "virtual-memory", 31: "drivers", 32: "files", 33: "shell", 34: "processes", 35: "runtimes", 36: "browser",
    37: "python-inside", 38: "data-structures", 39: "algorithms", 40: "readable-code", 41: "errors", 42: "testing", 43: "debugging", 44: "ai-pairing",
    45: "serialization", 46: "relational-dbs", 47: "other-stores", 48: "network-stack", 49: "http-tls", 50: "request",
    51: "architecture", 52: "api-design", 53: "state-at-scale", 54: "observability", 55: "integration", 56: "git", 57: "github", 58: "teams", 59: "system-design",
    60: "cryptography", 61: "authentication", 62: "authorization", 63: "memory-safety", 64: "signing",
    65: "builds", 66: "ci-cd", 67: "running-it", 68: "what-ai-is", 69: "claude", 70: "ai-in-apps", 71: "mcp-servers", 72: "interview",
}

W, H = 960, 1480
FONT = "Helvetica Neue, Helvetica, Arial, sans-serif"


def band_top(k):
    return H - 24 - (k + 1) * 106 + 6


def render(current):
    out = []
    a = out.append
    a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="{FONT}">')
    if current == 0:
        title = "From Electrons to Releases — the whole climb, before the first step"
        desc = ("The master diagram of the book, empty. Thirteen horizontal bands stacked from Physics at the bottom "
                "to Landing at the top, each holding small boxes for its chapters, all drawn in grey because no chapter "
                "has been read yet. Each chapter will light one box.")
    else:
        title = f"From Electrons to Releases — after Chapter {current}"
        desc = (f"The master diagram of the book after Chapter {current}. Thirteen horizontal bands from Physics at the "
                f"bottom to Landing at the top; chapters 1 through {current} are lit in their band's color, with "
                f"Chapter {current} outlined more heavily; later chapters remain grey.")
    a(f"  <title>{escape(title)}</title>")
    a(f"  <desc>{escape(desc)}</desc>")
    a(f'  <rect x="0" y="0" width="{W}" height="{H}" fill="{PALETTE["paper"]}"/>')
    a(f'  <text x="24" y="36" font-size="20" font-weight="600" fill="{PALETTE["ink"]}">{escape(title)}</text>')
    a(f'  <text x="24" y="54" font-size="11" fill="{PALETTE["muted"]}">Read it from the bottom up. Each chapter lights one box; each box stands on the ones below it.</text>')
    for k, (label, token, chapters) in enumerate(BANDS):
        top = band_top(k)
        color = PALETTE[token]
        a(f'  <!-- Band {k}: {label} -->')
        a(f'  <g id="band-{token}">')
        a(f'    <rect x="24" y="{top}" width="912" height="100" rx="6" fill="{color}" fill-opacity="0.04" stroke="{color}" stroke-opacity="0.35" stroke-width="1.5"/>')
        a(f'    <text x="32" y="{top + 54}" font-size="14" font-weight="600" fill="{PALETTE["ink"]}">{escape(label)}</text>')
        for i, (n, short) in enumerate(chapters):
            row, col = divmod(i, 6)
            x = 180 + col * 124
            y = top + 8 + row * 46
            lit = 1 <= n <= current
            cur = n == current
            gid = f"L{n:02d}-{SLUGS[n]}"
            if lit:
                stroke, fill, fo, txt = color, color, "0.12", PALETTE["ink"]
            else:
                stroke, fill, fo, txt = PALETTE["grid"], PALETTE["paper"], "1", PALETTE["muted"]
            sw = 3 if cur else 1.5
            a(f'    <g id="{gid}">')
            a(f'      <rect x="{x}" y="{y}" width="116" height="40" rx="4" fill="{fill}" fill-opacity="{fo}" stroke="{stroke}" stroke-width="{sw}"/>')
            a(f'      <text x="{x + 58}" y="{y + 25}" font-size="11" text-anchor="middle" fill="{txt}">{n} · {escape(short)}</text>')
            a('    </g>')
        a('  </g>')
    a('</svg>')
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    n = int(sys.argv[1])
    path = sys.argv[2]
    with open(path, "w") as f:
        f.write(render(n))
    print(f"wrote {path} (chapter {n})")
