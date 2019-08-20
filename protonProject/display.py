import cv2
import sys

sys.path.append('/usr/local/lib/python2.7/site-packages')

image = cv2.imread(sys.argv[1])
cv2.imshow ("Image", image)
cv2.waitKey(0)

