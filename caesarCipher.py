# Caesar Cipher

# initial values
pathIn = 'output.txt'
pathOut = 'caesarOutput/outputCaesar_D_(NUM).txt'
alpLen = 26 # length of current used alphabet
alphCorrection = 65 # to cycle in circles letters with mod operator

# read file as string and save into char array
f = open(pathIn, encoding="utf-8")
inputArr = list(f.read())
outputArr = []

# return files for all possible letter displacements
for i in range(1, alpLen): # length of english alphabet (1 to lengthAlph-1)
    for idx in range(0, len(inputArr)):
        # store current letter as num
        charToNum = ord(inputArr[idx])
        # apply current caesar displacement to letter
        charToNum = charToNum - alphCorrection # apply ascii correction
        charToNum = (charToNum+i) % alpLen # cycle alphabet and change
        charToNum = charToNum + alphCorrection # reverse ascii correction
        # return changed char to array
        outputArr.append(chr(charToNum))
    # print to output file
    path = pathOut.replace('(NUM)',str(i))
    fOut = open(path, 'w',encoding="utf-8")
    for idx in outputArr:
      fOut.write(str(idx))
    # reset output arr
    outputArr = []

# close file objects
f.close()
fOut.close()
