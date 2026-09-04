# Flowsmart Electrical — Website Handover

19 pages, one shared design system, generated from source. Single-page conversion
landing at `/`, with the supporting pages (services with galleries, blog, case
studies, contact, legal, utility) behind it. Built for local organic search and
Google Ads, with `contact.html` doubling as the Ads landing page.

Site by NetWorth Digital.

---

## It is generated, not hand-written

Do not edit the HTML directly — the next build wipes it. Edit the source and rebuild:

```bash
python3 build.py     # regenerates all 19 pages + robots + sitemap + llms.txt
python3 audit.py     # links, schema, titles, meta lengths, alt text, anchors
```

- `build.py` — config (SITE dict), header/footer/shell, schema, page registry
- `content.py` — every word of copy
- `assets/css/site.css`, `assets/js/site.js` — shared by every page
- `make_assets.py` — regenerates og-share.png and the touch icon

Change the phone number in one place (`build.py → SITE`) and 19 pages update.

## Before this goes live — the swap list

| # | Item | Where |
|---|------|-------|
| 1 | **GHL form id.** Currently empty, so a styled native form renders and redirects to `/thank-you.html`. Paste the real form id and rebuild to embed the GHL inline form. | `build.py → SITE["ghl_form_id"]` |
| 2 | **Point the GHL form's redirect at `/thank-you.html`.** That page fires the `generate_lead` event — without the redirect there is no conversion tracking. | GHL form settings |
| 3 | **DONE — GA4 live** (`G-P18HNWECWE`) and **GHL external tracking live** (`tk_c1dbb7f1…`). Both load only after the visitor accepts cookies. | `build.py → SITE`, `assets/js/site.js` |
| 4 | **Google Ads conversion label** on thank-you. | `assets/js/site.js`, commented TODO |
| 5 | **DONE — Search Console verified** and sitemap submitted (26 URLs). Resubmit after any URL change. | `build.py → SITE["gsc"]` |
| 6 | **Run `./localise-assets.sh` before DNS cutover.** Job photos currently hotlink the old WordPress site; when that site is replaced those URLs die. The script pulls every image local and rebuilds. Then compress (WebP ~82% quality ≈ 70% smaller). | project root |
| 7 | **Confirm the email address.** `info@flowsmartelec.com.au` was decoded from the current site's contact page — verify it's monitored. | `build.py → SITE` |
| 8 | **Team photo.** The About page uses a work photo with a marked caption; a real photo of Anthony converts better than almost anything else on a trade site. | `content.py → page_about` |
| 9 | **Facebook / Instagram.** No Flowsmart social pages exist today (only Anthony's LinkedIn, which is linked). When the Meta Ads build creates them, add the URLs to the footer + schema `sameAs`. | `build.py → footer / business_node` |
| 10 | **Braybrook & Melton contract references.** The commercial page and about page reference the 40-factory estate and school maintenance from your discovery notes. Kaisercraft and Vogue Hair Bar were already public on his old site; confirm Anthony is happy naming the others' details before launch. | `content.py` |

## Feature checklist

| Requested | Status |
|-----------|--------|
| Custom 404 page | `/404.html`, animated bolt, links to every key page, noindex |
| CTA above the fold | Every page: header button + hero CTA (verified by audit) |
| Internal links | Service pages ↔ blog ↔ case studies ↔ contact; zero orphans except noindex utility pages |
| Thank-you page | `/thank-you.html`, noindex, fires `generate_lead` |
| Breadcrumbs | Visible + `BreadcrumbList` schema on all non-home pages |
| Case studies | 3 (Kaisercraft, Vogue Hair Bar, "the 45-minute quote") from real jobs/reviews |
| 5 FAQs | 5 per content page (7 on the landing), all with `FAQPage` schema |
| Response time promise | "Answered or returned within two business hours, seven days" — site-wide |
| Sticky mobile CTA | Bottom bar: tap-to-call + quote, all pages |
| robots.txt | Sitemap reference, blocks utility pages |
| Unique page titles | 19 unique, 25–70 chars (audit-enforced) |
| Meta descriptions | 19 unique, 110–165 chars (audit-enforced) |
| Social share image | Generated 1200×630 og-share.png + Twitter card, all pages |
| Maps + directions | Embedded map + directions link on contact |
| Real reviews | 7 verbatim reviews from his current testimonials page, marquee + schema |
| Alt text on images | Every image (audit-enforced) |
| Local schema | `Electrician` type: geo, 12 areaServed suburbs, hours, licences, service catalogue |
| Privacy policy | `/privacy-policy.html` — GA, GHL, APP rights |
| Google Analytics | GA4 consent-gated, placeholder id |
| Team photo | Work photo + marked slot; real portrait pending (see swap list) |
| Sitemap XML | `/sitemap.xml`, 17 indexable URLs |
| Rich tooltips | Hover/focus tooltips on REC, COES, RCD jargon |
| Canonical tags | Absolute canonicals on every page |
| Site favicon | Bolt SVG + apple-touch-icon |
| Type to call | `tel:` links: header, hero, steps, final CTA, footer, sticky bar |
| Number visible | 0433 348 403 across all templates |
| Form error messages | Per-field inline validation with human copy |
| Opening hours | Footer, contact, final CTA + schema `openingHoursSpecification` |
| Google Search Console | Verification meta tag placeholder (see swap list) |
| Five blog posts | Switchboard costs, EV guide, safety switches, rental checks, choosing a sparky — all geo-targeted |
| About page + story | Founding story, the 9-staff/6-vehicle history, licences |
| Gallery per service | Each of the 4 service pages carries a captioned job gallery |
| Visible contact email | info@flowsmartelec.com.au in footer + contact |
| Working social links | LinkedIn (real) + Google Maps; FB/IG pending creation |
| Compressed images | Photos served via CDN params (`q=80/w=1200`); compress locally after `localise-assets.sh` |
| Cookie consent | Banner gates GA; "decline" sets nothing but the choice |
| LLMs.txt | `/llms.txt` summary for AI crawlers |
| TS page | `/terms-of-service.html`, plain English, ACL-aware |
| Clear payment method | Tap-to-pay card / transfer / invoice — footer, contact, terms, benefits |
| Guarantee statement | "We come back and make it right, no charge" + 12-month workmanship — benefits card + terms |

## Consent gating — read before changing tracking

Both GA4 and the GoHighLevel tracker are injected by `assets/js/site.js` **only
after the visitor clicks "That's fine"**. Declining stores the choice, clears any
`_ga`/`_gcl`/`_fbp` cookies from earlier visits, and loads nothing.

GHL's own instructions say to paste the tracking script directly before
`</body>`. It is deliberately not hardcoded there, because the cookie banner and
the privacy policy both promise the visitor a real choice — an unconditional
tracker would make those statements false. If you want it firing for everyone
regardless of consent, move the `FSE_GHL_TRACK` block out of `loadTracking()`
in `site.js` **and** reword the banner and privacy policy to match.

Note also: `.cookie-bar[hidden]` needs `display:none !important`, because the
bar's own `display:flex` otherwise beats the browser's `[hidden]` rule and the
banner never dismisses. That was a real bug; don't remove that line.

## Design system (extracted → evolved)

Extracted from flowsmartelec.com.au: brand green `#86C049` (logo + Elementor
primary), secondary `#333333`, accent `#61CE70` (unused template default),
surfaces `#FFFFFF/#F8F8F8`, Fira Sans headings / Roboto body, flat square
buttons, washed-out stock imagery. Verdict: clean but dated builder-template.

Evolved palette (the green is kept exact — it's his logo):

| Token | Hex | Role |
|-------|-----|------|
| `--volt` | `#86C049` | CTAs and key moments **only** |
| `--volt-deep` | `#6FA53A` | hover, ticks, eyebrows |
| `--spark` | `#B7E36E` | gradient partner, highlights on dark |
| `--ink` | `#10160F` | hero, final CTA, footer (evolved from flat #333) |
| `--pine` | `#2E3B2A` | support green, links |
| `--body-c` / `--mist` | `#3D463B` / `#7C8676` | text / captions |
| `--paper` / `--wash` / `--card` | `#FAFBF7` / `#F1F4EC` / `#FFFFFF` | surfaces |
| `--line` | `#E3E8DE` | borders |

**Type:** Space Grotesk 500–700 (headings, wordmark, buttons) + Inter 400–600
(body) via Google Fonts, with Fira Sans/Roboto as the fallback stack so the old
brand fonts still catch it if the CDN doesn't load.

**Shape/shadow:** 16px cards / 12px small radius / pill CTAs; two-layer soft
shadows (`0 8px 24px rgba(16,22,15,.06)` baseline, three layers on hover).

**Responsive:** fluid by construction — every section pad, gutter, gap and type
size is a `clamp()`, grids collapse at 1080/900/640. This is what fixes the
half-width-window case.

## Animation map (GSAP + IntersectionObserver)

- Hero: staggered fade-up (headline → sub → CTA → proof strip, ~800ms, power3.out);
  slow-drift gradient; floating shapes with mouse parallax (GSAP, pointer:fine only)
- Scroll reveals: every `.rv` fades/translates 28px at ~80% viewport, once:true
  (IntersectionObserver base so it works even if the GSAP CDN fails)
- Images: clip-path reveals (`.rv-clip`), not plain fades
- Steps: oversized outlined numbers scale-settle; icons draw on via dash-offset
- Testimonials: infinite CSS marquee, pauses on hover, duplicated track for a seamless loop
- Buttons: glow ring expands ~10px, brightness lift, scale 1.02, 200ms
- Cards: 5px lift + deepened shadow
- Sticky header: backdrop blur after 80px; nav underline reveals left→right
- Final CTA: 3.6s pulsing glow ring
- All motion behind `prefers-reduced-motion`
- Trailing-dot cursor considered and **skipped** — wrong vibe for a trade site

## SEO recommendations, priority order

1. **Google Business Profile first.** For "electrician near me", GBP outranks any
   website. Claim/verify it, load the gallery photos, keep the review flywheel going.
2. **Match ad headlines to page H1s** — point "Switchboard Upgrade" ad groups at
   `/services/switchboard-upgrades.html`, not the home page. Quality Score follows.
3. **Call tracking.** Most leads will be phone calls; without dynamic number
   insertion you'll optimise against a fraction of conversions.
4. **Suburb pages are the next content build** (Melton, Caroline Springs, Werribee,
   Point Cook) — only with genuinely local content each, or Google treats them as
   doorway pages.
5. **Self-serving review markup doesn't produce stars** — Google ignores
   `aggregateRating` hosted by the business itself; stars come from GBP. Review
   schema here is honest (no invented ratings) and that's deliberate.
6. **The domain decision is baked in as flowsmartelec.com.au.** If Anthony moves to
   flowsmartelectrical.com.au later, change `SITE["domain"]`, rebuild, 301 the old.
