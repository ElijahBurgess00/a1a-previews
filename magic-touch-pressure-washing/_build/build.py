# -*- coding: utf-8 -*-
"""Magic Touch Pressure Washing preview, built on the A1A house template
(Coastal Valley Charters chassis: promo bar, split hero, fact bar, photo wall,
card grids, ledger, book prompt, owner split, location panels, who grid,
list split, 3-step rail, FAQ accordion, CTA band, 4-column footer, sticky
mobile bar, desktop nudge). Static output with relative links so it runs
under previews.a1amarketingco.com/magic-touch-pressure-washing/.
Run: python3 _build/build.py"""
import html, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PHONE = "(321) 355-9521"
TEL = "+13213559521"
SMS = "sms:+13213559521"
EMAIL = "Magictouchpw7@gmail.com"
IG = "https://www.instagram.com/magictouchpw_/"
FB = "https://www.facebook.com/p/Magic-Touch-Pressure-Washing-100075876025896/"
NAME = "Magic Touch Pressure Washing"
EST = "estimate/"

ICON = {
    "clock": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" aria-hidden="true"><circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="2"/><path d="M12 7v5l3 2" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>',
    "pin": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M12 21s-7-4.5-7-10a7 7 0 0 1 14 0c0 5.5-7 10-7 10z" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/><circle cx="12" cy="11" r="2.5" stroke="currentColor" stroke-width="2"/></svg>',
    "phone": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M5 4h3l2 5-2 1a12 12 0 0 0 5 5l1-2 5 2v3a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>',
    "mail": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" aria-hidden="true"><rect x="3" y="5" width="18" height="14" stroke="currentColor" stroke-width="2"/><path d="M3 6l9 7 9-7" stroke="currentColor" stroke-width="2"/></svg>',
    "ig": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" aria-hidden="true"><rect x="3" y="3" width="18" height="18" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="2"/><circle cx="17.5" cy="6.5" r="1.2" fill="currentColor"/></svg>',
    "fb": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" aria-hidden="true"><rect x="3" y="3" width="18" height="18" stroke="currentColor" stroke-width="2"/><path d="M15.5 8H14a2 2 0 0 0-2 2v11M9.5 13h6" stroke="currentColor" stroke-width="2"/></svg>',
    "caret": '<svg class="caret" width="12" height="12" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M6 9l6 6 6-6" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "arrow": '<svg class="arrow" width="18" height="18" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M4 12h15M13 6l6 6-6 6" stroke="currentColor" stroke-width="2.2" stroke-linecap="square"/></svg>',
    "check": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M4 12.5l5 5L20 6.5" stroke="currentColor" stroke-width="2.6" stroke-linecap="square"/></svg>',
    "shield": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6l8-3z" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/></svg>',
}

# ------------------------------------------------------------------ content
SERVICES = [
    dict(slug="roof-soft-washing", name="Roof Soft Washing", short="Roofs", chip="Low pressure",
         desc="Black streaks, algae and lichen make a roof look years older than it is. Magic Touch soft washes roofs clean with low pressure, safe for shingle, tile and metal.",
         prose=["Those dark streaks on Central Florida roofs are algae, and the heat and humidity here help it spread fast. Blasting a roof with high pressure can strip granules and damage shingles, so Magic Touch uses a soft wash instead: a low-pressure application of cleaning solution that treats the growth, followed by a gentle rinse.",
                "The crew protects plants and landscaping before the roof is treated, rinses down the gutters, walkways and anything below the roofline, and walks the finished job with the homeowner before leaving."],
         suits=["Shingle, tile and metal roofs with black streaks", "Roofs with moss, lichen or mildew", "Homes getting ready to sell or host guests"],
         faq=[("Will soft washing damage my roof?", "Soft washing uses low pressure rather than a high-pressure blast, which is why it is the method Magic Touch uses on shingle, tile and metal roofs."),
              ("What causes the black streaks?", "The dark streaks on Florida roofs are usually algae. Heat, humidity and shade help it grow, and soft washing treats it at the source.")],
         pair="house-washing"),
    dict(slug="house-washing", name="House Washing", short="Homes", chip="Soft wash",
         desc="Stucco, siding, soffits and screen enclosures cleaned with a soft wash that clears mold, mildew and dirt without forcing water where it should not go.",
         prose=["Florida humidity leaves green and black film on the north and shaded sides of a home. Magic Touch washes stucco, siding, soffits, fascia and screen enclosures with a low-pressure soft wash so the surface comes clean without damage.",
                "Windows, doors and landscaping are protected first, and the job finishes with a walkthrough so the homeowner sees the result before the crew leaves."],
         suits=["Stucco and siding with mold or mildew", "Soffits, fascia and screen enclosures", "Homes that have not been washed in a year or more"],
         faq=[("How often should a house be washed in Florida?", "It depends on shade and buildup. Magic Touch can recommend a schedule after seeing the home during the free estimate."),
              ("Is house washing safe for screens and stucco?", "Yes. House washing uses a soft wash, a low-pressure method suited to stucco, siding and screen enclosures.")],
         pair="roof-soft-washing"),
    dict(slug="driveways-sidewalks", name="Driveways & Sidewalks", short="Concrete", chip="Surface cleaner",
         desc="Surface-cleaner pressure washing that lifts dirt, mildew and grime from concrete for an even, stripe-free finish.",
         prose=["Concrete driveways and sidewalks collect dirt, mildew and tire marks, and a wand alone tends to leave stripes. Magic Touch cleans flatwork with a surface cleaner for an even finish across the whole slab, then rinses the edges and curbs.",
                "The photo on this page is a Magic Touch job: the same walkway before and after cleaning."],
         suits=["Driveways with dirt, mildew or tire marks", "Sidewalks, walkways and entry paths", "Curbs and concrete edges"],
         faq=[("Will pressure washing leave stripes on my driveway?", "Magic Touch cleans concrete with a surface cleaner, a tool built to give flatwork an even finish."),
              ("Do I need to move my cars?", "Yes, please move vehicles off the driveway before the crew arrives so the whole slab can be cleaned.")],
         pair="patio-pool-decks", photo="after"),
    dict(slug="patio-pool-decks", name="Patio & Pool Decks", short="Pool decks", chip="Pavers and concrete",
         desc="Deep cleaning for pool decks, patios and lanais. Brighter surfaces and less slippery algae underfoot.",
         prose=["Pool decks and patios stay damp, and damp concrete and pavers grow algae that turns slick underfoot. Magic Touch cleans pool decks, patios and lanais with the method that suits the surface, then rinses everything down.",
                "Pavers can be sealed after cleaning. Ask about paver sealing when you request the estimate."],
         suits=["Pool decks with green or black buildup", "Patios and lanais", "Paver and concrete surfaces"],
         faq=[("Can the pool deck and the pavers be sealed too?", "Yes. Magic Touch offers paver sealing, which can be added to a pool deck or patio cleaning on the same estimate."),
              ("Is it safe around the pool?", "Tell Magic Touch about the pool when booking, and the crew plans the clean around it.")],
         pair="paver-sealing"),
    dict(slug="paver-sealing", name="Paver Sealing", short="Pavers", chip="Clean and seal",
         desc="Pavers cleaned, re-sanded and sealed to lock the joints, deepen the color and help resist stains and weeds.",
         prose=["Sealing protects a paver driveway, patio or pool deck after it has been cleaned. Magic Touch cleans the pavers first, replaces joint sand where it has washed out, then applies sealer.",
                "Sealed joints help hold pavers in place and make weeds and stains harder to take hold."],
         suits=["Paver driveways and walkways", "Paver patios and pool decks", "Pavers with washed-out joint sand"],
         faq=[("Do pavers need to be cleaned before sealing?", "Yes. Magic Touch cleans pavers before sealing so the sealer goes onto a clean surface."),
              ("How much does paver sealing cost?", "It depends on the size and condition of the area. Magic Touch gives a free, flat-rate estimate before any work starts.")],
         pair="patio-pool-decks"),
    dict(slug="gutter-cleaning", name="Gutter Cleaning", short="Gutters", chip="Gutters and downspouts",
         desc="Clogged gutters and downspouts cleared so rainwater flows away from the roof and foundation.",
         prose=["Leaves and debris back up gutters, and overflowing gutters send water where it does not belong. Magic Touch clears gutters and downspouts so Central Florida rain drains the way it should.",
                "Gutter cleaning pairs well with a roof soft wash, since both are done from the same side of the house."],
         suits=["Gutters overflowing in heavy rain", "Downspouts clogged with leaves", "Homes getting a roof soft wash"],
         faq=[("Can gutter cleaning be done with a roof wash?", "Yes. Many homeowners book gutter cleaning together with a roof soft wash on the same visit."),
              ("How do I know my gutters are clogged?", "Water spilling over the edge in a storm, or plants growing in the gutter, are the usual signs.")],
         pair="roof-soft-washing"),
    dict(slug="solar-panel-cleaning", name="Solar Panel Cleaning", short="Solar", chip="Gentle clean",
         desc="Gentle cleaning that clears dust, pollen and bird droppings so the panels stay clear.",
         prose=["Solar panels collect dust, pollen and bird droppings like any other roof surface. Magic Touch cleans panels gently so the glass is clear.",
                "Panel cleaning can be booked on its own or combined with a roof soft wash or gutter cleaning."],
         suits=["Rooftop solar panels with dust or pollen", "Panels with bird droppings", "Homes booking a roof wash"],
         faq=[("Can solar panels be cleaned with the roof?", "Yes. Solar panel cleaning can be added to a roof soft wash or gutter cleaning visit."),
              ("How often should panels be cleaned?", "It depends on pollen, trees and birds near the home. Ask during the free estimate.")],
         pair="gutter-cleaning"),
]
SVC = {s["slug"]: s for s in SERVICES}

