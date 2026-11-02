import asyncio, json
from playwright.async_api import async_playwright
F="file:///tmp/claude-0/fonts/node_modules/@fontsource/"
R="file:///home/claude/littlegasp.github.io/img/cards/"
FONTS=f"""@font-face{{font-family:Caprasimo;src:url({F}caprasimo/files/caprasimo-latin-400-normal.woff2)}}
@font-face{{font-family:Figtree;font-weight:700;src:url({F}figtree/files/figtree-latin-700-normal.woff2)}}
@font-face{{font-family:Figtree;font-weight:500;src:url({F}figtree/files/figtree-latin-500-normal.woff2)}}"""
P=json.load(open("/tmp/claude-0/mykit/pins-miss.json"))
async def m():
  async with async_playwright() as p:
    b=await p.chromium.launch()
    pg=await b.new_page(viewport={"width":1000,"height":1500})
    for k,v in P.items():
      html=f"""<html><head><style>{FONTS}*{{margin:0;box-sizing:border-box}}
      body{{width:1000px;height:1500px;overflow:hidden;position:relative;background:#2A1F5C;font-family:Figtree}}
      .bg{{position:absolute;inset:-60px;background:url({R}{k}.webp) center/cover;filter:blur(26px) saturate(1.15) brightness(.9)}}
      .top{{position:absolute;left:60px;right:60px;top:56px;padding:40px 44px 36px;border-radius:40px;background:rgba(253,239,244,.94);text-align:center;box-shadow:0 18px 40px rgba(0,0,0,.25)}}
      .k{{font:700 22px Figtree;letter-spacing:.2em;color:#E8457A}}
      h1{{font:400 74px/1.02 Caprasimo;color:#2A1F5C;margin:14px 0 14px}}
      .s{{font:500 32px/1.3 Figtree;color:#4a3f78}}
      .ph{{position:absolute;left:50%;top:{v.get('top',470)}px;width:470px;height:940px;margin-left:-235px;border-radius:62px;border:14px solid #1d1540;overflow:hidden;background:url({R}{k}-screen.webp) top/100% auto;box-shadow:0 34px 70px rgba(0,0,0,.5);transform:rotate(-3deg)}}
      .bot{{position:absolute;left:0;right:0;bottom:0;height:150px;background:#2A1F5C;color:#fff;display:flex;align-items:center;justify-content:center;gap:22px;font:700 40px Figtree}}
      .bot b{{background:#FFC857;color:#2A1F5C;border-radius:999px;padding:14px 30px;font:700 34px Figtree}}
      </style></head><body><div class=bg></div><div class=ph></div>
      <div class=top><div class=k>{v['kicker']}</div><h1>{v['h']}</h1><div class=s>{v['s']}</div></div>
      <div class=bot><b>Try it free</b> littlegasp.com</div></body></html>"""
      open(f"/tmp/claude-0/mykit/pin-{k}.html","w").write(html)
      await pg.goto(f"file:///tmp/claude-0/mykit/pin-{k}.html"); await pg.wait_for_timeout(500)
      await pg.screenshot(path=f"/home/claude/littlegasp.github.io/img/pins/{k}.jpg",type="jpeg",quality=86)
    await b.close()
asyncio.run(m())
