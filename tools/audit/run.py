import asyncio, json, os
from playwright.async_api import async_playwright
B="http://localhost:8765/"
PAGES=["","about.html","contact.html","privacy.html","terms.html","refund.html","create/",
"digital-surprise-gifts/","birthday-surprise-website/","apology-website/","digital-love-letter/","anniversary-surprise-website/","proposal-surprise-website/","long-distance-relationship-gift/","karwa-chauth-gift-for-wife/","diwali-surprise-website/","navratri-garba-surprise/",
"birthday-cake/","birthday-wish/","garba-circle/","karwa-chauth/","diwali/","apology/","love-letter/","anniversary/","proposal/","miss-you/"]
VP={"phone":{"width":375,"height":667},"laptop":{"width":1366,"height":768}}
EXT=("fonts.g","razorpay","script.google","googletagmanager","google-analytics","pinterest","clarity")
async def check(b,path,vn):
  ctx=await b.new_context(viewport=VP[vn]); pg=await ctx.new_page(); errs=[]; bad=[]
  pg.on("pageerror",lambda e:errs.append(str(e)[:160]))
  pg.on("console",lambda m: errs.append("console: "+m.text[:160]) if m.type=="error" else None)
  pg.on("response",lambda r: bad.append(f"{r.status} {r.url}") if r.status>=400 and not any(x in r.url for x in EXT) else None)
  pg.on("requestfailed",lambda r: bad.append(f"FAIL {r.url}") if not any(x in r.url for x in EXT) else None)
  await pg.goto(B+path); await pg.wait_for_timeout(2500)
  ov=await pg.evaluate("document.documentElement.scrollWidth-innerWidth")
  await ctx.close()
  return dict(errs=errs,bad=bad,overflowX=ov)
async def main():
  async with async_playwright() as p:
    b=await p.chromium.launch(); out={}
    for path in PAGES:
      for vn in VP:
        r=await check(b,path,vn)
        if r["errs"] or r["bad"] or r["overflowX"]>1: out[f"{path or '/'} [{vn}]"]=r
    json.dump(out,open("/tmp/claude-0/audit/run.json","w"),indent=1)
    print(json.dumps(out,indent=1) if out else "all pages clean")
    await b.close()
asyncio.run(main())
