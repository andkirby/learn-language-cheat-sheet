# Font vendoring (skin A «Тетрадь»)

Purpose: own the vendored webfonts behind skin A — why they are committed
to the repository, the exact inventory, the re-vendor procedure, the subset
policy and where they are consumed. This file is the maintenance reference
for the sanctioned exception to the no-external-dependencies rule
(AGENTS.md hard rule 5). It does not own the skin's tokens, components or
switcher contract — those live in
[.design/DESIGN_SYSTEM.md](../.design/DESIGN_SYSTEM.md) and
`assets/skin-a.css`.

## Why vendored

The site is an offline-first PWA on GitHub Pages: no CDN, no third-party
requests, everything works offline. Skin A's editorial voice needs real
typefaces (Onest for UI, Spectral for target-language/study text), and a
Google Fonts `<link>` would break all three rules at once — an external
request, a CDN dependency and an offline hole. The fonts are therefore
committed as woff2 binaries under `assets/fonts/` with their OFL license
texts alongside.

This is a user-approved exception to hard rule 5 (2026-10-10), and its
scope is deliberately narrow: the binaries in `assets/fonts/` plus the
`@font-face` rules at the top of `assets/skin-a.css`. No font CDN, no
build step, no JS font loader. It revisits the 2026-09-11 decision that
kept the study voice on system stacks — cross-device typographic
consistency for a designed skin now outweighs the zero-footprint rule,
but only inside skin A.

## Inventory

Twelve files, exactly these names and sizes (the re-vendor procedure
reuses them; renaming breaks `APP_SHELL` and the `@font-face` srcs):

| File | Size | Contents |
| --- | --- | --- |
| `onest-var-cyrillic.woff2` | 15,828 B | Onest variable, cyrillic subset |
| `onest-var-latin.woff2` | 33,808 B | Onest variable, latin subset |
| `spectral-400-cyrillic.woff2` | 9,404 B | Spectral 400 roman, cyrillic |
| `spectral-400-latin.woff2` | 14,028 B | Spectral 400 roman, latin |
| `spectral-800-cyrillic.woff2` | 9,932 B | Spectral 800 roman, cyrillic |
| `spectral-800-latin.woff2` | 14,328 B | Spectral 800 roman, latin |
| `spectral-i400-cyrillic.woff2` | 10,776 B | Spectral 400 italic, cyrillic |
| `spectral-i400-latin.woff2` | 14,988 B | Spectral 400 italic, latin |
| `spectral-i700-cyrillic.woff2` | 11,788 B | Spectral 700 italic, cyrillic |
| `spectral-i700-latin.woff2` | 16,004 B | Spectral 700 italic, latin |
| `OFL-Onest.txt` | — | Onest license (SIL OFL) |
| `OFL-Spectral.txt` | — | Spectral license (SIL OFL) |

The ten woff2 files total 150,884 B (≈147 KB). Onest ships as a variable
font — one file per subset covers every weight. Spectral has no variable
build on Google Fonts, so it ships as four static instances (400/800
roman, 400/700 italic).

## How to re-vendor

1. Ask the Google Fonts css2 API for the CSS with a woff2-capable
   User-Agent (otherwise it serves legacy TTF/EOF instead of split woff2):

   ```bash
   UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
   curl -A "$UA" "https://fonts.googleapis.com/css2?family=Onest&display=swap"
   curl -A "$UA" "https://fonts.googleapis.com/css2?family=Spectral:ital,wght@0,400;0,800;1,400;1,700&display=swap"
   ```

2. Keep only the `/* cyrillic */` and `/* latin */` blocks from the
   response; delete every other subset block (cyrillic-ext, latin-ext,
   vietnamese, …) — see the subset policy below.
3. Download each remaining `url(...)` to the **exact existing filename**
   from the inventory table (subset + weight + family encoded in the
   name), and rewrite the CSS `src:` to `./fonts/<name>` — relative, per
   hard rule 4; the site lives at a GitHub Pages subpath.
4. Refresh the license texts from `github.com/google/fonts` →
   `ofl/<family>/OFL.txt` into `OFL-Onest.txt` / `OFL-Spectral.txt`.
5. Bump `CACHE_VERSION` in the root `sw.js` (hard rule 9) — the ten woff2
   files are precached in `APP_SHELL` next to `skin-a.css`.

## Subset policy

- Russian content (UI, explanations, glosses) fits the **cyrillic**
  subset, including `ё`.
- German/English target text fits the **latin** subset, including the
  umlauts (ä ö ü) and `ß`.
- **latin-ext is deliberately not vendored.** A character outside the two
  kept ranges falls back to the system font stack for that glyph
  (per-character fallback via `unicode-range`) — it degrades to a system
  face, never to a tofu box and never to an extra download.
- Add a subset only when a real audience needs it: it rides the same
  re-vendor procedure, adds bytes to every precache, and needs an
  inventory row plus a `CACHE_VERSION` bump.

## Where used

- The `@font-face` rules live at the top of `assets/skin-a.css`, pointing
  at `./fonts/<name>` with `font-display: swap`.
- Browsers fetch font files only when a used rule actually references the
  family — since every skin rule is scoped `[data-skin="a"]`, classic
  visitors download zero font bytes over the network; the service worker
  precaches the files so the first switch works offline.
- There are deliberately no preload hints: a `<link rel="preload">` would
  ship skin-A bytes to every classic visitor; `font-display: swap` covers
  the one-time first-switch pop-in instead.
