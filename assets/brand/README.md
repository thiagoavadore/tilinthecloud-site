# Brand assets

The tilinthecloud logo: the three-body mark (from the site's "Three-Body System" direction)
joined to the original wordmark. The wordmark is **Nexa Bold**, closed up to one word
**tilinthecloud** ("tilin" orange, "thecloud" charcoal).

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
| Orange | `#F7941D` | "tilin", the mark's core |
| Charcoal | `#414042` | "thecloud", the mark's bodies (light bg) |
| Light orange | `#FFB96C` | secondary / app-tile gradient |
| Ring gray | `#C9CDD2` | the orbit rings (light bg) |

## Font

Wordmark: **Nexa Bold** (Svetoslav Simov, 2012). The source `.otf` is not redistributed here; the
wordmark is shipped as outlines. To re-typeset, install Nexa Bold and re-run the lockup pipeline.

## Regenerating

The lockup is produced by rendering an HTML lockup in Nexa Bold, printing to PDF, and converting to
SVG with `pdftocairo -svg` (which outlines the text). The mark is hand-authored SVG.
