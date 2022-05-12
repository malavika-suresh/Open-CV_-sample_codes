import cv2
import numpy as np
cap=cv2.VideoCapture(r'video.mp4')
cpt=0
while(cap.isOpened()):
      ret,frame=cap.read()
      gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
      cv2.imshow("frame",frame)
      cv2.imwrite('E:\imageprocessing/img%04i.jpg'%cpt,frame)
      cpt+=1
      if cv2.waitKey(1)&0xFF==ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
