# @Author: Alex Shelton <zoso>
# @Date:   2019-08-27T11:48:14-04:00
# @Email:  as305218@ohio.edu
# @Filename: main.py
# @Last modified by:   zoso
# @Last modified time: 2019-08-27T17:14:51-04:00


#CV uses BGR
import cv2
import numpy as np


#Loading a color image
img = cv2.imread('road.jpg')
img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# #access a pixel value by its row and column
# pixel = img[200,200]
# print(pixel)

# #collecting only blue images
# blues = img.item(100,0,0)
# print(blues)


# #Modifying pixel values
# img.itemset((255,0,0),0) #B
# img.itemset((255,0,0),0) #G
# img.itemset((255,0,0),255) #R

# Numpy is a optimized library for fast array calculations. So simply accessing each
# and every pixel values and modifying it will be very slow and it is discouraged.


# Returns tuple of number of rows columns and channels (if image has color )
print('rows, columns, and channels of colored image ',img.shape)
# print('rows, columns, and channels of greyscale image ',img_grey.shape)
# totalPixels = img.size
# print(totalPixels)




#
#    ROI
#
#

#selecting the lane to copy to another location
lane = img[1700:2000, 400:700] #from x valies: 300-600 and y values 300-500
#assigning the lane to a new location
img[800:1100, 0:300] = lane #copying the value to the images x-values 900-1100, 100-300

cv2.imwrite('edited.jpg',img)
