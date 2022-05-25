import cv2
import numpy as np

img=cv2.imread(r'rose.jpg')

img1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cpt=0
for thresh in range(0,255):
	imbw=cv2.threshold(img1,thresh,255,cv2.THRESH_BINARY)
cv2.imwrite(r'img%04i.jpg'%cpt,imbw)
cpt+=1
print("successfully completed")


cv2.waitKey(0)
cv2.destroyAllWindows()
