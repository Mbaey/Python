# import numpy as np
# import os
# import cv2 as cv
# import torch
# import torch.nn as nn
# import torchvision.transforms as transforms
# from PIL import Image

# class FaceDetector:
#     def __init__(self) -> None:
#         # 创建一个级联分类器 加载一个.xml分类器文件 它既可以是Haar特征也可以是LBP特征的分类器
#         self.face_detecter = cv.CascadeClassifier(
#             os.path.join("static/models", 'haarcascade_frontalface_default.xml'))
#             # r'./face_detection/haarcascades/haarcascade_frontalface_default.xml'")
        
#         pass
#     def face_detection(self, image):
#         # 转成灰度图像
#         gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
#         # 多个尺度空间进行人脸检测   返回检测到的人脸区域坐标信息
#         faces = self.face_detecter.detectMultiScale(image=gray, scaleFactor=1.1, minNeighbors=5)
#         print('检测人脸信息如下：\n', faces)
#         return faces

# class ClassifyerClass:
#     def __init__(self):
#         self.device = 'cpu' # torch.device("cuda" if torch.cuda.is_available() else 'cpu')
#         src_dir = os.path.dirname(os.path.abspath(__file__))
#         # print(src_dir)
#         # print(os.getcwd())
#         self.transform = transforms.Compose([
#             transforms.Resize(256),
#             transforms.CenterCrop(224),
#             transforms.ToTensor(),
#             transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),]) 
#         net =  AlexNet().to(self.device)
#         params = torch.load(os.path.join("static/models", 'alexnet.pth')
#             , map_location='cpu', encoding='latin1')
#         load_model(params, net)
#         net.eval()
        
#         self.model = net 


#     def recognize(self, data):
#         data = self.transform(data)

#         # data = data[np.newaxis, :]
#         print(data.shape)
#         result = 202  #此处应返回算法结果，数字应是201， 202 或203

#         with torch.no_grad():
#             # img = torch.from_numpy(data) 
#             img = data.unsqueeze(0).to(self.device)
#             output = self.model(img).squeeze(1) 

#         result = output.numpy()[0]
#         return result


# def load_model(pretrained_dict, new):
#     model_dict = new.state_dict()
#     # 1. filter out unnecessary keys
#     pretrained_dict = {k: v for k, v in pretrained_dict['state_dict'].items() if k in model_dict}
#     # 2. overwrite entries in the existing state dict
#     model_dict.update(pretrained_dict)
#     new.load_state_dict(model_dict)

# import torch
# import torch.nn as nn
# import math
# from collections import OrderedDict

# ################## AlexNet ##################
# def bn_relu(inplanes):
#     return nn.Sequential(nn.BatchNorm2d(inplanes), nn.ReLU(inplace=True))

# def bn_relu_pool(inplanes, kernel_size=3, stride=2):
#     return nn.Sequential(nn.BatchNorm2d(inplanes), nn.ReLU(inplace=True), nn.MaxPool2d(kernel_size=kernel_size, stride=stride))

# class AlexNet(nn.Module):
#     def __init__(self, num_classes=1):
#         super(AlexNet, self).__init__()
#         self.conv1 = nn.Conv2d(3, 96, kernel_size=11, stride=4, bias=False)
#         self.relu_pool1 = bn_relu_pool(inplanes=96)
#         self.conv2 = nn.Conv2d(96, 192, kernel_size=5, padding=2, groups=2, bias=False)
#         self.relu_pool2 = bn_relu_pool(inplanes=192)
#         self.conv3 = nn.Conv2d(192, 384, kernel_size=3, padding=1, groups=2, bias=False)
#         self.relu3 = bn_relu(inplanes=384)
#         self.conv4 = nn.Conv2d(384, 384, kernel_size=3, padding=1, groups=2, bias=False)
#         self.relu4 = bn_relu(inplanes=384)
#         self.conv5 = nn.Conv2d(384, 256, kernel_size=3, padding=1, groups=2, bias=False)
#         self.relu_pool5 = bn_relu_pool(inplanes=256)
#         # classifier
#         self.conv6 = nn.Conv2d(256, 256, kernel_size=5, groups=2, bias=False)
#         self.relu6 = bn_relu(inplanes=256)
#         self.conv7 = nn.Conv2d(256, num_classes, kernel_size=1, bias=False)

#     def forward(self, x):
#         x = self.conv1(x)
#         x = self.relu_pool1(x)
#         x = self.conv2(x)
#         x = self.relu_pool2(x)
#         x = self.conv3(x)
#         x = self.relu3(x)
#         x = self.conv4(x)
#         x = self.relu4(x)
#         x = self.conv5(x)
#         x = self.relu_pool5(x)
#         x = self.conv6(x)
#         x = self.relu6(x)
#         x = self.conv7(x)
#         x = x.view(x.size(0), -1)
#         return x
