from __future__ import print_function
from PIL import Image


char_Matrix = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
global width
global height

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
    im = im.resize((150,100))
    width = im.width
    print(width)
    height = im.height
    print(im.format, im.size, im.mode)
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
        brightness_array.append(getAverageBrightness(im_array[x]))
        #print(brightness_array[x])
    return brightness_array

def getAverageBrightness(tuple_array):
    average = ((tuple_array[0] + tuple_array[1] + tuple_array[2])) / 3
    return average

def createASCIIArray(brightness_array):
    ASCII_array = []
    for x in range (len(brightness_array)):
        ASCII_array.append(getASCIIEquivalent(brightness_array[x]))
    return ASCII_array

def getASCIIEquivalent(num):
    ratio = num/255
    #print(ratio)
    mapped_num = ratio * len(char_Matrix) - 1 #This number is going to be used as an index in an array. We can't accept values of len(char_Matrix), we'd get an index out of bounds error
    #print(mapped_num)
    rounded_mapped_num = round(mapped_num) 
    #print(rounded_mapped_num)
    #print(char_Matrix[rounded_mapped_num])
    return char_Matrix[rounded_mapped_num]

# You’re displaying each pixel in your image using a character in your terminal. 
# And whilst pixels are square, your terminal characters are rectangles, 
# roughly three times as tall as they are wide. This will make your image appear squashed and narrow. 
# The simplest way to fix this is to print each character in each row of your ASCII matrix three times, to stretch the image back out. 
# For example, the list ['$', 'A', '#'] would be printed out as $$$AAA###. This function, make square, prints each character in the ASCII array thrice|#
def printSquare(ASCII_array):
    for x in range (len(ASCII_array)):
        if (x % 150 == 0):
            print(ASCII_array[x] * 3)
        else:
            print(ASCII_array[x] * 3, end="")

def go():
    im = importImage()
    im_array = readImage(im)
    brightness_array = convertTuple(im_array)
    ASCII_array = createASCIIArray(brightness_array)
    printSquare(ASCII_array)
go()
