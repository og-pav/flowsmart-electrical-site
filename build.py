#!/usr/bin/env python3
"""
Flowsmart Electrical — static site generator.
Edit config/copy here and in content.py, then:  python3 build.py
Never hand-edit the generated HTML: the next build wipes it.
"""
import os, re, json, html
from pathlib import Path

ROOT = Path(__file__).parent

# ---------------------------------------------------------------- config ---
SITE = {
    "name":        "Flowsmart Electrical",
    "legal":       "Flowsmart Electrical Pty Ltd",
    "domain":      "https://flowsmartelec.com.au",   # canonical origin, no trailing slash
    "owner":       "Anthony Vella",
    "owner_first": "Anthony",
    "phone":       "0433 348 403",
    "phone_tel":   "+61433348403",
    "email":       "info@flowsmartelec.com.au",
    "street":      "32 Adriana Ct",
    "locality":    "Rowsley",
    "region":      "VIC",
    "postcode":    "3340",
    "lat":         -37.7290,
    "lng":         144.3760,
    "founded":     "2013",
    "rec":         "REC 20672",
    "licence":     "A Class Licence A44962",
    "insurance":   "$5M public liability",
    "ga":          "G-P18HNWECWE",            # GA4 measurement id (live)
    "gsc":         "lYJ4xY5yOkRVsYia_2qcDnOOr3vom4SuJlbe9sTxFf8",  # Search Console verification (live)
    # GoHighLevel form: leave "" to render the styled native form (redirects to
    # thank-you.html). Paste the GHL form id to embed the real inline form.
    "ghl_form_id": "",
    "linkedin":    "https://www.linkedin.com/in/anthony-vella-6346238a/",
    "gbp":         "https://www.google.com/maps/search/?api=1&query=Flowsmart+Electrical+Rowsley+VIC",
    "promise":     "Calls answered or returned within two business hours, seven days a week.",
    "hours_line":  "Mon–Fri 7:00am–8:00pm · Sat–Sun 8:30am–8:00pm",
}
AREAS = ["Melton", "Bacchus Marsh", "Caroline Springs", "Sunshine", "Braybrook",
         "Werribee", "Point Cook", "Hoppers Crossing", "Tarneit", "Truganina",
         "Deer Park", "Ballan"]

