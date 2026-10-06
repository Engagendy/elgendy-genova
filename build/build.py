#!/usr/bin/env python3
"""Generate the static El Gendy Genova site (Arabic + English) from build/content.py.

Usage:  python3 build/build.py
Needs:  Pillow (only to read photo dimensions).
"""
import hashlib
import json
import os
import sys
from html import escape
from urllib.parse import quote, urlparse

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import content as C  # noqa: E402

ORIGIN = "{0.scheme}://{0.netloc}".format(urlparse(C.SITE))
LANGS = ("ar", "en")
PHOTOS = json.load(open(os.path.join(ROOT, "build", "photos.json")))
PHOTO_CAT = {pid: cat for cat, ids in PHOTOS.items() for pid in ids}
SERVICE_BY_SLUG = {s["slug"]: s for s in C.SERVICES}


def e(text):
    return escape(str(text), quote=True)


def asset_version(path):
    with open(os.path.join(ROOT, path), "rb") as fh:
        return hashlib.md5(fh.read()).hexdigest()[:8]


CSS_V = asset_version("assets/css/site.css")
JS_V = asset_version("assets/js/site.js")

# ------------------------------------------------------------------ URLs


def path(lang, page="", slug=None):
    prefix = C.BASE + ("en/" if lang == "en" else "")
    if page == "service":
        return f"{prefix}services/{slug}/"
    if page == "guide":
        return f"{prefix}guide/{C.GUIDE['slug']}/"
    if page == "gallery":
        return f"{prefix}gallery/"
    return prefix


def absolute(p):
    return ORIGIN + p


def img(pid, small=False):
    return f"{C.BASE}assets/img/p/{pid:03d}{'-sm' if small else ''}.webp"


_dims = {}


def dims(pid):
    if pid not in _dims:
        with Image.open(os.path.join(ROOT, "assets/img/p", f"{pid:03d}-sm.webp")) as im:
            _dims[pid] = im.size
    return _dims[pid]


def wa(text):
    return f"https://wa.me/{C.PHONE}?text={quote(text)}"


def alt_text(pid, lang, n=None):
    label = C.CATEGORIES[PHOTO_CAT[pid]][lang]
    suffix = f" ({n})" if n else ""
    return f"{label} — {C.UI[lang]['workBy']}{suffix}"


# ------------------------------------------------------------------ icons

ICON = {
    "factory": '<path d="M3 21h18M5 21V9l5 3V9l5 3V5l4 2v14"/>',
    "shield": '<path d="M12 3l7 3v6c0 4.5-3 7.5-7 9-4-1.5-7-4.5-7-9V6z"/><path d="M9 12l2 2 4-4"/>',
    "grid": '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 10h18M9 10v10"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "pin": '<path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
    "phone": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>',
}
WA_PATH = '<path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm5.3 14.1c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .2-3.3-.7-2.8-1.1-4.6-4-4.7-4.2-.1-.2-1.1-1.5-1.1-2.9s.7-2.1 1-2.4c.3-.3.6-.3.8-.3h.6c.2 0 .4 0 .6.5l.9 2.1c.1.2.1.4 0 .6l-.4.6-.4.5c-.1.1-.3.3-.1.6.2.3.8 1.3 1.7 2.1 1.2 1 2.1 1.4 2.4 1.5.3.1.5.1.6-.1l.9-1c.2-.3.4-.2.6-.1l2 .9c.3.1.5.2.5.3.1.2.1.7-.2 1.3z"/>'


def icon(name):
    return f'<svg viewBox="0 0 24 24" aria-hidden="true">{ICON[name]}</svg>'


# ------------------------------------------------------------------ schema


def business(lang):
    u = C.UI[lang]
    return {
        "@type": ["HomeAndConstructionBusiness", "LocalBusiness"],
        "@id": f"{C.SITE}/#business",
        "name": u["brand"],
        "alternateName": [C.UI["en" if lang == "ar" else "ar"]["brand"], "El Gendy Genova", "الجندي للمطابخ والشبابيك", "EL GENDY Kitchens & Windows"],
        "slogan": "Designed to Impress. Built to Last.",
        "description": C.HOME[lang]["desc"],
        "url": absolute(path(lang)),
        "logo": absolute(f"{C.BASE}assets/img/brand/logo-512.webp"),
        "image": absolute(f"{C.BASE}assets/img/brand/og-cover.jpg"),
        "telephone": "+" + C.PHONE,
        "email": C.EMAIL,
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "آخر شارع سامية الجمل، شارع السلاب" if lang == "ar" else "End of Samia El-Gamal St., El-Sallab St.",
            "addressLocality": "المنصورة" if lang == "ar" else "Mansoura",
            "addressRegion": "الدقهلية" if lang == "ar" else "Dakahlia",
            "addressCountry": "EG",
        },
        "areaServed": [
            {"@type": "City", "name": "المنصورة" if lang == "ar" else "Mansoura"},
            {"@type": "AdministrativeArea", "name": "محافظة الدقهلية" if lang == "ar" else "Dakahlia Governorate"},
        ],
        "sameAs": [C.FACEBOOK],
        "makesOffer": [
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": s[lang]["name"], "url": absolute(path(lang, "service", s["slug"]))}}
            for s in C.SERVICES
        ],
    }


def breadcrumb(items):
    return {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": name, "item": absolute(p)} for i, (name, p) in enumerate(items)
        ],
    }


def faq_schema(faqs):
    return {
        "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs],
    }


def webpage(lang, p, title, desc, kind="WebPage", image=None):
    node = {
        "@type": kind,
        "@id": absolute(p) + "#webpage",
        "url": absolute(p),
        "name": title,
        "description": desc,
        "inLanguage": "ar-EG" if lang == "ar" else "en",
        "isPartOf": {"@id": f"{C.SITE}/#website"},
        "about": {"@id": f"{C.SITE}/#business"},
        "dateModified": C.UPDATED,
    }
    if image:
        node["primaryImageOfPage"] = absolute(image)
    return node


def website():
    return {
        "@type": "WebSite",
        "@id": f"{C.SITE}/#website",
        "name": C.UI["ar"]["brand"],
        "alternateName": C.UI["en"]["brand"],
        "url": C.SITE + "/",
        "inLanguage": ["ar-EG", "en"],
        "publisher": {"@id": f"{C.SITE}/#business"},
    }


