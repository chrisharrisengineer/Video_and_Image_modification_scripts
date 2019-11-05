from PIL import Image
import os.path, sys

path = "frames"
#path = os.getcwd()
dirs = os.listdir(path)

def crop():
    for item in dirs:
        fullpath = os.path.join(path,item)
        if os.path.isfile(fullpath):
            im = Image.open(fullpath)
            f, e = os.path.splitext(path+item)
            #top
            #imCrop = im.crop((400, 680, 3500, 1300))
            #bottom
            imCrop = im.crop((400, 1780, 3750, 2400))
            imCrop.save(f + 'Cropped', "BMP", quality=100)

crop()
