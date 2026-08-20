# Flowsmart Electrical — all page copy. Rebuild with: python3 build.py
# Tokens: %%PHONE%% %%TEL%% %%EMAIL%% %%OWNER%% %%PROMISE%% %%HOURS%% %%REL%% %%IMG:key%%

# ----------------------------------------------------------------- reviews --
# Verbatim from the current flowsmartelec.com.au testimonials page. Real names.
REVIEWS = [
    ("Colomba", "Anthony was great. I would highly recommend him to anyone. He quoted the job, came on time, was very clean (even removed his shoes) and did some other odd jobs around the house at no extra cost. He was a very pleasant and honest young man. I would use him again without hesitation.", True),
    ("Katrina", "They came and spent 45 minutes quoting, ensuring that all was covered as it was a big job. The workmanship was excellent. I highly recommend that others use this electrician.", False),
    ("Peter", "Excellent service. They made contact several times prior to the job being done and always returned calls promptly. They did a great job and cleaned up any mess. I'm very satisfied.", False),
    ("Vince", "Great guy and professional service. I would recommend them to everyone. Thank you very much, Anthony.", False),
    ("James", "The job was done very well and I'm very happy. Thanks again.", False),
    ("David S.", "Awesome service! Highly recommended.", False),
    ("Dawid K.", "The best!", False),
]

def review_schema():
    return [{
        "@type": "Review",
        "itemReviewed": {"@id": "https://flowsmartelec.com.au/#business"},
        "author": {"@type": "Person", "name": n},
        "reviewBody": b,
    } for n, b, _ in REVIEWS]

def marquee_cards():
    cards = ""
    for name, body, _ in REVIEWS:
        short = body if len(body) < 190 else body[:187].rsplit(" ", 1)[0] + "…"
        cards += f'''<figure class="review-card">
  <div class="stars" aria-label="Five star review">★★★★★</div>
  <blockquote>{short}</blockquote>
  <figcaption><b>{name}</b><span>Verified customer · Melbourne&rsquo;s west</span></figcaption>
</figure>'''
    return cards

# ------------------------------------------------------------------ landing --
LANDING_FAQS = [
    ("Which suburbs do you cover?",
     "Anthony is based just outside Bacchus Marsh and works across Melbourne&rsquo;s west: Melton, Caroline Springs, Sunshine, Braybrook, Werribee, Point Cook, Hoppers Crossing, Tarneit, Ballan and everywhere between. If you&rsquo;re nearby but not on that list, <a href='contact.html'>ask</a> — the answer is usually yes."),
    ("How fast will you get back to me?",
     "Within two business hours, seven days a week. If the call lands while Anthony is up a ladder, you&rsquo;ll get a call back the moment he&rsquo;s down — not Thursday week."),
    ("Do you charge a call-out fee?",
     "Quotes are free. For fault-finding and small repairs there&rsquo;s a standard call-out that&rsquo;s confirmed with you on the phone before anyone drives anywhere — you&rsquo;ll never discover a fee on the invoice."),
    ("Are you licensed and insured?",
     "Yes. Flowsmart Electrical is a Registered Electrical Contractor (REC 20672), Anthony holds a Victorian A Class licence (A44962), and the business carries $5&nbsp;million public liability insurance. Every job is closed out with a Certificate of Electrical Safety."),
    ("Can you install an EV charger at my house?",
     "Yes — home EV charging is one of our most requested jobs. Anthony checks your switchboard capacity first, recommends the right charger for your car and tariff, and installs it to standard. <a href='services/ev-charger-installation.html'>More on EV chargers</a>."),
    ("How do I know if my switchboard needs upgrading?",
     "Ceramic fuses, no safety switches, lights that flicker when the kettle&rsquo;s on, or breakers that trip weekly — any of these means it&rsquo;s worth a look. An old board isn&rsquo;t just annoying, it&rsquo;s the main fire risk in older homes. <a href='blog/switchboard-upgrade-cost-melbourne.html'>What an upgrade costs</a>."),
    ("Do you do commercial and factory work?",
     "All the time — shop fitouts, offices, warehouses and factories, plus ongoing maintenance contracts. See the <a href='case-studies.html'>Kaisercraft warehouse and Vogue Hair Bar fitout</a> for recent examples."),
]