# ------------------------------------------------------------------ layout pieces


def head(lang, page, slug, title, desc, graph, og_type="website", og_image=None, preload=None):
    ar_p, en_p = path("ar", page, slug), path("en", page, slug)
    me = ar_p if lang == "ar" else en_p
    og_image = absolute(og_image or f"{C.BASE}assets/img/brand/og-cover.jpg")
    fonts = (
        "family=El+Messiri:wght@500;600;700&family=Readex+Pro:wght@300;400;500;600&family=Playfair+Display:wght@500;600"
        if lang == "ar"
        else "family=Playfair+Display:wght@500;600;700&family=Readex+Pro:wght@300;400;500;600"
    )
    font_url = e(f"https://fonts.googleapis.com/css2?{fonts}&display=swap")
    pre = f'\n  <link rel="preload" as="image" href="{e(preload)}" fetchpriority="high">' if preload else ""
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1)
    return f"""<!doctype html>
<html lang="{'ar' if lang == 'ar' else 'en'}" dir="{'rtl' if lang == 'ar' else 'ltr'}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(title)}</title>
  <meta name="description" content="{e(desc)}">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="{absolute(me)}">
  <link rel="alternate" hreflang="ar-EG" href="{absolute(ar_p)}">
  <link rel="alternate" hreflang="en" href="{absolute(en_p)}">
  <link rel="alternate" hreflang="x-default" href="{absolute(ar_p)}">
  <meta property="og:site_name" content="{e(C.UI[lang]['brand'])}">
  <meta property="og:title" content="{e(title)}">
  <meta property="og:description" content="{e(desc)}">
  <meta property="og:type" content="{og_type}">
  <meta property="og:url" content="{absolute(me)}">
  <meta property="og:image" content="{og_image}">
  <meta property="og:locale" content="{'ar_EG' if lang == 'ar' else 'en_US'}">
  <meta property="og:locale:alternate" content="{'en_US' if lang == 'ar' else 'ar_EG'}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{e(title)}">
  <meta name="twitter:description" content="{e(desc)}">
  <meta name="twitter:image" content="{og_image}">
  <meta name="theme-color" content="#faf6ef">
  <script>
    document.documentElement.classList.add('js');
    try {{ if (localStorage.getItem('elgendy-theme') === 'dark') document.documentElement.dataset.theme = 'dark'; }} catch (e) {{}}
  </script>
  <link rel="icon" href="{C.BASE}favicon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="{C.BASE}assets/img/brand/logo-160.png">
  <link rel="alternate" type="text/plain" href="{C.BASE}llms.txt" title="LLMs.txt">{pre}
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="preload" as="style" href="{font_url}" onload="this.onload=null;this.rel='stylesheet'">
  <noscript><link rel="stylesheet" href="{font_url}"></noscript>
  <link rel="stylesheet" href="{C.BASE}assets/css/site.css?v={CSS_V}">
  <script type="application/ld+json">
{ld}
  </script>
</head>
<body>
"""


def header(lang, page, slug):
    u = C.UI[lang]
    home = path(lang)
    ar_p, en_p = path("ar", page, slug), path("en", page, slug)
    services_href = "#services" if page == "" else home + "#services"
    return f"""  <header class="header" id="header">
    <div class="container nav">
      <a class="brand" href="{home}" aria-label="{e(u['brand'])}">
        <img src="{C.BASE}assets/img/brand/logo-160.png" alt="" width="50" height="50" decoding="async">
        <span>
          <strong>{e(u['brandShort'])}</strong>
          <span>{e(u['brandSub'])}</span>
        </span>
      </a>
      <nav class="nav-links" id="navLinks" aria-label="{e(u['mainMenu'])}">
        <a href="{services_href}">{e(u['navServices'])}</a>
        <a href="{path(lang, 'gallery')}">{e(u['navWorks'])}</a>
        <a href="{path(lang, 'guide')}">{e(u['navGuide'])}</a>
        <a href="#faq">{e(u['navFaq'])}</a>
        <a href="#contact">{e(u['navContact'])}</a>
      </nav>
      <div class="nav-actions">
        <div class="lang-switch" role="group" aria-label="{e(u['langLabel'])}">
          <a href="{ar_p}" hreflang="ar" lang="ar"{' aria-current="true"' if lang == 'ar' else ''}>ع</a>
          <a href="{en_p}" hreflang="en" lang="en"{' aria-current="true"' if lang == 'en' else ''}>EN</a>
        </div>
        <button class="theme-toggle" type="button" id="themeToggle" aria-pressed="false" aria-label="{e(u['darkMode'])}">
          <svg class="sun" viewBox="0 0 24 24" aria-hidden="true"><path d="M20.5 14.5A8.5 8.5 0 0 1 9.5 3.5a8.5 8.5 0 1 0 11 11z"/></svg>
          <svg class="moon" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4.2"/><path d="M12 2v2.2M12 19.8V22M4.9 4.9l1.6 1.6M17.5 17.5l1.6 1.6M2 12h2.2M19.8 12H22M4.9 19.1l1.6-1.6M17.5 6.5l1.6-1.6"/></svg>
        </button>
        <a class="btn btn-line" href="tel:+{C.PHONE}">{e(u['callNow'])}</a>
        <a class="btn btn-gold" href="{e(wa(u['waMessage']))}" target="_blank" rel="noopener">{e(u['whatsapp'])}</a>
        <button class="menu-toggle" type="button" aria-label="{e(u['menu'])}" aria-expanded="false" aria-controls="navLinks"><span></span><span></span><span></span></button>
      </div>
    </div>
  </header>
"""