AREAS = [
    dict(slug="orlando", name="Orlando", county="Orange County", deck="Home base. Magic Touch Pressure Washing is based in Orlando and cleans roofs, homes, driveways and pool decks across the city and its neighborhoods."),
    dict(slug="kissimmee", name="Kissimmee", county="Osceola County", deck="Roof soft washing, house washing and concrete cleaning for Kissimmee homes, with the same flat-rate pricing and guarantees as in Orlando."),
    dict(slug="sanford", name="Sanford", county="Seminole County", deck="North of Orlando in Seminole County. Magic Touch serves Sanford homes with every service it offers, quoted free and flat-rate."),
]

INCLUDED = [("Free, flat-rate estimate", "One price before any work starts. No hourly meter."),
            ("On-time guarantee", "The crew shows up when Magic Touch says it will."),
            ("The right method for the surface", "Soft wash for roofs and siding, surface cleaner for concrete."),
            ("Landscaping protected", "Plants and sensitive areas are covered before cleaning."),
            ("Final walkthrough", "The finished job is checked with the homeowner."),
            ("1-year guarantee", "Magic Touch stands behind the work for a full year.")]

FAQ_HOME = [
    ("How much does pressure washing cost?", "Every property is different, so Magic Touch gives a free, flat-rate estimate before any work starts. The price quoted is the price paid, with no hourly billing. Call or text %s or request an estimate online." % PHONE),
    ("Will soft washing damage my roof?", "Roofs are soft washed with low pressure rather than blasted, which is why the method is used on shingle, tile and metal roofs."),
    ("What is the difference between soft washing and pressure washing?", "Pressure washing uses high-pressure water and suits hard surfaces like concrete driveways and sidewalks. Soft washing uses low pressure plus cleaning solution for roofs, stucco, siding and screens."),
    ("Which areas does Magic Touch serve?", "Orlando, Kissimmee, Sanford and the surrounding Central Florida area. If you are not sure about your street, call or text %s." % PHONE),
    ("Is Magic Touch licensed and insured?", "Yes. Magic Touch Pressure Washing is licensed and insured, and family-owned."),
    ("What guarantees come with the work?", "Every job comes with an on-time guarantee and a 1-year guarantee on the work, and the estimate is free and flat-rate."),
]

FAQ_GROUPS = [
    ("Estimates and pricing", [FAQ_HOME[0], ("Can I text for a quote?", "Yes. Call or text %s. Photos of the area you want cleaned help Magic Touch price it quickly." % PHONE), FAQ_HOME[5]]),
    ("Methods", [FAQ_HOME[1], FAQ_HOME[2], ("Will pressure washing leave stripes on my driveway?", "Concrete is cleaned with a surface cleaner, a tool built to give flatwork an even finish.")]),
    ("The company", [FAQ_HOME[4], FAQ_HOME[3], ("Who owns Magic Touch?", "Magic Touch Pressure Washing is family-owned. Magic Touch Mobile Pressure Washing LLC was incorporated in Orlando in October 2020 by Trevean J. McLeod.")]),
]

# ------------------------------------------------------------------ helpers
esc = lambda s: html.escape(s, quote=True)
R = ""  # relative prefix for the page being rendered


def u(path):
    """Site path ('' = home, 'services/' ...) -> link relative to the current page."""
    return R + path + "index.html"  # explicit index.html so links work on hosts without directory indexes


def a(path):
    return R + "assets/" + path


def est_btn(label="Get a free estimate", cta="estimate", cls="btn btn-primary", href=None):
    return '<a class="%s" data-cta="%s" href="%s">%s%s</a>' % (cls, cta, href or u(EST), esc(label), ICON["arrow"])


def call_btn(cls="btn btn-ghost", cta="call", label="Call or text"):
    return '<a class="%s" data-cta="%s" href="tel:%s">%s%s</a>' % (cls, cta, TEL, ICON["phone"], esc(label))


def pic(name, alt, pos="50% 55%", lazy=True):
    ld = ' loading="lazy"' if lazy else ' fetchpriority="high"'
    return ('<picture><source type="image/webp" srcset="%s"><img src="%s" alt="%s" width="720" height="1440" style="object-position:%s"%s decoding="async"></picture>'
            % (a("img/%s.webp" % name), a("img/%s.jpg" % name), esc(alt), pos, ld))


def ph(name, note="Job photo coming soon"):
    return '<span class="ph" role="img" aria-label="%s, photo placeholder"><span class="ph__note">%s</span><span class="ph__name">%s</span></span>' % (esc(name), esc(note), esc(name))


