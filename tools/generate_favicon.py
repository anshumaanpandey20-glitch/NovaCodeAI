from PIL import Image
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
INPUT = BASE / 'static' / 'images' / 'logo.png'
OUTPUT = BASE / 'static' / 'images' / 'favicon.png'

if not INPUT.exists():
    print(f"Input logo not found at {INPUT}")
    raise SystemExit(1)

with Image.open(INPUT) as img:
    # Create square canvas and paste centered
    size = (32, 32)
    img.thumbnail(size, Image.LANCZOS)

    # Create a transparent background if image has alpha, else white
    if img.mode in ('RGBA', 'LA'):
        background = Image.new('RGBA', size, (0, 0, 0, 0))
    else:
        background = Image.new('RGB', size, (255, 255, 255))

    # Center the thumbnail
    x = (size[0] - img.width) // 2
    y = (size[1] - img.height) // 2
    background.paste(img, (x, y), img if img.mode in ('RGBA', 'LA') else None)

    background.save(OUTPUT, format='PNG')

print(f"Saved favicon to {OUTPUT}")
