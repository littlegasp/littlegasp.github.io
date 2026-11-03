"""Late Night Vinyl reel recording: drives the demo (not the fast showcase run) with a visible finger,
slow enough to read every track, at 30 fps in virtual time. Writes frames + a chapter log to /tmp/claude-0/newreels/vinyl/.
Needs: repo on :8765, /tmp/claude-0/reelhost on :8766, /tmp/claude-0/vtime.js and fontroute.py."""
import sys, os, json, base64, time; sys.path.insert(0,"/tmp/claude-0")
from fontroute import install
from playwright.sync_api import sync_playwright
OUT="/tmp/claude-0/newreels/vinyl"; os.makedirs(OUT+"/sf",exist_ok=True)
for f in os.listdir(OUT+"/sf"): os.remove(OUT+"/sf/"+f)
FPS=30; DT=1000/FPS; VT=open("/tmp/claude-0/vtime.js").read()
marks=[]
with sync_playwright() as p:
    b=p.chromium.launch()
    ctx=b.new_context(viewport={"width":1080,"height":1920}); ctx.add_init_script(VT)
    pg=ctx.new_page(); install(pg); errs=[]
    pg.on("pageerror",lambda e: errs.append(str(e)))
    pg.goto("http://localhost:8766/host.html")
    pg.evaluate("document.getElementById('f').src='http://localhost:8765/late-night-vinyl/'")
    cdp=ctx.new_cdp_session(pg); NF=[0]; rec=[False]
    def step(cap=True):
        for fr in pg.frames:
            try: fr.evaluate(f"window.__vt && __vt.advance({DT})")
            except Exception: pass
        if cap and rec[0]:
            d=cdp.send("Page.captureScreenshot",{"format":"jpeg","quality":92})["data"]
            open(f"{OUT}/sf/{NF[0]:05d}.jpg","wb").write(base64.b64decode(d)); NF[0]+=1
    def W(ms):
        for _ in range(max(0,round(ms/DT))): step()
    def mark(name): marks.append((name, NF[0]))
    for _ in range(90): step(False); time.sleep(.03)
    time.sleep(1.5)
    for _ in range(10): step(False)
    F=pg.frame_locator("#f")
    def fin(x,y,tap=False): pg.evaluate(f"finger({x},{y},{str(tap).lower()})")
    def box(sel):
        bb=F.locator(sel).first.bounding_box()
        if not bb: pg.screenshot(path=OUT+"/fail.png"); raise SystemExit("no box for "+sel)
        return bb
    def ready(sel):
        for _ in range(400):
            ok=pg.frames[1].evaluate("s=>{const e=document.querySelector(s);if(!e)return false;const c=getComputedStyle(e);return c.visibility!=='hidden'&&c.display!=='none'&&e.offsetParent!==null&&!e.disabled&&!e.closest('.off')}", sel)
            if ok: return
            step()
    def tap(sel, after=700):
        ready(sel); bb=box(sel); x,y=bb["x"]+bb["width"]/2, bb["y"]+bb["height"]/2
        fin(x,y); W(260); fin(x,y,True); pg.mouse.click(x,y); W(170); pg.evaluate("nofinger()"); W(after)
    def drag(pts, steps=10, hold=0):
        x,y=pts[0]; fin(x,y); W(300); pg.mouse.move(x,y); pg.mouse.down()
        for (nx,ny) in pts[1:]:
            for k in range(1,steps+1):
                xx=x+(nx-x)*k/steps; yy=y+(ny-y)*k/steps; pg.mouse.move(xx,yy); fin(xx,yy); step()
            x,y=nx,ny
        if hold: W(hold)
        pg.mouse.up(); pg.evaluate("nofinger()")
    rec[0]=True
    mark("open"); W(1800); tap("#tag", 500)
    mark("cover"); W(600)
    o=box("#out"); y=o["y"]+o["height"]/2
    drag([(o["x"]+o["width"]*.9,y),(o["x"]+o["width"]*1.25,y),(o["x"]+o["width"]*1.45,y)], steps=12)
    W(2200); tap("#afterCover", 500)
    mark("needle"); W(700)
    d=box("#deck")
    drag([(d["x"]+d["width"]*.805,d["y"]+d["height"]*.58),(d["x"]+d["width"]*.74,d["y"]+d["height"]*.61),(d["x"]+d["width"]*.64,d["y"]+d["height"]*.62)], steps=14, hold=200)
    W(1200); mark("tracks"); W(1900)
    fr=pg.frames[1]
    for i in range(4):
        tap("#nextTrack", 2300 if i<2 else 1500)
    W(500); tap("#afterPlay", 500)
    mark("sideb"); W(1500)
    tap("#gNext", 1300); tap("#gNext", 1300); tap("#afterB", 400)
    mark("notes"); W(3600); tap("#notesSkip", 1500); tap("#afterNotes", 400)
    mark("ask")
    for _ in range(300):
        if not fr.evaluate("document.querySelector('#answers').classList.contains('off')"): break
        step()
    W(1300); tap("#yesBtn", 300)
    mark("end"); W(4200)
    b.close()
json.dump({"fps":FPS,"frames":NF[0],"marks":marks},open(OUT+"/story.json","w"),indent=1)
print(NF[0]/FPS,"s",marks,errs[:3])
