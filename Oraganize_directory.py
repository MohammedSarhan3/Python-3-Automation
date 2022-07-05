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
 #organize code files into Codes folder
    if filename.endswith((".py","css","html","js","c","cpp")):
        if not os.path.exists("Codes"):
            os.mkdir("Codes")
        shutil.copy(filename, "Codes")
        os.remove(filename)
#organize Video files into Videos folder
    if filename.endswith((".mp4")):
        if not os.path.exists("Video"):
            os.mkdir("Video")
        shutil.copy(filename, "Video")
        os.remove(filename)

 #organize Docs files into Documents folder
    if filename.endswith((".pdf",".word")):
        if not os.path.exists("Documents"):
            os.mkdir("Documents")
        shutil.copy(filename, "Documents")
        os.remove(filename)
        
#organize App files into Apps folder
    if filename.endswith((".exe",".dng")):
        if not os.path.exists("Apps"):
            os.mkdir("Apps")
        shutil.copy(filename, "Apps")
        os.remove(filename)

 #organize archive files into archive folder
    if filename.endswith((".zip",".rar","tar")):
        if not os.path.exists("archive"):
            os.mkdir("archive")
        shutil.copy(filename, "archive")
        os.remove(filename)