def landing_body():
    faq_items = ""
    for i, (q, a) in enumerate(LANDING_FAQS):
        faq_items += f'''<div class="faq-item rv">
  <button class="faq-q" aria-expanded="false" aria-controls="faq-a{i}">
    <span>{q}</span>
    <svg class="chev" viewBox="0 0 24 24" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg>
  </button>
  <div class="faq-a" id="faq-a{i}"><p>{a}</p></div>
</div>'''

    rows = [
        ("Residential electrical",
         "Your home, sorted end to end",
         "Powerpoints, rewires, fans, downlights and feature lighting, smoke alarms, oven and stove installs, fault-finding — plus the safety checks that catch problems before they cost you. Anthony treats your place like his own. Shoes off at the door is standard, not a favour.",
         ["Powerpoints, rewiring &amp; fault-finding", "Lighting, fans &amp; downlights", "Smoke alarms &amp; safety checks"],
         "services/residential-electrician.html", "See residential work", "%%IMG:u_lounge%%",
         "Warm living room lit by lamps and downlights — the kind of lighting work Flowsmart installs in homes across Melbourne's west"),
        ("Switchboard upgrades &amp; safety",
         "The upgrade that protects everything else",
         "Old boards with ceramic fuses are the biggest electrical fire risk in western-suburbs homes. Flowsmart replaces them with modern boards and safety switches on every circuit — tested, tagged and certified the same day.",
         ["Full board replacements", "Safety switches (RCDs) on every circuit", "Underground mains &amp; metering"],
         "services/switchboard-upgrades.html", "See switchboard work", "%%IMG:u_test%%",
         "Multimeter testing live wiring at a switchboard — every Flowsmart board upgrade is tested circuit by circuit"),
        ("EV charger installation",
         "Charge overnight, drive on sunlight prices",
         "A proper home charger turns an EV from a compromise into a no-brainer. Anthony sizes your switchboard, recommends the right unit for your car and tariff, and installs it clean — cable runs you don&rsquo;t notice, on a circuit that won&rsquo;t trip the house.",
         ["7kW home chargers, single or three phase", "Switchboard capacity assessment", "Off-peak &amp; solar-aware setups"],
         "services/ev-charger-installation.html", "See EV charger installs", "%%IMG:u_ev%%",
         "Electric vehicle plugged into a home charging point — Flowsmart installs EV chargers across Melbourne's west"),
        ("Commercial &amp; factories",
         "Fitouts and maintenance that don&rsquo;t stop trade",
         "From a 40-factory industrial estate to a hair salon fitout finished for opening day, Flowsmart runs commercial jobs around your trading hours, not ours. Cabling, lighting, three-phase power, test-and-tag and scheduled maintenance.",
         ["Shop &amp; office fitouts", "Warehouse &amp; factory maintenance", "Test &amp; tag, compliance, emergency work"],
         "services/commercial-electrical-fitouts.html", "See commercial work", "%%IMG:u_warehouse%%",
         "High-bay lighting in a warehouse aisle — Flowsmart maintains factories and warehouses across the western suburbs"),
    ]
    rows_html = ""
    for i, (kicker, h, body, feats, link, linktext, img, alt) in enumerate(rows):
        feats_html = "".join(f'<li>{f}</li>' for f in feats)
        rows_html += f'''<div class="svc-row {'svc-flip' if i % 2 else ''}">
  <div class="svc-media rv-clip"><img src="{img}" alt="{alt}" loading="lazy" width="1200" height="800"></div>
  <div class="svc-copy rv">
    <p class="eyebrow">{kicker}</p>
    <h3>{h}</h3>
    <p>{body}</p>
    <ul class="ticks">{feats_html}</ul>
    <a class="text-link" href="{link}">{linktext}<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14m-6-6 6 6-6 6"/></svg></a>
  </div>
</div>'''

    return f'''
<!-- 1 · HERO -->
<section class="hero" aria-label="Introduction">
  <div class="hero-bg" aria-hidden="true">
    <span class="hero-shape hs-1" data-depth="18"></span>
    <span class="hero-shape hs-2" data-depth="34"></span>
    <span class="hero-shape hs-3" data-depth="10"></span>
    <span class="hero-grid"></span>
  </div>
  <div class="hero-inner">
    <p class="eyebrow" data-hero>Licensed electricians · Melbourne&rsquo;s west</p>
    <h1 data-hero>Power done properly.<br><em>Answered the first time.</em></h1>
    <p class="hero-sub" data-hero>Thirteen years on the tools across Melton, Bacchus Marsh and Melbourne&rsquo;s west. One electrician who picks up the phone, turns up when he said he would, and leaves your place cleaner than he found it.</p>
    <div class="hero-cta" data-hero>
      <a class="btn btn-volt btn-lg" href="#quote">Get a Free Quote</a>
      <a class="hero-call" href="tel:%%TEL%%">or call %%OWNER%% — %%PHONE%%</a>
    </div>
    <div class="proof-strip" data-hero>
      <span class="proof"><b class="stars">★★★★★</b> 20+ Google reviews</span>
      <span class="proof">Since 2013</span>
      <span class="proof tip" data-tip="Registered Electrical Contractor 20672 — checkable on the Energy Safe Victoria register">REC 20672</span>
      <span class="proof">$5M insured</span>
    </div>
  </div>
</section>

<!-- 2 · THE PROBLEM -->
<section class="problem" id="problem">
  <div class="wrap-narrow">
    <p class="problem-line rv">You call three electricians. One rings back — Thursday week, maybe.</p>
    <p class="problem-line rv">Meanwhile the safety switch keeps tripping, the quote never lands, and a weekend job eats a month.</p>
    <p class="problem-line problem-punch rv">Finding a sparky isn&rsquo;t hard. Finding one who <em>answers, quotes and finishes</em> is.</p>
  </div>
</section>

<!-- 3 · THE SHIFT -->
<section class="shift" id="shift">
  <div class="wrap shift-grid">
    <div class="shift-copy rv">
      <p class="eyebrow">What changes with Flowsmart</p>
      <h2>One number. One bloke who owns the job.</h2>
      <p>No call centres, no subcontractor roulette. You deal with %%OWNER%% from first call to final test — and the little things say the most: he confirms before he drives, covers your floors, takes his shoes off at the door, and doesn&rsquo;t leave until the board is tested and the mess is gone.</p>
      <ul class="shift-list">
        <li class="rv"><b>Answered in hours, not days.</b> %%PROMISE%%</li>
        <li class="rv"><b>Quoted properly.</b> Anthony once spent 45 minutes quoting one job so nothing was missed. The customer wrote a review about it.</li>
        <li class="rv"><b>Certified, every time.</b> A Certificate of Electrical Safety with every job — your proof it&rsquo;s done to standard.</li>
      </ul>
      <a class="btn btn-volt" href="#quote">Get a Free Quote</a>
    </div>
    <div class="shift-media">
      <figure class="shift-img si-1 rv-clip"><img src="%%IMG:u_drill%%" alt="Electrician in safety gear installing a wall fitting" loading="lazy" width="800" height="600"></figure>
      <figure class="shift-img si-2 rv-clip"><img src="%%IMG:fse_sparky%%" alt="Anthony from Flowsmart Electrical working on a home electrical panel" loading="lazy" width="460" height="298"></figure>
      <figure class="shift-img si-3 rv-clip"><img src="%%IMG:fse_kitchen%%" alt="Finished kitchen with clean downlight and appliance wiring by Flowsmart Electrical" loading="lazy" width="460" height="298"></figure>
    </div>
  </div>
</section>

<!-- 4 · HOW IT WORKS -->
<section class="how" id="how">
  <div class="wrap">
    <p class="eyebrow rv">How it works</p>
    <h2 class="rv">Three steps between you and done</h2>
    <div class="steps">
      <article class="step-card rv" style="--d:0ms">
        <span class="step-num" aria-hidden="true">01</span>
        <svg class="step-ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M6.6 10.8a15.7 15.7 0 0 0 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.2.4 2.4.6 3.7.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1C10.6 21 3 13.4 3 4c0-.6.4-1 1-1h3.4c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.7.1.3 0 .7-.2 1l-2.2 2.1Z"/></svg>
        <h3>Tell us the job</h3>
        <p>Sixty seconds on the <a href="#quote">quote form</a>, or call %%PHONE%%. Either way you hear back within two business hours — with real questions, not a script.</p>
      </article>
      <article class="step-card rv" style="--d:120ms">
        <span class="step-num" aria-hidden="true">02</span>
        <svg class="step-ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M9 12h6m-6 4h6M9 8h2m8-5H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V7l-4-4Z"/></svg>
        <h3>Get a real quote</h3>
        <p>Big jobs get a proper on-site look, not a guess over the phone. You get one written price with everything included — and it doesn&rsquo;t move on the invoice.</p>
      </article>
      <article class="step-card rv" style="--d:240ms">
        <span class="step-num" aria-hidden="true">03</span>
        <svg class="step-ico" viewBox="0 0 24 24" aria-hidden="true"><path d="m5 13 4 4L19 7"/></svg>
        <h3>Done &amp; certified</h3>
        <p>On time, floors covered, every circuit tested. You get a <span class="tip" data-tip="Certificate of Electrical Safety — the legal record that the work meets Australian standards">COES certificate</span>, a tidy site, and tap-to-pay on the spot if you want it squared away.</p>
      </article>
    </div>
    <div class="center rv"><a class="btn btn-volt btn-lg" href="#quote">Start with a Free Quote</a></div>
  </div>
</section>

<!-- 5 · SOCIAL PROOF -->
<section class="reviews" id="reviews">
  <div class="wrap">
    <p class="eyebrow rv">Word of mouth, in writing</p>
    <h2 class="rv">The reviews read like this because the jobs go like this</h2>
  </div>
  <figure class="pull-quote rv">
    <blockquote>&ldquo;He quoted the job, came on time, was very clean — even removed his shoes — and did some other odd jobs around the house at no extra cost.&rdquo;</blockquote>
    <figcaption><b>Colomba</b> · Verified customer</figcaption>
  </figure>
  <div class="marquee" data-marquee>
    <div class="marquee-track">{marquee_cards()}</div>
  </div>
  <p class="reviews-foot rv">Verbatim reviews from Flowsmart customers · <a href="case-studies.html">see the jobs behind them</a></p>
</section>

<!-- 6 · SERVICE DEEP-DIVE -->
<section class="services" id="services">
  <div class="wrap">
    <p class="eyebrow rv">What we do</p>
    <h2 class="rv">Four things, done properly</h2>
    {rows_html}
  </div>
</section>

<!-- 7 · BENEFITS GRID -->
<section class="benefits" id="promise-grid">
  <div class="wrap">
    <p class="eyebrow rv">Why people stay</p>
    <h2 class="rv">The boring stuff, guaranteed in writing</h2>
    <div class="bene-grid">
      <article class="bene-card bene-hero rv">
        <h3>The Flowsmart Guarantee</h3>
        <p>If something&rsquo;s not right, %%OWNER%% comes back and makes it right — no charge, no argument. Every job is closed out with a Certificate of Electrical Safety and backed by $5M public liability insurance.</p>
        <a class="btn btn-volt" href="#quote">Get a Free Quote</a>
      </article>
      <article class="bene-card rv"><h3>Two-hour response</h3><p>%%PROMISE%% Missed calls get returned the moment %%OWNER%% is off the tools.</p></article>
      <article class="bene-card rv"><h3>Written quotes that hold</h3><p>The price you approve is the price you pay. Variations only ever happen with your say-so, in writing, before the work.</p></article>
      <article class="bene-card rv"><h3>Licensed &amp; checkable</h3><p><span class="tip" data-tip="Search 'Flowsmart' on the Energy Safe Victoria contractor register to verify">REC 20672</span> · A Class Licence A44962 · ACRS Master Cabler. Look us up before you let anyone near your board — you should do that with every trade.</p></article>
      <article class="bene-card rv"><h3>Clean-site habit</h3><p>Floors covered, shoes off, mess gone. It&rsquo;s in the reviews because it happens on every job, not just the ones being watched.</p></article>
      <article class="bene-card rv"><h3>Easy payment</h3><p>Tap-to-pay card on site, bank transfer or invoice — whatever suits. No deposit for standard residential work.</p></article>
    </div>
  </div>
</section>

<!-- 8 · FAQ -->
<section class="faq" id="faq">
  <div class="wrap-narrow">
    <p class="eyebrow rv">Fair questions</p>
    <h2 class="rv">Things people ask before they book</h2>
    {faq_items}
  </div>
</section>

<!-- 9 · FINAL CTA + INQUIRY -->
<section class="final-cta" id="quote">
  <div class="glow-ring" aria-hidden="true"></div>
  <div class="wrap final-grid">
    <div class="final-copy rv">
      <p class="eyebrow eyebrow-light">Free quote · No obligation</p>
      <h2>One call. One quote.<br>Done properly.</h2>
      <p>Tell %%OWNER%% what needs doing and he&rsquo;ll come back to you within two business hours — seven days a week, %%HOURS%%.</p>
      <a class="final-phone" href="tel:%%TEL%%"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.6 10.8a15.7 15.7 0 0 0 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.2.4 2.4.6 3.7.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1C10.6 21 3 13.4 3 4c0-.6.4-1 1-1h3.4c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.7.1.3 0 .7-.2 1l-2.2 2.1Z"/></svg>%%PHONE%%</a>
      <p class="final-fine">Prefer email? <a href="mailto:%%EMAIL%%">%%EMAIL%%</a></p>
    </div>
    <div class="final-form rv">%%QUOTE_FORM%%</div>
  </div>
</section>'''

