rec[0]=False
pg.evaluate("window.__done=0;addEventListener('message',e=>{if(e.data&&e.data.type==='lg-autoplay-done')window.__done=1})")
pg.evaluate(f"document.getElementById('f').src='http://localhost:8765/{AUTOKEY}/?autoplay=1'")
for _ in range(60): step(False); time.sleep(.05)
time.sleep(2)
for _ in range(10): step(False)
rec[0]=True
n=0
SCN=[]
while not pg.evaluate("window.__done") and n<30*130:
    step(); n+=1
    if n%5==0:
        try: SCN.append((NF[0], pg.frames[1].evaluate("typeof seq!=='undefined'?seq[current]:''")))
        except Exception: pass
import json as _j; _j.dump(SCN,open(OUT+"/scenes.json","w"))
W(600)
