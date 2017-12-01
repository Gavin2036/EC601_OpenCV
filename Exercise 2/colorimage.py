#Copyright 2017 Jinguang Guo gaving@bu.edu
import cv2
import numpy as np

img = cv2.imread("/Users/bisma/Documents/GitHub/EC601_OpenCV/Test_images/Lenna.png")
cv2.imwrite("/Users/bisma/Documents/GitHub/EC601_OpenCV/Exercise 2/outcomes/Original.png", img)

#RGB
b,g,r = cv2.split(img)
cv2.imwrite("/Users/bisma/Documents/GitHub/EC601_OpenCV/Exercise 2/outcomes/Blue.png",b)
cv2.imwrite("/Users/bisma/Documents/GitHub/EC601_OpenCV/Exercise 2/outcomes/Green.png",g)
cv2.imwrite("/Users/bisma/Documents/GitHub/EC601_OpenCV/Exercise 2/outcomes/Red.png",r)

#ycbcr
ycbcr_image = cv2.cvtColor(img,cv2.COLOR_BGR2YCR_CB)
y,cb,cr = cv2.split(ycbcr_image)
cv2.imwrite("/Users/bisma/Documents/GitHub/EC601_OpenCV/Exercise 2/outcomes/y.png",y)
cv2.imwrite("/Users/bisma/Documents/GitHub/EC601_OpenCV/Exercise 2/outcomes/cb.png",cb)
cv2.imwrite("/Users/bisma/Documents/GitHub/EC601_OpenCV/Exercise 2/outcomes/cr.png",cr)

#hsv
hsv_image = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv_image)
cv2.imwrite("/Users/bisma/Documents/GitHub/EC601_OpenCV/Exercise 2/outcomes/Hue.png",h)
cv2.imwrite("/Users/bisma/Documents/GitHub/EC601_OpenCV/Exercise 2/outcomes/Saturation.png",s)
cv2.imwrite("/Users/bisma/Documents/GitHub/EC601_OpenCV/Exercise 2/outcomes/Value.png",v)