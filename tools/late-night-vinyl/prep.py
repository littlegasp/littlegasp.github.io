"""Late Night Vinyl art kit (Canva DAHZzL7M0dc) export -> late-night-vinyl/img/*.webp
Usage: python3 prep.py <folder with 1.png..4.png>   (1 room 9:16, 2 deck square, 3 dance 9:16, 4 bg-wide 16:9)"""
import sys, os
from PIL import Image
src = sys.argv[1]; out = os.path.join(os.path.dirname(__file__), '..', '..', 'late-night-vinyl', 'img'); os.makedirs(out, exist_ok=True)
def go(n, name, size, q=80):
    im = Image.open(os.path.join(src, f'{n}.png')).convert('RGB').resize(size, Image.LANCZOS)
    im.save(os.path.join(out, name + '.webp'), quality=q, method=6); print(name, im.size)
go(1, 'room', (720, 1280)); go(2, 'deck', (900, 900)); go(3, 'dance', (720, 1280)); go(4, 'bg-wide', (1920, 1080), 74)
