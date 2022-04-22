import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread(r'rose1.jpg')

img1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh1=cv2.threshold(img1,127,255,cv2.THRESH_BINARY)

ret,thresh2=cv2.threshold(img1,127,255,cv2.THRESH_BINARY_INV)

ret,thresh3=cv2.threshold(img1,127,255,cv2.THRESH_TRUNC)

ret,thresh4=cv2.threshold(img1,127,255,cv2.THRESH_TOZERO)

ret,thresh5=cv2.threshold(img1,127,255,cv2.THRESH_TOZERO_INV)

title=['orginal-img','Binary','Binary-inv','Trunc','Tozero','TozeroInv']
images=['img','thresh1','thresh2','thresh3','thresh4','thresh5']
for i in range(6):
	plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
	plt.title(title[i])
	plt.xticks([]),plt.yticks([])

#cv2.waitKey(0)
#cv2.destroyAllWindows()
plt.show()
