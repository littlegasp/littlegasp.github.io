from playwright.sync_api import sync_playwright
import os,subprocess
D="/tmp/claude-0/newreels/op/"
SEG=[("a",2.8),("b",1.6),("e",3.2)]
with sync_playwright() as p:
  b=p.chromium.launch(); pg=b.new_page(viewport={"width":1080,"height":1920})
  pg.goto("file://"+D+"t.html"); pg.wait_for_timeout(1000)
  for k,d in SEG:
    os.makedirs(D+k,exist_ok=True)
    for i in range(int(d*30)):
      pg.evaluate(f"render('{k}',{i/30})"); pg.screenshot(path=D+f"{k}/{i:05d}.jpg",type="jpeg",quality=92)
    subprocess.run(["ffmpeg","-v","error","-y","-framerate","30","-i",D+f"{k}/%05d.jpg","-c:v","libx264","-crf","18","-pix_fmt","yuv420p","-r","30",D+f"T_{k}.mp4"],check=True)
  # clip labels
  F="file:///tmp/claude-0/fonts/node_modules/@fontsource/"
  L={"1":"The family you light up 🪔","2":"The words you never say 💌","3":"The ones far away ✈️","4":"The fights you make up 💗","5":"The gift you hide for them 🎁"}
  for k,v in L.items():
    open(D+"l.html","w").write(f"""<style>@font-face{{font-family:Cap;src:url({F}caprasimo/files/caprasimo-latin-400-normal.woff2)}}*{{margin:0}}html,body{{background:transparent}}body{{width:1080px;height:1920px;position:relative}}
    div{{position:absolute;left:50px;right:50px;top:110px;text-align:center;font:400 84px/1.1 Cap,'Noto Color Emoji';color:#fff;text-shadow:0 6px 24px rgba(0,0,0,.45)}}</style><div>{v}</div>""")
    pg.goto("file://"+D+"l.html"); pg.wait_for_timeout(300); pg.screenshot(path=D+f"L{k}.png",omit_background=True)
  b.close()
