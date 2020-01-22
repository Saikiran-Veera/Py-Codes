#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 11:08:41 2020

@author: ubuntu
"""


from PIL import Image
import cv2
import numpy as np 

black = (0,0,0)
white = (255,255,255)
threshold = (160,160,160)

# Open input image in grayscale mode and get its pixels.
img = Image.open("sign1.jpeg").convert("LA")
# newsize=(600,200)
newsize=(821,130)
img=img.resize(newsize)
pixels = img.getdata()

newPixels = []
# Compare each pixel 
for pixel in pixels:
    if pixel < threshold:
        newPixels.append(black)
    else:
        newPixels.append(white)

# Create and save new image.
newImg = Image.new("RGB",img.size)
newImg.putdata(newPixels)
image = np.array(newImg)
ret,thresh1 = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
sharpen = cv2.filter2D(image, -1, sharpen_kernel)
result = cv2.fastNlMeansDenoisingColored(thresh1,None,20,10,7,21)
cv2.imwrite('result.jpg', result)