PHOTO_ALT = {"before": "Walkway outside a storefront before Magic Touch cleaned it, with dark wet stains on the concrete",
             "after": "The same walkway after Magic Touch cleaned it, the concrete an even light gray"}


def media_for(s):
    if s.get("photo"):
        return pic(s["photo"], PHOTO_ALT[s["photo"]])
    return ph(s["name"])


def ba_slider(lazy=False):
    return ('<div class="ba" data-ba><img src="%s" alt="%s" width="720" height="1440"%s><img class="ba__after" src="%s" alt="%s" width="720" height="1440" loading="lazy">'
            '<span class="ba__line"></span><span class="ba__tag ba__tag--b">Before</span><span class="ba__tag ba__tag--a">After</span>'
            '<input type="range" min="0" max="100" value="50" aria-label="Drag to compare before and after"></div>') % (
        a("img/before.jpg"), esc(PHOTO_ALT["before"]), "" if not lazy else ' loading="lazy"', a("img/after.jpg"), esc(PHOTO_ALT["after"]))


def acc(items, pre):
    out = []
    for i, (q, ans) in enumerate(items):
        out.append('<div class="acc-item"><button class="acc-trigger" aria-expanded="false" aria-controls="%s%d"><span>%s</span><span class="acc-icon" aria-hidden="true"></span></button>'
                   '<div class="acc-panel" id="%s%d" role="region"><div class="acc-panel__inner"><p>%s</p></div></div></div>' % (pre, i, esc(q), pre, i, esc(ans)))
    return '<div class="accordion">%s</div>' % "".join(out)


def promise_line(light=True):
    return ('<p class="rate-line%s"><span><strong>Free</strong> estimates</span><span><strong>Flat-rate</strong> pricing</span><span><strong>1-year</strong> guarantee</span>'
            '<span class="rate-line__note">On-time guarantee. Licensed and insured.</span></p>') % (" rate-line--light" if light else "")


def ledger(head="Included on every job"):
    items = "".join('<li>%s<div><strong>%s</strong><span>%s</span></div></li>' % (ICON["check"], esc(t), esc(d)) for t, d in INCLUDED)
    return f'''<div class="ledger reveal">
  <div class="ledger__main"><h3>{head}</h3><ul class="ledger__list">{items}</ul></div>
  <div class="ledger__side">
    <div><h3>Before the crew arrives</h3><ul class="plain-list"><li>Move vehicles off the driveway</li><li>Keep pets inside while the crew works</li><li>Make sure an outdoor spigot is reachable</li><li>Close windows and doors near the work</li></ul></div>
    <div><h3>Good to know</h3><ul class="plain-list"><li>Licensed and insured</li><li>Family-owned, based in Orlando</li><li>Magic Touch Mobile Pressure Washing LLC, since 2020</li></ul></div>
    {est_btn(cls="btn btn-primary btn-block", cta="included")}
  </div>
</div>'''


def wall(dur="60s", heading="Before and after, from a Magic Touch job", deck="The walkway below is a Magic Touch job. More before and after photos from Orlando homes are being added.", link=True):
    tiles = [("pic", "before"), ("ph", SERVICES[0]["name"]), ("pic", "after"), ("ph", SERVICES[1]["name"]),
             ("pic", "before"), ("ph", SERVICES[3]["name"]), ("pic", "after"), ("ph", SERVICES[4]["name"])]

    def tile(kind, v, hidden):
        h = ' aria-hidden="true"' if hidden else ""
        if kind == "pic":
            return '<figure class="pw"%s>%s</figure>' % (h, pic(v, "" if hidden else PHOTO_ALT[v]))
        return '<figure class="pw pw--ph"%s>%s</figure>' % (h, ph(v))
    track = "".join(tile(k, v, False) for k, v in tiles) + "".join(tile(k, v, True) for k, v in tiles)
    side = '<a class="text-link" href="%s">Open the gallery</a>' % u("gallery/") if link else ""
    return f'''<section class="section section--wall"><div class="container"><div class="section-head"><h2>{heading}</h2><div class="section-head__side"><p class="deck">{deck}</p>{side}</div></div></div>
<div class="pw-wall"><div class="pw-row"><div class="pw-track" style="--pw-dur:{dur}">{track}</div></div></div>
<div class="container"><div class="cta-row cta-row--center mt-6">{est_btn("Get your after photo", "wall", "btn btn-primary btn-lg")}</div></div></section>'''


def cta_band(h="Ready for the after photo?", p="Free, flat-rate estimates across Orlando, Kissimmee, Sanford and the surrounding area."):
    return f'''<section class="cta-band">
  <div class="cta-band__media">{pic("after", PHOTO_ALT["after"], "50% 70%")}</div>
  <div class="cta-band__inner"><h2>{h}</h2><p>{p}</p>{promise_line()}
    <div class="cta-row">{est_btn("Get a free estimate", "cta-band", "btn btn-primary btn-lg")}{call_btn("btn btn-ghost--light btn-lg", "cta-band-call", "Call or text " + PHONE)}<a class="btn btn-ghost--light btn-lg" href="{u("services/")}">All services</a></div>
  </div>
</section>'''


# ------------------------------------------------------------------ chrome
def head(p):
    return f'''<!DOCTYPE html>
<html lang="en" class="no-js">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(p["title"])}</title>
<meta name="description" content="{esc(p["desc"])}">
<meta name="robots" content="noindex">
<meta name="theme-color" content="#13261A">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' fill='%2313261A'/%3E%3Cpath d='M16 6s-7 7.5-7 12a7 7 0 0 0 14 0c0-4.5-7-12-7-12z' fill='%237CD374'/%3E%3C/svg%3E">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{NAME}">
<meta property="og:title" content="{esc(p["title"])}">
<meta property="og:description" content="{esc(p["desc"])}">
<link rel="preload" href="{a("fonts/Tanker-Regular.woff2")}" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{a("fonts/Supreme-Regular.woff2")}" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{a("css/styles.css")}">
<script>document.documentElement.classList.remove('no-js');document.documentElement.classList.add('js');</script>
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"HomeAndConstructionBusiness","name":"{NAME}","telephone":"+1-321-355-9521","email":"{EMAIL}","address":{{"@type":"PostalAddress","addressLocality":"Orlando","addressRegion":"FL","addressCountry":"US"}},"areaServed":["Orlando, FL","Kissimmee, FL","Sanford, FL"],"founder":"Trevean J. McLeod","sameAs":["{IG}","{FB}"]}}</script>
</head>
<body class="{p.get("body", "")}">
<a class="skip-link" href="#main">Skip to content</a>'''


