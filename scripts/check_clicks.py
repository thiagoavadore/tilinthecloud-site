#!/usr/bin/env python3
"""End-to-end check for assets/js/clicks.js (ADR 0020) in headless Chrome.

Run from the repo root: `python3 scripts/check_clicks.py`. Exit 1 on any FAIL.
Serves the repo over a local http.server, opens a harness page that stubs
GoatCounter, and checks: booking links swap to the channel's calendar, the
form's hidden source field is filled, and clicks produce the right event names.
Then opens the real pages with ?utm_source=linkedin and checks every booking
link. Skips (exit 0) when no Chrome binary is found.
"""

import http.server
import os
import re
import shutil
import socketserver
import subprocess
import sys
import tempfile
import threading
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHROME_CANDIDATES = [
    os.environ.get("CHROME_BIN", ""),
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    shutil.which("google-chrome") or "",
    shutil.which("chromium") or "",
]
CALENDARS = {
    "site": "https://calendar.app.google/FEXpdugSUPuZpBtg6",
    "linkedin": "https://calendar.app.google/bBushU4HFchrVNR48",
    "substack": "https://calendar.app.google/wz5ugX2Letg92BH89",
}

HARNESS = """<!doctype html><html><head><meta charset="utf-8">
<script>
  window.goatcounter = { count: function (o) {
    var el = document.getElementById("events");
    el.textContent += o.path + ";";
  } };
</script>
<script src="/assets/js/clicks.js" defer></script>
</head><body>
<a id="book" href="https://calendar.app.google/FEXpdugSUPuZpBtg6">Book</a>
<a id="mail" href="mailto:info@tilinthecloud.com">Email</a>
<form id="form" action="https://formsubmit.co/x" method="POST">
  <input type="hidden" name="source" value="direct" />
</form>
<pre id="events"></pre>
<script>
  document.addEventListener("click", function (e) { e.preventDefault(); }, true);
  document.addEventListener("submit", function (e) { e.preventDefault(); }, true);
  window.addEventListener("load", function () {
    document.getElementById("book").dispatchEvent(new MouseEvent("click", { bubbles: true, cancelable: true }));
    document.getElementById("mail").dispatchEvent(new MouseEvent("click", { bubbles: true, cancelable: true }));
    document.getElementById("form").dispatchEvent(new Event("submit", { bubbles: true, cancelable: true }));
  });
</script>
</body></html>
"""

failures = []


def report(ok, msg):
    print(f"{'PASS' if ok else 'FAIL'}  {msg}")
    if not ok:
        failures.append(msg)


def find_chrome():
    for c in CHROME_CANDIDATES:
        if c and Path(c).exists():
            return c
    return None


def serve(directory):
    handler_cls = type("Quiet", (http.server.SimpleHTTPRequestHandler,), {"log_message": lambda *a: None})
    srv = socketserver.ThreadingTCPServer(("127.0.0.1", 0), lambda *a, **k: handler_cls(*a, directory=str(directory), **k))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv


def dump_dom(chrome, url):
    # Chrome prints the DOM and then sometimes never exits (a cancelled mailto click keeps
    # it alive), so read what it printed within the budget and kill it.
    with tempfile.TemporaryDirectory() as profile:
        proc = subprocess.Popen(
            [chrome, "--headless=new", "--disable-gpu", "--no-first-run", f"--user-data-dir={profile}",
             "--virtual-time-budget=4000", "--dump-dom", url],
            stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True,
        )
        try:
            out, _ = proc.communicate(timeout=20)
        except subprocess.TimeoutExpired:
            proc.kill()
            out, _ = proc.communicate()
    return out


def attr(html, element_id, name):
    m = re.search(rf'<[^>]*id="{element_id}"[^>]*\b{name}="([^"]*)"', html)
    return m.group(1) if m else ""


def check_harness(chrome, base, query, source):
    html = dump_dom(chrome, f"{base}/harness.html{query}")
    events = re.search(r'<pre id="events">([^<]*)</pre>', html)
    events = events.group(1) if events else ""
    label = query or "(no query)"
    report(attr(html, "book", "href") == CALENDARS.get(source, CALENDARS["site"]), f"harness {label}: booking link is the {source} calendar")
    report(re.search(r'name="source" value="' + re.escape(source) + '"', html) is not None, f"harness {label}: hidden source field is {source}")
    for name in ("click-book", "click-email", "submit-form"):
        report(f"{name}-{source};" in events, f"harness {label}: event {name}-{source}")


def check_page(chrome, base, path):
    html = dump_dom(chrome, f"{base}{path}?utm_source=linkedin")
    hrefs = re.findall(r'href="(https://calendar\.app\.google/[^"]+)"', html)
    report(len(hrefs) > 0 and all(h == CALENDARS["linkedin"] for h in hrefs), f"{path}: all {len(hrefs)} booking links point at the linkedin calendar")


def main():
    chrome = find_chrome()
    if not chrome:
        print("SKIP  no Chrome binary found (set CHROME_BIN); clicks.js not exercised")
        return
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        (tmp / "harness.html").write_text(HARNESS)
        os.symlink(ROOT / "assets", tmp / "assets")
        srv = serve(tmp)
        base = f"http://127.0.0.1:{srv.server_address[1]}"
        try:
            check_harness(chrome, base, "?utm_source=linkedin", "linkedin")
            check_harness(chrome, base, "?utm_source=substack", "substack")
            check_harness(chrome, base, "?utm_source=talk", "talk")
            check_harness(chrome, base, "", "direct")
        finally:
            srv.shutdown()
    srv = serve(ROOT)
    base = f"http://127.0.0.1:{srv.server_address[1]}"
    try:
        check_page(chrome, base, "/")
        check_page(chrome, base, "/delivery-lab/")
    finally:
        srv.shutdown()
    print()
    if failures:
        print(f"{len(failures)} FAIL")
        sys.exit(1)
    print("clicks.js checks green")


if __name__ == "__main__":
    main()
