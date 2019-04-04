import cv2

# http://ex2tron.wang/opencv-python-open-camera/

# 打开摄像头并灰度化显示
capture = cv2.VideoCapture(0)
# 获取捕获的分辨率
# propId可以直接写数字，也可以用OpenCV的符号表示
width, height = capture.get(3), capture.get(4)
print(width, height)
# 以原分辨率的一倍来捕获
# capture.set(cv2.CAP_PROP_FRAME_WIDTH, width * 2)
# capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height * 2)

while(True):
    # 获取一帧
    ret, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',gray)
    if cv2.waitKey(1) == ord('q'):
        break

# 录制视频

capture2 = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc()
outfile = cv2.VideoWriter('output.avi', fourcc, 25., (640, 480))
while(capture2.isOpened()):
    ret, frame = capture.read()
    if ret:
        outfile.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break


# # 播放本地视频
# capture3 = cv2.VideoCapture('demo_video.mp4')

# while(capture3.isOpened()):
#     ret, frame = capture3.read
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     cv2.show('frame', gray)
#     if cv2.waitKey(1) == ord('q'):
#         break
