# Little Gasp – website repo guide

Static site on GitHub Pages, custom domain https://littlegasp.com (CNAME file; DNS at GoDaddy: 4 A records 185.199.108-111.153 + CNAME www -> littlegasp.github.io). Pushing to `main` publishes in ~1 minute.
Brand Instagram: @littlegasp.co. Owner: Aniket Nandkumar Gurav, Mumbai.

## What's where
- `index.html` – homepage (glass theme, self-playing showcase, designs grid). Has a `DESIGNS` list.
- `create/index.html` – editor: buyer writes content, live preview (with PREVIEW watermark), Razorpay checkout, shows final link. Has a `DESIGNS` settings object and `API_URL`.
- `birthday-cake/index.html` – the Birthday Cake template. Modes: `?id=` (paid website, loads from API), `?preview=1` (inside editor, watermark), `?autoplay=1` (silent homepage showcase), no params (demo).
- `garba-circle/index.html` – Navratri Garba Circle (art = painted pieces cut from Canva asset kit DAHXTApHpwU into `garba-circle/img/*.webp`): one live top-down garba scene; tap the dhol on the beat to light 9 night-colour slots (photos + reasons spread across them, empty nights show the night's colour and Devi). Editor limits it to 4 photos + 5 reasons via `maxPhotos`/`maxReasons`.
- `karwa-chauth/index.html` – Karwa Chauth Moon template.
- `style.css` – shared glass theme. `site.js` – shared header, phone menu, footer (edit nav/footer links only here).
- `terms.html`, `refund.html`, `privacy.html`, `contact.html` – policies.
- `robots.txt`, `sitemap.xml`, `og-image.png`, icons.

Backend (NOT in this repo): Google Apps Script web app — TEMPORARILY deployed in tinysurpriseco.orders@gmail.com since 7 Oct 2026 (littlegasp.orders account disabled, appeal pending; move it back and update API_URL in all 4 files once restored) — (`API_URL`, ends in `/exec`) with a `PRICES` map in paise; Razorpay keys live in Apps Script Script Properties. Never put API keys or secrets in this repo – it is public.

## Rules
1. **Every design shares one content model:** to, from, number, photos [{src, caption}] (max 5), reasons (max 6), letter (lines), question, yesReply. New templates must read exactly these fields and support `?id=`, `?preview=1` (+ watermark), `?autoplay=1` (silent, no focus stealing) and demo mode.
2. **Adding/pricing a design touches three places that must match:** homepage `DESIGNS`, editor `DESIGNS`, and Apps Script `PRICES` (tell the owner to update Apps Script; it is not in this repo).
3. **Cache-busting:** whenever `style.css` or `site.js` changes, bump `?v=N` on their links in EVERY page (index, create, terms, refund, privacy, contact).
4. Keep the visual style consistent: Caprasimo (display) + Figtree (body), colours ink #2A1F5C, berry #E8457A, butter #FFC857, mint #8FD6BD, background #FDEFF4; glass panels; parallel sections reuse the same layout and naming.
5. Customer websites must stay out of search engines (`<meta name="robots" content="noindex">` in every template).
6. No fake reviews, counters or made-up numbers on the site. Crossed-out prices must reflect a real regular price.
7. Test on phone widths (375px) and laptop before pushing; describe changes to the owner in plain language.
8. **Every template also has:** a phone-shaped stage on laptops (centred 9:16 column, blurred sides); demo photos in `<template>/img/demo-N.svg` (used only in demo/autoplay); a WhatsApp/social preview (`og:` tags + `<template>/img/share.jpg`, 1200x630, no names); the full favicon set; "next" buttons that name the scene they open (built from the scene order, so skipped scenes never leave a wrong label); a finale that reads right for ANY question (no "It's a date").
9. **Prices/offers:** `regularPrice` (crossed-out) stays 0 until the design has really sold at that price. Offer badges carry `offerEnds` (YYYY-MM-DD) and hide themselves after that date in both homepage and editor; the price itself still has to be changed in all three places.
10. **Homepage cards** use `image` (1200x900 webp in `/img/cards/`): the real design on a phone over its own colours. Live designs also set `screen` (375x750 webp still of their first screen, `/img/cards/<key>-screen.webp`) for the hero's side phones, so two designs never look the same there. Each design in the editor `DESIGNS` sets `numberLabel`/`numberHint`, `questionHint`, `yesHint` so no other design's examples leak in.
12. **Homepage showcase:** a template's `?autoplay=1` run must end with `parent.postMessage({type:"tsc-autoplay-done"}, location.origin)` (reload only when not in a frame). The homepage then plays the next live design; the "Live now" pill and side phones follow whatever is playing.
14. Decorative props near text (Karwa Chauth thali + lantern) are hidden by measuring overlap (`fitProps()`), not by fixed screen heights; related props always hide together.
13. Every template's last screen ends with the "Made with love on Little Gasp" link.
11. In page CSS, any class that sets `display` on an element that uses the `hidden` attribute needs its own `[hidden]{display:none}` rule.

15. **Every new template must play differently** (its own interaction and structure), not the same slides with new art. Design it in Canva first and get the owner's approval before building.
17. **Songs:** a design's default song must be one we have the rights to (e.g. Pixabay licence; record it in the template's `SONG.credit`), never film/label songs. Editor `DESIGNS` with `song: "<sentence>"` let the buyer upload their own MP3/M4A (≤ 8 MB, rights checkbox required); the editor measures its bpm/offset so tap games follow it, the backend (v4, `Song` column) stores it in Drive and returns `song` from `doGet`; templates fall back to their default song if it won't load.
16. Editor `DESIGNS` may set `maxPhotos` / `maxReasons` when a design needs fewer than 5 / 6; templates must still work with any smaller number.