def chrome_top():
    svc_links = "".join('<a class="dropdown__link" role="menuitem" href="%s"><strong>%s</strong><span>%s</span></a>' % (u("services/%s/" % s["slug"]), esc(s["name"]), esc(s["chip"])) for s in SERVICES)
    area_links = "".join('<a class="dropdown__link" role="menuitem" href="%s"><strong>%s</strong><span>%s</span></a>' % (u("service-areas/%s/" % x["slug"]), x["name"], x["county"]) for x in AREAS)
    d_svc = "".join('<a href="%s">%s</a>' % (u("services/%s/" % s["slug"]), esc(s["name"])) for s in SERVICES)
    d_area = "".join('<a href="%s">%s</a>' % (u("service-areas/%s/" % x["slug"]), x["name"]) for x in AREAS)
    return f'''
<div class="promo-bar" role="region" aria-label="Estimates"><div class="promo-bar__inner"><span class="promo-bar__item"><span class="promo-bar__long">Family-owned &middot; </span><strong>Free</strong> flat-rate estimates</span><span class="promo-bar__item promo-bar__item--wide">Orlando, Kissimmee and Sanford</span><a class="promo-bar__call" data-cta="promo-call" href="tel:{TEL}">Call or text <strong>{PHONE}</strong></a><a class="promo-bar__link" data-cta="promo" href="{u(EST)}">Free estimate</a></div></div>
<header class="site-header">
  <div class="site-header__inner">
    <a class="brand" href="{u("")}" aria-label="{NAME} home"><span class="brand__word"><b>Magic Touch</b><small>Pressure Washing</small></span></a>
    <nav class="primary-nav" aria-label="Primary">
      <ul class="nav-list"><li class="nav-item has-dropdown"><button class="nav-link" type="button">Services{ICON["caret"]}</button><div class="dropdown" role="menu"><div class="dropdown__list">{svc_links}</div><div class="dropdown__foot"><a class="dropdown__link" role="menuitem" href="{u("services/")}"><strong>Every service</strong><span>What Magic Touch cleans</span></a></div></div></li><li class="nav-item has-dropdown"><button class="nav-link" type="button">Service Areas{ICON["caret"]}</button><div class="dropdown" role="menu"><div class="dropdown__list">{area_links}</div><div class="dropdown__foot"><a class="dropdown__link" role="menuitem" href="{u("service-areas/")}"><strong>All service areas</strong><span>Orlando and Central Florida</span></a></div></div></li><li class="nav-item"><a class="nav-link" href="{u("about/")}">About</a></li><li class="nav-item"><a class="nav-link" href="{u("gallery/")}">Gallery</a></li><li class="nav-item"><a class="nav-link" href="{u("faq/")}">FAQ</a></li></ul>
      {est_btn("Free estimate", "nav", "btn btn-primary nav-book__btn")}
    </nav>
    <a class="header-call" data-cta="header-call" href="tel:{TEL}" aria-label="Call or text Magic Touch at {PHONE}">{ICON["phone"]}</a>
    <a class="btn btn-primary header-book" data-cta="header-pill" href="{u(EST)}">Estimate</a>
    <button class="hamburger" aria-label="Open menu" aria-expanded="false" aria-controls="mobile-drawer"><span></span><span></span><span></span></button>
  </div>
</header>
<div class="mobile-drawer" id="mobile-drawer" aria-hidden="true">
  <div class="drawer-book-buttons">
    {est_btn("Get a free estimate", "drawer")}
    <a class="btn btn-ghost" data-cta="drawer-call" href="tel:{TEL}">{ICON["phone"]}Call or text</a>
  </div>
  <ul class="drawer-nav">
    <li class="drawer-group"><button class="drawer-link" type="button" aria-expanded="false">Services{ICON["caret"]}</button><div class="drawer-sub"><a href="{u("services/")}">Every service</a>{d_svc}</div></li>
    <li class="drawer-group"><button class="drawer-link" type="button" aria-expanded="false">Service Areas{ICON["caret"]}</button><div class="drawer-sub"><a href="{u("service-areas/")}">All service areas</a>{d_area}</div></li>
    <li><a class="drawer-link" href="{u("about/")}">About</a></li>
    <li><a class="drawer-link" href="{u("gallery/")}">Gallery</a></li>
    <li><a class="drawer-link" href="{u("faq/")}">FAQ</a></li>
  </ul>
  <div class="drawer-meta"><span>Free, flat-rate estimates</span><span>On-time and 1-year guarantees</span><span>Orlando, Kissimmee and Sanford</span><a class="drawer-tel" href="tel:{TEL}" data-cta="drawer-tel">Call or text {PHONE}</a></div>
</div>
<main id="main">'''


def chrome_bottom():
    svc = "".join('<a href="%s">%s</a>' % (u("services/%s/" % s["slug"]), esc(s["name"])) for s in SERVICES)
    areas = "".join('<a href="%s">Pressure washing in %s</a>' % (u("service-areas/%s/" % x["slug"]), x["name"]) for x in AREAS)
    return f'''</main>
<footer class="site-footer">
  <div class="container">
    <div class="footer-cta">
      <h2>Get a flat-rate price. Free.</h2>
      <div class="cta-row">{est_btn("Get a free estimate", "footer", "btn btn-primary btn-lg")}<a class="btn btn-ghost--light btn-lg" href="{u("services/")}">See services</a></div>
    </div>
    <div class="footer-grid">
      <div class="footer-col">
        <span class="brand__word footer-brand-word"><b>Magic Touch</b><small>Pressure Washing</small></span>
        <p class="footer-tag">Family-owned exterior cleaning for homes across Orlando, Kissimmee and Sanford. Licensed and insured, with flat-rate pricing, an on-time guarantee and a 1-year guarantee on the work.</p>
        <div class="footer-socials"><a href="{IG}" rel="noopener" aria-label="@magictouchpw_ on Instagram">{ICON["ig"]}<span>@magictouchpw_</span></a><a href="{FB}" rel="noopener" aria-label="Magic Touch Pressure Washing on Facebook">{ICON["fb"]}<span>Facebook</span></a></div>
      </div>
      <div class="footer-col">
        <h3>Services</h3>
        <nav class="footer-quick" aria-label="Services">{svc}<a href="{u(EST)}" data-cta="footer-link">Request a free estimate</a></nav>
      </div>
      <div class="footer-col">
        <h3>Service areas</h3>
        <nav class="footer-quick" aria-label="Service areas">{areas}</nav>
        <div class="nap"><div class="nap-row">{ICON["phone"]}<a href="tel:{TEL}" data-cta="footer-call">Call or text<br><span class="nap-sub">{PHONE}</span></a></div><div class="nap-row">{ICON["mail"]}<a href="mailto:{EMAIL}">Email<br><span class="nap-sub">{EMAIL}</span></a></div><div class="nap-row">{ICON["pin"]}<a href="{u("service-areas/orlando/")}">Orlando, Florida<br><span class="nap-sub">Serving Orlando, Kissimmee, Sanford and nearby</span></a></div></div>
      </div>
      <div class="footer-col">
        <h3>Explore</h3>
        <nav class="footer-quick" aria-label="Footer"><a href="{u("about/")}">About Magic Touch</a><a href="{u("gallery/")}">Gallery</a><a href="{u("faq/")}">FAQ</a><a href="{u("privacy/")}">Privacy Policy</a></nav>
      </div>
    </div>
    <div class="footer-bottom"><span>&copy; 2026 Magic Touch Mobile Pressure Washing LLC, Orlando, Florida</span><span>Website preview by A1A Marketing</span></div>
  </div>
</footer>
<div class="mobile-book-bar" aria-label="Get a free estimate">
  <div class="mobile-book-bar__label"><span class="lede">Free estimates</span><span class="sub">Flat-rate, Orlando area</span></div>
  <div class="mobile-book-bar__actions"><a class="btn btn-ghost--light mobile-book-bar__call" data-cta="sticky-call" href="tel:{TEL}" aria-label="Call or text Magic Touch at {PHONE}">{ICON["phone"]}<span>Call</span></a><a class="btn btn-primary" data-cta="sticky-bar" href="{u(EST)}">Estimate</a></div>
</div>
<div class="book-nudge" role="complementary" aria-label="Get a free estimate">
  <button class="book-nudge__close" type="button" aria-label="Dismiss">&times;</button>
  <div class="book-nudge__title">Want a price on your home?</div>
  <div class="book-nudge__meta">Free, flat-rate estimates &middot; {PHONE}</div>
  <a class="btn btn-primary" data-cta="desktop-nudge" href="{u(EST)}">Get an estimate</a>
</div>
<script src="{a("js/main.js")}" defer></script>
<script src="{a("js/magic.js")}" defer></script>
</body>
</html>
'''


