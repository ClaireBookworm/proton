# dislay an image

import cv2
import numpy as np
import sys

sys.path.append('/usr/local/lib/python2.7/site-packages')

image = cv2.imread(sys.argv[1])
cv2.imshow ("test.png", image)
cv2.waitKey(0)

