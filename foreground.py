#___________foreground substraction_______________________________________________________________

import numpy as np
import cv2

cap = cv2.VideoCapture('/home/paython/Videos/4K Video Downloader/Pogba Penalty, 10 seconds walking.mp4')
ret, frame = cap.read()
average = np.float32(frame)

while True:
    ret, frame = cap.read()
    cv2.accumulateWeighted(frame,average,0.01)
    background = cv2.convertScaleAbs(average)
    cv2.imshow('Input',frame)
    cv2.imshow('Disapering Background',background)
    if cv2.waitKey(1)==13:
        break
cap.release()
cv2.destroyAllWindows()

