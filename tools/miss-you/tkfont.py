import sys; sys.path.insert(0,"/tmp/claude-0")
from fontroute import install
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
  b=p.chromium.launch()
  for (w,h,city,frm) in [(360,640,'Bengaluru','Pune'),(360,640,'Thiruvananthapuram','Navi Mumbai'),(375,667,'San Francisco','Hyderabad'),(1366,768,'Bengaluru','Pune')]:
    pg=b.new_page(viewport={"width":w,"height":h}); install(pg)
    pg.goto("http://localhost:8765/miss-you/"); pg.wait_for_timeout(2000)
    pg.evaluate(f"document.querySelector('#tkTo').textContent='{city}';document.querySelector('#tkFrom').textContent='{frm}'; go(seq.indexOf('ask'))"); pg.wait_for_timeout(2800)
    print(w,city,pg.evaluate("['#tkFrom','#tkTo'].map(k=>{const e=document.querySelector(k);return [e.style.fontSize,e.className,e.getBoundingClientRect().height|0]})"))
    pg.screenshot(path=f"/tmp/claude-0/mykit/tkf-{w}-{city}.png")
  b.close()