# ================================================================ subpages ==

def page_hero(eyebrow, h1, lede, cta_label="Get a Free Quote", cta_href="%%REL%%contact.html"):
    return f'''<section class="page-hero">
  <div class="wrap-narrow">
    <p class="eyebrow">{eyebrow}</p>
    <h1>{h1}</h1>
    <p class="lede">{lede}</p>
    <div class="hero-cta">
      <a class="btn btn-volt btn-lg" href="{cta_href}">{cta_label}</a>
      <a class="hero-call" href="tel:%%TEL%%">or call %%PHONE%%</a>
    </div>
  </div>
</section>'''

def faq_block(faqs, title="Fair questions"):
    items = ""
    for i, (q, a) in enumerate(faqs):
        items += f'''<div class="faq-item rv">
  <button class="faq-q" aria-expanded="false" aria-controls="pfaq-{i}">
    <span>{q}</span>
    <svg class="chev" viewBox="0 0 24 24" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg>
  </button>
  <div class="faq-a" id="pfaq-{i}"><p>{a}</p></div>
</div>'''
    return f'''<section class="faq">
  <div class="wrap-narrow">
    <p class="eyebrow rv">{title}</p>
    <h2 class="rv">Before you book</h2>
    {items}
  </div>
</section>'''

def gallery(items, caption):
    figs = "".join(
        f'''<figure class="g-item rv-clip"><img src="{src}" alt="{alt}" loading="lazy" width="640" height="427"><figcaption>{cap}</figcaption></figure>'''
        for src, alt, cap in items)
    return f'''<section class="gallery-sec">
  <div class="wrap">
    <p class="eyebrow rv">On the tools</p>
    <h2 class="rv">{caption}</h2>
    <div class="gallery-grid">{figs}</div>
  </div>
</section>'''

def cta_band(h="Ready when you are.", sub="Free quote, answered within two business hours."):
    return f'''<section class="cta-band">
  <div class="wrap cta-band-inner">
    <div><h2>{h}</h2><p>{sub}</p></div>
    <div class="cta-band-actions">
      <a class="btn btn-volt btn-lg" href="%%REL%%contact.html">Get a Free Quote</a>
      <a class="hero-call" href="tel:%%TEL%%">%%PHONE%%</a>
    </div>
  </div>
</section>'''

def svc_body(h1, eyebrow, lede, intro_h, intro, ticks, gal_items, gal_caption, faqs, related):
    ticks_html = "".join(f"<li>{t}</li>" for t in ticks)
    rel_html = "".join(f'<a class="chip" href="{h}">{t}</a>' for t, h in related)
    return f'''{page_hero(eyebrow, h1, lede)}
<section class="svc-detail">
  <div class="wrap svc-detail-grid">
    <div class="rv">
      <h2>{intro_h}</h2>
      {intro}
    </div>
    <aside class="svc-side rv">
      <h3>What&rsquo;s included</h3>
      <ul class="ticks">{ticks_html}</ul>
      <p class="side-promise">%%PROMISE%%</p>
    </aside>
  </div>
</section>
{gallery(gal_items, gal_caption)}
{faq_block(faqs)}
<section class="related"><div class="wrap"><p class="eyebrow">Keep reading</p><div class="chips">{rel_html}</div></div></section>
{cta_band()}'''

# ---- residential ----
RES_FAQS = [
    ("Do you do small jobs, or only big ones?",
     "Both. A single powerpoint gets the same booking, the same care and the same certificate as a full rewire. Small jobs are often bundled — customers regularly have Anthony knock over three or four little things in one visit."),
    ("Will you actually turn up on time?",
     "Yes — and you get a confirmation before Anthony drives, so you&rsquo;re never waiting on a maybe. If a job before yours runs long, you hear about it early, not at 5pm."),
    ("Can you find why my safety switch keeps tripping?",
     "That&rsquo;s bread-and-butter fault-finding. It&rsquo;s usually one appliance, one circuit or moisture in a fitting — Anthony isolates it methodically instead of guessing and swapping parts. <a href='../blog/safety-switch-tripping.html'>Why safety switches trip</a>."),
    ("Do I get a certificate for the work?",
     "Every job that requires one gets a Certificate of Electrical Safety (COES). Keep it — it matters for insurance and when you sell."),
    ("Which areas do you cover for home jobs?",
     "Melton, Bacchus Marsh, Caroline Springs, Sunshine, Werribee, Point Cook, Hoppers Crossing, Tarneit, Ballan and the suburbs between. Based just west of Bacchus Marsh, so the western suburbs are the home patch."),
]
def page_residential():
    return svc_body(
        "Residential electrician in Melbourne&rsquo;s west",
        "Residential electrical",
        "Powerpoints to full rewires across Melton, Bacchus Marsh, Caroline Springs and the western suburbs — done clean, done once, certified every time.",
        "Your home, treated like his own",
        '''<p>Most electrical bad experiences aren&rsquo;t about wiring — they&rsquo;re about behaviour. Not answering. Not turning up. Leaving dust in every room. Flowsmart is built on the opposite habits: confirmed bookings, covered floors, shoes off at the door, and a vacuum before the van leaves.</p>
<p>On the technical side, Anthony has thirteen years across every corner of home electrical: rewires in weatherboard originals, new builds and multi-unit developments, fault-finding in homes where three other sparkies gave up, smoke alarm compliance, and the lighting work — fans, downlights, pendants, feature lighting — that changes how a room feels.</p>
<p>If your home still runs on an old board with ceramic fuses, start with the <a href="switchboard-upgrades.html">switchboard page</a> — it&rsquo;s the single upgrade that protects everything else.</p>''',
        ["Powerpoints, USB points &amp; rewiring", "Fans, downlights &amp; feature lighting",
         "Oven, stove &amp; appliance circuits", "Smoke alarms to AS 3786",
         "Safety checks &amp; fault-finding", "New builds &amp; multi-unit developments"],
        [("%%IMG:fse_kitchen%%", "Kitchen with finished downlighting and appliance circuits installed by Flowsmart Electrical", "Kitchen lighting &amp; appliance circuits"),
         ("%%IMG:u_lounge%%", "Living room lamp and wall lighting installed as part of a residential lighting plan", "Living-area lighting plan"),
         ("%%IMG:fse_sparky%%", "Anthony from Flowsmart Electrical fault-finding at a residential switchboard", "Fault-finding at the board"),
         ("%%IMG:u_pendant%%", "Matte pendant light hanging in a renovated room", "Pendant &amp; feature lighting"),
         ("%%IMG:u_drill%%", "Licensed electrician fixing off a wall-mounted installation", "Install work, fixed off properly"),
         ("%%IMG:fse_switch%%", "Modern switchboard with labelled safety switches after an upgrade", "Boards labelled &amp; tested")],
        "Recent residential work",
        RES_FAQS,
        [("Switchboard upgrades", "switchboard-upgrades.html"),
         ("EV charger installation", "ev-charger-installation.html"),
         ("What a switchboard upgrade costs", "../blog/switchboard-upgrade-cost-melbourne.html"),
         ("Rental safety checks in Victoria", "../blog/rental-electrical-safety-checks-victoria.html")])

