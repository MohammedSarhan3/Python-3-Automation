import os
from PIL import Image
## ADD logo , new folder 
LOGO_NAME = input('Enter The Logo Nmae With Extension: ')
NEW_FOLDER_NAME =input('Enter the new folder name: ')


## ADD logo information
logo_image =Image.open( LOGO_NAME)
logo_width , logo_heigh = logo_image.size
