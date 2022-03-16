import sys
import cv2
import numpy as np
import time
import imutils
from matplotlib import pyplot as plt
import os

# Functions
import HSV_filter as hsv
import shape_recognition as shape
import triangulation as tri
import calibration as calib

name = ["vibrate1.h", "vibrate2.h", "vibrate3.h", "stopVibrate.h"]

def vibrate(i):
        pid = os.fork() #fork a child
        if pid < 0: #error
            print("Error forking a child process\n")
            sys.exit(); #exit program
        elif pid == 0: #child process
            print("In child process\n")
            scriptName = name[i]
            os.execlp("bash", "bash", scriptName) #run bash to execute script
        os.waitpid(pid, 0) #wait for child to finish


def show():
    cv2.imshow("frame right", frame_right) 
    cv2.imshow("frame left", frame_left)
    cv2.imshow("mask right", mask_right) 
    cv2.imshow("mask left", mask_left)

# Open both cameras
cap_right = cv2.VideoCapture(6)                    
cap_left =  cv2.VideoCapture(0)

frame_rate = 120    #Camera frame rate (maximum at 120 fps)

B = 9               #Distance between the cameras [cm]
f = 6               #Camera lense's focal length [mm]
alpha = 56.6        #Camera field of view in the horisontal plane [degrees]


#Initial values
count = -1

prev = 0
current = 0
once = 0
while(True):
    count += 1

    ret_right, frame_right = cap_right.read()
    ret_left, frame_left = cap_left.read()

################## CALIBRATION #########################################################

    #frame_right, frame_left = calib.undistorted(frame_right, frame_left)

########################################################################################

    # If cannot catch any frame, break
    if ret_right==False or ret_left==False:                    
        break

    else:
        # APPLYING HSV-FILTER:
        mask_right = hsv.add_HSV_filter(frame_right, 0)
        mask_left = hsv.add_HSV_filter(frame_left, 1)

        # Result-frames after applying HSV-filter mask
        res_right = cv2.bitwise_and(frame_right, frame_right, mask=mask_right)
        res_left = cv2.bitwise_and(frame_left, frame_left, mask=mask_left) 

        # APPLYING SHAPE RECOGNITION:
        circles_right = shape.find_circles(frame_right, mask_right)
        circles_left  = shape.find_circles(frame_left, mask_left)

        # Hough Transforms can be used aswell or some neural network to do object detection


        ################## CALCULATING BALL DEPTH #########################################################

        # If no ball can be caught in one camera show text "TRACKING LOST"
        if np.all(circles_right) == None or np.all(circles_left) == None:
            cv2.putText(frame_right, "TRACKING LOST", (75,50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255),2)
            cv2.putText(frame_left, "TRACKING LOST", (75,50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255),2)

        else:
            # Function to calculate depth of object. Outputs vector of all depths in case of several balls.
            # All formulas used to find depth is in video presentaion
            depth = tri.find_depth(circles_right, circles_left, frame_right, frame_left, B, f, alpha)

            cv2.putText(frame_right, "TRACKING", (75,50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (124,252,0),2)
            cv2.putText(frame_left, "TRACKING", (75,50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (124,252,0),2)
            cv2.putText(frame_right, "Distance: " + str(round(depth,3)) + " cm", (200,50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (124,252,0),2)
            cv2.putText(frame_left, "Distance: " + str(round(depth,3)) + " cm", (200,50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (124,252,0),2)
            # Multiply computer value with 205.8 to get real-life depth in [cm]. The factor was found manually.
            #print("Depth: ", depth)

            #vibrate once every second at an intensity of 150
            if depth < 20:
                if(once == 1):
                   show()
                else:
                    show()
                    once = 1
                    vibrate(0)
            #vibrate twice every second at an intensity of 255
            elif depth > 20 and depth < 31:
                if(once == 2):
                   show()
                else:
                    show()
                    once = 2
                    vibrate(1)
            #vibrate 10 times every 100ms at an intensity of 100        
            elif depth > 30 and depth < 41:
                if(once == 3):
                   show()
                else:
                    show()
                    once = 3
                    vibrate(2)
            #stop vibration
            elif depth > 40:
                if(once == 4):
                   show()
                else:
                    show()
                    once = 4
                    vibrate(3)


        # Hit "q" to close the window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


# Release and destroy all windows before termination
cap_right.release()
cap_left.release()

cv2.destroyAllWindows()