# Images. Keys used in content.py as %%IMG:key%%. If localise-assets.sh has
# pulled a copy into assets/img/remote/, the local file is used instead.
IMAGES = {
    # real photos from the existing site (Anthony's own jobs + originals)
    "fse_kitchen":    ("https://flowsmartelec.com.au/wp-content/uploads/2023/05/misc-862342412-480w.jpg", "fse_kitchen.jpg"),
    "fse_sparky":     ("https://flowsmartelec.com.au/wp-content/uploads/2023/05/misc-722215405-480w.jpg", "fse_sparky.jpg"),
    "fse_commercial": ("https://flowsmartelec.com.au/wp-content/uploads/2023/05/misc-556416247-480w.jpg", "fse_commercial.jpg"),
    "fse_switch":     ("https://flowsmartelec.com.au/wp-content/uploads/2023/05/misc-900217718-320w.jpg", "fse_switch.jpg"),
    "kaiser_1":       ("https://flowsmartelec.com.au/wp-content/uploads/2023/05/IMG_1861-640w.jpg", "kaiser_1.jpg"),
    "kaiser_2":       ("https://flowsmartelec.com.au/wp-content/uploads/2023/05/IMG_1864-480w.jpg", "kaiser_2.jpg"),
    "vogue_1":        ("https://flowsmartelec.com.au/wp-content/uploads/2023/05/IMG_1856-e1683691260556.jpg", "vogue_1.jpg"),
    "vogue_2":        ("https://flowsmartelec.com.au/wp-content/uploads/2023/05/IMG_1855.jpg", "vogue_2.jpg"),
    "vogue_3":        ("https://flowsmartelec.com.au/wp-content/uploads/2023/05/IMG_1848-e1683691266133.jpg", "vogue_3.jpg"),
    "vogue_4":        ("https://flowsmartelec.com.au/wp-content/uploads/2023/05/IMG_1850.jpg", "vogue_4.jpg"),
    "vogue_5":        ("https://flowsmartelec.com.au/wp-content/uploads/2023/05/IMG_1851-e1683691273313.jpg", "vogue_5.jpg"),
    "vogue_6":        ("https://flowsmartelec.com.au/wp-content/uploads/2023/05/IMG_1852.jpg", "vogue_6.jpg"),
    "vogue_7":        ("https://flowsmartelec.com.au/wp-content/uploads/2023/05/IMG_1854-e1683691281340.jpg", "vogue_7.jpg"),
    "vogue_8":        ("https://flowsmartelec.com.au/wp-content/uploads/2023/05/IMG_1847.jpg", "vogue_8.jpg"),
    "logo_svg":       ("https://flowsmartelec.com.au/wp-content/uploads/2023/05/FSE_SVG.svg", "fse-logo.svg"),
    "logo_svg_rev":   ("https://flowsmartelec.com.au/wp-content/uploads/2023/05/FSE_SVG_Reversed-03.svg", "fse-logo-reversed.svg"),
    # high-quality supplementary photography (Unsplash CDN, hotlink-intended, no watermark)
    "u_drill":     ("https://images.unsplash.com/photo-1621905251189-08b45d6a269e?auto=format&fit=crop&w=1200&q=80", "u_drill.jpg"),
    "u_ev":        ("https://images.unsplash.com/photo-1593941707882-a5bba14938c7?auto=format&fit=crop&w=1200&q=80", "u_ev.jpg"),
    "u_warehouse": ("https://images.unsplash.com/photo-1553413077-190dd305871c?auto=format&fit=crop&w=1200&q=80", "u_warehouse.jpg"),
    "u_lounge":    ("https://images.unsplash.com/photo-1513694203232-719a280e022f?auto=format&fit=crop&w=1200&q=80", "u_lounge.jpg"),
    "u_pendant":   ("https://images.unsplash.com/photo-1565814329452-e1efa11c5b89?auto=format&fit=crop&w=1200&q=80", "u_pendant.jpg"),
    "u_test":      ("https://images.unsplash.com/photo-1517420704952-d9f39e95b43e?auto=format&fit=crop&w=1200&q=80", "u_test.jpg"),
    "u_office":    ("https://images.unsplash.com/photo-1497366754035-f200968a6e72?auto=format&fit=crop&w=1200&q=80", "u_office.jpg"),
    "u_sparks":    ("https://images.unsplash.com/photo-1504328345606-18bbc8c9d7d1?auto=format&fit=crop&w=1200&q=80", "u_sparks.jpg"),
}

def img_src(key, depth=0):
    url, local = IMAGES[key]
    local_path = ROOT / "assets" / "img" / "remote" / local
    if local_path.exists():
        return rel_prefix(depth) + f"assets/img/remote/{local}"
    return url

def rel_prefix(depth):
    return "../" * depth

# ---------------------------------------------------------------- chrome ---
def wordmark(depth, reversed_=False):
    """Evolved two-tone wordmark derived from the extracted FSE logo
    (lowercase bold, ink + volt green, spark glyph)."""
    tone = "wm-rev" if reversed_ else ""
    return f'''<a class="wordmark {tone}" href="{rel_prefix(depth)}index.html" aria-label="Flowsmart Electrical — home">
  <svg class="wm-spark" viewBox="0 0 24 24" aria-hidden="true"><path d="M13.4 1.5 4.2 13.7h5.3L9 22.5l9.8-13h-5.6l.2-8z"/></svg>
  <span class="wm-text"><b>flowsmart</b><i>electrical</i></span>
</a>'''