# ------------------------------------------------------------------ sections
def hero(kicker, h1, accent, sub, media, extra="", ctas=None, label=None):
    acc_html = ' <span class="accent">%s</span>' % accent if accent else ""
    ctas = ctas or (est_btn("Get a free estimate", "hero", "btn btn-primary btn-lg") + '<a class="btn btn-ghost--light btn-lg" href="%s">See services</a>' % u("services/") + call_btn("btn btn-ghost--light btn-lg", "hero-call", "Call or text"))
    return f'''<section class="hero hero--navy" aria-label="{esc(label or h1)}">
  <div class="hero__media">{media}</div>
  <div class="hero__panel"><div class="hero__content">
    <p class="hero__kicker">{kicker}</p>
    <h1>{h1}{acc_html}</h1>
    <p class="hero__sub">{sub}</p>
    {extra}
    <div class="hero__cta cta-row">{ctas}</div>
  </div></div>
</section>'''


def fact_bar():
    facts = [("5-star", "Rated by homeowners"), ("Free", "Flat-rate estimates"), ("1 year", "Guarantee on the work"), ("On time", "On-time guarantee")]
    items = "".join('<div class="fact-item"><span class="fact-item__figure">%s</span><span class="fact-item__label">%s</span></div>' % f for f in facts)
    return f'<section class="fact-bar" aria-label="Guarantees"><div class="fact-bar__inner">{items}<a class="fact-item fact-item--cta" data-cta="fact-bar" href="{u(EST)}"><span class="fact-item__figure">Estimate{ICON["arrow"]}</span><span class="fact-item__label">Free, no pressure</span></a></div></section>'


def svc_card(s, big=True):
    href = u("services/%s/" % s["slug"])
    if big:
        return f'''<article class="trip reveal">
  <a class="trip__media" href="{href}" tabindex="-1" aria-hidden="true">{media_for(s)}<span class="chip chip--fill">{esc(s["chip"])}</span></a>
  <div class="trip__body">
    <h3><a href="{href}">{esc(s["name"])}</a></h3>
    <p class="trip__desc">{esc(s["desc"])}</p>
    <div class="trip__price"><span class="amt">Free</span><span class="per">flat-rate<br>estimate</span></div>
    <div class="trip__meta"><span class="detail-chip">{ICON["shield"]}1-year guarantee</span><span class="detail-chip">{ICON["clock"]}On-time guarantee</span></div>
    <div class="trip__actions">{est_btn("Price my " + s["short"].lower(), "svc-card")}<a class="btn btn-ghost" href="{href}">Service details</a></div>
  </div>
</article>'''
    return f'''<article class="xtrip reveal">
  <a class="xtrip__media" href="{href}" tabindex="-1" aria-hidden="true">{media_for(s)}<span class="chip chip--fill">{esc(s["chip"])}</span></a>
  <div class="xtrip__body">
    <h3><a href="{href}">{esc(s["name"])}</a></h3>
    <p class="trip__desc">{esc(s["desc"])}</p>
    <div class="trip__price"><span class="amt">Free</span><span class="per">flat-rate<br>estimate</span></div>
    <div class="trip__actions">{est_btn("Get a price", "extra-card")}<a class="btn btn-ghost" href="{href}">Details</a></div>
  </div>
</article>'''


def steps_rail():
    return ('<div class="rail"><div class="rail__step"><span class="rail__time">Step 1</span><h3 class="rail__h">Call, text or send the form</h3><p>Tell Magic Touch what needs cleaning and where. Photos of the area help.</p></div>'
            '<div class="rail__step"><span class="rail__time">Step 2</span><h3 class="rail__h">Get one flat-rate price</h3><p>The estimate is free, and the price is set before any work starts.</p></div>'
            '<div class="rail__step"><span class="rail__time">Step 3</span><h3 class="rail__h">The crew shows up on time</h3><p>The job is cleaned with the right method, walked with you at the end, and backed by a 1-year guarantee.</p></div></div>')


def book_prompt(h="Get a flat-rate price before any work starts.", p="Free estimates for Orlando, Kissimmee, Sanford and the surrounding area."):
    return f'<section class="book-prompt"><div class="container"><div class="book-prompt__inner"><div><h2>{h}</h2><p>{p}</p></div><div class="cta-row">{est_btn("Get a free estimate", "mid-band", "btn btn-navy btn-lg")}{call_btn("btn btn-ghost", "mid-band-call", "Call or text")}</div></div></div></section>'


def loc_grid():
    panels = "".join(f'<a class="loc-panel reveal" href="{u("service-areas/%s/" % x["slug"])}">{ph(x["name"], x["county"])}<span class="loc-panel__body"><span class="loc-panel__name">{x["name"]}</span><span class="loc-panel__deck">{esc(x["deck"])}</span><span class="text-link">Pressure washing in {x["name"]}</span></span></a>' for x in AREAS)
    return f'<div class="loc-grid loc-grid--3">{panels}</div>'


def species_list():
    rows = "".join('<a class="species-row" href="%s"><span class="species-row__name">%s</span><span class="species-row__go">%s</span></a>' % (u("services/%s/" % s["slug"]), esc(s["name"]), ICON["arrow"]) for s in SERVICES)
    return '<div class="species-list">%s</div>' % rows


