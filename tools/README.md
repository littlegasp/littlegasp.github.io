# tools/ – helper scripts (not part of the website)

Everything here was written by Claude while building Little Gasp. None of it is served to buyers.
Most scripts were first run from `/tmp/claude-0/...`; paths inside them may still point there,
so change the paths (or copy the folder back to that place) before running.

Common setup: serve the repo on port 8765 (`python3 -m http.server 8765` from the repo root),
Python 3 with `playwright` (Chromium), `Pillow`, and `ffmpeg` for the reels.

## Generators (part of the site workflow)
- `seo_pages.py` – builds every search landing page (`*-surprise-website/`, `digital-love-letter/` …). Edit its data and rerun; keep `CSSV` and prices in step with the homepage. It also builds the guides (`GUIDES`: `surprise-website-vs-e-card/`, `long-distance-surprise-ideas/`, `how-to-write-an-apology/`) and `llms.txt` (from `DESIGN`, `PAGES`, `GUIDES`), so a new live design shows up there after a rerun.
- `prepare-art.py` – trims/converts Canva exports into the webp art the templates use.

## audit/ – checks to run before pushing
- `scenes.py [design,…]` – every scene of each design on 4 phone sizes; reports any scroll or button below the screen (the phone rule). `SHOT=1` saves screenshots to `shots/`, `INIT=1` checks the starting state.
- `auto.py [design]` – plays the homepage showcase (`?autoplay=1`) on phone + laptop and checks it ends with `lg-autoplay-done`.
- `ed.py [design]` – opens the editor for each design and checks the live preview shows the typed name.
- `run.py` – loads every page at phone and laptop size and lists JS errors, broken images and sideways overflow.
- `static.py` – links, assets and SEO tags (title/description length, canonical, sitemap) across the repo.
- `fit.py`, `one.py` – first-screen fit check, and a one-scene screenshot helper.

## miss-you/ – how the Miss You design was built
- `build.py` (+ `parts.py`) writes `miss-you/index.html` from its parts. Edit there, rebuild, then check with `t4.py` (plays the whole journey at 4 phone sizes and measures overflow per state).
- `mkcard.py`, `mkpin.py`, `card.html`, `pin-miss-you.html` – the homepage card, screen still and Pinterest pin images. Same method works for new designs.

## late-night-vinyl/
- `prep.py` turns the Canva kit export into the template's webp art; `mkimages.py` makes the homepage card, screen still and Pinterest pin.

## reels/ – Instagram reels (delivered WITHOUT music; the owner adds songs in Instagram)
- `rec-<design>.py` + `flow-auto-log.py` – record a design playing in Chromium, frame by frame, and log scene times.
- Each folder is one reel: `t.html` (or `chat.html`, `ride.html`, `l.html`) is an HTML timeline with a `render(t)` function; `render.py`/`mk.py` screenshots it frame by frame and joins the frames with ffmpeg; `hook.py` makes the opening hook.
  `anr` Memory Lane ride, `llr` Sealed with Love split, `myr`/`mc` Miss You chat, `op` Diwali opinion, `ed` editor time-lapse, `bd` Bhai Dooj countdown, `prr` Ring Hunt, `ml`, `sw` earlier tests.
- Owner's rule: every reel needs a different storyboard, format and hook; no prices (except the ₹200 carousel); never say "AI-made".
