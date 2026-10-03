"""
Prepare Karwa Chauth artwork for the website.

Put the downloaded Canva images in one folder with these names (.png/.jpg/.jpeg/.webp):
  bg, bg2, moon, channi, diya, frame, thali, lantern, cloth, card, scroll, corner
Then run:
  pip install pillow numpy
  python tools/prepare-art.py <that-folder> karwa-chauth/img

How the black background is removed:
  "cutout" - removes only the black that touches the outside edge (plus the centre, for
             rings/frames), so dark maroon/clay parts of the object stay fully solid.
  "glow"   - turns brightness into transparency; best for thin gold line art.
"""
import sys, pathlib
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

SRC, OUT = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
OUT.mkdir(parents=True, exist_ok=True)

def find(name):
    for ext in (".png", ".jpg", ".jpeg", ".webp"):
        p = SRC / (name + ext)
        if p.exists():
            return Image.open(p).convert("RGB")
    sys.exit(f"Missing {name}.png/.jpg/.webp in {SRC}")

def trim(img):
    return img.crop(img.getbbox() or (0, 0, *img.size))

def glow(im, floor=10):
    a = np.asarray(im).astype(np.float32)
    alpha = np.clip((a.max(axis=2) - floor) / (255 - floor), 0, 1)
    rgb = np.clip(a / 255 / np.maximum(alpha, 1e-6)[..., None], 0, 1)
    return trim(Image.fromarray(np.dstack([rgb * 255, alpha * 255]).astype(np.uint8), "RGBA"))

def cutout(im, thr=34, centre=False):
    a = np.asarray(im)
    mask = Image.fromarray((a.max(axis=2) < thr).astype(np.uint8) * 255, "L").copy()  # copy: arrays are read-only
    w, h = mask.size
    seeds = [(x, 0) for x in range(0, w, 4)] + [(x, h - 1) for x in range(0, w, 4)] + \
            [(0, y) for y in range(0, h, 4)] + [(w - 1, y) for y in range(0, h, 4)]
    if centre:
        seeds.append((w // 2, h // 2))
    for s in seeds:
        if mask.getpixel(s) == 255:
            ImageDraw.floodfill(mask, s, 128)
    bg = np.asarray(mask) == 128
    alpha = Image.fromarray(np.where(bg, 0, 255).astype(np.uint8), "L")
    alpha = alpha.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(1))  # trim dark fringe, soften edge
    out = im.convert("RGBA"); out.putalpha(alpha)
    return trim(out)

def fit(im, width):
    if im.width > width:
        im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    return im

def square(im):
    side = max(im.size); sq = Image.new("RGBA", (side, side))
    sq.paste(im, ((side - im.width) // 2, (side - im.height) // 2)); return sq

def save(im, name, q=82):
    p = OUT / f"{name}.webp"
    im.save(p, "WEBP", quality=q, method=6)
    print(f"{p}  {im.size[0]}x{im.size[1]}  {p.stat().st_size // 1024} KB")

save(fit(find("bg"), 1080), "bg", 72)
save(fit(find("bg2"), 1080), "bg2", 72)
save(fit(find("moon"), 640), "moon", 80)
save(fit(square(cutout(find("channi"), centre=True)), 640), "channi")
save(fit(cutout(find("frame"), centre=True), 720), "frame")
save(fit(cutout(find("diya")), 320), "diya")
save(fit(cutout(find("thali")), 560), "thali")
save(fit(cutout(find("lantern")), 300), "lantern")
save(fit(cutout(find("cloth")), 1080), "cloth", 76)
save(fit(cutout(find("card")), 760), "card")
save(fit(cutout(find("scroll")), 900), "scroll")
save(fit(glow(find("corner")), 360), "corner")
