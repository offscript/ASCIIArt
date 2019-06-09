from __future__ import print_function
from PIL import Image

def importImage():
    try: 
        im = Image.open("TheDream.jpg")
    except IOError as error:
        print(error)
        print('The image did not load successfully')
    else:
        print("The image loaded successfully")
        print(im.format, im.size, im.mode)
    finally:
        print("End of Step 1")

importImage()


