#!/usr/bin/env python3
"""Page gates for tilinthecloud.com: forbidden strings, structure, metadata, assets.

Run from the repo root: `python3 scripts/check_pages.py`. Exit 1 on any FAIL.
Stdlib only, no build step (ADR 0002). Replaces the manual T08 checklist.
"""

import re
import struct
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HOME = ROOT / "index.html"
NOT_FOUND = ROOT / "404.html"
LAB = ROOT / "delivery-lab" / "index.html"
SITEMAP = ROOT / "sitemap.xml"
NAMES_FILE = ROOT / "drafts-local" / "forbidden-names.txt"
LAB_URL = "https://tilinthecloud.com/delivery-lab/"
LAB_OG = "https://tilinthecloud.com/assets/brand/social/og-delivery-lab.png"

JARGON = ["leverage", "synergy", "align on", "double-click", "circle back"]
LEAD_WORDS = ["Eduardo", "Stijn", "GDP", "Agentic SDLC Hub"]
COMMERCIAL = ["€", "EUR", "excl. VAT", "procurement", "pilot price"]
UNEARNED = ["proven", "measured", "results show", "case study", "customers report"]
METHOD = ["EBA", "Experience-Based Acceleration"]

failures = []


def report(ok, gate, msg):
    print(f"{'PASS' if ok else 'FAIL'}  {gate}  {msg}")
    if not ok:
        failures.append(f"{gate}: {msg}")


def visible(html):
    """Drop script blocks; the inline motion script legitimately contains '%'."""
    return re.sub(r"<script\b.*?</script>", "", html, flags=re.S)


def block(html, tag):
    m = re.search(rf"<{tag}\b.*?</{tag}>", html, re.S)
    return m.group(0) if m else ""


def last_script(html):
    found = re.findall(r"<script\b.*?</script>", html, re.S)
    return found[-1] if found else ""


def normalise(chrome):
    chrome = chrome.replace(' aria-current="page"', "")
    return re.sub(r"\s+", " ", chrome).strip()


