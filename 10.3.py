from PIL import Image, ImageDraw, ImageFont


def add_text(image_path, name, output_path):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    #шрифт
    font_path = "C:/Windows/Fonts/arialbd.ttf"
    font = ImageFont.truetype(font_path, 40)


    text = f"{name}, поздравляю!"

    #размеры
    w, h = image.size
    bbox = draw.textbbox((0,0), text, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]

    #положение текста
    x = (w - text_w) // 2
    y = h - text_h - 20


    draw.text((x, y), text, font=font, fill="red")


    image.save(output_path, "PNG")
    print(f"Открытка сохранена как {output_path}")


name = input("Введите имя того, кого хотите поздравить: ")
holiday = input("К какому празднику открытка? день рождение, новый год, 8 марта ").lower()

postcards = {
    "день рождение": "bir.jpg",
    "новый год": "new.jpg",
    "8 марта": "mar.jpg"
}

if holiday in postcards:
    input_file = postcards[holiday]
    output_file = f"{holiday}_{name}.png"
    add_text(input_file, name, output_file)
else:
    print("Открытка к этому празднику не найдена.")