import json, os
from PIL import Image, ImageDraw, ImageFont
D="/tmp/claude-0/newreels/ed/"; os.makedirs(D+"o",exist_ok=True)
FP="/tmp/claude-0/fonts/node_modules/@fontsource/"
def ttf(): 
  import glob
  return None
F=json.load(open(D+"frames.json"))
F=F[:35]  # drop the still tail of the preview
F[0]=(F[0][0],2.6,0)
# fonts: convert woff2 not supported by PIL; use rendered PNG pills via playwright instead
from playwright.sync_api import sync_playwright
pills={}
with sync_playwright() as p:
  b=p.chromium.launch(); pg=b.new_page(viewport={"width":1080,"height":1920})
  CSS=f"""<style>@font-face{{font-family:Fig;font-weight:800;src:url(file://{FP}figtree/files/figtree-latin-800-normal.woff2)}}@font-face{{font-family:Cap;src:url(file://{FP}caprasimo/files/caprasimo-latin-400-normal.woff2)}}*{{margin:0}}html,body{{background:transparent}}body{{width:1080px;height:1920px;position:relative;font-family:Fig,'Noto Color Emoji'}}
  .pill{{position:absolute;right:36px;top:1600px;background:#2A1F5C;color:#FFC857;font:800 64px Fig,'Noto Color Emoji';padding:16px 34px;border-radius:999px;box-shadow:0 10px 30px rgba(0,0,0,.35)}}
  .hook{{position:absolute;left:50px;right:50px;top:620px;background:#2A1F5C;color:#fff;border-radius:44px;padding:50px 40px;text-align:center;font:400 92px/1.1 Cap,'Noto Color Emoji';box-shadow:0 20px 50px rgba(0,0,0,.35)}}
  .hook b{{color:#FFC857;font-weight:400}}
  .end{{position:absolute;inset:0;background:rgba(42,31,92,.86);display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;color:#fff;padding:0 70px}}
  .end h1{{font:400 120px/1.08 Cap,'Noto Color Emoji'}} .end p{{font:800 54px Fig;color:#FFC857;margin-top:40px}}</style>"""
  def png(html,name):
    open(D+"t.html","w").write(CSS+html); pg.goto("file://"+D+"t.html"); pg.wait_for_timeout(200); pg.screenshot(path=D+name,omit_background=True)
  png('<div class="hook">Making a birthday surprise,<br><b>start to finish</b> ⏱</div>','hook.png')
  secs=sorted(set(int(round(c)) for _,_,c in F))
  for s in secs: png(f'<div class="pill">⏱ {s//60}:{s%60:02d}</div>',f"pill{s}.png")
  png('<div class="end"><h1>Ready to send 💌</h1><p>Make a Wish · Try it free · link in bio</p></div>','end.png')
  b.close()
hook=Image.open(D+"hook.png"); end=Image.open(D+"end.png")
lst=[]
for i,(fn,dur,c) in enumerate(F):
  im=Image.open(fn).convert("RGBA")
  im.alpha_composite(Image.open(D+f"pill{int(round(c))}.png"))
  if i==0: im.alpha_composite(hook)
  out=D+f"o/{i:04d}.png"; im.convert("RGB").save(out); lst.append((out,dur))
last=Image.open(F[-1][0]).convert("RGBA"); last.alpha_composite(Image.open(D+f"pill{int(round(F[-1][2]))}.png")); last.alpha_composite(end)
last.convert("RGB").save(D+"o/end.png"); lst.append((D+"o/end.png",3.0))
with open(D+"list.txt","w") as f:
  for fn,d in lst: f.write(f"file '{fn}'\nduration {d}\n")
  f.write(f"file '{lst[-1][0]}'\n")
print(sum(d for _,d in lst))