def header(page, depth):
    p = rel_prefix(depth)
    links = [(p + "services.html", "Services"), (p + "areas.html", "Areas"),
             (p + "about.html", "About"), (p + "testimonials.html", "Reviews"),
             (p + "blog.html", "Blog"), (p + "contact.html", "Contact")]
    nav = "".join(f'<a class="nav-link" href="{h}">{t}</a>' for h, t in links)
    cta_href = "#quote" if page.get("landing") else p + "contact.html"
    return f'''<header class="site-header" id="top">
  <div class="header-inner">
    {wordmark(depth)}
    <nav class="main-nav" aria-label="Main">{nav}</nav>
    <div class="header-actions">
      <a class="header-phone" href="tel:{SITE['phone_tel']}"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.6 10.8a15.7 15.7 0 0 0 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.2.4 2.4.6 3.7.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1C10.6 21 3 13.4 3 4c0-.6.4-1 1-1h3.4c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.7.1.3 0 .7-.2 1l-2.2 2.1Z"/></svg><span>{SITE['phone']}</span></a>
      <a class="btn btn-volt btn-header" href="{cta_href}">Get a Free Quote</a>
      <button class="nav-burger" aria-label="Open menu" aria-expanded="false"><span></span><span></span><span></span></button>
    </div>
  </div>
  <div class="mobile-nav" hidden>
    <nav aria-label="Mobile">{nav}
      <a class="nav-link" href="tel:{SITE['phone_tel']}">Call {SITE['phone']}</a>
      <a class="btn btn-volt" href="{cta_href}">Get a Free Quote</a>
    </nav>
  </div>
</header>'''

def sticky_cta(page, depth):
    href = "#quote" if page.get("landing") else rel_prefix(depth) + "contact.html"
    return f'''<div class="sticky-cta" role="complementary" aria-label="Quick contact">
  <a class="sc-call" href="tel:{SITE['phone_tel']}">Call {SITE['owner_first']}</a>
  <a class="sc-quote" href="{href}">Get a Free Quote</a>
</div>'''

AREA_PAGES = [
    ("Melton", "areas/electrician-melton.html"),
    ("Bacchus Marsh", "areas/electrician-bacchus-marsh.html"),
    ("Caroline Springs", "areas/electrician-caroline-springs.html"),
    ("Werribee", "areas/electrician-werribee.html"),
    ("Point Cook", "areas/electrician-point-cook.html"),
    ("Sunshine & Braybrook", "areas/electrician-sunshine-braybrook.html"),
]

def footer(page, depth):
    p = rel_prefix(depth)
    areas = " · ".join(f'<a href="{p}{path}">{name}</a>' for name, path in AREA_PAGES)
    return f'''<footer class="site-footer">
  <div class="footer-inner">
    <div class="f-brand">
      {wordmark(depth, reversed_=True)}
      <p class="f-tag">For every bright start.</p>
      <p class="f-meta"><span class="tip" data-tip="Registered Electrical Contractor — checkable on the ESV register">{SITE['rec']}</span> · <span class="tip" data-tip="Victorian A Class electrician licence">{SITE['licence']}</span><br>{SITE['insurance']} · Serving Melbourne&rsquo;s west since {SITE['founded']}</p>
    </div>
    <div class="f-col">
      <h3>Explore</h3>
      <a href="{p}services.html">Services</a>
      <a href="{p}areas.html">Areas we cover</a>
      <a href="{p}case-studies.html">Our Work</a>
      <a href="{p}testimonials.html">Reviews</a>
      <a href="{p}faq.html">FAQ</a>
      <a href="{p}about.html">About Anthony</a>
      <a href="{p}blog.html">Blog</a>
      <a href="{p}contact.html">Contact &amp; directions</a>
    </div>
    <div class="f-col">
      <h3>Services</h3>
      <a href="{p}services/residential-electrician.html">Residential electrical</a>
      <a href="{p}services/switchboard-upgrades.html">Switchboard upgrades</a>
      <a href="{p}services/ev-charger-installation.html">EV charger installation</a>
      <a href="{p}services/commercial-electrical-fitouts.html">Commercial &amp; fitouts</a>
    </div>
    <div class="f-col">
      <h3>Talk to us</h3>
      <a href="tel:{SITE['phone_tel']}">{SITE['phone']}</a>
      <a href="mailto:{SITE['email']}">{SITE['email']}</a>
      <p class="f-hours">{SITE['hours_line']}</p>
      <p class="f-pay">Payment: tap-to-pay card on site, bank transfer or invoice.</p>
      <div class="f-social">
        <a href="{SITE['linkedin']}" rel="noopener" target="_blank" aria-label="Anthony Vella on LinkedIn"><svg viewBox="0 0 24 24"><path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5ZM3 9h4v12H3V9Zm7 0h3.8v1.7h.1c.5-1 1.8-2 3.7-2 4 0 4.7 2.6 4.7 6V21h-4v-5.6c0-1.3 0-3-1.9-3s-2.2 1.4-2.2 2.9V21h-4V9Z"/></svg></a>
        <a href="{SITE['gbp']}" rel="noopener" target="_blank" aria-label="Flowsmart Electrical on Google Maps"><svg viewBox="0 0 24 24"><path d="M12 2a7 7 0 0 0-7 7c0 5.2 7 13 7 13s7-7.8 7-13a7 7 0 0 0-7-7Zm0 9.5A2.5 2.5 0 1 1 12 6a2.5 2.5 0 0 1 0 5.5Z"/></svg></a>
      </div>
    </div>
  </div>
  <div class="footer-fine">
    <p>Servicing {areas} and Melbourne&rsquo;s western suburbs.</p>
    <p>&copy; 2026 {SITE['legal']} · <a href="{p}privacy-policy.html">Privacy</a> · <a href="{p}terms-of-service.html">Terms</a> · ABN on request</p>
  </div>
</footer>
<div class="cookie-bar" hidden role="dialog" aria-label="Cookies">
  <p>We use one analytics cookie to see which pages help people. No ads, no tracking across sites.</p>
  <div><button class="btn btn-ghost" data-cookie="decline">No thanks</button>
  <button class="btn btn-volt" data-cookie="accept">That&rsquo;s fine</button></div>
</div>'''

