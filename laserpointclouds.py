#!/bin/python
# -*- coding: iso-8859-15 -*-
# Author: Johanna Schwehn 2015

# Test 1, Harvest GPS Tracks

# modules sys for reading program options and urllib2 for opening url
import os, sys
import time
startTime = time.time()

dirIn = sys.argv[1]
outFileName = sys.argv[2]
ext = ".asc"

def getAllFilesByExt(directory, fileext):
    retFiles = []
    for subdir, dirs, files in os.walk(dirIn):
        for file in files:
            if file.endswith(fileext):
                retFiles.append(file)
    return retFiles

def changeColor(changeFile, r, g, b):
    readObj = file(dirIn + "\\" + currFile, "r") #read the file to change
    content = readObj.read()
    parts = content.split("\n") #split file (one string) into lines
    for i in range(len(parts)):
        parts[i] = parts[i][:26] #cut the last 3 values
        parts[i] += str(r) + " " + str(g) + " " + str(b) #add the new rgb values
    newline = "\n"

    return newline.join(parts) #rebuild the file by adding newline after each line



allFiles = getAllFilesByExt(dirIn, ext)

#read files and add merge into one
outFile = file(__file__ + "\\..\\" + outFileName, "w") #write merged stuff here
for currFile in allFiles:
    print "merging " + currFile + "..."
    readObj = file(dirIn + "\\" + currFile, "r") #files to read from
    content = readObj.read()
    if currFile == "Reflector.asc": #change color value to red for file 'Reflector.asc'
        content = changeColor(currFile, 255, 0, 0)
    outFile.write(content)
    readObj.close()
    print "done."
outFile.close()
print "Merged file saved as " + outFileName + " in " + __file__ + "\\..\\"
print "Time needed to execute: " + str(time.time() - startTime) + " seconds"
