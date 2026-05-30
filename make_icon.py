from PIL import Image
import os

base = os.path.dirname(os.path.abspath(__file__))
src = os.path.join(base, "1.jpg")
dst = os.path.join(base, "app_icon.ico")

img = Image.open(src).convert("RGBA")
sizes = [256, 128, 64, 48, 32, 16]
icons = [img.resize((s, s), Image.LANCZOS) for s in sizes]
icons[0].save(dst, format="ICO", sizes=[(s, s) for s in sizes], append_images=icons[1:])
print("Saved:", dst)
