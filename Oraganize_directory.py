import os
import shutil

current_dir = os.path.dirname(os.path.realpath(__file__))

for filename in os.listdir(current_dir):

    #organize images into images folder
    if filename.endswith((".png","jpg","jpeg")):
        if not os.path.exists("Images"):
            os.mkdir("Images")
        shutil.copy(filename, "Images")
        os.remove(filename)
