import asyncio
from playwright.async_api import async_playwright
F="file:///tmp/claude-0/fonts/node_modules/@fontsource/"
A="file:///home/claude/littlegasp.github.io/miss-you/img/"
R="/home/claude/littlegasp.github.io/"
K="/tmp/claude-0/mykit/"
FONTS=f"""@font-face{{font-family:Caprasimo;src:url({F}caprasimo/files/caprasimo-latin-400-normal.woff2)}}
@font-face{{font-family:Figtree;font-weight:600;src:url({F}figtree/files/figtree-latin-600-normal.woff2)}}
@font-face{{font-family:Figtree;font-weight:700;src:url({F}figtree/files/figtree-latin-700-normal.woff2)}}
@font-face{{font-family:Caveat;font-weight:700;src:url({F}caveat/files/caveat-latin-700-normal.woff2)}}"""
CSS=open("/tmp/claude-0/ll/t.py").read().split('CSS=f"""')[1].split('"""')[0].replace("{{","{").replace("}}","}")
async def m():
  async with async_playwright() as p:
    b=await p.chromium.launch()
    pg=await b.new_page(viewport={"width":375,"height":750},device_scale_factor=2)
    async def fonts(route): await route.fulfill(body=CSS,content_type="text/css")
    await pg.route("**/fonts.g*/**",fonts)
    async def ff(route): await route.fulfill(path="/tmp/claude-0/fonts/node_modules/@fontsource/"+route.request.url.split("/__f/")[1])
    await pg.route("**/__f/**",ff)
    await pg.goto("http://localhost:8765/miss-you/"); await pg.wait_for_timeout(2600)
    await pg.screenshot(path=K+"screen-open.png")
    await pg.click("#openBtn"); await pg.wait_for_timeout(500)
    await pg.evaluate("setPlane(maps.plane,.17); document.querySelector('[data-map=plane]').classList.add('moving')"); await pg.wait_for_timeout(300)
    await pg.screenshot(path=K+"screen-plane.png")
    card=f"""<html><head><style>{FONTS}*{{margin:0}}body{{width:1200px;height:900px;overflow:hidden;position:relative;background:#1E1A3A}}
    .bg{{position:absolute;inset:-40px;background:url({A}bg-wide.webp) center/cover;filter:blur(10px) brightness(.85)}}
    .ph{{position:absolute;left:350px;top:78px;width:520px;height:1040px;border-radius:64px;border:14px solid #2A1F5C;overflow:hidden;transform:rotate(-4deg);box-shadow:0 30px 60px rgba(0,0,0,.45);background:url({K}screen-plane.png) top/100% auto}}</style></head>
    <body><div class=bg></div><div class=ph></div></body></html>"""
    open(K+"card.html","w").write(card)
    pc=await b.new_page(viewport={"width":1200,"height":900}); await pc.goto("file://"+K+"card.html"); await pc.wait_for_timeout(600); await pc.screenshot(path=K+"card.png")
    await b.close()
asyncio.run(m())
from PIL import Image
Image.open(K+"card.png").convert("RGB").save(R+"img/cards/miss-you.webp",quality=82,method=6)
Image.open(K+"screen-open.png").convert("RGB").resize((375,750),Image.LANCZOS).save(R+"img/cards/miss-you-screen.webp",quality=80,method=6)
print("ok")
