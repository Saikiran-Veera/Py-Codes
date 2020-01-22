#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 13:17:50 2019

@author: ubuntu
"""
import pytesseract
import cv2
import re

config = ('-l eng+ara --oem 1 --psm 3')
filename='in4-2'
impath=filename+'.jpg'
  # Read image from disk
im = cv2.imread(impath, cv2.IMREAD_COLOR)
  # Run tesseract OCR on image
# text = pytesseract.image_to_string(im, config=config)
osd = pytesseract.image_to_osd(im)
angle = re.search('(?<=Rotate: )\d+', osd).group(0)
#script = re.search('(?<=Script: )\d+', osd).group(0)
print("angle: ", angle)
#print("script: ", script)
# file = open(filename+'_jpg'+'.txt', 'w')
# file.write(text)
# file.close()
#   # Print recognized text
#print(text)


#1. text orientation based on median angle
#2.script implementation and testing
#3.detection of orientaion text angle using tesseract 
#4.implementation with different modes of tesseract segmentation
#5.oriented angle using tesseract OSDs
