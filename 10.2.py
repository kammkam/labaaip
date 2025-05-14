from PIL import Image


postcards = {
    "день рождение": "bir.jpg",
    "новый год": "new.jpg",
    "8 марта": "mar.jpg"
}


holiday = input("К какому празднику вам нужна открытка? день рождение, новый год, 8 марта ").lower()


if holiday in postcards:
    image = Image.open(postcards[holiday])
    image.show()
else:
    print("Открытка к этому празднику не найдена.")