def footer(lang):
    u = C.UI[lang]
    services = "\n".join(
        f'            <li><a href="{path(lang, "service", s["slug"])}">{e(s[lang]["name"])}</a></li>' for s in C.SERVICES
    )
    lb_prev = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M15 5l-7 7 7 7"/></svg>'
    lb_next = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 5l7 7-7 7"/></svg>'
    lb_close = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>'
    return f"""  <footer class="footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <a class="brand" href="{path(lang)}">
            <img src="{C.BASE}assets/img/brand/logo-160.png" alt="" width="50" height="50" loading="lazy" decoding="async">
            <span><strong>{e(u['brandShort'])}</strong><span>{e(u['brandSub'])}</span></span>
          </a>
          <p>{e(u['footerAbout'])}</p>
        </div>
        <div>
          <h3>{e(u['footerServices'])}</h3>
          <ul>
{services}
          </ul>
        </div>
        <div>
          <h3>{e(u['footerContact'])}</h3>
          <ul>
            <li><a href="tel:+{C.PHONE}" dir="ltr">{C.PHONE_DISPLAY}</a></li>
            <li><a href="mailto:{C.EMAIL}">{C.EMAIL}</a></li>
            <li><a href="{C.FACEBOOK}" target="_blank" rel="noopener">Facebook</a></li>
            <li><a href="{path(lang, 'gallery')}">{e(u['navWorks'])}</a></li>
            <li><a href="{path(lang, 'guide')}">{e(u['navGuide'])}</a></li>
            <li>{e(u['footerCity'])}</li>
          </ul>
        </div>
      </div>
      <div class="copy">
        <span>© <span id="year">2026</span> {e(u['brand'])}</span>
        <span>Designed to Impress. Built to Last.</span>
      </div>
    </div>
  </footer>

  <div class="float-actions">
    <a class="wa" href="{e(wa(u['waMessage']))}" target="_blank" rel="noopener" aria-label="{e(u['whatsapp'])}">
      <svg viewBox="0 0 24 24" fill="#fff" aria-hidden="true">{WA_PATH}</svg>
    </a>
    <a class="call" href="tel:+{C.PHONE}" aria-label="{e(u['callNow'])}">
      <svg viewBox="0 0 24 24" fill="none" stroke="#1a1408" stroke-width="1.8" aria-hidden="true">{ICON['phone']}</svg>
    </a>
  </div>

  <div class="lightbox" id="lightbox" role="dialog" aria-modal="true" aria-labelledby="lbTitle" aria-hidden="true">
    <div class="lb-head">
      <div><strong id="lbTitle"></strong><span id="lbCount"></span></div>
      <button class="icon-btn" type="button" id="lbClose" aria-label="{e(u['close'])}">{lb_close}</button>
    </div>
    <div class="lb-stage">
      <img id="lbImg" src="data:," alt="">
      <button class="icon-btn lb-nav lb-prev" type="button" id="lbPrev" aria-label="{e(u['prev'])}">{lb_prev}</button>
      <button class="icon-btn lb-nav lb-next" type="button" id="lbNext" aria-label="{e(u['next'])}">{lb_next}</button>
    </div>
    <div class="lb-thumbs" id="lbThumbs"></div>
  </div>

  <script src="{C.BASE}assets/js/site.js?v={JS_V}" defer></script>
</body>
</html>
"""


def section_head(kicker, title, lead, h="h2", tag_id=None):
    hid = f' id="{tag_id}"' if tag_id else ""
    return f"""        <div class="section-head reveal">
          <div>
            <p class="kicker">{e(kicker)}</p>
            <{h}{hid}>{e(title)}</{h}>
          </div>
          <p>{e(lead)}</p>
        </div>
"""


def works_grid(lang, ids, grid_id, page=None, filters=False):
    u = C.UI[lang]
    items = []
    counter = {}
    for pid in ids:
        cat = PHOTO_CAT[pid]
        counter[cat] = counter.get(cat, 0) + 1
        w, h = dims(pid)
        label = C.CATEGORIES[cat][lang]
        items.append(
            f'          <a class="work" href="{img(pid)}" data-cat="{cat}" data-label="{e(label)}">'
            f'<img src="{img(pid, True)}" alt="{e(alt_text(pid, lang, counter[cat]))}" width="{w}" height="{h}" loading="lazy" decoding="async"></a>'
        )
    out = ""
    if filters:
        cats = [c for c in C.CATEGORIES if any(PHOTO_CAT[p] == c for p in ids)]
        btns = [f'<button type="button" data-filter="all" aria-pressed="true">{e(u["all"])}<span>{len(ids)}</span></button>']
        for c in cats:
            n = sum(1 for p in ids if PHOTO_CAT[p] == c)
            btns.append(f'<button type="button" data-filter="{c}" aria-pressed="false">{e(C.CATEGORIES[c][lang])}<span>{n}</span></button>')
        out += f'        <div class="filters reveal" data-filters="{grid_id}" role="group">\n          ' + "\n          ".join(btns) + "\n        </div>\n"
    page_attr = f' data-page="{page}"' if page else ""
    out += f'        <div class="works-grid" id="{grid_id}" data-gallery{page_attr}>\n' + "\n".join(items) + "\n        </div>\n"
    return out


def faq_section(lang, faqs, title, lead):
    u = C.UI[lang]
    items = "\n".join(
        f"""          <details{' open' if i == 0 else ''}>
            <summary>{e(q)}</summary>
            <p>{e(a)}</p>
          </details>"""
        for i, (q, a) in enumerate(faqs)
    )
    return f"""    <section class="section" id="faq">
      <div class="container faq-grid">
        <div class="reveal">
          <p class="kicker">{e(u['faqKicker'])}</p>
          <h2 style="font-size: clamp(1.9rem, 3.4vw, 2.9rem);">{e(title)}</h2>
          <p style="color: var(--muted); margin-top: 14px;">{e(lead)}</p>
        </div>
        <div class="faq-list reveal">
{items}
        </div>
      </div>
    </section>
"""


def quote_form(lang, selected=None):
    u = C.UI[lang]
    opts = []
    for s in C.SERVICES:
        sel = " selected" if s["slug"] == selected else ""
        opts.append(f"<option{sel}>{e(s[lang]['name'])}</option>")
    opts.append(f"<option>{e(u['fMore'])}</option>")
    options = "\n                ".join(opts)
    return f"""        <aside class="quote reveal">
          <h2>{e(u['quoteTitle'])}</h2>
          <p>{e(u['quoteLead'])}</p>
          <form class="form" id="quoteForm" data-phone="{C.PHONE}" data-intro="{e(u['quoteIntro'])}">
            <div class="field">
              <label for="qName">{e(u['fName'])}</label>
              <input id="qName" name="name" autocomplete="name" required placeholder="{e(u['fNamePh'])}">
            </div>
            <div class="field">
              <label for="qPhone">{e(u['fPhone'])}</label>
              <input id="qPhone" name="phone" autocomplete="tel" inputmode="tel" required placeholder="01xxxxxxxxx" dir="ltr">
            </div>
            <div class="field">
              <label for="qService">{e(u['fService'])}</label>
              <select id="qService" name="service">
                {options}
              </select>
            </div>
            <div class="field">
              <label for="qArea">{e(u['fArea'])}</label>
              <input id="qArea" name="area" placeholder="{e(u['fAreaPh'])}">
            </div>
            <div class="field full">
              <label for="qMsg">{e(u['fMsg'])}</label>
              <textarea id="qMsg" name="message" placeholder="{e(u['fMsgPh'])}"></textarea>
            </div>
            <button class="btn btn-gold" type="submit">
              <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">{WA_PATH}</svg>
              <span>{e(u['send'])}</span>
            </button>
          </form>
        </aside>
"""


