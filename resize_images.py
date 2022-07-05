from PIL import Image
import os
fit_size = int(input('Enter Size: '))
output_folder= input('Enter output Folder Name: ')
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

for filename in os.listdir('.'):
    
    if filename.endswith((".png","jpg","jpeg")):
        continue
    ## open image ----> get image size ---> resize
    image = Image.open(filename)
    width , height = image.size
    if width > fit_size and height > fit_size:
        if width > height:
            height = int((fit_size/width)*height)
            width = fit_size
        else:
            height = int((fit_size/height)*width)
            width = fit_size
        image = image.resize((width,height))
        print('resizing : %S' %(filename))
    image = image.save(os.path.join(output_folder,filename))
    print('---------------------------------------')
print('Done Resizing All Image') 
