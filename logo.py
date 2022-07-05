import os
from PIL import Image
## ADD logo , new folder 
LOGO_NAME = input('Enter The Logo Nmae With Extension: ')
NEW_FOLDER_NAME =input('Enter the new folder name: ')


## ADD logo information
logo_image =Image.open( LOGO_NAME)
logo_width , logo_heigh = logo_image.size


##creat folder
os.mkdir(NEW_FOLDER_NAME)

## ADD loop over images
for filename in os.listdir('.'):
    ##check in file image & not logo
    if not (filename.endswith('.png') or filename.endswith('.jpj') or filename == LOGO_NAME):
        continue
    img= Image.open(filename)
    width , height = img.size

##add logo to the image
    img.paste(logo_image ,(width-logo_width , height-logo_heigh ))

    ## save image 
    img.save(os.path.join(NEW_FOLDER_NAME, filename))
print("DONE")
