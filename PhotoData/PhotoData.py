from PIL import Image, ExifTags
import os, json

# r = raw string
photo_folder_path = r"D:\Work\_PythonSuli\kezdo-230304\photos"

# check path validity
assert os.path.exists(photo_folder_path), f"A útvonal nem létezik: {photo_folder_path}"

# check if path is a folder
assert os.path.isdir(photo_folder_path), "Az útvonal könyvtár kell legyen!"

# list photo_folder_path and get all content
file_list = os.listdir(photo_folder_path)

# these are the file extensions we want to care about
alowed_extensions = [".jpg", ".jpeg"]

# create an empty list for store data
photo_data_container = {}

# iterate on the file_list
for file in file_list:
    # create the full path to the file
    image_full_path = os.path.join(photo_folder_path, file)

    # get the file extension. unpacking
    path, ext = os.path.splitext(image_full_path)

    if not ext.lower() in alowed_extensions:
        continue
    
    img = Image.open(image_full_path)

    exif_data = img._getexif()
    if not exif_data:
        continue

    photo_data_container[file] = {
        "size": img.size,
        "camera": exif_data.get(0x0110),
        "creation_date": exif_data.get(0x9003),
        "iso": exif_data.get(0x8827)
    }

with open("photo_data.json", "w") as my_file:
    json.dump(photo_data_container, my_file)


"""
# save photo_data_container into a txt file
with open("photo_data.txt", "w") as my_file:
    my_file.write(str(photo_data_container))

# read photo_data.txt

with open("photo_data.txt") as my_file:
    print(my_file.read())
"""