# ---- switchboards ----
SB_FAQS = [
    ("How do I know my board needs upgrading?",
     "Ceramic fuses, no safety switches, a board that&rsquo;s warm to touch, breakers tripping weekly, or flickering when big appliances start — any one of these is enough to book an inspection. Two or more means don&rsquo;t wait."),
    ("How long does a switchboard upgrade take?",
     "Most single-home upgrades are done in a day, power back on the same evening. Underground mains or metering changes can add time — you&rsquo;ll know from the quote, not on the day."),
    ("Will my power be off the whole time?",
     "Off for the working hours of the swap, yes — that&rsquo;s unavoidable. Anthony schedules around what matters (medical equipment, freezers, work-from-home days) and confirms the outage window before booking."),
    ("Is an old board actually dangerous?",
     "Old rewireable fuse boards don&rsquo;t have RCD protection — the technology that cuts power in milliseconds when current leaks through a person. They&rsquo;re also the most common origin point for house fires in older suburbs. It&rsquo;s the one upgrade Anthony recommends without hesitation."),
    ("What does it cost?",
     "Depends on circuits, mains and metering — see the honest breakdown in <a href='../blog/switchboard-upgrade-cost-melbourne.html'>our switchboard cost guide</a>. You get a fixed written quote before anything is touched."),
]
def page_switchboards():
    return svc_body(
        "Switchboard upgrades in Melbourne&rsquo;s west",
        "Switchboards &amp; safety",
        "Replace the old fuse board before it fails you. Modern boards, safety switches on every circuit, tested and certified the same day.",
        "The upgrade that protects everything else",
        '''<p>Everything electrical in your home passes through one grey box. If that box is thirty years old, running ceramic fuses with no safety switches, then every other job — the new oven, the EV charger, the extra powerpoints — is building on a weak foundation.</p>
<p>A Flowsmart upgrade replaces the lot: modern circuit breakers, <span class="tip" data-tip="Residual Current Devices — safety switches that cut power in under 30 milliseconds when current leaks">RCD protection</span> on every circuit, clear labelling, and surge protection where it earns its keep. Underground mains and metering upgrades are handled in the same visit where needed.</p>
<p>Every board is load-tested circuit by circuit before handover, and you get the Certificate of Electrical Safety on the spot.</p>''',
        ["Full board replacement &amp; relabelling", "Safety switches (RCDs) on every circuit",
         "Surge protection", "Underground mains &amp; consumer mains",
         "Meter isolation &amp; coordination", "Same-day test, tag &amp; certificate"],
        [("%%IMG:fse_switch%%", "Upgraded residential switchboard with labelled safety switches", "After: labelled, protected, certified"),
         ("%%IMG:u_test%%", "Multimeter verification of circuits during a switchboard upgrade", "Every circuit verified under load"),
         ("%%IMG:fse_sparky%%", "Electrician working through circuits at a home switchboard", "Methodical, circuit by circuit"),
         ("%%IMG:u_drill%%", "Electrician mounting hardware during an electrical upgrade", "Mounted, fixed and sealed properly")],
        "Board upgrades, before and after",
        SB_FAQS,
        [("What upgrades cost in 2026", "../blog/switchboard-upgrade-cost-melbourne.html"),
         ("Why safety switches trip", "../blog/safety-switch-tripping.html"),
         ("Residential electrical", "residential-electrician.html"),
         ("EV chargers need board capacity", "ev-charger-installation.html")])

# ---- EV ----
EV_FAQS = [
    ("Can my switchboard handle an EV charger?",
     "That&rsquo;s the first thing Anthony checks — for free, as part of the quote. Many western-suburbs homes need a minor board tidy-up or a dedicated circuit; some need nothing at all. You&rsquo;ll know before you buy a charger."),
    ("Single phase or three phase?",
     "Most homes are single phase, which supports a 7kW charger — a full overnight charge for almost any EV. If you have three phase (or want it), 11–22kW is possible. Anthony sizes it to your car, your driving and your tariff, not to the dearest unit on the shelf."),
    ("Can it charge from my solar?",
     "Yes — several chargers can follow your solar output so you&rsquo;re charging on sunlight instead of the grid. If you have panels, say so in the quote form; it changes the recommendation."),
    ("How long does installation take?",
     "A straightforward install with the board nearby is half a day. Long cable runs or board upgrades extend that — the written quote states the time as well as the price."),
    ("Do you supply the charger or just install it?",
     "Either. Anthony can supply proven units at trade pricing or install one you&rsquo;ve bought — after checking it&rsquo;s compliant and right for your setup."),
]
def page_ev():
    return svc_body(
        "EV charger installation, Melbourne&rsquo;s west",
        "EV charging at home",
        "Wake up to a full battery. Home chargers sized to your car, your board and your tariff — installed clean and certified.",
        "Charge overnight, skip the queue",
        '''<p>Public charging works until it doesn&rsquo;t — the queue, the app, the bay that&rsquo;s ICE&rsquo;d. A home charger ends all of it: plug in at night, leave full every morning, and pay off-peak (or solar) rates instead of public fast-charge prices.</p>
<p>The install matters more than the brand. A charger is a big continuous load — the biggest single appliance most homes will ever add — so Anthony starts at the switchboard: capacity, protection, and a dedicated circuit run cleanly to where the car actually parks. No daisy-chained powerpoints, no cable draped across a wall.</p>
<p>Flowsmart installs across Melton, Caroline Springs, Point Cook, Werribee, Tarneit and the growth suburbs where EVs are landing fastest — read the <a href="../blog/ev-charger-installation-home-guide.html">home charging guide</a> if you&rsquo;re still weighing it up.</p>''',
        ["7kW single-phase &amp; 11–22kW three-phase installs", "Switchboard capacity assessment first",
         "Dedicated protected circuit", "Solar-aware &amp; off-peak configurations",
         "Supply &amp; install or install-only", "COES certificate with every install"],
        [("%%IMG:u_ev%%", "Electric vehicle charging via a wall-mounted home charging point", "Home charging, done properly"),
         ("%%IMG:u_test%%", "Circuit testing before commissioning an EV charger", "Commissioned under load, not guessed"),
         ("%%IMG:fse_switch%%", "Switchboard prepared with a dedicated protected EV circuit", "Dedicated circuit at the board")],
        "EV charging installs",
        EV_FAQS,
        [("The home EV charging guide", "../blog/ev-charger-installation-home-guide.html"),
         ("Switchboard upgrades", "switchboard-upgrades.html"),
         ("What upgrades cost", "../blog/switchboard-upgrade-cost-melbourne.html"),
         ("Residential electrical", "residential-electrician.html")])