def mini_steps(lang):
    return "\n".join(
        f"            <li><strong>{e(t)}</strong><span>{e(d)}</span></li>" for t, d in C.UI[lang]["steps"]
    )


def contact_section(lang, left_html, selected=None, top_pad=True):
    style = "" if top_pad else ' style="padding-top: 0;"'
    return f"""    <section class="section" id="contact"{style}>
      <div class="container why-grid">
{left_html}
{quote_form(lang, selected)}
      </div>
    </section>
"""


def process_left(lang):
    u = C.UI[lang]
    return f"""        <div class="reveal">
          <p class="kicker">{e(u['processKicker'])}</p>
          <h2 style="font-size: clamp(1.8rem, 3.2vw, 2.6rem); margin-bottom: 26px;">{e(C.HOME[lang]['processTitle'])}</h2>
          <ol class="mini-steps">
{mini_steps(lang)}
          </ol>
        </div>"""


def visit_section(lang):
    u = C.UI[lang]
    h = C.HOME[lang]
    return f"""    <section class="section visit" id="visit">
      <div class="container">
{section_head(h['visitKicker'], h['visitTitle'], h['visitLead'])}        <div class="visit-grid">
          <article class="place reveal">
            {icon('pin')}
            <h3>{e(u['showroom'])}</h3>
            <p>{e(u['showroomAddr'])}</p>
            <a class="more" href="{e(C.MAP_SHOWROOM)}" target="_blank" rel="noopener">{e(u['openMap'])}</a>
          </article>
          <article class="place reveal">
            {icon('factory')}
            <h3>{e(u['factory'])}</h3>
            <p>{e(u['factoryAddr'])}</p>
            <a class="more" href="{e(C.MAP_FACTORY)}" target="_blank" rel="noopener">{e(u['openMap'])}</a>
          </article>
          <article class="place reveal">
            {icon('phone')}
            <h3>{e(u['reach'])}</h3>
            <p><a href="tel:+{C.PHONE}" dir="ltr">{C.PHONE_DISPLAY}</a><br><a href="mailto:{C.EMAIL}">{C.EMAIL}</a></p>
            <a class="more" href="{e(wa(u['waMessage']))}" target="_blank" rel="noopener">{e(u['chatWa'])}</a>
          </article>
        </div>
      </div>
    </section>
"""


def cta_section(lang, message=None):
    u = C.UI[lang]
    return f"""    <section class="cta">
      <div class="container">
        <div class="cta-box reveal">
          <div>
            <h2>{e(u['ctaTitle'])}</h2>
            <p>{e(u['ctaLead'])}</p>
          </div>
          <div class="cta-actions">
            <a class="btn btn-gold" href="{e(wa(message or u['waMessage']))}" target="_blank" rel="noopener">{e(u['ctaWa'])}</a>
            <a class="btn btn-line" href="tel:+{C.PHONE}">{e(u['callNow'])}</a>
          </div>
        </div>
      </div>
    </section>
"""


def service_thumb(svc, cls=""):
    if svc["hero"] is None:
        return '<div class="glass-art"></div>'
    return f'<img src="{img(svc["hero"], True)}" alt="" loading="lazy" decoding="async"{cls}>'


def related_section(lang, exclude, slugs=None):
    u = C.UI[lang]
    picks = [SERVICE_BY_SLUG[s] for s in slugs] if slugs else [s for s in C.SERVICES if s["slug"] != exclude][:3]
    if not slugs:
        # Prefer services from a different family first (kitchens <-> windows)
        others = [s for s in C.SERVICES if s["slug"] != exclude]
        picks = others[:3] if exclude not in ("aluminum-kitchens", "wood-kitchens") else [s for s in others if "kitchen" not in s["slug"]][:2] + [s for s in others if "kitchen" in s["slug"]][:1]
    cards = "\n".join(
        f"""          <a href="{path(lang, 'service', s['slug'])}" class="reveal">
            {service_thumb(s)}
            <span><strong>{e(s[lang]['name'])}</strong><small>{e(s[lang]['card'])}</small></span>
          </a>"""
        for s in picks
    )
    return f"""    <section class="section" style="padding-top: 0;">
      <div class="container">
        <div class="section-head reveal">
          <div>
            <p class="kicker">{e(u['relatedKicker'])}</p>
            <h2>{e(u['relatedTitle'])}</h2>
          </div>
          <p></p>
        </div>
        <div class="related">
{cards}
        </div>
      </div>
    </section>
"""


def crumbs_html(items):
    lis = []
    for i, (name, p) in enumerate(items):
        if i == len(items) - 1:
            lis.append(f'<li aria-current="page">{e(name)}</li>')
        else:
            lis.append(f'<li><a href="{p}">{e(name)}</a></li>')
    return '<ol class="crumbs">' + "".join(lis) + "</ol>"


def write(rel, html):
    full = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as fh:
        fh.write(html)


# ------------------------------------------------------------------ pages


def interleave(cats, limit):
    lists = [list(PHOTOS[c]) for c in cats]
    out = []
    i = 0
    while len(out) < limit and any(i < len(l) for l in lists):
        for l in lists:
            if i < len(l) and len(out) < limit:
                out.append(l[i])
        i += 1
    return out