# ---------------------------------------------------------------- schema ---
def business_node():
    return {
        "@type": "Electrician",
        "@id": SITE["domain"] + "/#business",
        "name": SITE["name"],
        "legalName": SITE["legal"],
        "url": SITE["domain"] + "/",
        "logo": SITE["domain"] + "/assets/img/og-share.png",
        "image": SITE["domain"] + "/assets/img/og-share.png",
        "telephone": SITE["phone_tel"],
        "email": SITE["email"],
        "foundingDate": SITE["founded"],
        "founder": {"@type": "Person", "name": SITE["owner"]},
        "slogan": "For every bright start",
        "priceRange": "$$",
        "paymentAccepted": "Credit card (tap-to-pay on site), EFTPOS, bank transfer, invoice",
        "address": {"@type": "PostalAddress", "streetAddress": SITE["street"],
                    "addressLocality": SITE["locality"], "addressRegion": SITE["region"],
                    "postalCode": SITE["postcode"], "addressCountry": "AU"},
        "geo": {"@type": "GeoCoordinates", "latitude": SITE["lat"], "longitude": SITE["lng"]},
        "areaServed": [{"@type": "City", "name": a} for a in AREAS] +
                      [{"@type": "AdministrativeArea", "name": "Western Melbourne, VIC"}],
        "openingHoursSpecification": [
            {"@type": "OpeningHoursSpecification",
             "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
             "opens": "07:00", "closes": "20:00"},
            {"@type": "OpeningHoursSpecification",
             "dayOfWeek": ["Saturday", "Sunday"], "opens": "08:30", "closes": "20:00"}],
        "sameAs": [SITE["linkedin"]],
        "hasCredential": [SITE["rec"], SITE["licence"], "White Card 22302",
                          "ACRS Master Cabler A032422", "EWPA 355176"],
        "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Electrical services",
            "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": s}}
                for s in ["Switchboard upgrades", "EV charger installation",
                          "Safety switches and RCD testing", "Powerpoints and rewiring",
                          "Lighting, fans and downlights", "Smoke alarm installation",
                          "Commercial fitouts", "Factory and warehouse maintenance",
                          "Rental electrical safety checks"]]},
    }

