
import cv2
import numpy as np
from matplotlib import pyplot as plt

left = cv2.VideoCapture(0,cv2.CAP_DSHOW)
#right = cv2.VideoCapture(3,cv2.CAP_DSHOW)
while(True):
   ret,img = left.read()
   if ret == true:
      cv2.imshow('video output',img)
      k=cv2.waitKey(10)& 0xFF
      if k==113:
          break
      else:
         break
left.release()
cv2.destroyAllWindows()
      

  
