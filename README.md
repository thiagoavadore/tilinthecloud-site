# tilinthecloud.com

Static one-pager for **TilinTheCloud BV**. Plain HTML + CSS, no build step. Visual direction: "Three-Body System" (Clash Display + Switzer, ink ground, copper accent, animated three-body mark).

See [CLAUDE.md](./CLAUDE.md) for positioning, voice rules, and confidentiality constraints.

## Structure

```
index.html            the page (all five sections)
assets/css/style.css  the full visual system
assets/fonts/*.woff2  self-hosted Clash Display + Switzer (no CDN)
assets/favicon.svg    the three-body mark
CNAME                 tilinthecloud.com (GitHub Pages apex)
.nojekyll             serve files as-is, skip Jekyll
robots.txt, sitemap.xml
```

## Run locally

No build. Serve the folder so absolute `/assets/...` paths resolve:

```bash
python3 -m http.server 8000
# open http://localhost:8000
```

## Before going live (placeholders to fill)

1. **Book-a-call link**: in `index.html`, replace `https://cal.com/REPLACE-WITH-YOUR-SCHEDULING-LINK` with your real Cal.com / Calendly / SavvyCal URL. (Search for `REPLACE-WITH`.)
2. **Contact form**: wired to `info@tilinthecloud.com` via [FormSubmit](https://formsubmit.co) (no backend). The **first** real submission triggers a one-time confirmation email to that address; click the link once and it is live. To use a different provider, change the `<form action=...>` only.
3. **Substack**: links point to `https://writing.tilinthecloud.com`. Confirm it resolves before launch.

## Deploy (GitHub Pages, apex domain)

1. Push to `main`, then Settings → Pages → Source: `main` / root.
2. Custom domain: `tilinthecloud.com` (the `CNAME` file already sets this).
3. **DNS at the registrar** (not in this repo):
   - Four `A` records for the apex → `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - One `CNAME` for `www` → `<your-github-username>.github.io`
4. Enable **Enforce HTTPS** once the cert provisions.

> Email MX records are independent. Do not touch them.
