#https://www.learnopencv.com/invisibility-cloak-using-color-detection-and-segmentation-with-opencv/
# https://www.geeksforgeeks.org/detection-specific-colorblue-using-opencv-python/

# Python program for Detection of a  
# specific color(blue here) using OpenCV with Python 
import sys
import argparse
import cv2 
import numpy as np  
import time
import imageio

  
cap = cv2.VideoCapture('trim.mp4')  
fps = cap.get(cv2.CAP_PROP_FPS)

hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
sensitivity = 60;
lower_green = np.array([60 - sensitivity, 100, 100]) 
upper_green = np.array([60 + sensitivity, 255, 255])


def extractImages(pathIn, pathOut):
    count = 0
    cap = cv2.VideoCapture(pathIn)
    success,image = cap.read()
    success = True
    while success:
      cap.set(cv2.CAP_PROP_POS_MSEC,(count*1000))    # 60 fps, 16.6
      success,image = cap.read()
      print ('Read a new frame: ', success)
      cv2.imwrite( pathOut + "frame%d.jpg" % count, image)     # save frame as JPEG file
      count = count + 1

# coor = np.zeroes()
count = 0
while(1):        
    # Captures the live stream frame-by-frame 
    _, frame = cap.read()  
    #frame = cap.read()
    #print(color)
    # Converts images from BGR to HSV 
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
    #lower_green = np.array([91, 96.3, 94.1]) # darker green
    #upper_green = np.array([180, 0.4, 100])  # white green

    mask = cv2.inRange(hsv, lower_green, upper_green) 
    res = cv2.bitwise_and(frame,frame, mask= mask) # merges images to find mask
    
    # resize the image to reduce processing time
    modified_frame = cv2.resize(frame, (600, 400), interpolation = cv2.INTER_AREA)
    modified_frame = modified_frame.reshape(modified_frame.shape[0]*modified_frame.shape[1], 3)


    color = frame[150, 150]
    if (color[0] == 105, color[1] == 255, color[2] == 63):
        cv2.imwrite( "images/" + "frame%d.jpg" % count, frame)
    count += 1
    print(mask)
    cv2.imshow('frame', frame)
    cv2.imshow('mask',mask) 
    cv2.imshow('res', mask)

    k = cv2.waitKey(0)
    if(k == 27):
        break
    #cv2.imshow('res',res) 
    #if 
    #extractImages("trim.mp4", "images/")


  
# Here we are defining range of green color in HSV 
# This creates a mask of green coloured  
# objects found in the frame. 


# The bitwise and of the frame and mask is done so  
# that only the green coloured objects are highlighted  
# and stored in res 

#res = cv2.bitwise_and(frame,frame, mask= mask) # merges images to find mask
#cv2.imshow('frame',frame) # supposedly prints the frames
#cv2.imshow('mask',mask) 
#cv2.imshow('res',res) 
  
#k = cv2.waitKey(5) & 0xFF
  
# Destroys all of the HighGUI windows. 
cv2.destroyAllWindows() 
  
# release the captured frame 
cap.release() 