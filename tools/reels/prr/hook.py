import asyncio
from playwright.async_api import async_playwright
F="file:///tmp/claude-0/fonts/node_modules/@fontsource/"
D="/tmp/claude-0/newreels/prr/"
CSS=f"""<style>@font-face{{font-family:Figtree;font-weight:800;src:url({F}figtree/files/figtree-latin-800-normal.woff2)}}
*{{margin:0;box-sizing:border-box}}html,body{{background:transparent}}body{{width:1080px;height:1920px;overflow:hidden;position:relative}}
.logo{{position:absolute;right:48px;top:150px;width:120px;height:120px;border-radius:26px;box-shadow:0 6px 18px rgba(0,0,0,.3)}}
.hook{{position:absolute;left:60px;right:60px;top:360px;text-align:center;font:800 90px/1.14 Figtree,'Noto Color Emoji';color:#fff;text-shadow:0 4px 24px rgba(0,0,0,.75),0 0 4px rgba(0,0,0,.5)}}
b{{color:#FFC857}}</style>"""
HOOK=['Usse <b>propose</b><br>karna tha 💍', 'Par seedha nahi…<br><b>treasure hunt</b> se 🔦', 'Toh maine usse<br><b>yeh link</b> bheja 👇']
async def m():
  async with async_playwright() as p:
    b=await p.chromium.launch(); pg=await b.new_page(viewport={"width":1080,"height":1920})
    for i,h in enumerate(HOOK):
      open(D+"t.html","w").write(CSS+f'<img class="logo" src="{D}logo.png"><div class="hook">{h}</div>')
      await pg.goto("file://"+D+"t.html"); await pg.wait_for_timeout(250); await pg.screenshot(path=D+f"png/hk{i}.png",omit_background=True)
    await b.close()
asyncio.run(m())
