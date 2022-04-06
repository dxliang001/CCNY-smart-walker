import cv2
from realsense_camera import *
#from mask_rcnn import *
from smbus import SMBus
import time
import sys

addr = 0x8                                 # slave name
bus = SMBus(1)
reg_write_dac = 0xff                       # buffer name
Intensity = 0
Interval = 0
nBlink = 0
SendData = [nBlink, Interval,Intensity]    # buffer


def sendData(nblink, interval, intensity):                    #function to send data
    SendData = [nblink, interval,intensity]                   #Put needed parameters into a buffer
    bus.write_i2c_block_data(addr, reg_write_dac, SendData)   # send the buffer thru i2c block to arduino


x = 640
y = 360
once = 0
rs = RealsenseCamera()
smallestDist = sys.maxsize
dist = 0

while True:
    #get frames from realsense camera
    ret, bgr_frame, depth_frame, depth_colormap = rs.get_frame_stream()
    
    for i in range(y):
        for j in range(x):
            dist = depth_frame[i, j]
            #(f"Dist = {dist}")
            if(dist < smallestDist and dist >= 300):
                smallestDist = dist
    
    print(f"Smallest Distance = {smallestDist}")
    if(smallestDist >= 300 and smallestDist <= 350):
        if once != 1:
            sendData(5, 3000, 255)
            once = 1
    elif (smallestDist > 350 and smallestDist <= 400):
        if once != 2:
            sendData(3, 3000, 150)
            once = 2
    elif (smallestDist > 400 and smallestDist <= 450):
        if once != 3:
            sendData(1, 3000, 100)
            once = 3
    elif(smallestDist > 450):
        if once != 4:
            sendData(0, 0, 0)
            once = 4
            
    cv2.imshow("RGB Camera", bgr_frame)
    cv2.imshow("depth frame", depth_colormap)
    
    smallestDist = sys.maxsize
    
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q') or key == 27:
        sendData(0, 0, 0)
        break

rs.release()
cv2.destroyAllWindows()