# ---- commercial ----
COM_FAQS = [
    ("Do you work around trading hours?",
     "Yes — that&rsquo;s the point. Salon fitouts happen between close and open; factory work slots into planned downtime. The Vogue Hair Bar fitout was finished without costing the owner a single trading day."),
    ("Can you handle three-phase and machinery?",
     "Yes. Factories and warehouses are a big part of the week — three-phase supply, machine circuits, high-bay lighting and the maintenance schedules that keep WorkSafe and your insurer satisfied."),
    ("Do you do test and tag?",
     "Yes — scheduled test-and-tag, RCD trip testing, exit and emergency light checks, all documented so an audit is a formality instead of a scramble."),
    ("Can we put you on a maintenance contract?",
     "That&rsquo;s how most commercial clients use Flowsmart — a schedule that suits the site, priority response between visits, and one contact who already knows your board. Flowsmart currently maintains sites from single shops to a 40-factory estate."),
    ("Are you insured for commercial sites?",
     "$5M public liability, White Card, EWPA licence for elevated work platforms, and ACRS Master Cabler registration for structured cabling. Paperwork available before you ask."),
]
def page_commercial():
    return svc_body(
        "Commercial electricians &amp; fitouts, Melbourne&rsquo;s west",
        "Commercial &amp; industrial",
        "Fitouts, factories and maintenance contracts across the western suburbs — scheduled around your trade, not ours.",
        "Downtime is the real cost. We plan around it.",
        '''<p>Commercial electrical isn&rsquo;t harder than residential — it&rsquo;s less forgiving. A tripped circuit at home is an annoyance; in a salon on a Saturday it&rsquo;s a day of refunds. So Flowsmart plans commercial work backwards from your trading calendar: fitouts staged between close and open, factory work in planned windows, and everything tested before handback.</p>
<p>Anthony has run electrical for shop fitouts, offices, dental practices, restaurants and warehouses — including the full electrical fitout of the Kaisercraft warehouse and ongoing maintenance across a 40-factory industrial estate in Braybrook. See both in the <a href="../case-studies.html">case studies</a>.</p>
<p>For ongoing sites, a maintenance contract gets you scheduled compliance work plus priority response — one sparky who already knows your board beats a stranger reading it cold at emergency rates.</p>''',
        ["Shop, office &amp; hospitality fitouts", "Factory &amp; warehouse maintenance",
         "Three-phase supply &amp; machine circuits", "High-bay &amp; emergency lighting",
         "Test &amp; tag, RCD testing, compliance", "Structured cabling (ACRS Master Cabler)"],
        [("%%IMG:kaiser_1%%", "Warehouse electrical fitout at Kaisercraft by Flowsmart Electrical", "Kaisercraft warehouse fitout"),
         ("%%IMG:kaiser_2%%", "Completed commercial electrical installation inside the Kaisercraft site", "Kaisercraft — completed install"),
         ("%%IMG:vogue_4%%", "Salon lighting and power installed at Vogue Hair Bar", "Vogue Hair Bar fitout"),
         ("%%IMG:vogue_2%%", "Feature lighting at the Vogue Hair Bar salon fitout", "Feature lighting, salon floor"),
         ("%%IMG:u_warehouse%%", "High-bay LED lighting down a warehouse aisle", "High-bay LED conversions"),
         ("%%IMG:u_office%%", "Modern office fitout with glass partitions and integrated lighting", "Office fitouts &amp; partition power")],
        "Commercial jobs on the board",
        COM_FAQS,
        [("Kaisercraft &amp; Vogue case studies", "../case-studies.html"),
         ("Switchboard upgrades", "switchboard-upgrades.html"),
         ("About Anthony", "../about.html"),
         ("Talk through a fitout", "../contact.html")])

# ---- services hub ----
def page_services_hub():
    cards = [
        ("Residential electrical", "Powerpoints to full rewires — clean, certified home electrical.", "services/residential-electrician.html", "%%IMG:fse_kitchen%%", "Finished kitchen electrical work by Flowsmart"),
        ("Switchboard upgrades", "Replace the old fuse board before it fails you.", "services/switchboard-upgrades.html", "%%IMG:fse_switch%%", "Upgraded switchboard with safety switches"),
        ("EV charger installation", "Wake up to a full battery, on off-peak or solar rates.", "services/ev-charger-installation.html", "%%IMG:u_ev%%", "EV charging at a home charge point"),
        ("Commercial &amp; factories", "Fitouts and maintenance scheduled around your trade.", "services/commercial-electrical-fitouts.html", "%%IMG:kaiser_1%%", "Commercial warehouse electrical fitout"),
    ]
    cards_html = "".join(f'''<a class="svc-card rv" href="{h}">
  <div class="svc-card-img"><img src="{img}" alt="{alt}" loading="lazy" width="640" height="420"></div>
  <div class="svc-card-body"><h2>{t}</h2><p>{d}</p><span class="text-link">View service &amp; gallery<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14m-6-6 6 6-6 6"/></svg></span></div>
</a>''' for t, d, h, img, alt in cards)
    return f'''{page_hero("Services", "Electrical services across Melbourne&rsquo;s west",
    "Four core services, one standard: answered fast, quoted in writing, finished certified. Every service page includes a gallery of real jobs.")}
<section class="svc-hub"><div class="wrap svc-hub-grid">{cards_html}</div></section>
{cta_band("Not sure which service you need?", "Describe the job in plain words — %%OWNER%% will tell you what it actually requires.")}'''

# ---- about ----
def page_about():
    return f'''{page_hero("About Flowsmart", "The sparky who answers his phone",
    "Flowsmart Electrical is %%OWNER%% — an A Class licensed electrician who has wired everything from weatherboard rewires to a 40-factory estate since 2013.")}
<section class="about-main">
  <div class="wrap about-grid">
    <div class="about-copy rv">
      <h2>The story</h2>
      <p>Anthony Vella started Flowsmart Electrical in 2013 with a simple observation: the trade wasn&rsquo;t short of good electricians, it was short of electricians who behaved like professionals off the tools. Who answered. Who confirmed. Who cleaned up.</p>
      <p>The name comes from the goal — power that just flows, smartly, without you thinking about it. The tagline, <em>for every bright start</em>, came from the first jobs: new builds and young families getting homes wired for the life ahead of them.</p>
      <p>Since then Flowsmart has grown, shrunk and rebuilt — at its peak running nine staff and six vehicles across Melbourne. Today Anthony has deliberately returned to what made the reviews glow in the first place: one accountable tradesman on your job from quote to certificate, backed by systems that mean no call, quote or invoice slips.</p>
      <p>The work spans both worlds. Weekdays might mean a switchboard in Melton in the morning and factory maintenance in Braybrook after lunch; the client list runs from single-room rewires to the Kaisercraft warehouse fitout and school maintenance contracts. That range is the point — commercial discipline on residential jobs, residential care on commercial ones.</p>
      <h2>Licences &amp; cover</h2>
      <ul class="ticks">
        <li><span class="tip" data-tip="Registered Electrical Contractor — verify on the Energy Safe Victoria register">Registered Electrical Contractor — REC 20672</span></li>
        <li>A Class Electrical Licence A44962</li>
        <li>ACRS Master Cabler A032422 · EWPA 355176 · White Card 22302</li>
        <li>Refrigeration Handling Licence L126432</li>
        <li>$5M public liability insurance · COES with every job</li>
      </ul>
    </div>
    <aside class="about-side">
      <figure class="team-photo rv-clip">
        <img src="%%IMG:fse_sparky%%" alt="Anthony Vella of Flowsmart Electrical working at a residential switchboard" loading="lazy" width="460" height="298">
        <figcaption>%%OWNER%% on the tools. (A proper team photo is coming — Anthony keeps promising to stand still for one.)</figcaption>
      </figure>
      <div class="fact-card rv"><b>2013</b><span>on the tools under the Flowsmart name</span></div>
      <div class="fact-card rv"><b>9 &amp; 6</b><span>staff and vehicles at peak — he knows how to run jobs at scale</span></div>
      <div class="fact-card rv"><b>2 hrs</b><span>maximum response time, seven days a week</span></div>
    </aside>
  </div>
</section>
{faq_block([
 ("Is it really just Anthony?", "Day to day, yes — one accountable electrician, with trusted offsiders brought in for big installs. You always know exactly who was in your roof."),
 ("Why should the peak-years history matter to me?", "Because running nine staff and six vehicles teaches you scheduling, compliance and paperwork discipline that most sole traders never build. You get big-company process with one person&rsquo;s accountability."),
 ("Do you subcontract my job out?", "No. If Flowsmart quotes it, Anthony runs it. Extra hands on large jobs work alongside him, never instead of him."),
 ("What&rsquo;s the service area?", "Based at Rowsley, just west of Bacchus Marsh. The working patch is Melbourne&rsquo;s west — Melton to Point Cook, Ballan to Braybrook — with commercial contracts wider by arrangement."),
 ("How do I verify the licences?", "Search the Energy Safe Victoria public register for REC 20672. Every claim on this page is checkable, which is exactly how it should be."),
], "About the business")}
{cta_band("Talk to Anthony directly.", "No call centre, no sales layer — the person who answers is the person who does the work.")}'''