def breadcrumb_schema(page, depth):
    if page.get("landing") or page.get("noindex"):
        return None
    items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": SITE["domain"] + "/"}]
    pos = 2
    for name, path in page.get("crumbs", []):
        node = {"@type": "ListItem", "position": pos, "name": name}
        if path:
            node["item"] = SITE["domain"] + "/" + path
        items.append(node)
        pos += 1
    items.append({"@type": "ListItem", "position": pos, "name": page["crumb"]})
    return {"@type": "BreadcrumbList", "itemListElement": items}

def faq_schema(faqs):
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q,
         "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}}
        for q, a in faqs]}

def breadcrumb_html(page, depth):
    if page.get("landing") or page.get("no_breadcrumb"):
        return ""
    p = rel_prefix(depth)
    parts = [f'<a href="{p}index.html">Home</a>']
    for name, path in page.get("crumbs", []):
        parts.append(f'<a href="{p}{path}">{name}</a>' if path else f"<span>{name}</span>")
    parts.append(f"<span aria-current='page'>{page['crumb']}</span>")
    sep = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m9 6 6 6-6 6"/></svg>'
    return f'<nav class="breadcrumbs" aria-label="Breadcrumb">{sep.join(parts)}</nav>'

# ------------------------------------------------------------------ shell ---
def render(page):
    depth = page["path"].count("/")
    p = rel_prefix(depth)
    canonical = SITE["domain"] + "/" + ("" if page["path"] == "index.html" else page["path"])
    robots = '<meta name="robots" content="noindex,nofollow">' if page.get("noindex") else ""
    og_img = SITE["domain"] + "/assets/img/og-share.png"
    schema = {"@context": "https://schema.org", "@graph": [business_node()]}
    bc = breadcrumb_schema(page, depth)
    if bc: schema["@graph"].append(bc)
    if page.get("faqs"): schema["@graph"].append(faq_schema(page["faqs"]))
    for extra in page.get("schema_extra", []):
        schema["@graph"].append(extra)
    gsap = ""
    if page.get("landing"):
        gsap = ('<script defer src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>\n'
                '<script defer src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>')
    body_class = "landing" if page.get("landing") else "subpage"
    body = page["body"]
    doc = f'''<!doctype html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(page["title"])}</title>
<meta name="description" content="{html.escape(page["desc"])}">
<link rel="canonical" href="{canonical}">
{robots}
<meta name="google-site-verification" content="{SITE['gsc']}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{SITE['name']}">
<meta property="og:title" content="{html.escape(page["title"])}">
<meta property="og:description" content="{html.escape(page["desc"])}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og_img}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Flowsmart Electrical — licensed electricians, Melbourne's west">
<meta property="og:locale" content="en_AU">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{html.escape(page["title"])}">
<meta name="twitter:description" content="{html.escape(page["desc"])}">
<meta name="twitter:image" content="{og_img}">
<meta name="theme-color" content="#10160F">
<link rel="icon" href="{p}assets/img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{p}assets/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p}assets/css/site.css">
{gsap}
<script defer src="{p}assets/js/site.js"></script>
<!-- GA4 loads only after cookie consent; configured in site.js -->
<script>window.FSE_GA="{SITE['ga']}";</script>
<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>
</head>
<body class="{body_class}" data-page="{page['path']}">
<a class="skip-link" href="#main">Skip to content</a>
{header(page, depth)}
<main id="main">
{breadcrumb_html(page, depth)}
{body}
</main>
{footer(page, depth)}
{sticky_cta(page, depth)}
</body>
</html>'''
    # token substitution
    doc = doc.replace("%%QUOTE_FORM%%", quote_form(page["path"].replace("/", "-")))
    doc = (doc.replace("%%PHONE%%", SITE["phone"])
              .replace("%%TEL%%", SITE["phone_tel"])
              .replace("%%EMAIL%%", SITE["email"])
              .replace("%%OWNER%%", SITE["owner_first"])
              .replace("%%PROMISE%%", SITE["promise"])
              .replace("%%HOURS%%", SITE["hours_line"])
              .replace("%%REL%%", p))
    doc = re.sub(r"%%IMG:([a-z0-9_]+)%%", lambda m: img_src(m.group(1), depth), doc)
    out = ROOT / page["path"]
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(doc, encoding="utf-8")
    return out

