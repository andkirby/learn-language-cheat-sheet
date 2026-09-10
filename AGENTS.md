# AGENTS.md

Multi-language PWA cheatsheet hub: German and English grammar for
Russian-speaking learners (A1–B1). Static site on GitHub Pages — no build
step, no external dependencies, everything works offline.

## Structure

```
index.html          landing (language cards)
deutsch/            German page + its manifest, icons, SITE_PLAN.md
english/            English page + its manifest, icons, SITE_PLAN.md
sw.js               shared service worker (root scope, all languages)
icons/              landing favicon + og image
tools/make_icons.py icon generator (stdlib only)
docs/ADD_LANGUAGE.md  playbook for adding a new language
```

## Source-of-truth map

| Question | Read this first |
|---|---|
| How to add a new language | `docs/ADD_LANGUAGE.md` |
| One language's scope/content/update rules | `deutsch/SITE_PLAN.md` / `english/SITE_PLAN.md` |
| Design tokens, components, a11y rules | `.design/DESIGN_SYSTEM.md` |
| Why a UI decision was made | `.design/decisions.md` |
| Known open/deferred UI issues | `UI_AUDIT.md` |
| Deployment / GitHub Pages | `README.md` |

## Hard rules

1. Each language is **self-contained** in its folder; shared things live at
   the root. Don't cross-reference assets between language folders.
2. A language's `SITE_PLAN.md` is updated **before** its page when
   scope/coverage/interaction changes (its update protocol applies).
3. All asset paths relative (`./…`, `../sw.js`) — the site lives at a GitHub
   Pages subpath.
4. No build tools, frameworks, fonts, or CDNs.
5. Colors only via semantic tokens (light **and** dark + manual-dark blocks)
   — see `.design/DESIGN_SYSTEM.md`. Theme toggle is part of the contract.
6. Keep section anchor ids stable within a language.
7. New tappable explanations go into that page's `DETAILS` object; cards stay
   concise, depth goes in dialogs.
8. After changing any page or asset: bump `CACHE_VERSION` in the root `sw.js`
   and add any new shell URLs to its `APP_SHELL`.
9. A UI change that touches the shared contract is applied to **every**
   language page in the same commit and logged in `.design/decisions.md`.

## Verify before declaring done

```bash
python3 -m http.server 8931   # open http://127.0.0.1:8931/
```

- Landing loads, language cards link to `./deutsch/`, `./english/`.
- No console errors on any page; manifests, icons, `sw.js` resolve.
- At ~390px: no horizontal page overflow; tables scroll inside `.table-scroll`.
- Theme toggle cycles авто → светлая → тёмная, persists across reload.
- Search filters cards and restores on clear; dialogs close via ×, Escape,
  backdrop; practice reveal works.
- Offline reload works after first load.
- Live check after push: `https://andkirby.github.io/learn-language-cheat-sheet/`
  (+ `/deutsch/`, `/english/`; `/deutsch.html` redirects).

## Regenerating icons

```bash
python3 tools/make_icons.py                    # all sets (Aa, DE, EN)
python3 tools/make_icons.py --mark IT --out ital   # new language (see docs/)
```
Then bump `CACHE_VERSION` in `sw.js`.
