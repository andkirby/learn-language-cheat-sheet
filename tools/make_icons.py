#!/usr/bin/env python3
"""Generate PWA PNG icons with the Python stdlib only (no Pillow).

Regenerate every language set (root "Aa", German "DE", English "EN"):
    python3 tools/make_icons.py

Add a set for a new language (letters must exist in FONT below):
    python3 tools/make_icons.py --mark IT --out ital
    (see docs/ADD_LANGUAGE.md for the full checklist)

The mark is the brand pattern from the pages: navy rounded square + white
two-letter text. Maskable variants are full-bleed with a smaller mark.
"""
import argparse
import math
import pathlib
import struct
import zlib

BG = (23, 32, 51)     # brand navy, same as --text / hero #172033
FG = (255, 255, 255)  # mark text white

# 5x7 uppercase bitmap glyphs. Extend when a new language needs a letter.
FONT = {
    "A": [
        ".XXX.",
        "X...X",
        "X...X",
        "XXXXX",
        "X...X",
        "X...X",
        "X...X",
    ],
    "D": [
        "XXXX.",
        "X...X",
        "X...X",
        "X...X",
        "X...X",
        "X...X",
        "XXXX.",
    ],
    "E": [
        "XXXXX",
        "X....",
        "X....",
        "XXXX.",
        "X....",
        "X....",
        "XXXXX",
    ],
    "N": [
        "X...X",
        "XX..X",
        "XX..X",
        "X.X.X",
        "X..XX",
        "X..XX",
        "X...X",
    ],
    "a": [
        ".....",
        ".XXX.",
        "X...X",
        "XXXXX",
        "X...X",
        "X...X",
        ".....",
    ],
}
GAP = 2  # blank columns between letters
SS = 4   # supersampling factor for anti-aliasing

FULL_SIZES = [
    ("icon-32.png", 32, False),
    ("icon-180.png", 180, False),
    ("icon-192.png", 192, False),
    ("icon-512.png", 512, False),
    ("icon-512-maskable.png", 512, True),
]

# The landing (root) has no manifest: it only needs a favicon and an og:image.
SETS = [
    {"mark": "Aa", "out": ".", "sizes": FULL_SIZES[:1] + FULL_SIZES[3:4]},
    {"mark": "DE", "out": "de/ru"},
    {"mark": "EN", "out": "en/ru"},
]


def make_set(mark, out_dir, sizes=None):
    root = pathlib.Path(__file__).resolve().parent.parent
    out = root / out_dir / "icons"
    out.mkdir(parents=True, exist_ok=True)
    grid = glyph_grid(mark)
    for name, size, maskable in (sizes or FULL_SIZES):
        write_png(out / name, size, grid, maskable)


def glyph_grid(mark):
    rows = [FONT.get(c, FONT[c.upper()]) for c in mark]
    height = len(rows[0])
    grid = []
    for r in range(height):
        grid.append(("." * GAP).join(g[r] for g in rows))
    return grid


def in_rounded_rect(x, y, w, h, radius):
    if radius <= 0:
        return 0 <= x < w and 0 <= y < h
    rx = ry = min(radius, w / 2, h / 2)
    if rx <= x <= w - rx or ry <= y <= h - ry:
        return 0 <= x < w and 0 <= y < h
    cx = min(max(x, rx), w - rx)
    cy = min(max(y, ry), h - ry)
    return (x - cx) ** 2 + (y - cy) ** 2 <= rx * ry


def render(size, grid, maskable=False):
    rows_n, cols_n = len(grid), len(grid[0])
    letters_h = size * (0.34 if maskable else 0.42)
    scale = letters_h / rows_n
    ox = (size - cols_n * scale) / 2
    oy = (size - letters_h) / 2
    radius = 0 if maskable else size * 0.22
    hi = size * SS
    hi_ox, hi_oy, hi_scale = ox * SS, oy * SS, scale * SS

    def in_letter(px, py):
        gx, gy = (px - hi_ox) / hi_scale, (py - hi_oy) / hi_scale
        col, row = math.floor(gx), math.floor(gy)
        return 0 <= row < rows_n and 0 <= col < cols_n and grid[row][col] == "X"

    buf = bytearray()
    total = SS * SS
    for y in range(size):
        for x in range(size):
            bg_hits = fg_hits = 0
            for sy in range(SS):
                py = y * SS + sy + 0.5
                for sx in range(SS):
                    px = x * SS + sx + 0.5
                    if not (maskable or in_rounded_rect(px, py, hi, hi, radius * SS)):
                        continue
                    bg_hits += 1
                    if in_letter(px, py):
                        fg_hits += 1
            bg_a, fg_a = bg_hits / total, fg_hits / total
            a = fg_a + bg_a * (1 - fg_a)
            if a == 0:
                buf += b"\x00\x00\x00\x00"
            else:
                w_f, w_b = fg_a, bg_a * (1 - fg_a)
                rgb = [round((FG[c] * w_f + BG[c] * w_b) / a) for c in range(3)]
                buf += bytes(rgb + [round(a * 255)])
    return bytes(buf)


def write_png(path, size, grid, maskable=False):
    raw = render(size, grid, maskable)
    stride = size * 4
    scanlines = b"".join(b"\x00" + raw[i:i + stride] for i in range(0, len(raw), stride))

    def chunk(tag, data):
        body = tag + data
        return struct.pack(">I", len(data)) + body + struct.pack(">I", zlib.crc32(body))

    png = (b"\x89PNG\r\n\x1a\n"
           + chunk(b"IHDR", struct.pack(">IIBBBBB", size, size, 8, 6, 0, 0, 0))
           + chunk(b"IDAT", zlib.compress(scanlines, 9))
           + chunk(b"IEND", b""))
    pathlib.Path(path).write_bytes(png)
    print(f"wrote {path} ({size}x{size}, {len(png)} bytes)")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--mark", help="two-letter mark, e.g. IT (for a new language set)")
    ap.add_argument("--out", help="output folder, e.g. ital")
    args = ap.parse_args()
    if args.mark or args.out:
        if not (args.mark and args.out):
            ap.error("--mark and --out must be used together")
        make_set(args.mark, args.out)
    else:
        for s in SETS:
            make_set(s["mark"], s["out"], s.get("sizes"))


if __name__ == "__main__":
    main()
