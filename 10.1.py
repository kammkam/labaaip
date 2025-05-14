from PIL import Image

def crop_postcard(image_path, crop_box, new_name):

    image = Image.open(image_path)

    cropped = image.crop(crop_box)  # crop obrez

    cropped.save(new_name)
    print(f"Изображение сохранено как {new_name}")

crop_postcard("image.jpg", (50, 50, 400, 300), "image_cropped.jpg")

