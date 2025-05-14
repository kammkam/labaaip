from pathlib import Path
from PIL import Image


folder = Path('images')  


allowed_extensions = ['.jpg', '.jpeg', '.png']


for file in folder.iterdir():
    if file.is_file() and file.suffix.lower() in allowed_extensions:

        with Image.open(file) as img:
            img.show()

            # info
            print(f"Файл: {file.name}")
            print(f"Формат: {img.format}")
            print(f"Размер: {img.size}")
            print(f"Цветовая модель: {img.mode}")
            print('-' * 30)