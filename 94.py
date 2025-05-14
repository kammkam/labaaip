from PIL import Image, ImageDraw, Image, ImageFont
import os

inp1 = '.'
out1 = 'water_images'

os.makedirs(out1, exist_ok=True)

try:
    font = ImageFont.truetype('arial.ttf', 36)
except IOError:
    font = ImageFont.load_default()  # для шрифта

for i in range(1, 6):
    name = f'{i}.jpg'
    image = Image.open(name).convert("RGBA")

    # слой для вв знака
    watermark = Image.new('RGBA', image.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(watermark)

    text = "cat cat cat cat cat"

    textbbox = draw.textbbox((0, 0), text, font=font)
    textwidht = textbbox[2] - textbbox[0]
    textheight = textbbox[3] - textbbox[1]

    # там где он находится
    x = image.width - textwidht - 10
    y = image.height - textheight - 10

    draw.text((x, y), text, font=font, fill=(255, 0, 0, 128))  # 128 значит что он полупразрачный  и ргб

    combined = Image.alpha_composite(image, watermark)  # добавляем вв в картинку

    combined = combined.convert("RGB")
    combined.save(os.path.join(out1, f'watermarked_{i}.jpg'))
