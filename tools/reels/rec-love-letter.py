import sys, os, json, base64, time; sys.path.insert(0,"/tmp/claude-0")
from fontroute import install
from playwright.sync_api import sync_playwright
KEY="love-letter"; AUTOKEY="love-letter"; OUT="/tmp/claude-0/newreels/love-letter"; os.makedirs(OUT+"/vf",exist_ok=True)
for f in os.listdir(OUT+"/vf"): os.remove(OUT+"/vf/"+f)
FPS=30; DT=1000/FPS; VT=open("/tmp/claude-0/vtime.js").read()
with sync_playwright() as p:
    b=p.chromium.launch()
    ctx=b.new_context(viewport={"width":1080,"height":1920}); ctx.add_init_script(VT)
    pg=ctx.new_page(); install(pg); errs=[]
    pg.on("pageerror",lambda e: errs.append(str(e)))
    pg.goto("http://localhost:8766/host.html")
    url={"apology":"apology/","diwali":"diwali/","garba-circle":"garba-circle/","birthday-wish":"birthday-wish/","karwa-chauth":"karwa-chauth/","birthday-cake":"birthday-cake/","love-letter":"love-letter/","anniversary":"anniversary/"}[KEY]
    pg.evaluate(f"document.getElementById('f').src='http://localhost:8765/{url}'")
    cdp=ctx.new_cdp_session(pg); NF=[0]; rec=[False]
    def step(cap=True):
        for fr in pg.frames:
            try: fr.evaluate(f"window.__vt && __vt.advance({DT})")
            except Exception: pass
        if cap and rec[0]:
            d=cdp.send("Page.captureScreenshot",{"format":"jpeg","quality":90})["data"]
            open(f"{OUT}/vf/{NF[0]:05d}.jpg","wb").write(base64.b64decode(d)); NF[0]+=1
    def W(ms):
        for _ in range(max(0,round(ms/DT))): step()
    # pre-roll: let the page load and build (not recorded)
    for _ in range(90): step(False); time.sleep(.03)
    time.sleep(1.5)
    for _ in range(10): step(False)
    F=pg.frame_locator("#f"); fr=pg.frames[1]
    def fin(x,y,tap=False): pg.evaluate(f"finger({x},{y},{str(tap).lower()})")
    def tap(sel, n_=0, after=700):
        loc=F.locator(sel).nth(n_); bb=loc.bounding_box()
        if not bb or bb["y"]<0 or bb["y"]+bb["height"]>1900:
            loc.evaluate("e=>e.scrollIntoView({block:'center'})"); W(100); bb=loc.bounding_box()
        if not bb: pg.screenshot(path=OUT+"/fail.png"); raise SystemExit("no box for "+sel)
        x,y=bb["x"]+bb["width"]/2, bb["y"]+bb["height"]/2
        fin(x,y); W(200); fin(x,y,True); pg.mouse.click(x,y); W(170); pg.evaluate("nofinger()"); W(after)
    def drag(pts, steps=8, hold=0):
        x,y=pts[0]; fin(x,y); W(230); pg.mouse.move(x,y); pg.mouse.down()
        for (nx,ny) in pts[1:]:
            for k in range(1,steps+1):
                xx=x+(nx-x)*k/steps; yy=y+(ny-y)*k/steps; pg.mouse.move(xx,yy); fin(xx,yy); step()
            x,y=nx,ny
        if hold: W(hold)
        pg.mouse.up(); pg.evaluate("nofinger()")
    rec[0]=True; v0=fr.evaluate("__vt.now()"); MUSIC_AT=None
    def music_now():
        global MUSIC_AT
        MUSIC_AT=(fr.evaluate("__vt.now()")-v0)/1000
    exec(open("/tmp/claude-0/flow-auto.py").read())
    plays=fr.evaluate("__plays")
    b.close()
play=[q for q in plays][0] if plays else None
if MUSIC_AT is not None: play={"at":MUSIC_AT*1000+v0,"ct":0,"src":"synth:"+KEY}
meta={"fps":FPS,"frames":NF[0],"dur":NF[0]/FPS,"play_at":(play["at"]-v0)/1000 if play else None,"seek":play["ct"] if play else 0,"src":play["src"] if play else None}
json.dump(meta,open(OUT+"/vmeta.json","w"),indent=1); print(KEY,meta,errs[:3])
