"""Generate Android mipmap launcher icons and adaptive icon layers from 1.jpg"""
import os
from PIL import Image

base = os.path.dirname(os.path.abspath(__file__))
src = os.path.join(os.path.dirname(base), "1.jpg")
res = os.path.join(base, "app", "src", "main", "res")

img = Image.open(src).convert("RGBA")

# Standard launcher icons
sizes = {
    "mipmap-mdpi":    48,
    "mipmap-hdpi":    72,
    "mipmap-xhdpi":   96,
    "mipmap-xxhdpi":  144,
    "mipmap-xxxhdpi": 192,
}
for folder, size in sizes.items():
    out = img.resize((size, size), Image.LANCZOS)
    path = os.path.join(res, folder, "ic_launcher.png")
    out.save(path, "PNG")
    print(f"Saved {path}")

# Adaptive icon foreground (108x108 dp nominal; use 432px at xxxhdpi x4 for best quality)
# Foreground: icon centred on transparent canvas with 18% safe-zone padding
for folder, size in sizes.items():
    canvas_size = int(size * (108 / 72))  # adaptive canvas is 108dp, regular is 72dp
    canvas = Image.new("RGBA", (canvas_size, canvas_size), (0, 0, 0, 0))
    # Fit icon inside safe zone (66% of canvas = 66/108 ≈ 0.611)
    icon_size = int(canvas_size * 0.72)
    resized = img.resize((icon_size, icon_size), Image.LANCZOS)
    offset = (canvas_size - icon_size) // 2
    canvas.paste(resized, (offset, offset), resized)
    path = os.path.join(res, folder, "ic_launcher_foreground.png")
    canvas.save(path, "PNG")
    print(f"Saved {path}")

print("All icons generated.")
