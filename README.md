# El Gendy Genova — Kitchens & Windows

Static bilingual website for **الجندي جينوفا للمطابخ والشبابيك** (Mansoura, Egypt), published with GitHub Pages:
https://engagendy.github.io/elgendy-genova/

## Pages

| Arabic (primary) | English |
| --- | --- |
| `/` | `/en/` |
| `/services/<slug>/` × 6 | `/en/services/<slug>/` × 6 |
| `/guide/aluminum-vs-upvc/` | `/en/guide/aluminum-vs-upvc/` |
| `/gallery/` | `/en/gallery/` |

Service slugs: `aluminum-kitchens`, `wood-kitchens`, `upvc-windows-doors`, `aluminum-windows-facades`, `glass-showers`, `wall-decor-tv-units`.

Each language is fully rendered in the HTML (no client-side translation), with its own title, description, canonical, `hreflang` alternates, Open Graph tags and JSON-LD (LocalBusiness, Service, BreadcrumbList, FAQPage, Article, ImageGallery). `sitemap.xml`, `robots.txt` and `llms.txt` are generated too.

## Editing

All copy lives in `build/content.py`; photo categories in `build/photos.json`. After editing, regenerate the pages:

```sh
python3 build/build.py   # requires Pillow (reads photo sizes)
```

- Styles: `assets/css/site.css` (light theme default, `html[data-theme="dark"]` optional)
- Behaviour: `assets/js/site.js` (theme toggle, menu, tabs, gallery filter + lightbox, WhatsApp quote form)
- Photos: `assets/img/p/<id>.webp` (full) and `<id>-sm.webp` (thumbnail), sourced from the business Facebook page

To add a photo: add both WebP sizes to `assets/img/p/`, put its id in the right category in `build/photos.json`, and rebuild.

To move to a custom domain: set `SITE` and `BASE = "/"` in `build/content.py`, add a `CNAME` file, and rebuild.
