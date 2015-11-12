#!/bin/python
# -*- coding: iso-8859-15 -*-
# Author: Johanna Schwehn 2015

# Test 1, Harvest GPS Tracks

# modules sys for reading program options and urllib2 for opening url
import os, sys

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

allFiles = getAllFilesByExt(dirIn, ext)

#read files and add merge into one
outFile = file(__file__ + "\\..\\" + outFileName, "w") #write merged stuff here
for currFile in allFiles:
    print "merging " + currFile + "..."
    readObj = file(dirIn + "\\" + currFile, "r") #files to read from
    content = readObj.read()
    outFile.write(content)
    readObj.close()
    print "done."
outFile.close()
print "Merged file saved as " + outFileName + " in " + __file__ + "\\..\\"
