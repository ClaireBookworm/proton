# https://www.geeksforgeeks.org/detection-specific-colorblue-using-opencv-python/

# Python program for Detection of a  
# specific color(blue here) using OpenCV with Python 
import sys
import argparse
import cv2 
import numpy as np  
import time
import imageio
from PIL import Image

  
cap = cv2.VideoCapture('trim.mp4')  
fps = cap.get(cv2.CAP_PROP_FPS)

count = 0

def millTime (ms, fps):
    return (ms/fps) * 100

def inRange(main, lower, upper):
    c = 0
    for num in range(0, 3):
        print("main: " + str(main[num]) + " upper: " + str(upper[num]) + " lower: " + str(lower[num]) + ".")
        if int(main[num]) <= int(upper[num]) and int (main[num]) >= int(lower[num]):
            c += 1
    return c >= 3
# 116 125 124

#hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
sensitivity = 60;
#lower_green = np.array([60 - sensitivity, 100, 100]) 
#upper_green = np.array([60 + sensitivity, 255, 255])
#lower_green = np.array([48, 138, 66]) 

#lower_green = np.array([100, 200, 100]) 
#upper_green = np.array([255, 255, 255])

lower_green = [100, 200, 100]
upper_green = [255, 255, 255]

success = True
# while success:
while success:
    cap.set(cv2.CAP_PROP_POS_MSEC,(count*16.6))    # 60 fps, 16.6
    success,image = cap.read()
    #im = Image.fromarray(image) # Can be many different formats.
    #pix = im.load()
    #green = pix[125, 125]
    
    #im = Image.fromarray(image)
    #green = list(image.getdata)
    #im = Image.fromarray(image.astype('uint8'), 'RGB')
    #green = im.getpixel((3, 3))
    green = image[10, 10]
    print(green)
    if inRange(green, lower_green, upper_green):
        print ('Read a new frame%d: ' % count,success)
        print ("Time: %f" % ((count/16.6)*100))
        cv2.imwrite("images/" + "frame%d.jpg" % count, image) 
    print ("Num: " + str(count))
    count = count + 1

# coor = np.zeroes()
  
#k = cv2.waitKey(5) & 0xFF
  
# Destroys all of the HighGUI windows. 
#cv2.destroyAllWindows() 
  
# release the captured frame 
cap.release() 