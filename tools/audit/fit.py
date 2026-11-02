import asyncio
from playwright.async_api import async_playwright
B="http://localhost:8765/"
T=["birthday-cake","birthday-wish","garba-circle","karwa-chauth","diwali","apology","love-letter","anniversary","proposal","miss-you"]
async def one(b,k,w,h):
  pg=await b.new_page(viewport={"width":w,"height":h}); await pg.goto(B+k+"/"); await pg.wait_for_timeout(2500)
  r=await pg.evaluate("""()=>{const sc=[...document.querySelectorAll('[data-scene]')].find(s=>!s.hidden);const btns=[...(sc||document).querySelectorAll('button,.btn')].filter(b=>b.offsetParent&&!b.hidden);
   const vis=btns.map(b=>Math.round(b.getBoundingClientRect().bottom));return [sc?sc.dataset.scene:'?',Math.max(0,...vis),innerHeight]}""")
  await pg.close(); return k,w,h,r
async def main():
  async with async_playwright() as p:
    b=await p.chromium.launch()
    for r in await asyncio.gather(*[one(b,k,w,h) for k in T for (w,h) in ((360,640),(375,667))]):
      k,w,h,(sc,bot,ih)=r; print(f"{k:14} {w}x{h} first screen '{sc}': lowest button bottom {bot}px of {ih}px {'OK' if bot<=ih else 'NEEDS SCROLL'}")
    await b.close()
asyncio.run(main())