# ---- case studies ----
def page_case_studies():
    return f'''{page_hero("Our Work", "Case studies from Melbourne&rsquo;s west",
    "Real jobs with the photos to prove them — and the reviews customers wrote afterwards.")}
<section class="cs-list">
  <div class="wrap">
    <article class="cs rv">
      <div class="cs-media rv-clip"><img src="%%IMG:kaiser_1%%" alt="Warehouse electrical installation completed at the Kaisercraft site" loading="lazy" width="640" height="414"></div>
      <div class="cs-body">
        <p class="eyebrow">Commercial · Warehouse</p>
        <h2>Kaisercraft warehouse fitout</h2>
        <p><b>The job:</b> full electrical fitout of a working distribution warehouse — power distribution, lighting layout and compliance — delivered without stopping the pick-and-pack floor.</p>
        <p><b>The approach:</b> staged circuits so racking aisles were never dark during shifts, with switching zoned so the site only lights the aisles in use.</p>
        <p><b>The result:</b> a compliant, energy-sane warehouse and a client that kept trading through the entire install.</p>
      </div>
    </article>
    <article class="cs cs-flip rv">
      <div class="cs-media rv-clip"><img src="%%IMG:vogue_4%%" alt="Salon lighting installed for the Vogue Hair Bar fitout" loading="lazy" width="640" height="427"></div>
      <div class="cs-body">
        <p class="eyebrow">Commercial · Salon fitout</p>
        <h2>Vogue Hair Bar</h2>
        <p><b>The job:</b> complete electrical fitout for a new salon — station power, feature lighting that flatters (a salon lives or dies on its mirrors), three-phase for dryers and hot water.</p>
        <p><b>The approach:</b> lighting temperature tested at the chairs with the owner before final fix, and every install run outside fit-out trading deadlines.</p>
        <p><b>The result:</b> opened on schedule. Eight photos of this job live in the <a href="services/commercial-electrical-fitouts.html">commercial gallery</a>.</p>
      </div>
    </article>
    <article class="cs rv">
      <div class="cs-media rv-clip"><img src="%%IMG:fse_switch%%" alt="Rebuilt residential switchboard from a large home electrical job" loading="lazy" width="460" height="298"></div>
      <div class="cs-body">
        <p class="eyebrow">Residential · Big job, quoted properly</p>
        <h2>The 45-minute quote</h2>
        <p><b>The job:</b> a large multi-part residential upgrade where a rushed quote would have guaranteed variations and arguments later.</p>
        <p><b>The approach:</b> Anthony spent 45 minutes on the walkthrough measuring everything into one fixed written price.</p>
        <p><b>The result:</b> in the customer&rsquo;s words: &ldquo;They came and spent 45 minutes quoting, ensuring that all was covered as it was a big job. The workmanship was excellent. I highly recommend that others use this electrician.&rdquo; — <b>Katrina</b>, verified review.</p>
      </div>
    </article>
  </div>
</section>
{cta_band("Want your job on this page?", "It starts with a free quote and ends with photos we&rsquo;re proud to publish.")}'''

# ---- blog ----
BLOG_POSTS = []  # (slug, title, meta_desc, h1, date, read_mins, teaser, body_html)

def _post(slug, title, desc, h1, date, mins, teaser, body):
    BLOG_POSTS.append(dict(slug=slug, title=title, desc=desc, h1=h1, date=date, mins=mins, teaser=teaser, body=body))

_post("switchboard-upgrade-cost-melbourne",
 "Switchboard Upgrade Cost in Melbourne (2026 Guide) | Flowsmart",
 "What a switchboard upgrade really costs in Melbourne's west in 2026, what moves the price, and the warning signs your old fuse board is due.",
 "What does a switchboard upgrade cost in Melbourne? (2026)",
 "2026-08-10", 6,
 "Real 2026 numbers, what moves the price up or down, and the signs your board is overdue.",
 '''<p>Short answer for Melbourne in 2026: most single-home switchboard upgrades land between <b>$1,500 and $4,000</b>. Where yours falls inside that band comes down to four things — and none of them is a mystery once you know what to look for.</p>
<h2>What moves the price</h2>
<p><b>Circuit count.</b> A two-bedroom unit with eight circuits is a smaller job than a five-bedroom home with ducted air, a pool and a shed. More circuits means more breakers, more safety switches and more testing time.</p>
<p><b>Mains and metering.</b> If your consumer mains are old or undersized — common in Melton and Bacchus Marsh homes built before the 90s — replacing them adds real cost but removes the biggest hidden constraint on everything you add later, including EV chargers.</p>
<p><b>Asbestos panels.</b> Some older boards are mounted on asbestos backing. Safe handling is regulated and priced in — anyone quoting suspiciously low on an old board hasn&rsquo;t looked or isn&rsquo;t telling you.</p>
<p><b>What&rsquo;s behind the board.</b> Occasionally an upgrade uncovers degraded wiring that must be fixed to certify the job. A proper quote includes a look first, which is exactly why <a href="../services/switchboard-upgrades.html">Flowsmart quotes on-site</a> rather than over the phone.</p>
<h2>Signs your board is due</h2>
<p>Ceramic fuses. No safety switches. Breakers that trip weekly. Flickering lights when the kettle or dryer starts. Any warmth or buzzing at the board. A house built before 1990 that&rsquo;s never had the board touched. Two or more of these — book an inspection this month, not this year.</p>
<h2>Why it&rsquo;s the first upgrade, not the last</h2>
<p>Everything else electrical you ever add — induction cooktop, air conditioning, <a href="ev-charger-installation-home-guide.html">EV charger</a>, solar — draws through this one box. Upgrading it first means every later job is smaller, safer and cheaper.</p>
<p>Flowsmart replaces boards across Melton, Caroline Springs, Werribee, Sunshine and Melbourne&rsquo;s west with fixed written quotes and a Certificate of Electrical Safety issued the same day.</p>''')

_post("ev-charger-installation-home-guide",
 "Home EV Charger Installation Guide — Melbourne's West | Flowsmart",
 "Thinking about a home EV charger in Melton, Point Cook or Werribee? Sizing, switchboard capacity, solar setups and what installation involves.",
 "The straight-talk guide to home EV charging in Melbourne's west",
 "2026-07-28", 7,
 "Charger sizing, switchboard capacity, solar smarts — what actually matters before you buy.",
 '''<p>EVs are landing fastest exactly where Flowsmart works — Point Cook, Tarneit, Truganina, Melton. New estates, long commutes, driveways with off-street parking: the western suburbs are built for home charging. Here&rsquo;s what matters before you spend a dollar.</p>
<h2>Start at the switchboard, not the charger</h2>
<p>A 7kW charger is the largest continuous load most homes will ever run — bigger than your oven, longer than your air con. Whether your board can take it depends on your supply capacity and what else runs at night. That assessment comes first; it&rsquo;s free as part of a <a href="../contact.html">Flowsmart quote</a>, and it occasionally saves people from buying a charger their <a href="../services/switchboard-upgrades.html">board can&rsquo;t support</a> yet.</p>
<h2>Charger sizing, honestly</h2>
<p>A standard powerpoint adds roughly 10–15km of range per hour — fine for a plug-in hybrid, painful for a full EV. A 7kW single-phase charger adds 40–50km per hour: empty-to-full overnight for nearly every EV sold in Australia. Three-phase 11–22kW units are quicker again, but for most households they&rsquo;re speed you&rsquo;ll never use — the car sits there all night anyway.</p>
<h2>The solar angle</h2>
<p>If you have panels, a solar-aware charger can throttle itself to match what your roof is exporting, charging the car on power that would otherwise earn you a few cents of feed-in tariff. Over a year that&rsquo;s the difference between charging at roughly free and charging at grid rates.</p>
<h2>What installation involves</h2>
<p>A dedicated circuit from the board to where the car parks, proper RCD protection, a wall-mounted unit fixed and sealed for weather, commissioning under load, and a Certificate of Electrical Safety. Straightforward installs take half a day. The <a href="../services/ev-charger-installation.html">EV charger service page</a> has photos and FAQs.</p>''')

