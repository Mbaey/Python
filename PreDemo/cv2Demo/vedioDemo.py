import numpy as np
import cv2

cap = cv2.VideoCapture('H5_DV_19700102-073504.mp4')

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('image', gray)
        k = cv2.waitKey(20)
        if (k & 0xff == ord('q')):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()  