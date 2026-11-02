import asyncio,sys
from playwright.async_api import async_playwright
t,scene,w,h,wait=sys.argv[1],sys.argv[2],int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5])
q=sys.argv[6] if len(sys.argv)>6 else ""
async def m():
  async with async_playwright() as p:
    b=await p.chromium.launch(); pg=await b.new_page(viewport={"width":w,"height":h},has_touch=True,is_mobile=True)
    await pg.goto(f"http://localhost:8765/{t}/{q}"); await pg.wait_for_timeout(1200)
    await pg.evaluate(f"go('{scene}')"); await pg.wait_for_timeout(wait)
    await pg.screenshot(path=f"/tmp/claude-0/audit/one-{t}-{scene}-{w}.png"); await b.close()
asyncio.run(m())