# ------------------------------------------------------------------ pages
def page_home():
    who = [("Homeowners", "Roofs, siding and driveways that have picked up Florida mold, mildew and algae."),
           ("Pool and patio owners", "Pool decks, patios and lanais that have turned green or slick."),
           ("Paver owners", "Paver driveways and patios that need cleaning, new joint sand and a seal."),
           ("Solar owners", "Rooftop panels coated in dust, pollen or bird droppings.")]
    who_html = "".join(f'<div class="who-item reveal"><div class="who-item__media">{ph(t, "Photo coming soon")}</div><div class="who-item__body"><span class="who-item__num">0{i+1}</span><h3>{t}</h3><p>{d}</p></div></div>' for i, (t, d) in enumerate(who))
    return hero("Licensed and insured &middot; Orlando, Florida", "Pressure washing in Orlando.", "Flat-rate and on time.",
                "Magic Touch Pressure Washing is a family-owned exterior cleaning company run by Trevean McLeod. Roofs, homes, driveways and pool decks across Orlando, Kissimmee and Sanford.",
                ba_slider(), promise_line(), label="Pressure washing in Orlando") + fact_bar() + wall() + f'''
<section class="section section--sand-deep" id="services"><div class="container">
<div class="section-head"><h2>Soft wash up top. Surface clean below.</h2><div class="section-head__side"><p class="deck">Roofs get a low-pressure soft wash. Concrete gets a surface cleaner for an even finish. Every job is quoted free and flat-rate.</p><a class="text-link" href="{u("services/")}">Every service</a></div></div>
<div class="trip-grid">{svc_card(SVC["roof-soft-washing"])}{svc_card(SVC["driveways-sidewalks"])}</div>
</div></section>

<section class="section"><div class="container">
<div class="section-head"><h2>More surfaces Magic Touch cleans</h2><div class="section-head__side"><p class="deck">House washing, pool decks, paver sealing, gutters and solar panels, all with the same guarantees.</p></div></div>
<div class="xtrip-grid">{"".join(svc_card(SVC[k], False) for k in ("house-washing", "patio-pool-decks", "paver-sealing", "gutter-cleaning", "solar-panel-cleaning"))}</div>
</div></section>

<section class="section"><div class="container">
<div class="section-head"><h2>One standard on every job</h2><div class="section-head__side"><p class="deck">The same steps and the same guarantees, whether it is a driveway or a whole house.</p></div></div>
{ledger()}
</div></section>

{book_prompt()}

<section class="section section--navy"><div class="container"><div class="captain-split">
  <div class="captain-split__media reveal">{ph("Trevean McLeod", "Owner photo coming soon")}</div>
  <div class="captain-split__body">
    <h2>Family-owned and run by Trevean McLeod</h2>
    <p class="deck">Magic Touch Mobile Pressure Washing LLC was incorporated in Orlando in October 2020 by Trevean J. McLeod.</p>
    <p>The company cleans homes across Orlando, Kissimmee and Sanford with one flat-rate price quoted up front, an on-time guarantee and a 1-year guarantee on the work. It is licensed and insured.</p>
    <div class="cta-row mt-5">{est_btn("Get a free estimate", "owner")}<a class="btn btn-ghost--light" href="{u("about/")}">About Magic Touch</a></div>
  </div>
</div></div></section>

<section class="section"><div class="container">
<div class="section-head"><h2>Where Magic Touch works</h2><div class="section-head__side"><p class="deck">Based in Orlando, serving Kissimmee, Sanford and the surrounding Central Florida area.</p><a class="text-link" href="{u("service-areas/")}">All service areas</a></div></div>
{loc_grid()}
</div></section>

<section class="section section--sand-deep"><div class="container">
<div class="section-head"><h2>Who calls Magic Touch</h2><div class="section-head__side"><p class="deck">Central Florida heat and humidity are hard on every outdoor surface of a home.</p></div></div>
<div class="who-grid">{who_html}</div>
<div class="cta-row cta-row--center mt-7">{est_btn("Get your free estimate", "who", "btn btn-primary btn-lg")}</div>
</div></section>

<section class="section section--navy"><div class="container"><div class="species-split">
  <div><h2>What Magic Touch cleans</h2><p class="deck">Seven services, one flat-rate estimate. Bundle a few and get them done on the same visit.</p><div class="cta-row mt-5">{est_btn("Get a free estimate", "species")}<a class="btn btn-ghost--light" href="{u("services/")}">Every service</a></div></div>
  {species_list()}
</div></div></section>

<section class="section"><div class="container"><div class="how-split">
  <div><h2>How a free estimate works</h2><p class="deck">Three steps. One price, set before any work starts.</p><div class="cta-row mt-5">{est_btn("Start an estimate", "how")}</div></div>
  {steps_rail()}
</div></div></section>

<section class="section section--sand-deep"><div class="container container--narrow">
<div class="section-head"><h2>Questions before booking</h2><div class="section-head__side"><a class="text-link" href="{u("faq/")}">All questions</a></div></div>
{acc(FAQ_HOME, "hf")}
<div class="cta-row cta-row--center mt-6">{est_btn("Get a free estimate", "faq", "btn btn-primary btn-lg")}</div>
</div></section>
''' + cta_band()


def booking_panel(title):
    return f'''<aside class="booking-panel" aria-label="Get a price for {esc(title)}">
  <div class="booking-panel__head"><h2>Get a price</h2><p>Free estimate. One flat-rate price.</p></div>
  <div class="pricing-tiers">
    <div class="pricing-tier"><div class="pricing-tier__label">Estimate<span>Quoted before any work starts</span></div><div class="pricing-tier__price">Free</div></div>
    <div class="pricing-tier"><div class="pricing-tier__label">Guarantee<span>On the cleaning work</span></div><div class="pricing-tier__price">1 yr</div></div>
  </div>
  <div class="booking-panel__cta">{est_btn("Request an estimate", "booking-panel", "btn btn-primary btn-lg btn-block")}<a class="btn btn-ghost btn-block mt-3" data-cta="booking-panel-call" href="tel:{TEL}">{ICON["phone"]}Call or text {PHONE}</a>
    <p class="booking-panel__note">Magic Touch replies with a flat-rate price. No hourly billing.</p></div>
  <div class="quick-details">
    <div class="quick-detail">{ICON["clock"]}<div><div class="quick-detail__label">Scheduling</div><div class="quick-detail__value">On-time guarantee</div></div></div>
    <div class="quick-detail">{ICON["pin"]}<div><div class="quick-detail__label">Service area</div><div class="quick-detail__value">Orlando, Kissimmee, Sanford and nearby</div></div></div>
    <div class="quick-detail">{ICON["shield"]}<div><div class="quick-detail__label">Company</div><div class="quick-detail__value">Licensed and insured, family-owned</div></div></div>
  </div>
</aside>'''


