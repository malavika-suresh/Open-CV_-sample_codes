import cv2
import numpy as np
img=cv2.imread('messi.png')
blur=cv2.bilateralFilter(img,9,75,75)
cv2.imshow("Blur Image",blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
