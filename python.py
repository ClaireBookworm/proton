# Proton Project for video green color detection -- Claire
import sys
import argparse
import cv2 
import numpy as np  
import time
import imageio
from PIL import Image

# ENTER FILE NAME
cap = cv2.VideoCapture('trim.mp4')  
# calculates frame rate -- more accurate
fps = cap.get(cv2.CAP_PROP_FPS) 

print('Youre camera\'s FPS is: ' + str(fps))
# should be 16.6 milliseconds / frame because it's 60 fps
# frame_gap: time between each frame
frame_gap = (1/fps) * 1000 
fInterval = 5 

def millTime (count, fps):
    # takes in count and converts to seconds
    return round(count*(1/fps), 2)

def inRange(main, lower, upper):
    c = 0
    for num in range(0, 3):
        if int(main[num]) <= int(upper[num]) and int (main[num]) >= int(lower[num]):
            c += 1
    return c >= 3

#hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# GREEN COLOR DEFINITION
lower_green = [100, 200, 100]
upper_green = [255, 255, 255]

success = True
def extract (results, fps, limit):
    count = 0 
    # count is the # of frames we go through, when interval not 1, be careful!
    while count < limit:
        #cap.set(cv2.CAP_PROP_POS_MSEC,(count*16.6))    # 60 fps, 16.6
        cap.set(cv2.CAP_PROP_POS_MSEC,(count*frame_gap))
        success,image = cap.read()
        
        green = image[10, 10]
        # print(green)
        if inRange(green, lower_green, upper_green):
            print ('Read frame %d: ' % count,success) # useless but helpful
            time = millTime(count, 60)
            print ("Time: %f" % time)
            results.append(time)
            # cv2.imwrite("images/" + "frame%d.jpg" % count, image) 
        print ("Num: " + str(count))
        print("TIMESTAMPS")
        print(results)
        count = count + fInterval
    return count

results = []

def calc_limit (vid_length, fps):
    return (vid_length * fps) # vid_length in seconds


# CALC_LIMIT (video length in seconds, fps) -- fps stays as fps
limit = calc_limit (60, fps)

# EXTRACT(results array name, fps, limit) -- limit from above
extract (results, fps, limit)
