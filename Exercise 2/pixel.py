#Copyright 2017 Jinguang Guo gaving@bu.edu
import cv2
import numpy as np

img = cv2.imread("/Users/bisma/Documents/GitHub/EC601_OpenCV/Test_images/Lenna.png")

#RGB
RGB = img[20,25]

#ycbcr
ycbcr_image = cv2.cvtColor(img,cv2.COLOR_BGR2YCR_CB)
ycbcr = ycbcr_image[20,25]
#hsv
hsv_image = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
hsv = hsv_image[20,25]

print("RGB [20,25] : " , RGB)
print("YCbCr [20,25] : " , ycbcr)
print("HSV [20,25] : " , hsv)
