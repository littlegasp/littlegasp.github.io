import asyncio
from playwright.async_api import async_playwright
async def m():
  async with async_playwright() as p:
    b=await p.chromium.launch()
    for vp in [{"width":375,"height":760},{"width":1366,"height":768}]:
      pg=await b.new_page(viewport=vp); errs=[]; pg.on("pageerror",lambda e:errs.append(str(e)))
      await pg.goto("http://localhost:8765/"); await pg.wait_for_timeout(2500)
      n=await pg.evaluate("document.querySelectorAll('.cf').length"); cards=await pg.evaluate("[...document.querySelectorAll('#designs a,[data-key]')].filter(a=>/miss-you/.test(a.outerHTML)).length")
      print(vp['width'], "phones",n,"miss-you refs",cards, errs)
      el=await pg.query_selector("text=Miss You")
      if el: await el.scroll_into_view_if_needed(); await pg.wait_for_timeout(800); await pg.screenshot(path=f"/tmp/claude-0/mykit/home-{vp['width']}.png")
      await pg.goto("http://localhost:8765/long-distance-relationship-gift/"); await pg.wait_for_timeout(1500)
      await pg.screenshot(path=f"/tmp/claude-0/mykit/ld-{vp['width']}.png"); print("landing", errs)
      await pg.goto("http://localhost:8765/create/?d=miss-you"); await pg.wait_for_timeout(2500); print("editor", errs, await pg.title())
    # autoplay ends with the postMessage inside a frame
    pg=await b.new_page(viewport={"width":1366,"height":768})
    await pg.goto("http://localhost:8765/about.html")
    await pg.evaluate("""()=>{window.done=0;addEventListener('message',e=>{if(e.data&&e.data.type==='lg-autoplay-done')window.done=1});const f=document.createElement('iframe');f.src='/miss-you/?autoplay=1';f.style='width:375px;height:750px';document.body.prepend(f)}""")
    for t in range(90):
      await pg.wait_for_timeout(1000)
      if await pg.evaluate("window.done"): print("autoplay done at", t, "s"); break
    else: print("autoplay NOT done")
    await b.close()
asyncio.run(m())