def build_home(lang):
    u, h = C.UI[lang], C.HOME[lang]
    p = path(lang)
    graph = [
        website(),
        business(lang),
        webpage(lang, p, h["title"], h["desc"], image=img(26)),
        faq_schema(h["faqs"]),
    ]
    out = head(lang, "", None, h["title"], h["desc"], graph, preload=img(26))
    out += header(lang, "", None)

    tags = "\n".join(f"            <span>{e(s[lang]['name'])}</span>" for s in C.SERVICES[:4])
    stats = "\n".join(f'        <div class="stat"><strong>{e(a)}</strong><span>{e(b)}</span></div>' for a, b in h["stats"])
    cards = []
    for i, s in enumerate(C.SERVICES):
        media = '<div class="glass-art"></div>' if s["hero"] is None else f'<img src="{img(s["hero"], True)}" alt="" loading="lazy" decoding="async">'
        cards.append(f"""          <article class="service reveal">
            {media}
            <span class="tag">0{i + 1}</span>
            <h3><a class="service-link" href="{path(lang, 'service', s['slug'])}" aria-label="{e(s[lang]['name'])}"></a>{e(s[lang]['name'])}</h3>
            <p>{e(s[lang]['card'])}</p>
            <span class="more">{e(u['learnMore'])}</span>
          </article>""")
    tabs, panels = [], []
    for i, (key, label, pid, title, lead, checks, best) in enumerate(h["materials"]):
        on = i == 0
        tabs.append(f'<button type="button" role="tab" id="tab-{key}" aria-controls="panel-{key}" aria-selected="{str(on).lower()}"{"" if on else " tabindex=\"-1\""}>{e(label)}</button>')
        lis = "\n".join(f"              <li>{e(c)}</li>" for c in checks)
        panels.append(f"""        <div class="tab-panel{' reveal' if on else ''}" role="tabpanel" id="panel-{key}" aria-labelledby="tab-{key}"{'' if on else ' hidden'}>
          <img src="{img(pid)}" alt="{e(alt_text(pid, lang))}" loading="lazy" decoding="async">
          <div class="tab-body">
            <h3>{e(title)}</h3>
            <p>{e(lead)}</p>
            <ul class="checks">
{lis}
            </ul>
            <p class="best-for"><b>{e(h['bestFor'])}</b> {e(best)}</p>
          </div>
        </div>""")
    timeline = "\n".join(
        f'          <article class="step reveal"><b>{i + 1}</b><h3>{e(t)}</h3><p>{e(d)}</p></article>' for i, (t, d) in enumerate(u["steps"])
    )
    reels = "\n".join(
        f"""          <a class="reel reveal" href="{C.FACEBOOK}/reels" target="_blank" rel="noopener">
            <img src="{img(pid, True)}" alt="" loading="lazy" decoding="async">
            <span class="play"><svg viewBox="0 0 24 24"><path d="M7 4.5v15l13-7.5z"/></svg></span>
            <span class="reel-text"><strong>{e(t)}</strong><small>{e(d)}</small></span>
          </a>"""
        for pid, t, d in h["reels"]
    )
    why = "\n".join(
        f"""            <div class="why-item">
              {icon(ic)}
              <div><strong>{e(t)}</strong><p>{e(d)}</p></div>
            </div>"""
        for ic, t, d in h["whyItems"]
    )
    why_left = f"""        <div class="reveal">
          <p class="kicker">{e(h['whyKicker'])}</p>
          <h2 style="font-size: clamp(1.9rem, 3.4vw, 2.9rem);">{e(h['whyTitle'])}</h2>
          <div class="why-list">
{why}
          </div>
        </div>"""
    home_works = interleave(["modern", "upvc", "alukitchen", "doors", "aluwindow", "classic", "decor"], 12)

    out += f"""
  <main id="top">
    <section class="hero">
      <div class="container hero-grid">
        <div class="reveal">
          <p class="kicker">{e(u['tagline'])}</p>
          <h1><span class="gold-text">{e(h['heroTitle'])}</span><small>{e(h['heroSub'])}</small></h1>
          <p class="hero-lead">{e(h['heroLead'])}</p>
          <div class="hero-actions">
            <a class="btn btn-gold" href="#contact">{e(u['freeConsult'])}</a>
            <a class="btn btn-line" href="#works">{e(u['seeWorks'])}</a>
          </div>
          <div class="hero-tags">
{tags}
          </div>
        </div>
        <div class="mosaic reveal">
          <figure>
            <img src="{img(26)}" alt="{e(h['mosaic'][0])}" fetchpriority="high" decoding="async" width="1280" height="960">
            <figcaption>{e(h['mosaic'][0])}</figcaption>
          </figure>
          <figure>
            <img src="{img(99, True)}" alt="{e(h['mosaic'][1])}" decoding="async" width="420" height="560">
            <figcaption>{e(h['mosaic'][1])}</figcaption>
          </figure>
          <figure>
            <img src="{img(97, True)}" alt="{e(h['mosaic'][2])}" decoding="async" width="420" height="560">
            <figcaption>{e(h['mosaic'][2])}</figcaption>
          </figure>
          <div class="seal" aria-hidden="true">
            <svg viewBox="0 0 120 120" direction="ltr">
              <defs><path id="circle" d="M60,60 m-48,0 a48,48 0 1,1 96,0 a48,48 0 1,1 -96,0"></path></defs>
              <text><textPath href="#circle" textLength="298" lengthAdjust="spacing">EL GENDY · GENOVA · MANSOURA · </textPath></text>
            </svg>
            <b>EG</b>
          </div>
        </div>
      </div>
    </section>

    <section class="stats">
      <div class="container stats-grid">
{stats}
      </div>
    </section>

    <section class="section" id="services">
      <div class="container">
{section_head(h['servicesKicker'], h['servicesTitle'], h['servicesLead'])}        <div class="services-grid">
{chr(10).join(cards)}
        </div>
      </div>
    </section>

    <section class="section materials" id="materials">
      <div class="container">
{section_head(h['matKicker'], h['matTitle'], h['matLead'])}        <div class="tabs reveal" role="tablist" aria-label="{e(h['matKicker'])}">
          {chr(10).join('          ' + t if i else t for i, t in enumerate(tabs))}
        </div>
{chr(10).join(panels)}
        <a class="section-link" href="{path(lang, 'guide')}" style="color: var(--gold-deep);">{e(h['matGuide'])}</a>
      </div>
    </section>

    <section class="section" id="works">
      <div class="container">
{section_head(u['worksKicker'], h['worksTitle'], h['worksLead'])}{works_grid(lang, home_works, 'homeWorks')}        <div class="works-more">
          <a class="btn btn-gold" href="{path(lang, 'gallery')}">{e(u['allPhotos'])}</a>
          <a class="btn btn-line" href="{C.FACEBOOK}/photos" target="_blank" rel="noopener">{e(u['moreOnFb'])}</a>
        </div>
      </div>
    </section>

    <section class="section process" id="process">
      <div class="container">
{section_head(u['processKicker'], h['processTitle'], h['processLead'])}        <div class="timeline">
{timeline}
        </div>
      </div>
    </section>

    <section class="section" id="reels">
      <div class="container">
{section_head(h['reelsKicker'], h['reelsTitle'], h['reelsLead'])}        <div class="reels-grid">
{reels}
        </div>
      </div>
    </section>

{contact_section(lang, why_left, top_pad=False)}
{visit_section(lang)}
{faq_section(lang, h['faqs'], h['faqTitle'], h['faqLead'])}
{cta_section(lang)}  </main>

"""
    out += footer(lang)
    write(("en/" if lang == "en" else "") + "index.html", out)


