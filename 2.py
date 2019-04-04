import cv2

# http://ex2tron.wang/opencv-python-basic-element-image/
# 加载灰度图
'''
cv2.IMREAD_COLOR：彩色图，默认值(1)
cv2.IMREAD_GRAYSCALE：灰度图(0)
cv2.IMREAD_UNCHANGED：包含透明通道的彩色图(-1)
'''
img = cv2.imread('1.jpg',0)
cv2.namedWindow('1', cv2.WINDOW_NORMAL)
# 使用cv2.imshow()显示图片，窗口会自适应图片的大小：
cv2.imshow('1', img)
cv2.waitKey(0)
cv2.imwrite('save1.jpg', img)