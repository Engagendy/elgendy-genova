# El Gendy Genova — Kitchens & Windows

Static bilingual landing page for **الجندي جينوفا للمطابخ والشبابيك** (Mansoura, Egypt).

- Arabic homepage: `index.html` · English: `en.html` (same page, in-page AR/EN switcher)
- Filterable project gallery with lightbox — photos sourced from the business Facebook page (`facebook.com/atceg`), stored in `assets/img/work/` (`*-sm.webp` thumbnails, full size without suffix)
- Materials guide, process timeline, FAQ, showroom/factory locations
- Quote form opens a pre-filled WhatsApp message to +20 100 945 5453
- SEO: LocalBusiness + FAQ structured data, hreflang, sitemap, `llms.txt`

Published with GitHub Pages from the repository root: https://engagendy.github.io/elgendy-genova/

To add photos: drop `<category>-<id>.webp` and `<category>-<id>-sm.webp` into `assets/img/work/` and add `{"id","w","h"}` to the matching category in the `WORKS` object in both HTML files.