def build_service(lang, svc):
    u = C.UI[lang]
    s = svc[lang]
    slug = svc["slug"]
    p = path(lang, "service", slug)
    ids = [pid for c in svc["cats"] for pid in PHOTOS[c]]
    hero_img = img(svc["hero"]) if svc["hero"] is not None else None
    crumbs = [(u["home"], path(lang)), (u["navServices"], path(lang) + "#services"), (s["name"], p)]
    service_node = {
        "@type": "Service",
        "@id": absolute(p) + "#service",
        "name": s["name"],
        "serviceType": s["name"],
        "description": s["desc"],
        "url": absolute(p),
        "provider": {"@id": f"{C.SITE}/#business"},
        "areaServed": {"@type": "City", "name": u["city"]},
        "availableLanguage": ["ar", "en"],
    }
    if ids:
        service_node["image"] = [absolute(img(pid)) for pid in ids[:6]]
    graph = [
        business(lang),
        webpage(lang, p, s["title"], s["desc"], image=hero_img),
        service_node,
        breadcrumb(crumbs),
        faq_schema(s["faqs"]),
    ]
    waq = (
        f"السلام عليكم، عايز أستفسر عن {s['name']} من الجندي جينوفا"
        if lang == "ar"
        else f"Hello, I would like to ask about {s['name']} from El Gendy Genova"
    )
    out = head(lang, "service", slug, s["title"], s["desc"], graph, og_image=hero_img, preload=hero_img)
    out += header(lang, "service", slug)

    media = (
        f'<img src="{hero_img}" alt="{e(s["h1"])}" fetchpriority="high" decoding="async">'
        if hero_img
        else '<div class="glass-art"></div>'
    )
    facts = "\n".join(f"            <span>{e(f)}</span>" for f in s["facts"])
    intro = "\n".join(f"          <p>{e(t)}</p>" for t in s["intro"])
    why = "\n".join(f"              <li>{e(t)}</li>" for t in s["why"])
    types = "\n".join(
        f"""          <article class="card reveal"><span class="num">0{i + 1}</span><h3>{e(t)}</h3><p>{e(d)}</p></article>"""
        for i, (t, d) in enumerate(s["types"])
    )
    factors = "\n".join(
        f"            <li><b>{i + 1}</b><div><strong>{e(t)}</strong><span>{e(d)}</span></div></li>" for i, (t, d) in enumerate(s["factors"])
    )
    guide_link = (
        f'<a class="section-link" href="{path(lang, "guide")}">{e(C.HOME[lang]["matGuide"])}</a>'
        if slug in ("upvc-windows-doors", "aluminum-windows-facades", "aluminum-kitchens", "wood-kitchens")
        else ""
    )
    factors_lead = (
        "الأسعار بتتغير مع أسعار الخامات، فبدل رقم ممكن يبقى قديم، دي العوامل اللي فعلًا بتحدد تكلفة شغلك. ابعتلنا المقاسات وناخد عرض سعر دقيق."
        if lang == "ar"
        else "Prices move with material costs, so instead of a number that quickly goes stale, these are the factors that actually set your cost. Send us your measurements for an exact quote."
    )
    factors_title = "عرض سعر واضح… من غير مفاجآت" if lang == "ar" else "A clear quote, no surprises"

    if ids:
        works_title = (f"من أعمالنا في {s['name']}" if lang == "ar" else f"Our {s['name']} projects")
        works_lead = (
            "صور حقيقية من مشاريع نفّذناها في المنصورة. اضغط على أي صورة لعرضها بالحجم الكامل."
            if lang == "ar"
            else "Real photos from projects we built in Mansoura. Tap any photo to view it full size."
        )
        works = f"""    <section class="section" id="works">
      <div class="container">
{section_head(u['worksKicker'], works_title, works_lead)}{works_grid(lang, ids, 'svcWorks', page=12, filters=len(svc['cats']) > 1)}        <div class="works-more">
          <button class="btn btn-line" type="button" data-more="svcWorks">{e(u['loadMore'])}</button>
          <a class="btn btn-line" href="{path(lang, 'gallery')}">{e(u['allPhotos'])}</a>
        </div>
      </div>
    </section>
"""
    else:
        note = (
            "صور كبائن الشاور اللي نفّذناها بنبعتها على واتساب حسب الشكل اللي بتدور عليه — اطلبها وإحنا نرد عليك بسرعة."
            if lang == "ar"
            else "We share photos of shower enclosures we have installed on WhatsApp, matched to the style you want — just ask and we will reply quickly."
        )
        works = f"""    <section class="section" id="works" style="padding-top: 0;">
      <div class="container">
        <p class="note reveal">{e(note)} <a href="{e(wa(waq))}" target="_blank" rel="noopener" style="color: var(--gold);">{e(u['chatWa'])}</a></p>
      </div>
    </section>
"""

    out += f"""
  <main id="top">
    <section class="page-hero">
      <div class="container page-hero-grid">
        <div class="reveal">
          {crumbs_html(crumbs)}
          <p class="kicker">{e(u['brand'])}</p>
          <h1>{e(s['h1'])}</h1>
          <p class="lead">{e(s['lead'])}</p>
          <div class="hero-actions">
            <a class="btn btn-gold" href="{e(wa(waq))}" target="_blank" rel="noopener">{e(u['whatsapp'])}</a>
            <a class="btn btn-line" href="#contact">{e(u['freeConsult'])}</a>
          </div>
          <div class="quick-facts">
{facts}
          </div>
        </div>
        <div class="page-hero-media reveal">
          {media}
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container split-2">
        <div class="reveal">
          <h2>{e(s['introTitle'])}</h2>
{intro}
        </div>
        <div class="card reveal">
          <h3>{e(s['whyTitle'])}</h3>
          <ul class="checks" style="grid-template-columns: 1fr; margin: 14px 0 0;">
{why}
          </ul>
        </div>
      </div>
    </section>

    <section class="section alt-band">
      <div class="container">
        <div class="section-head reveal">
          <div>
            <p class="kicker">{e(u['navServices'])}</p>
            <h2>{e(s['typesTitle'])}</h2>
          </div>
          <p>{e(s['card'])}</p>
        </div>
        <div class="card-grid">
{types}
        </div>
      </div>
    </section>

{works}
    <section class="section alt-band">
      <div class="container split-2">
        <div class="reveal">
          <p class="kicker">{e(u['factorsKicker'])}</p>
          <h2>{e(factors_title)}</h2>
          <p>{e(factors_lead)}</p>
          {guide_link}
        </div>
        <ol class="factor-list reveal">
{factors}
        </ol>
      </div>
    </section>

{contact_section(lang, process_left(lang), selected=slug)}
{faq_section(lang, s['faqs'], s['name'] + (' — أسئلة شائعة' if lang == 'ar' else ' — FAQ'), C.HOME[lang]['faqLead'])}
{related_section(lang, slug)}
{cta_section(lang, waq)}  </main>

"""
    out += footer(lang)
    write(("en/" if lang == "en" else "") + f"services/{slug}/index.html", out)


