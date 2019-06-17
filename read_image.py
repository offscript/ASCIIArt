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
    return im

def readImage(im):
    #create a two dimensional array with first dimesion width, second dimension height
    im_array = []
    #print("value: " + str(x) + "y: value" + str(y))
    for y in range(im.height):
        for x in range(im.width) :
            #print("x value: " + str(x) + "y: value" + str(y))
            im_array.append(im.getpixel((x, y)))
    #print(im_array)
    return im_array

def convertTuple(im_array):
    brightness_array = []
    for x in range (len(im_array)):
        #print(x)
        brightness_array.append(getAverageBrightness(im_array[x]))
    return brightness_array

def getAverageBrightness(tuple_array):
    return (tuple_array[0] + tuple_array[1] + tuple_array[2]) / 3


def go():
    im = importImage()
    im_array = readImage(im)
    brightness_array = convertTuple(im_array)

go()
