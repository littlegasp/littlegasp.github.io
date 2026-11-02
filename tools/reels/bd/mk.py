from playwright.sync_api import sync_playwright
import os,subprocess
D="/tmp/claude-0/newreels/bd/"
SEG=[("hook",2.4),("n1",.7),("n2",.7),("n3",.7),("end",3.0)]
with sync_playwright() as p:
  b=p.chromium.launch(); pg=b.new_page(viewport={"width":1080,"height":1920})
  pg.goto("file://"+D+"t.html"); pg.wait_for_timeout(1000)
  for k,d in SEG:
    os.makedirs(D+k,exist_ok=True)
    for i in range(int(d*30)):
      pg.evaluate(f"render('{k}',{i/30+(0.4 if k=='hook' else 0)})"); pg.screenshot(path=D+f"{k}/{i:05d}.jpg",type="jpeg",quality=92)
    subprocess.run(["ffmpeg","-v","error","-y","-framerate","30","-i",D+f"{k}/%05d.jpg","-c:v","libx264","-crf","18","-pix_fmt","yuv420p","-r","30",D+f"T_{k}.mp4"],check=True)
  F="file:///tmp/claude-0/fonts/node_modules/@fontsource/"
  for k,v in {"1":"#1 Their childhood crimes 😂","2":"#2 A wish in sparklers ✨","3":"#3 The real gift 🎁"}.items():
    open(D+"l.html","w").write(f"""<style>@font-face{{font-family:Cap;src:url({F}caprasimo/files/caprasimo-latin-400-normal.woff2)}}*{{margin:0}}html,body{{background:transparent}}body{{width:1080px;height:1920px;position:relative}}
    div{{position:absolute;left:60px;right:60px;top:90px;text-align:center;font:400 78px/1.1 Cap,'Noto Color Emoji';color:#fff;background:rgba(26,21,56,.82);padding:26px 20px;border-radius:36px}}</style><div>{v}</div>""")
    pg.goto("file://"+D+"l.html"); pg.wait_for_timeout(300); pg.screenshot(path=D+f"L{k}.png",omit_background=True)
  b.close()
