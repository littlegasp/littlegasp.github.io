"""Turn the Love Catcher art kit export (Canva DAHZy5XupUc, pages 1-8 as PNG, transparent background)
into love-catcher/img/*.webp.  Usage: python3 prep.py <folder with 1.png..8.png>
Pages: 1 machine-her, 2 machine-him, 3 couple-her, 4 couple-him, 5 bg-wide, 6 claw, 7 coin, 8 toys sheet."""
import sys, os
from PIL import Image
src = sys.argv[1]; out = os.path.join(os.path.dirname(__file__), '..', '..', 'love-catcher', 'img'); os.makedirs(out, exist_ok=True)
def page(n): return Image.open(os.path.join(src, f'{n}.png'))
def save(im, name, w=None, q=82):
    if w and im.width > w: im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
    im.save(os.path.join(out, name + '.webp'), quality=q, method=6); print(name, im.size)
for n, name in [(1, 'machine-her'), (2, 'machine-him'), (3, 'couple-her'), (4, 'couple-him')]:
    save(page(n).convert('RGB').resize((720, 1280), Image.LANCZOS), name)
save(page(5).convert('RGB').resize((1920, 1080), Image.LANCZOS), 'bg-wide', q=78)
def trim(im):
    im = im.convert('RGBA'); a = im.split()[3].point(lambda v: 255 if v > 24 else 0); bb = a.getbbox(); return im.crop(bb) if bb else im
save(trim(page(6)), 'claw', 360); save(trim(page(7)), 'coin', 240)
# toys sheet: 3 x 2 grid -> bear, bunny, cat, heart, star, gift
sh = page(8).convert('RGBA'); W, H = sh.size
names = ['toy-bear', 'toy-bunny', 'toy-cat', 'toy-heart', 'toy-star', 'gift']
for i, nm in enumerate(names):
    c, r = i % 3, i // 3
    save(trim(sh.crop((c * W // 3, r * H // 2, (c + 1) * W // 3, (r + 1) * H // 2))), nm, 300)
