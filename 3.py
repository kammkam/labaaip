import os
from PIL import Image, ImageFilter

inp = '.'  # текущая папка
out = 'out'

os.makedirs(out, exist_ok=True) #папка для сохранения

for i in range(1, 6):
    name = f'{i}.jpg'
    image = Image.open(name)
    filt = image.filter(ImageFilter.SHARPEN) #резкость ++
    filt.save(os.path.join(out, f'filtered_{i}.jpg'))
