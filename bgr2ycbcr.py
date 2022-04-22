import cv2
import numpy as np

img=cv2.imread(r'rose1.jpg')
imgysc=cv2.cvtColor(img,cv2.COLOR_BGR2YCR_CB)

cv2.imshow("YSCRimage",imgysc)

cv2.waitKey(0)
cv2.destroyAllWindows()
