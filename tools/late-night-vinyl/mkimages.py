"""Homepage card (1200x900), coverflow screen still (375x750) and Pinterest pin (1000x1500) for Late Night Vinyl.
Needs the repo served on :8765 and @fontsource fonts in /tmp/claude-0/fonts (npm i @fontsource/cormorant-garamond @fontsource/figtree @fontsource/caveat @fontsource/caprasimo)."""
import asyncio
from playwright.async_api import async_playwright
from PIL import Image
FD="/tmp/claude-0/fonts/node_modules/@fontsource/"; F="file://"+FD
R="/home/claude/littlegasp.github.io/"; K="/tmp/claude-0/vk/"
def ff(fam, pkg, w, st="normal"): return f"@font-face{{font-family:'{fam}';font-weight:{w};font-style:{st};src:url(/__f/{pkg}/files/{pkg}-latin-{w}-{st}.woff2)}}"
GCSS="\n".join([ff("Cormorant Garamond","cormorant-garamond",w,s) for w in (500,600) for s in ("normal","italic")]+
  [ff("Figtree","figtree",w) for w in (400,600,700)]+[ff("Caveat","caveat",w) for w in (500,700)]+[ff("Caprasimo","caprasimo",400)])
async def m():
  async with async_playwright() as p:
    b=await p.chromium.launch()
    pg=await b.new_page(viewport={"width":375,"height":750},device_scale_factor=2)
    async def fonts(route): await route.fulfill(body=GCSS,content_type="text/css")
    await pg.route("**/fonts.googleapis.com/**",fonts)
    async def fl(route): await route.fulfill(path=FD+route.request.url.split("/__f/")[1])
    await pg.route("**/__f/**",fl)
    await pg.goto("http://localhost:8765/late-night-vinyl/"); await pg.wait_for_timeout(2500)
    await pg.screenshot(path=K+"screen-open.png")
    # the record playing, for the card
    await pg.evaluate("go('play')"); await pg.wait_for_timeout(500)
    await pg.evaluate("(async()=>{await dropNeedle();})()"); await pg.wait_for_timeout(2600)
    await pg.screenshot(path=K+"screen-play.png")
    card=f"""<html><head><style>*{{margin:0}}body{{width:1200px;height:900px;overflow:hidden;position:relative;background:#0E2326}}
    .bg{{position:absolute;inset:-40px;background:url(file://{R}late-night-vinyl/img/bg-wide.webp) center/cover;filter:blur(8px) brightness(.8)}}
    .ph{{position:absolute;left:350px;top:78px;width:520px;height:1040px;border-radius:64px;border:14px solid #1b1320;overflow:hidden;transform:rotate(-4deg);box-shadow:0 30px 60px rgba(0,0,0,.55);background:url({K}screen-play.png) top/100% auto}}</style></head>
    <body><div class=bg></div><div class=ph></div></body></html>"""
    open(K+"card.html","w").write(card)
    pc=await b.new_page(viewport={"width":1200,"height":900}); await pc.goto("file://"+K+"card.html"); await pc.wait_for_timeout(600); await pc.screenshot(path=K+"card.png")
    Image.open(K+"card.png").convert("RGB").save(R+"img/cards/late-night-vinyl.webp",quality=82,method=6)
    Image.open(K+"screen-open.png").convert("RGB").resize((375,750),Image.LANCZOS).save(R+"img/cards/late-night-vinyl-screen.webp",quality=80,method=6)
    pin=f"""<html><head><style>@font-face{{font-family:Caprasimo;src:url({F}caprasimo/files/caprasimo-latin-400-normal.woff2)}}
@font-face{{font-family:Figtree;font-weight:700;src:url({F}figtree/files/figtree-latin-700-normal.woff2)}}
@font-face{{font-family:Figtree;font-weight:500;src:url({F}figtree/files/figtree-latin-500-normal.woff2)}}*{{margin:0;box-sizing:border-box}}
      body{{width:1000px;height:1500px;overflow:hidden;position:relative;background:#2A1F5C;font-family:Figtree}}
      .bg{{position:absolute;inset:-60px;background:url(file://{R}img/cards/late-night-vinyl.webp) center/cover;filter:blur(26px) saturate(1.1) brightness(.85)}}
      .top{{position:absolute;left:60px;right:60px;top:56px;padding:40px 44px 36px;border-radius:40px;background:rgba(253,239,244,.94);text-align:center;box-shadow:0 18px 40px rgba(0,0,0,.25)}}
      .k{{font:700 22px Figtree;letter-spacing:.2em;color:#E8457A}}
      h1{{font:400 74px/1.02 Caprasimo;color:#2A1F5C;margin:14px 0 14px}}
      .s{{font:500 32px/1.3 Figtree;color:#4a3f78}}
      .ph{{position:absolute;left:50%;top:470px;width:470px;height:940px;margin-left:-235px;border-radius:62px;border:14px solid #1d1540;overflow:hidden;background:url(file://{R}img/cards/late-night-vinyl-screen.webp) top/100% auto;box-shadow:0 34px 70px rgba(0,0,0,.5);transform:rotate(-3deg)}}
      .bot{{position:absolute;left:0;right:0;bottom:0;height:150px;background:#2A1F5C;color:#fff;display:flex;align-items:center;justify-content:center;gap:22px;font:700 40px Figtree}}
      .bot b{{background:#FFC857;color:#2A1F5C;border-radius:999px;padding:14px 30px;font:700 34px Figtree}}
      </style></head><body><div class=bg></div><div class=ph></div>
      <div class=top><div class=k>A SURPRISE FOR YOUR PERSON</div><h1>A record made just for them</h1><div class=s>Drop the needle: your reasons are the tracks, your photos the B-side, your letter the liner notes</div></div>
      <div class=bot><b>Try it free</b> littlegasp.com</div></body></html>"""
    open(K+"pin.html","w").write(pin)
    pp=await b.new_page(viewport={"width":1000,"height":1500}); await pp.goto("file://"+K+"pin.html"); await pp.wait_for_timeout(600)
    await pp.screenshot(path=R+"img/pins/late-night-vinyl.jpg",type="jpeg",quality=86)
    await b.close()
asyncio.run(m()); print("ok")
