# implement caesar cipher algorithm

# imports
from tkinter import filedialog as fd
from PIL import Image

# output file
outputCaesar = 'output.txt'

# File dialog to extract file
# filename = fd.askopenfilename()

# function to process byte and return corresponding ascii
def byteToAscii(arrOfByte):
    toReturn = None
    binStr = ''
    # turn pixels to bit string of possible letter
    for i in arrOfByte :
        if (i % 2 == 0):
            binStr += '0'
        else:
            binStr += '1'
    # turn bit string into corresponding ascii, and return
    symbol = int(binStr, 2)
    # filter only valid letters
    if (symbol >= 97 and symbol <= 122) or (symbol >= 65 and symbol <= 90):
        toReturn = chr(symbol)
    return toReturn



# Open image
img = input("Enter image name(with extension) : ")
# set iterator in image
image = Image.open(img, 'r')
data = ''
imgdata = iter(image.getdata())
# get img size in bytes
image_copy = Image.open(img)
sizeImg = len(image_copy.fp.read())
print('sizeImg', sizeImg)

# iter byte colors and print to file
f = open(outputCaesar, 'w',encoding="utf-8")

# list of all bytes in img
byteList = []
for i in range(0,sizeImg):
    # f.write(f'\nbyte {i}')
    # f.write(str(imgdata.__next__()))
    try:
        byteList.extend(list(imgdata.__next__()))
    except StopIteration:
        # if StopIteration is raised, break from loop
        break

# turn bytes to letters
count = 1
asciiArr = [] # final array to store letters
currByte = [] # temporal array to process each 8 bytes
for i in range(1,len(byteList)+1):
    currByte.append(byteList[i-1])
    if(i%8==0):
        # turn pixels to bit string of possible letter
        asciiSymb = ''
        byteToAsc = byteToAscii(currByte)
        if byteToAsc: 
            asciiSymb += byteToAsc
        # print('byteToAscii(currByte)', byteToAscii(currByte))
        
        # turn bit string into corresponding ascii
        if asciiSymb:
            asciiArr.append(asciiSymb.upper())
        # reset temporal array and string
        currByte = []

# to add last bytes, if the number of bytes are not multiple of 8
if currByte:
    byteToAsc = byteToAscii(currByte)
    if byteToAsc:
        asciiSymb += byteToAsc
    if asciiSymb:
            asciiArr.append(asciiSymb.upper())


# iter array of ascii and print to file
# print(asciiArr)
count = 1
for symb in asciiArr:
    f.write(str(symb)) # +'  ')
    # if count % 30 == 0:
        # f.write('\n')
    count += 1
f.close()