def build_gallery(lang):
    u, g = C.UI[lang], C.GALLERY[lang]
    p = path(lang, "gallery")
    order = ["modern", "alukitchen", "upvc", "aluwindow", "doors", "classic", "decor", "details"]
    ids = interleave(order, 10_000)
    crumbs = [(u["home"], path(lang)), (g["h1"], p)]
    gallery_node = webpage(lang, p, g["title"], g["desc"], kind="CollectionPage", image=img(26))
    gallery_node["mainEntity"] = {
        "@type": "ImageGallery",
        "name": g["h1"],
        "associatedMedia": [
            {"@type": "ImageObject", "contentUrl": absolute(img(pid)), "thumbnailUrl": absolute(img(pid, True)), "caption": alt_text(pid, lang)}
            for pid in ids[:40]
        ],
    }
    faqs = C.HOME[lang]["faqs"][:3]
    graph = [business(lang), gallery_node, breadcrumb(crumbs), faq_schema(faqs)]
    out = head(lang, "gallery", None, g["title"], g["desc"], graph)
    out += header(lang, "gallery", None)
    out += f"""
  <main id="top">
    <section class="page-hero">
      <div class="container reveal">
        {crumbs_html(crumbs)}
        <p class="kicker">{e(u['worksKicker'])}</p>
        <h1>{e(g['h1'])}</h1>
        <p class="lead">{e(g['lead'])}</p>
      </div>
    </section>

    <section class="section" id="works" style="padding-top: 56px;">
      <div class="container">
{works_grid(lang, ids, 'galleryGrid', page=24, filters=True)}        <div class="works-more">
          <button class="btn btn-line" type="button" data-more="galleryGrid">{e(u['loadMore'])}</button>
          <a class="btn btn-line" href="{C.FACEBOOK}/photos" target="_blank" rel="noopener">{e(u['moreOnFb'])}</a>
        </div>
      </div>
    </section>

{related_section(lang, None, ["aluminum-kitchens", "wood-kitchens", "upvc-windows-doors"])}
{contact_section(lang, process_left(lang))}
{faq_section(lang, faqs, C.HOME[lang]['faqTitle'], C.HOME[lang]['faqLead'])}
{cta_section(lang)}  </main>

"""
    out += footer(lang)
    write(("en/" if lang == "en" else "") + "gallery/index.html", out)


def build_guide(lang):
    u, g = C.UI[lang], C.GUIDE[lang]
    p = path(lang, "guide")
    hero = img(C.GUIDE["hero"])
    crumbs = [(u["home"], path(lang)), (u["navGuide"], p)]
    article = {
        "@type": "Article",
        "@id": absolute(p) + "#article",
        "headline": g["h1"],
        "description": g["desc"],
        "image": absolute(hero),
        "datePublished": C.UPDATED,
        "dateModified": C.UPDATED,
        "inLanguage": "ar-EG" if lang == "ar" else "en",
        "author": {"@id": f"{C.SITE}/#business"},
        "publisher": {"@id": f"{C.SITE}/#business"},
        "mainEntityOfPage": absolute(p),
        "about": [{"@id": absolute(path(lang, "service", s)) + "#service"} for s in ("upvc-windows-doors", "aluminum-windows-facades")],
    }
    graph = [business(lang), webpage(lang, p, g["title"], g["desc"], image=hero), article, breadcrumb(crumbs), faq_schema(g["faqs"])]

    def links(html):
        html = html.replace("{gallery}", path(lang, "gallery")).replace("{contact}", "#contact")
        for s in C.SERVICES:
            html = html.replace("{svc:" + s["slug"] + "}", path(lang, "service", s["slug"]))
        return html

    toc = "\n".join(f'            <li><a href="#{sid}">{e(t)}</a></li>' for sid, t, _ in g["sections"])
    body = "\n".join(f'          <h2 id="{sid}">{e(t)}</h2>{links(html)}' for sid, t, html in g["sections"])
    fig_cap = alt_text(C.GUIDE["hero"], lang)
    out = head(lang, "guide", None, g["title"], g["desc"], graph, og_type="article", og_image=hero, preload=None)
    out += header(lang, "guide", None)
    out += f"""
  <main id="top">
    <section class="page-hero">
      <div class="container reveal">
        {crumbs_html(crumbs)}
        <p class="kicker">{e(u['navGuide'])}</p>
        <h1>{e(g['h1'])}</h1>
        <p class="lead">{e(g['lead'])}</p>
        <p class="meta-line">{e(u['updated'])}: <time datetime="{C.UPDATED}">{C.UPDATED}</time> · {e(u['brand'])}</p>
      </div>
    </section>

    <section class="section">
      <div class="container article-wrap">
        <nav class="toc reveal" aria-label="{e(g['toc'])}">
          <strong>{e(g['toc'])}</strong>
          <ol>
{toc}
          </ol>
        </nav>
        <article class="prose">
          <div class="tldr"><strong>{e(g['tldrTitle'])}</strong>{e(g['tldr'])}</div>
          <figure>
            <img src="{hero}" alt="{e(fig_cap)}" loading="lazy" decoding="async">
            <figcaption>{e(fig_cap)}</figcaption>
          </figure>
{body}
        </article>
      </div>
    </section>

{faq_section(lang, g['faqs'], g['h1'].split('؟')[0] + ('؟' if lang == 'ar' else '') if lang == 'ar' else 'Aluminum vs UPVC — FAQ', C.HOME[lang]['faqLead'])}
{related_section(lang, None, ["upvc-windows-doors", "aluminum-windows-facades", "aluminum-kitchens"])}
{contact_section(lang, process_left(lang), selected="upvc-windows-doors")}
{cta_section(lang)}  </main>

"""
    out += footer(lang)
    write(("en/" if lang == "en" else "") + f"guide/{C.GUIDE['slug']}/index.html", out)


