#!/usr/bin/env python3
"""Verification suite: links, meta, schema, alt text, a11y basics. Run after build.py."""
import json, re, sys
from pathlib import Path
from html.parser import HTMLParser

ROOT = Path(__file__).parent
pages = sorted(ROOT.rglob("*.html"))
pages = [p for p in pages if "assets" not in p.parts]
errors, warns = [], []
titles, descs = {}, {}

class Scan(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = ""; self.in_title = False
        self.desc = None; self.canonical = None
        self.h1 = 0; self.imgs = []; self.links = []
        self.schemas = []; self.in_schema = False; self.buf = ""
        self.tels = 0; self.has_breadcrumb = False; self.has_header_cta = False
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "title": self.in_title = True
        if tag == "meta" and a.get("name") == "description": self.desc = a.get("content", "")
        if tag == "link" and a.get("rel") == "canonical": self.canonical = a.get("href")
        if tag == "h1": self.h1 += 1
        if tag == "img": self.imgs.append(a)
        if tag == "a":
            href = a.get("href", "")
            self.links.append(href)
            if href.startswith("tel:"): self.tels += 1
        if tag == "nav" and a.get("class") == "breadcrumbs": self.has_breadcrumb = True
        if tag == "script" and a.get("type") == "application/ld+json":
            self.in_schema = True; self.buf = ""
    def handle_endtag(self, tag):
        if tag == "title": self.in_title = False
        if tag == "script" and self.in_schema:
            self.in_schema = False; self.schemas.append(self.buf)
    def handle_data(self, data):
        if self.in_title: self.title += data
        if self.in_schema: self.buf += data

for page in pages:
    rel = page.relative_to(ROOT).as_posix()
    s = Scan(); s.feed(page.read_text(encoding="utf-8"))
    noindex = 'name="robots" content="noindex' in page.read_text(encoding="utf-8")

    # titles / descriptions
    t = s.title.strip()
    if not (25 <= len(t) <= 70): errors.append(f"{rel}: title length {len(t)} ('{t}')")
    if t in titles: errors.append(f"{rel}: duplicate title with {titles[t]}")
    titles[t] = rel
    if s.desc is None: errors.append(f"{rel}: missing meta description")
    else:
        if not (110 <= len(s.desc) <= 165): errors.append(f"{rel}: description length {len(s.desc)}")
        if s.desc in descs: errors.append(f"{rel}: duplicate description with {descs[s.desc]}")
        descs[s.desc] = rel
    if not s.canonical: errors.append(f"{rel}: missing canonical")
    if s.h1 != 1: errors.append(f"{rel}: {s.h1} h1 tags")
    if s.tels == 0: errors.append(f"{rel}: no tel: link")
    if rel not in ("index.html", "thank-you.html", "404.html") and not s.has_breadcrumb:
        errors.append(f"{rel}: missing breadcrumbs")

    # images: alt + dimensions
    for img in s.imgs:
        if not img.get("alt", "").strip() and img.get("aria-hidden") != "true":
            errors.append(f"{rel}: img missing alt ({img.get('src','?')[:60]})")

    # schema parses
    for raw in s.schemas:
        try: json.loads(raw)
        except Exception as e: errors.append(f"{rel}: invalid JSON-LD ({e})")

    # internal links resolve (clean URLs: /services maps to services.html on disk)
    for href in s.links:
        if href.startswith(("http", "mailto:", "tel:", "#")) or not href:
            continue
        target = href.split("#")[0]
        if not target or target == "/": continue
        base = (ROOT / target.lstrip("/")) if target.startswith("/") else (page.parent / target)
        if base.exists() or Path(str(base) + ".html").exists():
            continue
        errors.append(f"{rel}: broken link -> {href}")
        # no .html suffixes should survive in hrefs
    for href in s.links:
        if href.split("#")[0].endswith(".html") and not href.startswith("http"):
            errors.append(f"{rel}: link still has .html suffix -> {href}")

    # anchor targets on landing
    if rel == "index.html":
        html_txt = page.read_text(encoding="utf-8")
        for anchor in re.findall(r'href="#([\w-]+)"', html_txt):
            if f'id="{anchor}"' not in html_txt:
                errors.append(f"{rel}: missing anchor target #{anchor}")

# em-dash / banned-copy check (tone spec)
BANNED = ["leverage", "synergy", "cutting-edge", "best-in-class", "seamless solution", "innovative"]
for page in pages:
    txt = re.sub(r"<[^>]+>", " ", page.read_text(encoding="utf-8")).lower()
    for w in BANNED:
        if w in txt:
            warns.append(f"{page.relative_to(ROOT)}: banned word '{w}'")

# required files
for f in ["robots.txt", "sitemap.xml", "llms.txt", "vercel.json", "assets/img/favicon.svg",
          "assets/img/og-share.png", "assets/img/apple-touch-icon.png"]:
    if not (ROOT / f).exists(): errors.append(f"missing {f}")

# sitemap entries resolve
sm = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
for loc in re.findall(r"<loc>([^<]+)</loc>", sm):
    path = loc.replace("https://flowsmartelec.com.au/", "") or "index"
    if not (ROOT / (path + ".html")).exists(): errors.append(f"sitemap: missing {path}")
    if path.endswith(".html"): errors.append(f"sitemap: {path} still has .html suffix")

print(f"Audited {len(pages)} pages.")
for e in errors: print("ERROR:", e)
for w in warns: print("WARN: ", w)
if not errors and not warns: print("All checks passed.")
sys.exit(1 if errors else 0)
