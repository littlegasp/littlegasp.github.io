import asyncio, json
from playwright.async_api import async_playwright
B="http://localhost:8765/"
import sys
T=sys.argv[1].split(",") if len(sys.argv)>1 else ["birthday-cake","birthday-wish","garba-circle","karwa-chauth","diwali","apology","love-letter","anniversary","proposal","miss-you"]
async def one(b,k,vp):
  pg=await b.new_page(viewport=vp); errs=[]
  pg.on("pageerror",lambda e:errs.append(str(e)[:200]))
  await pg.goto(B+"about.html")
  await pg.evaluate("""k=>{window.done=0;addEventListener('message',e=>{if(e.data&&e.data.type==='lg-autoplay-done')window.done=1});const f=document.createElement('iframe');f.src='/'+k+'/?autoplay=1';f.style='position:fixed;inset:0;width:100%;height:100%;border:0;z-index:99';document.body.append(f)}""",k)
  f=None
  for t in range(200):
    await pg.wait_for_timeout(1000)
    if await pg.evaluate("window.done"): break
  ok=await pg.evaluate("window.done"); fr=pg.frames[1] if len(pg.frames)>1 else None
  ferr=[]
  await pg.close()
  return k,vp["width"],bool(ok),t,errs
async def main():
  async with async_playwright() as p:
    b=await p.chromium.launch()
    res=await asyncio.gather(*[one(b,k,vp) for k in T for vp in ({"width":375,"height":667},{"width":1366,"height":768})])
    for r in res: print(r)
    await b.close()
asyncio.run(main())
