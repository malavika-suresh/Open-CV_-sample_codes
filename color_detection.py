import cv2
import numpy as np

img=cv2.imread(r'merge.png')
HSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

#lower_blue=np.array([110,50,50])#blue
#upper_blue=np.array([130,256,255])#blue

#lower_blue=np.array([0,120,70])#red
#upper_blue=np.array([10,255,255])#red

lower_green=np.array([25,52,72])#green
upper_green=np.array([102,255,255])#green



mask=cv2.inRange(HSV,lower_green,upper_green)

cv2.imshow("Color Detection",mask)
cv2.waitKey(0)
cv2.desroyAllWindows()
