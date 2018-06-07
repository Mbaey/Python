#导入cv模块
import cv2 as cv
#读取图像，支持 bmp、jpg、png、tiff 等常用格式
img = cv.imread("black.png")
#创建窗口并显示图像
cv.namedWindow("Image")
cv.imshow("Image",img)
for i in range(20):
    for j in range(20):
        print("RGB:  ",img[i,j,0])
        print("RGB:  ",img[i,j,1])
        print("RGB:  ",img[i,j,2])
print("Shape:  ",img.shape)

cv.waitKey(0)
#释放窗口
cv.destroyAllWindows()