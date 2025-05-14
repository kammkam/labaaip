from PIL import Image, ImageOps

image = Image.open('hor.jpg')

small_image = image.resize((image.width // 3, image.height // 3))
small_image.save('size.jpg')



ver = ImageOps.flip(image)
ver.save('ver.jpg')