def build_extras():
    # Legacy URL from the first version
    target = path("en")
    write(
        "en.html",
        f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>El Gendy Genova</title>
  <link rel="canonical" href="{absolute(target)}">
  <meta name="robots" content="noindex, follow">
  <meta http-equiv="refresh" content="0; url={target}">
  <script>location.replace({json.dumps(target)} + location.hash);</script>
</head>
<body><a href="{target}">El Gendy Genova — English</a></body>
</html>
""",
    )
    write(
        "404.html",
        f"""<!doctype html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>الصفحة غير موجودة | Page not found — الجندي جينوفا</title>
  <meta name="robots" content="noindex">
  <link rel="icon" href="{C.BASE}favicon.svg" type="image/svg+xml">
  <style>
    body {{ margin: 0; min-height: 100vh; display: grid; place-items: center; font-family: system-ui, sans-serif; background: #faf6ef; color: #1d1a15; text-align: center; padding: 24px; }}
    h1 {{ font-size: 2rem; margin: 0 0 8px; color: #8f6d2f; }}
    p {{ color: #6b6253; }}
    a {{ display: inline-block; margin: 6px; padding: 12px 22px; border-radius: 999px; background: #d4af6a; color: #1a1408; text-decoration: none; font-weight: 600; }}
    a.alt {{ background: transparent; border: 1px solid #d4af6a; }}
  </style>
</head>
<body>
  <main>
    <h1>404</h1>
    <p>الصفحة دي مش موجودة. — This page could not be found.</p>
    <a href="{path('ar')}">الرئيسية</a>
    <a class="alt" href="{path('en')}" lang="en">English home</a>
    <a class="alt" href="{path('ar', 'gallery')}">معرض الأعمال</a>
  </main>
</body>
</html>
""",
    )

    # Sitemap
    pages = [("", None), ("gallery", None), ("guide", None)] + [("service", s["slug"]) for s in C.SERVICES]
    urls = []
    for page, slug in pages:
        ar_p, en_p = path("ar", page, slug), path("en", page, slug)
        for me in (ar_p, en_p):
            urls.append(
                f"""  <url>
    <loc>{absolute(me)}</loc>
    <lastmod>{C.UPDATED}</lastmod>
    <xhtml:link rel="alternate" hreflang="ar-EG" href="{absolute(ar_p)}"/>
    <xhtml:link rel="alternate" hreflang="en" href="{absolute(en_p)}"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="{absolute(ar_p)}"/>
  </url>"""
            )
    write(
        "sitemap.xml",
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
        + "\n".join(urls)
        + "\n</urlset>\n",
    )
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {C.SITE}/sitemap.xml\n")

    # llms.txt
    svc_lines = "\n".join(
        f"- [{s['en']['name']} / {s['ar']['name']}]({absolute(path('en', 'service', s['slug']))}): {s['en']['desc']} Arabic: {absolute(path('ar', 'service', s['slug']))}"
        for s in C.SERVICES
    )
    faq_lines = "\n".join(f"- Q: {q}\n  A: {a}" for q, a in C.HOME["en"]["faqs"])
    write(
        "llms.txt",
        f"""# El Gendy Genova Kitchens & Windows (الجندي جينوفا للمطابخ والشبابيك)

> Kitchen and window manufacturer in Mansoura, Dakahlia, Egypt. Designs, manufactures in its own factory, and installs aluminum and wood kitchens, UPVC and aluminum windows and doors, aluminum shopfronts, tempered (securit) glass shower enclosures, and feature walls / TV units. Bilingual site: Arabic (primary) and English.

## Business details

- Name: El Gendy Genova Kitchens & Windows — الجندي جينوفا للمطابخ والشبابيك (also known as El Gendy / الجندي للمطابخ والشبابيك)
- Showroom: end of Samia El-Gamal St., El-Sallab St., Mansoura, Egypt (المنصورة — آخر شارع سامية الجمل، شارع السلاب)
- Factory: behind the Central Security camp, Mansoura (خلف الأمن المركزي)
- Phone / WhatsApp: {C.PHONE_DISPLAY}
- Email: {C.EMAIL}
- Facebook: {C.FACEBOOK}
- Service area: Mansoura and Dakahlia governorate
- Offers: free site visit and measurements, written warranty on manufacturing and installation

## Services

{svc_lines}

## Guides

- [Aluminum vs UPVC windows — complete comparison]({absolute(path('en', 'guide'))}): insulation, strength, looks, maintenance, price factors, and when to choose each. Arabic: {absolute(path('ar', 'guide'))}

## Other pages

- [Home (Arabic)]({absolute(path('ar'))})
- [Home (English)]({absolute(path('en'))})
- [Project gallery — 160+ real project photos]({absolute(path('en', 'gallery'))}) · Arabic: {absolute(path('ar', 'gallery'))}

## FAQ

{faq_lines}
""",
    )


def main():
    for lang in LANGS:
        build_home(lang)
        for svc in C.SERVICES:
            build_service(lang, svc)
        build_gallery(lang)
        build_guide(lang)
    build_extras()
    print("Built", 2 * (3 + len(C.SERVICES)), "pages")


if __name__ == "__main__":
    main()