def png_size(path):
    with open(path, "rb") as f:
        head = f.read(24)
    if head[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    return struct.unpack(">II", head[16:24])


def meta(html, attr, key):
    m = re.search(rf'<meta\s+{attr}="{re.escape(key)}"\s+content="([^"]*)"', html)
    return m.group(1) if m else ""


def g1_forbidden(name, html, is_lab):
    text = visible(html)
    low = text.lower()
    report("—" not in text, "G1", f"{name}: no em dash")
    report(" – " not in text, "G1", f"{name}: no en dash used as a dash")
    for w in JARGON:
        report(w not in low, "G1", f"{name}: no '{w}'")
    if not NAMES_FILE.exists():
        report(False, "G1", f"{NAMES_FILE.relative_to(ROOT)} missing; cannot check confidential names")
    else:
        names = [n.strip() for n in NAMES_FILE.read_text().splitlines() if n.strip()]
        for n in names:
            report(n.lower() not in low, "G1", f"{name}: confidential name absent")
    for w in LEAD_WORDS:
        report(w not in text, "G1", f"{name}: no '{w}'")
    for w in COMMERCIAL:
        report(w not in text, "G1", f"{name}: no '{w}'")
    for w in METHOD:
        report(re.search(rf"\b{re.escape(w)}\b", text) is None, "G1", f"{name}: no '{w}'")
    if is_lab:
        stripped = re.sub(r'<span class="proof-item">Rabobank</span>', "", text)
        report("Rabobank" not in stripped, "G1", f"{name}: 'Rabobank' only inside the proof strip")
        for w in UNEARNED:
            report(w not in low, "G1", f"{name}: no '{w}'")
        report("%" not in text, "G1", f"{name}: no percent sign")
        report(re.search(r"\d+\s*x faster", low) is None, "G1", f"{name}: no 'Nx faster'")


def g2_structure(home, lab, nf):
    for name, html in (("index.html", home), ("delivery-lab/index.html", lab)):
        if html is None:
            continue
        report(len(re.findall(r"<h1\b", html)) == 1, "G2", f"{name}: exactly one h1")
    cal = re.search(r'href="(https://calendar\.app\.google/[^"]+)"', home)
    report(cal is not None, "G2", "index.html: calendar link present")
    if lab is not None:
        ids = [m.group(1) for m in re.finditer(r'\bid="([^"]+)"', lab)]
        order = [ids.index(i) if i in ids else -1 for i in ("how", "faq", "contact")]
        report(all(o >= 0 for o in order) and order == sorted(order), "G2", "lab: ids how, faq, contact in order")
        h1 = re.search(r"<h1\b[^>]*>(.*?)</h1>", lab, re.S)
        h1_text = re.sub(r"<[^>]+>", "", h1.group(1)).split() if h1 else []
        report(" ".join(h1_text).startswith("Your developers write code faster"), "G2", "lab: h1 starts with the hero line")
        primary = re.search(r'<a class="btn btn-primary"[^>]*href="([^"]+)"', lab)
        report(bool(cal and primary and primary.group(1) == cal.group(1)), "G2", "lab: primary CTA is the home calendar link")
        report('href="/delivery-lab/"' in block(home, "nav"), "G2", "index.html: nav links to /delivery-lab/")
        what = home.find('id="what"')
        proof = home.find('class="proof"')
        teaser = home.find('class="lab-teaser')
        report(0 < what < teaser < proof, "G2", "index.html: one .lab-teaser between #what and the proof strip")
        report(LAB_URL in SITEMAP.read_text(), "G2", "sitemap.xml lists the lab URL")
        for tag in ("header", "footer"):
            report(normalise(block(home, tag)) == normalise(block(lab, tag)), "G2", f"chrome: <{tag}> identical index vs lab")
        report(normalise(last_script(home)) == normalise(last_script(lab)), "G2", "chrome: inline script identical index vs lab")
    for tag in ("header", "footer"):
        same = normalise(block(home, tag)) == normalise(block(nf, tag))
        print(f"{'PASS' if same else 'WARN'}  G2  chrome: <{tag}> identical index vs 404")


def g3_metadata(name, html, canonical, og_image):
    report(bool(re.search(r"<title>[^<]+</title>", html)), "G3", f"{name}: title")
    desc = meta(html, "name", "description")
    report(0 < len(desc) <= 200, "G3", f"{name}: meta description present and at most 200 chars ({len(desc)})")
    if len(desc) > 160:
        print(f"WARN  G3  {name}: meta description over 160 chars ({len(desc)}), search snippets will truncate")
    report(f'<link rel="canonical" href="{canonical}"' in html, "G3", f"{name}: canonical is {canonical}")
    for key in ("og:title", "og:description", "og:url", "og:image", "og:image:width", "og:image:height"):
        report(bool(meta(html, "property", key)), "G3", f"{name}: {key}")
    ogd = meta(html, "property", "og:description")
    report(0 < len(ogd) < 160, "G3", f"{name}: og:description under 160 chars ({len(ogd)})")
    report(meta(html, "property", "og:image") == og_image, "G3", f"{name}: og:image is {og_image.rsplit('/', 1)[-1]}")
    report(meta(html, "property", "og:image:width") == "1200" and meta(html, "property", "og:image:height") == "630", "G3", f"{name}: og:image 1200x630 declared")
    for key in ("twitter:card", "twitter:image"):
        report(bool(meta(html, "name", key)), "G3", f"{name}: {key}")


def g4_assets(name, html):
    refs = set(re.findall(r'(?:src|href|content)="(?:https://tilinthecloud\.com)?(/assets/[^"?#]+)"', html))
    for ref in sorted(refs):
        report((ROOT / ref.lstrip("/")).is_file(), "G4", f"{name}: {ref} exists")
    for ref in refs:
        if ref.endswith(".png") and "/social/og-" in ref and (ROOT / ref.lstrip("/")).is_file():
            report(png_size(ROOT / ref.lstrip("/")) == (1200, 630), "G4", f"{name}: {ref} is 1200x630")
    for m in re.finditer(r'<(?:a|button) class="btn[^"]*"[^>]*>\s*<svg\b([^>]*)>', html):
        attrs = m.group(1)
        report('width="' in attrs and 'height="' in attrs, "G4", f"{name}: button icon SVG has width/height attributes")


def main():
    home = HOME.read_text()
    nf = NOT_FOUND.read_text()
    lab = LAB.read_text() if LAB.exists() else None
    print(f"pages: index.html, 404.html{', delivery-lab/index.html' if lab else ' (lab page absent)'}")
    g1_forbidden("index.html", home, False)
    g1_forbidden("404.html", nf, False)
    if lab is not None:
        g1_forbidden("delivery-lab/index.html", lab, True)
    g2_structure(home, lab, nf)
    g3_metadata("index.html", home, "https://tilinthecloud.com/", "https://tilinthecloud.com/assets/brand/social/og-cover.png")
    if lab is not None:
        g3_metadata("delivery-lab/index.html", lab, LAB_URL, LAB_OG)
    for name, html in (("index.html", home), ("404.html", nf)) + ((("delivery-lab/index.html", lab),) if lab else ()):
        g4_assets(name, html)
    print()
    if failures:
        print(f"{len(failures)} FAIL")
        for f in failures:
            print(f"  {f}")
        sys.exit(1)
    print("all gates green")


if __name__ == "__main__":
    main()
