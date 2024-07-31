# -------------------Exercise 3---------------------------- 
# The image names were generated in two formats .png and .jpg:
# import random
# random.seed(30)
# images = [
#     f"{str(i).zfill(3)}_image.{random.choice(['png', 'jpg'])}"
#     for i in range(1, 20)
# ]
# Next, a directory called images was created:

# base_dir = 'images'
 
# if not os.path.exists(base_dir):
#     os.mkdir(base_dir)

# Then two directories were also created in this directory named images_png and images_jpg. Assign file names to appropriate directories:
# files with the extension .png to the images_png directory
# files with the extension .jpg to the images_jpg directory
# and create empty files with the given names.

# In response, execute the following code:
# for root, dirs, files in os.walk(base_dir):
#     print(root)
#     for file in sorted(files):
#         print(f'\t{file}')

# Expected result:

# images
# images/images_jpg
# 	001_image.jpg
# 	004_image.jpg
# 	006_image.jpg
# 	007_image.jpg
# 	010_image.jpg
# 	016_image.jpg
# 	017_image.jpg
# 	019_image.jpg
# images/images_png
# 	002_image.png
# 	003_image.png
# 	005_image.png
# 	008_image.png
# 	009_image.png
# 	011_image.png
# 	012_image.png
# 	013_image.png
# 	014_image.png
# 	015_image.png
# 	018_image.png
# ---------------------------------------------------------

import os
import random
 
 
random.seed(30)
images = [
    f"{str(i).zfill(3)}_image.{random.choice(['png', 'jpg'])}"
    for i in range(1, 20)
]
 
base_dir = 'images'
 
if not os.path.exists(base_dir):
    os.mkdir(base_dir)
 
png_dir = os.path.join(base_dir, 'images_png')
jpg_dir = os.path.join(base_dir, 'images_jpg')
 
if not os.path.exists(png_dir):
    os.mkdir(png_dir)
 
if not os.path.exists(jpg_dir):
    os.mkdir(jpg_dir)
 
for image in images:
    if image.endswith('.png'):
        open(os.path.join(png_dir, image), 'w').close()
    elif image.endswith('.jpg'):
        open(os.path.join(jpg_dir, image), 'w').close()
 
for root, dirs, files in os.walk(base_dir):
    print(root)
    for file in sorted(files):
        print(f'\t{file}')