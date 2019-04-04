import cv2
img = cv2.imread('1.jpg')
cv2.imshow('1',img)
px = img[100,99]  #  img[y,x]
px1 = img[100,99,0]  # B
px2 = img[100,99,1]  # G
px3 = img[100,99,2]  # R
img[100,90] = [255,255,255]  # 修改像素点
print(px)
print(px1)
print(px2)
print(px3)
print(img.shape)
print(img.dtype)
print(img.size)
face = img[100:200,100:200]
cv2.imshow('face',face)
b = img[:, :, 1]
cv2.imshow('blue',b)
cv2.waitKey(0)  