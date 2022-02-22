import cv2
import os

def vibrate(done):
    if done == 0:
        pid = os.fork() #fork a child
        if pid < 0: #error
            print("Error forking a child process\n")
            sys.exit(); #exit program
        elif pid == 0: #child process
            print("In child process\n")
            scriptName = "arduinoScriptVibrate.h"
            os.execlp("bash", "bash", scriptName) #run bash to execute script
        os.waitpid(pid, 0) #wait for child to finish
        done = 1

def stopVibrate():
    pid = os.fork() #fork a child
    if pid < 0: #error
        print("Error forking a child process\n")
        sys.exit(); #exitprogram
    elif pid == 0: #child process
        print("In child process\n")
        scriptName = "arduinoScriptStopVib.h"
        os.execlp("bash", "bash", scriptName)  #run bash to execute script
    os.waitpid(pid, 0) #wait for child to finish


#reading a video stream from a webcam
vidCap = cv2.VideoCapture(0)

#isOpened() is a method used to confirm the video file was
#opened successfully, returns true if opened successfully
#else returns false
#get() is a method to retrieve information associated with the
#video
#5/CAP_PROP_FPS - is the frame rate
#7/CAP_PROP_FRAME_COUNT - is the frame count
if(vidCap.isOpened() == False):
    print("Error opening the video file")
else:
    #Get frame rate info
    fps = int(vidCap.get(5))
    print ("Frame Rate : ", fps, "frames per second")
    
    #Get Frame Count
    frameCount = vidCap.get(7)
    print("Frame Count : ", frameCount)
  
#Obtain frame size
#3/CAP_PROP_FRAME_WIDTH is the frame width
#4/CAP_PROP_FRAME_HEIGHT is the frame height
frameWidth = int(vidCap.get(3))
frameHeight = int(vidCap.get(4))
frameSize = (frameWidth, frameHeight)
fps = 20

#To write/save a video file
#we need a VideoWriter object
#Syntax -VideoWriter(filename, apiPreference, fourcc, fps, frameSize[, isColor])
#filename: pathname for the output video file
#apiPreference:  API backends identifier
#fourcc: 4-character code of codec, used to compress the frames (fourcc)
#fps: Frame rate of the created video stream
#frame_size: Size of the video frames
#isColor: If not zero, the encoder will expect and encode color frames. 
#Else it will work with grayscale frames (the flag is currently supported on Windows only).
output = cv2.VideoWriter('videoTest.mp4', cv2.VideoWriter_fourcc(*'XVID'), fps, frameSize)

  
#Read each frame from the video
#read() functions returns a tuple where
#the first value is a boolean, the next is a 
#video frame
#When the first value returns true it means
#there is a frame to read
done = 0
while(vidCap.isOpened()):
    ret, frame = vidCap.read()
    if ret == True:
        #write frame to file
        output.write(frame)
        cv2.imshow('Frame', frame) #show the frame in a window
        k = cv2.waitKey(20)
        if k == 115: #115 is ascii code for s
            done = vibrate(done) #vibrate after window pops up
        if k == 113: #113 is ascii code for q
            stopVibrate()
            break
    else:
        stopVibrate()
        break
            
#release objects
vidCap.release()
cv2.destroyAllWindows()