# ------------------------------------------------- GHL form / native form ---
def quote_form(variant="landing"):
    """Inline GHL embed when a form id is set; styled native form otherwise.
    The native form validates client-side and redirects to thank-you.html,
    where the generate_lead conversion event fires."""
    if SITE["ghl_form_id"]:
        return f'''<div class="ghl-wrap">
<iframe src="https://api.leadconnectorhq.com/widget/form/{SITE['ghl_form_id']}"
  style="width:100%;height:520px;border:none;border-radius:16px"
  id="inline-{SITE['ghl_form_id']}" data-layout="{{'id':'INLINE'}}"
  data-trigger-type="alwaysShow" data-activation-type="alwaysActivated"
  data-deactivation-type="neverDeactivate" title="Free quote form">
</iframe>
<script src="https://link.msgsndr.com/js/form_embed.js"></script>
</div>'''
    return f'''<form class="quote-form" novalidate data-redirect="thank-you.html" aria-label="Request a free quote">
  <div class="qf-field">
    <label for="qf-name-{variant}">Your name</label>
    <input id="qf-name-{variant}" name="name" type="text" autocomplete="name" required minlength="2" placeholder="Jane Citizen">
    <p class="qf-error">Add your name so %%OWNER%% knows who to ask for.</p>
  </div>
  <div class="qf-field">
    <label for="qf-phone-{variant}">Mobile number</label>
    <input id="qf-phone-{variant}" name="phone" type="tel" inputmode="tel" autocomplete="tel" required pattern="^[\\d\\s()+-]{{8,}}$" placeholder="04xx xxx xxx">
    <p class="qf-error">That number doesn&rsquo;t look right — check the digits.</p>
  </div>
  <div class="qf-field">
    <label for="qf-email-{variant}">Email</label>
    <input id="qf-email-{variant}" name="email" type="email" autocomplete="email" required placeholder="you@email.com.au">
    <p class="qf-error">That email doesn&rsquo;t look complete — check for typos.</p>
  </div>
  <div class="qf-field qf-wide">
    <label for="qf-job-{variant}">What needs doing? <span>(optional)</span></label>
    <textarea id="qf-job-{variant}" name="job" rows="3" placeholder="e.g. Switchboard keeps tripping in Melton — two bedrooms lose power"></textarea>
  </div>
  <button class="btn btn-volt btn-lg qf-submit" type="submit">Get My Free Quote</button>
  <p class="qf-note">%%PROMISE%%</p>
</form>'''

