from PIL import Image
import os

# r = raw string
photo_folder_path = r"D:\Work\_PythonSuli\kezdo-230304\photos"

# check path validity
assert os.path.exists(photo_folder_path), f"A útvonal nem létezik: {photo_folder_path}"

# check if path is a folder
assert os.path.isdir(photo_folder_path), "Az útvonal könyvtár kell legyen!"


file_list = os.listdir(photo_folder_path)
alowed_extensions = [".jpg", ".jpeg"]

for file in file_list:
    image_full_path = os.path.join(photo_folder_path, file)
    path, ext = os.path.splitext(image_full_path)

    if not ext.lower() in alowed_extensions:
        continue
    
    img = Image.open(image_full_path)
    print(file, img.size)