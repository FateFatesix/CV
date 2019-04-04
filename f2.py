import cv2
import matplotlib.pyplot as plt
# http://ex2tron.wang/opencv-python-basic-element-image/
# 加载灰度图
'''
cv2.IMREAD_COLOR：彩色图，默认值(1)
cv2.IMREAD_GRAYSCALE：灰度图(0)
cv2.IMREAD_UNCHANGED：包含透明通道的彩色图(-1)
'''
img = cv2.imread('1.jpg',0)
plt.imshow(img, cmap='gray')
plt.show()

# OpenCV中的图像是以BGR的通道顺序存储的，但Matplotlib是以RGB模式显示的，所以直接在Matplotlib中显示OpenCV图像会出现问题，因此需要转换一下:
img2 = cv2.imread('1.jpg')
img22 = img2[:, :, ::-1]
plt.xticks([])
plt.yticks([])
plt.imshow(img22)
plt.show()
