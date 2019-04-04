# import cv2
# img = cv2.imread('1.jpg')
# # 转换为灰度图
# flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
# print(flags)
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('img', img)
# cv2.imshow('img_gray', img_gray)
# cv2.waitKey(0)

# http://ex2tron.wang/opencv-python-changing-colorspaces/
import numpy as np
import cv2
capture = cv2.VideoCapture(0)
lower_blue = np.array([0, 110, 110])
upper_blue = np.array([130, 255, 255])
while(True):
    # 1.捕获视频中的一帧
    ret, frame = capture.read()

    # 2.从BGR转换到HSV

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 3.inRange()：介于lower/upper之间的为白色，其余黑色

    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # 4.只保留原图中的蓝色部分
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    if cv2.waitKey(1) == ord('q'):
        break