# ------------------------------------------------------------------- main ---
def main():
    import content

    pages = []
    A = pages.append

    A(dict(path="index.html", landing=True,
        title="Flowsmart Electrical | Electricians, Melbourne's West",
        desc="Licensed electricians across Melbourne's west since 2013. Switchboards, EV chargers, rewires, commercial fitouts. Free quotes answered within two business hours.",
        faqs=content.LANDING_FAQS,
        schema_extra=content.review_schema(),
        body=content.landing_body()))

    A(dict(path="services.html", crumb="Services",
        title="Electrical Services | Flowsmart Electrical, Melbourne's West",
        desc="Residential electrical, switchboard upgrades, EV charger installation and commercial fitouts across Melton, Bacchus Marsh and Melbourne's western suburbs.",
        body=content.page_services_hub()))

    A(dict(path="services/residential-electrician.html", crumb="Residential",
        crumbs=[("Services", "services.html")],
        title="Residential Electrician Melton & Melbourne's West | Flowsmart",
        desc="Home electrical done clean and certified: powerpoints, rewires, lighting, fans, smoke alarms and fault-finding across Melton, Bacchus Marsh and the west.",
        faqs=content.RES_FAQS, body=content.page_residential()))

    A(dict(path="services/switchboard-upgrades.html", crumb="Switchboard upgrades",
        crumbs=[("Services", "services.html")],
        title="Switchboard Upgrades Melbourne's West | Flowsmart Electrical",
        desc="Replace old fuse boards with modern boards and safety switches on every circuit. Fixed written quotes, same-day certification, Melbourne's western suburbs.",
        faqs=content.SB_FAQS, body=content.page_switchboards()))

    A(dict(path="services/ev-charger-installation.html", crumb="EV charger installation",
        crumbs=[("Services", "services.html")],
        title="EV Charger Installation Melbourne's West | Flowsmart Electrical",
        desc="Home EV chargers sized to your car, switchboard and tariff. Capacity checks first, clean installs, solar-aware setups. Melton to Point Cook.",
        faqs=content.EV_FAQS, body=content.page_ev()))

    A(dict(path="services/commercial-electrical-fitouts.html", crumb="Commercial & fitouts",
        crumbs=[("Services", "services.html")],
        title="Commercial Electricians & Fitouts, Melbourne's West | Flowsmart",
        desc="Shop fitouts, factory maintenance, three-phase and test & tag across Melbourne's west — scheduled around your trading hours. REC 20672, $5M insured.",
        faqs=content.COM_FAQS, body=content.page_commercial()))

    A(dict(path="about.html", crumb="About",
        title="About Anthony Vella & Flowsmart Electrical | Since 2013",
        desc="The story behind Flowsmart Electrical: 13 years on the tools, a crew of nine at peak, and a deliberate return to one accountable electrician per job.",
        body=content.page_about()))

    A(dict(path="case-studies.html", crumb="Our Work",
        title="Case Studies: Kaisercraft, Vogue Hair Bar & More | Flowsmart",
        desc="Real electrical jobs with photos and the reviews customers wrote afterwards — warehouse fitouts, salon fitouts and residential upgrades in Melbourne's west.",
        schema_extra=content.review_schema(),
        body=content.page_case_studies()))

    A(dict(path="blog.html", crumb="Blog",
        title="Electrical Guides & Straight Answers | Flowsmart Blog",
        desc="Plain-English guides on switchboard costs, EV chargers, safety switches and rental compliance from a licensed Melbourne's-west electrician.",
        body=content.page_blog_hub()))

    for p in content.BLOG_POSTS:
        A(dict(path=f"blog/{p['slug']}.html", crumb=p["h1"],
            crumbs=[("Blog", "blog.html")],
            title=p["title"], desc=p["desc"],
            schema_extra=[{
                "@type": "Article", "headline": p["h1"], "datePublished": p["date"],
                "dateModified": p["date"],
                "author": {"@type": "Person", "name": SITE["owner"]},
                "publisher": {"@id": SITE["domain"] + "/#business"},
                "mainEntityOfPage": SITE["domain"] + f"/blog/{p['slug']}.html",
                "image": SITE["domain"] + "/assets/img/og-share.png"}],
            body=content.blog_post_body(p)))

    A(dict(path="areas.html", crumb="Areas",
        title="Service Areas: Electricians Across Melbourne's West | Flowsmart",
        desc="Local electrician pages for Melton, Bacchus Marsh, Caroline Springs, Werribee, Point Cook, Sunshine and Braybrook — each written from real jobs in that suburb.",
        body=content.page_areas_hub()))

    for a in content.AREA_DATA:
        A(dict(path=f"areas/{a['slug']}.html", crumb=a["name"],
            crumbs=[("Areas", "areas.html")],
            title=a["title"], desc=a["desc"],
            faqs=a["faqs"], body=content.area_page(a)))

    A(dict(path="testimonials.html", crumb="Reviews",
        title="Reviews of Flowsmart Electrical | Verbatim & Verified",
        desc="Real reviews from Flowsmart Electrical customers across Melbourne's west — on time, clean, properly quoted, certified. Every word verbatim.",
        schema_extra=content.review_schema(),
        body=content.page_testimonials()))

    A(dict(path="faq.html", crumb="FAQ",
        title="FAQ: Quotes, Licensing & Common Problems | Flowsmart",
        desc="Every fair question answered straight: response times, free quotes, licences and insurance, certificates, safety switches, switchboards and EV chargers.",
        faqs=content.FAQ_HUB_FLAT,
        body=content.page_faq_hub()))

    A(dict(path="contact.html", crumb="Contact",
        title="Free Quotes: Contact Flowsmart Electrical | 0433 348 403",
        desc="Get a free electrical quote answered within two business hours. Call 0433 348 403, email, or use the 60-second form. Melton, Bacchus Marsh & Melbourne's west.",
        body=content.page_contact()))

    A(dict(path="thank-you.html", crumb="Thank you", noindex=True, no_breadcrumb=True,
        title="Request Received | Flowsmart Electrical",
        desc="Your quote request has landed with Anthony. Expect a call or reply within two business hours, seven days a week, anywhere in Melbourne's west.",
        body=content.page_thank_you()))

    A(dict(path="404.html", crumb="Page not found", noindex=True, no_breadcrumb=True,
        title="Page Not Found | Flowsmart Electrical",
        desc="That page isn't wired in. Jump straight to services, switchboard upgrades, EV chargers, case studies or a free quote from Flowsmart Electrical.",
        body=content.page_404()))

    A(dict(path="privacy-policy.html", crumb="Privacy Policy",
        title="Privacy Policy | Flowsmart Electrical",
        desc="How Flowsmart Electrical collects, uses and protects your personal information — quote details, job records and analytics, under the Australian Privacy Principles.",
        body=content.page_privacy()))

    A(dict(path="terms-of-service.html", crumb="Terms of Service",
        title="Terms of Service | Flowsmart Electrical",
        desc="Plain-English service terms: fixed written quotes, certified work, a 12-month workmanship guarantee and payment by card, transfer or invoice.",
        body=content.page_terms()))

    for page in pages:
        render(page)

    # robots.txt
    (ROOT / "robots.txt").write_text(f"""User-agent: *
Allow: /
Disallow: /thank-you.html
Disallow: /404.html

Sitemap: {SITE['domain']}/sitemap.xml
""", encoding="utf-8")

    # sitemap.xml
    urls = ""
    for page in pages:
        if page.get("noindex"):
            continue
        loc = SITE["domain"] + "/" + ("" if page["path"] == "index.html" else page["path"])
        pr = "1.0" if page["path"] == "index.html" else ("0.9" if page["path"] in ("contact.html", "services.html") else "0.7")
        urls += f"  <url><loc>{loc}</loc><lastmod>2026-08-20</lastmod><priority>{pr}</priority></url>\n"
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + "</urlset>\n",
        encoding="utf-8")

    # llms.txt
    (ROOT / "llms.txt").write_text(f"""# Flowsmart Electrical

> Licensed electrical contractor (REC 20672) serving Melbourne's western suburbs
> since 2013: Melton, Bacchus Marsh, Caroline Springs, Sunshine, Werribee,
> Point Cook, Tarneit and surrounds. Owner-operated by Anthony Vella,
> A Class Licence A44962, $5M public liability insurance.
> Phone {SITE['phone']} · {SITE['email']} · Hours: {SITE['hours_line']}.
> Free quotes answered within two business hours, seven days a week.

## Services
- [Residential electrical]({SITE['domain']}/services/residential-electrician.html): powerpoints, rewires, lighting, smoke alarms, fault-finding
- [Switchboard upgrades]({SITE['domain']}/services/switchboard-upgrades.html): board replacements with RCD safety switches, certified same day
- [EV charger installation]({SITE['domain']}/services/ev-charger-installation.html): 7-22kW home chargers, capacity assessments, solar-aware setups
- [Commercial & fitouts]({SITE['domain']}/services/commercial-electrical-fitouts.html): shop fitouts, factory maintenance, test & tag

## Key pages
- [Free quote / contact]({SITE['domain']}/contact.html)
- [Case studies]({SITE['domain']}/case-studies.html): Kaisercraft warehouse, Vogue Hair Bar
- [Guides]({SITE['domain']}/blog.html): switchboard costs, EV charging, safety switches, rental compliance
""", encoding="utf-8")

    print(f"Built {len(pages)} pages + robots.txt, sitemap.xml, llms.txt")

if __name__ == "__main__":
    main()
