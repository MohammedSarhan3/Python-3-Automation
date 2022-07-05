from PIL import Image
import os
fit_size = int(input('Enter Size: '))
output_folder= input('Enter output Folder Name: ')
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

for filename in os.listdir('.'):
    
    if filename.endswith((".png","jpg","jpeg")):
        continue
    ## open image ----> get image size 