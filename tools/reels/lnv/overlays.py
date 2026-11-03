"""Late Night Vinyl reel ("tracklist" format): renders the transparent overlays (hook lines, chapter labels, outro)
with Playwright so emoji and fonts render properly. Output: /tmp/claude-0/newreels/vinyl/ov/*.png"""
import asyncio
from playwright.async_api import async_playwright
F="file:///tmp/claude-0/fonts/node_modules/@fontsource/"
D="/tmp/claude-0/newreels/vinyl/"
FONTS=f"""@font-face{{font-family:Figtree;font-weight:800;src:url({F}figtree/files/figtree-latin-800-normal.woff2)}}
@font-face{{font-family:Figtree;font-weight:700;src:url({F}figtree/files/figtree-latin-700-normal.woff2)}}
@font-face{{font-family:Cor;font-weight:600;font-style:italic;src:url({F}cormorant-garamond/files/cormorant-garamond-latin-600-italic.woff2)}}
@font-face{{font-family:Cor;font-weight:600;src:url({F}cormorant-garamond/files/cormorant-garamond-latin-600-normal.woff2)}}"""
CSS=f"""<style>{FONTS}*{{margin:0;box-sizing:border-box}}html,body{{background:transparent}}
body{{width:1080px;height:1920px;overflow:hidden;position:relative;color:#F2E6D0}}
.hook{{position:absolute;left:70px;right:70px;top:520px;text-align:center;font:800 88px/1.15 Figtree,'Noto Color Emoji';text-shadow:0 4px 28px rgba(0,0,0,.85),0 0 6px rgba(0,0,0,.6)}}
.hook b{{color:#E9B872}}
.lab{{position:absolute;left:80px;right:80px;top:190px;height:250px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}}
.k{{font:700 34px Figtree;letter-spacing:.32em;color:#E9B872;display:flex;align-items:center;gap:22px}}
.k:before,.k:after{{content:"";width:70px;height:2px;background:rgba(233,184,114,.6)}}
.t{{font:600 italic 78px/1.08 Cor,'Noto Color Emoji';margin-top:16px;text-shadow:0 4px 20px rgba(0,0,0,.6)}}
.out{{position:absolute;inset:0;background:radial-gradient(90% 60% at 50% 45%,#173438,#0B1A1C 75%);display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:0 90px}}
.out img{{width:170px;height:170px;border-radius:44px;margin-bottom:64px;box-shadow:0 10px 30px rgba(0,0,0,.5)}}
.out .a{{font:600 italic 96px/1.08 Cor,'Noto Color Emoji'}}
.out .b{{font:700 50px/1.35 Figtree;margin-top:40px;color:rgba(242,230,208,.85)}}
.out .u{{font:800 84px/1 Figtree;color:#E9B872;margin-top:80px}}
.out .s{{font:700 40px/1.3 Figtree;margin-top:26px;color:rgba(242,230,208,.7)}}
</style>"""
HOOK=['Koi <b>occasion</b><br>nahi tha…','Bas usse batana tha<br>ki woh <b>meri favourite<br>song</b> hai 🎵','Toh maine usse<br>ek <b>record</b> bheja 👇']
LABS=[("INTRO","A note on the shelf: “Play me”"),("TRACK 01","Our photo is the album cover"),
      ("TRACK 02","Drop the needle"),("SIDE A","Every reason is one track"),
      ("SIDE B","Flip it for our photos"),("LINER NOTES","My letter, inside the sleeve"),
      ("HIDDEN TRACK","The question, at the very end"),("OUTRO","…and then, our slow dance")]
async def m():
  async with async_playwright() as p:
    b=await p.chromium.launch(); pg=await b.new_page(viewport={"width":1080,"height":1920})
    async def shot(html,name):
      open(D+"t.html","w").write(CSS+html); await pg.goto("file://"+D+"t.html"); await pg.wait_for_timeout(300)
      await pg.screenshot(path=D+"ov/"+name,omit_background=True)
    for i,h in enumerate(HOOK): await shot(f'<div class="hook">{h}</div>',f"hk{i}.png")
    for i,(k,t) in enumerate(LABS): await shot(f'<div class="lab"><div class="k">{k}</div><div class="t">{t}</div></div>',f"lab{i}.png")
    await shot(f'<div class="out"><img src="file://{D}../prr/logo.png"><div class="a">Kisi bhi raat ke liye 🌙</div><div class="b">Your photos, your reasons,<br>your letter. On a record.</div><div class="u">littlegasp.com</div><div class="s">Try it free · @littlegasp.co</div></div>',"outro.png")
    await b.close()
asyncio.run(m()); print("ok")