def page_service(s):
    pair = SVC[s["pair"]]
    prose = "".join("<p>%s</p>" % esc(x) for x in s["prose"])
    suits = "".join("<li>%s</li>" % esc(x) for x in s["suits"])
    faqs = s["faq"] + [FAQ_HOME[0], FAQ_HOME[5]]
    ctas = est_btn("Get a free estimate", "hero", "btn btn-primary btn-lg") + '<a class="btn btn-ghost--light btn-lg" href="#details">Service details</a>'
    extra = '<p class="hero__price"><span class="amt">Free</span><span>flat-rate estimate<br>1-year guarantee</span></p>'
    media = ba_slider() if s.get("photo") else ph(s["name"])
    return hero("%s &middot; Orlando, Kissimmee and Sanford" % esc(s["chip"]), esc(s["name"]), "", esc(s["desc"]), media, extra, ctas) + f'''
<section class="section" id="details"><div class="container"><div class="tour-layout">
  <div class="prose">
    <h2>What the job covers</h2>
    {prose}
    <h3>Good fit for</h3><ul class="plain-list">{suits}</ul>
    <div class="cta-row mt-5">{est_btn("Request an estimate", "prose")}</div>
    <h3>How the job runs</h3>
    {steps_rail()}
  </div>
  {booking_panel(s["name"])}
</div></div></section>
<section class="section section--sand-deep"><div class="container"><div class="section-head"><h2>Included with {esc(s["name"].lower())}</h2></div>{ledger()}</div></section>
{wall("45s", "From Magic Touch jobs", "A real Magic Touch walkway, before and after. More job photos are being added.")}
<section class="section"><div class="container container--narrow"><div class="section-head"><h2>Before you book</h2></div>{acc(faqs, "tf")}</div></section>
<section class="section section--navy"><div class="container"><div class="captain-split">
  <div class="captain-split__media reveal">{media_for(pair)}</div>
  <div class="captain-split__body"><h2>Pair it with {esc(pair["name"].lower())}</h2><p class="deck">{esc(pair["desc"])}</p><p>Add it to the same estimate and it can be done on the same visit.</p>
  <div class="cta-row mt-5">{est_btn("Estimate both", "cross")}<a class="btn btn-ghost--light" href="{u("services/%s/" % pair["slug"])}">{esc(pair["name"])}</a></div></div>
</div></div></section>
''' + cta_band("Book your %s estimate" % s["short"].lower())


def page_services():
    return f'''<section class="page-hero"><div class="container"><h1>Services</h1><p class="deck">Seven exterior cleaning services for homes across Orlando, Kissimmee and Sanford. Every job is quoted free and flat-rate, with an on-time guarantee and a 1-year guarantee on the work.</p><div class="cta-row mt-5">{est_btn("Get a free estimate", "page-hero", "btn btn-primary btn-lg")}{call_btn("btn btn-ghost btn-lg", "page-hero-call", "Call or text " + PHONE)}</div></div></section>
<section class="section section--tight-top"><div class="container"><div class="trip-grid">{"".join(svc_card(s) for s in SERVICES[:2])}</div></div></section>
<section class="section"><div class="container"><div class="xtrip-grid">{"".join(svc_card(s, False) for s in SERVICES[2:])}</div></div></section>
<section class="section section--sand-deep"><div class="container"><div class="section-head"><h2>Included on every job</h2></div>{ledger()}</div></section>
''' + cta_band()


def page_areas():
    return f'''<section class="page-hero"><div class="container"><h1>Service areas</h1><p class="deck">Magic Touch Pressure Washing is based in Orlando and serves Kissimmee, Sanford and the surrounding Central Florida area. Not sure about your street? Call or text {PHONE}.</p></div></section>
<section class="section section--tight-top"><div class="container">{loc_grid()}</div></section>
{book_prompt()}
''' + cta_band()


def page_area(x):
    others = [o for o in AREAS if o is not x]
    rows = "".join('<a class="species-row" href="%s"><span class="species-row__name">%s in %s</span><span class="species-row__go">%s</span></a>' % (u("services/%s/" % s["slug"]), esc(s["name"]), x["name"], ICON["arrow"]) for s in SERVICES)
    return hero("%s &middot; Central Florida" % x["county"], "Pressure washing in %s" % x["name"], "", esc(x["deck"]), ph(x["name"], x["county"]), promise_line()) + f'''
<section class="section"><div class="container"><div class="tour-layout">
  <div class="prose">
    <h2>Exterior cleaning for {x["name"]} homes</h2>
    <p>Magic Touch Pressure Washing brings every service to {x["name"]}: roof soft washing, house washing, driveways and sidewalks, patio and pool decks, paver sealing, gutter cleaning and solar panel cleaning.</p>
    <p>Each job starts with a free, flat-rate estimate and comes with an on-time guarantee and a 1-year guarantee on the work.</p>
    <h3>How it works</h3>{steps_rail()}
  </div>
  {booking_panel("service in " + x["name"])}
</div></div></section>
<section class="section section--navy"><div class="container"><div class="species-split">
  <div><h2>Services in {x["name"]}</h2><p class="deck">Also serving {others[0]["name"]} and {others[1]["name"]}.</p><div class="cta-row mt-5">{est_btn("Get a free estimate", "area")}</div></div>
  <div class="species-list">{rows}</div>
</div></div></section>
''' + cta_band()


def page_about():
    return hero("Family-owned &middot; Orlando since 2020", "About Magic Touch", "", "Magic Touch Pressure Washing is a family-owned exterior cleaning company in Orlando, run by Trevean J. McLeod.", ph("Trevean McLeod", "Owner photo coming soon")) + f'''
<section class="section"><div class="container"><div class="tour-layout">
  <div class="prose">
    <h2>A family business built on three promises</h2>
    <p>Magic Touch Mobile Pressure Washing LLC was incorporated in Orlando in October 2020 by Trevean J. McLeod. Today Magic Touch cleans roofs, homes, driveways, pool decks and pavers for homeowners across Orlando, Kissimmee and Sanford.</p>
    <p>Every job comes with the same three promises: one flat-rate price quoted before the work starts, an on-time guarantee, and a 1-year guarantee on the cleaning. The company is licensed and insured.</p>
    <h3>What working with Magic Touch is like</h3>{steps_rail()}
  </div>
  {booking_panel("Magic Touch")}
</div></div></section>
{wall("45s", "The work", "A real Magic Touch walkway, before and after. More job photos are being added.")}
''' + cta_band("Put Magic Touch on the calendar")


def page_gallery():
    figs = "".join('<figure>%s<figcaption>%s</figcaption></figure>' % (pic(n, PHOTO_ALT[n]), t) for n, t in (("before", "Before"), ("after", "After")))
    figs += "".join('<figure>%s</figure>' % ph(s["name"]) for s in SERVICES)
    return f'''<section class="page-hero"><div class="container"><h1>Gallery</h1><p class="deck">Before and after photos from Magic Touch jobs. The walkway below is a real Magic Touch job; photos for each service are being added.</p></div></section>
<section class="section section--tight-top"><div class="container"><div class="gal-grid">{figs}</div>
<div class="cta-row cta-row--center mt-6"><a class="btn btn-ghost" href="{IG}" rel="noopener">{ICON["ig"]}More on Instagram</a></div></div></section>
''' + cta_band("Your home is the next after photo")


def page_faq():
    groups = "".join('<div class="section-head"><h2>%s</h2></div>%s<div class="mt-7"></div>' % (esc(g), acc(items, "f%d" % i)) for i, (g, items) in enumerate(FAQ_GROUPS))
    return f'''<section class="page-hero"><div class="container"><h1>Questions, answered</h1><p class="deck">Straight answers about estimates, methods and the company. Still unsure? Call or text {PHONE}.</p></div></section>
<section class="section"><div class="container container--narrow">{groups}</div></section>
''' + cta_band("Still deciding? Ask for a price anyway.")


