import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread(r'colorball.jpg')
img1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

blur=cv2.blur(img1,(3,3))

circles=cv2.HoughCircles(blur,cv2.HOUGH_GRADIENT,1,45,param1=50,param2=30,minRadius=1,maxRadius=40)
circles1=np.uint16(np.around(circles))
for i in circles1[0,:]:
	cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
cv2.imshow('detected-circles',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