_post("safety-switch-tripping",
 "Why Does My Safety Switch Keep Tripping? | Flowsmart Electrical",
 "A tripping safety switch is doing its job — the question is why. The four usual causes, what you can safely check yourself, and when to call.",
 "Why does my safety switch keep tripping?",
 "2026-07-14", 5,
 "It's protecting you from something. Here's how to work out what — and what to check safely yourself.",
 '''<p>First: a tripping safety switch isn&rsquo;t broken. It&rsquo;s working — cutting power in milliseconds because current is leaking somewhere it shouldn&rsquo;t. The question is what&rsquo;s leaking. In thirteen years of fault-finding across Melbourne&rsquo;s west, it&rsquo;s almost always one of four things.</p>
<h2>1. One faulty appliance</h2>
<p>The most common by far. Kettles, old fridges, cheap phone chargers, anything with a heating element. <b>The safe self-check:</b> unplug everything on the affected circuit, reset the switch, then plug things back one at a time. When it trips again, you&rsquo;ve found your culprit.</p>
<h2>2. Moisture</h2>
<p>Outdoor powerpoints after rain, bathroom fittings, a roof leak dripping onto a junction. If the tripping follows weather, tell your electrician — it shortcuts the diagnosis.</p>
<h2>3. An overloaded or degraded circuit</h2>
<p>Older homes in Melton, Sunshine and Braybrook often run modern appliance loads on circuits sized for 1975. Insulation breaks down, connections loosen, and the leak grows until the switch notices weekly instead of never.</p>
<h2>4. The switch itself</h2>
<p>Rarely, an aged RCD gets over-sensitive. This is a diagnosis of last resort — assume a real fault until testing proves otherwise.</p>
<h2>When to stop DIY-ing</h2>
<p>If the switch won&rsquo;t reset with everything unplugged, trips with no pattern, or any powerpoint is warm, discoloured or buzzing — stop there. That&rsquo;s methodical test-equipment territory, and it&rsquo;s exactly the fault-finding work <a href="../services/residential-electrician.html">Flowsmart does daily</a>. If your board has no safety switches at all, that&rsquo;s the more urgent conversation: <a href="switchboard-upgrade-cost-melbourne.html">start here</a>.</p>''')

_post("rental-electrical-safety-checks-victoria",
 "Rental Electrical Safety Checks in Victoria | Flowsmart",
 "Victorian rentals need an electrical safety check every two years. What the check covers, what it costs landlords in Melbourne's west, and the paperwork.",
 "Rental electrical safety checks in Victoria: what landlords must do",
 "2026-06-30", 6,
 "Every two years, by a licensed electrician, with records kept. What the check actually covers.",
 '''<p>If you own a rental in Victoria, an electrical safety check by a licensed electrician every two years isn&rsquo;t a nice-to-have — it&rsquo;s a compliance obligation under the state&rsquo;s rental minimum standards, and agents increasingly won&rsquo;t manage properties without the paperwork current.</p>
<h2>What the check covers</h2>
<p>A proper check works through the installation, not just the smoke alarms: the switchboard and its protection, safety switch operation (trip-tested, not just looked at), earthing, powerpoints and light fittings, visible wiring condition, and any obvious DIY sins left by previous owners or tenants.</p>
<h2>What you get</h2>
<p>A written record of the check — who did it, licence number, date, what was tested, what passed and anything that needs work. Keep it: you must be able to produce evidence of the most recent check, and it&rsquo;s your first exhibit if anything is ever disputed.</p>
<h2>The traps landlords hit</h2>
<p><b>The two-year clock runs from the last check, not the last tenancy.</b> Changing tenants doesn&rsquo;t reset anything. <b>Old boards fail checks.</b> If your rental still runs ceramic fuses without RCD protection, budget for a <a href="../services/switchboard-upgrades.html">switchboard upgrade</a> rather than paying for a failed check first. <b>Bundling saves money.</b> If you own several properties around Melton, Werribee or Tarneit, batching checks into one run costs less than four separate call-outs.</p>
<h2>What it costs</h2>
<p>For a standard home in Melbourne&rsquo;s west, a compliant check is a modest fixed fee — <a href="../contact.html">ask for the current price</a> — and Flowsmart schedules directly with tenants, provides the compliance record to you or your agent, and diary-flags the next due date so it never lapses.</p>''')

_post("how-to-choose-an-electrician-melbourne-west",
 "How to Choose an Electrician in Melbourne's West | Flowsmart",
 "Five checks that separate a professional electrician from an expensive lesson — licence lookups, quote red flags and the questions worth asking.",
 "How to choose an electrician in Melbourne's west (without getting burned)",
 "2026-06-12", 6,
 "Five checks before anyone touches your board — including the licence lookup that takes 60 seconds.",
 '''<p>Every suburb Facebook group has the thread: &ldquo;anyone know a good sparky?&rdquo; — followed by forty tags and no way to tell them apart. Here are the five checks that actually separate professionals, from someone who&rsquo;s spent thirteen years being compared to the cheapest quote.</p>
<h2>1. Look up the licence — really</h2>
<p>Victoria runs a public register through Energy Safe Victoria. Search the business (Flowsmart is REC 20672) and the individual&rsquo;s licence. Sixty seconds. Anyone cagey about their REC number has answered your question already.</p>
<h2>2. Written quote or no deal</h2>
<p>&ldquo;Should be around eight hundred&rdquo; is not a quote — it&rsquo;s an opening bid you&rsquo;ll renegotiate on the invoice. A professional puts the scope and the number in writing. On bigger jobs, be suspicious of anyone who quotes <em>fast</em>: one Flowsmart customer&rsquo;s review specifically praised a 45-minute quoting walkthrough, because that&rsquo;s what a real fixed price requires.</p>
<h2>3. Ask what certificate you&rsquo;ll get</h2>
<p>Notifiable electrical work in Victoria comes with a Certificate of Electrical Safety. The right answer to &ldquo;will I get a COES?&rdquo; is an unhesitating yes. It protects your insurance and your resale — and its absence protects the person who cut the corner.</p>
<h2>4. Insurance, in numbers</h2>
<p>Public liability should be stated without squirming ($5M is standard for a serious operator). If they&rsquo;re on your roof or in your ceiling, this is not a detail.</p>
<h2>5. Watch the response, not the reviews</h2>
<p>Reviews matter — read <a href="../case-studies.html">ours</a> — but the strongest predictor of how your job will go is how the first 48 hours feel. Did they answer or call back fast? Confirm the visit? Show up when they said? An electrician who is sloppy while trying to win your work will not get sharper after you&rsquo;ve paid a deposit. (Flowsmart&rsquo;s standard: %%PROMISE%%)</p>''')

def page_blog_hub():
    cards = ""
    for p in BLOG_POSTS:
        cards += f'''<a class="post-card rv" href="blog/{p['slug']}.html">
  <p class="post-meta">{p['date']} · {p['mins']} min read</p>
  <h2>{p['h1']}</h2>
  <p>{p['teaser']}</p>
  <span class="text-link">Read the guide<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14m-6-6 6 6-6 6"/></svg></span>
</a>'''
    return f'''{page_hero("The Flowsmart blog", "Straight answers about home &amp; commercial electrical",
    "No filler, no scare tactics — the guides %%OWNER%% wishes every customer read before calling any electrician, including him.")}
<section class="post-list"><div class="wrap post-grid">{cards}</div></section>
{cta_band()}'''

def blog_post_body(p):
    return f'''<article class="post">
  <header class="post-header">
    <div class="wrap-narrow">
      <p class="post-meta">{p['date']} · {p['mins']} min read · By %%OWNER%% Vella, {('REC 20672')}</p>
      <h1>{p['h1']}</h1>
    </div>
  </header>
  <div class="wrap-narrow post-body">{p['body']}</div>
  <div class="wrap-narrow post-cta">
    <div class="post-cta-card">
      <h2>Got this exact problem?</h2>
      <p>%%PROMISE%% Free quotes across Melbourne&rsquo;s west.</p>
      <a class="btn btn-volt" href="../contact.html">Get a Free Quote</a>
      <a class="hero-call" href="tel:%%TEL%%">%%PHONE%%</a>
    </div>
  </div>
</article>'''

