from playwright.sync_api import sync_playwright
import os,sys
os.makedirs("/tmp/claude-0/newreels/ml/f",exist_ok=True)
with sync_playwright() as p:
  b=p.chromium.launch(); pg=b.new_page(viewport={"width":1080,"height":1920})
  pg.goto("file:///tmp/claude-0/newreels/ml/ride.html"); pg.wait_for_timeout(1500)
  T=pg.evaluate("TOTAL"); print("total",T)
  only=sys.argv[1:] 
  ts=[float(x) for x in only] if only else [i/30 for i in range(int(T*30))]
  for i,t in enumerate(ts):
    pg.evaluate(f"render({t})")
    pg.screenshot(path=f"/tmp/claude-0/newreels/ml/f/{i:05d}.jpg",type="jpeg",quality=92)
  b.close()
