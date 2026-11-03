"""Records the Late Night Vinyl showcase run (?autoplay=1) frame by frame at 30 fps in virtual time,
and logs which scene is on screen for every frame (vinyl/scenes.json) so the reel can cut chapters on it.
Needs: repo on :8765, /tmp/claude-0/reelhost on :8766, /tmp/claude-0/vtime.js and fontroute.py."""
import sys, os, json, base64, time; sys.path.insert(0,"/tmp/claude-0")
from fontroute import install
from playwright.sync_api import sync_playwright
OUT="/tmp/claude-0/newreels/vinyl"; os.makedirs(OUT+"/vf",exist_ok=True)
for f in os.listdir(OUT+"/vf"): os.remove(OUT+"/vf/"+f)
FPS=30; DT=1000/FPS; VT=open("/tmp/claude-0/vtime.js").read()
with sync_playwright() as p:
    b=p.chromium.launch()
    ctx=b.new_context(viewport={"width":1080,"height":1920}); ctx.add_init_script(VT)
    pg=ctx.new_page(); install(pg); errs=[]
    pg.on("pageerror",lambda e: errs.append(str(e)))
    pg.goto("http://localhost:8766/host.html")
    pg.evaluate("window.__done=0;addEventListener('message',e=>{if(e.data&&e.data.type==='lg-autoplay-done')window.__done=1})")
    pg.evaluate("document.getElementById('f').src='http://localhost:8765/late-night-vinyl/?autoplay=1'")
    cdp=ctx.new_cdp_session(pg); NF=0; scenes=[]
    def step(cap=True):
        global NF
        for fr in pg.frames:
            try: fr.evaluate(f"window.__vt && __vt.advance({DT})")
            except Exception: pass
        if cap:
            d=cdp.send("Page.captureScreenshot",{"format":"jpeg","quality":90})["data"]
            open(f"{OUT}/vf/{NF:05d}.jpg","wb").write(base64.b64decode(d)); NF+=1
            try: scenes.append(pg.frames[1].evaluate("seq[current]"))
            except Exception: scenes.append(None)
    for _ in range(60): step(False); time.sleep(.05)
    time.sleep(2)
    for _ in range(10): step(False)
    n=0
    while not pg.evaluate("window.__done") and n<FPS*130: step(); n+=1
    for _ in range(18): step()
    b.close()
json.dump({"fps":FPS,"frames":NF,"scenes":scenes},open(OUT+"/scenes.json","w"))
from itertools import groupby
t=0
for k,g in groupby(scenes):
    l=len(list(g)); print(f"{t/FPS:6.2f}s {k} ({l/FPS:.1f}s)"); t+=l
print("frames",NF,"errors",errs[:3])
