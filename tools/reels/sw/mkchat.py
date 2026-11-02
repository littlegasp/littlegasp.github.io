from playwright.sync_api import sync_playwright
import os
os.makedirs("/tmp/claude-0/newreels/sw/cf",exist_ok=True)
DUR=17.4; FPS=30
with sync_playwright() as p:
  b=p.chromium.launch(); pg=b.new_page(viewport={"width":360,"height":640},device_scale_factor=1.5)
  pg.goto("file:///tmp/claude-0/newreels/sw/chat.html"); pg.wait_for_timeout(800)
  last=None
  for i in range(int(DUR*FPS)):
    t=i/FPS; pg.evaluate(f"render({t})")
    pg.screenshot(path=f"/tmp/claude-0/newreels/sw/cf/{i:05d}.png")
  b.close()
print("ok")
