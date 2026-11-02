import asyncio
from playwright.async_api import async_playwright
F="file:///tmp/claude-0/fonts/node_modules/@fontsource/"
FONTS=f"""@font-face{{font-family:Figtree;font-weight:800;src:url({F}figtree/files/figtree-latin-800-normal.woff2)}}
@font-face{{font-family:Figtree;font-weight:700;src:url({F}figtree/files/figtree-latin-700-normal.woff2)}}"""
D="/tmp/claude-0/newreels/anr/"
CSS=f"""<style>{FONTS}*{{margin:0;box-sizing:border-box}}body{{width:1080px;height:1920px;overflow:hidden;position:relative;font-family:Figtree,'Noto Color Emoji'}}
.bg{{position:absolute;inset:0;background:radial-gradient(120% 60% at 50% 0%,#5A2450,#24102C 70%)}}
.blur{{position:absolute;inset:-60px;background:url({D}hookbg.png) center/cover;filter:blur(18px) brightness(.45)}}
.logo{{position:absolute;right:48px;top:150px;width:120px;height:120px;border-radius:26px;box-shadow:0 6px 18px rgba(0,0,0,.3)}}
.hook{{position:absolute;left:60px;right:60px;top:700px;text-align:center;font:800 104px/1.12 Figtree,'Noto Color Emoji';color:#fff;text-shadow:0 6px 30px rgba(0,0,0,.5)}}
.cap{{position:absolute;left:60px;right:60px;top:170px;height:330px;display:flex;align-items:center;justify-content:center;text-align:center;font:800 70px/1.15 Figtree,'Noto Color Emoji';color:#fff;padding-right:120px}}
b{{color:#FFC857}}
</style>"""
HOOK=["Woh poora din<br><b>bhookhi-pyaasi</b> rahi 🥺","Sirf <b>mere liye</b> 🌙","Toh maine usse<br><b>yeh bheja</b> 👇"]
CAPS=['Helmets on 🪖', 'Kick-start the<br><b>scooter</b> 🛵', 'A map of <b>our years</b> 🗺️', 'Fill the tank with<br><b>reasons</b> ⛽', 'Ride past <b>every photo</b><br>of us 📸', 'Promises at the<br><b>toll gate</b> 💛', 'Chai stop… and<br><b>my letter</b> ☕', 'A <b>love lock</b><br>on the bridge 🔒', 'And off we ride…<br><b>together</b> 🛵💛']
async def m():
  async with async_playwright() as p:
    b=await p.chromium.launch(); pg=await b.new_page(viewport={"width":1080,"height":1920})
    async def shot(html,name,transparent=False):
      open(D+"t.html","w").write(CSS+html); await pg.goto("file://"+D+"t.html"); await pg.wait_for_timeout(250); await pg.screenshot(path=D+"png/"+name)
    pass #: await shot(f'<div class="blur"></div><img class="logo" src="{D}logo.png"><div class="hook">{h}</div>',f"h{i}.png")
    for i,c in enumerate(CAPS): await shot(f'<div class="bg"></div><img class="logo" src="{D}logo.png"><div class="cap"><span>{c}</span></div>',f"c{i}.png")
    await b.close()
asyncio.run(m())
