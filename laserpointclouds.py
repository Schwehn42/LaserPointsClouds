#!/bin/python
# -*- coding: iso-8859-15 -*-
# Author: Johanna Schwehn 2015

# Test 1, Harvest GPS Tracks

# modules sys for reading program options and urllib2 for opening url
import os, sys

dirIn = sys.argv[1]
dirOut = sys.argv[2]

def getAllFilesByExt(directory, fileext):
    retFiles = []
    for subdir, dirs, files in os.walk(dirIn):
        for file in files:
            print file
            if file.endswith(fileext):
                retFiles.append(file)
    return retFiles

allFiles = getAllFilesByExt(dirIn, ".asc")
