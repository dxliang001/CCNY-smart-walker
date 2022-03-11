import cv2
import numpy as np
from matplotlib import pyplot as plt

##leftimg = cv2.imread('im1.jpg',cv2.IMREAD_REDUCED_GRAYSCALE_2)

##rytimg2 = cv2.imread('im2.jpg',cv2.IMREAD_REDUCED_GRAYSCALE_2)  
##rytimg2=cv2.resize(rytimg2,leftimg.shape)

##########################################################
left = cv2.VideoCapture(0,cv2.CAP_DSHOW)
right = cv2.VideoCapture(2,cv2.CAP_DSHOW)

while(True):
    if not (left.grab() and right.grab()):
        print("No more frames")
        break

    _, leftFrame = left.retrieve()
    _, rightFrame = right.retrieve()
    grayL = cv2.cvtColor(leftFrame, cv2.COLOR_BGR2GRAY)
    grayR = cv2.cvtColor(rightFrame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('left', grayL)
    cv2.imshow('right', grayR)
    stereo = cv2.StereoBM_create(numDisparities=0,blockSize=21)
    depth = stereo.compute(grayL,grayR)
    disparity = depth.astype(np.float32)
    map = depth.astype(np.matrix)
    cv2.imshow("disp",disparity)
    

    matrix =plt.imshow(depth)
    rows =480
    columns= 640
    #for j in range(columns):
    #    for i in range(rows):
    #         if map[i][j]!= -16:
    #             print(map[i][j])
    #plt.imshow(depth)
    #plt.show()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
##stereo = cv2.StereoBM_create(numDisparities=0,blockSize=21)
##depth = stereo.compute(leftimg,rytimg2)

##cv2.imshow('Imagell',leftimg)
##cv2.imshow('Imagerr',rytimg2)
left.release()
right.release()
cv2.destroyAllWindows()
#plt.imshow(depth)
#plt.axis('off')
#plt.show()  