from playwright.sync_api import sync_playwright
import os,sys
D="/tmp/claude-0/newreels/mc/"
for d in ("a","b"): os.makedirs(D+d,exist_ok=True)
with sync_playwright() as p:
  b=p.chromium.launch(); pg=b.new_page(viewport={"width":360,"height":640},device_scale_factor=3)
  pg.goto("file://"+D+"chat.html"); pg.wait_for_timeout(1200)
  if len(sys.argv)>1:
    for i,t in enumerate(sys.argv[1:]): pg.evaluate(f"render({t})"); pg.screenshot(path=D+f"chk{i}.png")
  else:
    for i in range(int(5.4*30)): pg.evaluate(f"render({i/30})"); pg.screenshot(path=D+f"a/{i:05d}.jpg",type="jpeg",quality=92)
    for i in range(int(5.2*30)): pg.evaluate(f"render({10+i/30})"); pg.screenshot(path=D+f"b/{i:05d}.jpg",type="jpeg",quality=92)
  b.close()
