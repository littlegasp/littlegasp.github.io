import asyncio, json, sys
from playwright.async_api import async_playwright
T=sys.argv[1].split(',') if len(sys.argv)>1 else ["birthday-cake","birthday-wish","garba-circle","karwa-chauth","diwali","apology","love-letter","anniversary","proposal","miss-you"]
VPS=[(360,640),(375,667),(390,844),(414,736)]
import os
EXTRA={"proposal":".after,#openNote","miss-you":""}
SHOT=os.environ.get("SHOT")
MEAS="""async ([name,extra])=>{
 go(name); await new Promise(r=>setTimeout(r,700));
 const sc=document.querySelector(`[data-scene="${name}"]`); const m=document.querySelector('main')||document.scrollingElement;
 const nx=[...sc.querySelectorAll('[data-next]'+(extra?','+extra:''))]; if(!window.__init) nx.forEach(b=>{b.dataset.wasHidden=b.hidden; b.hidden=false});
 await new Promise(r=>setTimeout(r,150));
 const over=Math.max(m.scrollHeight-m.clientHeight, document.scrollingElement.scrollHeight-innerHeight);
 const btns=[...sc.querySelectorAll('button,[role=button],input[type=range]')].filter(b=>b.offsetParent&&getComputedStyle(b).visibility!='hidden');
 const bad=btns.map(b=>{const r=b.getBoundingClientRect();return [b.id||(b.className+'').slice(0,16)||b.textContent.trim().slice(0,16),Math.round(r.top),Math.round(r.bottom)]}).filter(x=>x[2]>innerHeight+1||x[1]<-1);
 return {name,over,bad};
}"""
async def main():
  async with async_playwright() as p:
    b=await p.chromium.launch(); out={}
    for t in T:
      for (w,h) in VPS:
        pg=await b.new_page(viewport={"width":w,"height":h},has_touch=True,is_mobile=True); errs=[]
        pg.on("pageerror",lambda e:errs.append(str(e)[:80]))
        await pg.goto(f"http://localhost:8765/{t}/"); await pg.wait_for_timeout(1200)
        if os.environ.get("INIT"): await pg.evaluate("window.__init=1")
        names=await pg.evaluate("[...new Set([...document.querySelectorAll('[data-scene]')].map(s=>s.dataset.scene))]")
        res=[]
        for n in names:
          try:
            r=await pg.evaluate(MEAS,[n,EXTRA.get(t,'')])
            if SHOT: await pg.screenshot(path=f'/tmp/claude-0/audit/shots/{t}-{w}x{h}-{n}{"-i" if os.environ.get("INIT") else ""}.png')
          except Exception as e: r={"name":n,"err":str(e)[:80]}
          if r.get("over",0)>2 or r.get("bad") or r.get("err"): res.append(r)
        out[f"{t} {w}x{h}"]={"problems":res,"errs":errs[:3],"n":len(names)}
        await pg.close()
    await b.close()
    for k,v in out.items(): print(k, v["n"], "scenes", "OK" if not v["problems"] and not v["errs"] else json.dumps(v))
asyncio.run(main())
