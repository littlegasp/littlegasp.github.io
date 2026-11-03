"""Late Night Vinyl reel ("tracklist" format): hook over the painted room, then the recorded demo in a framed
phone with a chapter label above it (Intro, Track 01, Side A, Side B, Liner notes, Hidden track, Outro), then the outro card.
Inputs: sf/ frames + story.json from rec-vinyl-story.py, ov/ from overlays.py. Output: out/*.jpg + the mp4 (silent)."""
import json, os, subprocess
from PIL import Image, ImageFilter, ImageDraw
D="/tmp/claude-0/newreels/vinyl/"; R="/home/claude/littlegasp.github.io/"
FPS=30; meta=json.load(open(D+"story.json")); M=dict(meta["marks"]); N=meta["frames"]
for f in os.listdir(D+"out"): os.remove(D+"out/"+f)
# background: the wide night room, blurred and dark
bw=Image.open(R+"late-night-vinyl/img/bg-wide.webp").convert("RGB")
h=1920; w=int(bw.width*h/bw.height); bw=bw.resize((w,h)).crop(((w-1080)//2,0,(w-1080)//2+1080,1920)).filter(ImageFilter.GaussianBlur(22))
BG=Image.eval(bw,lambda v:int(v*.42)).convert("RGBA")
room=Image.open(D+"room.png").convert("RGB").resize((1080,1920))
grad=Image.new("L",(1080,1920)); gd=ImageDraw.Draw(grad)
for y in range(1920): gd.line([(0,y),(1080,y)],fill=int(150+60*abs(y-960)/960))
ROOM=Image.composite(Image.new("RGB",(1080,1920),(6,14,16)),room,grad).convert("RGBA")
ov=lambda n: Image.open(D+"ov/"+n).convert("RGBA")
HK=[ov(f"hk{i}.png") for i in range(3)]; LAB=[ov(f"lab{i}.png") for i in range(8)]; OUT=ov("outro.png")
SC=0.7; FW,FH=int(1080*SC),int(1920*SC); FX,FY=(1080-FW)//2,480
mask=Image.new("L",(FW,FH)); ImageDraw.Draw(mask).rounded_rectangle([0,0,FW-1,FH-1],radius=46,fill=255)
sh=Image.new("RGBA",(1080,1920),(0,0,0,0)); ImageDraw.Draw(sh).rounded_rectangle([FX-4,FY+18,FX+FW+4,FY+FH+30],radius=52,fill=(0,0,0,170))
sh=sh.filter(ImageFilter.GaussianBlur(26))
rim=Image.new("RGBA",(1080,1920),(0,0,0,0)); ImageDraw.Draw(rim).rounded_rectangle([FX-7,FY-7,FX+FW+6,FY+FH+6],radius=52,outline=(233,184,114,110),width=3)
BASE=Image.alpha_composite(BG,sh)
def framed(i):
    im=Image.open(D+"sf/%05d.jpg"%min(i,N-1)).convert("RGB").resize((FW,FH),Image.LANCZOS)
    c=BASE.copy(); c.paste(im,(FX,FY),mask); return Image.alpha_composite(c,rim)
# chapters: (mark, label, speed)
CH=[("open",0,1.0),("cover",1,1.0),("needle",2,1.0),("tracks",3,1.4),("sideb",4,1.2),("notes",5,1.4),("ask",6,1.2),("end",7,1.0)]
names=[c[0] for c in CH]; plan=[]   # (src frame, label)
for k,(nm,lab,sp) in enumerate(CH):
    a=M[nm]; b=M[names[k+1]] if k+1<len(CH) else min(N, M["end"]+96)
    t=a
    while t<b: plan.append((int(t),lab)); t+=sp
HOOKN=114; XF=10; LF=9; OUTN=100
out=[]
n=0
def save(im):
    global n; im.convert("RGB").save(D+"out/%05d.jpg"%n,quality=92); n+=1
for i in range(HOOKN):
    j=0 if i<34 else (1 if i<80 else 2)
    im=Image.alpha_composite(ROOM,HK[j]); save(im)
last=None; prevlab=None; since=0
for idx,(src,lab) in enumerate(plan):
    c=framed(src)
    if lab!=prevlab: since=0; oldlab=prevlab; prevlab=lab
    if since<LF and oldlab is not None:
        a=since/LF
        c=Image.alpha_composite(c,Image.blend(LAB[oldlab],Image.new("RGBA",(1080,1920),(0,0,0,0)),a))
        l=LAB[lab].copy(); l.putalpha(Image.eval(l.getchannel("A"),lambda v:int(v*a)))
        c=Image.alpha_composite(c,l)
    else: c=Image.alpha_composite(c,LAB[lab])
    since+=1
    if idx<XF:   # crossfade from the hook
        c=Image.blend(Image.alpha_composite(ROOM,HK[2]),c,(idx+1)/XF)
    save(c); last=c
for i in range(OUTN):
    a=min(1,(i+1)/14); save(Image.blend(last,OUT,a))
print("frames",n,"seconds",n/FPS)
dst="/tmp/claude-0/newreels/littlegasp-late-night-vinyl-tracklist-reel.mp4"
subprocess.run(["ffmpeg","-y","-v","error","-framerate",str(FPS),"-i",D+"out/%05d.jpg","-f","lavfi","-i","anullsrc=r=44100:cl=stereo",
  "-shortest","-c:v","libx264","-pix_fmt","yuv420p","-profile:v","high","-crf","18","-preset","medium","-c:a","aac","-b:a","128k","-movflags","+faststart",dst],check=True)
print(dst)
