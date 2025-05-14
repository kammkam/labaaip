from PIL import Image

image = Image.open('1.jpg')

print('Размер изображения:', image.size)
print('Формат изображения:', image.format)
print('Цветовая модель изображения:', image.mode)



