from PIL import Image
import os

# r = raw string
photo_folder_path = r"D:\Work\_PythonSuli\kezdo-230304\photos"

# check path validity
assert os.path.exists(photo_folder_path), f"A útvonal nem létezik: {photo_folder_path}"

# check if path is a folder
assert os.path.isdir(photo_folder_path), "Az útvonal könyvtár kell legyen!"


file_list = os.listdir(photo_folder_path)
for file in file_list:
    print(file)