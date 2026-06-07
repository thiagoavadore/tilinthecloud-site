#!/usr/bin/env bash
# Regenerate the social / share PNGs from the HTML sources in this folder.
# Faithful webfont rendering needs headless Chrome (rsvg-convert can't load woff2).
# Renders at 2x then downsamples to the platform's canonical size for clean anti-aliasing.
#
#   ./render.sh            # uses the default Chrome path below
#   CHROME=/path/to/chrome ./render.sh
set -euo pipefail
SRC="$(cd "$(dirname "$0")" && pwd)"
OUT="$(cd "$SRC/.." && pwd)"
CHROME="${CHROME:-/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}"

render() { # html  win_w  win_h  out_name  final_w
  local html="$1" w="$2" h="$3" out="$4" fw="$5"
  local tmp="$SRC/.tmp-$out"
  "$CHROME" --headless --disable-gpu --hide-scrollbars --force-device-scale-factor=2 \
    --screenshot="$tmp" --window-size="$w,$h" "file://$SRC/$html" >/dev/null 2>&1
  sips --resampleWidth "$fw" "$tmp" --out "$OUT/$out" >/dev/null
  rm -f "$tmp"
  printf "  %-32s %s px wide\n" "$out" "$fw"
}

echo "Rendering social assets -> $OUT"
render og.html                       1200 630  og-cover.png                 1200
render linkedin-company-logo.html     600 600  linkedin-company-logo.png     400
render linkedin-company-cover.html   1128 191  linkedin-company-cover.png   1128
render linkedin-personal-header.html 1584 396  linkedin-personal-header.png 1584
render linkedin-personal-avatar.html  800 800  linkedin-personal-avatar.png  800
echo "Done."