def page_estimate():
    opts = "".join('<label class="trip-opt"><input type="checkbox" name="services" value="%s"%s><span class="trip-opt__body"><strong>%s</strong><span>%s</span></span></label>' % (esc(s["name"]), " checked" if i == 0 else "", esc(s["name"]), esc(s["chip"])) for i, s in enumerate(SERVICES))
    cities = "".join("<option>%s</option>" % x["name"] for x in AREAS) + "<option>Nearby area</option>"
    return f'''<section class="page-hero page-hero--book"><div class="container"><h1>Free estimate</h1><p class="deck">Tell Magic Touch what needs cleaning, or call or text {PHONE}. You get one flat-rate price before any work starts.</p></div></section>
<section class="section section--tight-top"><div class="container"><div class="book-layout">
  <form class="book-form" id="estimate-form" novalidate data-email="{EMAIL}">
    <fieldset><legend>1. What needs cleaning?</legend><div class="svc-check">{opts}</div></fieldset>
    <fieldset><legend>2. Where</legend><div class="field-row">
      <div class="field"><label for="ef-city">City</label><select id="ef-city" name="city">{cities}</select></div>
      <div class="field"><label for="ef-street">Street address <span class="opt">optional</span></label><input id="ef-street" name="address" type="text" autocomplete="street-address"></div>
    </div></fieldset>
    <fieldset><legend>3. Your details</legend><div class="field-row">
      <div class="field"><label for="ef-name">Name</label><input id="ef-name" name="name" type="text" autocomplete="name" required></div>
      <div class="field"><label for="ef-phone">Mobile number</label><input id="ef-phone" name="phone" type="tel" autocomplete="tel" inputmode="tel" required></div>
      <div class="field"><label for="ef-email">Email <span class="opt">optional</span></label><input id="ef-email" name="email" type="email" autocomplete="email"></div>
    </div>
    <div class="field"><label for="ef-notes">Anything Magic Touch should know <span class="opt">optional</span></label><textarea id="ef-notes" name="notes" rows="3" placeholder="Roof type, rough size of the driveway, pool deck or pavers, best days for the crew"></textarea></div></fieldset>
    <button class="btn btn-primary btn-lg btn-block" type="submit" data-cta="estimate-submit">Send estimate request{ICON["arrow"]}</button>
    <p class="form-status" id="form-status" role="status" hidden></p>
    <p class="form-fine">Sending opens your email app with the request addressed to {EMAIL}. See the <a href="{u("privacy/")}">privacy policy</a>.</p>
  </form>
  <aside class="book-side">
    <div class="side-card side-card--navy"><h2 class="side-card__h">What happens next</h2><div class="rail"><div class="rail__step"><span class="rail__time">1</span><h3 class="rail__h">Magic Touch reviews the request</h3><p>Photos of the area help, and can be texted to {PHONE}.</p></div><div class="rail__step"><span class="rail__time">2</span><h3 class="rail__h">You get a flat-rate price</h3><p>Free, with no hourly billing.</p></div><div class="rail__step"><span class="rail__time">3</span><h3 class="rail__h">The crew shows up on time</h3><p>Backed by the on-time guarantee and a 1-year guarantee on the work.</p></div></div></div>
    <div class="side-card"><h2 class="side-card__h">Prefer to talk?</h2><p>Call or text Magic Touch at <a class="side-card__tel" href="tel:{TEL}">{PHONE}</a>.</p><a class="btn btn-navy btn-block" data-cta="book-call" href="tel:{TEL}">{ICON["phone"]}Call {PHONE}</a><a class="btn btn-ghost btn-block mt-3" data-cta="book-text" href="{SMS}">Send a text</a></div>
    <div class="side-card side-card--photo">{ba_slider(lazy=True)}</div>
  </aside>
</div></div></section>
<section class="section section--sand-deep"><div class="container"><div class="section-head"><h2>Included on every job</h2></div>{ledger()}</div></section>
'''


def page_privacy():
    return f'''<section class="page-hero"><div class="container"><h1>Privacy policy</h1></div></section>
<section class="section section--tight-top"><div class="container container--narrow"><div class="prose">
<p>Magic Touch Pressure Washing uses the details you send through this website, by phone, by text or by email only to reply to your request, prepare an estimate and schedule the work.</p>
<p>Your details are not sold or shared with third parties for marketing.</p>
<p>To ask about or remove your information, email <a href="mailto:{EMAIL}">{EMAIL}</a> or call {PHONE}.</p>
</div></div></section>
'''


PAGES = [
    ("", page_home, "Pressure Washing Orlando FL | Magic Touch Pressure Washing", "Family-owned pressure washing and roof soft washing in Orlando, Kissimmee and Sanford. Free flat-rate estimates, on-time guarantee, 1-year guarantee. Call or text (321) 355-9521.", "home"),
    ("services/", page_services, "Services | Magic Touch Pressure Washing", "Roof soft washing, house washing, driveways, pool decks, paver sealing, gutter and solar panel cleaning in Orlando.", ""),
    ("service-areas/", page_areas, "Service Areas | Magic Touch Pressure Washing", "Pressure washing in Orlando, Kissimmee, Sanford and the surrounding Central Florida area.", ""),
    ("about/", page_about, "About | Magic Touch Pressure Washing", "Family-owned Orlando exterior cleaning company run by Trevean J. McLeod since 2020.", ""),
    ("gallery/", page_gallery, "Gallery | Magic Touch Pressure Washing", "Before and after photos from Magic Touch Pressure Washing jobs.", ""),
    ("faq/", page_faq, "FAQ | Magic Touch Pressure Washing", "Answers about estimates, soft washing, pressure washing and service areas.", ""),
    ("estimate/", page_estimate, "Free Estimate | Magic Touch Pressure Washing", "Request a free, flat-rate pressure washing estimate in Orlando, Kissimmee or Sanford.", "page-book"),
    ("privacy/", page_privacy, "Privacy Policy | Magic Touch Pressure Washing", "How Magic Touch Pressure Washing uses your details.", ""),
] + [("services/%s/" % s["slug"], (lambda s=s: page_service(s)), "%s in Orlando FL | Magic Touch Pressure Washing" % s["name"], s["desc"], "") for s in SERVICES] \
  + [("service-areas/%s/" % x["slug"], (lambda x=x: page_area(x)), "Pressure Washing in %s FL | Magic Touch Pressure Washing" % x["name"], x["deck"], "") for x in AREAS]


def build():
    global R
    bad = []
    for path, fn, title, desc, body in PAGES:
        R = "../" * path.count("/")
        out = head(dict(title=title, desc=desc, body=body)) + chrome_top() + fn() + chrome_bottom()
        text = re.sub(r"<[^>]+>", " ", out)
        if "—" in out or "–" in text:
            bad.append((path, "dash"))
        if re.search(r"\b(we|our|us|I)\b", re.sub(r"<script.*?</script>", "", text, flags=re.S)):
            bad.append((path, "first person: " + ", ".join(sorted(set(re.findall(r"\b(we|our|us|I)\b", text))))))
        if re.search(r"[★☆✦✧]", out):
            bad.append((path, "star glyph"))
        d = os.path.join(ROOT, path)
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "index.html"), "w").write(out)
    print("built %d pages" % len(PAGES))
    for b in bad:
        print("GATE", b)


if __name__ == "__main__":
    build()
