import asyncio, sys, json
from playwright.async_api import async_playwright
S="/tmp/claude-0/mykit/f-"
VPS=[tuple(map(int,v.split('x'))) for v in sys.argv[1:] if v!='shot'] or [(360,640),(375,667),(390,844)]
SHOT='shot' in ''.join(sys.argv)
async def drag_leg(pg):
  pts=await pg.evaluate("""()=>{const M=maps.plane,svg=M.svg,a=M.p,b=LEG_END[leg];const out=[];for(let i=0;i<=14;i++){const q=M.path.getPointAtLength(M.len*(a+(b-a)*i/14));const pt=svg.createSVGPoint();pt.x=q.x;pt.y=q.y;const s=pt.matrixTransform(svg.getScreenCTM());out.push([s.x,s.y]);}return out}""")
  await pg.mouse.move(*pts[0]); await pg.mouse.down()
  for q in pts[1:]: await pg.mouse.move(*q, steps=3)
  await pg.mouse.up(); await pg.wait_for_timeout(900)
MEAS="""(tag)=>{const m=document.querySelector('main');const over=m.scrollHeight-m.clientHeight;
 const vis=[...document.querySelectorAll('main button, .mapbox, #fog, #phone, #parcel, #grid')].filter(b=>b.offsetParent&&!b.closest('[hidden]'));
 const bad=vis.map(b=>{const r=b.getBoundingClientRect();return [b.id||b.className.toString().slice(0,18), Math.round(r.top), Math.round(r.bottom)]}).filter(x=>x[2]>innerHeight+1||x[1]<0);
 return [tag, over, JSON.stringify(bad)]}"""
async def m():
  async with async_playwright() as p:
    b=await p.chromium.launch()
    for (w,h) in VPS:
      pg=await b.new_page(viewport={"width":w,"height":h}); errs=[]; pg.on("pageerror",lambda e:errs.append(str(e)))
      await pg.goto("http://localhost:8765/miss-you/"); await pg.wait_for_timeout(1500)
      res=[]
      async def meas(tag):
        await pg.evaluate("document.querySelector('main').scrollTo(0,0)")
        r=await pg.evaluate(MEAS, tag); res.append(r)
        if SHOT: await pg.screenshot(path=S+f"{w}x{h}-{len(res):02d}.png")
      await meas("open")
      await pg.click("#openBtn"); await pg.wait_for_timeout(600); await meas("plane0")
      await drag_leg(pg); await meas("plane0-landed")
      await pg.click("#afterPlane"); await pg.wait_for_timeout(500); await meas("window")
      fog=await pg.query_selector("#fog")
      for ph in range(3):
        fb=await fog.bounding_box()
        await pg.mouse.move(fb['x']+10,fb['y']+20); await pg.mouse.down()
        for i in range(12):
          y=fb['y']+20+i*fb['height']/12
          await pg.mouse.move(fb['x']+fb['width']-10, y, steps=5); await pg.mouse.move(fb['x']+10, y+fb['height']/24, steps=5)
        await pg.mouse.up(); await pg.wait_for_timeout(1300)
        await meas(f"window-photo{ph}")
        if ph<2: await pg.click("#nextPhoto"); await pg.wait_for_timeout(300)
      await pg.click("#afterWindow"); await pg.wait_for_timeout(600)
      await drag_leg(pg); await meas("plane1-landed")
      await pg.click("#afterPlane"); await pg.wait_for_timeout(500); await meas("call-ring")
      await pg.click("#phone"); await pg.wait_for_timeout(11000); await meas("call-done")
      await pg.click("#afterCall"); await pg.wait_for_timeout(500)
      await drag_leg(pg)
      await pg.click("#afterPlane"); await pg.wait_for_timeout(500); await meas("parcel")
      await pg.click("#parcel"); await pg.wait_for_timeout(1800); await meas("parcel-writing")
      await pg.wait_for_timeout(6000); await meas("parcel-done")
      await pg.click("#afterParcel"); await pg.wait_for_timeout(500)
      await drag_leg(pg); await meas("plane3-landed")
      await pg.click("#afterPlane"); await pg.wait_for_timeout(2500); await meas("ask"); await pg.click("#pickBtn"); await pg.wait_for_timeout(300); await meas("ask-cal")
      await pg.click("#nextM"); await pg.wait_for_timeout(200); btn=(await pg.query_selector_all("#grid button:not([disabled])"))[5]; await btn.click(); await pg.wait_for_timeout(500); await meas("ask-picked")
      await pg.click("#lockDate"); await pg.wait_for_timeout(1200); await meas("ask-locked")
      await pg.click("#afterAsk"); await pg.wait_for_timeout(2200); await meas("end")
      print(w,h,errs)
      for r in res: print("  ",r)
    await b.close()
asyncio.run(m())
