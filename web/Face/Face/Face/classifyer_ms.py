import numpy as np
import os
import cv2 as cv
import mindspore.nn as nn
from mindspore import context
from mindspore.common import dtype as mstype
import mindspore.dataset.vision.c_transforms as CV
import mindspore.dataset.transforms.c_transforms as C
from mindspore.train.serialization import load_checkpoint
import mindspore.dataset as ds

from PIL import Image
from mindspore import Model, Tensor
import threading

class FaceDetector:
    def __init__(self) -> None:
        # 创建一个级联分类器 加载一个.xml分类器文件 它既可以是Haar特征也可以是LBP特征的分类器
        self.face_detecter = cv.CascadeClassifier(
            os.path.join("static/models", 'haarcascade_frontalface_default.xml'))        

    def face_detection(self, image):
        # 转成灰度图像
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        # 多个尺度空间进行人脸检测   返回检测到的人脸区域坐标信息
        faces = self.face_detecter.detectMultiScale(image=gray, scaleFactor=1.1, minNeighbors=5)
        print('检测人脸信息如下：\n', faces)
        return faces

class ClassifyerClass:
    def __init__(self):
        self.device = 'CPU' # torch.device("cuda" if torch.cuda.is_available() else 'cpu')
        src_dir = os.path.dirname(os.path.abspath(__file__))
        # print(src_dir)
        # print(os.getcwd())
            # imagenet_state
        mean = [0.485 * 255, 0.456 * 255, 0.406 * 255]
        std = [0.229 * 255, 0.224 * 255, 0.225 * 255]

        type_cast_op = C.TypeCast(mstype.float32)  # ms.float32
        image_size = 224
        self.transform_img = [
            # CV.Decode(),
            CV.Resize((256, 256)),
            CV.CenterCrop(image_size),
            CV.Normalize(mean=mean, std=std),
            CV.HWC2CHW(),
            type_cast_op,
        ]

        # context.set_context(device_target="CPU")
        context.set_context(device_target="GPU")

        net =  AlexNet(num_classes=1)
        model_name=os.path.join("static/models", 'alexnet_best.ckpt')
        load_checkpoint(model_name, net=net)
        loss = nn.loss.MSELoss()
        self.model = Model(net, loss_fn=loss)

    def recognize(self, data):
        data = np.array(data)
        ds_img = ds.NumpySlicesDataset({"image": data[np.newaxis, :]})
        ds_img = ds_img.map(input_columns="image", operations=self.transform_img)
        ds_img = ds_img.batch(1)
        # data = data[np.newaxis, :]
        # print(data.shape)
        result = 5.0  

        pred = []
        for batch in ds_img.create_dict_iterator():
            X = batch["image"]
            # print(X.shape)
            y_pred = self.model.predict(X)
            # print(y_pred.shape)
            pred.append(y_pred.asnumpy().flatten())
        
        result = pred[0][0]
        return result


"""Alexnet."""
import mindspore.nn as nn


def conv(in_channels, out_channels, kernel_size, stride=1, padding=0, pad_mode="valid", group=1, has_bias=True):
    return nn.Conv2d(in_channels, out_channels, kernel_size=kernel_size, stride=stride, padding=padding,
                     group=group, has_bias=has_bias, pad_mode=pad_mode)


def bn_relu(inplanes):
    return nn.SequentialCell(nn.BatchNorm2d(inplanes), nn.ReLU())


def bn_relu_pool(inplanes, kernel_size=3, stride=2):
    return nn.SequentialCell(nn.BatchNorm2d(inplanes), nn.ReLU(), nn.MaxPool2d(kernel_size=kernel_size, stride=stride, pad_mode='valid'))


class AlexNet(nn.Cell):
    """
    Alexnet
    """

    def __init__(self, num_classes=10, channel=3, phase='train', include_top=True):
        super(AlexNet, self).__init__()

        self.conv1 = conv(channel, 96, 11, stride=4,
                          has_bias=False)
        self.relu_pool1 = bn_relu_pool(inplanes=96)
        self.conv2 = conv(96, 192, 5, pad_mode="pad", padding=2, group=2, has_bias=False)
        self.relu_pool2 = bn_relu_pool(inplanes=192)
        self.conv3 = conv(192, 384, 3, pad_mode="pad", padding=1, group=2, has_bias=False)
        self.relu3 = bn_relu(inplanes=384)
        self.conv4 = conv(384, 384, 3, pad_mode="pad", padding=1, group=2, has_bias=False)
        self.relu4 = bn_relu(inplanes=384)
        self.conv5 = conv(384, 256, 3, pad_mode="pad", padding=1, group=2, has_bias=False)
        self.relu_pool5 = bn_relu_pool(inplanes=256)

        # classifier
        self.conv6 = conv(256, 256, 5,  group=2, has_bias=False)
        self.relu6 = bn_relu(inplanes=256)
        self.conv7 = conv(256, num_classes, 1, has_bias=False)
        self.flatten = nn.Flatten()

    def construct(self, x):
        """define network"""
        x = self.conv1(x)
        x = self.relu_pool1(x)
        x = self.conv2(x)
        x = self.relu_pool2(x)
        x = self.conv3(x)
        x = self.relu3(x)
        x = self.conv4(x)
        x = self.relu4(x)
        x = self.conv5(x)
        x = self.relu_pool5(x)
        x = self.conv6(x)
        x = self.relu6(x)
        x = self.conv7(x)
        x = self.flatten(x)
        return x
