import cv2

#Create a video capture object to read a video from a file
vidCap = cv2.VideoCapture('Cars.mp4')


#isOpened() is a method used to confirm the video file was
#opened successfully, returns true if opened successfully
#else returns false
#get() is a method to retrieve information associated with the
#video
#5/CAP_PROP_FPS - is the frame rate
#7/CAP_PROP_FRAME_COUNT - is the frame count
if(vidCap.isOpened() == False):
    pint("Error opening the video file")
else:
    #Get frame rate info
    fps = int(vidCap.get(5))
    print ("Frame Rate : ", fps, "frames per second")
    
    #Get Frame Count
    frameCount = vidCap.get(7)
    print("Frame Count : ", frameCount)
  
  
#Read each frame from the video
#read() functions returns a tuple where
#the first value is a boolean, the next is a 
#video frame
#When the first value returns true it means
#there is a frame to read
while(vidCap.isOpened()):
    ret, frame = vidCap.read()
    if ret == True:
        cv2.imshow('Frame', frame) #show the frame in a window
        k = cv2.waitKey(20)
        if k == 113: #113 is ascii code for q
            break
    else:
      break
            
#release objects
vidCap.release()
cv2.destroyAllWindows()


        
    
