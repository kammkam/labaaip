from pathlib import Path
from PIL import Image

input_folder = Path('images')
output_folder = input_folder / 'processed'


output_folder.mkdir(parents=True, exist_ok=True)

#обработка
for image_path in input_folder.glob('*.*'):
    if image_path.is_file() and image_path.suffix.lower() in ['.jpg', '.jpeg', '.png', '.bmp']:

        with Image.open(image_path) as img:
            #  делаем изображение черно-белым
            gray_img = img.convert('L')


            output_path = output_folder / image_path.name
            gray_img.save(output_path)

print('Обработка завершена.')
