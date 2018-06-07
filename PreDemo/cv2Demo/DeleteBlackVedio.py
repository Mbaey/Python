import numpy as np
import cv2
import os
#参考文档： http://blog.csdn.net/sunny2038
def vedioIsBlack(vedio_name):
    cap = cv2.VideoCapture(vedio_name)
    # cap = cv2.VideoCapture('H5_DV_19700101-005156.mp4')
    # cap = cv2.VideoCapture('H5_DV_19700102-073504.mp4')#黑的
    isBlack = True
    cnt = 0
    if (cap.isOpened()):
        ret, frame = cap.read()
        # if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # cv2.imshow('image', gray)
        for i in range(100):
            for j in range(100):
                # print(gray[i,j],  end='')test
                if(gray[i,j] != 0):
                    # isBlack = False
                    cnt+=1
                    # print("Flase")
            # print()test
        # print(gray.shape) test
        if(cnt > 100):
            isBlack = False
        k = cv2.waitKey(20)
        # if (k & 0xff == ord('q')):
        #     break
        # else:
        #     break

    cap.release()
    cv2.destroyAllWindows()
    return isBlack

if __name__=="__main__":
    dirs = os.listdir(os.getcwd())
    for file in dirs:
        if(file[-3:] == 'mp4'):
            if(vedioIsBlack(file)):
                os.remove(file)
                print('delete')

    print("Hello")

    # file = 'H5_DV_19700102-040505.mp4'
    # if(vedioIsBlack(file)):
    #     print("YEs")

