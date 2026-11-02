import asyncio
from playwright.async_api import async_playwright
B="http://localhost:8765/"
import sys
T=sys.argv[1].split(",") if len(sys.argv)>1 else ["birthday-cake","birthday-wish","garba-circle","karwa-chauth","diwali","apology","love-letter","anniversary","proposal","miss-you"]
async def one(b,k):
  pg=await b.new_page(viewport={"width":1366,"height":800}); errs=[]
  pg.on("pageerror",lambda e:errs.append(str(e)[:200]))
  await pg.goto(B+f"create/?d={k}"); await pg.wait_for_timeout(2500)
  await pg.fill("#f-to","Meera"); await pg.fill("#f-from","Aarav"); await pg.click("#replay"); await pg.wait_for_timeout(3500)
  pv=pg.frame_locator("#pv")
  txt=await pg.evaluate("(()=>{const f=document.querySelector('#pv');try{return f.contentDocument.body.innerText.slice(0,4000)}catch(e){return 'ERR '+e}})()")
  src=await pg.evaluate("document.querySelector('#pv').src")
  chips=await pg.evaluate("document.querySelectorAll('#forChips button').length")
  title=await pg.evaluate("document.querySelector('#title').textContent")
  price=await pg.evaluate("document.querySelector('.pricebox')?.innerText||''")
  await pg.close()
  return k,('meera' in txt.lower()),src.split('/')[3],chips,title,price.replace('\n',' '),errs
async def main():
  async with async_playwright() as p:
    b=await p.chromium.launch()
    for r in await asyncio.gather(*[one(b,k) for k in T]): print(r)
    await b.close()
asyncio.run(main())
