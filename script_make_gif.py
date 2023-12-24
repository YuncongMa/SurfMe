# Yuncong Ma, 12/24/2023
#

import os
from PIL import Image

dir_figure = '/Users/yuncongma/Desktop/Figures'

image_size = (800, 600)

list_subdir = [x[0] for x in os.walk(dir_figure)]
for i, subdir in enumerate(list_subdir):
    if subdir == dir_figure:
        continue
    all_files = os.listdir(subdir)
    list_figure = [file for file in all_files if file.lower().endswith('.jpg') and not file.endswith('(Compressed).jpg')]
    for j, file_figure in enumerate(list_figure):
        original_image = Image.open(os.path.join(subdir, file_figure))
        # image_rgb.thumbnail(image_size)
        # image_rgb.save(os.path.join(subdir, file_figure.replace('.jpg', '(Compressed).jpg')))
        # image_rgb.close()
        # Calculate the size keeping the aspect ratio
        original_image.thumbnail(image_size, Image.Resampling.LANCZOS)
        # Create a white background
        new_image = Image.new("RGB", image_size, (255, 255, 255))
        # Get the size of the thumbnail and calculate the position to paste
        thumb_size = original_image.size
        position = ((image_size[0] - thumb_size[0]) // 2, (image_size[1] - thumb_size[1]) // 2)
        # Paste the thumbnail onto the white background
        new_image.paste(original_image, position)
        new_image.save(os.path.join(subdir, file_figure.replace('.jpg', '(Compressed).jpg')))
        new_image.close()

    frames = [Image.open(os.path.join(subdir, file_figure.replace('.jpg', '(Compressed).jpg'))) for i, file_figure in enumerate(list_figure)]
    frame_one = frames[0]
    frame_one.save(os.path.join(dir_figure, os.path.split(subdir)[1] + '.gif'), format="GIF", append_images=frames, save_all=True, duration=500, loop=0, optimize=False)


