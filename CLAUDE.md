# Tiny Surprise Co – website repo guide

Static site on GitHub Pages: https://tinysurprise-co.github.io (pushing to `main` publishes in ~1 minute).
Brand Instagram: @tinysurprise_co. Owner: Aniket Nandkumar Gurav, Mumbai.

## What's where
- `index.html` – homepage (glass theme, self-playing showcase, designs grid). Has a `DESIGNS` list.
- `create/index.html` – editor: buyer writes content, live preview (with PREVIEW watermark), Razorpay checkout, shows final link. Has a `DESIGNS` settings object and `API_URL`.
- `birthday-cake/index.html` – the Birthday Cake template. Modes: `?id=` (paid website, loads from API), `?preview=1` (inside editor, watermark), `?autoplay=1` (silent homepage showcase), no params (demo).
- `style.css` – shared glass theme. `site.js` – shared header, phone menu, footer (edit nav/footer links only here).
- `terms.html`, `refund.html`, `privacy.html`, `contact.html` – policies.
- `robots.txt`, `sitemap.xml`, `og-image.png`, icons.

Backend (NOT in this repo): Google Apps Script web app (`API_URL`, ends in `/exec`) with a `PRICES` map in paise; Razorpay keys live in Apps Script Script Properties. Never put API keys or secrets in this repo – it is public.

## Rules
1. **Every design shares one content model:** to, from, number, photos [{src, caption}] (max 5), reasons (max 6), letter (lines), question, yesReply. New templates must read exactly these fields and support `?id=`, `?preview=1` (+ watermark), `?autoplay=1` (silent, no focus stealing) and demo mode.
2. **Adding/pricing a design touches three places that must match:** homepage `DESIGNS`, editor `DESIGNS`, and Apps Script `PRICES` (tell the owner to update Apps Script; it is not in this repo).
3. **Cache-busting:** whenever `style.css` or `site.js` changes, bump `?v=N` on their links in EVERY page (index, create, terms, refund, privacy, contact).
4. Keep the visual style consistent: Caprasimo (display) + Figtree (body), colours ink #2A1F5C, berry #E8457A, butter #FFC857, mint #8FD6BD, background #FDEFF4; glass panels; parallel sections reuse the same layout and naming.
5. Customer websites must stay out of search engines (`<meta name="robots" content="noindex">` in every template).
6. No fake reviews, counters or made-up numbers on the site. Crossed-out prices must reflect a real regular price.
7. Test on phone widths (375px) and laptop before pushing; describe changes to the owner in plain language.
