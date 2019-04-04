import cv2
import numpy as np
import matplotlib.pyplot as plt
# http://ex2tron.wang/opencv-python-extra-trackbar/

def nothing():
    pass
img = np.zeros((300, 512, 3), np.uint8)
print(img)
cv2.namedWindow('image')

cv2.createTrackbar('R', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('B', 'image', 0, 255, nothing)

while (True):
    cv2.imshow('image', img)
    if cv2.waitKey(1) == ord('q'):
        break
    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')
    img[:] = [b,g,r]

