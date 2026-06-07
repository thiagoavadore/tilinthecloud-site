# Brand assets

The tilinthecloud logo: the three-body mark (from the site's "Three-Body System" direction)
joined to the original wordmark. The wordmark is **Nexa Bold**, closed up to one word
**tilinthecloud** ("tilin" copper, "thecloud" charcoal).

The wordmark in the SVGs is **outlined to vector paths**, so the files are self-contained and need
no font installed to render (and no Nexa webfont license to use them on the web).

## Files

| File | Use |
|------|-----|
| `tilinthecloud-logo.svg` / `.png` | Primary lockup, for light backgrounds |
| `tilinthecloud-logo-reversed.svg` / `.png` | For dark backgrounds (orange "tilin" + white "thecloud") |
| `tilinthecloud-mark.svg` | The mark only (icon), for avatars / favicons |
| `tilinthecloud-logo-site.svg` | On-site variant, recolored to the site palette (copper + bone) for the dark header. See ADR 0013. |

PNGs are transparent. Regenerate from the SVGs with `rsvg-convert -w <width> in.svg -o out.png`.

## Colors

| Token | Hex | Where |
|-------|-----|-------|
| Copper | `#CC7A3B` | "tilin", the mark's core (matches the site accent) |
| Charcoal | `#414042` | "thecloud", the mark's bodies (light bg) |
| Bone | `#ECE7DB` | "thecloud" / bodies on dark backgrounds |
| Ring gray | `#C9CDD2` | the orbit rings (light bg) |

Unified on copper `#CC7A3B` across the site, the logo files, and social (ADR 0013). The original
Fiverr wordmark was bright orange `#F7941D`, now superseded.

## Font

Wordmark: **Nexa Bold** (Svetoslav Simov, 2012). The source `.otf` is not redistributed here; the
wordmark is shipped as outlines. To re-typeset, install Nexa Bold and re-run the lockup pipeline.

## Regenerating

The lockup is produced by rendering an HTML lockup in Nexa Bold, printing to PDF, and converting to
SVG with `pdftocairo -svg` (which outlines the text). The mark is hand-authored SVG.

## Social / share assets (`social/`)

Raster cards for off-site surfaces, all on the dark brand treatment (ink ground, copper accent,
the three-body mark on its dark variant: `#4E596B` rings, bone bodies, copper core). See ADR 0014.

| File | Size | Use |
|------|------|-----|
| `social/og-cover.png` | 1200×630 | Open Graph / Twitter card. Wired in `index.html` + `404.html`. |
| `social/linkedin-company-logo.png` | 400×400 | LinkedIn **company** logo (mark on ink, circle-crop safe). Replaces the pre-rebrand Fiverr cloud logo. |
| `social/linkedin-company-cover.png` | 1128×191 | LinkedIn **company** cover. Left ~210px kept clear for the logo overlay. |
| `social/linkedin-personal-avatar.png` | 800×800 | Thiago's **personal** profile photo, brand-framed (copper ring + mark badge). |
| `social/linkedin-personal-header.png` | 1584×396 | Thiago's **personal** header. Bottom-left kept clear for the avatar. |

These are not SVG because LinkedIn and OG scrapers only accept raster (PNG/JPG).

**Regenerate:** sources are HTML in `social/src/` (relative paths, self-contained). Faithful webfont
rendering needs headless Chrome, so the pipeline is Chrome `--screenshot` (not `rsvg-convert`, which
can't load woff2). Run:

```sh
assets/brand/social/src/render.sh        # or: CHROME=/path/to/chrome assets/brand/social/src/render.sh
```

It renders each `src/*.html` at 2x and downsamples to the canonical size above. The avatar source
reads `src/headshot.jpg` (Thiago's studio headshot); swap that file to re-cut the avatar.
