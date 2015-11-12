#!/bin/python
# -*- coding: iso-8859-15 -*-
# Author: Johanna Schwehn 2015

# Test 1, Harvest GPS Tracks

# modules sys for reading program options and urllib2 for opening url
import sys, urllib2
#first argument http://koenigstuhl.geog.uni-heidelberg.de/~bhoefle/geoscripting/GPS_track_HD_Bodensee.csv
webURL = sys.argv[1]
# name for KML ASCII file, example: earth.kml
outputFileName = sys.argv[2]
start = 1001 #start here including /skip the first 1000 coordinates

# catch an error, if url is wrong
try:
  req = urllib2.Request(webURL)
  webpage = urllib2.urlopen(req)
except StandardError, err:
  print "An error occured: ", err
  sys.exit() #exit program

# read content of url (coordinates) and close webpage after
content = webpage.readlines()
webpage.close()

# header and footer for kml

headerKML = """<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
<Placemark>
<name>GPS track</name>
<MultiGeometry>
<LineString>
<coordinates>\n"""

footerKML = """</coordinates>
</LineString>
</MultiGeometry>
</Placemark>
</kml>"""

#function to format the coordinates in the new order
def formatCoordinates(contentLine):
  outputF = content[contentLine]
  parts = outputF.split(",") #split line into three parts

  latitude = parts[0]
  longitude = parts[1]
  elevation = parts[2][:-4] #remove \r\n

  newOutput = longitude + "," + latitude + "," + elevation #new output in changed order
  return newOutput



#create file
fileObj = file(outputFileName, "w")
fileObj.write(headerKML) #starts with headerKML

#all lines from start to end of file
for x in range(start - 1, len(content)):
  addLine = formatCoordinates(x) #input: coordinates from start (1001) to the end of file
  fileObj.write(addLine + "\n")  #splits the coordinates

fileObj.write(footerKML) #ends with footerKML

fileObj.close() #close file when finished writing