# ---- contact ----
def page_contact():
    return f'''{page_hero("Contact · Free quotes", "Tell %%OWNER%% what needs doing",
    "Form, phone or email — whichever suits. Either way: %%PROMISE%%", cta_label="Call %%PHONE%%", cta_href="tel:%%TEL%%")}
<section class="contact-main">
  <div class="wrap contact-grid">
    <div class="contact-form-col rv">
      <h2>Request a free quote</h2>
      %%QUOTE_FORM%%
    </div>
    <aside class="contact-side">
      <div class="side-card rv">
        <h3>Direct lines</h3>
        <p class="big-tel"><a href="tel:%%TEL%%">%%PHONE%%</a></p>
        <p><a href="mailto:%%EMAIL%%">%%EMAIL%%</a></p>
        <p class="side-hours"><b>Hours:</b> %%HOURS%%</p>
        <p><b>Payment:</b> tap-to-pay card on site, bank transfer or invoice.</p>
      </div>
      <div class="side-card rv">
        <h3>Based at Rowsley, working everywhere west</h3>
        <p>32 Adriana Ct, Rowsley VIC 3340 — five minutes from Bacchus Marsh, thirty from the West Gate.</p>
        <p><a class="text-link" href="https://www.google.com/maps/dir/?api=1&amp;destination=32+Adriana+Ct+Rowsley+VIC+3340" target="_blank" rel="noopener">Get directions<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14m-6-6 6 6-6 6"/></svg></a></p>
      </div>
    </aside>
  </div>
  <div class="wrap map-wrap rv">
    <iframe title="Map showing the Flowsmart Electrical service base at Rowsley, Victoria" src="https://maps.google.com/maps?q=32%20Adriana%20Ct%2C%20Rowsley%20VIC%203340&z=11&output=embed" loading="lazy" allowfullscreen referrerpolicy="no-referrer-when-downgrade"></iframe>
  </div>
</section>
{faq_block([
 ("What happens after I submit the form?", "It lands directly with %%OWNER%% — not a call centre. You&rsquo;ll hear back within two business hours with either a price or the two or three questions needed to give you one."),
 ("Can I just text a photo of the problem?", "Absolutely — a photo of the board or the fault often answers half the quoting questions. Text it to %%PHONE%% with your suburb."),
 ("Do you quote over the phone?", "Small, well-defined jobs, yes. Anything structural — switchboards, rewires, fitouts — gets an on-site look so the written price actually holds."),
 ("How far will you travel?", "The core patch is Melbourne&rsquo;s west: Melton, Bacchus Marsh, Caroline Springs, Sunshine, Werribee, Point Cook, Tarneit, Ballan. Further afield for commercial contracts — ask."),
 ("Is the quote really free?", "Yes, including on-site quotes for larger jobs. You&rsquo;re paying for electrical work, not for finding out what it costs."),
])}'''

# ---- thank you ----
def page_thank_you():
    return '''<section class="ty">
  <div class="wrap-narrow ty-inner">
    <svg class="ty-tick" viewBox="0 0 24 24" aria-hidden="true"><path d="m5 13 4 4L19 7"/></svg>
    <h1>Got it. %%OWNER%% is on it.</h1>
    <p class="lede">Your request just landed. Expect a call or reply <b>within two business hours</b> (%%HOURS%%).</p>
    <div class="ty-next">
      <h2>While you wait</h2>
      <ul>
        <li>Snap a photo of the switchboard or the problem area — it speeds up quoting enormously. Text it to <a href="tel:%%TEL%%">%%PHONE%%</a>.</li>
        <li>Urgent? Don&rsquo;t wait for the callback — <a href="tel:%%TEL%%">call now</a>.</li>
        <li>Curious what your job might involve? The <a href="blog.html">guides</a> cover switchboards, EV chargers and safety switches in plain English.</li>
      </ul>
    </div>
    <a class="btn btn-volt" href="index.html">Back to the site</a>
  </div>
</section>'''

# ---- 404 ----
def page_404():
    return '''<section class="e404">
  <div class="wrap-narrow e404-inner">
    <p class="e404-code" aria-hidden="true">4<svg viewBox="0 0 24 24"><path d="M13.4 1.5 4.2 13.7h5.3L9 22.5l9.8-13h-5.6l.2-8z"/></svg>4</p>
    <h1>This circuit&rsquo;s dead.</h1>
    <p class="lede">The page you&rsquo;re after has been moved, renamed or never wired in. Everything that matters is one click away:</p>
    <div class="chips">
      <a class="chip" href="index.html">Home</a>
      <a class="chip" href="services/residential-electrician.html">Residential</a>
      <a class="chip" href="services/switchboard-upgrades.html">Switchboards</a>
      <a class="chip" href="services/ev-charger-installation.html">EV chargers</a>
      <a class="chip" href="services/commercial-electrical-fitouts.html">Commercial</a>
      <a class="chip" href="case-studies.html">Our work</a>
      <a class="chip" href="blog.html">Blog</a>
      <a class="chip" href="contact.html">Contact</a>
    </div>
    <p>Or skip the clicking: <a href="tel:%%TEL%%">%%PHONE%%</a></p>
  </div>
</section>'''

# ---- privacy ----
def page_privacy():
    return '''<section class="legal"><div class="wrap-narrow">
<h1>Privacy Policy</h1>
<p class="post-meta">Flowsmart Electrical Pty Ltd · Last updated August 2026</p>
<p>Flowsmart Electrical collects only the personal information needed to quote, schedule and complete electrical work, and to stay in contact about it. In practice that means your name, phone number, email address, property address and a description of the job.</p>
<h2>What we collect and why</h2>
<p><b>Quote form and contact details.</b> When you submit the quote form, your details go into our customer management system (GoHighLevel) so your inquiry is tracked and answered rather than lost in a phone. They are used to contact you about your job — not for unrelated marketing lists, and never sold.</p>
<p><b>Job records.</b> We keep records of work performed, quotes, invoices and Certificates of Electrical Safety. Some of this we are required to retain for compliance purposes.</p>
<p><b>Website analytics.</b> With your consent (the cookie banner), the site uses Google Analytics 4 to understand which pages help people. Analytics data is aggregated; we don&rsquo;t use it to identify you. Decline the banner and no analytics cookie is set.</p>
<h2>How it&rsquo;s stored</h2>
<p>Customer records live in access-controlled systems (GoHighLevel CRM, accounting software). We take reasonable steps to protect information from misuse, loss and unauthorised access. Some providers store data outside Australia; we choose reputable providers with equivalent protections.</p>
<h2>Your rights</h2>
<p>Under the Australian Privacy Principles you can ask what personal information we hold about you, ask for it to be corrected, or ask for it to be deleted where the law doesn&rsquo;t require us to keep it. Email <a href="mailto:%%EMAIL%%">%%EMAIL%%</a> and we&rsquo;ll respond within 30 days.</p>
<h2>Contact</h2>
<p>Privacy questions or complaints: <a href="mailto:%%EMAIL%%">%%EMAIL%%</a> or %%PHONE%%. If you&rsquo;re not satisfied with our response, you can contact the Office of the Australian Information Commissioner (oaic.gov.au).</p>
</div></section>'''

# ---- terms ----
def page_terms():
    return '''<section class="legal"><div class="wrap-narrow">
<h1>Terms of Service</h1>
<p class="post-meta">Flowsmart Electrical Pty Ltd · Last updated August 2026</p>
<h2>Quotes</h2>
<p>Written quotes are fixed for the scope described and valid for 30 days. If something unforeseeable emerges once work begins (for example concealed wiring damage), any variation is put to you in writing, with a price, before the additional work proceeds. No verbal variations, in either direction.</p>
<h2>Doing the work</h2>
<p>All work is performed by or under the direct supervision of a licensed A Class electrician, in accordance with AS/NZS 3000 (the Wiring Rules). Notifiable work is certified with a Certificate of Electrical Safety supplied to you on completion. Flowsmart holds $5M public liability insurance; documentation is available on request.</p>
<h2>Payment</h2>
<p>Standard residential work is payable on completion — tap-to-pay card on site, bank transfer or invoice with 7-day terms. Commercial and contract work is invoiced per the agreed schedule. Materials for large jobs may require a deposit, stated on the quote.</p>
<h2>Workmanship guarantee</h2>
<p>If our workmanship is not right, we return and make it right at no charge. This guarantee covers workmanship for 12 months from completion and sits alongside — never instead of — your rights under the Australian Consumer Law, including consumer guarantees that cannot be excluded.</p>
<h2>Access &amp; safety</h2>
<p>You agree to provide safe access to the work area. Anthony may pause work if a site condition is unsafe (live hazards, asbestos disturbance, unrestrained dogs with opinions) until it&rsquo;s resolved together.</p>
<h2>Cancellations</h2>
<p>Life happens — reschedule with a day&rsquo;s notice at no cost. Repeated same-day cancellations may incur a call-out fee, which we&rsquo;ll tell you about before rebooking, not after.</p>
<h2>Questions</h2>
<p><a href="mailto:%%EMAIL%%">%%EMAIL%%</a> · %%PHONE%%</p>
</div></section>'''
