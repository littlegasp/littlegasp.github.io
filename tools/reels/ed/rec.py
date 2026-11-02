import sys, json, os; sys.path.insert(0,"/tmp/claude-0")
from fontroute import install
from playwright.sync_api import sync_playwright
D="/tmp/claude-0/newreels/ed/"; os.makedirs(D+"s",exist_ok=True)
for f in os.listdir(D+"s"): os.remove(D+"s/"+f)
FR=[]  # (file, out_dur, clock)
clock=[0.0]
with sync_playwright() as p:
  b=p.chromium.launch()
  ph=b.new_page(viewport={"width":600,"height":600})
  for i in (1,2,3):
    ph.goto(f"http://localhost:8765/birthday-wish/img/demo-{i}.svg"); ph.wait_for_timeout(300); ph.screenshot(path=D+f"photo{i}.jpg",type="jpeg")
  pg=b.new_page(viewport={"width":360,"height":640},device_scale_factor=3); install(pg)
  pg.goto("http://localhost:8765/create/?d=birthday-wish"); pg.wait_for_timeout(3000)
  pg.add_style_tag(content="#pricebox,.pricebox{visibility:hidden!important}")
  def shot(out, real):
    clock[0]+=real; n=len(FR); fn=D+f"s/{n:04d}.png"; pg.screenshot(path=fn); FR.append((fn,out,clock[0]))
  def see(sel):
    pg.evaluate(f"document.querySelector('{sel}').scrollIntoView({{block:'center'}})"); pg.wait_for_timeout(250)
  def typ(sel,text,per=.35):
    see(sel); pg.click(sel)
    for i,ch in enumerate(text):
      pg.keyboard.type(ch)
      if i%2==1 or i==len(text)-1: shot(.09,per*2)
  shot(1.6,0)
  see("#forChips"); shot(.35,4); pg.click("#forChips button >> nth=2"); pg.wait_for_timeout(400); shot(.45,3)
  typ("#f-to","Meera"); typ("#f-from","Aarav"); typ("#f-number","24",.5)
  see("#photos"); shot(.4,4)
  pg.set_input_files("#fileIn",[D+"photo1.jpg",D+"photo2.jpg",D+"photo3.jpg"]); pg.wait_for_timeout(1500); see("#photos"); shot(.5,35)
  see("#capIdeas"); 
  for k in range(2):
    pg.click(f"#capIdeas button >> nth={k}"); pg.wait_for_timeout(300); shot(.3,10)
  see("#reasonIdeas"); shot(.3,3)
  for k in range(3):
    pg.click(f"#reasonIdeas button >> nth={k}"); pg.wait_for_timeout(300); see("#reasonIdeas"); shot(.3,9)
  see("#letterIdeas"); shot(.3,5); pg.click("#letterIdeas button >> nth=2"); pg.wait_for_timeout(500); see("#f-letter"); shot(.5,40)
  # personal touch typed at the end of the letter
  pg.click("#f-letter"); pg.keyboard.press("Control+End"); 
  for i,ch in enumerate("\nP.S. Cake is on me 🎂"):
    pg.keyboard.type(ch)
    if i%3==2: shot(.08,1.0)
  shot(.3,1)
  see("#askIdeas"); pg.click("#askIdeas button >> nth=0"); pg.wait_for_timeout(300); see("#askIdeas"); shot(.5,12)
  # preview
  if pg.is_visible("#tabPreview"):
    pg.click("#tabPreview")
  else:
    pg.click("#toPreview")
  pg.wait_for_timeout(2500)
  shot(.8,2.5)
  fr=pg.frames[1] if len(pg.frames)>1 else None
  try:
    pg.frame_locator("#pv").locator("[data-next]").first.click(timeout=3000)
  except Exception as e: print("noclick",e)
  for k in range(10):
    pg.wait_for_timeout(300); shot(.3,0)
  b.close()
json.dump(FR,open(D+"frames.json","w")); print(len(FR), round(clock[0]))
