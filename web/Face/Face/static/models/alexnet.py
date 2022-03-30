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
